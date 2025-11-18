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

from function.framework.eh_reloadWrapper import reloadWrapper as reload 

from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

from function.rigging.autoRig.components import eh_rootRig as rootRig
reload(rootRig)

from function.rigging.autoRig.components import eh_hipRig as hipRig
reload(hipRig)

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
charScale = rigTools.findCharScale( topJnt = 'head02_tmpJnt' )

charScale = 1

# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)


# = = = = = 02 Create hipRig = = = = = #
hip_bJnt = hipRig.hipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale, cogPivot = True   )


from function.rigging.autoRig.bodyRig import spineIKRig
reload(spineIKRig)

topSpine_bJnt = spineIKRig.spineHybridIK(
				nameSpace = '' 		,
				parentTo = 'ctrl_grp' 						,		
				tmpJnt = (		'spine01_tmpJnt' 			,
								'spine02_tmpJnt' 			,
								'spine03_tmpJnt' 			,
								'spine04_tmpJnt'			),
				priorCtrl = 'cog_gmbCtrl'					,
				priorJnt = hip_bJnt						,				
				charScale = charScale								,							
				linkRotOrder = True							)