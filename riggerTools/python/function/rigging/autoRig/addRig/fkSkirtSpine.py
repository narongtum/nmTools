# rigging.autoRig.addRig

"""
from function.rigging.autoRig.addRig import fkSkirtSpine as fse
reload(fse)

"""

from function.pipeline import logger
from function.rigging.autoRig.addRig import createFkRig
from function.rigging.util import misc as misc
from function.rigging.autoRig.base import rigTools
from maya import cmds as mc
import pymel.core as pm
import maya.mel as mel

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

reload(rigTools)

reload(misc)

reload(logger)


class DynLogger(logger.MayaLogger):
	LOGGER_NAME = "fkSpineLogger"


def fkSkirtSpline(
	side='RGT',
	baseName='jacketAA',
	firstJnt='jacketAA01RGT_bJnt',
	lastJnt='jacketAA01RGT_bJnt',
	charScale=1,
	nameSpace='',
	curlCtrl=False,
	nbrOfCtrl=3,
	parentTo='ctrl_grp',
	priorJnt='joint1',
	ctrlShape='cube_ctrlShape'
):

	if mc.objExists(firstJnt) and mc.objExists(lastJnt):
		pass
	else:
		raise RuntimeError('No joint attached found.')

	# make spIkJnt Chain
	spIkJnt = mc.duplicate(firstJnt, rr=1)
	mc.select(spIkJnt, hi=1)

	lastName = misc.findLastName(firstJnt)
	misc.searchReplace(searchText=lastName, replaceText='ikJnt')
	spIkJnt = misc.searchReplace(searchText='ikJnt1', replaceText='ikJnt')
	pm.select(clear=True)

	mc.parent(spIkJnt[0], world=True)

	# define joint chain
	mc.select(cl=1)
	mc.select(firstJnt, hi=1)
	jntChain = mc.ls(sl=1)
	lastJntIndx = jntChain.index(lastJnt)
	#del jntChain [(lastJntIndx + 1):]

	# redesign of vtx number
	jntsReduce = []
	for jnt in range(len(jntChain)):
		if jnt == 0:
			jntsReduce.append(jntChain[jnt])
		elif jnt % 2:
			jntsReduce.append(jntChain[jnt])
		elif jnt == len(jntChain):
			jntsReduce.append(jntChain[jnt])

	# create curve prepare for ik skine rig
	jntsPositions = []
	# for jnt in jntChain:
	for jnt in jntsReduce:
		jntPos = mc.xform(jnt, q=1, ws=1, t=1)
		jntsPositions.append(jntPos)

	rawCrv = mc.curve(d=3, ep=jntsPositions)
	baseCrv = mc.rename(rawCrv, baseName + side + "Dyn_baseCurve")
	mc.rebuildCurve(baseCrv, rpo=1, rt=0, end=1, kr=0,
					kcp=0, kep=1, kt=1, s=2, d=3, tol=0.01)

	# create curve prepare for ik skine rig

	if not nbrOfCtrl:
		# create fk control
		nbrOfCtrl = len(jntChain)  # number of control
		DynLogger.info('Using specific joint number: %s ' % nbrOfCtrl)

	if nbrOfCtrl == 0:
		mc.error("You have to create at least two FK control.")
	# elif nbrOfCtrl == 2:
	#   mc.error ("The number of FK controls can't be superior to the number of joints in the chain.")
	elif nbrOfCtrl > len(jntChain):
		mc.error(
			"The number of FK controls can't be superior to the number of joints in the chain.")

	# create Temp joint for fk joint chain
	origCrv = baseCrv
	x = 0
	fkJntChain = []
	radius = mc.joint(firstJnt, q=1, rad=1)[0]
	crv = mc.duplicate(origCrv, rr=1)
	mc.rebuildCurve(crv, rpo=1, rt=0, end=1, kr=0,
					kcp=0, kep=1, kt=1, s=20, d=3, tol=0)

	# no need to check , check this condition as abrove
	# if nbrOfCtrl >= 2:
	DynLogger.info('This number of ctrl is more than two.')

	# for make output following arg that user want
	nbrOfCtrl = nbrOfCtrl - 1

	# change condition (edit#v 2)
	# for x in range (x, nbrOfCtrl + 1, x + 1):
	for x in range(x, nbrOfCtrl + 1, x + 1):
		# for x in range (nbrOfCtrl):
		incr = (1.0/nbrOfCtrl) * x
		ptOnCrvPos = mc.pointOnCurve(crv, pr=incr)
		rawFkJnt = mc.joint(rad=radius*0.75)
		fkJnt = mc.rename(rawFkJnt, baseName + "0%d_temp" % (x + 1) + side)
		fkJntChain.append(fkJnt)
		mc.xform(ws=1, t=ptOnCrvPos)
	mc.delete(crv)
	# Orient FK joint chain
	# mc.joint (fkJntChain[0], e = 1, oj = "yzx", secondaryAxisOrient = "yup", ch = 1, zso = 1)
	# fix the orientation
	mc.joint(fkJntChain[0], e=1, oj="yxz",
			 secondaryAxisOrient="xdown", ch=1, zso=1)
	mc.setAttr(fkJntChain[-1] + ".jointOrientX", 0)
	mc.setAttr(fkJntChain[-1] + ".jointOrientY", 0)
	mc.setAttr(fkJntChain[-1] + ".jointOrientZ", 0)
	# return fkJntChain
	DynLogger.info('%s is joint chain.' % fkJntChain)

	# MAKE TEMP JOINT TO IK JOINT
	# make controllre and parenting my method

	reload(createFkRig)

	# dup fk joint chain to ik joint
	ikSpGen_jnt_grp = createFkRig.newCreateFkRig(nameSpace='',  name=baseName + 'Ik', parentTo='',
												 tmpJnt=fkJntChain,
												 charScale=1, priorJnt='',
												 side=side, ctrlShape=ctrlShape, localWorld=False,
												 color='white', curlCtrl=curlCtrl, suffix='_drivJnt')

	pm.delete(fkJntChain)

	# skin ik joint to curve

	# add all joint (edit#v 2)
	mc.select(ikSpGen_jnt_grp[2], baseCrv, r=1)

	# mc.select (ikSpGen_jnt_grp[2], baseCrv, r = 1)
	# mc.select (fkJntChain[:-1], baseCrv, r = 1)
	mc.skinCluster(n=baseName + side + "Dyn_Fk_skinCluster", tsb=1,
				   bm=0, sm=0, nw=1, wd=0, mi=5, omi=1, dr=4, rui=1)

	dynFkSplineRaw = mc.ikHandle(
		sol="ikSplineSolver", ccv=0, pcv=0, sj=spIkJnt[0], ee=spIkJnt[-1], c=origCrv)
	dynFkSpline = mc.rename(dynFkSplineRaw[0], baseName + side + "Manual_ikh")
	mc.rename(dynFkSplineRaw[1], baseName + side + "Manual_eff")
	mc.setAttr(dynFkSpline + ".visibility", 0)

	# making pair psCon between fk << bJnt >> ik
	# fkChain = spFk_jnt_grp

	# Fkjnt
	ikChain = spIkJnt
	# bjnt
	bJntChain = jntChain


	num = 0
	for i in range(len(bJntChain)):
		# psCon = mc.parentConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_buffJnt'  , name = each + 'Switch' + side + '_parCons' )
		print '# # # pair constraint # # #'
		print baseName + '%02d%s_psCon' % ((num + 1), side)
		# print fkChain[i]
		print ikChain[i]
		print bJntChain[i]

		# psCon = mc.parentConstraint( fkChain[i] , ikChain[i] , bJntChain[i] , name = baseName + '%02d%s_psCon' %(( num +1),side) )
		psCon = mc.parentConstraint(
			ikChain[i], bJntChain[i], name=baseName + '%02d%s_psCon' % ((num + 1), side))

	# make fkSpine twistable
	ctrlShape = mc.listHistory(ikSpGen_jnt_grp[3][0])[0]
	fk_ctrl = core.Dag(ctrlShape)
	fk_ctrl.addAttribute( longName = 'Twist' , defaultValue = 0 , keyable = True )
	fk_ctrl.addAttribute( longName = 'Roll' , defaultValue = 0 , keyable = True )

	mc.connectAttr(fk_ctrl.name + '.Twist', dynFkSpline+'.twist')
	mc.connectAttr(fk_ctrl.name + '.Roll', dynFkSpline+'.roll')
	
	
	
	mc.setAttr( '{0}.visibility'.format(ikSpGen_jnt_grp[2][0].name), 0 )

	DynLogger.info('Return name: {0}, {1}, {2}'.format(
		origCrv, ikSpGen_jnt_grp[1], ikSpGen_jnt_grp[2][0], dynFkSpline))
		
	return (
		origCrv, ikSpGen_jnt_grp[1], ikSpGen_jnt_grp[2][0], dynFkSpline, ikChain[0])

	'''    
	crv_grp = mc.group (n = baseName + side + "Crv_grp", em = 1)    
	jnt_grp = mc.group (n = baseName + side + "Jnt_grp", em = 1)   
	ctrl_grp = mc.group (n = baseName + side + "Ctrl_grp", em = 1)  
	'''




'''



sample = fkSkirtSpline(
	side='RGT',
	baseName='jacketAA',
	firstJnt='jacketAA01RGT_bJnt',
	lastJnt='jacketAA01RGT_bJnt',
	charScale=1,
	nameSpace='',
	curlCtrl=False,
	nbrOfCtrl=3,
	parentTo='ctrl_grp',
	priorJnt='joint1',
	ctrlShape='cube_ctrlShape'
)
'''