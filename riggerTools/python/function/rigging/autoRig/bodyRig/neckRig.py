#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 04_Neck rig module



import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.pipeline import logger 
reload(logger)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

color_part_dict = mnd.COLOR_part_dict

# import logging
# logger = logging.getLogger('debug_text')
# logger.setLevel(logging.DEBUG)

class NeckRigLogger(logger.MayaLogger):
	LOGGER_NAME = "neckRig"

def neckRig( 	nameSpace = '' ,
				parentTo = 'ctrl_grp'  , 
				tmpJnt = (		'neck_tmpJnt' ,'head01_tmpJnt' 	) , 
				priorJnt = ''	,
				charScale=''	,
				linkRotOrder = False									):

	core.makeHeader('Start of neck Rig')
	# size arg
	# charScale = mc.getAttr( 'template_ctrl.scaleX' )
	# nameSpace = charName + elem

	# parentTo = '%s%s' %(nameSpace,parentTo)

	# Get name object
	neck = core.Dag( tmpJnt[ 0 ] )
	# head01 = core.Dag( tmpJnt[ 1 ] )

	# Create bind joint at
	neck_bJnt = rigTools.jointAt( neck )
	# head01_bJnt = rigTools.jointAt( head01 )

	# Parent each 
	# head01_bJnt.parent( neck_bJnt )

	# Set Name 
	neck_bJnt.name = nameSpace + 'neck' + '_bJnt'
	# head01_bJnt.name = 'head' + '01' + '_bJnt'

	# set joint lable
	neck_bJnt.setLable('CEN','neck')

	# Create Rig Group
	neckRig_grp = core.Null()
	neckRig_grp.name = nameSpace +'neckRig_grp'

	# Parenting and positioning
	neckRig_grp.matchPosition( neck )
	neckRig_grp.matchRotation( neck )



	# FK main group
	neckFkCtrl_grp = core.Null()
	neckFkCtrl_grp.snap( neck )
	neckFkCtrl_grp.parent( neckRig_grp )
	neckFkCtrl_grp.name = nameSpace +'neckFkCtrl_grp'

	# Create FK neck
	part = nameSpace +'neck'
	neck_ctrl = core.Dag( part + '_ctrl' )
	neck_ctrl.nmCreateController('circle_ctrlShape')
	neckZro_grp = rigTools.zeroGroup( neck_ctrl )
	neckZro_grp.name = part + 'Zro_grp'
	neck_ctrl.editCtrlShape( axis = charScale * 2.8 )
	neckGmbl_ctrl = core.createGimbal( neck_ctrl )
	neck_ctrl.color = color_part_dict['primary'] #... yellow
	neck_ctrl.rotateOrder = 'xzy'
	neckGmbl_ctrl.rotateOrder = 'xzy'


	if linkRotOrder:
		# link rotate order
		neck_ctrl.addRotEnum()
		neckGmbl_ctrl.addRotEnum()



	

	# Parenting and positioning
	neckZro_grp.matchPosition( neck_bJnt )
	neckZro_grp.matchRotation( neck_bJnt )



	neckZro_grp.parent( neckRig_grp )
	neck_bJnt.parent( priorJnt )
	neckRig_grp.parent( parentTo )

	partName = nameSpace + 'neck'
	#.... Change ctrl to ctrlShape instead
	neckLoc_grp , neckWor_grp , neckWorGrp_oriCons , neckZroGrp_oriCons , neckZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( neck_ctrl.shape , neckRig_grp , parentTo , neckZro_grp , partName )
	neckLoc_grp.name = nameSpace + 'neckLoc_grp'
	neckWor_grp.name = nameSpace + 'neckWor_grp'
	neckWorGrp_oriCons.name = nameSpace + 'neckWorGrp_orientCons'
	neckZroGrp_oriCons.name = nameSpace + 'neckZroGrp_orientCons'
	neckZroGrpOriCons_rev.name = nameSpace + 'neckZroGrpOrientCons_rev'


	# Constraint rig_grp to prior controller grp
	neckRigGrp_parCons = core.parentConstraint( priorJnt , neckRig_grp , mo = True)
	neckRigGrp_parCons.name = nameSpace +'neckRigGrp_parCons'	

	# shift to here because of having an unexpect head grp prosition
	# Constraint joint parent of controller
	neckJnt_parCons = core.parentConstraint( neckGmbl_ctrl , neck_bJnt )
	neckJnt_parCons.name = part + 'Jnt_parCons'
	# Scale Constraint 
	neckJnt_scaleCons = core.scaleConstraint( neckGmbl_ctrl , neck_bJnt )
	neckJnt_scaleCons.name = part + 'Jnt_scaleCons'

	print ('\n#### End of %s Rig ####' %(part))
	print('\n\n\n\n\n')
	return neck_bJnt.name

	

