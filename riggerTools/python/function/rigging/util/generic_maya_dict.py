#... Generig dictionary file USE THIS FILE INSTEAD mayaNodeDict
#... Generig dictionary file USE THIS FILE INSTEAD mayaNodeDict
#... Generig dictionary file USE THIS FILE INSTEAD mayaNodeDict
#... Generig dictionary file USE THIS FILE INSTEAD mayaNodeDict

'''




from function.rigging.util import generic_maya_dict as mnd
reload(mnd)



mnd.select_body_jnt()

'''



'''
#... How to use

nodeDict = mnd.NODE_dict

for each in nodeDict:
	if each["longName"] == 'joint':
		node_exp = each["shortName"]







#... select body bind joint

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

nodeDict = mnd.standardJnt_list

for each in nodeDict:
	mc.select(each, add=True)

		
'''


'''
from function.rigging.util import generic_maya_dict as mnd
reload(mnd)
mnd.COLOR_part_dict['right']
'''



COLOR_part_dict = { 	'right': 'red', 
						'left': 'blue', 
						'dynamic': 'white',
						'primary': 'yellow',
						'secondary': 'white',
						'tertiary': 'softBlue',
						'offset':'white',
						'gimbal': 'white'}


def askColor(side):
	if side == 'LFT':
		return 'red'
	elif side == 'RGT':
		return 'blue'
	elif side == 'MID':
		return 'yellow'
	else:
		return 'white'





dForwardAxis_dict = {	'x+':'0',
						'x-':'1',
						'y+':'2',
						'y-':'3',
						'z+':'4',
						'z-':'5',	}

dWorldUpAxis_dict = {	'y+':'0',
						'y-':'1',
						'yc':'2',
						'z+':'3',
						'z-':'4',
						'zc':'5',
						'x+':'6',
						'x-':'7',
						'xc':'8'	}





alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

#... newr version using this instead
NODE_short_dict = {
	'nurbsSurface': 'nrb',
	'nurbsCurve': 'ctrl',
	'condition': 'cnd',
	'blendColors': 'blc',
	'distanceBetween': 'dtw',
	'expression': 'exp',
	'file': 'file',
	'lambert': 'lambert',
	'place2dTexture': 'place2d',
	'plusMinusAverage': 'pma',
	'skinCluster': 'skc',
	'multiplyDivide': 'mdv',
	'reverse': 'rev',
	'mesh': 'ply',
	'cluster': 'clus',
	'parentConstraint': 'parCons',
	'scaleConstraint': 'scaleCons',
	'orientConstraint': 'orienCons',
	'pointConstraint': 'poinCons',
	'ikHandle': 'ikh',
	'ikEffector': 'ike',
	'poleVectorConstraint': 'poleCons',
	'joint': 'jnt',
	'group': 'grp',
	'locator': 'loc',
	'clamp': 'cmp',
	'pointOnCurveInfo': 'poci',
	'decomposeMatrix': 'deComp',
	'animCurveU': 'animCrv',
	'multDoubleLinear': 'mdl',
	'phong': 'phong',
	'shadingEngine': 'sg',
	'motionPath': 'mp',
	'cMuscleSmartConstraint': 'musleCons',
	'addDoubleLinear': 'adl',
	'aimConstraint': 'aimCons',
	'animCurveUU': 'animUU',
	'curveInfo': 'crvInfo',
	'follicle': 'flc',
	'remapValue': 'remap',
	'composeMatrix': 'composeMatrix',
	'vectorProduct': 'vecProd',
	'fourByFourMatrix': 'fBFMat',
	'multMatrix': 'multMatrix',
	'aimMatrix': 'aimMatrix',
	'wtAddMatrix': 'wtAddMat',
	'eulerToQuat': 'eulToQuat',
	'quatInvert': 'quatInv',
	'quatProd': 'quatProd',
	'quatToEuler': 'quatToEul',
	'blendMatrix': 'blendMat',
	'blendShape': 'bsh',
	'network': 'meta',
	'setRange': 'setRange',
	'deformSquash': 'defSquash' ,
	'blendWeighted':'blendWeighted',
	'animCurveUL':'animCurveUL',
	'deformSine':'defSine',
	'blendTwoAttr':'bta',
	'pickMatrix':'pickMat'

}

