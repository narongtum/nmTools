# -*- coding: utf-8 -*-
"""
Module: eh_headRig
Description: Head Rig generator with Matrix-based approach (Aim, Space Switch).
			 Includes Head, Jaw, and Eye setup.
			 [UPDATE] Enhanced debugging for Face Ctrl issues.
"""

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

# --- Import Core ---
from function.rigging.autoRig.base import core
reload(core)

# --- Import Matrix Constraint ---
from function.rigging.constraint import eh_orientLocalWorldMatrix as olm
reload(olm)

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

# --- Import Rig Tools ---
from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

# --- Import EH Controller ---
from function.rigging.controllerBox import eh_controller as eh_adjust
reload(eh_adjust)

from function.pipeline import logger
reload(logger)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

class HeadRigLogger(logger.MayaLogger):
	LOGGER_NAME = "HeadRig"

color_part_dict = mnd.COLOR_part_dict


def _createEyeSetup(nameSpace, side, eyeJnt, headJnt, charScale, parentTo, eyeCenCtrl, eyeTarget):
	"""
	Internal helper to create Eye Rig (Joint, Ctrl, Aim).
	"""
	partName = f"{nameSpace}eye{side}" if nameSpace else f"eye{side}"
	
	# 1. Create Bind Joint
	eyeSide_bJnt = rigTools.jointAt(eyeJnt)
	eyeSide_bJnt.name = f"{partName}_bJnt"
	eyeSide_bJnt.parent(headJnt)
	eyeSide_bJnt.freeze()

	# 2. Create Controller (Eye Ball)
	eye_zro, eye_ctrl, eye_gmbl = eh_adjust.create(
		nameSpace=None,
		name=eyeSide_bJnt.name,
		ctrlShape='sphere_ctrlShape',
		rotateOrder='zxy',
		charScale=charScale * 1.01,
		color='softBlue',
		parentTo=None,
		rotation=(0,0,0),
		matrixConstraint=False
	)
	
	# Create Aim Group
	offset_grp = eye_ctrl.getParent()
	eyeAim_grp = core.Null(f"{partName}Aim_grp")
	eyeAim_grp.snap(offset_grp)
	
	offset_grp.parent(eyeAim_grp)
	eyeAim_grp.parent(eye_zro)
	
	# 3. Create Eye Target Controller
	targetPart = f"{nameSpace}eyeTarget{side}" if nameSpace else f"eyeTarget{side}"
	
	target_zro, target_ctrl, target_gmbl = eh_adjust.create(
		nameSpace=None,
		name=targetPart,
		ctrlShape='legRGT_pov_ctrlShape',
		rotateOrder='zxy',
		charScale=charScale * 0.8,
		color='softBlue',
		parentTo=eyeCenCtrl,
		rotation=(0,0,0),
		matrixConstraint=False
	)
	
	target_zro.maSnap(eyeTarget)
	
	# 4. Matrix Aim Constraint
	mtc.aimConstraintMatrix(
		source=target_ctrl.name, 
		target=eyeAim_grp.name, 
		aimVector=(0, 0, 1), 
		upVector=(0, 1, 0), 
		worldUpObject=headJnt,
		maintainOffset=False
	)
	
	# 5. Finalize Eye Ball
	mtc.parentConMatrixGPT(
		source=eye_gmbl.name,
		target=eyeSide_bJnt.name,
		mo=True,
		translate=True, rotate=True, scale=True
	)
	
	eye_zro.parent(parentTo)
	
	for attr in ('rx','ry','rz','sx','sy','sz','v'):
		target_ctrl.attr(attr).lockHide()
		
	return eyeSide_bJnt


