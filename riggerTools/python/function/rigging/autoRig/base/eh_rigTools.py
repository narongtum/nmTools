# -*- coding: utf-8 -*-
# ...
# ... DESCRIPTION: Enhanced Rigging Tools (eh_rigTools.py)
# ... ใช้ฟังก์ชันชื่อเดียวกับ rigTools.py เดิม แต่ปรับปรุงการคืนค่า (Return)
# ... ให้เป็น Object เพื่อความต่อเนื่องของระบบ
# ...

from function.framework.reloadWrapper import reloadWrapper as reload
import maya.cmds as mc
import pymel.core as pm

from function.rigging.autoRig.base import core
reload(core)

from function.pipeline import logger 
reload(logger)

class RigToolsLogger(logger.MayaLogger):
	LOGGER_NAME = "EHRigTools"


# ... return core.Dag objects
def zroNewGrpWithOffset(obj):

	
	child = core.Dag(obj) 
	

	name = core.check_name_style(name=child.name)[0]

	zro_grp = core.Null(name + 'Zro_grp')
	offset_grp = core.Null(name + 'Offset_grp')

	offset_grp.parent(zro_grp)
	zro_grp.snap(child)
	child.parent(offset_grp)


	return zro_grp, offset_grp



def jointAt(obj, orient=True):

	target = core.Dag(obj)
	jnt = core.Joint() 

	if orient:
		jnt.maSnap(target)
	else:
		jnt.maSnap(target, pos=True, rot=False, scl=True)

	jnt.freeze(r=True, s=True)
	jnt.rotateOrder = target.rotateOrder
	jnt.attr('segmentScaleCompensate').value = 0
	
	mc.select(cl=True)


	return jnt




def _creControl(nameSpace, 
				name, # ... ชื่อ Joint ที่จะ Match
				ctrlShape, 
				rotateOrder='yzx', 
				parentTo=None, # ... ควรเป็น core.Dag object
				charScale=1, 
				color='red', 
				rotation=(0,0,0), 
				needConstraint=True):

	RigToolsLogger.info(f"Creating Enhanced Control for: {name}")
	
	if not nameSpace:
		part = core.check_name_style(name)[0]
	elif nameSpace:
		base_name = core.check_name_style(name)[0]
		part = f"{nameSpace}_{base_name}"
		
	RigToolsLogger.info(f"Control Base Name: {part}")

	# ... 1. create Control and Zero Group
	controller_ctrl = core.Dag(part + '_ctrl')
	controller_ctrl.nmCreateController(ctrlShape)
	controller_ctrl.rotateShape(rotation)
	
	# ... use new function zroNewGrpWithOffset 
	controllerZro_grp, offset_grp = zroNewGrpWithOffset(controller_ctrl)
	offset_grp.rename(part + 'Offset_grp')
	
	# ... 2. Scale, Color, Gimbal
	controller_ctrl.editCtrlShape(axis=charScale * 0.9) 
	controllerGmbl_ctrl = core.createGimbal(controller_ctrl) # ... (จาก core.py)
	controller_ctrl.color = color
	
	# ... 3. Rotation Order
	controller_ctrl.rotateOrder = rotateOrder
	controllerGmbl_ctrl.rotateOrder = rotateOrder

	# ... 4. Positioning
	controllerZro_grp.matchPosition(name)
	controllerZro_grp.matchRotation(name)
	controller_ctrl.matchRotation(name)

	# ... 5. Constraint
	if needConstraint:
		controllerJnt_parCons = core.parentConstraint(controllerGmbl_ctrl, name)
		controllerJnt_parCons.name = part + 'Jnt_parCons'

		controllerJnt_sclCons = core.scaleConstraint(controllerGmbl_ctrl, name)
		controllerJnt_sclCons.name = part + 'Jnt_sclCons'

	# ... 6. Parent
	if parentTo:
		controllerZro_grp.parent(parentTo)

	RigToolsLogger.info(f"Parent constraint: {controllerGmbl_ctrl} >> {name}")
	
	# ... return OBJECTS
	return controllerZro_grp, controller_ctrl, controllerGmbl_ctrl



def findCharScale(topJnt = 'head02_tmpJnt'):
	logger.AutoRigLogger.info('Start of %s function' %findCharScale.__name__)
	''' get charScale from topJoint height '''

	topGrp = 'top_grp'
	mc.group(em=1, n=topGrp)
	mc.matchTransform(topGrp,topJnt)
	cmHeight = mc.getAttr(topGrp+'.ty')
	mc.delete(topGrp)
	height = (cmHeight/100) # Already convert to meter
	charScale = (	"{:.{}f}".format(height,2)	)

	logger.AutoRigLogger.info(  'Character Scale is >>>>>>>>> ' + charScale )
	# charScale = float(charScale)
	logger.AutoRigLogger.info('End of findCharScale function')
	print('\n\n\n\n\n')
	return float(charScale)