#... Example usage
# ext = mnd.NODE_short_dict.get('parentConstraint', 'Unknown') # Output: parCons









# same as the mayaNodeDict not sure which dict to put
NODE_dict = [
	
	{	'longName': 'nurbsSurface'		, 		'shortName': 'nrb'					},
	{	'longName': 'nurbsCurve'			, 	'shortName': 'ctrl'					},
	{	'longName': 'condition'				, 	'shortName': 'cnd'					},
	{	'longName': 'blendColors'			, 	'shortName': 'blc'					},
	{	'longName': 'distanceBetween'		, 	'shortName': 'dtw'					},
	{	'longName': 'expression'			, 	'shortName': 'exp'					},
	{	'longName': 'file'					, 	'shortName': 'file'					},
	{	'longName': 'lambert'				, 	'shortName': 'lambert'				},					
	{	'longName': 'place2dTexture'		, 	'shortName': 'place2d'				},
	{	'longName': 'plusMinusAverage'		, 	'shortName': 'pma'					},
	{	'longName': 'skinCluster'			, 	'shortName': 'skc'					},
	{	'longName': 'multiplyDivide'		, 	'shortName': 'mdv'					},
	{	'longName': 'reverse'				, 	'shortName': 'rev'					},
	{	'longName': 'mesh'					, 	'shortName': 'ply'					},
	{	'longName': 'cluster'				, 	'shortName': 'clus'					},
	{	'longName': 'parentConstraint'		, 	'shortName': 'parCons'				},
	{	'longName': 'scaleConstraint'		, 	'shortName': 'scaleCons'			},
	{	'longName': 'orientConstraint'		, 	'shortName': 'orienCons'			},
	{	'longName': 'pointConstraint'		, 	'shortName': 'poinCons'				},
	{	'longName': 'ikHandle'				, 	'shortName': 'ikh'					},
	{	'longName': 'ikEffector'			, 	'shortName': 'ike'					},
	{	'longName': 'poleVectorConstraint'	, 	'shortName': 'poleCons'				},
	{	'longName': 'joint'					, 	'shortName': 'jnt'					},
	{	'longName': 'group'					, 	'shortName': 'grp'					},
	{	'longName': 'locator'				, 	'shortName': 'loc'					},
	{	'longName': 'clamp'					, 	'shortName': 'cmp'					},
	{	'longName': 'pointOnCurveInfo'		, 	'shortName': 'poci'					},
	{	'longName': 'decomposeMatrix'		, 	'shortName': 'deComp'				},
	{	'longName': 'animCurveU'			, 	'shortName': 'animCrv'				},
	{	'longName': 'multDoubleLinear'		, 	'shortName': 'mdl'					},
	{	'longName': 'phong'					, 	'shortName': 'phong'				},
	{	'longName': 'shadingEngine'			, 	'shortName': 'sg'					},
	{	'longName': 'motionPath'							, 	'shortName': 'mp'						},
	{	'longName': 'cMuscleSmartConstraint'				, 	'shortName': 'musleCons'				},
	{	'longName': 'addDoubleLinear'						, 	'shortName': 'adl'						},
	{	'longName': 'aimConstraint'							, 	'shortName': 'aimCons'					},
	{	'longName': 'aimConstraint'							, 	'shortName': 'aimCons'					},
	{	'longName': 'animCurveUU'							, 	'shortName': 'animUU'					},
	{	'longName': 'curveInfo'								,	'shortName': 'crvInfo'					},
	{	'longName': 'follicle'								,	'shortName': 'flc'						},
	{	'longName': 'remapValue'							,	'shortName': 'remap'					},
	{	'longName': 'composeMatrix'							,	'shortName': 'composeMat'			},
	{	'longName': 'vectorProduct'							,	'shortName': 'vectorProd'					},
	{	'longName': 'fourByFourMatrix'						,	'shortName': 'fourByFourMat'				},
	{	'longName': 'multMatrix'							,	'shortName': 'multMat'					},
	{	'longName': 'aimMatrix'								,	'shortName': 'aimMat'					},
	{	'longName': 'wtAddMatrix'							,	'shortName': 'wtAddMat'					},
	{	'longName': 'eulerToQuat'							,	'shortName': 'eulerToQuat'					},
	{	'longName': 'quatInvert'							,	'shortName': 'quatInvert'					},
	{	'longName': 'quatProd'								,	'shortName': 'quatProd'						},
	{	'longName': 'quatToEuler'							,	'shortName': 'quatToEuler'					},
	{	'longName': 'blendMatrix'							,	'shortName': 'blendMat'					},
	{	'longName': 'blendShape'							,	'shortName': 'bsh'					},
	{	'longName': 'network'							,	'shortName': 'meta'						},
	{	'longName': 'setRange'							,	'shortName': 'setRange'					},
	{	'longName': 'blendWeighted'							,	'shortName': 'blendWeighted'		},	
	{	'longName': 'animCurveUL'							,	'shortName': 'animCurveUL'}	,
	{	'longName': 'deformSine'							,	'shortName': 'defSine'}	,
	{	'longName': 'blendTwoAttr'							,	'shortName': 'bta'},
	{	'longName': 'pickMatrix'							,	'shortName': 'pickMat'}
]



