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

from function.rigging.autoRig.bodyRig import armRigMatrix as armRig
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


nameSpace = '' 


# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )



# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)




# = = = = = 02 Create hipRig = = = = = #
hip_bJnt = hipRig.hipRig(	nameSpace = '' , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale  )




# = = = = = 03 Create spineRig = = = = = #
'''
topSpine_bJnt = spineFkRig.spineRig( 		
										nameSpace = '' 					, 
										parentTo = 'ctrl_grp' 			,
										tmpJnt = (	'spine01_tmpJnt' ,'spine02_tmpJnt' ,
													'spine03_tmpJnt' ,'spine04_tmpJnt'	),
										priorCtrl = 'cog_gmbCtrl'		,
										priorJnt = hip_bJnt,
										charScale = charScale							)

'''

# = = = = = 03 Create spine IK Rig ( Optional rig you must select one ) = = = = = #
topSpine_bJnt = spineRig.spineIK(nameSpace = ''                  ,
						spineNum = 4                  	 ,
						hipJnt = 'hip_bJnt'           	,
					   cog_ctrl = 'cog_gmbCtrl'			,
					   ctrl_grp = 'ctrl_grp'      		,
					   isIK = True                      ,
					   charScale = charScale                  )





# = = = = = 04 Neck Rig = = = = = #
neck_bJnt = neckRig.neckRig(	
							nameSpace = '' 					, 
							parentTo = 'ctrl_grp'  , 
							tmpJnt = (		'neck_tmpJnt' ,'head01_tmpJnt' 	) ,  
							priorJnt = topSpine_bJnt ,
							charScale = charScale	)



# = = = = = 05 HeadRig = = = = = #
headRig.headRig(	
					nameSpace = '' 					, 
					parentTo = 'ctrl_grp'  , 
					tmpJnt = ( 		'head01_tmpJnt' , 'eyeLFT_tmpJnt' , 'eyeRGT_tmpJnt' ,		# head
					'jaw01Lwr_tmpJnt' , 'jaw02Lwr_tmpJnt' , 'jaw03Lwr_tmpJnt' 			,		# jaw
					'jaw01Upr_tmpJnt' , 'jaw02Upr_tmpJnt','eye_tmpJnt' , 
					'eyeTargetLFT_tmpJnt' , 'eyeTargetRGT_tmpJnt'		 				),		# eye			
					faceCtrl = True	,
					priorJnt = neck_bJnt	,
					charScale = charScale			)



# = = = = = 06 clavicleRig LFT = = = = = #
clavLFT_bJnt = clavicleRig.clavicleRig(		nameSpace = '' 						, 
											parentTo = 'ctrl_grp' 				,
											side = 'LFT'						,
											tmpJnt = ( 	'clavLFT_tmpJnt'  )		,
											priorJnt = topSpine_bJnt 			,
											charScale = charScale )



# = = = = = 06 clavicleRig RGT = = = = = #
clavRGT_bJnt = clavicleRig.clavicleRig(		nameSpace = '' 					, 
										parentTo = 'ctrl_grp' ,
										side = 'RGT',
										tmpJnt = ( 	'clavRGT_tmpJnt'  ),
										priorJnt = topSpine_bJnt	,
										charScale = charScale )




# = = = = = 07 arm LFT Rig = = = = = #
stickNamLFT,handLFT_bJnt = armRig.armRig(	nameSpace = '' 						,
								charScale = charScale,
								parentTo = 'ctrl_grp' ,
								side = 'LFT',
								tmpJnt = (	'upperArmLFT_tmpJnt'  , 'lowerArmLFT_tmpJnt' ,  
											'handLFT_tmpJnt' , 'armLFT_pov_tmpJnt' ),
								priorJnt = clavLFT_bJnt ,
								ikhGrp = 'ikh_grp' ,
								noTouchGrp = 'noTouch_grp' 			,
								nullGrp = 'snapNull_grp'			,
								showInfo = False ,
								ribbon = True ,
								ribbonRes = 'low' )


# = = = = = 07 arm RGT Rig = = = = = #
stickNamRGT,handRGT_bJnt = armRig.armRig(	nameSpace = '' 						,
								charScale = charScale,
								parentTo = 'ctrl_grp' ,
								side = 'RGT',
								tmpJnt = (	'upperArmRGT_tmpJnt'  , 'lowerArmRGT_tmpJnt' ,  
											'handRGT_tmpJnt' , 'armRGT_pov_tmpJnt' ),
								priorJnt = clavRGT_bJnt,
								ikhGrp = 'ikh_grp' ,
								noTouchGrp = 'noTouch_grp' 			,
								nullGrp = 'snapNull_grp'			,
								showInfo = False ,
								ribbon = True ,
								ribbonRes = 'low' )

