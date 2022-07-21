# -*- coding: utf-8 -*-
import maya.cmds as mc

#sys.path.append(r'D:\True_Axion\Tools\riggerTools\python\axionTools\rigging\autoRig\bodyRig')

#  quradrupedLegRig is real skelenton of animal back leg rig using 4 joint
# for realistic animal leg rig 


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

from function.rigging.autoRig.bodyRig import bipedLegRig
reload( bipedLegRig )

from function.rigging.autoRig.bodyRig import ribbonRig
reload( ribbonRig )

from function.rigging.autoRig.bodyRig import quradrupedLegRig as quRig
reload( quRig )

from function.rigging.tools import proc as pc 
reload(pc)

from function.rigging.autoRig import util 
reload(util)

# using ribbon or not
ribbon = False

nameSpace = '' 

# = = = = = Check charactor hight  = = = = = #
charScale = rigTools.findCharScale( topJnt = 'head01_tmpJnt' )


# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)



chest_bJntName , hip_bJntName  = hipRig.quradpedHipRig( 	nameSpace = nameSpace , 
						parentTo = 'ctrl_grp'   , 
						tmpJnt = 	( 	'body_tmpJnt','hip_tmpJnt' , 
										'upperBody_tmpJnt' , 'chest_tmpJnt' , 
										'lowerBody_tmpJnt' )	,
						charScale = charScale	 )



neck2_bJntName = neckRig.quradpedNeckRig( 	nameSpace = nameSpace , 
							parentTo = 'ctrl_grp'   , 
							tmpJnt = 	( 	'neck01_tmpJnt','neck02_tmpJnt'  )	,
							charScale = charScale	,
							priorJnt = chest_bJntName )



# = = = = = 05 HeadRig = = = = = #
head_bJntName = headRig.headRig(	
					nameSpace = nameSpace 					, 
					parentTo = 'ctrl_grp'  , 
					tmpJnt = ( 		'head01_tmpJnt' , 'eyeLFT_tmpJnt' , 'eyeRGT_tmpJnt' ,		# head
					'jaw01Lwr_tmpJnt' , 'jaw02Lwr_tmpJnt' , 'jaw03Lwr_tmpJnt' 			,		# jaw
					'jaw01Upr_tmpJnt' , 'jaw02Upr_tmpJnt','eye_tmpJnt' , 
					'eyeTargetLFT_tmpJnt' , 'eyeTargetRGT_tmpJnt'		 				),		# eye			
					faceCtrl = True	,
					priorJnt = neck2_bJntName	,
					charScale = charScale*2			)



# = = = = = 061 Ear LFT = = = = = #
rigTools.createFkRig(	nameSpace = nameSpace  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
						tmpJnt = 	( 	'ear01LFT_tmpJnt'	,
										'ear02LFT_tmpJnt'  	,
										'ear03LFT_tmpJnt')	,
					charScale = charScale	, priorJnt = head_bJntName			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'		, localWorld = True							)



# = = = = = 062 Ear RGT = = = = = #
rigTools.createFkRig(	nameSpace = nameSpace  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
						tmpJnt = 	( 	'ear01RGT_tmpJnt'	,
										'ear02RGT_tmpJnt'  	,
										'ear03RGT_tmpJnt')	,
					charScale = charScale	, priorJnt = head_bJntName 			,
					side = 'RGT' ,ctrlShape = 'circle_ctrlShape'			, localWorld = True						)



# = = = = = 11 Leg Front LFT = = = = = #
quRig.quradrupedLegRig(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'LFT'		,	
							region = 'frontLeg',		
							tmpJnt = (	'upLegFrontLFT_tmpJnt'  , 'midLegFrontLFT_tmpJnt' ,  'ankleFrontLFT_tmpJnt' , 
										'legPovFrontLFT_tmpJnt' ,'ballRollFrontLFT_tmpJnt' ,'toeRollFrontLFT_tmpJnt' ,
										'heelRollFrontLFT_tmpJnt' , 'footOutFrontLFT_tmpJnt' , 'footInFrontLFT_tmpJnt' , 'lowLegFrontLFT_tmpJnt'),

							priorJnt = chest_bJntName	,				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = ribbon	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upFrontLeg', 'lwrFrontLeg'),	
							charScale = 1			
							)	

	

# = = = = = 11 Leg Front RGT = = = = = #
quRig.quradrupedLegRig(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'RGT'		,	
							region = 'frontLeg',		
							tmpJnt = (	'upLegFrontRGT_tmpJnt'  , 'midLegFrontRGT_tmpJnt' ,  'ankleFrontRGT_tmpJnt' , 
										'legPovFrontRGT_tmpJnt' ,'ballRollFrontRGT_tmpJnt' ,'toeRollFrontRGT_tmpJnt' ,
										'heelRollFrontRGT_tmpJnt' , 'footOutFrontRGT_tmpJnt' , 'footInFrontRGT_tmpJnt' , 'lowLegFrontRGT_tmpJnt'),

							priorJnt = chest_bJntName	,				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = ribbon	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upFrontLeg', 'lwrFrontLeg'),	
							charScale = 1		
								)	



# = = = = = 11 Leg Back LFT = = = = = #
quRig.quradrupedLegRig(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'LFT'		,	
							region = 'backLeg',		
							tmpJnt = (	'upLegBackLFT_tmpJnt'  , 'midLegBackLFT_tmpJnt' ,  'ankleBackLFT_tmpJnt' , 
										'legPovBackLFT_tmpJnt' ,'ballRollBackLFT_tmpJnt' ,'toeRollBackLFT_tmpJnt' ,
										'heelRollBackLFT_tmpJnt' , 'footOutBackLFT_tmpJnt' , 'footInBackLFT_tmpJnt' , 'lowLegBackLFT_tmpJnt'),
							priorJnt = hip_bJntName ,				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = ribbon	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upBackLeg', 'lwrBackLeg'),	
							charScale = 1			)	



# = = = = = 11 Leg Back RGT = = = = = #		
quRig.quradrupedLegRig(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'RGT'		,	
							region = 'backLeg',		
							tmpJnt = (	'upLegBackRGT_tmpJnt'  , 'midLegBackRGT_tmpJnt' ,  'ankleBackRGT_tmpJnt' , 
										'legPovBackRGT_tmpJnt' ,'ballRollBackRGT_tmpJnt' ,'toeRollBackRGT_tmpJnt' ,
										'heelRollBackRGT_tmpJnt' , 'footOutBackRGT_tmpJnt' , 'footInBackRGT_tmpJnt' , 'lowLegBackRGT_tmpJnt'),
							priorJnt = hip_bJntName ,				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = ribbon	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upBackLeg', 'lwrBackLeg'),	
							charScale = 1		)	



# = = = = = 12 Tail  = = = = = #
rigTools.createFkRig(	nameSpace = nameSpace  ,  name = 'tail' , parentTo = 'ctrl_grp'  ,
						tmpJnt = 	( 	'tail01_tmpJnt'	,
										'tail02_tmpJnt'  	,
										'tail03_tmpJnt'  ,
										'tail04_tmpJnt'  )	,
					charScale = charScale	, priorJnt = hip_bJntName			,
					side = '' ,ctrlShape = 'circle_ctrlShape'		, localWorld = True		)
					
					

# Lock attr
util.cleanup()
