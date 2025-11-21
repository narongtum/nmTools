#... using wtAddMatrix for make something like rivet
#... this is latest file
#... move to constraint module 

# D:\sysTools\nmTools_github\riggerTools\python\function\rigging\constraint




'''
from function.rigging.constraint import rivetWithAddMatrix as rwm
reload(rwm)

rwm.rivetMatrix( 	skinCluster = 'SK_DM011_skc', 
					vtx = 'SK_DM011.vtx[1507]'	, 
					target = 'spineHi27_bJnt'	, 
					thresholdValue = 0.001)

'''




import maya.OpenMaya as om

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)

import maya.cmds as mc

# # # # # # # # 
# Gether argument
# # # # # # # # 


'''
from function.rigging.constraint import rivetWithAddMatrix as rwm
reload(rwm)

# Define your data
targetWeights = [
	{
		'target': 'spineBtw01_loc',
		'weight': [('lower_jnt', 0.666), ('upper_jnt', 0.334)]
	},
	{
		'target': 'spineBtw02_loc',
		'weight': [('lower_jnt', 0.334), ('upper_jnt', 0.666)]
	}
]



# Run the function
rwm.rivetMatrixWeight(data_list=targetWeights)
'''






from function.pipeline import logger
reload(logger)

class riveAddMatrixLog(logger.MayaLogger):
	LOGGER_NAME = "rivetWithAddMatrix"

# ------------------------------------------------------------------------------
# Helper Functions for Matrix Calculation
# ------------------------------------------------------------------------------
def get_dag_path(node_name):
	"""Returns MDagPath from node name."""
	sel = om.MSelectionList()
	sel.add(node_name)
	dag_path = om.MDagPath()
	sel.getDagPath(0, dag_path)
	return dag_path

def get_matrix(node_name):
	"""Returns inclusive matrix of a node."""
	return get_dag_path(node_name).inclusiveMatrix()

# ------------------------------------------------------------------------------
# Main Function
# ------------------------------------------------------------------------------

