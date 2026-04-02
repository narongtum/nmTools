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
					color = 'yellow' , curlCtrl = True ,suffix = '_bJnt'	)[2][-1]
#... return
topSpine_bJnt = topSpine_bJnt.name





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
					priorJnt = topSpine_bJnt	,
					charScale = charScale	,
					ctrlShape = 'circle_ctrlShape',
					priorCtrl ='spine01_gmbCtrl',
					linkRotOrder = linkRotOrder			)








