# ========== # 
# move from rigging.misc
# ========== #

'''

from function.rigging.constraint import normalConstraint as nmCon
reload(nmCon)

'''

import maya.cmds as mc

from function.rigging.util import misc

from function.framework.reloadWrapper import reloadWrapper as reload
reload(misc)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)



def constraint_pair(pairs, maintainOffset=False):
	"""
	Create parentConstraint and scaleConstraint for multiple parent-child pairs.

	Args:
		*pairs: Variable length argument list of tuples (parent, child).
		maintainOffset (bool): Keep offset if True.
	"""
	for parent, child in pairs:
		print(f'parent {parent} with {child}')
		# Create parentConstraint
		mc.parentConstraint(parent, child, maintainOffset=maintainOffset,
							name=f'{parent}_psCon')
		# Create scaleConstraint
		mc.scaleConstraint(parent, child, maintainOffset=maintainOffset,
						   name=f'{parent}_scCon')








def snapPointCon():
	sel = mc.ls(sl = True)
	src = sel[0]
	tgt = sel[1]
	mc.matchTransform( tgt , src, position = True, rotation = False, scale = False )



def snapOrientCon():
	sel = mc.ls(sl = True)
	src = sel[0]
	tgt = sel[1]
	mc.matchTransform( tgt , src, position = False, rotation = True, scale = False )

def snapScaleCon():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]
	mc.delete(mc.parentConstraint(src,tgt, mo = False))
	mc.delete(mc.scaleConstraint(src,tgt, mo = False))

# snap for key frame object	
def snapMat():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]

	srcMatrix = mc.xform( src, query=True, worldSpace=True, matrix=True )
	mc.xform( tgt, worldSpace=True, matrix = srcMatrix )


def snapMatArg( source , target ):
	srcMatrix = mc.xform( source, query = True , worldSpace = True , matrix = True )
	mc.xform( target, worldSpace = True, matrix = srcMatrix )








#####################################################
#      remain  constraint  snapParentCon snapScaleCon                      
#####################################################
def normalParentConstr( source, target , **kwargs ):
	mc.parentConstraint( source ,target  ) 
def normalScaleConstr( source, target , **kwargs ):
	mc.scaleConstraint( source ,target )	
def normalPointConstr( source, target , **kwargs  ):
	mc.pointConstraint( source ,target )	
def orientConstr( source, target , **kwargs  ):
	mc.pointConstraint( source ,target )	









def check_obj_exists(obj_name):
	if not mc.objExists(obj_name):
		raise ValueError(f"Object '{obj_name}' does not exist.")
		return False
	else:
		return True









def constraintSuffix( child = 'bJnt', parent = 'pxyJnt' ):
	nodeDict = mnd.NODE_short_dict
	psC_suffix = nodeDict.get('parentConstraint', 'Unknown')
	scC_suffix = nodeDict.get('scaleConstraint', 'Unknown')
	naming = '*_' + parent
	proxyList = mc.ls( naming )
	
	for each in proxyList:
		if check_obj_exists(each):
			baseName = core.check_name_style(each)[0]
			childNam = baseName + '_' + child
			mc.parentConstraint( each , childNam, maintainOffset = True, name = f'{baseName}_{psC_suffix}')
			mc.scaleConstraint( each , childNam, maintainOffset = True, name = f'{baseName}_{scC_suffix}')
		else:
			pass
		print('DONE')





#... this method work because it use parent local/world group under parent object 