#... naming for auto name in meta data
auto_name_variation = ('01','02')
auto_name_used = ('Gameplay_Model','Charactor_Model','Other')




#... finger dict
FINGER_dict = {		'fingerName':		('thumb','index','middle','ring','pinky'),
					'fingerbehavior':	('fist','roll','relax','cup','spread','wide')
					 }



#... foot dict
FOOT_dict = {	
					'footbehavior':	('ballRoll','toeRoll','heelTwist','toeTwist','footRock','ballRise')
					 }



def select_body_jnt():
	for each in standardJnt_list:
		if mc.objExists(each):
			mc.select(each, add = True)
	print('DONE')




def get_short_name(long_name):
	for node in NODE_dict:
		if node['longName'] == long_name:
			return node['shortName']
	return long_name



# color dictionary calling in core
COLOR_dict = {   'yellow'    : 17 ,          'red'           : 13 ,
				'softBlue'  : 18 ,          'blue'          : 6 ,
				'white'     : 16 ,          'brown'         : 11 ,
				'black'     : 1 ,           'gray'          : 3 ,
				'softGray'  : 3 ,           'darkRed'       : 4 ,
				'darkBlue'  : 5 ,           'darkGreen'     : 7 ,
				'green'     : 14 ,          'softBlue'      : 18 ,
				'none'      : 0     }




# for arg message in arm and leg function
MESSAGE_dict = { 	'listString':	('region' , 'location'), # location get foot or angle only
					'listbJnt' 	:	('stick' , 'upJnt' , 'midJnt' , 'lowJnt'), 
					'listCtrl' 	:	('upFkCtrl' , 'midFkCtrl' , 'lowFkCtrl' , 'offset'), 
					'listPov'  	:	('pov' , 'ikCtrl' ),
					'listIkRoot':	('ikRootCtrl',),
					'meta'		:	['metaNode']							}


rotOrder_dict = {		'xyz'  : 0   ,
						'yzx'  : 1   ,
						'zxy'  : 2   ,
						'xzy'  : 3   ,
						'yxz'  : 4   ,
						'zyx'  : 5		}

rgbCode = {		'black':	(0,0,0)		,
				'red':		(1,0,0)		,
				'green':	(0,1,0)		,
				'blue':		(0,0,1)		,
				'yellow':	(1,1,0)		,
				'white':	(1,1,1)			}


