'''

node short name dictionary


from function.rigging.util import mayaNodeDict as mnd
reload(mnd)
'''



'''
# How to use



nodeDict = ext.NODE_dict

for each in nodeDict:
	if each["longName"] == 'joint':
		node_exp = each["shortName"]
			
'''




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
	{	'longName': 'decomposeMatrix'		, 	'shortName': 'dcom'					},
	{	'longName': 'animCurveU'			, 	'shortName': 'animCrv'				},
	{	'longName': 'multDoubleLinear'		, 	'shortName': 'mdl'					},
	{	'longName': 'phong'					, 	'shortName': 'phong'				},
	{	'longName': 'shadingEngine'			, 	'shortName': 'sg'					},
	{	'longName': 'motionPath'							, 	'shortName': 'mp'						},
	{	'longName': 'cMuscleSmartConstraint'				, 	'shortName': 'musleCons'				},
	{	'longName': 'addDoubleLinear'						, 	'shortName': 'adl'						},
	{	'longName': 'aimConstraint'							, 	'shortName': 'aimCons'					},
	{	'longName': 'animCurveUU'							, 	'shortName': 'animUU'					},
	{	'longName': 'curveInfo'								,	'shortName': 'crvInfo'					},
	{	'longName': 'follicle'								,	'shortName': 'flc'					},
	{	'longName': 'remapValue'								,	'shortName': 'remap'					}
	

]



# color dictionary calling in core
COLOR_dict = {   'yellow'    : 17 ,          'red'           : 13 ,
				'softBlue'  : 18 ,          'blue'          : 6 ,
				'white'     : 16 ,          'brown'         : 11 ,
				'black'     : 1 ,           'gray'          : 2 ,
				'softGray'  : 3 ,           'darkRed'       : 4 ,
				'darkBlue'  : 5 ,           'darkGreen'     : 7 ,
				'green'     : 14 ,          'none'          : 0     }


# for arg message in arm and leg function
MESSAGE_dict = { 	'listString': ('region' , 'location'), # location get foot or angle only
					'listbJnt' :  ('stick' , 'upJnt' , 'midJnt' , 'lowJnt'), 
					'listCtrl' :  ('upFkCtrl' , 'midFkCtrl' , 'lowFkCtrl' , 'offset'), 
					'listPov'  :  ('pov' , 'ikCtrl' )							}


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

def askColor(side):
	if side == 'LFT':
		return 'red'
	elif side == 'RGT':
		return 'blue'
	elif side == 'MID':
		return 'yellow'
	else:
		return 'white'



standardJnt_list = [		'ankleLFT_bJnt','ankleRGT_bJnt','ballLFT_bJnt','ballRGT_bJnt',
		'clavLFT_bJnt','clavRGT_bJnt','handLFT_bJnt','handRGT_bJnt','head01_bJnt',
		'hip_bJnt','index01LFT_bJnt','index01RGT_bJnt','index02LFT_bJnt','index02RGT_bJnt',
		'index03LFT_bJnt','index03RGT_bJnt','lowerArmLFT_bJnt',
		'lowerArmRGT_bJnt','lowerLegLFT_bJnt','lowerLegRGT_bJnt','neck_bJnt',
		'ring01LFT_bJnt','ring01RGT_bJnt','ring02LFT_bJnt',
		'ring02RGT_bJnt','ring03LFT_bJnt','ring03RGT_bJnt',
		'spine01_bJnt','spine02_bJnt','spine03_bJnt','spine04_bJnt',
		'thumb01LFT_bJnt','thumb01RGT_bJnt','thumb02LFT_bJnt',
		'thumb02RGT_bJnt','thumb03LFT_bJnt','thumb03RGT_bJnt',
		'upperArmLFT_bJnt','upperArmRGT_bJnt','upperLegLFT_bJnt','upperLegRGT_bJnt'	]



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
								'tongueOut']                 ,

						'name_exclude':[	'jawForward','jawLeft','jawRight','mouthLeft',
											'mouthRight','mouthFrownLeft','mouthFrownRight',
											'mouthDimpleLeft','mouthDimpleRight','mouthStretchLeft',
											'mouthStretchRight','mouthShrugLower','mouthShrugUpper',
											'mouthPressLeft','mouthPressRight','mouthLowerDownLeft',
											'mouthLowerDownRight','mouthUpperUpLeft','mouthUpperUpRight',
											'cheekPuff','cheekSquintLeft','cheekSquintRight','noseSneerLeft',
											'noseSneerRight'] }