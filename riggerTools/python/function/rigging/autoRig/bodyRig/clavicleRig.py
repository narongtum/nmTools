import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc as misc
reload( misc )

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


def clavicleRig(		nameSpace = ''  ,
						parentTo = 'ctrl_grp' 				,
						side = 'LFT'						,
						tmpJnt = ( 	'clavLFT_tmpJnt'  )		,
						priorJnt = ''						,
						charScale = ''

					):

	
	if side == 'LFT':
		colorSide = 'red'
	else:
		colorSide = 'blue'


	core.makeHeader( 'Start of %s%s Rig' %('clavicle',side) )
	logger.info(__name__)
	# nameSpace condition for name element
	rawPriorNam = misc.splitName( priorJnt )

	print (rawPriorNam)

	if len(rawPriorNam) == 2:
		rawPriorNam = rawPriorNam[0]
	elif len(rawPriorNam) == 3:
		rawPriorNam = rawPriorNam[0] + '_' + rawPriorNam[1]
	elif len(rawPriorNam) == 4:
		rawPriorNam = rawPriorNam[0] + '_' + rawPriorNam[1] + '_' + rawPriorNam[2]
	else:
		mc.error('Element is too much.')




	

	# nameSpace = charName + elem
	# parentTo = '%s%s' %(nameSpace,parentTo)
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# clavicle rig  
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	# get name
	clav = misc.splitName(tmpJnt)[0]
	# remove side
	clav = clav.replace(side,'')


	part = nameSpace + clav
	clav1 = core.Dag(tmpJnt)
	clav_bJnt = rigTools.jointAt( clav1 )
	clav_bJnt.name = part + side + '_bJnt'

	# set joint lable
	clav_bJnt.setLable( side ,'collar')
	
	clav_bJnt.parent( priorJnt )
	# Create Rig Group of 'clavRig'
	clavRig_grp = core.Null( nameSpace + clav + 'Rig' + side + '_grp')
	clavRigGrp_parCons = core.parentConstraint( priorJnt , clavRig_grp )
	clavRigGrp_parCons.name = nameSpace + clav + 'Rig' + side +'Grp' + '_parCons'

	# Set Sacle seqment compensate
	clav_bJnt.attr('segmentScaleCompensate').value = 0
	clav_ctrl = core.Dag( nameSpace + clav + side + '_ctrl' )
	clav_ctrl.nmCreateController('shoulder%s_FK_ctrlShape' %side)
	clav_ctrl.editCtrlShape( axis = charScale * 0.75 )
	clav_ctrl.rotateShape(  rotate = (0 , 0 , 90)  )

	# Create zero group
	clavZro_grp = rigTools.zeroGroup( clav_ctrl )
	clavZro_grp.name =  nameSpace + clav + side + 'Zro_grp'

	clavGmbl_ctrl = core.createGimbal( clav_ctrl )
	clav_ctrl.color = colorSide
	clav_ctrl.rotateOrder = 'xyz'
	clavGmbl_ctrl.rotateOrder = 'xyz'
	clavZro_grp.matchPosition( clav_bJnt )
	clavZro_grp.matchRotation( clav_bJnt )

	# Making joint parentConstraint to controller
	clav_parCons = core.parentConstraint( clavGmbl_ctrl , clav_bJnt )
	clav_parCons.name =   nameSpace + clav + side + 'Jnt_parCons'
	clavZro_grp.parent( clavRig_grp )




	# = = = = = = = = = = = = = #
	#  Local / World setup 
	# = = = = = = = = = = = = = #
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( clav_ctrl , clavRig_grp , parentTo , clavZro_grp.name ,part )
	Loc_grp.name = part + side + 'Local_grp'
	World_grp.name = part + side + 'World_grp'
	WorldGrp_orientCons.name = part + side + 'WorldGrp_orientCons'
	ZroGrp_orientCons.name = part + side + 'ZroGrp_orientCons'
	reverseNode_rev.name = part + side + 'ZroGrpOrientCons_rev'


	clavRig_grp.parent( parentTo )
	print ('#### End of %s%s Rig ####' %( part , side ))
	print('\n\n\n\n\n')
	return clav_bJnt.name
	
	