make_bigger_list = (		'head01_ctrl','eyeCenter_ctrl',

					'hip_ctrl','spine01FK_ctrl','spine02FK_ctrl','spine03FK_ctrl',

					'upperArmFkLFT_ctrl','lowerArmFkLFT_ctrl','handFkLFT_ctrl',
					'ballLegFkLFT_ctrl','ankleFkLFT_ctrl','lowerLegFkLFT_ctrl','upperLegFkLFT_ctrl'

					'upperArmFkRGT_ctrl','lowerArmFkRGT_ctrl','handFkRGT_ctrl',
					'ballLegFkRGT_ctrl','ankleFkRGT_ctrl','lowerLegFkRGT_ctrl','upperLegFkRGT_ctrl'	,

					'upperArmIkRootLFT_ctrl','upperLegIkRootLFT_ctrl','footIkLFT_ctrl','handIkLFT_ctrl',
					'upperArmIkRootRGT_ctrl','upperLegIkRootRGT_ctrl','footIkRGT_ctrl','handIkRGT_ctrl'
)
					







controller_thicker_list = (		'head01_ctrl','eyeCenter_ctrl','upperArmLFTFK_ctrl',
								'lowerArmLFTFK_ctrl','handLFTFK_ctrl','upperLegLFTFK_ctrl','lowerLegLFTFK_ctrl','footLFTFK_ctrl','upperArmLFTFK_ctrl','handLFTFK_ctrl'
								'lowerArmRGTFK_ctrl','handRGTFK_ctrl','upperLegRGTFK_ctrl','lowerLegRGTFK_ctrl','footRGTFK_ctrl','upperArmRGTFK_ctrl','handRGTFK_ctrl'
								'hip_ctrl','spine01FK_ctrl','spine02FK_ctrl','spine03FK_ctrl',
								'upperArmFkLFT_ctrl','lowerArmFkLFT_ctrl','handFkLFT_ctrl',
								'upperArmFkRGT_ctrl','lowerArmFkRGT_ctrl','handFkRGT_ctrl',
								'handIkLFT_ctrl','handIkRGT_ctrl','hip_ctrl','handStickLFT_ctrl','handStickRGT_ctrl',
								'cog_ctrl','clavLFT_ctrl','clavRGT_ctrl','footIkRGT_ctrl','footIkLFT_ctrl',
								'ballLegFkLFT_ctrl','ankleFkLFT_ctrl','lowerLegFkLFT_ctrl','upperLegFkLFT_ctrl',
								'ballLegFkRGT_ctrl','ankleFkRGT_ctrl','lowerLegFkRGT_ctrl','upperLegFkRGT_ctrl')


"""standardJnt_list = [		'ankleLFT_bJnt','ankleRGT_bJnt','ballLFT_bJnt','ballRGT_bJnt',
		'clavLFT_bJnt','clavRGT_bJnt','handLFT_bJnt','handRGT_bJnt','head01_bJnt',
		'hip_bJnt','index01LFT_bJnt','index01RGT_bJnt','index02LFT_bJnt','index02RGT_bJnt',
		'index03LFT_bJnt','index03RGT_bJnt','lowerArmLFT_bJnt',
		'lowerArmRGT_bJnt','lowerLegLFT_bJnt','lowerLegRGT_bJnt','neck_bJnt',
		'ring01LFT_bJnt','ring01RGT_bJnt','ring02LFT_bJnt',
		'ring02RGT_bJnt','ring03LFT_bJnt','ring03RGT_bJnt',
		'spine01_bJnt','spine02_bJnt','spine03_bJnt','spine04_bJnt',
		'thumb01LFT_bJnt','thumb01RGT_bJnt','thumb02LFT_bJnt',
		'thumb02RGT_bJnt','thumb03LFT_bJnt','thumb03RGT_bJnt',
		'upperArmLFT_bJnt','upperArmRGT_bJnt','upperLegLFT_bJnt','upperLegRGT_bJnt'	]"""