def createHeadRig(
		nameSpace='',
		parentTo='ctrl_grp',
		tmpJnt=(
			'head01_tmpJnt', 'eyeLFT_tmpJnt', 'eyeRGT_tmpJnt',          # 0-2
			'jaw01Lwr_tmpJnt', 'jaw02Lwr_tmpJnt', 'jaw03Lwr_tmpJnt',    # 3-5
			'jaw01Upr_tmpJnt', 'jaw02Upr_tmpJnt',                       # 6-7
			'eye_tmpJnt', 'eyeTargetLFT_tmpJnt', 'eyeTargetRGT_tmpJnt'  # 8-10
		),
		faceCtrl=False,
		priorJnt='', # Neck Joint
		charScale=1.0,
		ctrlShape='cubeExpand_ctrlShape',
		linkRotOrder=False
	):

	# --- 1. Header & Setup ---
	# Validating input length
	if len(tmpJnt) < 11 and faceCtrl:
		HeadRigLogger.error(f"TmpJnt list is too short ({len(tmpJnt)}). Face setup requires 11 elements.")
		return None

	head1_tmp = tmpJnt[0]
	if not mc.objExists(head1_tmp):
		HeadRigLogger.error(f"Head Temp Joint {head1_tmp} not found.")
		return None

	name_info = core.check_name_style(head1_tmp)
	base_name = name_info[4]
	
	if nameSpace:
		partName = f"{nameSpace}{base_name.capitalize()}"
		prefix = f"{nameSpace}"
	else:
		partName = base_name
		prefix = ""

	core.makeHeader(f'Start of {partName} Rig')
	
	# --- 2. Create Main Groups ---
	headRig_grp = core.Null(f'{prefix}headRig_grp')
	headRig_grp.matchPosition(head1_tmp)
	headRig_grp.matchRotation(head1_tmp)

	head01_bJnt = rigTools.jointAt(head1_tmp)
	head01_bJnt.name = f"{prefix}head01_bJnt"
	head01_bJnt.attr('segmentScaleCompensate').value = 0
	head01_bJnt.setLable('CEN','head')
	
	if mc.objExists(priorJnt):
		head01_bJnt.parent(priorJnt)

	# --- 3. Head Controller ---
	head_zro, head_ctrl, head_gmbl = eh_adjust.create(
		nameSpace=nameSpace,
		name=head01_bJnt.name,
		ctrlShape=ctrlShape,
		rotateOrder='xzy',
		charScale=charScale * 7.0,
		color='yellow',
		parentTo=headRig_grp,
		rotation=(0,0,0),
		matrixConstraint=True
	)
	
	head_ctrl.moveShape(move=(0, charScale * 4.2, 0))
	head_gmbl.moveShape(move=(0, charScale * 4.2, 0))
	
	if linkRotOrder:
		head_ctrl.addRotEnum()

	# --- 4. Local / World Setup ---
	olm.orientLocalWorldMatrix(
		ctrl=head_ctrl,
		localObj=headRig_grp,
		worldObj=parentTo,
		target=head_zro,
		attrName='localWorld',
		bodyPart=f'{prefix}head'
	)

	# --- 5. Face Setup (Jaw & Eyes) ---
	if faceCtrl:
		HeadRigLogger.info("Starting Face Setup...")
		
		# --- JAW ---
		jawLwr_tmp = tmpJnt[3]
		jawUpr_tmp = tmpJnt[6]
		
		if mc.objExists(jawLwr_tmp):
			# Create Jaw Joints
			jaw1Lwr_bJnt = rigTools.jointAt(jawLwr_tmp)
			jaw1Lwr_bJnt.name = f"{prefix}jaw01Lwr_bJnt"
			jaw1Lwr_bJnt.parent(head01_bJnt)
			
			# Upper Jaw
			jawUpr_zro, jawUpr_ctrl, jawUpr_gmbl = eh_adjust.create(
				nameSpace=nameSpace,
				name=f"{prefix}jaw01Upr",
				ctrlShape='squareExpand_ctrlShape',
				rotateOrder='xzy',
				charScale=charScale * 3.5,
				color='yellow',
				parentTo=head_gmbl,
				rotation=(0,0,0),
				matrixConstraint=False
			)
			if mc.objExists(jawUpr_tmp):
				jawUpr_zro.snap(jawUpr_tmp)
			
			# Lower Jaw
			jawLwr_zro, jawLwr_ctrl, jawLwr_gmbl = eh_adjust.create(
				nameSpace=nameSpace,
				name=jaw1Lwr_bJnt.name,
				ctrlShape='squareExpand_ctrlShape',
				rotateOrder='xzy',
				charScale=charScale * 2.8,
				color='yellow',
				parentTo=head_gmbl,
				rotation=(0,0,0),
				matrixConstraint=True
			)
			jawLwr_ctrl.moveShape(move=(0, charScale * -1.8, charScale * 2.8))
			HeadRigLogger.info("Jaw Setup Complete.")
		else:
			HeadRigLogger.error(f"Jaw Joint {jawLwr_tmp} not found!")

		# --- EYES ---
		eyeCen_tmp = tmpJnt[8]
		eyeTargetL_tmp = tmpJnt[9]
		eyeTargetR_tmp = tmpJnt[10]
		eyeL_tmp = tmpJnt[1]
		eyeR_tmp = tmpJnt[2]
		
		if mc.objExists(eyeCen_tmp):
			# Eye Center
			eyeCen_zro, eyeCen_ctrl, eyeCen_gmbl = eh_adjust.create(
				nameSpace=nameSpace,
				name=f"{prefix}eyeCenter",
				ctrlShape='capsule_ctrlShape',
				rotateOrder='xzy',
				charScale=charScale * 0.8,
				color='yellow',
				parentTo=head_gmbl,
				rotation=(0,0,0),
				matrixConstraint=False
			)
			eyeCen_zro.snap(eyeCen_tmp)
			
			# Eye Center Local/World
			olm.orientLocalWorldMatrix(
				ctrl=eyeCen_ctrl,
				localObj=head_gmbl,
				worldObj=parentTo,
				target=eyeCen_zro,
				attrName='localWorld',
				bodyPart=f'{prefix}eyeCenter'
			)
			
			# Create Left Eye
			_createEyeSetup(nameSpace, 'LFT', eyeL_tmp, head01_bJnt.name, charScale, 
							parentTo=head_gmbl.name, 
							eyeCenCtrl=eyeCen_ctrl.name, 
							eyeTarget=eyeTargetL_tmp)
			
			# Create Right Eye
			_createEyeSetup(nameSpace, 'RGT', eyeR_tmp, head01_bJnt.name, charScale, 
							parentTo=head_gmbl.name, 
							eyeCenCtrl=eyeCen_ctrl.name, 
							eyeTarget=eyeTargetR_tmp)
			
			HeadRigLogger.info("Eye Setup Complete.")
		else:
			HeadRigLogger.error(f"Eye Center {eyeCen_tmp} not found!")


	# --- 6. Final Organization ---
	if mc.objExists(parentTo):
		headRig_grp.parent(parentTo)
	
	if mc.objExists(priorJnt):
		mtc.parentConMatrixGPT(
			source=priorJnt,
			target=headRig_grp.name,
			mo=True,
			translate=True, rotate=True, scale=True
		)

	HeadRigLogger.info(f'#### End of {partName} Rig ####')
	return head01_bJnt.name