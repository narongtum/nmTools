import maya.cmds as mc

# sys.path.append(r'D:\True_Axion\Tools\riggerTools\python\axionTools\rigging\autoRig\bodyRig')

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.autoRig.bodyRig import rootRig
reload( rootRig )

from function.rigging.autoRig.bodyRig import hipRig
reload( hipRig )

from function.rigging.autoRig.bodyRig import spineFkRig
reload( spineFkRig )

# # Option of spine Rig
from function.rigging.autoRig.bodyRig import spineRig
reload( spineRig )

from function.rigging.autoRig.bodyRig import neckRig
reload( neckRig )

from function.rigging.autoRig.bodyRig import headRig
reload( headRig )

from function.rigging.autoRig.bodyRig import clavicleRig
reload( clavicleRig )

from function.rigging.autoRig.bodyRig import armRig
reload( armRig )

from function.rigging.autoRig.bodyRig import fingerRig
reload( fingerRig )


from function.rigging.autoRig.bodyRig import finger_mainCurlExec as fingerCurl
reload( fingerCurl )

from function.rigging.autoRig.bodyRig import finger_localCurlExec as finloCurl
reload( finloCurl )

from function.rigging.autoRig.bodyRig import bipedLegRig
reload( bipedLegRig )

from function.rigging.autoRig.bodyRig import ribbonRig
reload( ribbonRig )

from function.rigging.autoRig.bodyRig import propRig
reload( propRig )

from function.rigging.feature import baseFingerSpread as baseFinger
reload(baseFinger)

from function.rigging.autoRig.bodyRig import torsoRig
reload(torsoRig)

from function.rigging.tools import proc as pc 
reload(pc)

from function.rigging.autoRig import util 
reload(util)



import time

#...timeStart
timeStart = time.time()

# Declare some global variables
nameSpace = '' 
ribbon = False
linkRotOrder = True
keepFkIkBoth = False
creTwistJnt = True
showInfo = False
stickShape = 'stick_ctrlShape'

from function.rigging.autoRig.bodyRig import fkIkGenRig
reload( fkIkGenRig )



# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )



# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)




# = = = = = 02 Create hipRig = = = = = #
hip_bJnt = hipRig.hipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale, cogPivot = True   )




'''
# = = = = = 03 Create spine IK Rig  = = = = = #
topSpine_bJnt = torsoRig.torsoRig( 
									nameSpace = nameSpace									,
									ctrl_grp = 'ctrl_grp'							,
									tmpJnt = ( 'spine01_tmpJnt', 'spine02_tmpJnt' )	,
									charScale = charScale 									)

'''



from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
topSpine_bJnt = createFkRig.newCreateFkRig(	nameSpace = ''  ,  name = 'spine' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'spine01_tmpJnt','spine02_tmpJnt', 'spine03_tmpJnt', 'spine04_tmpJnt'   )	,
					charScale = 0.1*charScale	, priorJnt = 'hip_bJnt',priorCtrl = 'cog_ctrl',
					side = '' ,ctrlShape = 'neck_ctrlShape'  , localWorld = True , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt'	)[2][-1]


topSpine_bJnt = topSpine_bJnt.name






# = = = = = 04 Neck Rig = = = = = #
neck_bJnt = neckRig.neckRig(	
							nameSpace = nameSpace 					, 
							parentTo = 'ctrl_grp'  , 
							tmpJnt = (		'neck_tmpJnt' ,'head01_tmpJnt' 	) ,  
							priorJnt = topSpine_bJnt ,
							charScale = charScale	)