standardJnt_list = ('ankleLFT_bJnt',
'ankleRGT_bJnt',
'ballLFT_bJnt',
'ballRGT_bJnt',
'clavLFT_bJnt',
'clavRGT_bJnt',
'handLFT_bJnt',
'handRGT_bJnt',
'hip_bJnt',
'index01LFT_bJnt',
'index01RGT_bJnt',
'index02LFT_bJnt',
'index02RGT_bJnt',
'index03LFT_bJnt',
'index03RGT_bJnt',
'lowerArmLFT_bJnt',
'lowerArmRGT_bJnt',
'lowerLegLFT_bJnt',
'lowerLegRGT_bJnt',
'ring01LFT_bJnt',
'ring01RGT_bJnt',
'ring02LFT_bJnt',
'ring02RGT_bJnt',
'ring03LFT_bJnt',
'ring03RGT_bJnt',
'spine01_bJnt',
'spine02_bJnt',
'spine03_bJnt','thumb01LFT_bJnt',
'thumb01RGT_bJnt','thumb02LFT_bJnt',
'thumb02RGT_bJnt','thumb03LFT_bJnt',
'thumb03RGT_bJnt',
'upperArmLFT_bJnt',
'upperArmRGT_bJnt',
'upperLegLFT_bJnt',
'upperLegRGT_bJnt','neck_bJnt',
'middle03LFT_bJnt',
'middle02LFT_bJnt',
'middle01LFT_bJnt',
'middle03RGT_bJnt',
'middle02RGT_bJnt',
'middle01RGT_bJnt',
'pinky01LFT_bJnt',
'pinky02LFT_bJnt',
'pinky03LFT_bJnt',
'pinky01RGT_bJnt',
'pinky02RGT_bJnt',
'pinky03RGT_bJnt',
'head01_bJnt',
'eyeLFT_bJnt',
'eyeRGT_bJnt')






standard_jnt_dict = {
	'root': ['root','L_weapon_bJnt','R_weapon_bJnt'],
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

	'R_leg': ['upperLegRGT_bJnt', 'lowerLegRGT_bJnt', 'ankleRGT_bJnt', 'ballRGT_bJnt'],

	'spine': ['hip_bJnt', 'spine01_bJnt', 'spine02_bJnt', 'spine03_bJnt'],

	'head': ['neck_bJnt', 'head01_bJnt', 'eyeLFT_bJnt', 'eyeRGT_bJnt']
}


