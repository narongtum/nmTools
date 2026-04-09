# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # #
# Autorig with following feature
# # # # # # # # # # # # # # # #

# stretchy IK
# auto upper arm/leg twist
# Fk/Ik switch
# kneelock
# ribbon limb (option)
# head clavicle local world
# finger curl
# arm space snaping
# foot roll behavior


import maya.cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import rigTools
reload(rigTools)

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

# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )

#charScale = 1

# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(charScale = charScale)



# = = = = = 02 Create hipRig = = = = = #
from function.rigging.autoRig.components import eh_hipRig as hipRig
reload(hipRig)
hip_bJnt = hipRig.createHipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale, cogPivot = True)






# = = = = = 03 Create spine FK Rig  = = = = = #
from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)




topSpine_bJnt = createFkRig.fkRig_omni_newCurl( nameSpace = '', parentCtrlTo = 'cog_gmbCtrl',
					jntLst = ( 'spine01_tmpJnt','spine02_tmpJnt', 'spine03_tmpJnt'),
					charScale = charScale, priorJnt = 'hip_bJnt',side = '',
					ctrlShape = 'circle_ctrlShape', localWorld = True ,
					color = 'yellow', curlCtrl = True, rotateOrder = 'zxy',
					parentToPriorJnt = False,
					parentCtrlToPriorJnt = True, parentMatrix = True,
					curlCtrlShape = 'circle_ctrlShape', constraintCurl = True,
					isTmpJnt = True, suffix = '_bJnt')[2][0]





# = = = = = 04 Neck Rig = = = = = #
from function.rigging.autoRig.components import eh_neckRig as neckRig
reload(neckRig)

neck_bJnt = neckRig.createNeckRig(
		nameSpace='',
		parentTo='ctrl_grp',
		priorCtrl = 'spine03_gmbCtrl',
		priorJnt='spine03_bJnt', # Should be the top spine joint or chest
		tmpJnt='neck_tmpJnt',    # Single joint input
		ctrl_shape = 'circle_ctrlShape',
		charScale=charScale,
		linkRotOrder=linkRotOrder)




# = = = = = 05 HeadRig = = = = = #
from function.rigging.autoRig.components import eh_headRig as headRig
reload(headRig)
headRig.createHeadRig(	
					nameSpace = nameSpace 					, 
					parentTo = 'ctrl_grp'  , 
					tmpJnt = ( 		'head01_tmpJnt' , 'eyeLFT_tmpJnt' , 'eyeRGT_tmpJnt' ,		# head
					'jaw01Lwr_tmpJnt' , 'jaw02Lwr_tmpJnt' , 'jaw03Lwr_tmpJnt' 			,		# jaw
					'jaw01Upr_tmpJnt' , 'jaw02Upr_tmpJnt','eye_tmpJnt' , 
					'eyeTargetLFT_tmpJnt' , 'eyeTargetRGT_tmpJnt'		 				),		# eye			
					faceCtrl = True	,
					priorJnt = neck_bJnt[1][0]	,
					charScale = charScale	,
					ctrlShape = 'circle_ctrlShape',
					priorCtrl ='neck_gmbCtrl',
					linkRotOrder = linkRotOrder			)




# = = = = = 05 HeadRig = = = = = #
from function.rigging.autoRig.components import eh_clavicleRig as clavicleRig
reload(clavicleRig)

clavLFT_bJnt = clavicleRig.createClavicleRig(
		nameSpace='',
		side='LFT',
		parentTo = 'ctrl_grp',
		priorCtrl='ctrl_grp',
		priorJnt='spine03_bJnt', # Should be the top spine joint
		tmpJnt='clavLFT_tmpJnt',
		charScale=charScale
	)



clavRGT_bJnt = clavicleRig.createClavicleRig(
		nameSpace='',
		side='RGT',
		parentTo = 'ctrl_grp',
		priorCtrl='ctrl_grp',
		priorJnt='spine03_bJnt', # Should be the top spine joint
		tmpJnt='clavRGT_tmpJnt',
		charScale=charScale
	)



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

				nameSpace = '' 	,				
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
				linkRotOrder = linkRotOrder	,
				stickShape = stickShape 	,
				creTwistJnt = creTwistJnt		
				 )


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
				linkRotOrder = linkRotOrder	,
				stickShape = stickShape 	,
				creTwistJnt = creTwistJnt		
				 )


