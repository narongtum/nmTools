'''
from function.rigging.skeleton import jointTools as jtt
reload(jtt)
'''

from function.framework.reloadWrapper import reloadWrapper as reloader

from function.rigging.autoRig.base import core
reloader(core)

from function.rigging.autoRig.base import rigTools
reloader( rigTools )

from function.pipeline import logger 
reloader(logger)

class utilLogger(logger.MayaLogger):
	LOGGER_NAME = "JointTools"

import maya.cmds as mc
import pymel.core as pm





from function.rigging.util import misc
reloader(misc)



def rename_tip_jnt(root_joint = 'R_wing01_tmpJnt', search = '_tmpJnt', replace = '_tipJnt'):
	list_tip_joint_grp = list_tip_joints(root_joint)
	misc.searchReplace( searchText=search, replaceText=replace )

	








def mirror_joint_chain(root_joint = 'R_wing01_tmpJnt'):
	root_obj = pm.PyNode(root_joint)

	# Retrieve the joint chain
	joint_chain = pm.listRelatives(root_joint, allDescendents=True, type='joint')

	# Store original parent connections for later re-parenting
	original_parents = {}
	for joint in joint_chain:
	   original_parents[joint] = joint.getParent()

	# Unparent all joints to world
	pm.parent(joint_chain, world=True)

	# Set Y rotation to 180 for each joint
	for joint in joint_chain:
	   joint.rotateY.set(180)
	   
	root_obj.rotateY.set(180)

	# Re-parent joints back to their original parents
	for joint, parent in original_parents.items():
	   pm.parent(joint, parent)

	# Freeze at last
	pm.makeIdentity(root_obj, apply=True)

	mc.select(deselect=True)
	utilLogger.info('End of the {0}.'.format(__name__))






def list_tip_joints(root_joint):
	if root_joint == None:
		print("Please select one root joint")
		return False
	else:
		# Get the children of the root joint
		children = mc.listRelatives(root_joint, children=True)

		# Recursively list the tip joints of the children
		tip_joints = []
		for child in children:
			# Check if the child is a joint
			if mc.nodeType(child) == 'joint':
				# If the child has no children, it is a tip joint
				if not mc.listRelatives(child, children=True):
					tip_joints.append(child)
				# Otherwise, recursively list the tip joints of the child
				else:
					tip_joints.extend(list_tip_joints(child))
					
		print('This is tip joint >>> {}'.format(tip_joints))
		mc.select(tip_joints, r=True)
		return tip_joints
	
	
def list_joint_hierarchy(root_joint):
	joint_hierarchy = []
	
	if not mc.objExists(root_joint) or mc.objectType(root_joint) != "joint":
		mc.warning("Root joint '{0}' does not exist or is not a joint.".format(root_joint))
		return joint_hierarchy
	
	joint_hierarchy.append(root_joint)
	
	child_joints = mc.listRelatives(root_joint, type="joint", ad=True) or []
	for child_joint in child_joints:
		joint_hierarchy.append(child_joint)
	
	return joint_hierarchy




#... Example usage:
# aac = jtt.list_tip_joints('skirt_rtJnt')
# aab = jtt.list_joint_hierarchy('skirt_rtJnt')






def replaceTmpJnt(			nameSpace = '',
							tmpJnt = (	'tail01_tmpJnt' ,
										'tail02_tmpJnt' ,
										'tail03_tmpJnt' ,
										'tail04_tmpJnt'	)		,
							side = ''							,
							extName = 'bJnt'):

	""" Replace template joint with new ext name

	Args:
		nameSpace: name space if have.
		tmpJnt: The first parameter.
		side: side
		extName = name of last name

	Returns:
		List of the new joint

	"""

	# make raw name
	rawName = []
	for each in tmpJnt:
		if side:
			tmp = each.split('_')[0][:-3]
		else:
			tmp = each.split('_')[0]
		rawName.append(tmp)


	bJnts_list = []

	for num in range(0,len(tmpJnt)):
		tmp = core.Dag( tmpJnt[num] )
		bJnt = rigTools.jointAt( tmp )

		bJnt.name = "{0}{1}{2}_{3}".format(nameSpace,rawName[num],side,extName )
		# bJnt.name = nameSpace + rawName[num] + side + '_' + extName

		bJnts_list.append( bJnt.name  )


		if not  num == 0:
			bJnt.parent( bJnts_list[ num -1] )

	utilLogger.info('End of the replaceTmpJnt function.')
	return bJnts_list

