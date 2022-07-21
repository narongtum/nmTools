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

# from function.rigging.autoRig.bodyRig import fingerCurl
# reload( fingerCurl )

# from function.rigging.autoRig.bodyRig import localFinger
# reload( localFinger )

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

from function.rigging.feature import baseFingerSpread as baseFinger
reload(baseFinger)

from function.rigging.autoRig.bodyRig import torsoRig
reload(torsoRig)

from function.rigging.tools import proc as pc 
reload(pc)

from function.rigging.autoRig import util 
reload(util)

nameSpace = '' 

from function.rigging.autoRig.bodyRig import fkIkGenRig
reload( fkIkGenRig )

charScale = 1


# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )



# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)




# = = = = = 02 Create hipRig = = = = = #
hip_bJnt = hipRig.hipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale  )


'''
# = = = = = 03 Create spine IK Rig  = = = = = #
topSpine_bJnt = torsoRig.torsoRig( 
									nameSpace = nameSpace									,
						 			ctrl_grp = 'ctrl_grp'							,
						 			tmpJnt = ( 'spine01_tmpJnt', 'spine02_tmpJnt' )	,
						 			charScale = 1 									)
'''

topSpine_bJnt = spineFkRig.spineRig( 		parentTo = 'ctrl_grp' 								,
										tmpJnt = (	'spine01_tmpJnt' ,'spine02_tmpJnt', 
												'spine03_tmpJnt', 'spine04_tmpJnt')			,
										priorCtrl = 'cog_gmbCtrl'	,
										charScale = charScale 	,
										ctrShape = 'circleCurlUp_ctrlShape'						)



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
					charScale = charScale			)




# Normal arm




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
						'armLFT_pov_tmpJnt' ),
				priorJnt = 'clavLFT_bJnt'	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,			
				povShape = 'sphereAxis',
				keepFkIkBoth = False,
				ribbon = True,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = False ,
					)


# = = = = = 08 Create finger LFT = = = = = #	 		
fingerLFT = fingerRig.fingerRig( 	
								nameSpace = nameSpace 						,
								side = 'LFT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = handLFT_bJnt ,stickNam = stickNamLFT )

# arm RGT Side
stickNamRGT, handRGT_bJnt= armRig.armRigExt(

				nameSpace = nameSpace 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'RGT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmRGT_tmpJnt' ,	
						'lowerArmRGT_tmpJnt', 	 
						'handRGT_tmpJnt' ,	
						'armRGT_pov_tmpJnt' ),
				priorJnt = 'clavRGT_bJnt'	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,			
				povShape = 'sphereAxis',
				keepFkIkBoth = False,
				ribbon = True,
				ribbonRes = 'low', 
				ribbonName = ('upArm', 'lwrArm'),
				showInfo = False 	)


