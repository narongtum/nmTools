# # # # # # # # # # # # # # # #
#...  list end joint
# # # # # # # # # # # # # # # #

import maya.cmds as cmds

# Get the selected joint(s)
selected_joints = cmds.ls(sl=True, type='joint')

# Iterate through the selected joints
for selected_joint in selected_joints:
	 # Find the tip joint(s) in the hierarchy
	 tip_joints = cmds.listRelatives(selected_joint, allDescendents=True, type='joint')
	 tip_joints = [joint for joint in tip_joints if not cmds.listRelatives(joint, c=True, type='joint')]

	 # Print the tip joint(s)
	 if tip_joints:
		  print("Tip joint(s) of", selected_joint, ":", tip_joints)
		  mc.select(tip_joints, r=True )
	 else:
		  print("No tip joints found for", selected_joint)
