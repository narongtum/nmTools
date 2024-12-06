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
stickShape = 'stick_ctrlShape'
povShape = 'sphereAxis'

# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )

charScale = 1

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
					tmpJnt = 	( 	'spine01_tmpJnt','spine02_tmpJnt', 'spine03_tmpJnt'   )	,
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
					ctrlShape = 'plainSphereB_ctrlShape',
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




# = = = = = Arm LFT Side = = = = = #
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
				povShape = povShape,
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

# = = = = = Arm RGT Side
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
				povShape = povShape,
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







# # # # # # # # # # # # # # # # # # # # # # # #
# Additional Rig    
# # # # # # # # # # # # # # # # # # # # # # # #





"""
from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)



#... Breast 
createFkRig.fkMulChild(	nameSpace = ''  ,  name = 'breast' , parentTo = 'ctrl_grp'  ,
						tmpJnt = (  'breast_bJnt' , ['breastLFT_bJnt'] , ['breastRGT_bJnt'] 	)		,
						charScale = 1	, 
						priorJnt = 'spine02_bJnt' 							,
						side = '' ,ctrlShape = 'circle_ctrlShape' 	 	, 
						color = 'red' , 
						curlCtrl = False	)




#... Hair Left
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairRear' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairRear01LFT_bJnt', 'hairRear02LFT_bJnt', 'hairRear03LFT_bJnt')	,
					charScale = 0.75, priorJnt = 'head01_bJnt'  ,
					side = 'LFT', ctrlShape = 'circle_ctrlShape', localWorld = True , 
					color = 'red', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,curlCtrlShape = 'sphereRound_ctrlShape')
					
					
#... Hair Right
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairRear' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairRear01RGT_bJnt', 'hairRear02RGT_bJnt', 'hairRear03RGT_bJnt')	,
					charScale = 0.75, priorJnt = 'head01_bJnt'  ,
					side = 'RGT', ctrlShape = 'circle_ctrlShape', localWorld = True , 
					color = 'red', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,curlCtrlShape = 'sphereRound_ctrlShape')

#... Hair Front
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairFRT' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairFRT01_bJnt', 'hairFRT02_bJnt')	,
					charScale = 0.75, priorJnt = 'head01_bJnt'  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = True , 
					color = 'red', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,curlCtrlShape = 'sphereRound_ctrlShape')
					
					
					
#... Jacket
createFkRig.fkMulChild(	nameSpace = ''  ,  name = 'jacket' , parentTo = 'jacketCtrl_grp'  ,
						tmpJnt = (  	'jacket_rtJnt', ['jacketA01_tmpJnt','jacketA02_tmpJnt'], ['jacketB01_tmpJnt','jacketB02_tmpJnt'],
										['jacketC01_tmpJnt','jacketC02_tmpJnt'] , ['jacketD01_tmpJnt','jacketD02_tmpJnt'] , ['jacketE01_tmpJnt','jacketE02_tmpJnt'],
										['jacketF01_tmpJnt','jacketF02_tmpJnt']	)		,
						charScale = 1	, 
						priorJnt = 'spine01_jnt' 							,
						side = '' ,ctrlShape = 'circle_ctrlShape' 	 	, 
						color = 'red' , 
						curlCtrl = True	)	"""