# = = = = = add arm space switch = = = = = #	
rigTools.addSpace( giveSys = ['hand'] , giveSide = ['LFT','RGT'] , giveGrp = ['world','local','neck','chest','cog'] , giveCtrl = ['placement','clav','neck','spine04','cog'])

# = = = = = 08 Create finger LFT = = = = = #	 		
handLFT = fingerRig.fingerRig( 	
								nameSpace = '' 						,
								side = 'LFT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale ,priorJnt = handLFT_bJnt ,stickNam = stickNamLFT )



# = = = = = Create finger RGT = = = = = #
handRGT = fingerRig.fingerRig( 	
								nameSpace = '' 						,
								side = 'RGT', fingerNum = 3 , 
								fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'], 
								charScale = charScale  ,priorJnt = handRGT_bJnt , stickNam = stickNamRGT )




# = = = = = 09 Main finger curl = = = = = #
fingerCurl.mainFingerCurlRig( 	nameSpace = '' 	 ,
								fingerbehavior = ('fist','roll','relax','spread') , 
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'LFT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' )

fingerCurl.mainFingerCurlRig( 	nameSpace = '' 	 ,
								fingerbehavior = ('fist','roll','relax','spread') , 
								fingerName = ('thumb','index','middle','ring','pinky') , 
								side = 'RGT'  , numCtrl = 3 , zroNam = 'Zro_grp' , 
								offsetNam = 'Offset_grp' )



# 10 local finger curl

# Create Grp for Local finger
stickGrpNam = localFinger.creEachFingerGrp( 	nameSpace = ''  , 
												parentTo = 'ctrl_grp' , side = 'LFT'  )

# Local Thumb LFT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'thumb' , side = 'LFT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Index LFT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'index' , side = 'LFT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Middle LFT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'middle' , side = 'LFT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Ring LFT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'ring' , side = 'LFT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Pinky LFT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'pinky' , side = 'LFT' , 
									charScale = charScale , parentTo = stickGrpNam )




# Create Grp for Local finger
stickGrpNam = finloCurl.creEachFingerGrp( 	nameSpace = '' 						, 
												parentTo = 'ctrl_grp' , side = 'RGT'  )

# Local Thumb RGT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'thumb' , side = 'RGT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Index RGT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'index' , side = 'RGT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Middle RGT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'middle' , side = 'RGT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Ring RGT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'ring' , side = 'RGT' , 
									charScale = charScale , parentTo = stickGrpNam )

# Local Pinky RGT
finloCurl.runLocalFingerRig( 		nameSpace = '' 						,
									fingerName = 'pinky' , side = 'RGT' , 
									charScale = charScale , parentTo = stickGrpNam )




# 11 Leg LFT
bipedLegRig.bipedLegRig(		nameSpace = '' 	                ,
								parentTo = 'ctrl_grp' 				,
								side = 'LFT'						,
								tmpJnt = (	'upperLegLFT_tmpJnt'  , 'lowerLegLFT_tmpJnt' ,  'ankleLFT_tmpJnt'	 , 
											'legLFT_pov_tmpJnt' ,'ballLFT_tmpJnt' ,'toesTipLFT_tmpJnt' ,'heelRollLFT_tmpJnt'  , 'footOutLFT_tmpJnt' , 'footInLFT_tmpJnt' )		,
								priorJnt = 'hip_bJnt'				,
								ikhGrp = 'ikh_grp' 					,
								noTouchGrp = 'noTouch_grp' 			,
								nullGrp = 'snapNull_grp'			,
								showInfo = False 					,
								ribbon = True 						,
								charScale = charScale                )


# 11 Leg RGT
bipedLegRig.bipedLegRig(		nameSpace = '' 	                        ,
								parentTo = 'ctrl_grp' 					,
								side = 'RGT'							,	
								tmpJnt = (	'upperLegRGT_tmpJnt'  , 'lowerLegRGT_tmpJnt' ,  'ankleRGT_tmpJnt' 	, 
											'legRGT_pov_tmpJnt' ,'ballRGT_tmpJnt' ,'toesTipRGT_tmpJnt' ,'heelRollRGT_tmpJnt'  , 'footOutRGT_tmpJnt' , 'footInRGT_tmpJnt'  )		,
								priorJnt = 'hip_bJnt'					,
								ikhGrp = 'ikh_grp' 						,
								noTouchGrp = 'noTouch_grp' 				,
								nullGrp = 'snapNull_grp'				,
								showInfo = False 						,
								ribbon = True 							,
								charScale = charScale                    )


# add space switch
rigTools.addSpace( giveSys = ['ankleLeg'] , giveSide = ['LFT','RGT'] , giveGrp = ['world','chest','cog'] , giveCtrl = ['placement','hip','cog'])




if mc.objExists('template_ctrl'):
	mc.delete('template_ctrl')