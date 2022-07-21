# Creature Rig

import maya.cmds as mc
from function.rigging.tools import dTool as dc 
reload(dc)
from function.rigging.tools import proc as pc 
reload(pc)
from function.rigging.autoRig.base import core
reload(core)
from function.rigging.autoRig.base import rigTools
reload(rigTools)
from function.rigging.autoRig import util 
reload(util)


def createMasterGrp( nameSpace = '' , charScale = ''):
	part = 'master controller'

	# Create empty Node
	rig_grp = core.Null( 'rig_grp'  )
	noTouch_grp = core.Null('noTouch_grp' ) # Change still to no touch grp
	jnt_grp = core.Null('jnt_grp' )
	ikh_grp = core.Null('ikh_grp'  )
	ctrl_grp = core.Null('ctrl_grp' )

	# Snap null make for FK/IKmatcher
	snapNull_grp = core.Null('snapNull_grp' )
	# Create controller
	master_ctrl = core.Dag( 'master_ctrl'  )
	master_ctrl.nmCreateController( 'placement_ctrlShape' )
	master_ctrl.editCtrlShape( axis = charScale * .5 )
	master_ctrl.renameShape( master_ctrl.shape )
	master_ctrl.setColor( 'yellow' )

	# Create controller
	# placement_ctrl = core.Dag( '%s%splacement_ctrl' %( charName , elem ) )
	placement_ctrl = core.Dag( 'placement_ctrl'  )
	placement_ctrl.nmCreateController( 'fly_ctrlShape' )
	
	placement_ctrl.editCtrlShape( axis = charScale * .5 )
	#placement_ctrl.addAttribute( ln = 'size' , k = True , dv = 1 )
	placement_ctrl.setColor('white')

	# Lock and Hide attr
	'''
	for attr in ('sx','sy','sz'):
		placement_ctrl.attr(attr).lockHide()
	'''

	# parenting grp used parent
	# call parent function
	master_ctrl.parent( rig_grp )
	placement_ctrl.parent( master_ctrl )
	ctrl_grp.parent( placement_ctrl )
	jnt_grp.parent( placement_ctrl )
	ikh_grp.parent( placement_ctrl )
	noTouch_grp.parent( rig_grp )
	snapNull_grp.parent( noTouch_grp )
	master_ctrl.rotateOrder = 'xzy'
	placement_ctrl.rotateOrder = 'xzy'

	for attr in ('tx','ty','tz','rx','ry','rz','sx','sy','sz'):
		rig_grp.attr(attr).lockHide()
		jnt_grp.attr(attr).lockHide()
		ikh_grp.attr(attr).lockHide()
		noTouch_grp.attr(attr).lockHide()

	print '\n#### End of %s Rig ####' %(part)

def rootRig( nameSpace = '' ):

	# creat joint and name root
	rootJnt = core.Joint()
	rootJnt.name = nameSpace + 'root'
	# set joint label
	rootJnt.attr('side').value = 0
	rootJnt.attr('type').value = 1
	return rootJnt.name

def hipRig( 	nameSpace = '' , 
				ctrl_grp = 'ctrl_grp'  ,
				tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' )	, 
				root = '' ,
				charScale = ''					):

	hip = core.Dag( tmpJnt[1] )
	# Create joint at Hip
	hip_bJnt = rigTools.jointAt( hip )
	hip_bJnt.parent( root )

	#hip_bJnt.rename('hip_bJnt')
	hip_bJnt.name = nameSpace + 'hip_bJnt'
	# add lable
	hip_bJnt.setLable('CEN','hip')

	# Create Main group
	name = nameSpace + 'hipRig'
	hipRig_grp = core.Null()
	hipRig_grp.rename( name + '_' + 'grp')

	# Create COG controller
	part = nameSpace + 'cog'
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

	print '\n#### End of %s Rig ####' %(part)
	return hip_bJnt.name


#createMasterGrp( nameSpace = '' , charScale = 1)
'''
hipRig( 	nameSpace = '' 								, 
			ctrl_grp = 'ctrl_grp'  						,
			tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' )	, 
			root = '' 									,
			charScale = '')

'''
#mc.connectAttr( cogOff_ctrl.translate, cogCtrlZro_grp.rotatePivot , f = True)
#mc.connectAttr( cogOff_ctrl.translate, cogCtrlZro_grp.scalePivot , f = True)




