# New Spine Rig
from function.framework.reloadWrapper import reloadWrapper as reload
# PS : RUN THIS AFTER HIP AND SETUP RIG NAJA
import maya.cmds as mc
from function.rigging.tools import dTool as dc 
reload(dc)
from function.rigging.tools import proc as pc 
reload(pc)
from function.rigging.autoRig.base import core
reload(core)
from function.rigging.autoRig.base import rigTools
reload( rigTools )
from function.rigging.feature import localWorld as lcw
reload( lcw )

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)

def torsoRig( nameSpace = '', ctrl_grp = 'ctrl_grp', tmpJnt = ( 'spine01_tmpJnt', 'spine02_tmpJnt' ), charScale = 1 ):

	core.makeHeader('Start of torso Rig')
	cogCtrl = 'cog_gmbCtrl'
	pior = 'hip_tmpJnt'
	piorCtrl = pior.split('_')[0] + '_ctrl'
	piorJnt = pior.split('_')[0] + '_bJnt'

	# start with Name
	ns = nameSpace
	spNoTouch = dc.lock_grp( ns + 'spine_noTouch_grp' )
	flc_grp = dc.lock_grp( ns + 'spineIKFlc_grp' )
	dc.hide( flc_grp )
	rev = 'spine' + '_rev'
	mc.parent( flc_grp, spNoTouch)
	mc.parent( spNoTouch, 'noTouch_grp')

	# Create Group and parent
	rig_grp = dc.lock_grp( ns + 'spineRig_grp' )
	IK_grp = dc.lock_grp( ns + 'spineIK_grp' )
	FK_grp = dc.lock_grp( ns + 'spineFK_grp' )
	IK_Ctrl_grp = dc.lock_grp( ns + 'spineIKCtrl_grp' )
	mc.parent( IK_grp, FK_grp, rig_grp )
	mc.parent( IK_Ctrl_grp, IK_grp )
	mc.parent( rig_grp, ctrl_grp )

	#switchZro = ns + 'spineSwitch' + 'Zro_grp'
	IK_FK = ns + 'cog_ctrlShape' + '.IK_FK'

	# switch ctrl
	switch_ctrl = core.Dag( 'cog_ctrlShape' )

	'''
	switch_ctrl.nmCreateController('diamond_ctrlShape' )
	switch_ctrl.editCtrlShape( axis = charScale * 1 )
	switch_ctrl.color = 'yellow'
	switch_ctrl.hideArnoldNode()
	switchZro_grp = rigTools.zeroGroup( switch_ctrl )
	switchZro_grp.name = switchZro

	mc.parent( switchZro, rig_grp )
	dc.allMat( switchZro_grp , piorJnt )
	mc.setAttr( switchZro + '.tx', charScale * 12 )
	dc.parCon( piorJnt, switchZro )

	dc.blankCtrl( switch_ctrl )
	'''
	mc.addAttr( switch_ctrl , ln = 'IK_FK', sn = 'ikfk', attributeType = 'float', k = True, min = 0, max = 1 , dv = 1)
	mc.createNode( 'reverse', n = rev )
	
	# Con rev to fk grp
	mc.connectAttr( IK_FK, rev + '.inputX' )
	# Con rev to fk grp
	mc.connectAttr( rev + '.inputX', FK_grp + '.v' )

	# FK start here -----------------------------------------------------------------------
	bJntList = []
	# joint dup and parent
	for i in range(len(tmpJnt)):
		# Name
		tmp = tmpJnt[i]
		name = tmp.split('_tmpJnt')[0]
		bJnt = name + '_bJnt'
		fkJnt = name + '_fkJnt'
		ikJnt = name + '_ikJnt'

		bJntList.append( bJnt )
		# fk
		fk_Ctrl = core.Dag( name + '_ctrl' )
		fk_Ctrl.nmCreateController('neck_ctrlShape')
		fk_Ctrl.editCtrlShape( axis = charScale * 1 )
		fk_Ctrl.color = 'yellow'
		fk_Ctrl.hideArnoldNode()

		fkZro_grp = rigTools.zeroGroup( fk_Ctrl )
		fkZro_grp.name = name + 'Zro_grp'
		dc.allMat( fkZro_grp , tmp )
		# Command
		mc.select( cl = True )
		mc.joint( n = bJnt )
		mc.setAttr( bJnt + '.segmentScaleCompensate', + 0 )
		dc.allMat( bJnt, tmp )

		mc.select( bJnt, r = True)
		mc.makeIdentity( apply=True, t=1, r=1, s=1, n=0)
		mc.select( cl = True )

		mc.duplicate( bJnt, n = fkJnt )
		mc.duplicate( bJnt, n = ikJnt )
		if i == 0:
			mc.parent( bJnt, 'hip_bJnt' )
			mc.parent( fkZro_grp, FK_grp )
			mc.parent( fkJnt, FK_grp )
			mc.parent( ikJnt, IK_grp )
			dc.parCon( cogCtrl, fkZro_grp.name )

		elif i > 0:
			# upName
			upName = tmpJnt[i-1].split('_tmpJnt')[0]
			upBind = upName + '_bJnt'
			upFK = upName + '_fkJnt'
			upIK = upName + '_ikJnt'
			upCtrl = upName + '_ctrl'
			# Command
			mc.parent( bJnt, upBind )
			mc.parent( fkJnt, upFK )
			mc.parent( ikJnt, upIK )

			mc.parent( fkZro_grp, upCtrl )

		dc.hide( fkJnt )
		dc.hide( ikJnt )
		dc.parCon( fk_Ctrl, fkJnt )
		cons = dc.parCon( [ikJnt,fkJnt], bJnt )
		mc.connectAttr( rev + '.outputX', cons + '.w0' )
		mc.connectAttr( rev + '.inputX', cons + '.w1' )

	# IK Start Here ----------------------------------------------------------------------
	
	# jointCreate and MAT
	chestJnt = mc.joint( n = 'chest_ikJnt' )
	backJnt = mc.joint( n = 'back_ikJnt' )
	hipJnt = mc.joint( n = 'hip_ikJnt' )
	dc.allMat( chestJnt, tmpJnt[-1] )
	dc.allMat( backJnt, tmpJnt[0] )
	dc.parCon( 'hip_bJnt', hipJnt, mo = 0)
	mc.parent( chestJnt, IK_grp )
	mc.parent( backJnt, IK_grp )
	mc.parent( hipJnt, IK_grp )
	dc.hide( chestJnt )
	dc.hide( backJnt )
	dc.hide( hipJnt )

	topSkinJnt = core.Dag( chestJnt )
	btmSkinJnt = core.Dag( hipJnt )

	# controlCreate and MAT
	chest = core.Dag( 'chest' + '_ctrl' )
	back = core.Dag( 'back' + '_ctrl' )
	# chestCtrl
	chest.nmCreateController( 'spine_ctrlShape' )
	chest.editCtrlShape( axis = charScale * .8 )
	chest.color = 'red'
	chest.hideArnoldNode()
	chestCtrl = chest.name
	chestZro = rigTools.zeroGroup( chest )
	chestZro.name = 'chest' + 'Zro_grp'
	# backCtrl
	back.nmCreateController( 'square_ctrlShape' )
	back.editCtrlShape( axis = charScale * 10 )
	back.color = 'blue'
	back.hideArnoldNode()
	backZro = rigTools.zeroGroup( back )
	backZro.name = 'back' + 'Zro_grp'

	# match to joint
	dc.allMat( chestZro , tmpJnt[-1] )
	dc.allMat( backZro , tmpJnt[0] )
	# parent in GRP and Cons
	mc.parent( chestZro, IK_Ctrl_grp )
	mc.parent( backZro, IK_Ctrl_grp )
	dc.parCon( chest, chestJnt)
	# connect to hide VIS
	mc.connectAttr( rev + '.outputX', 'chest' + 'Zro_grp' + '.v' )
	mc.connectAttr( rev + '.outputX', 'back' + 'Zro_grp' + '.v' )
	# IK non-touch
	nrb = 'spineIK_nrb'
	nrbSkin = core.Dag( nrb )
	mc.nurbsPlane( n = nrb, ch = False, v = 1, u = 4)
	dc.hide( nrb )
	mc.setAttr( nrb + '.ry', -90 )
	mc.setAttr( nrb + '.rx', 90 )
	mc.setAttr( nrb + '.ty', .5 )
	mc.makeIdentity( nrb, apply = True, t=1, r=1, s=1 )
	mc.makeIdentity( nrb, apply = False, t=1, r=1, s=1 )

	# MAT nrb to piorJnt
	dc.allMat( nrb, piorJnt )

	scale = []
	for jnt in bJntList:
		getScale = mc.getAttr( jnt + '.ty' )
		scale.append( getScale )
		if jnt == bJntList[0]:
			ratioJnt = getScale

	lenght = sum(scale)
	backPos = ratioJnt/lenght
	print ('lenght' , lenght)
	print ('back' , backPos)
	mc.setAttr( nrb + '.sy', lenght )
	mc.makeIdentity( nrb, apply = True, t=1, r=1, s=1 )
	mc.parent( nrb, spNoTouch )

	# flc create
	for f in range(3):
		name = 'spine%02d' %(f+1)
		ikJnt = name + '_ikJnt'
		flc = name + '_flc'
		flcShp = flc + 'Shape'
		mc.createNode( 'follicle', n = flcShp )
		mc.setAttr( flcShp + '.pv', 0.5 )
		# flc
		mc.connectAttr( flcShp + '.outTranslate', flc + '.translate' )
		mc.connectAttr( flcShp + '.outRotate', flc + '.rotate' )
		# nrb
		mc.connectAttr( nrb + '.local' , flcShp + '.inputSurface' )
		mc.connectAttr( nrb + '.worldMatrix[0]' , flcShp + '.inputWorldMatrix' )
		if f == 0:
			mc.setAttr( flcShp + '.pu', 0 )
			dc.parCon( backJnt, ikJnt )
		elif f == 1:
			mc.setAttr( flcShp + '.pu', backPos )
			dc.parCon( flc, 'back' + 'Zro_grp' )
		elif f == 2:
			mc.setAttr( flcShp + '.pu', 1 )
			topIK = 'spine%02d' %(f) + '_ikJnt'
			dc.parCon( flc, topIK )
		mc.parent( flc, flc_grp )

	# Next Step
	dc.parCon( 'back' + '_ctrl', backJnt )
	nrb_skc = core.SkinCluster( topSkinJnt.name, btmSkinJnt.name, nrbSkin.name, dr = 2 , mi = 2 )
	nrb_skc.name =  nrb + '_skc'

	# IK TO FOLLOW COG #
	lcw.localWorld( fromSel = False, giveCtrl =  ['chest' + '_ctrl']  , ori = False, worldCtrl = 'ctrl_grp' )
	dc.parCon( cogCtrl, 'chestLoc_grp' )

	# CLEAR CTRL VIS
	# IF YOU WANT TO CLEAR VIS FOR *_CTRL
	#pc.clearVis()

	print ('\n#### End of %s Rig ####' %('torso'))
	print('\n\n\n\n\n')


	# for return only
	lastSpine = (tmpJnt[-1].split('_')[0]) + '_bJnt'
	return lastSpine



# for test na ja
#torsoRig( nameSpace = '', ctrl_grp = 'ctrl_grp', tmpJnt = ( 'spine01_tmpJnt', 'spine02_tmpJnt' ), charScale = 1 )
#mc.delete( 'COG_tmpJnt' )