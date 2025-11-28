# -*- coding: utf-8 -*-
"""
Module: eh_neckRig
Description: Neck Rig generator (Single Joint) using standard eh_controller and matrix constraints.
"""

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

# --- Import Core ---
from function.rigging.autoRig.base import core
reload(core)

# --- Import Matrix Constraint (Original for Parent Constraint) ---
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

# --- Import Rig Tools ---
from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

# --- Import EH Controller ---
from function.rigging.controllerBox import eh_controller as eh_adjust
reload(eh_adjust)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

from function.pipeline import logger
reload(logger)

class NeckRigLogger(logger.MayaLogger):
	LOGGER_NAME = "NeckRig"

def createNeckRig(
		nameSpace='',
		parentTo='ctrl_grp',
		priorCtrl = '',
		priorJnt='spineTop_bJnt', # Should be the top spine joint or chest
		tmpJnt='neck_tmpJnt',    # Single joint input
		ctrl_shape = 'circle_ctrlShape',
		charScale=1.0,
		linkRotOrder=True
	):

	# --- 0. Validate Input ---
	if isinstance(tmpJnt, str):
		tmpJnt = [tmpJnt]
		
	first_tmp = tmpJnt[0]
	
	if not mc.objExists(first_tmp):
		NeckRigLogger.error(f"Template Joint '{first_tmp}' not found.")
		return None

	# --- 1. Header & Naming Setup ---
	name_info = core.check_name_style(first_tmp)
	clean_base_name = name_info[4] # e.g., 'neck'
	
	if nameSpace:
		partName = f"{nameSpace}{clean_base_name.capitalize()}"
	else:
		partName = clean_base_name

	core.makeHeader(f'Start of {partName} Rig')
	ctrl_color = mnd.COLOR_part_dict['primary']

	# --- 2. Create Main Group ---
	neckRig_grp = core.Null(f'{partName}Rig_grp')
	neckRig_grp.matchPosition(first_tmp)

	# [FIXED] ย้ายการ Parent มาไว้ตรงนี้ (ก่อนสร้าง Constraint)
	# เพื่อให้ Matrix Constraint รู้จัก Parent ที่แท้จริงและต่อ Inverse Matrix ได้ถูกต้อง

	neckRig_grp.parent(priorCtrl)



	# [UPDATE] Use Matrix Constraint for Prior Joint
	if mc.objExists(priorJnt):
		# Using matrix constraint instead of standard parentConstraint
		mtc.parentConMatrixGPT(
			source=priorJnt, 
			target=neckRig_grp.name, 
			mo=True, 
			translate=True, 
			rotate=True, 
			scale=True
		)
	else:
		NeckRigLogger.warning(f"Prior Joint '{priorJnt}' not found.")


	# --- 3. Joint & Controller Creation (Single Neck) ---
	
	controllers = []
	bind_joints = []

	for tmp in tmpJnt:
		# 3.1 Naming Logic
		current_name_info = core.check_name_style(tmp)
		base_name = current_name_info[4]
		
		if nameSpace:
			full_name = f"{nameSpace}{base_name}"
		else:
			full_name = base_name

		# 3.2 Create Bind Joint
		bJnt = rigTools.jointAt(tmp)
		bJnt.name = f'{full_name}_bJnt'
		
		bJnt.attr('side').value = 0
		bJnt.attr('type').value = 7 # Neck
		bJnt.attr('segmentScaleCompensate').value = 0
		
		bind_joints.append(bJnt)

		# Parent to Prior (Hierarchy)
		if mc.objExists(priorJnt):
			bJnt.parent(priorJnt)


		zro, ctrl, gmbl = eh_adjust.create(
			nameSpace=nameSpace,
			name=bJnt.name,
			ctrlShape=ctrl_shape,
			rotateOrder='xzy',
			charScale=charScale*6.5,
			color=ctrl_color,
			parentTo=neckRig_grp, # Parent Zro to Rig Group
			rotation=(0, 0, 0),
			matrixConstraint=True
		)
		


		controllers.append(ctrl)


	# --- 4. Local / World Setup (Matrix) ---
	# Apply to the Neck Controller
	
	if controllers:
		neck_ctrl = controllers[0]
		# Access Zro via parent of parent (Ctrl -> Offset -> Zro)
		neck_zro = neck_ctrl.getParent().getParent()
		
		mtc.eh_orientLocalWorldMatrix(
			ctrl=neck_ctrl.shape,	# Attr at shape node
			localObj=neckRig_grp,   # Moving with body/prior
			worldObj=parentTo,      # Static World (ctrl_grp)
			target=neck_zro,
			attrName='localWorld',
			bodyPart=f'{partName}'
		)

	#... add rotEnum after local/world
	if linkRotOrder:
		ctrl.addRotEnum()

	# --- 5. Final Organization ---
	# (ตัดส่วน Parenting ออกเพราะทำไปแล้วข้างบน)
	core.makeHeader('End of %s rig' %partName)
	NeckRigLogger.info(f'#### End of {partName} Rig ####')

	return neckRig_grp, bind_joints, controllers