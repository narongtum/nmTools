# -*- coding: utf-8 -*-
import maya.cmds as mc

#sys.path.append(r'D:\True_Axion\Tools\riggerTools\python\axionTools\rigging\autoRig\bodyRig')


# simple quradrupedLegRig using human leg rig for each animal leg
# for simple cartoon animal leg rig that pretent having bone struster like human leg
# not fit for realistic and for plantigate leg type suck as donky horse leg

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

# change module name 
from function.rigging.autoRig.bodyRig import finger_mainCurlExec as fingerCurl
reload( fingerCurl )

# from function.rigging.autoRig.bodyRig import localFinger
# reload( localFinger )

from function.rigging.autoRig.bodyRig import bipedLegRig
reload( bipedLegRig )

from function.rigging.autoRig.bodyRig import ribbonRig
reload( ribbonRig )

from function.rigging.autoRig.bodyRig import quradrupedLegRig as quRig
reload( quRig )

from function.rigging.autoRig.bodyRig import bipedLegRig
reload( bipedLegRig )

from function.rigging.autoRig import util 
reload(util)

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



neck_bJntName = neckRig.neckRig( 	nameSpace = nameSpace , 
							parentTo = 'ctrl_grp'   , 
							tmpJnt = 	( 	'neck01_tmpJnt','head01_tmpJnt'  )	,
							charScale = charScale	,
							priorJnt = chest_bJntName )





# = = = = = 061 Ear LFT = = = = = #
rigTools.createFkRig(	nameSpace = nameSpace  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
						tmpJnt = 	( 	['ear01LFT_tmpJnt','ear02LFT_tmpJnt'] 	)	,					
						charScale = charScale	, priorJnt = neck_bJntName			,
						side = 'LFT' ,ctrlShape = 'circle_ctrlShape'		, localWorld = True							)



# = = = = = 062 Ear RGT = = = = = #
rigTools.createFkRig(	nameSpace = nameSpace  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
						tmpJnt = 	( ['ear01RGT_tmpJnt','ear02RGT_tmpJnt'] ),

					charScale = charScale	, priorJnt = neck_bJntName			,
					side = 'RGT' ,ctrlShape = 'circle_ctrlShape'			, localWorld = True						)



# front leg left
bipedLegRig.bipedLegRigExt(		nameSpace = '' 	                ,
								parentTo = 'ctrl_grp' 				,
								side = 'LFT'						,
								tmpJnt = (	'upLegFrontLFT_tmpJnt'  , 'midLegFrontLFT_tmpJnt' ,  'ankleFrontLFT_tmpJnt'	 , 									
											'legPovFrontLFT_tmpJnt' ,'ballRollFrontLFT_tmpJnt' ,'toeRollFrontLFT_tmpJnt' ,
											'heelRollFrontLFT_tmpJnt'  , 'footOutFrontLFT_tmpJnt' , 'footInFrontLFT_tmpJnt' )		,
								region = 'frontLeg',
								priorJnt = chest_bJntName				,
								ikhGrp = 'ikh_grp' 					,
								noTouchGrp = 'noTouch_grp' 			,
								nullGrp = 'snapNull_grp'			,
								showInfo = False 					,				
								ribbon = False 						,								
								charScale = 1    ,
								ikPosi = 'animalFoot' , # if biped use arg 'foot'
								keepFkIkBoth = True	,
								povShape = 'pyramid',
								jnt_grp = 'jnt_grp' ,
								footAttr = False	,
								linkRotOrder = True ,
								 )



