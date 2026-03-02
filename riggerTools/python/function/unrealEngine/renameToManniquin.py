import maya.cmds as mc

# 1. Dictionary Maya 
maya_jnt_dict = {
	'root': ['root', 'L_weapon_bJnt', 'R_weapon_bJnt'],
	'spine': ['hip_bJnt', 'spine01_bJnt', 'spine02_bJnt', 'spine03_bJnt', 'spine04_bJnt'],
	'head': ['neck_bJnt', 'head01_bJnt', 'eyeLFT_bJnt', 'eyeRGT_bJnt'],
	'L_arm': ['clavLFT_bJnt', 'upperArmLFT_bJnt', 'lowerArmLFT_bJnt', 'handLFT_bJnt',
			  'thumb01LFT_bJnt', 'thumb02LFT_bJnt', 'thumb03LFT_bJnt',
			  'index01LFT_bJnt', 'index02LFT_bJnt', 'index03LFT_bJnt',
			  'middle01LFT_bJnt', 'middle02LFT_bJnt', 'middle03LFT_bJnt',
			  'ring01LFT_bJnt', 'ring02LFT_bJnt', 'ring03LFT_bJnt',
			  'pinky01LFT_bJnt', 'pinky02LFT_bJnt', 'pinky03LFT_bJnt'],
	'R_arm': ['clavRGT_bJnt', 'upperArmRGT_bJnt', 'lowerArmRGT_bJnt', 'handRGT_bJnt',
			  'thumb01RGT_bJnt', 'thumb02RGT_bJnt', 'thumb03RGT_bJnt',
			  'index01RGT_bJnt', 'index02RGT_bJnt', 'index03RGT_bJnt',
			  'middle01RGT_bJnt', 'middle02RGT_bJnt', 'middle03RGT_bJnt',
			  'ring01RGT_bJnt', 'ring02RGT_bJnt', 'ring03RGT_bJnt',
			  'pinky01RGT_bJnt', 'pinky02RGT_bJnt', 'pinky03RGT_bJnt'],
	'L_leg': ['upperLegLFT_bJnt', 'lowerLegLFT_bJnt', 'ankleLFT_bJnt', 'ballLFT_bJnt'],
	'R_leg': ['upperLegRGT_bJnt', 'lowerLegRGT_bJnt', 'ankleRGT_bJnt', 'ballRGT_bJnt']
}

# 2. Dictionary side Unreal 
ue_jnt_dict = {
	'root': ['root', 'weapon_l', 'weapon_r'],
	'spine': ['pelvis', 'spine_01', 'spine_02', 'spine_03', 'spine_04'],
	'head': ['neck_01', 'head', 'eye_l', 'eye_r'],
	'L_arm': ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l',
			  'thumb_01_l', 'thumb_02_l', 'thumb_03_l',
			  'index_01_l', 'index_02_l', 'index_03_l',
			  'middle_01_l', 'middle_02_l', 'middle_03_l',
			  'ring_01_l', 'ring_02_l', 'ring_03_l',
			  'pinky_01_l', 'pinky_02_l', 'pinky_03_l'],
	'R_arm': ['clavicle_r', 'upperarm_r', 'lowerarm_r', 'hand_r',
			  'thumb_01_r', 'thumb_02_r', 'thumb_03_r',
			  'index_01_r', 'index_02_r', 'index_03_r',
			  'middle_01_r', 'middle_02_r', 'middle_03_r',
			  'ring_01_r', 'ring_02_r', 'ring_03_r',
			  'pinky_01_r', 'pinky_02_r', 'pinky_03_r'],
	'L_leg': ['thigh_l', 'calf_l', 'foot_l', 'ball_l'],
	'R_leg': ['thigh_r', 'calf_r', 'foot_r', 'ball_r']
}

def clean_rename_for_unreal(maya_map, ue_map):
	count = 0
	for category in maya_map:
		old_list = maya_map[category]
		new_list = ue_map.get(category, [])
		
		for i in range(len(old_list)):
			old_name = old_list[i]
			if i < len(new_list):
				new_clean_name = new_list[i]
				
				if mc.objExists(old_name):
					mc.rename(old_name, new_clean_name)
					print(f"Renamed: {old_name} -> {new_clean_name}")
					count += 1
	print(f"\n[Success] Renamed {count} joints to Unreal Standard.")

#... runcode
clean_rename_for_unreal(maya_jnt_dict, ue_jnt_dict)