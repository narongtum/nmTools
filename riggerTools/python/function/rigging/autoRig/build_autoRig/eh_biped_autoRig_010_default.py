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

from function.rigging.autoRig.components import eh_ikfkSpineRig as ikfkSpineRig
reload(ikfkSpineRig)

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

# = = = = = 01 Create main Controller = = = = = #
rootRig.createMasterGrp(	charScale = charScale 	)


# = = = = = 02 Create hipRig = = = = = #
hip_bJnt = hipRig.hipRig(	nameSpace = nameSpace , 
				ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) , 
				charScale = charScale)



spine_bJnt = ikfkSpineRig.createIkFkSpineRig(
		nameSpace=nameSpace,
		parentTo='ctrl_grp',
		priorJnt=hip_bJnt,
		priorCtrl='cog_gmbCtrl',
		hipCtrl = 'hip_gmbCtrl',
		charScale=charScale,
		# Specific Arguments for this method
		polyplane_L02='spine01_L02_ply',
		placement_ctrl='Placement_ctrl', # Needed for Global Scale Logic
		tmpJnt=['lwrSpine_tmpJnt', 'spineBtw01_tmpJnt', 'spineBtw02_tmpJnt', 'uprSpine_tmpJnt'],
		# Constants
		rotateOrder = 'zxy')
