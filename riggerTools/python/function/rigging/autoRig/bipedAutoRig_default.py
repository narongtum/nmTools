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

# change module name please update
from function.rigging.autoRig.bodyRig import finger_mainCurlExec as fingerCurl
reload( fingerCurl )
# change module name please update
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
stickShape = 'stickCircle_Y_long_ctrlShape'

# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )

# charScale = 1

# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)



# = = = = = 02 Create hipRig = = = = = #
hip_bJnt = hipRig.hipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale, cogPivot = True   )






# = = = = = 03 Create spine FK Rig  = = = = = #


from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
topSpine_bJnt = createFkRig.newCreateFkRig(	nameSpace = ''  ,  name = 'spine' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'spine01_tmpJnt','spine02_tmpJnt','spine03_tmpJnt' )	,
					charScale = charScale	, priorJnt = 'hip_bJnt',priorCtrl = 'cog_ctrl',
					side = '' ,ctrlShape = 'circle_ctrlShape'  , localWorld = True , 
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
					faceCtrl = True	,
					priorJnt = neck_bJnt	,
					charScale = charScale	,
					ctrlShape = 'sphereRound_ctrlShape',
					linkRotOrder = linkRotOrder			)









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
stickNamLFT, handLFT_bJnt, handLFT_meta = armRig.armRigExt(

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
stickNamRGT, handRGT_bJnt, handRGT_meta= armRig.armRigExt(

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
				povShape = 'sphereAxis',
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





# add base finger spread 
baseFinger.baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadLFT_tmpJnt' , stick = stickNamLFT , fingerGrpNam = fingerLFT )
baseFinger.baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadRGT_tmpJnt' , stick = stickNamRGT , fingerGrpNam = fingerRGT )








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





# # # # # # # # # # # #
# Additional Rig      #
# # # # # # # # # # # #

from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)



#... ear

createFkRig.fkRig_new_curl_ext(	nameSpace = '', parentCtrlTo = 'head01_gmbCtrl',
					jntLst = ('L_ear01_bJnt',),
					charScale = 1, priorJnt = 'head01_bJnt',side = 'L',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = False, rotateOrder = 'zxy',
					curlCtrlShape = 'stick_tri02_ctrlShape')

createFkRig.fkRig_new_curl_ext(	nameSpace = '', parentCtrlTo = 'head01_gmbCtrl',
					jntLst = ('R_ear01_bJnt',),
					charScale = 1, priorJnt = 'head01_bJnt',side = 'R',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = False, rotateOrder = 'zxy',
					curlCtrlShape = 'stick_tri02_ctrlShape')