def quradpedNeckRig( 		nameSpace = '' , 
							parentTo = 'ctrl_grp'   , 
							tmpJnt = 	( 	'neck01_tmpJnt','neck02_tmpJnt'  )	,
							charScale = ''	 ,
							priorJnt = ''):
	''' neck rig for quradruped '''
	core.makeHeader('Start of neck Rig')

	neck1 = core.Dag( tmpJnt[ 0 ] )
	neck2 = core.Dag( tmpJnt[ 1 ] )

	neck1_bJnt = rigTools.jointAt( neck1 )
	neck2_bJnt = rigTools.jointAt( neck2 )

	neck2_bJnt.parent( neck1_bJnt )


	neck1Name = neck1.makeRawName()
	neck2Name = neck2.makeRawName()

	neck1_bJnt.name = nameSpace + neck1Name + '_bJnt'
	neck2_bJnt.name = nameSpace + neck2Name + '_bJnt'

	# Create Rig Group
	neckRig_grp = core.Null()
	neckRig_grp.name = nameSpace +'neckRig_grp'

	# Parenting and positioning
	neckRig_grp.matchPosition( neck1_bJnt )


	# Constraint rig_grp to prior controller grp
	neckRigGrp_parCons = core.parentConstraint( priorJnt , neckRig_grp , mo = True)
	neckRigGrp_parCons.name = nameSpace +'neckRigGrp_parCons'

	# FK main group
	neckFkCtrl_grp = core.Null()
	neckFkCtrl_grp.parent( neckRig_grp )
	neckFkCtrl_grp.name = nameSpace +'neckFkCtrl_grp'



	# create lowerBody controller
	neck1Zro_grp , neck1_ctrl, neck1_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = neck1_bJnt.name  , 
													ctrlShape = 'circle_ctrlShape', charScale = 10 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = neckFkCtrl_grp , 
													rotation = (0,0,0)  )

	# create lowerBody controller
	neck2Zro_grp , neck2_ctrl, neck2_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = neck2_bJnt.name  , 
													ctrlShape = 'circle_ctrlShape', charScale = 10 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = neck1_gmblCtrl , 
													rotation = (0,0,0)  )

	# Constraint rig_grp to prior controller grp
	neckRigGrp_parCons = core.parentConstraint( priorJnt , neckRig_grp , mo = True)
	neckRigGrp_parCons.name = nameSpace +'neckRigGrp_parCons'


	neckLoc_grp , neckWor_grp , neckWorGrp_oriCons , neckZroGrp_oriCons , neckZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( neck1_ctrl , neckRig_grp , parentTo , neck1Zro_grp )
	neckLoc_grp.name = nameSpace + 'neckLoc_grp'
	neckWor_grp.name = nameSpace + 'neckWor_grp'
	neckWorGrp_oriCons.name = nameSpace + 'neckWorGrp_orientCons'
	neckZroGrp_oriCons.name = nameSpace + 'neckZroGrp_orientCons'
	neckZroGrpOriCons_rev.name = nameSpace + 'neckZroGrpOrientCons_rev'

	mc.parent( neck1Zro_grp , neckRig_grp )
	neck1_bJnt.parent( priorJnt )
	
	neckRig_grp.parent( parentTo )
	NeckRigLogger.info('\n#### End of %s ####' %(__name__))
	print('\n\n\n\n\n')

	return neck2_bJnt.name


# neckJnt = neckRig(	parentTo = 'ctrl_grp'  , tmpJnt = (		'neck_tmpJnt' ,'head01_tmpJnt' 	) ,  priorJnt = topSpine	)