def parent_localWorld_ext(zro_grp='L_skirt_L03_A01Zro_grp',  # Zero out group
						ctrl='L_skirt_L03_A01_ctrl',
						local_obj='upperLegLFT_bJnt',  # Parent object to assign in local space
						world_obj='ctrl_grp',  # Parent object to assign in world space
						base_grp='L_skirt_L03_A01Offset_grp',  # Offset group
						body_part='L_skirt_L03_A01',
						attr_occur='L_skirt_L03_A01Curl_ctrlShape'):

	# Check if all necessary objects exist
	try:
		check_obj_exists(zro_grp)
		check_obj_exists(local_obj)
		check_obj_exists(world_obj)
		check_obj_exists(base_grp)
		check_obj_exists(attr_occur)
	except ValueError as e:
		print(e)
		raise SystemExit(f"Error: {e}")

	try:
		# Create a null group under zero group
		local_world_grp = core.Null(body_part + 'LocalWorld_grp')
		local_world_grp.snap(base_grp)
		local_world_grp.parent(zro_grp)

		# Parent control under it
		base_grp = core.Dag(base_grp)
		base_grp.parent(local_world_grp)

		# Create and snap local and world groups
		loc_grp = core.Null()
		wor_grp = core.Null()
		loc_grp.snap(base_grp)
		wor_grp.snap(base_grp)

		# Assign names to local and world groups
		if body_part:
			loc_grp.name = body_part + '_local_grp'
			wor_grp.name = body_part + '_world_grp'
		else:
			loc_grp.name = 'local'
			wor_grp.name = 'world'

		# Orient constraints
		world_grp_cons = core.orientConstraint(world_obj, wor_grp, mo=True)
		world_grp_cons.name = body_part + 'World'
		world_grp_cons.suffix

		base_grp_base_cons = core.orientConstraint(loc_grp, wor_grp, local_world_grp)
		base_grp_base_cons.name = body_part + 'Base'
		base_grp_base_cons.suffix

		reverse_node_rev = core.Reverse()
		reverse_node_rev.name = body_part + '_rev'

		# Set up attributes for switching between local and world space
		controller_shape = core.Dag(attr_occur)
		attr = 'localWorld'
		controller_shape.addAttribute(ln=attr, k=True, min=0, max=1)

		# Connect attributes
		controller_shape.attr(attr) >> base_grp_base_cons.attr('w1')
		controller_shape.attr(attr) >> reverse_node_rev.attr('ix')
		reverse_node_rev.attr('ox') >> base_grp_base_cons.attr('w0')

		# Parent local and world groups
		loc_grp.parent(local_obj)
		wor_grp.parent(local_obj)

		# Clear selection and indicate completion
		core.clearSel()
		print('\n# # # DONE')

		# Optional: Return the created objects if needed
		# return loc_grp, wor_grp, world_grp_cons, base_grp_base_cons, reverse_node_rev

	except Exception as e:
		print(f"An error occurred: {e}")
		raise






def parent_localWorld(	zro_grp='L_pinStrap02_Zro_grp',  # Zero out group
						ctrl='L_pinStrap02_ctrl',
						local_obj='L_pinStrap02_gmblCtrl',  # Parent object to assign in local space
						world_obj='ctrl_grp',  # Parent object to assign in world space
						base_grp='L_pinStrap02Offset_grp',  # Offset group
						body_part='L_pinStrap02',
						attr_occur='L_pinStrap02_ctrlShape',
						noTouch = 'noTouch_grp'):  # Attribute occurrence object
	
	def check_obj_exists(obj_name):
		"""Check if an object exists in the Maya scene."""
		if not mc.objExists(obj_name):
			raise ValueError(f"Object '{obj_name}' does not exist.")

	# Check if all necessary objects exist
	try:
		check_obj_exists(zro_grp)
		check_obj_exists(local_obj)
		check_obj_exists(world_obj)
		check_obj_exists(base_grp)
		check_obj_exists(attr_occur)
	except ValueError as e:
		print(e)
		mc.error(e)
	
	try:
		# Create a null group under zero group
		local_world_grp = core.Null(body_part + '_localWorld_grp')
		local_world_grp.snap(base_grp)
		local_world_grp.parent(zro_grp)

		# Parent control under it
		base_grp_dag = core.Dag(base_grp)  # Assign core.Dag instance for base group
		base_grp_dag.parent(local_world_grp)

		# Create and snap local and world groups under zero group
		loc_grp = core.Null(body_part + '_local_grp')
		locZro_grp = core.Null(body_part + '_localZro_grp')
		wor_grp = core.Null(body_part + '_world_grp')
		loc_grp.snap(base_grp_dag)
		locZro_grp.snap(base_grp_dag)
		wor_grp.snap(base_grp)
		
		# Parent local and world groups correctly
		locZro_grp.parent(local_obj)
		loc_grp.parent(locZro_grp)
		# wor_grp.parent(world_obj)  #... Fixed potential cycle issue
		wor_grp.parent(noTouch)#... parent here
		

		# Create and apply constraints
		world_grp_cons = core.orientConstraint(world_obj, wor_grp, mo=True)
		world_grp_cons.name = body_part + '_WorldCons'
		
		base_grp_base_cons = core.orientConstraint(loc_grp, wor_grp, local_world_grp, mo=True)
		base_grp_base_cons.name = body_part + '_BaseCons'
		
		reverse_node_rev = core.Reverse()
		reverse_node_rev.name = body_part + '_rev'
		
		# Set up attributes for switching
		controller_shape = core.Dag(attr_occur)
		attr = 'localWorld'
		# controller_shape.addAttribute(attr, at='double', min=0, max=1, k=True)
		controller_shape.addAttribute(ln=attr, k=True, min=0, max=1)

		#... Connect attributes
		controller_shape.attr(attr) >> base_grp_base_cons.attr('w1')
		controller_shape.attr(attr) >> reverse_node_rev.attr('inputX')
		reverse_node_rev.attr('outputX') >> base_grp_base_cons.attr('w0')

		# reverse_node_rev.attr('outputX') >> world_grp_cons.attr('w1')




		# Clear selection
		core.clearSel()
		print(f'\n# # # DONE: {body_part}')
		
		return loc_grp, wor_grp, world_grp_cons, base_grp_base_cons, reverse_node_rev

	except Exception as e:
		print(f"An error occurred: {e}")
		raise