# front leg right
bipedLegRig.bipedLegRigExt(		nameSpace = '' 	                ,
								parentTo = 'ctrl_grp' 				,
								side = 'RGT'						,
								tmpJnt = (	'upLegFrontRGT_tmpJnt'  , 'midLegFrontRGT_tmpJnt' ,  'ankleFrontRGT_tmpJnt'	 , 
											'legPovFrontRGT_tmpJnt' ,'ballRollFrontRGT_tmpJnt' ,'toeRollFrontRGT_tmpJnt' ,'heelRollFrontRGT_tmpJnt'  , 
											'footOutFrontRGT_tmpJnt' , 'footInFrontRGT_tmpJnt' )		,
								region = 'frontLeg',
								priorJnt = chest_bJntName				,
								ikhGrp = 'ikh_grp' 					,
								noTouchGrp = 'noTouch_grp' 			,
								nullGrp = 'snapNull_grp'			,
								showInfo = False 					,				
								ribbon = False 						,								
								charScale = 1    ,
								ikPosi = 'animalFoot' ,  # if biped use arg 'foot'
								keepFkIkBoth = True	,
								povShape = 'pyramid',
								jnt_grp = 'jnt_grp' ,
								footAttr = False	,
								linkRotOrder = True ,
								 )	



# back leg left
bipedLegRig.bipedLegRigExt(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'LFT'		,			
							tmpJnt = (	'upLegBackLFT_tmpJnt'  , 'midLegBackLFT_tmpJnt' ,  'ankleBackLFT_tmpJnt' , 
										'legPovBackLFT_tmpJnt' ,'ballRollBackLFT_tmpJnt' ,'toeRollBackLFT_tmpJnt' ,
										'heelRollBackLFT_tmpJnt' , 'footOutBackLFT_tmpJnt' , 'footInBackLFT_tmpJnt' ),
							region = 'backLeg',
							priorJnt = hip_bJntName ,				
							ikhGrp = 'ikh_grp' 					,
							noTouchGrp = 'noTouch_grp' 			,
							nullGrp = 'snapNull_grp'			,
							showInfo = False 					,				
							ribbon = False 						,								
							charScale = 1    ,
							ikPosi = 'animalFoot' , # if biped use arg 'foot'
							keepFkIkBoth = True	,
							povShape = 'pyramid',
							jnt_grp = 'jnt_grp' ,
							footAttr = False	,
							linkRotOrder = True ,
							 )	



# back leg right	
bipedLegRig.bipedLegRigExt(		nameSpace = nameSpace 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'RGT'		,			
							tmpJnt = (	'upLegBackRGT_tmpJnt'  , 'midLegBackRGT_tmpJnt' ,  'ankleBackRGT_tmpJnt' , 
										'legPovBackRGT_tmpJnt' ,'ballRollBackRGT_tmpJnt' ,'toeRollBackRGT_tmpJnt' ,
										'heelRollBackRGT_tmpJnt' , 'footOutBackRGT_tmpJnt' , 'footInBackRGT_tmpJnt' ),
							region = 'backLeg',
							priorJnt = hip_bJntName ,				
							ikhGrp = 'ikh_grp' 					,
							noTouchGrp = 'noTouch_grp' 			,
							nullGrp = 'snapNull_grp'			,
							showInfo = False 					,				
							ribbon = False 						,								
							charScale = 1    ,
							ikPosi = 'animalFoot' , # if biped use arg 'foot'
							keepFkIkBoth = True	,
							povShape = 'pyramid',
							jnt_grp = 'jnt_grp' ,
							footAttr = False	,
							linkRotOrder = True ,
							 )	



# = = = = = 12 Tail  = = = = = #
rigTools.createFkRig(	nameSpace = nameSpace  ,  name = 'tail' , parentTo = 'ctrl_grp'  ,
						tmpJnt = 	( 	'tail01_tmpJnt'	,
										'tail02_tmpJnt'  	,
										'tail03_tmpJnt'  ,
										'tail04_tmpJnt'  )	,
					charScale = charScale	, priorJnt = hip_bJntName			,
					side = '' ,ctrlShape = 'circle_ctrlShape'		, localWorld = True		)
					


if mc.objExists('template_ctrl'):
	mc.delete('template_ctrl')


print '''\n
# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# 				Create Autorig done
# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
'''

# util.cleanup()