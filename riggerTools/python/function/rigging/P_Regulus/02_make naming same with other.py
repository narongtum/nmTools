import maya.cmds as cmds
#... Pair renaming between no and dode
# Define the controls dictionary
controls = {
	"noman": {
		"arm_leg_FK": [
			'ballLegFkLFT_ctrl', 'ankleFkLFT_ctrl', 'lowerLegFkLFT_ctrl', 'upperLegFkLFT_ctrl',
			'ballLegFkRGT_ctrl', 'ankleFkRGT_ctrl', 'lowerLegFkRGT_ctrl', 'upperLegFkRGT_ctrl',
			'handFkLFT_ctrl', 'lowerArmFkLFT_ctrl', 'upperArmFkLFT_ctrl',
			'handFkRGT_ctrl', 'lowerArmFkRGT_ctrl', 'upperArmFkRGT_ctrl'
		],
		"arm_leg_IK": [
			'footIkLFT_ctrl', 'kneePovLFT_ctrl', 'footIkRGT_ctrl', 'kneePovRGT_ctrl',
			'handIkLFT_ctrl', 'elbowPovLFT_ctrl', 'handIkRGT_ctrl', 'elbowPovRGT_ctrl',
			'upperLegIkRootLFT_ctrl', 'upperLegIkRootRGT_ctrl',
			'upperArmIkRootLFT_ctrl', 'upperArmIkRootRGT_ctrl'
		],
		"spine": [
			'spineCurl_ctrl', 'spine01_ctrl', 'spine02_ctrl', 'clavLFT_ctrl', 'clavRGT_ctrl'
		]
	},
	"dode": {
		"spine": [
			'spineCurl_ctrl', 'spine01FK_ctrl', 'spine02FK_ctrl', 'clvLFT_ctrl', 'clvRGT_ctrl'
		],
		"arm_leg_FK": [
			'ballLFT_ctrl', 'footLFTFK_ctrl', 'lowerLegLFTFK_ctrl', 'upperLegLFTFK_ctrl',
			'ballRGT_ctrl', 'footRGTFK_ctrl', 'lowerLegRGTFK_ctrl', 'upperLegRGTFK_ctrl',
			'handLFTFK_ctrl', 'lowerArmLFTFK_ctrl', 'upperArmLFTFK_ctrl',
			'handRGTFK_ctrl', 'lowerArmRGTFK_ctrl', 'upperArmRGTFK_ctrl'
		],
		"arm_leg_IK": [
			'footLFTIK_ctrl', 'legLFTPov_ctrl', 'footRGTIK_ctrl', 'legRGTPov_ctrl',
			'armLFTIK_ctrl', 'armLFTPov_ctrl', 'armRGTIK_ctrl', 'armRGTPov_ctrl',
			'upperLegLFTIK_ctrl', 'upperLegRGTIK_ctrl', 'upperArmLFTIK_ctrl', 'upperArmRGTIK_ctrl'
		]
	}
}

# Iterate through each category in the controls dictionary
for category in controls["noman"]:
	# Iterate through the noman controllers in the current category
	for idx, noman_ctrl in enumerate(controls["noman"][category]):
		# Check if the noman control exists in the Maya scene
		if mc.objExists(noman_ctrl):
			# Get the corresponding dode control
			dode_ctrl = controls["dode"][category][idx]

			# Print or perform the replacement
			print(f"Replacing '{noman_ctrl}' with '{dode_ctrl}'")

			# Rename the noman controller to the dode controller name
			mc.rename(noman_ctrl, dode_ctrl)
		else:
			print(f"'{noman_ctrl}' does not exist in the scene.")