#
# newer local world function 
#

def parent_localWorld_backup(	zro_grp = 'L_pinStrap02Zro_grp',  # Zero out group
						ctrl = 'L_pinStrap02_ctrl',
						local_obj = 'L_pinStrap02_gmblCtrl',  # Parent object to assign in local space):
						world_obj = 'ctrl_grp',  # Parent object to assign in world space
						base_grp = 'L_pinStrap02Offset_grp',  # Offset group
						body_part = 'L_pinStrap02',
						attr_occur = 'L_pinStrap02_ctrlShape'):	 # attr occur at	
	
	

	# # Function to check if an object exists
	# def check_obj_exists(obj_name):
	# 	if not mc.objExists(obj_name):
	# 		raise ValueError(f"Object '{obj_name}' does not exist.")

	# Check if all necessary objects exist
	try:
		check_obj_exists(zro_grp)
		check_obj_exists(local_obj)
		check_obj_exists(world_obj)
		check_obj_exists(base_grp)
		check_obj_exists(attr_occur)
	except ValueError as e:
		print(e)
		raise SystemExit(f"Error: {e}")

	try:
		# Create a null group under zero group
		local_world_grp = core.Null(body_part + 'LocalWorld_grp')
		local_world_grp.snap(base_grp)
		local_world_grp.parent(zro_grp)

		# Parent control under it
		base_grp = core.Dag(base_grp)
		base_grp.parent(local_world_grp)

		# Create and snap local and world groups
		loc_grp = core.Null()
		wor_grp = core.Null()
		loc_grp.snap(base_grp)
		wor_grp.snap(base_grp)

		# Assign names to local and world groups
		if body_part:
			loc_grp.name = body_part + '_local'
			wor_grp.name = body_part + '_world'
		else:
			loc_grp.name = 'local'
			wor_grp.name = 'world'

		# Orient constraints
		world_grp_cons = core.orientConstraint(world_obj, wor_grp, mo=True)
		base_grp_base_cons = core.orientConstraint(loc_grp, wor_grp, local_world_grp)
		reverse_node_rev = core.Reverse()
		reverse_node_rev.name = body_part + '_rev'

		# Set up attributes for switching between local and world space
		controller_shape = core.Dag(attr_occur)
		attr = 'localWorld'
		controller_shape.addAttribute(ln=attr, k=True, min=0, max=1)

		# Connect attributes
		controller_shape.attr(attr) >> base_grp_base_cons.attr('w1')
		controller_shape.attr(attr) >> reverse_node_rev.attr('ix')
		reverse_node_rev.attr('ox') >> base_grp_base_cons.attr('w0')

		# Parent local and world groups
		loc_grp.parent(local_obj)
		wor_grp.parent(local_obj)

		# Clear selection and indicate completion
		core.clearSel()
		print('\n# # # DONE')

		# Optional: Return the created objects if needed
		# return loc_grp, wor_grp, world_grp_cons, base_grp_base_cons, reverse_node_rev

	except Exception as e:
		print(f"An error occurred: {e}")
		raise













####################################################
#      constraint pair between proxy joint and bind joint old(naming)               
#####################################################
def constraintProxyJnt( child = 'bJnt', parent = 'pxyJnt' ):
	naming = '*_' + parent
	proxyList = mc.ls( naming )
	
	for each in proxyList:
		# spEach = each.split('_')
		baseName = misc.check_name_style(each)[0]
		childNam = baseName + '_' + child
		mc.parentConstraint( each , childNam , maintainOffset = True)
		mc.scaleConstraint( each , childNam , maintainOffset = True)
	print('DONE')













#####################################################
#      multiple constraint new condition           
#####################################################
def multipleCon( child = '*_bJnt', parent = '*Gmbl_ctrl' ):
	naming = '*_' + parent
	proxyList = mc.ls( naming )
	
	for each in proxyList:
		if check_obj_exists(each):
			spEach = each.split('_')
			childNam = spEach[0] + '_' + child
			mc.parentConstraint( each , childNam , maintainOffset = True)
			mc.scaleConstraint( each , childNam , maintainOffset = True)
		else:
			print('Object not found skipt.')


	print('DONE')





# ... constraint parent suffix name to bind suffix name

def constraintListJnt( namJntList = [] , child = 'ikJnt', parent = 'bJnt' ):
	namLst = []
	for each in namJntList:
		fitstNam = misc.check_name_style(each)[0]
		namLst.append( fitstNam )

	
	for each in namLst:
		parentNam = each + '_' + parent
		childNam = each + '_' + child
		mc.parentConstraint( parentNam , childNam , maintainOffset = True , name = parentNam + '_psCon')
		mc.scaleConstraint( parentNam , childNam , maintainOffset = True , name = parentNam + '_scCon')

		print ('%s object has been create.' %each)