def headRig( 	nameSpace = '',
				ctrl_grp = 'ctrl_grp'  ,
				tmpJnt = ( 'head_tmpJnt' )	, 
				parentTo = '' ,
				charScale = ''	):
	

	head = core.Dag( tmpJnt )

	# Create joint at Head
	head_bJnt = rigTools.jointAt( head )
	head_bJnt.parent( parentTo )
	head_bJnt.name = nameSpace + 'head_bJnt'

	# add lable
	head_bJnt.setLable('CEN','head')

	# Create Main group
	name = nameSpace + 'headRig'
	headRig_grp = core.Null()
	headRig_grp.rename( name + '_' + 'grp')

	# Create head ctrl
	part = nameSpace + 'head'
	head_ctrl = core.Dag( part + '_ctrl' )
	head_ctrl.nmCreateController('cubeExpand_ctrlShape')
	head_ctrl.editCtrlShape( axis = charScale * 5 )
	headZro_grp = rigTools.zeroGroup( head_ctrl )
	headZro_grp.name = part + 'Zro_grp'
	headGmbl_ctrl = core.createGimbal( head_ctrl )
	# shape adjustment
	head_ctrl.color = 'yellow'

	# Parenting and positioning
	headZro_grp.matchPosition( head_bJnt )
	head_ctrl.matchRotation( head_bJnt )
	head_ctrl.freeze()

	headZro_grp.parent( headRig_grp )

	# rotate order adjustment
	headGmbl_ctrl.rotateOrder = 'xzy'

	dc.parCon( head_ctrl.name, head_bJnt.name )
	dc.sclCon( head_ctrl.name, head_bJnt.name )

	# parent main grp
	headRig_grp.parent( ctrl_grp )
	dc.parCon( parentTo, headRig_grp.name )

	return head_bJnt.name


def bodyRig( 	nameSpace = '',
				ctrl_grp = 'ctrl_grp'  ,
				tmpJnt = ( 'body_tmpJnt' )	, 
				parentTo = '' ,
				charScale = ''	):
	

	body = core.Dag( tmpJnt )

	# Create joint at body
	body_bJnt = rigTools.jointAt( body )
	body_bJnt.parent( parentTo )
	body_bJnt.name = nameSpace + 'body_bJnt'

	# add lable
	body_bJnt.setLable('CEN','body')

	# Create Main group
	name = nameSpace + 'bodyRig'
	bodyRig_grp = core.Null()
	bodyRig_grp.rename( name + '_' + 'grp')

	# Create body ctrl
	part = nameSpace + 'body'
	body_ctrl = core.Dag( part + '_ctrl' )
	body_ctrl.nmCreateController('cube_ctrlShape')
	body_ctrl.editCtrlShape( axis = charScale * 5 )
	bodyZro_grp = rigTools.zeroGroup( body_ctrl )
	bodyZro_grp.name = part + 'Zro_grp'
	bodyGmbl_ctrl = core.createGimbal( body_ctrl )
	# shape adjustment
	body_ctrl.color = 'yellow'

	# Parenting and positioning
	bodyZro_grp.matchPosition( body_bJnt )
	body_ctrl.matchRotation( body_bJnt )
	body_ctrl.freeze()

	bodyZro_grp.parent( bodyRig_grp )

	# rotate order adjustment
	bodyGmbl_ctrl.rotateOrder = 'xzy'

	dc.parCon( body_ctrl.name, body_bJnt.name )
	dc.sclCon( body_ctrl.name, body_bJnt.name )

	# parent main grp
	bodyRig_grp.parent( ctrl_grp )
	dc.parCon( parentTo, bodyRig_grp.name )

	return body_bJnt.name


