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





def check_obj_exists(obj_name):
	if not mc.objExists(obj_name):
		raise ValueError(f"Object '{obj_name}' does not exist.")
		return False
	else:
		return True







#
# newer local world function 
#

def parent_localWorld(	zro_grp = 'L_pinStrap02Zro_grp',  # Zero out group
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