# = = = = = Create finger RGT = = = = = #
fingerRGT = fingerRig.fingerRig( 	
								nameSpace = nameSpace 						,
								side = 'RGT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale  ,priorJnt = handRGT_bJnt , stickNam = stickNamRGT )




# = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = nameSpace 	 ,
								fingerbehavior = ('fist','roll','relax','spread') , 
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'LFT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickNamLFT)

fingerCurl.mainFingerCurlRig( 	nameSpace = nameSpace 	 ,
								fingerbehavior = ('fist','roll','relax','spread') , 
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'RGT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickNamRGT)



# = = = = = # 10 Local finger curl # = = = = = #
finloCurl.localFingerAllRig( 		nameSpace = nameSpace, parentTo='ctrl_grp' , side = 'LFT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, stickNam = stickNamLFT)


finloCurl.localFingerAllRig( 		nameSpace = nameSpace, parentTo='ctrl_grp' , side = 'RGT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, stickNam = stickNamRGT)




# add base finger spread 
baseFinger.baseFingerSpread( tmpJnt = 'baseSpreadLFT_tmpJnt' , stick = stickNamLFT ,fingerGrpNam = fingerLFT)
baseFinger.baseFingerSpread( tmpJnt = 'baseSpreadRGT_tmpJnt' , stick = stickNamRGT ,fingerGrpNam = fingerRGT)






























# LOWER ARM

# LOWER ARM # = = = = = 06 clavicleRig LFT = = = = = #
clavLwrLFT_bJnt = clavicleRig.clavicleRig(		nameSpace = '' 						, 
											parentTo = 'ctrl_grp' 				,
											side = 'LFT'						,
											tmpJnt = ( 	'clavLwrLFT_tmpJnt'  )		,
											priorJnt = 'spine03_bJnt' 			,
											charScale = charScale )






# LOWER ARM # = = = = = 06 clavicleRig RGT = = = = = #
clavLwrRGT_bJnt = clavicleRig.clavicleRig(		nameSpace = '' 					, 
										parentTo = 'ctrl_grp' ,
										side = 'RGT',
										tmpJnt = ( 	'clavLwrRGT_tmpJnt'  ),
										priorJnt = 'spine03_bJnt'	,
										charScale = charScale )





# LOWER ARM # arm LFT Side
stickLwrLFT, handLwrLFT_bJnt= armRig.armRigExt(

				nameSpace = '' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'LFT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmLwrLFT_tmpJnt' ,	
						'lowerArmLwrLFT_tmpJnt', 	 
						'handLwrLFT_tmpJnt' ,	
						'armLwrLFT_pov_tmpJnt' ),
				priorJnt = clavLwrLFT_bJnt	,	
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
handLwrLFT = fingerRig.fingerRig( 	
								nameSpace = 'lwr' 						,
								side = 'LFT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = handLwrLFT_bJnt ,stickNam = stickLwrLFT )




## LOWER ARM  = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = 'lwr' 	 ,
								fingerbehavior = ('fist','roll','relax','spread') , 
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'LFT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickLwrLFT)



# LOWER ARM # = = = = = # 10 Local finger curl # = = = = = #
localFinger.localFingerAllRig( 		nameSpace = 'lwr', parentTo='ctrl_grp' , side = 'LFT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, stickNam = stickNamLFT)










# LOWER ARM # arm RGT Side
stickLwrRGT, handLwrRGT_bJnt= armRig.armRigExt(

				nameSpace = 'lwr' 	,				
				charScale = charScale	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'RGT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmLwrRGT_tmpJnt' ,	
						'lowerArmLwrRGT_tmpJnt', 	 
						'handLwrRGT_tmpJnt' ,	
						'armLwrRGT_pov_tmpJnt' ),
				priorJnt = clavLwrRGT_bJnt	,	
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
handLwrRGT = fingerRig.fingerRig( 	
								nameSpace = 'lwr' 						,
								side = 'RGT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = handLwrRGT_bJnt ,stickNam = stickLwrRGT )




# LOWER ARM # = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = 'lwr' 	 ,
								fingerbehavior = ('fist','roll','relax','spread') , 
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'RGT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' , stickNam = stickLwrRGT)


# LOWER ARM # = = = = = # 10 Local finger curl # = = = = = #
localFinger.localFingerAllRig( 		nameSpace = 'lwr', parentTo='ctrl_grp' , side = 'RGT' , 
									fingerName = ('thumb','index','middle','ring','pinky') ,
									charScale= charScale, stickNam = stickNamLFT)







'''


# 11 Leg LFT
bipedLegRig.bipedLegRigExt(
					nameSpace = '' 	,	
					parentTo = 'ctrl_grp' ,			
					side = 'LFT'	,				
					region = 'leg',
					tmpJnt = (	'upperLegLFT_tmpJnt'  , 'lowerLegLFT_tmpJnt' ,  'ankleLFT_tmpJnt' , 
								'legLFT_pov_tmpJnt' ,'ballLFT_tmpJnt' ,'toesTipLFT_tmpJnt' ,
								'heelRollLFT_tmpJnt' , 'footOutLFT_tmpJnt' , 'footInLFT_tmpJnt'),
					priorJnt = 'hip_bJnt'	,			
					ikhGrp = 'ikh_grp' 	,				
					noTouchGrp = 'noTouch_grp' 	,		
					nullGrp = 'snapNull_grp'	,		
					showInfo = False  ,					
					ribbon = True	,				
					ribbonRes = 'low'	,				
					ribbonName = ('upLeg', 'lwrLeg'),	
					charScale = 1	,					
					ikPosi = 'foot', # get only 2 variable 'foot' or 'ankle'
					keepFkIkBoth = True	,# keep fk/ik ctrl visibility both or not
					povShape = 'pyramid' ,# choice pyramid or sphereAxis
					jnt_grp = 'jnt_grp' )


# 11 Leg RGT

bipedLegRig.bipedLegRigExt(
					nameSpace = '' 	,	
					parentTo = 'ctrl_grp' ,			
					side = 'RGT'	,				
					region = 'leg',
					tmpJnt = (	'upperLegRGT_tmpJnt'  , 'lowerLegRGT_tmpJnt' ,  'ankleRGT_tmpJnt' , 
								'legRGT_pov_tmpJnt' ,'ballRGT_tmpJnt' ,'toesTipRGT_tmpJnt' ,
								'heelRollRGT_tmpJnt' , 'footOutRGT_tmpJnt' , 'footInRGT_tmpJnt'),
					priorJnt = 'hip_bJnt'	,			
					ikhGrp = 'ikh_grp' 	,				
					noTouchGrp = 'noTouch_grp' 	,		
					nullGrp = 'snapNull_grp'	,		
					showInfo = False  ,					
					ribbon = True	,				
					ribbonRes = 'low'	,				
					ribbonName = ('upLeg', 'lwrLeg'),	
					charScale = 1	,					
					ikPosi = 'foot', # get only 2 variable 'foot' or 'ankle'
					keepFkIkBoth = True	,# keep fk/ik ctrl visibility both or not
					povShape = 'pyramid' ,# choice pyramid or sphereAxis
					jnt_grp = 'jnt_grp' )

'''
# add space switch
rigTools.addSpace( 	giveStick =  stickNamLFT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', neck_bJnt, topSpine_bJnt, hip_bJnt ] )
rigTools.addSpace( 	giveStick =  stickNamRGT  , spaces = ['world','neck','chest','cog'] , piors = [ 'placement_ctrl', neck_bJnt, topSpine_bJnt, hip_bJnt ] )


# Lock attr
util.cleanup()
