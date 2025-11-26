# -*- coding: utf-8 -*-
"""
Module: eh_clavicleRig
Description: Clavicle Rig generator using standard eh_controller and matrix constraints.
"""

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

# --- Import Core ---
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.constraint import eh_orientLocalWorldMatrix as olm
reload(olm)


# --- Import Rig Tools (Still needed for jointAt) ---
from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

# --- Import EH Controller (NEW Standard) ---
from function.rigging.controllerBox import eh_controller as eh_adjust
reload(eh_adjust)

from function.pipeline import logger
reload(logger)

class ClavicleRigLogger(logger.MayaLogger):
	LOGGER_NAME = "ClavicleRig"

def createClavicleRig(
		nameSpace='',
		side='LFT',
		parentTo='ctrl_grp',
		priorJnt='spineTop_bJnt', # Should be the top spine joint
		tmpJnt='clavLFT_tmpJnt',
		charScale=1.0
	):

	# --- 1. Header & Naming Setup ---
	# Extract base name
	raw_name = core.check_name_style(tmpJnt)[0] # Get 'clavLFT'
	base_name = raw_name.replace(side, '') # Get 'clav'
	
	partName = base_name
	if nameSpace:
		partName = f"{nameSpace}{partName.capitalize()}"
	
	core.makeHeader(f'Start of {partName}{side} Rig')
	
	# Determine Color
	ctrl_color = 'red' if side == 'LFT' else 'blue'
	
	
	# --- 2. Create Main Group ---
	clavRig_grp = core.Null(f'{partName}Rig{side}_grp')
	
	# Parent/Constrain Rig Group to Prior Joint
	if mc.objExists(priorJnt):
		clavRigGrp_cons = core.parentConstraint(priorJnt, clavRig_grp)
		clavRigGrp_cons.name = f'{partName}Rig{side}Grp_parCons'
	else:
		ClavicleRigLogger.warning(f"Prior Joint '{priorJnt}' not found. Clavicle group will not follow spine.")


	# --- 3. Joint Creation ---
	if not mc.objExists(tmpJnt):
		ClavicleRigLogger.error(f"Template Joint '{tmpJnt}' not found.")
		return None

	# Create Bind Joint (Using rigTools for jointAt logic)
	clav_bJnt = rigTools.jointAt(tmpJnt)
	clav_bJnt.name = f'{partName}{side}_bJnt'
	
	# Set Label
	label_side = 1 if side == 'LFT' else 2
	clav_bJnt.attr('side').value = label_side
	clav_bJnt.attr('type').value = 18 # Collar
	
	# Parent Bind Joint
	if mc.objExists(priorJnt):
		clav_bJnt.parent(priorJnt)
		
	# Disable Segment Scale Compensate
	clav_bJnt.attr('segmentScaleCompensate').value = 0


	# --- 4. Controller Creation (Using eh_controller) ---
	ctrl_shape = f'shoulder{side}_FK_ctrlShape'
	
	# [UPDATE] Using eh_adjust.create
	clav_zro, clav_ctrl, clav_gmbl = eh_adjust.create(
		nameSpace=nameSpace,
		name=clav_bJnt.name,
		ctrlShape=ctrl_shape,
		rotateOrder='xyz',
		charScale=charScale,
		color=ctrl_color,
		parentTo=clavRig_grp,
		rotation=(0, 0, 90), # Rotate shape 90 degrees
		matrixConstraint=True # Enable Matrix Constraint
	)
	
	# Pattern: Add Rot Enum
	clav_ctrl.addRotEnum()
	
	
	# --- 5. Local / World Setup (Using Matrix Switch) ---
	# Naming for Space Switch
	space_name = f'{partName}{side}'
	
	# [UPDATE] Using olm.orientLocalWorldMatrix (Cleaner graph)
	olm.orientLocalWorldMatrix(
		ctrl=clav_ctrl,
		localObj=clavRig_grp,   # Moves with Spine/Prior
		worldObj=parentTo,      # Static World (ctrl_grp)
		target=clav_zro,        # Drive the Zro Group
		attrName='localWorld',
		bodyPart=space_name
	)
	
	
	# --- 6. Final Organization ---
	
	# Parent Main Group
	if mc.objExists(parentTo):
		clavRig_grp.parent(parentTo)
		
	
	ClavicleRigLogger.info(f'#### End of {partName}{side} Rig ####')
	
	# Return Objects
	return clavRig_grp, clav_bJnt, clav_ctrl