'''
#... lineA

from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)

createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'lineA' , parentTo = 'hip_gmbCtrl' ,
					tmpJnt = 	( 'lineA01_tmpJnt', 'lineA02_tmpJnt', 'lineA03_tmpJnt')	,
					charScale = 0.25, priorJnt = 'hip_bJnt' ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = True, useParentInstead = True)



createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'lineB' , parentTo = 'hip_gmbCtrl' ,
					tmpJnt = 	( 'lineB01_bJnt', 'lineB02_bJnt', 'lineB03_bJnt')	,
					charScale = 0.25, priorJnt = 'hip_bJnt'  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)












#... hair
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairC' , parentTo = 'rootHair_gmbCtrl' ,
					tmpJnt = 	( 'hairC01_bJnt', 'hairC02_bJnt', 'hairC03_bJnt', 'hairC06_bJnt', 'hairC07_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)







createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairE' , parentTo = 'rootHair_gmbCtrl' ,
					tmpJnt = 	( 'hairE01_bJnt', 'hairE02_bJnt', 'hairE03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)






#...RGT side C
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairH' , parentTo = 'rootHair_gmbCtrl' ,
					tmpJnt = 	( 'hairH01_bJnt', 'hairH02_bJnt', 'hairH03_bJnt', 'hairH07_bJnt', 'hairH08_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)






######################################################## overhaul Rig
from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)

#...RGT side B HairI
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairI' , parentTo = 'rootHair_bJnt' ,
					tmpJnt = 	( 'hairI01_bJnt', 'hairI02_bJnt', 'hairI03_bJnt', 'hairI06_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True, priorCtrl = 'mainSub_grp',curlCtrlShape = 'circle_ctrlShape' )



#... hairB overhaul
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairB' , parentTo = '' ,
					tmpJnt = 	( 'hairB01_bJnt', 'hairB02_bJnt', 'hairB03_bJnt', 'hairB06_bJnt')	,
					charScale = 1, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True, 
					priorCtrl = 'mainSub_grp',curlCtrlShape = 'circle_ctrlShape')







createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairD' , parentTo = '' ,
					tmpJnt = 	( 'hairD01_bJnt', 'hairD02_bJnt', 'hairD03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,
					priorCtrl = 'mainSub_grp',curlCtrlShape = 'circle_ctrlShape')

#...hair G
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairG' , parentTo = '' ,
					tmpJnt = 	( 'hairG01_bJnt', 'hairG02_bJnt', 'hairG03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,
					priorCtrl = 'mainSub_grp',curlCtrlShape = 'circle_ctrlShape')



createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairE' , parentTo = '' ,
					tmpJnt = 	( 'hairE01_bJnt', 'hairE02_bJnt', 'hairE03_bJnt','hairE04_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,
					priorCtrl = 'mainSub_grp',curlCtrlShape = 'circle_ctrlShape')


#...RGT side E
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairF' , parentTo = '' ,
					tmpJnt = 	( 'hairF01_bJnt', 'hairF02_bJnt', 'hairF03_bJnt','hairF04_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True,
					priorCtrl = 'mainSub_grp',curlCtrlShape = 'circle_ctrlShape')









#...RGT side A
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairJ' , parentTo = 'rootHair_gmbCtrl' ,
					tmpJnt = 	( 'hairJ01_bJnt', 'hairJ02_bJnt', 'hairJ03_bJnt', 'hairJ06_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)







from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
#... front hair





createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairFRTA' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairFRTA01_bJnt', 'hairFRTA02_bJnt', 'hairFRTA03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)


createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairFRTB' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairFRTB01_bJnt', 'hairFRTB02_bJnt','hairFRTB03_bJnt', 'hairFRTB04_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)



createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairFRTC' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairFRTC01_bJnt', 'hairFRTC02_bJnt', 'hairFRTC03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)



createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairFRTD' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairFRTD01_bJnt', 'hairFRTD02_bJnt', 'hairFRTD03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)
					
					
					
					
createFkRig.fkRig_newCurl(	nameSpace = '' , name = 'hairFRTE' , parentTo = 'head01_gmbCtrl' ,
					tmpJnt = 	( 'hairFRTE01_bJnt', 'hairFRTE02_bJnt', 'hairFRTE03_bJnt')	,
					charScale = 0.5, priorJnt = ''  ,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'yellow', curlCtrl = True, suffix = '_bJnt', rotateOrder = 'zxy' ,
					isTmpJnt = False, useParentInstead = True)					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
######################################################## not define zone ###########################################################

#... hair face rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairFRTB' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairB01FRT_tmpJnt', 'hairB02FRT_tmpJnt', 'hairB03FRT_tmpJnt', 'hairB04FRT_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'head01_bJnt' 			,
					side = '' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = None , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)

#... hair face rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairFRTA' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairA01FRT_tmpJnt', 'hairA02FRT_tmpJnt', 'hairA03FRT_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'head01_bJnt' 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = None , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)


#... hair forehead rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairCFRT' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairC01FRT_tmpJnt', 'hairC02FRT_tmpJnt', 'hairC03FRT_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'head01_bJnt' 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)


from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
#... hair forehead rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairDFRT' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairD01FRT_tmpJnt', 'hairD02FRT_tmpJnt', 'hairD03FRT_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'head01_bJnt' 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)





#... hair forehead rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairABCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairA01BCK_tmpJnt', 'hairA02BCK_tmpJnt', 'hairA03BCK_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'head01_bJnt' 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)



from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

hair_bck_root= ['brushHair_bJnt']

hair_bck_rig = adjust.creControllerFunc(	hair_bck_root ,scale = 1, ctrlShape = 'circle_ctrlShape',color = 'yellow'	)


mc.parent(hair_bck_rig[0], 'head01_gmbCtrl')



#...back hair
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairBBCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairH01BCK_tmpJnt', 'hairH02BCK_tmpJnt', 'hairH03BCK_tmpJnt')	,
					charScale = 0.25	, priorJnt = hair_bck_root[0] 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)


createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairFBCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairF01BCK_tmpJnt', 'hairF02BCK_tmpJnt', 'hairF03BCK_tmpJnt')	,
					charScale = 0.25	, priorJnt = hair_bck_root[0] 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)


hairG01BCK_rig = adjust.creControllerFunc(	['hairG01BCK_tmpJnt'] ,scale = 1, ctrlShape = 'circle_ctrlShape',color = 'yellow'	)
mc.parent(hairG01BCK_rig[0], 'brushHair_gmbCtrl')


createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairEBCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairE01BCK_tmpJnt', 'hairE02BCK_tmpJnt', 'hairE03BCK_tmpJnt')	,
					charScale = 0.25	, priorJnt = hair_bck_root[0] 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)
					
					
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairDBCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairD01BCK_tmpJnt', 'hairD02BCK_tmpJnt', 'hairD03BCK_tmpJnt')	,
					charScale = 0.25	, priorJnt = hair_bck_root[0] 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)					
					
					
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairIBCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairI01BCK_tmpJnt', 'hairI02BCK_tmpJnt', 'hairI03BCK_tmpJnt')	,
					charScale = 0.25	, priorJnt = hair_bck_root[0] 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)		


					
					
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'hairJBCK' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'hairJ01BCK_tmpJnt', 'hairJ02BCK_tmpJnt', 'hairJ03BCK_tmpJnt')	,
					charScale = 0.5	, priorJnt = hair_bck_root[0] 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True, isTmpJnt = True	)						
					





#... ear rig
createFkRig.newCreateFkRig(	nameSpace = '' , name = 'ear' , parentTo = 'ctrl_grp' ,
					tmpJnt = 	['ear01LFT_tmpJnt']	,
					charScale = charScale, priorJnt = 'head01_bJnt' 			,
					side = 'LFT', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = None, curlCtrl = False, suffix = '_bJnt', useHierarchy = True	)

#... ear rig
createFkRig.newCreateFkRig(	nameSpace = '' , name = 'ear' , parentTo = 'ctrl_grp' ,
					tmpJnt = 	['ear01RGT_tmpJnt']	,
					charScale = charScale, priorJnt = 'head01_bJnt' 			,
					side = 'RGT', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = None, curlCtrl = False, suffix = '_bJnt', useHierarchy = True	)






#...wing rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'wingLFT' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'wing01LFT_tmpJnt', 'wing02LFT_tmpJnt', 'wing03LFT_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'spine02_bJnt' 			,
					side = '' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)	


#...wing rig
createFkRig.fkRig_newCurl(	nameSpace = ''  ,  name = 'wingRGT' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'wing01RGT_tmpJnt', 'wing02RGT_tmpJnt', 'wing03RGT_tmpJnt')	,
					charScale = 0.5	, priorJnt = 'spine02_bJnt' 			,
					side = 'RGT' , ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt' , useHierarchy = True	)	



from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
#... breasts
createFkRig.createFkRig_direct(	nameSpace = ''  ,  name = 'breast' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	 ['breast_bJnt']	,
					charScale = 1	, priorJnt = 'spine02_bJnt' 			,
					side = '' ,ctrlShape = 'stick_ctrlShape'  , localWorld = False , 
					color = 'yellow' , curlCtrl = False, suffix = '_bJnt', parentToPriorJnt = False,
					parentMatrix = False, rotateOrder = 'xzy')



from function.rigging.autoRig.addRig import pinLocatorToSurfac as pls
reload(pls)



pls.pin_locator_surface(	# need pxy nrb to drive locator
							nurbs = 'L_eyebrow_nrb',
							region = 'eyebrow',
							side = 'LFT',
							source_loc = ('eyebrow01LFT_loc','eyebrow02LFT_loc','eyebrow03LFT_loc'),
							locator_scale = 1,
							creJnt = True , suffixJnt = 'bJnt',
							creCtrl = True , ctrlShape = 'square_ctrlShape',
							snapAtEnd = False,
							priorJnt = 'head01_bJnt',
							scale = 2
							)
							
							
pls.pin_locator_surface(	# need pxy nrb to drive locator
							nurbs = 'R_eyebrow_nrb',
							region = 'eyebrow',
							side = 'RGT',
							source_loc = ('eyebrow01RGT_loc','eyebrow02RGT_loc','eyebrow03RGT_loc'),
							locator_scale = 1,
							creJnt = True , suffixJnt = 'bJnt',
							creCtrl = True , ctrlShape = 'squarePlain_ctrlShape',
							snapAtEnd = False,
							priorJnt = 'head01_bJnt',
							scale = 1
							)
							
							
							
							
							
from function.rigging.util import misc
reload(misc)							
							
this = misc.check_name_style(name = 'ahahaLFT_nrb')



'''