ue_jnt_dict = {
	'root': ['root', 'weapon_l', 'weapon_r'],
	'spine': ['pelvis', 'spine_01', 'spine_02', 'spine_03'],
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





nanuq_jnt_dict = {
	'root': ['Root_JNT','L_HandSlot_JNT','R_HandSlot_JNT'],
	'L_arm': ['L_Clav_JNT', 'L_Shoulder_JNT', 'L_Elbow_JNT', 'L_Wrist_JNT',
			  'L_Thumb1_JNT', 'L_Thumb2_JNT', 'L_Thumb3_JNT',
			  'L_Index1_JNT', 'L_Index2_JNT', 'L_Index3_JNT',
			  'L_Middle1_JNT', 'L_Middle2_JNT', 'L_Middle3_JNT',
			  'L_Ring1_JNT', 'L_Ring2_JNT', 'L_Ring3_JNT',
			  'L_Pinky1_JNT', 'L_Pinky2_JNT', 'L_Pinky3_JNT'],

	'R_arm': ['R_Clav_JNT', 'R_Shoulder_JNT', 'R_Elbow_JNT', 'R_Wrist_JNT',
			  'R_Thumb1_JNT', 'R_Thumb2_JNT', 'R_Thumb3_JNT',
			  'R_Index1_JNT', 'R_Index2_JNT', 'R_Index3_JNT',
			  'R_Middle1_JNT', 'R_Middle2_JNT', 'R_Middle3_JNT',
			  'R_Ring1_JNT', 'R_Ring2_JNT', 'R_Ring3_JNT',
			  'R_Pinky1_JNT', 'R_Pinky2_JNT', 'R_Pinky3_JNT'],

	'L_leg': ['L_Hip_JNT', 'L_Knee_JNT', 'L_Ankle_JNT', 'L_Ball_JNT'],

	'R_leg': ['R_Hip_JNT', 'R_Knee_JNT', 'R_Ankle_JNT', 'R_Ball_JNT'],

	'spine': ['Hip_JNT', 'Back_JNT', 'Spine1_JNT', 'Chest_JNT'],

	'head': ['Neck_JNT', 'Head_JNT', 'L_Eye_JNT', 'R_Eye_JNT']
}



import maya.cmds as mc

# Rename function
def rename_joints(standard_dict, nanuq_dict):
	for body_part in standard_dict:
		# Iterate over joints in each part
		for i, standard_jnt in enumerate(standard_dict[body_part]):
			if i < len(nanuq_dict[body_part]):  # Ensure there is a corresponding nanuq joint
				nanuq_jnt = nanuq_dict[body_part][i]
				
				# Check if the standard joint exists in the scene
				if mc.objExists(standard_jnt):
					# Rename to the corresponding nanuq joint
					mc.rename(standard_jnt, nanuq_jnt)
					print(f"Renamed {standard_jnt} to {nanuq_jnt}")
				else:
					print(f"{standard_jnt} does not exist.")
















regulus_facial_dict = {'facialRegion': 'facial'    ,
							   'posiBlock' : (1,1)         	,

							   'name_all':['eyeWondering_L',
										   'eyeWondering_R',
										   'eyeBlink_L',
										   'eyeBlink_R',
										   'eyeAngry_L',
										   'eyeAngry_R'] ,

							   'name_exclude':[]}










facial_dict_ARKit =   {   'facialRegion'  :   'facial'    	,
							'posiBlock' : (1,1)         	,
						
						'name_all':['eyeBlinkLeft',
								'eyeLookDownLeft',
								'eyeLookInLeft',
								'eyeLookOutLeft',
								'eyeLookUpLeft',
								'eyeSquintLeft',
								'eyeWideLeft',
								'eyeBlinkRight',
								'eyeLookDownRight',
								'eyeLookInRight',
								'eyeLookOutRight',
								'eyeLookUpRight',
								'eyeSquintRight',
								'eyeWideRight',
								'jawForward',
								'jawLeft',
								'jawRight',
								'jawOpen',
								'mouthClose',
								'mouthFunnel',
								'mouthPucker',
								'mouthRight',
								'mouthLeft',
								'mouthSmileLeft',
								'mouthSmileRight',
								'mouthFrownRight',
								'mouthFrownLeft',
								'mouthDimpleLeft',
								'mouthDimpleRight',
								'mouthStretchLeft',
								'mouthStretchRight',
								'mouthRollLower',
								'mouthRollUpper',
								'mouthShrugLower',
								'mouthShrugUpper',
								'mouthPressLeft',
								'mouthPressRight',
								'mouthLowerDownLeft',
								'mouthLowerDownRight',
								'mouthUpperUpLeft',
								'mouthUpperUpRight',
								'browDownLeft',
								'browDownRight',
								'browInnerUp',
								'browOuterUpLeft',
								'browOuterUpRight',
								'cheekPuff',
								'cheekSquintLeft',
								'cheekSquintRight',
								'noseSneerLeft',
								'noseSneerRight',
								'tongueOut',
								'uniqueFace']                 ,

						'name_exclude':[	'jawForward','jawLeft','jawRight','mouthLeft',
											'mouthRight','mouthFrownLeft','mouthFrownRight',
											'mouthDimpleLeft','mouthDimpleRight','mouthStretchLeft',
											'mouthStretchRight','mouthShrugLower','mouthShrugUpper',
											'mouthPressLeft','mouthPressRight','mouthLowerDownLeft',
											'mouthLowerDownRight','mouthUpperUpLeft','mouthUpperUpRight',
											'cheekPuff','cheekSquintLeft','cheekSquintRight','noseSneerLeft',
											'noseSneerRight'] ,

						'kite_additional':[			 u'eyeBlinkLookDownLeft',
													 u'eyeBlinkLookDownRight',
													 u'eyeBlinkLookUpLeft',
													 u'eyeBlinkLookUpRight',
													 u'eyeBlinkLookOutLeft',
													 u'eyeBlinkLookInRight',
													 u'eyeBlinkLookInLeft',
													 u'eyeBlinkLookOutRight',
													 u'eyeBlinkSquintLeft',
													 u'eyeBlinkSquintRight',
													 u'eyeBlinkCheekSquintLeft',
													 u'eyeBlinkCheekSquintRight']	,
						'mouth_oUU':[]

						}


# facial full
facial_dict_ARKit_full =   {   'facialRegion'  :   'facial'    	,
							'posiBlock' : (1,1)         	,
						
						'name_all':['eyeBlinkLeft',
								'eyeLookDownLeft',
								'eyeLookInLeft',
								'eyeLookOutLeft',
								'eyeLookUpLeft',
								'eyeSquintLeft',
								'eyeWideLeft',
								'eyeBlinkRight',
								'eyeLookDownRight',
								'eyeLookInRight',
								'eyeLookOutRight',
								'eyeLookUpRight',
								'eyeSquintRight',
								'eyeWideRight',
								'jawForward',
								'jawLeft',
								'jawRight',
								'jawOpen',
								'mouthClose',
								'mouthFunnel',
								'mouthPucker',
								'mouthRight',
								'mouthLeft',
								'mouthSmileLeft',
								'mouthSmileRight',
								'mouthFrownRight',
								'mouthFrownLeft',
								'mouthDimpleLeft',
								'mouthDimpleRight',
								'mouthStretchLeft',
								'mouthStretchRight',
								'mouthRollLower',
								'mouthRollUpper',
								'mouthShrugLower',
								'mouthShrugUpper',
								'mouthPressLeft',
								'mouthPressRight',
								'mouthLowerDownLeft',
								'mouthLowerDownRight',
								'mouthUpperUpLeft',
								'mouthUpperUpRight',
								'browDownLeft',
								'browDownRight',
								'browInnerUp',
								'browOuterUpLeft',
								'browOuterUpRight',
								'cheekPuff',
								'cheekSquintLeft',
								'cheekSquintRight',
								'noseSneerLeft',
								'noseSneerRight',
								'tongueOut',
								'jawForward','jawLeft','jawRight','mouthLeft',
								'mouthRight','mouthFrownLeft','mouthFrownRight',
								'mouthDimpleLeft','mouthDimpleRight','mouthStretchLeft',
								'mouthStretchRight','mouthShrugLower','mouthShrugUpper',
								'mouthPressLeft','mouthPressRight','mouthLowerDownLeft',
								'mouthLowerDownRight','mouthUpperUpLeft','mouthUpperUpRight',
								'cheekPuff','cheekSquintLeft','cheekSquintRight','noseSneerLeft',
								'noseSneerRight'] ,

						'kite_additional':[			 u'eyeBlinkLookDownLeft',
													 u'eyeBlinkLookDownRight',
													 u'eyeBlinkLookUpLeft',
													 u'eyeBlinkLookUpRight',
													 u'eyeBlinkLookOutLeft',
													 u'eyeBlinkLookInRight',
													 u'eyeBlinkLookInLeft',
													 u'eyeBlinkLookOutRight',
													 u'eyeBlinkSquintLeft',
													 u'eyeBlinkSquintRight',
													 u'eyeBlinkCheekSquintLeft',
													 u'eyeBlinkCheekSquintRight']	,


						}





ribbon_joint =   {   'arm_rbn'  :	[	u'lwrArmRbn01RGT_rbnBJnt',
										 u'lwrArmRbn02RGT_rbnBJnt',
										 u'lwrArmRbn03RGT_rbnBJnt',
										 u'armHingesRbnRGT_rbnBJnt',
										 u'upArmRbn01RGT_rbnBJnt',
										 u'upArmRbn02RGT_rbnBJnt',
										 u'upArmRbn03RGT_rbnBJnt',
										 u'lwrArmRbn01LFT_rbnBJnt',
										 u'lwrArmRbn02LFT_rbnBJnt',
										 u'lwrArmRbn03LFT_rbnBJnt',
										 u'armHingesRbnLFT_rbnBJnt',
										 u'upArmRbn01LFT_rbnBJnt',
										 u'upArmRbn02LFT_rbnBJnt',
										 u'upArmRbn03LFT_rbnBJnt'],




					'leg_rbn'  :   					[		u'legHingesRbnLFT_rbnBJnt',
															u'legHingesRbnRGT_rbnBJnt',
															u'lwrLegRbn01LFT_rbnBJnt',
															u'lwrLegRbn01RGT_rbnBJnt',
															u'lwrLegRbn02LFT_rbnBJnt',
															u'lwrLegRbn02RGT_rbnBJnt',
															u'lwrLegRbn03LFT_rbnBJnt',
															u'lwrLegRbn03RGT_rbnBJnt',
															u'upLegRbn01LFT_rbnBJnt',
															u'upLegRbn01RGT_rbnBJnt',
															u'upLegRbn02LFT_rbnBJnt',
															u'upLegRbn02RGT_rbnBJnt',
															u'upLegRbn03LFT_rbnBJnt',
															u'upLegRbn03RGT_rbnBJnt']    	}





noman_arm_leg_FK = ['ballLegFkLFT_ctrl',
'ankleFkLFT_ctrl',
'lowerLegFkLFT_ctrl',
'upperLegFkLFT_ctrl',
'ballLegFkRGT_ctrl',
'ankleFkRGT_ctrl',
'lowerLegFkRGT_ctrl',
'upperLegFkRGT_ctrl',
'handFkLFT_ctrl',
'lowerArmFkLFT_ctrl',
'upperArmFkLFT_ctrl',
'handFkRGT_ctrl',
'lowerArmFkRGT_ctrl',
'upperArmFkRGT_ctrl']

noman_arm_leg_IK = ['footIkLFT_ctrl',
'kneePovLFT_ctrl',
'footIkRGT_ctrl',
'kneePovRGT_ctrl',
'handIkLFT_ctrl',
'elbowPovLFT_ctrl',
'handIkRGT_ctrl',
'elbowPovRGT_ctrl',
'upperLegIkRootLFT_ctrl',
'upperLegIkRootRGT_ctrl',
'upperArmIkRootLFT_ctrl',
'upperArmIkRootRGT_ctrl'
]


noman_spine=['spineCurl_ctrl',
'spine01_ctrl',
'spine02_ctrl',
'clavLFT_ctrl',
'clavRGT_ctrl']

dode_spine = ['spineCurl_ctrl',
'spine01FK_ctrl',
'spine02FK_ctrl',
'clvLFT_ctrl',
'clvRGT_ctrl']



dode_arm_leg_FK = ['ballLFT_ctrl',
'footLFTFK_ctrl',
'lowerLegLFTFK_ctrl',
'upperLegLFTFK_ctrl',
'ballRGT_ctrl',
'footRGTFK_ctrl',
'lowerLegRGTFK_ctrl',
'upperLegRGTFK_ctrl',
'handLFTFK_ctrl',
'lowerArmLFTFK_ctrl',
'upperArmLFTFK_ctrl',
'handRGTFK_ctrl',
'lowerArmRGTFK_ctrl',
'upperArmRGTFK_ctrl']


dode_arm_leg_IK = ['footLFTIK_ctrl',
'legLFTPov_ctrl',
'footRGTIK_ctrl',
'legRGTPov_ctrl',
'armLFTIK_ctrl',
'armLFTPov_ctrl',
'armRGTIK_ctrl',
'armRGTPov_ctrl',
'upperLegLFTIK_ctrl',
'upperLegRGTIK_ctrl',
'upperArmLFTIK_ctrl',
'upperArmRGTIK_ctrl']





match_naming_dict = {
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



handle_behavior_dict = {
						'finger':{
									'stick_name':'handStickLFT_ctrl',
									'behavior_name':['fist','roll','relax','cup','spread','wide'],
									'side':['LFT','RGT']		
									},
						'foot':{
									'stick_name':'footIkLFT_ctrl',
									'behavior_name':['ballRoll','toeRoll','heelTwist','toeTwist','footRock','ballRise'],
									'side':['LFT','RGT']		
									}
								}


eachFinger_behavior_dict = {
						'finger':{
									'stick_name':['thumblocalLFT_ctrl','indexlocalLFT_ctrl','middlelocalLFT_ctrl','ringlocalLFT_ctrl','pinkylocalLFT_ctrl'],
									'behavior_name':['roll','stretch'],
									'side':['LFT','RGT']			}
						}









