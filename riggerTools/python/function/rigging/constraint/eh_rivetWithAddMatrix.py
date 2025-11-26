
'''
from function.rigging.constraint import eh_rivetWithAddMatrix as rwm
reload(rwm)
'''
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

from function.rigging.autoRig.base import core
reload(core)

import maya.cmds as mc

from function.pipeline import logger
reload(logger)

import maya.OpenMaya as om

from function.rigging.util import misc
reload(misc)

class riveAddMatrixLog(logger.MayaLogger):
	LOGGER_NAME = "EHrivetWithAddMatrix"

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





def rivetMatrixWeight(data_list):
	"""
	Create a matrix-based rivet constraint (wtAddMatrix) using explicit weight arguments.
	
	Fixed: Uses OrientConstraint for rotation to avoid matrix linear interpolation artifacts.
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

		# --- 1. Create Main Calculation Nodes (For Translation) ---
		
		# 1.1 Weighted Add Matrix Node
		wt_add_node = core.WtAddMatrix(target_rivet_name)
		
		# 1.2 Invert Parent Matrix Node (To handle local space of the target)
		invert_node_name = '{}_invertParent_mulMtx'.format(target_rivet_name)
		invert_mul_mtx = core.MultMatrix(invert_node_name)
		
		# 1.3 Decompose Matrix (To drive Translate ONLY)
		decompose_node = core.DecomposeMatrix(target_rivet_name)
		
		# 1.4 Meta Node for storing/adjusting weights
		meta_name = '{}_weight_meta'.format(target_rivet_name)
		meta_node = core.MetaBlank(meta_name)
		
		
		# --- 2. Loop through Drivers (Joints) to setup Matrix Chain ---
		
		# Get Target World Matrix for Offset Calculation
		target_m_obj = get_matrix(target)
		
		# Helper lists for Orient Constraint
		driver_list = []
		weight_list = []

		for i, (driver, weight_val) in enumerate(weight_data):
			
			if not mc.objExists(driver):
				mc.error('Driver not found: {}'.format(driver))
			
			driver_base = core.findBaseName(driver)
			
			# Collect drivers for OrientConstraint later
			driver_list.append(driver)
			weight_list.append(weight_val)

			# --- 2.1 Create Weight Attribute on Meta Node ---
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
			mc.connectAttr('{}.matrixSum'.format(calc_node), '{}.wtMatrix[{}].matrixIn'.format(wt_add_node.name, i))
			
			# Connect Weight from Meta Node (Driving Matrix Weight)
			mc.connectAttr('{}.{}'.format(meta_node.name, attr_name), '{}.wtMatrix[{}].weightIn'.format(wt_add_node.name, i))


		# --- 3. Final Connections to Target (Translation) ---
		
		# 3.1 Connect WtAddMatrix -> Invert Parent MultMatrix
		wt_add_node.attr('matrixSum') >> invert_mul_mtx.attr('matrixIn[0]')
		
		# 3.2 Connect Target's Parent Inverse Matrix -> Input[1]
		mc.connectAttr('{}.parentInverseMatrix[0]'.format(target), '{}.matrixIn[1]'.format(invert_mul_mtx.name))
		
		# 3.3 Connect Result -> Decompose
		invert_mul_mtx.attr('matrixSum') >> decompose_node.attr('inputMatrix')
		
		# 3.4 Drive the Target (TRANSLATE ONLY)
		# We DO NOT connect Rotate here because Matrix blending ruins rotation
		decompose_node.attr('outputTranslate') >> item['target'] + '.translate'
		# Optional: Scale can be driven by matrix if needed
		# decompose_node.attr('outputScale') >> item['target'] + '.scale'
		
		
		# --- 4. Handle Rotation with Orient Constraint ---
		# Orient Constraint handles spherical interpolation (SLERP) correctly
		
		# 4.1 Create Orient Constraint
		# maintainOffset=True is important to keep the initial offset relative to drivers
		try:
			ori_cons = mc.orientConstraint(driver_list, target, mo=True, name=target_rivet_name + '_oriCons')[0]
		except Exception as e:
			mc.warning(f"Orient constraint failed for {target}. Ensure pivots match or try without offset. Error: {e}")
			continue

		# 4.2 Connect Meta Weights to Constraint Weights
		# We reuse the same meta attributes so one slider drives both Position (Matrix) and Rotation (Constraint)
		constraint_attrs = mc.orientConstraint(ori_cons, query=True, weightAliasList=True)

		
		for i, (driver, weight_val) in enumerate(weight_data):
			driver_base = core.findBaseName(driver)
			attr_name = '{}_{}_w'.format(driver_base, i) # Same attr name as above
			
			# Connect Meta -> Constraint Weight
			# Ensure index matches the constraint alias list order
			if i < len(constraint_attrs):
				mc.connectAttr('{}.{}'.format(meta_node.name, attr_name), '{}.{}'.format(ori_cons, constraint_attrs[i]))

		riveAddMatrixLog.info('   > Rivet created successfully for {}'.format(target))

	riveAddMatrixLog.info('# All rivets processed.')