def rivetMatrixWeight(data_list):
	"""
	Create a matrix-based rivet constraint (wtAddMatrix) using explicit weight arguments.
	
	Args:
		data_list (list): A list of dictionaries containing target and weight info.
		
		Format:
		[
			{
				'target': 'object_name',
				'weight': [('driver_A', 0.666), ('driver_B', 0.334)]
			},
			...
		]
	"""

	for item in data_list:
		target = item['target']
		weight_data = item['weight']
		
		# Check if target exists
		if not mc.objExists(target):
			mc.warning('Target not found: {}'.format(target))
			continue
			
		base_name = core.findBaseName(target)
		target_rivet_name = base_name + '_Rivet'
		
		print('\n# Processing Rivet: {}'.format(target))

		# --- 1. Create Main Calculation Nodes ---
		
		# 1.1 Weighted Add Matrix Node
		wt_add_node = core.WtAddMatrix(target_rivet_name)
		
		# 1.2 Invert Parent Matrix Node (To handle local space of the target)
		# This ensures the target stays in place relative to its parent
		invert_node_name = '{}_invertParent_mulMtx'.format(target_rivet_name)
		invert_mul_mtx = core.MultMatrix(invert_node_name)
		
		# 1.3 Decompose Matrix (To drive Translate/Rotate/Scale)
		decompose_node = core.DecomposeMatrix(target_rivet_name)
		
		# 1.4 Meta Node for storing/adjusting weights (User Friendly)
		meta_name = '{}_weight_meta'.format(target_rivet_name)
		meta_node = core.MetaBlank(meta_name)
		
		
		# --- 2. Loop through Drivers (Joints) to setup Matrix Chain ---
		
		# Get Target World Matrix for Offset Calculation
		target_m_obj = get_matrix(target)
		
		for i, (driver, weight_val) in enumerate(weight_data):
			
			if not mc.objExists(driver):
				mc.error('Driver not found: {}'.format(driver))
			
			driver_base = core.findBaseName(driver)
			
			# --- 2.1 Create Weight Attribute on Meta Node ---
			# This allows animators/riggers to slide weights later
			attr_name = '{}_{}_w'.format(driver_base, i)
			meta_node.addAttribute(longName=attr_name, dv=weight_val, min=0.0, max=1.0)
			
			# --- 2.2 Calculate Offset Matrix ---
			# Offset = TargetWorld * DriverWorldInverse
			driver_m_obj = get_matrix(driver)
			driver_m_inv = driver_m_obj.inverse()
			
			offset_matrix = target_m_obj * driver_m_inv
			
			# Convert to list for setAttr
			offset_val = [offset_matrix(r, c) for r in range(4) for c in range(4)]
			
			# --- 2.3 Create Matrix Network for this Driver ---
			
			# Node A: Offset Holder (Static)
			# We create a multMatrix just to hold the static offset value in input[0]
			offset_node_name = '{}_{}_offset_mulMtx'.format(target_rivet_name, driver_base)
			offset_node = mc.createNode('multMatrix', name=offset_node_name)
			mc.setAttr('{}.matrixIn[0]'.format(offset_node), offset_val, type='matrix')
			
			# Node B: Runtime Calculation (Offset * CurrentDriver)
			calc_node_name = '{}_{}_calc_mulMtx'.format(target_rivet_name, driver_base)
			calc_node = mc.createNode('multMatrix', name=calc_node_name)
			
			# Connect Static Offset -> Calc Node
			mc.connectAttr('{}.matrixSum'.format(offset_node), '{}.matrixIn[0]'.format(calc_node))
			
			# Connect Real Driver World Matrix -> Calc Node
			mc.connectAttr('{}.worldMatrix[0]'.format(driver), '{}.matrixIn[1]'.format(calc_node))
			
			# --- 2.4 Connect to Weighted Add Matrix ---
			# Connect Matrix Result
			mc.connectAttr('{}.matrixSum'.format(calc_node), '{}.wtMatrix[{}].matrixIn'.format(wt_add_node.name, i))
			
			# Connect Weight from Meta Node
			mc.connectAttr('{}.{}'.format(meta_node.name, attr_name), '{}.wtMatrix[{}].weightIn'.format(wt_add_node.name, i))


		# --- 3. Final Connections to Target ---
		
		# 3.1 Connect WtAddMatrix -> Invert Parent MultMatrix
		# wtAddMatrix result goes to Input[0]
		wt_add_node.attr('matrixSum') >> invert_mul_mtx.attr('matrixIn[0]')
		
		# 3.2 Connect Target's Parent Inverse Matrix -> Input[1]
		# This neutralizes the parent's transform, giving us correct local values
		mc.connectAttr('{}.parentInverseMatrix[0]'.format(target), '{}.matrixIn[1]'.format(invert_mul_mtx.name))
		
		# 3.3 Connect Result -> Decompose
		invert_mul_mtx.attr('matrixSum') >> decompose_node.attr('inputMatrix')
		
		# 3.4 Drive the Target
		# We drive Translate and Rotate. Scale is optional depending on needs (added here for completeness)
		decompose_node.attr('outputTranslate') >> item['target'] + '.translate'
		decompose_node.attr('outputRotate') >> item['target'] + '.rotate'
		decompose_node.attr('outputScale') >> item['target'] + '.scale'
		
		riveAddMatrixLog.info('   > Rivet created successfully for {}'.format(target))

	riveAddMatrixLog.info('# All rivets processed.')










#... give skin cluster and vtx number

