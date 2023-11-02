


'''

#... Generig dictionary file 


from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

'''



'''
#... How to use



nodeDict = mnd.NODE_dict

for each in nodeDict:
	if each["longName"] == 'joint':
		node_exp = each["shortName"]




nodeDict = mnd.NODE_dict['eulerToQuat']
		
'''





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
	{	'longName': 'composeMatrix'							,	'shortName': 'composeMatrix'			},
	{	'longName': 'vectorProduct'							,	'shortName': 'vectorProd'					},
	{	'longName': 'fourByFourMatrix'						,	'shortName': 'fourByFourMat'				},
	{	'longName': 'multMatrix'							,	'shortName': 'multMatrix'					},
	{	'longName': 'aimMatrix'								,	'shortName': 'aimMatrix'					},
	{	'longName': 'wtAddMatrix'							,	'shortName': 'wtAddMatrix'					},
	{	'longName': 'eulerToQuat'							,	'shortName': 'eulerToQuat'					},
	{	'longName': 'quatInvert'							,	'shortName': 'quatInvert'					},
	{	'longName': 'quatProd'								,	'shortName': 'quatProd'						},
	{	'longName': 'quatToEuler'							,	'shortName': 'quatToEuler'					},
	{	'longName': 'blendMatrix'							,	'shortName': 'blendMat'					},
	{	'longName': 'blendShape'							,	'shortName': 'bsh'					},
	{	'longName': 'network'							,	'shortName': 'meta'					}
	

]



def get_short_name(long_name):
	for node in NODE_dict:
		if node['longName'] == long_name:
			return node['shortName']
	return long_name



# color dictionary calling in core
COLOR_dict = {   'yellow'    : 17 ,          'red'           : 13 ,
				'softBlue'  : 18 ,          'blue'          : 6 ,
				'white'     : 16 ,          'brown'         : 11 ,
				'black'     : 1 ,           'gray'          : 2 ,
				'softGray'  : 3 ,           'darkRed'       : 4 ,
				'darkBlue'  : 5 ,           'darkGreen'     : 7 ,
				'green'     : 14 ,          'softBlue'      : 18 ,
				'none'      : 0     }


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



make_controller_thicker = (		'head01_ctrl','eyeCenter_ctrl','upperArmLFTFK_ctrl',
								'lowerArmLFTFK_ctrl','handLFTFK_ctrl','upperLegLFTFK_ctrl','lowerLegLFTFK_ctrl','footLFTFK_ctrl','upperArmLFTFK_ctrl','handLFTFK_ctrl'
								'lowerArmRGTFK_ctrl','handRGTFK_ctrl','upperLegRGTFK_ctrl','lowerLegRGTFK_ctrl','footRGTFK_ctrl','upperArmRGTFK_ctrl','handRGTFK_ctrl'
								'hip_ctrl','spine01FK_ctrl','spine02FK_ctrl','spine03FK_ctrl',					
								'upperArmFkLFT_ctrl','lowerArmFkLFT_ctrl','handFkLFT_ctrl',
								'upperArmFkRGT_ctrl','lowerArmFkRGT_ctrl','handFkRGT_ctrl',
								'handIkLFT_ctrl','handIkRGT_ctrl','hip_ctrl','handStickLFT_ctrl','handStickRGT_ctrl',
								'cog_ctrl','clavLFT_ctrl','clavRGT_ctrl')


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
					