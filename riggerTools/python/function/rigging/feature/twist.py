# TWIST TEST

# PS : RUN THIS AFTER HIP AND SETUP RIG NAJA
import maya.cmds as mc
from function.rigging.autoRig.base import core
reload(core)
from function.rigging.tools import dTool as dc 
reload(dc)
from function.rigging.tools import proc as pc 
reload(pc)
from function.rigging.autoRig.base import core
reload(core)

def twistRig( nameSpace = '', stJnt = 'lowerArmLFT_bJnt', enJnt = 'handLFT_bJnt' , charScale = 1 ):

	# start with Name
	ns = nameSpace
	twist_grp = ns + 'twist_noTouch_grp'
	flc_grp = ns + 'twistFlc_grp'

	if mc.objExists( twist_grp ) == 0:
		dc.lock_grp( ns + 'twist_noTouch_grp' )
		dc.lock_grp( flc_grp )
		dc.hide( flc_grp )
		mc.parent( flc_grp, twist_grp )
		mc.parent( twist_grp, 'noTouch_grp' )

	# start here
	stName = stJnt.split('_')[0]
	print stName
	enName = enJnt.split('_')[0]
	print enName
	
	side = enName[-3:]
	print side

	preName = enName.split( side )[0]
	twName = preName + 'Twist' + side
	twJnt =  twName + '_bJnt' 
	# twist nrb
	nrb = twName + '_nrb'
	nrbSkin = core.Dag( nrb )
	mc.nurbsPlane( n = nrb, ch = False, v = 1, u = 4)
	dc.hide( nrb )
	mc.setAttr( nrb + '.ry', -90 )
	mc.setAttr( nrb + '.rx', 90 )
	mc.setAttr( nrb + '.ty', .5 )
	mc.makeIdentity( nrb, apply = True, t=1, r=1, s=1 )
	mc.makeIdentity( nrb, apply = False, t=1, r=1, s=1 )

	# MAT nrb to piorJnt
	dc.allMat( nrb, stJnt )
	mc.joint( n = twJnt )
	getScale = mc.getAttr( enJnt + '.ty' )
	mc.setAttr( nrb + '.sy', getScale )
	mc.makeIdentity( nrb, apply = True, t=1, r=1, s=1 )
	mc.parent( nrb, twist_grp )

	# nrb skinCluster
	stSkinJnt = core.Dag( stJnt )
	enSkinJnt = core.Dag( enJnt )
	nrb_skc = core.SkinCluster( stSkinJnt.name, enSkinJnt.name, nrbSkin.name, dr = 10 , mi = 2 )
	nrb_skc.name =  nrb + '_skc'


	flc = twName + '_flc'
	flcShp = flc + 'Shape'
	mc.createNode( 'follicle', n = flcShp )
	# flc
	mc.connectAttr( flcShp + '.outTranslate', flc + '.translate' )
	mc.connectAttr( flcShp + '.outRotate', flc + '.rotate' )
	# nrb
	mc.connectAttr( nrb + '.local' , flcShp + '.inputSurface' )
	mc.connectAttr( nrb + '.worldMatrix[0]' , flcShp + '.inputWorldMatrix' )
	# set
	mc.setAttr( flcShp + '.pv', 0.5 )
	mc.setAttr( flcShp + '.pu', 0.5 )

	dc.allMat( twJnt, flc)
	mc.makeIdentity( twJnt, apply = True, t=1, r=1, s=1 )
	dc.oriCon( flc, twJnt, mo = 1 )
	mc.parent( flc, flc_grp )
	mc.parent( twJnt, stJnt )


#twistRig( nameSpace = '', stJnt = 'lowerArmLFT_bJnt', enJnt = 'handLFT_bJnt' , charScale = 1 )
#twistRig( nameSpace = '', stJnt = 'lowerArmRGT_bJnt', enJnt = 'handRGT_bJnt' , charScale = 1 )