# = = = = = 05 HeadRig = = = = = #
headRig.headRig(	
					nameSpace = nameSpace 					, 
					parentTo = 'ctrl_grp'  , 
					tmpJnt = ( 		'head01_tmpJnt' , 'eyeLFT_tmpJnt' , 'eyeRGT_tmpJnt' ,		# head
					'jaw01Lwr_tmpJnt' , 'jaw02Lwr_tmpJnt' , 'jaw03Lwr_tmpJnt' 			,		# jaw
					'jaw01Upr_tmpJnt' , 'jaw02Upr_tmpJnt','eye_tmpJnt' , 
					'eyeTargetLFT_tmpJnt' , 'eyeTargetRGT_tmpJnt'		 				),		# eye			
					faceCtrl = False	,
					priorJnt = neck_bJnt	,
					charScale = charScale	,
					linkRotOrder = True			)








# = = = = = 06 clavicleRig LFT = = = = = #
clavLFT_bJnt = clavicleRig.clavicleRig(		nameSpace = nameSpace 						, 
											parentTo = 'ctrl_grp' 				,
											side = 'LFT'						,
											tmpJnt = ( 	'clavLFT_tmpJnt'  )		,
											priorJnt = topSpine_bJnt 			,
											charScale = charScale )







# = = = = = 06 clavicleRig RGT = = = = = #
clavRGT_bJnt = clavicleRig.clavicleRig(		nameSpace = nameSpace 					, 
										parentTo = 'ctrl_grp' ,
										side = 'RGT',
										tmpJnt = ( 	'clavRGT_tmpJnt'  ),
										priorJnt = topSpine_bJnt	,
										charScale = charScale )





# arm LFT Side
stickNamLFT, handLFT_bJnt= armRig.armRigExt(

				nameSpace = nameSpace 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'LFT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmLFT_tmpJnt' ,	
						'lowerArmLFT_tmpJnt', 	 
						'handLFT_tmpJnt' ,	
						'elbowPovLFT_tmpJnt' ),
				priorJnt = 'clavLFT_bJnt'	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,			
				povShape = 'pyramid',
				keepFkIkBoth = keepFkIkBoth,
				ribbon = ribbon,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = showInfo ,
				linkRotOrder = linkRotOrder )


# = = = = = 08 Create finger LFT = = = = = #	 		
fingerLFT = fingerRig.fingerRigExt( 	
								nameSpace = nameSpace 						,
								side = 'LFT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = handLFT_bJnt ,stickNam = stickNamLFT )

# arm RGT Side
stickNamRGT, handRGT_bJnt= armRig.armRigExt(

				nameSpace = '' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'RGT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmRGT_tmpJnt' ,	
						'lowerArmRGT_tmpJnt', 	 
						'handRGT_tmpJnt' ,	
						'elbowPovRGT_tmpJnt' ),
				priorJnt = 'clavRGT_bJnt'	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,			
				povShape = 'pyramid',
				keepFkIkBoth = keepFkIkBoth,
				ribbon = ribbon,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = showInfo 	,
				linkRotOrder = linkRotOrder )