# Create Finger RGT = = = = = #
fingerRGT = fingerRig.fingerRigExt( 	
								nameSpace = nameSpace 						,
								side = 'RGT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale  ,priorJnt = handRGT_bJnt , stickNam = stickNamRGT )




# = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = nameSpace 	 ,
								fingerName = ('thumb','index','middle','ring','pinky') , 
								# fingerName = ('thumb','index','middle','ring') , 
								side = 'LFT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickNamLFT )

fingerCurl.mainFingerCurlRig( 	nameSpace = nameSpace 	 ,
								fingerName = ('thumb','index','middle','ring','pinky') , 
								# fingerName = ('thumb','index','middle','ring') , 
								side = 'RGT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickNamRGT )







# 10 Local finger curl # = = = = = #
finloCurl.localFingerAllRig( 		nameSpace = nameSpace, parentTo='ctrl_grp' , side = 'LFT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, numCtrl = 3, stickNam = stickNamLFT)


finloCurl.localFingerAllRig( 		nameSpace = nameSpace, parentTo='ctrl_grp' , side = 'RGT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, numCtrl = 3,stickNam = stickNamRGT)





# add base finger spread 
baseFinger.baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadLFT_tmpJnt' , stick = stickNamLFT , fingerGrpNam = fingerLFT, fingerGrp = ['index', 'middle', 'ring'] )
baseFinger.baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadRGT_tmpJnt' , stick = stickNamRGT , fingerGrpNam = fingerRGT, fingerGrp = ['index', 'middle', 'ring'] )








# 11 Leg LFT
bipedLegRig.bipedLegRigExt(
					nameSpace = '' 	,	
					parentTo = 'ctrl_grp' ,			
					side = 'LFT'	,				
					region = 'leg',
					tmpJnt = (	'upperLegLFT_tmpJnt'  , 'lowerLegLFT_tmpJnt' ,  'ankleLFT_tmpJnt' , 
								'kneePovLFT_tmpJnt' ,'ballLFT_tmpJnt' ,'toesTipLFT_tmpJnt' ,
								'heelRollLFT_tmpJnt' , 'footOutLFT_tmpJnt' , 'footInLFT_tmpJnt'),
					priorJnt = 'hip_bJnt'	,			
					ikhGrp = 'ikh_grp' 	,				
					noTouchGrp = 'noTouch_grp' 	,		
					nullGrp = 'snapNull_grp'	,		
					showInfo = showInfo  ,					
					ribbon = ribbon	,				
					ribbonRes = 'low'	,				
					ribbonName = ('upLeg', 'lwrLeg'),	
					charScale = charScale	,					
					ikPosi = 'foot', # get only 2 variable 'foot' or 'ankle'
					keepFkIkBoth = keepFkIkBoth	,# keep fk/ik ctrl visibility both or not
					povShape = 'pyramid' ,# choice pyramid or sphereAxis
					jnt_grp = 'jnt_grp' ,
					linkRotOrder = linkRotOrder	,
					footAttr = True,
					stickShape = stickShape 	,
					creTwistJnt = creTwistJnt		
					 )


# 11 Leg RGT

bipedLegRig.bipedLegRigExt(
					nameSpace = '' 	,	
					parentTo = 'ctrl_grp' ,			
					side = 'RGT'	,				
					region = 'leg',
					tmpJnt = (	'upperLegRGT_tmpJnt'  , 'lowerLegRGT_tmpJnt' ,  'ankleRGT_tmpJnt' , 
								'kneePovRGT_tmpJnt' ,'ballRGT_tmpJnt' ,'toesTipRGT_tmpJnt' ,
								'heelRollRGT_tmpJnt' , 'footOutRGT_tmpJnt' , 'footInRGT_tmpJnt'),
					priorJnt = 'hip_bJnt'	,			
					ikhGrp = 'ikh_grp' 	,				
					noTouchGrp = 'noTouch_grp' 	,		
					nullGrp = 'snapNull_grp'	,		
					showInfo = showInfo  ,					
					ribbon = ribbon	,				
					ribbonRes = 'low'	,				
					ribbonName = ('upLeg', 'lwrLeg'),	
					charScale = charScale	,					
					ikPosi = 'foot', # get only 2 variable 'foot' or 'ankle'
					keepFkIkBoth = keepFkIkBoth	,# keep fk/ik ctrl visibility both or not
					povShape = 'pyramid' ,# choice pyramid or sphereAxis
					jnt_grp = 'jnt_grp' ,
					linkRotOrder = linkRotOrder	,
					footAttr = True 			,
					stickShape = stickShape 	,
					creTwistJnt = creTwistJnt		
					 )


# add space switch
rigTools.addSpace(  nameSpace = '',	giveStick =  stickNamLFT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', neck_bJnt, topSpine_bJnt, hip_bJnt ] )
rigTools.addSpace(  nameSpace = '',	giveStick =  stickNamRGT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', neck_bJnt, topSpine_bJnt, hip_bJnt ] )


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



# Lock attr
util.cleanup()







#...timeEnd
timeEnd = time.time()
timeElapsed = timeEnd-timeStart

roundedTimeElapsed = round(timeElapsed, 1)

#...print time
print('SaveData Elapsed: %s'%roundedTimeElapsed)







# # # # # # # # # # # # # # # # # # # # # # # #
# Additional Rig    
# # # # # # # # # # # # # # # # # # # # # # # #






from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)


createFkRig.fkRig_omni_newCurl( nameSpace = '', parentCtrlTo = 'hip_gmbCtrl',
					jntLst = ('loinclothFRT001_bJnt','loinclothFRT002_bJnt', 'loinclothFRT003_bJnt', 'loinclothFRT004_bJnt'),
					charScale = charScale, priorJnt = 'hip_bJnt',side = '',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = True, curlPosiAtFirst = False, rotateOrder = 'zxy',
					parentToPriorJnt = True, parentMatrix = True,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = True)




createFkRig.fkRig_omni_newCurl( nameSpace = '', parentCtrlTo = 'hip_gmbCtrl',
					jntLst = ('loinclothBCK001_bJnt','loinclothBCK002_bJnt', 'loinclothBCK003_bJnt', 'loinclothBCK004_bJnt'),
					charScale = charScale, priorJnt = 'hip_bJnt',side = '',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = True, curlPosiAtFirst = False, rotateOrder = 'zxy',
					parentToPriorJnt = True, parentMatrix = True,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = True)