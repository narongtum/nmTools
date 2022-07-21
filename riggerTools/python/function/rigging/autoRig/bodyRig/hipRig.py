#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Pelvis rig module
# 02_hipRig

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.tools import proc as pc 
reload(pc)

from function.pipeline import logger 
reload(logger)

class HipRigLogger(logger.MayaLogger):
	LOGGER_NAME = "hipRig"

def hipRig( 	nameSpace = '' , 
				ctrl_grp = 'ctrl_grp'  ,
				tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' )	, 
				charScale = ''					,
				cogPivot = True ):

	
	
	part = nameSpace + 'cog'
	HipRigLogger.info('Start of %s rig' %part)
	# core.makeHeader('Start of %s rig' %part)

	# ctrl_grp = '%s%s' %(nameSpace,ctrl_grp) 
	# Create joint and rename to root
	rootJnt = core.Joint()
	rootJnt.name = nameSpace + 'root'

	# seting joint label
	rootJnt.attr('side').value = 0
	rootJnt.attr('type').value = 1
		
	# Specify Group name
	# Specify temp joint name
	# find charscale
	# charScale = mc.getAttr( 'template_ctrl.scaleX' )
	# Template objects
	hip = core.Dag( tmpJnt[1] )
	# Create joint at Hip
	hip_bJnt = rigTools.jointAt( hip )
	hip_bJnt.parent( rootJnt.name )

	#hip_bJnt.rename('hip_bJnt')
	hip_bJnt.name = nameSpace + 'hip_bJnt'
	# add lable
	hip_bJnt.setLable('CEN','hip')

	# Create Main group
	name = nameSpace + 'hipRig'
	hipRig_grp = core.Null()
	hipRig_grp.rename( name + '_' + 'grp')

	# Create COG controller
	cog_ctrl = core.Dag( part + '_ctrl' )
	cog_ctrl.nmCreateController('cog_ctrlShape')
	cogZro_grp = rigTools.zeroGroup( cog_ctrl )
	cogZro_grp.name = part + 'CtrlZro_grp'
	cog_ctrl.editCtrlShape( axis = charScale * 0.7 )
	cogGmbl_ctrl = core.createGimbal( cog_ctrl )
	cog_ctrl.color = 'white'
	cog_ctrl.rotateOrder = 'xzy'
	cogGmbl_ctrl.rotateOrder = 'xzy'
	
	# Parenting cog controller to cog_tmpJnt
	cogZro_grp.matchPosition( tmpJnt[0] )
	cog_ctrl.matchRotation( tmpJnt[0]  )

	# Create hip ctrl
	part = nameSpace + 'hip'
	hip_ctrl = core.Dag( part + '_ctrl' )
	hip_ctrl.nmCreateController('hips_ctrlShape')
	hip_ctrl.editCtrlShape( axis = charScale * 0.9 )
	hipZro_grp = rigTools.zeroGroup( hip_ctrl )
	hipZro_grp.name = part + 'Zro_grp'
	hipGmbl_ctrl = core.createGimbal( hip_ctrl )
	# shape adjustment
	hip_ctrl.color = 'red'

	# Parenting and positioning
	hipZro_grp.matchPosition( hip_bJnt )
	hip_ctrl.matchRotation( hip_bJnt )
	hip_ctrl.freeze()

	#cogZro_grp.parent( hipRig_grp )
	hipZro_grp.parent( cogGmbl_ctrl )

	# rotate order adjustment
	cog_ctrl.rotateOrder = 'xzy'
	hipGmbl_ctrl.rotateOrder = 'xzy'

	# Making joint parent to controller
	hipJnt_parCons = core.parentConstraint( hipGmbl_ctrl , hip_bJnt )
	hipJnt_parCons.name = part + 'Jnt_parCons'
	hipJnt_scaleCons = core.scaleConstraint( hipGmbl_ctrl , hip_bJnt )
	hipJnt_scaleCons.name = part + 'Jnt_scaleCons'

	# move cog under tohipRig_grp
	cogZro_grp.parent( hipRig_grp )
	hipRig_grp.parent( ctrl_grp )

	if cogPivot == True:
		pc.cogPivot( cog = cog_ctrl.name , cogZro = cogZro_grp.name , piorGrp = hipRig_grp.name , charScale = charScale )


	HipRigLogger.info('\n#### End of %s Rig ####' %(part))
	# print '\n#### End of %s Rig ####' %(part)
	print('\n\n\n\n\n')
	return hip_bJnt.name



#hipRig( ctrl_grp = 'ctrl_grp'  , tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' ) )