# Create Finger RGT = = = = = #
fingerRGT = fingerRig.fingerRigExt( 	
								nameSpace = nameSpace 						,
								side = 'RGT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale  ,priorJnt = handRGT_bJnt , stickNam = stickNamRGT )




# = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = nameSpace 	 ,
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'LFT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickNamLFT )

fingerCurl.mainFingerCurlRig( 	nameSpace = nameSpace 	 ,
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'RGT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickNamRGT )















# 10 Local finger curl # = = = = = #
finloCurl.localFingerAllRig( 		nameSpace = nameSpace, parentTo='ctrl_grp' , side = 'LFT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, numCtrl = 3, stickNam = stickNamLFT)


finloCurl.localFingerAllRig( 		nameSpace = nameSpace, parentTo='ctrl_grp' , side = 'RGT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, numCtrl = 3,stickNam = stickNamRGT)

# prop Rig LFT
propRig.propRig(	nameSpace = nameSpace		,
					ctrl_grp =  'ctrl_grp' 		,
					tmpJnt = 'propLFT_tmpJnt' 	,
					charScale = charScale		,
					side = 'LFT'				,
					priorJnt ='handLFT_bJnt'		)

# prop Rig RGT
propRig.propRig(	nameSpace = nameSpace		,
					ctrl_grp =  'ctrl_grp' 		,
					tmpJnt = 'propRGT_tmpJnt' 	,
					charScale = charScale		,
					side = 'RGT'				,
					priorJnt ='handRGT_bJnt'		)


# add base finger spread 
baseFinger.baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadLFT_tmpJnt' , stick = stickNamLFT , fingerGrpNam = fingerLFT )
baseFinger.baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadRGT_tmpJnt' , stick = stickNamRGT , fingerGrpNam = fingerRGT )






























from function.rigging.autoRig.bodyRig import eh_quradrupedLegRig_ext as quRig
reload(quRig)

#from function.rigging.autoRig.bodyRig import quradrupedLegRig as quRig
#reload(quRig)




# = = = = = 11 Leg Back LFT = = = = = #
quRig.quradrupedLegRig(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'LFT'		,	
							region = 'backLeg',		
							tmpJnt = (	'upLegBackLFT_tmpJnt'  , 'midLegBackLFT_tmpJnt' ,  'ankleBackLFT_tmpJnt' , 
										'legPovBackLFT_tmpJnt' ,'ballRollBackLFT_tmpJnt' ,'toeRollBackLFT_tmpJnt' ,
										'heelRollBackLFT_tmpJnt' , 'footOutBackLFT_tmpJnt' , 'footInBackLFT_tmpJnt' , 'lowLegBackLFT_tmpJnt'),
							priorJnt = hip_bJnt ,				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = ribbon	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upBackLeg', 'lwrBackLeg'),	
							charScale = charScale			)	



from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)


out_toe = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'ctrl_grp',
					jntLst = ('L_toeOut01_bJnt',),
					charScale = charScale*0.25, priorJnt = 'ankleBackLFT_bJnt',side = 'LFT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'red', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentCtrlToPriorJnt = True, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)


mid_toe = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'ctrl_grp',
					jntLst = ('L_toeMid01_bJnt',),
					charScale = charScale*0.25, priorJnt = 'ankleBackLFT_bJnt',side = 'LFT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'red', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentCtrlToPriorJnt = True, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)


in_toe = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'ctrl_grp',
					jntLst = ('L_inToe01_bJnt',),
					charScale = charScale*0.25, priorJnt = 'ankleBackLFT_bJnt',side = 'LFT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'red', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentCtrlToPriorJnt = True, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)







# = = = = = 11 Leg Back RGT = = = = = #		
quRig.quradrupedLegRig(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'RGT'		,	
							region = 'backLeg',		
							tmpJnt = (	'upLegBackRGT_tmpJnt'  , 'midLegBackRGT_tmpJnt' ,  'ankleBackRGT_tmpJnt' , 
										'legPovBackRGT_tmpJnt' ,'ballRollBackRGT_tmpJnt' ,'toeRollBackRGT_tmpJnt' ,
										'heelRollBackRGT_tmpJnt' , 'footOutBackRGT_tmpJnt' , 'footInBackRGT_tmpJnt' , 'lowLegBackRGT_tmpJnt'),
							priorJnt = hip_bJnt ,				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = ribbon	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upBackLeg', 'lwrBackLeg'),	
							charScale = charScale		)	




out_toe = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'ctrl_grp',
					jntLst = ('R_toeOut01_bJnt',),
					charScale = charScale*0.25, priorJnt = 'ankleBackRGT_bJnt',side = 'RGT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'blue', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentCtrlToPriorJnt = True, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)


mid_toe = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'ctrl_grp',
					jntLst = ('R_toeMid01_bJnt',),
					charScale = charScale*0.25, priorJnt = 'ankleBackRGT_bJnt',side = 'RGT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'blue', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentCtrlToPriorJnt = True, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)


in_toe = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'ctrl_grp',
					jntLst = ('R_inToe01_bJnt',),
					charScale = charScale*0.25, priorJnt = 'ankleBackRGT_bJnt',side = 'RGT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'blue', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentCtrlToPriorJnt = True, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)















# add space switch
rigTools.addSpace(  nameSpace = '',	giveStick =  stickNamLFT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', neck_bJnt, topSpine_bJnt, hip_bJnt ] )
rigTools.addSpace(  nameSpace = '',	giveStick =  stickNamRGT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', neck_bJnt, topSpine_bJnt, hip_bJnt ] )



















#.... ADDITIONAL arm and leg at the head



# = = = = = 06 clavicleRig LFT = = = = = #
clavUprLFT_bJnt = clavicleRig.clavicleRig(		nameSpace = 'upr' , 
										parentTo = 'ctrl_grp' ,
										side = 'LFT',
										tmpJnt = ( 	'uprclavLFT_tmpJnt'  ),
										priorJnt = 'head01_bJnt'	,
										charScale = charScale )


#... I know it wired but put namespace + joint in maya scene  Ex 'uprupperArmLFT_tmpJnt'
#... but in arg just joint name without namespace

from function.rigging.autoRig.bodyRig import armRig
reload(armRig)

#... hand LFT Side
stickHHandLFT, HhandLFT_bJnt= armRig.armRigExt(

				nameSpace = 'upr' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'LFT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmLFT_tmpJnt' ,	
						'lowerArmLFT_tmpJnt', 	 
						'handLFT_tmpJnt' ,	
						'elbowPovLFT_tmpJnt' ),
				priorJnt = clavUprLFT_bJnt	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,			
				povShape = 'sphereAxis',
				keepFkIkBoth = False,
				ribbon = False,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = False )
				
				
# LOWER ARM # = = = = = 08 Create finger LFT = = = = = #
	
from function.rigging.autoRig.bodyRig import fingerRig
reload( fingerRig )

handLwrLFT = fingerRig.fingerRigExt( 	
								nameSpace = 'upr' ,
								side = 'LFT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = HhandLFT_bJnt ,stickNam = stickHHandLFT )
								#charScale= charScale, stickNam = stickNamLFT)

# = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = 'upr' 	 ,
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'LFT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickHHandLFT )
# 10 Local finger curl # = = = = = #
finloCurl.localFingerAllRig( 		nameSpace = 'upr', parentTo='ctrl_grp' , side = 'LFT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, numCtrl = 3, stickNam = stickHHandLFT)



from function.rigging.autoRig.bodyRig import fkIkTwistGenRig as fkg
reload(fkg)
fkg.fkIkTwistGenRig(

				nameSpace = 'upB' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'LFT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperLegLFT_tmpJnt' ,	
						'lowerLegLFT_tmpJnt', 	 
						'ankleLFT_tmpJnt' ,	
						'legPovLFT_tmpJnt' ),
				priorJnt = clavUprLFT_bJnt	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,
				showInfo = False ,
				ribbon = False,	
				ribbonRes = 'low',
				ribbonName = ('upLeg', 'lwrLeg'),
				propCtrl = False,
				keepFkIkBoth = False,	
				povShape = 'sphereAxis',
				ikPosi = None ,
				linkRotOrder = True ,
				ctrlShape = 'fk_ctrlShape', #... ctrl shape for fk ctrl only
				creTwistJnt = True ,
				stickShape = 'stickCircle_Y_long_ctrlShape',
				alongAxis = 'y' ,
				pinMethod = 'matrix',
				povPosi = 'front'
				)


from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)

#... brach at head
L_branchA = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'head01_gmbCtrl',
					jntLst = ('L_uprBranchA01_bJnt','L_uprBranchA02_bJnt', 'L_uprBranchA03_bJnt','L_uprBranchA04_bJnt'),
					charScale = charScale*0.25, priorJnt = 'head01_bJnt',side = 'LFT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'blue', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentToPriorJnt = False, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)

L_branchB = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'head01_gmbCtrl',
					jntLst = ('L_uprBranchB01_bJnt','L_uprBranchB02_bJnt', 'L_uprBranchB03_bJnt','L_uprBranchB04_bJnt'),
					charScale = charScale*0.25, priorJnt = 'head01_bJnt',side = 'LFT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'blue', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentToPriorJnt = False, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)









					

# = = = = = 06 clavicleRig RGT = = = = = #
clavUprRGT_bJnt = clavicleRig.clavicleRig(		nameSpace = 'upr' , 
										parentTo = 'ctrl_grp' ,
										side = 'RGT',
										tmpJnt = ( 	'uprclavRGT_tmpJnt'  ),
										priorJnt = 'head01_bJnt'	,
										charScale = charScale )


#... I know it wired but put namespace + joint in maya scene  Ex 'uprupperArmLFT_tmpJnt'
#... but in arg just joint name without namespace

from function.rigging.autoRig.bodyRig import armRig
reload(armRig)

#... hand RGT Side
stickHHandRGT, HhandRGT_bJnt= armRig.armRigExt(

				nameSpace = 'upr' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'RGT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmRGT_tmpJnt' ,	
						'lowerArmRGT_tmpJnt', 	 
						'handRGT_tmpJnt' ,	
						'elbowPovRGT_tmpJnt' ),
				priorJnt = clavUprRGT_bJnt	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,			
				povShape = 'sphereAxis',
				keepFkIkBoth = False,
				ribbon = False,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = False )
				
				
# LOWER ARM # = = = = = 08 Create finger RGT = = = = = #
	
from function.rigging.autoRig.bodyRig import fingerRig
reload( fingerRig )

handLwrRGT = fingerRig.fingerRigExt( 	
								nameSpace = 'upr' ,
								side = 'RGT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = HhandRGT_bJnt ,stickNam = stickHHandRGT )
								#charScale= charScale, stickNam = stickNamRGT)

# = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = 'upr' 	 ,
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'RGT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickHHandRGT )
# 10 Local finger curl # = = = = = #
finloCurl.localFingerAllRig( 		nameSpace = 'upr', parentTo='ctrl_grp' , side = 'RGT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, numCtrl = 3, stickNam = stickHHandRGT)



from function.rigging.autoRig.bodyRig import fkIkTwistGenRig as fkg
reload(fkg)
fkg.fkIkTwistGenRig(

				nameSpace = 'upB' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'RGT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperLegRGT_tmpJnt' ,	
						'lowerLegRGT_tmpJnt', 	 
						'ankleRGT_tmpJnt' ,	
						'legPovRGT_tmpJnt' ),
				priorJnt = clavUprRGT_bJnt	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,
				showInfo = False ,
				ribbon = False,	
				ribbonRes = 'low',
				ribbonName = ('upLeg', 'lwrLeg'),
				propCtrl = False,
				keepFkIkBoth = False,	
				povShape = 'sphereAxis',
				ikPosi = None ,
				linkRotOrder = True ,
				ctrlShape = 'fk_ctrlShape', #... ctrl shape for fk ctrl only
				creTwistJnt = True ,
				stickShape = 'stickCircle_Y_long_ctrlShape',
				alongAxis = 'y' ,
				pinMethod = 'matrix',
				povPosi = 'front'
				)


from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)

#... brach at head
R_branchA = createFkRig.fkRig_omni_newCurl( nameSpace = nameSpace, parentCtrlTo = 'head01_gmbCtrl',
					jntLst = ('R_uprBranchA01_bJnt','R_uprBranchA02_bJnt', 'R_uprBranchA03_bJnt','R_uprBranchA04_bJnt'),
					charScale = charScale*0.25, priorJnt = 'head01_bJnt',side = 'R',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'red', curlCtrl = False, curlPosiAtFirst = True, rotateOrder = 'zxy',
					parentToPriorJnt = False, parentMatrix = False,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = False)





# Lock attr
util.cleanup()