def rivetMatrix( 	skinCluster = 'SK_DM011_skc', 
					vtx = 'SK_DM011.vtx[1507]'	, 
					target = 'spineHi27_bJnt'	, 
					thresholdValue = 0.001):




	#.... name for main function
	base = misc.check_name_style(target)[0]
	targetName = base + 'Rivet'




	# # # # # # # # # # # # # # # # # # # # # # # # 
	# find vtx influence joint and weight value
	# # # # # # # # # # # # # # # # # # # # # # # # 

	#... find joint weight
	# influenceVals   = mc.skinPercent(skinCluster, vtx, q=True, v = True, ib = thresholdValue )
	influenceJoint  = mc.skinPercent(skinCluster, vtx, q=True, t=None)
	influenceData   = mc.skinPercent(skinCluster, vtx, q=True, v=True)


	# Initialize an empty dictionary to store joint and influence value pairs
	joint_influence_dict = {}


	#... Print the list of joints and their corresponding influence values
	for joint, value in zip(influenceJoint, influenceData):
		if value != 0:
			print("Joint:", joint, "Influence Value:", value)
			joint_influence_dict[joint] = value
		else:
			pass




	#.... Assign influence joint 
	print( joint_influence_dict.keys() )
	influence_obj = list(joint_influence_dict.keys())



	#.... Next Create MetaNode for store weight
	from function.rigging.autoRig.base import core
	reload(core)

	#... Store value to meta
	meta = core.MetaBlank(targetName)
	joint_influence_dict

	for index, (key, value) in enumerate(joint_influence_dict.items()):
		print(key)
		print(value)
		#rIndex = index + 1
		#meta.addAttribute(longName = '{0}_{1}'.format(key,rIndex), dv = value)
		meta.addAttribute(longName = '{0}'.format(key), dv = value)




	# # # # # # # # 
	# Find offset vector
	# # # # # # # # 

	#... Useful function
	def getDagPath(node=None):
		sel = om.MSelectionList()
		sel.add(node)
		dagPath = om.MDagPath()
		sel.getDagPath(0, dagPath)
		return dagPath

	def getLocalOffset(parent, child):
		
		parentWorldMatrix = getDagPath(parent).inclusiveMatrix()
		childWorldMatrix = getDagPath(child).inclusiveMatrix()
		# child World Matrix * invert parent World Matrix = child local matrix
		# return child local matrix
		return childWorldMatrix * parentWorldMatrix.inverse()




	for each in influence_obj:

		#... find base name
		influ_jnt = core.findBaseName(each)
		

		#... Create offset mult matrix

		#... CreateNode
		mulMtx = '{0}_{1}_offset_mulMtx'.format(targetName, influ_jnt) #... duplicate name if we run this script again
		mc.createNode( 'multMatrix', n = mulMtx )


		#... get world matrix to [0]
		parentWorldMatrix = getDagPath(target).inclusiveMatrix()
		parentWorldMatrix_val = [parentWorldMatrix(i,j) for i in range(4) for j in range(4)]
		mc.setAttr( mulMtx + '.matrixIn[0]', parentWorldMatrix_val , type = 'matrix')


		#... get world matrix to [1]
		invert_Matrix = getDagPath(each).inclusiveMatrix()
		invert_Matrix_val = [invert_Matrix.inverse()(i,j) for i in range(4) for j in range(4)]
		mc.setAttr( mulMtx + '.matrixIn[1]', invert_Matrix_val , type = 'matrix')


		#... Next create XFORM for collect value 
		xform_mulMtx = mc.createNode( 'multMatrix', name = '{0}_{1}_xform_mulMtx'.format(targetName, influ_jnt))
		mc.connectAttr('{0}.matrixSum'.format(mulMtx),'{0}.matrixIn[0]'.format(xform_mulMtx))
		mc.connectAttr('{0}.worldMatrix[0]'.format(each),'{0}.matrixIn[1]'.format(xform_mulMtx))








	# # # # # # # # 
	# wtAddMatrix
	# # # # # # # # 



	#... Create wtAddMatrix
	weight_matrix = core.WtAddMatrix(targetName)




	#...Create Invert space for make it static
	#... CreateNode
	invert_name = '{0}_invert'.format(targetName)
	invert_mulMtx = core.MultMatrix(invert_name)

	#mc.createNode( 'multMatrix', name = invert_mulMtx )




	mc.connectAttr('{0}.matrixSum'.format(weight_matrix),'{0}.matrixIn[0]'.format(invert_mulMtx.name))
	decompost = core.DecomposeMatrix('{0}'.format(targetName))
	invert_mulMtx.attr('matrixSum') >> decompost.attr('inputMatrix')




	#... create null grp
	offset_grp = '{0}_offsetGrp'.format(targetName)
	# offset_grp = core.Null(offset_grp)


	#... create locator instead
	offset_grp = core.Locator(offset_grp, lock = True)

	#... optional
	# invert_mulMtx.attr('matrixSum') >> offset_grp.attr('offsetParentMatrix')









	#... Assign value from meta to weight node
	#... For each index and key-value pair in the dictionary
	for num, (key, value) in enumerate(joint_influence_dict.items()):
		print(f"Index: {num}, Key: {key}, Value: {value}")
		
		baseName = core.findBaseName(key)
	 
		mc.connectAttr('{0}_{1}_xform_mulMtx.matrixSum'.format(targetName, baseName), '{0}.wtMatrix[{1}].matrixIn'.format(weight_matrix,num))
		mc.connectAttr('{0}.{1}'.format(meta.name,key), '{0}.wtMatrix[{1}].weightIn'.format(weight_matrix,num))
		
		#mc.setAttr('{0}.wtMatrix[0].matrixIn'.format(weight_matrix)





	#... connect to offset grp
	decompost.attr('outputTranslate') >> offset_grp.attr('translate')
	decompost.attr('outputRotate') >> offset_grp.attr('rotate')
	decompost.attr('outputScale') >> offset_grp.attr('scale')




	#.... parent invert to mult matrix just in case
	offset_grp.attr('parentInverseMatrix[0]') >> invert_mulMtx.attr('matrixIn[1]')


	print('\t\t\trivetWithAddMatrix Done...')


	#... TODO
	# merge matrix * invert parent matrix in one node