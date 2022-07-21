#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# prop Rig module


import maya.cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


def propRig(
	nameSpace = '',
	ctrl_grp =  'ctrl_grp' ,
	tmpJnt = 'propLFT_tmpJnt' ,
	charScale =''	,
	side = 'LFT',
	priorJnt =''):

	core.makeHeader('Start of %s%s Rig' %('prop',side)	)
	handProp = core.Dag( tmpJnt )
	#handProp = handProp.makeRawName()[:-3]

	part = nameSpace + 'handProp%s' %side 


	# handPropRig_grp = core.Null()
	# handPropRig_grp.name( part + '_' + 'grp')
	handProp_ctrl = core.Dag( part + '_ctrl' )
	handProp_ctrl.nmCreateController('tubeY_ctrlShape')
	handPropZro_grp = rigTools.zeroGroup( handProp_ctrl )
	handPropZro_grp.name = part + 'CtrlZro_grp'

	handProp_ctrl.editCtrlShape( axis = charScale * 0.8 )
	handPropGmbl_ctrl = core.createGimbal( handProp_ctrl )
	handProp_ctrl.color = 'white'
	handProp_ctrl.rotateOrder = 'xzy'
	handPropGmbl_ctrl.rotateOrder = 'xzy'


	# Parenting cog controller to cog_tmpJnt
	handPropZro_grp.matchPosition( handProp )
	handPropZro_grp.matchRotation( handProp  )


	handPropZro_grp.parent( ctrl_grp )


	hand_bJnt = core.Dag( priorJnt )


	# Constraint joint parent of controller
	controllerJnt_parCons = core.parentConstraint( hand_bJnt , handPropZro_grp , mo = True)
	controllerJnt_parCons.name = part + 'Jnt_parCons'
	print('#### End of %s%s Rig ####' %( 'prop' , side ))
	print('\n\n\n\n\n')