def quradpedHipRig( 	nameSpace = '' , 
						parentTo = 'ctrl_grp'   , 
						tmpJnt = 	( 	'body_tmpJnt','hip_tmpJnt' , 
										'upperBody_tmpJnt' , 'chest_tmpJnt' , 
										'lowerBody_tmpJnt' )	,
						charScale = ''	 ):

	# because of this is  Quadruped hipSpine merge hip and spine together 
	#charScale = 2					

	# Create joint and rename to root
	rootJnt = core.Joint()
	rootJnt.name = nameSpace + 'root'


	# Create spine joint
	lowerBody = core.Dag( tmpJnt[4] )
	chest = core.Dag( tmpJnt[3] )
	upperBody = core.Dag( tmpJnt[2] )
	hip = core.Dag( tmpJnt[1] )
	body = core.Dag( tmpJnt[0] )


	# Create joint at Hip
	body_bJnt = rigTools.jointAt( body )
	lowerBody_bJnt = rigTools.jointAt( lowerBody )
	chest_bJnt = rigTools.jointAt( chest )
	upperBody_bJnt = rigTools.jointAt( upperBody )
	hip_bJnt = rigTools.jointAt( hip )


	lwrName = lowerBody.makeRawName()
	hipName = hip.makeRawName()
	bodyName = body.makeRawName()
	uprName = upperBody.makeRawName()
	chestName = chest.makeRawName()


	#hip_bJnt.rename('hip_bJnt')
	body_bJnt.name = nameSpace + bodyName+ '_bJnt'
	lowerBody_bJnt.name = nameSpace + lwrName + '_bJnt'
	chest_bJnt.name = nameSpace + chestName + '_bJnt'
	upperBody_bJnt.name = nameSpace + 'upperBody_bJnt'
	hip_bJnt.name = nameSpace + 'hip_bJnt'



	# new hirachy
	# body > upper > chest
	# cog > lower > hip
	# Parenting
	hip_bJnt.parent( lowerBody_bJnt )
	chest_bJnt.parent( upperBody_bJnt )

	upperBody_bJnt.parent( body_bJnt )
	lowerBody_bJnt.parent( body_bJnt )
	body_bJnt.parent( rootJnt )


	# Specify Group name
	# Specify temp joint name
	# find charscale
	# Create Main group
	name = nameSpace + 'hipSpineRig'
	hipRig_grp = core.Null()
	hipRig_grp.rename( name + '_' + 'grp')







	# Create COG controller to the hip animal reason
	part = nameSpace + 'cog'
	cog_ctrl = core.Dag( part + '_ctrl' )
	cog_ctrl.nmCreateController('cog_ctrlShape')
	cogZro_grp = rigTools.zeroGroup( cog_ctrl )
	cogZro_grp.name = part + 'CtrlZro_grp'
	cog_ctrl.editCtrlShape( axis = charScale * 2.8 )
	cogGmbl_ctrl = core.createGimbal( cog_ctrl )
	cog_ctrl.color = 'white'
	cog_ctrl.rotateOrder = 'xzy'
	cogGmbl_ctrl.rotateOrder = 'xzy'
		
	# Parenting cog controller to cog_tmpJnt
	cogZro_grp.matchPosition( hip_bJnt )
	cog_ctrl.matchRotation( hip_bJnt  )





	print (lowerBody_bJnt.name) 
	# create lowerBody controller
	lowerBodyZro_grp , lowerBody_ctrl, lowerBody_gmblCtrl  = rigTools._creControl( 	nameSpace = nameSpace , name = lowerBody_bJnt.name  , 
													ctrlShape = 'neck_ctrlShape', charScale = 1.8 , 
													color = 'yellow' , rotateOrder = 'xzy', parentTo = cogGmbl_ctrl.name , 
													rotation = (90,0,0)  )


	# create hip controller
	hipZro_grp , hip_ctrl , hip_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = hip_bJnt.name  , 
													ctrlShape = 'hips_ctrlShape', charScale = 1.9 , 
													color = 'yellow' , rotateOrder = 'xzy', parentTo = lowerBody_gmblCtrl  , 
													rotation = (90,0,0)  )


	# create  body
	bodyZro_grp , body_ctrl, body_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = body_bJnt.name   , 
													ctrlShape = 'neck_ctrlShape', charScale = 2 , 
													color = 'yellow' , rotateOrder = 'xzy', parentTo = cogGmbl_ctrl  , 
													rotation = (90,0,0)  )
													

	# create  upperBody
	upperBodyZro_grp , upperBody_ctrl, upperBody_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = upperBody_bJnt.name   , 
													ctrlShape = 'neck_ctrlShape', charScale = 2.2 , 
													color = 'yellow' , rotateOrder = 'xzy', parentTo = body_gmblCtrl  , 
													rotation = (90,0,0)  )
													
																								
	# create  chest
	chestZro_grp , chest_ctrl, chest_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = chest_bJnt.name   , 
													ctrlShape = 'cube_ctrlShape', charScale = 20.5 , 
													color = 'yellow' , rotateOrder = 'xzy', parentTo = upperBody_gmblCtrl  , 
													rotation = (90,0,0)  )



	# move cog under to hipRig_grp
	cogZro_grp.parent( hipRig_grp )
	hipRig_grp.parent( parentTo )

	print ('\n#### End of %s Rig ####' %(part))
	print('\n\n\n\n\n')
	return chest_bJnt.name , hip_bJnt.name
