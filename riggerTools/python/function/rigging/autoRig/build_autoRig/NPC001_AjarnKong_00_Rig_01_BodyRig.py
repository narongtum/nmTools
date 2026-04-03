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





# import time

#...timeStart
# timeStart = time.time()

#... Declare some global variables
nameSpace = '' 
ribbon = False
linkRotOrder = True
keepFkIkBoth = False
creTwistJnt = True
showInfo = False
stickShape = 'stick_ctrlShape'
povShape = 'sphereAxis'

# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head01_tmpJnt' )


# = = = = = 01 Create main Controller = = = = = #
from function.rigging.autoRig.components import eh_rootRig as rootRig
reload(rootRig)
rootRig.createMasterGrp(charScale = charScale)



# = = = = = 02 Create hipRig = = = = = #
from function.rigging.autoRig.components import eh_hipRig as hipRig
reload(hipRig)
hip_bJnt = hipRig.createHipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale, cogPivot = True   )






# = = = = = 03 Create spine FK Rig  = = = = = #
from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
topSpine_bJnt = createFkRig.newCreateFkRig(	nameSpace = ''  ,  name = 'spine' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'spine01_tmpJnt',)	,
					charScale = charScale	, priorJnt = 'hip_bJnt',priorCtrl = 'cog_ctrl',
					side = '' ,ctrlShape = 'circle_ctrlShape'  , localWorld = True , 
					color = 'yellow' , curlCtrl = False ,suffix = '_bJnt'	)[2][-1]



# # = = = = = 04 Neck Rig = = = = = #
# neck_bJnt = neckRig.neckRig(	
# 							nameSpace = nameSpace 					, 
# 							parentTo = 'ctrl_grp'  , 
# 							tmpJnt = (		'neck_tmpJnt' ,'head01_tmpJnt' 	) ,  
# 							priorJnt = topSpine_bJnt ,
# 							charScale = charScale	)




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
					faceCtrl = False	,
					priorJnt = topSpine_bJnt.name	,
					charScale = charScale	,
					ctrlShape = 'circle_ctrlShape',
					priorCtrl ='spine01_gmbCtrl',
					linkRotOrder = linkRotOrder			)




# = = = = = 06 arm LFT Side
from function.rigging.autoRig.components import eh_armRigR15 as armRig
reload(armRig)

#... right arm side
stickNamRGT, handRGT_bJnt= armRig.eh_armRigExtR15(

				nameSpace = '' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'RGT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmRGT_tmpJnt' ,	
						'lowerArmRGT_tmpJnt', 	 
						'handRGT_tmpJnt' ,	
						'elbowPovRGT_tmpJnt' ),
				priorJnt = topSpine_bJnt.name	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,						
				jnt_grp =  'jnt_grp'	,			
				povShape = 'pyramid',
				keepFkIkBoth = keepFkIkBoth,
				ribbon = ribbon,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = showInfo ,
				linkRotOrder = linkRotOrder	,
				stickShape = stickShape 	,
				creTwistJnt = creTwistJnt	,	
				upperArmR15	= 'upperArmRGT_IKtmpJnt' )
				
				
				
				
stickNamLFT, handLFT_bJnt= armRig.eh_armRigExtR15(

				nameSpace = '' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'LFT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmLFT_tmpJnt' ,	
						'lowerArmLFT_tmpJnt', 	 
						'handLFT_tmpJnt' ,	
						'elbowPovLFT_tmpJnt' ),
				priorJnt = topSpine_bJnt.name	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,					
				jnt_grp =  'jnt_grp'	,			
				povShape = 'pyramid',
				keepFkIkBoth = keepFkIkBoth,
				ribbon = ribbon,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = showInfo ,
				linkRotOrder = linkRotOrder	,
				stickShape = stickShape 	,
				creTwistJnt = creTwistJnt	,
				upperArmR15	= 'upperArmLFT_IKtmpJnt')





#... add space switch
rigTools.addSpace(  nameSpace = '',	giveStick =  stickNamLFT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', 'head01_bJnt', topSpine_bJnt, hip_bJnt ] )
rigTools.addSpace(  nameSpace = '',	giveStick =  stickNamRGT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', 'head01_bJnt', topSpine_bJnt, hip_bJnt ] )

#... Leg LFT
from function.rigging.autoRig.bodyRig import bipedLegRig as bipedLegRig
reload(bipedLegRig)

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
					povShape = povShape ,# choice pyramid or sphereAxis
					jnt_grp = 'jnt_grp' ,
					linkRotOrder = linkRotOrder	,
					footAttr = True,
					stickShape = stickShape 	,
					creTwistJnt = creTwistJnt		
					 )


#... Leg RGT
bipedLegRig.bipedLegRigExt(
					nameSpace = '' 	,	
					parentTo = 'ctrl_grp' ,		
					side = 'RGT'	,				
					region = 'leg',
					tmpJnt = ( 	'upperLegRGT_tmpJnt'  , 'lowerLegRGT_tmpJnt' ,  'ankleRGT_tmpJnt' , 
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
					povShape = povShape ,# choice pyramid or sphereAxis
					jnt_grp = 'jnt_grp' ,
					linkRotOrder = linkRotOrder	,
					footAttr = True,
					stickShape = stickShape 	,
					creTwistJnt = creTwistJnt					 
					 )




# # # # # # # # # # # # # # # # # # # # # # # #
# Additional Rig    
# # # # # # # # # # # # # # # # # # # # # # # #





from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)


createFkRig.fkRig_omni_newCurl( nameSpace = '', parentCtrlTo = 'hip_gmbCtrl',
					jntLst = ('L_tail01_bJnt','L_tail02_bJnt'),
					charScale = charScale, priorJnt = 'hip_bJnt',side = 'L',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = True, curlPosiAtFirst = False, rotateOrder = 'zxy',
					parentToPriorJnt = True, parentMatrix = True,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = True)




createFkRig.fkRig_omni_newCurl( nameSpace = '', parentCtrlTo = 'hip_gmbCtrl',
					jntLst = ('R_tail01_bJnt','R_tail02_bJnt'),
					charScale = charScale, priorJnt = 'hip_bJnt',side = 'R',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = True, curlPosiAtFirst = False, rotateOrder = 'zxy',
					parentToPriorJnt = True, parentMatrix = True,
					curlCtrlShape = 'stick_ctrlShape', constraintCurl = True)



from function.rigging.autoRig import util 
reload(util)
#... Lock attr
util.cleanup()