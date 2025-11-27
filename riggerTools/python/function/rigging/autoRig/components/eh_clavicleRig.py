# -*- coding: utf-8 -*-
"""
Module: eh_clavicleRig
Description: Clavicle Rig generator using standard eh_controller and matrix constraints.
			 Supports both 'Side Follow' (clavLFT) and 'Capital Lead' (L_clav) naming conventions.
			 Updated naming logic for Capital Lead with Namespace: {side}_{nameSpace}{baseName}
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

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

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

	# --- 1. Analyze Naming Convention ---
	# check_name_style returns: (base_name, side, reverse_side, isDefault(True=Suffix), nameNoSide, ...)
	name_info = core.check_name_style(tmpJnt)
	is_side_follow_style = name_info[3]  # True if 'clavLFT' (Default), False if 'L_clav'
	clean_base_name = name_info[4]       # 'clav'

	# Determine Format based on style
	if is_side_follow_style:
		# --- Pattern: Side Follow (e.g., clavLFT) ---
		# Standard logic: Namespace + Base + Side
		
		# Ensure side matches naming (clavLFT uses 'LFT')
		base_final_name = f"{clean_base_name}{side}"
		ctrl_shape = f"shoulder{side}_FK_ctrlShape"
		
		# Maya Label ID (1=L, 2=R)
		label_side = 1 if 'LFT' in side or ('L' in side and 'R' not in side) else 2
		
		# Apply Namespace (Standard prefix)
		if nameSpace:
			full_name = f"{nameSpace}{base_final_name}"
		else:
			full_name = base_final_name
		
	else:
		# --- Pattern: Capital Lead (e.g., L_clav) ---
		
		# Convert 'LFT' to 'L' for prefix style if needed
		if side == 'LFT': prefix_side = 'L'
		elif side == 'RGT': prefix_side = 'R'
		else: prefix_side = side 
			
		ctrl_shape = f"{prefix_side}_shoulder_FK_ctrlShape"
		
		# Maya Label ID
		label_side = 1 if prefix_side == 'L' else 2
		
		# Apply Namespace (Custom logic requested: {side}_{nameSpace}{baseName})
		if nameSpace:
			# Example: L_Ns_clav (Assuming nameSpace includes separator like 'Ns_')
			full_name = f"{prefix_side}_{nameSpace}{clean_base_name}"
		else:
			# Standard: L_clav
			full_name = f"{prefix_side}_{clean_base_name}"

	# Common Settings
	# Color logic: Always use 'red'/'blue' for Core to understand
	if side == 'LFT' or side == 'L':
		ctrl_color = 'red'
	else:
		ctrl_color = 'blue'

	core.makeHeader(f'Start of {full_name} Rig')
	ClavicleRigLogger.info(f"Naming Style: {'Side Follow' if is_side_follow_style else 'Capital Lead'}")
	ClavicleRigLogger.info(f"Full Name generated: {full_name}")





	# --- 2. Create Main Group ---
	clavRig_grp = core.Null(f'{full_name}_grp')
	# priorJnt_obj = core.Dag(priorJnt)
	# clavRig_grp.snap(priorJnt_obj)


	# --- 6. Final Organization ---
	#... Parent Main Group
	if mc.objExists(parentTo):
		clavRig_grp.parent(parentTo)

	print('ERROR PAW')
	# Parent/Constrain Rig Group to Prior Joint
	if mc.objExists(priorJnt):
		# clavRigGrp_cons = core.parentConstraint(priorJnt, clavRig_grp)
		# clavRigGrp_cons.name = f'{full_name}Grp_parCons'

		mtc.parentConMatrixGPT(
			source=priorJnt, 
			target=clavRig_grp.name, 
			mo=False, #... Do not maintain offset 
			translate=True, 
			rotate=True, 
			scale=True)

	else:
		ClavicleRigLogger.warning(f"Prior Joint '{priorJnt}' not found. Clavicle group will not follow spine.")


	# --- 3. Joint Creation ---
	if not mc.objExists(tmpJnt):
		ClavicleRigLogger.error(f"Template Joint '{tmpJnt}' not found.")
		return None

	# Create Bind Joint (Using rigTools for jointAt logic)
	clav_bJnt = rigTools.jointAt(tmpJnt)
	clav_bJnt.name = f'{full_name}_bJnt'
	
	# Set Label
	clav_bJnt.attr('side').value = label_side
	clav_bJnt.attr('type').value = 18 # Collar
	
	# Parent Bind Joint
	if mc.objExists(priorJnt):
		clav_bJnt.parent(priorJnt)
		
	# Disable Segment Scale Compensate
	clav_bJnt.attr('segmentScaleCompensate').value = 0


	# --- 4. Controller Creation (Using eh_controller) ---
	
	# [UPDATE] Using eh_adjust.create
	# Note: nameSpace argument in create() is used to construct name. 
	# Since we already built the 'full_name' manually above, we pass None to nameSpace 
	# and pass the full base name to 'name' to avoid double-prefixing inside create().
	
	clav_zro, clav_ctrl, clav_gmbl = eh_adjust.create(
		nameSpace=None,          # We handled namespace in full_name already
		name=clav_bJnt.name,     # Use the joint name which is already {full_name}_bJnt
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
	# Naming for Space Switch (Uses the full_name)
	space_name = full_name
	
	print('[UPDATE] Using olm.orientLocalWorldMatrix')
	mtc.eh_orientLocalWorldMatrix(
		ctrl=clav_ctrl,
		localObj=clavRig_grp,   # Moves with Spine/Prior
		worldObj=parentTo,      # Static World (ctrl_grp)
		target=clav_zro,        # Drive the Zro Group
		attrName='localWorld',
		bodyPart=space_name
	)
	
	

		
	
	ClavicleRigLogger.info(f'#### End of {full_name} Rig ####')
	
	# Return Objects
	return clavRig_grp, clav_bJnt, clav_ctrl