def fkChainRig( 	nameSpace = '',
					ctrl_grp = 'ctrl_grp'  ,
					tmpJnt = ( 'upLegLFT_tmpJnt', 'midLegLFT_tmpJnt' )	,
					ctrlShape = 'circle_ctrlShape'  , 
					parentTo = '' ,
					charScale = ''	):

	# head grp create
	findChainName = tmpJnt[0].split('_')[0]
	chainHead = findChainName + 'Rig_grp'
	chainHeadRig_grp = core.Null( chainHead )
	chainHeadRig_grp.parent( ctrl_grp )
	side = findChainName[-3:] 

	

	for i in range(len(tmpJnt)):
		name = nameSpace + tmpJnt[i].split('_')[0]
		ctrl = name + '_ctrl'
		bJnt = name + '_bJnt'

		# create joint
		chain = core.Dag( tmpJnt[i] )
		chain_bJnt = rigTools.jointAt( chain )
		chain_bJnt.name = nameSpace + bJnt

		# create ctrl
		chain_ctrl = core.Dag( name + '_ctrl' )

		chain_ctrl.nmCreateController( ctrlShape ) # Add ctrl shape free

		chain_ctrl.editCtrlShape( axis = charScale * 2 )
		chainZro_grp = rigTools.zeroGroup( chain_ctrl )
		chainZro_grp.name = name + 'Zro_grp'
		chainGmbl_ctrl = core.createGimbal( chain_ctrl )

		# parenting and positioning
		chainZro_grp.matchPosition( chain_bJnt )
		chainZro_grp.matchRotation( chain_bJnt )
		chain_ctrl.freeze()

		# color adjustment
		if side == 'LFT':
			print 'LFT'
			chain_ctrl.color = 'red'
		elif side == 'FRN':
			print 'FRN'
			chain_ctrl.color = 'yellow'
		elif side == 'CNT':
			print 'CNT'
			chain_ctrl.color = 'yellow'
		elif side == 'BCK':
			print 'BCK'
			chain_ctrl.color = 'yellow'
		elif side == 'RGT':
			print 'RGT'
			chain_ctrl.color = 'blue'
		else:
			print 'Normal'
			chain_ctrl.color = 'yellow' 

		# parent to upJnt and upCtrl
		if i == 0:	
			chain_bJnt.parent( parentTo )
			chainZro_grp.parent( chainHeadRig_grp )
			dc.parCon( parentTo, chainZro_grp.name )
			
		else:
			up_name = tmpJnt[i-1].split('_')[0]
			up_bJnt = up_name + '_bJnt'
			up_ctrl = up_name + '_ctrl'

			# parent 
			chain_bJnt.parent( up_bJnt )
			chainZro_grp.parent( up_ctrl )

		# do parent Con
		dc.parCon( chain_ctrl.name, chain_bJnt.name )
		dc.sclCon( chain_ctrl.name, chain_bJnt.name )


	return chainHeadRig_grp.name
	








'''
# RUN TEST
charScale = 5
createMasterGrp( nameSpace = '' , charScale = charScale)

rootJnt = rootRig( nameSpace = '' )

hipJnt = hipRig( 	nameSpace = '' , 
					ctrl_grp = 'ctrl_grp'  ,
					tmpJnt = ( 'cog_tmpJnt','body_tmpJnt' )	, 
					root = rootJnt ,
					charScale = charScale					)

headJnt = headRig( 	nameSpace = '',
					ctrl_grp = 'ctrl_grp'  ,
					tmpJnt = ( 'head_tmpJnt' )	, 
					parentTo = hipJnt ,
					charScale = charScale	)


legLFT = fkChainRig( 	nameSpace = '',
						tmpJnt = ( 'upLegLFT_tmpJnt', 'midLegLFT_tmpJnt' )	,
						ctrl_grp = 'ctrl_grp', parentTo = hipJnt, charScale = charScale)

legRGT = fkChainRig( 	nameSpace = '',
						tmpJnt = ( 'upLegRGT_tmpJnt', 'midLegRGT_tmpJnt' )	,
						ctrl_grp = 'ctrl_grp', parentTo = hipJnt, charScale = charScale)

legBCK = fkChainRig( 	nameSpace = '',
						tmpJnt = ( 'upLegBCK_tmpJnt', 'midLegBCK_tmpJnt' )	,
						ctrl_grp = 'ctrl_grp', parentTo = hipJnt, charScale = charScale)

util.cleanup()
'''