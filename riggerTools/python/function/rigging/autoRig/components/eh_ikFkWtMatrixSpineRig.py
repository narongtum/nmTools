# -*- coding: utf-8 -*-
"""
Module: eh_ikFkWtMatrixSpineRig
Description: Spine Rig (4-Joint Method) using Weighted Matrix Constraint (Rivet).
			 Fix: Parenting Zro groups BEFORE creating Rivet to ensure correct offset calculation.
"""

from function.framework.reloadWrapper import reloadWrapper as reload
# from importlib import reload

import maya.cmds as mc

# --- Import Dependencies ---
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

from function.rigging.controllerBox import eh_controller as eh_adjust
reload(eh_adjust)

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

from function.rigging.constraint import rivetWithAddMatrix as rwm
reload(rwm)

from function.pipeline import logger
reload(logger)

class spineWtMatrixSpineLogger(logger.MayaLogger):
	LOGGER_NAME = "WtMatrixSpine"

def createSpineRig(
		nameSpace='',
		parentTo='ctrl_grp',
		priorJnt='hip_bJnt',
		priorCtrl='cog_gmbCtrl',
		charScale=1.0,
		placement_ctrl='Placement_ctrl', 
		tmpJnt=['lwrSpine_tmpJnt', 'spineBtw01_tmpJnt', 'spineBtw02_tmpJnt', 'uprSpine_tmpJnt']
	):

	# --- 1. Header & Setup ---
	partName = 'spine'
	if nameSpace:
		partName = f"{nameSpace}{partName.capitalize()}"
		
	core.makeHeader(f'Start of {partName} Rig (Matrix Version)')


	
	# --- 2. Create Groups ---
	spineRig_grp = core.Null(f'{partName}Rig_grp')
	jntStill_grp = core.Null(f'{partName}JntStill_grp')

	#... Change to parent under jnt grp
	mc.parent(jntStill_grp.name, 'jnt_grp')
	
	
	# --- 3. Create Joints & Controllers ---
	spine_jnt_list = []
	spine_ctrl_list = []
	bind_jnt_list = []
	
	# Constants
	rotateOrder = 'zxy'
	secondary_ctrl_shape = 'ring_ctrlShape'
	between_ctrl_shape = 'circle_ctrlShape'
	primary_ctrl_shape = 'cube_ctrlShape'

	for num, tmp in enumerate(tmpJnt):
		# Naming
		raw_name = core.check_name_style(tmp)[0]
		full_name = f'{nameSpace}{raw_name}' if nameSpace else raw_name
		
		temp_jnt_name = f'{nameSpace}{tmp}' if nameSpace else tmp
		if not mc.objExists(temp_jnt_name):
			 spineWtMatrixSpineLogger.error(f'Temp Joint "{temp_jnt_name}" not found.')
			 return None

		# Bind Joint
		bind_jnt = rigTools.jointAt(temp_jnt_name)
		bind_jnt.name = f'{full_name}_bJnt'
		bind_jnt.setLable('CEN', 'spine')
		bind_jnt_list.append(bind_jnt)

		# Rig Joint (Driver)
		rig_jnt = rigTools.jointAt(temp_jnt_name)
		rig_jnt.name = f'{full_name}_jnt'
		rig_jnt.attr('radius').value = 2.0
		spine_jnt_list.append(rig_jnt)

		# Determine Shape
		if num == 0: ctrlShape = secondary_ctrl_shape
		elif num == 3: ctrlShape = primary_ctrl_shape
		else: ctrlShape = between_ctrl_shape 

		# Create Controller
		# [IMPORTANT] We disable matrixConstraint here for Mid ctrls because we will use Rivet later
		# Only Start/End might need direct constraint (but usually we constrain later manually)
		zro, ctrl, gmbl = eh_adjust.create(
			nameSpace=None,
			name=rig_jnt.name,
			ctrlShape=ctrlShape,
			charScale=charScale * 15,
			color='yellow',
			parentTo=None, 
			rotateOrder=rotateOrder,
			rotation=(0,0,0),
			matrixConstraint=False # We will constrain manually
		)
		ctrl.addRotEnum()
		spine_ctrl_list.append([zro, ctrl, gmbl])


	# --- 4. Finalize Structure & Parenting (CRITICAL STEP) ---
	
	# 4.1 Position Main Group to Match Base
	spineRig_grp.matchPosition(bind_jnt_list[0])
	spineRig_grp.matchRotation(bind_jnt_list[0])
	
	# 4.2 Parent Main Group to Hierarchy
	if parentTo and mc.objExists(parentTo):
		spineRig_grp.parent(parentTo)
	
	# 4.3 Parent Controllers to Main Group *BEFORE* Rivet
	# This ensures their 'parentInverseMatrix' is correct when calculating Rivet Offset
	ctrl_lower_zro = spine_ctrl_list[0][0]
	ctrl_mid_bot_zro = spine_ctrl_list[1][0]
	ctrl_mid_top_zro = spine_ctrl_list[2][0]
	ctrl_upper_zro = spine_ctrl_list[3][0]
	
	ctrl_lower_zro.parent(spineRig_grp)
	ctrl_mid_bot_zro.parent(spineRig_grp)
	ctrl_mid_top_zro.parent(spineRig_grp)
	ctrl_upper_zro.parent(spineRig_grp)
	
	# 4.4 Parent Joints to Still Group
	for jnt in spine_jnt_list:
		jnt.parent(jntStill_grp)


	# --- 5. Connect Controls to Drivers ---
	
	# 5.1 Direct Constraint for Top/Bot Controllers
	# Lower Ctrl drives Lower Rig Joint
	mtc.parentConMatrixGPT(spine_ctrl_list[0][2].name, spine_jnt_list[0].name, mo=True)
	# Upper Ctrl drives Upper Rig Joint
	mtc.parentConMatrixGPT(spine_ctrl_list[3][2].name, spine_jnt_list[3].name, mo=True)
	
	# 5.2 Matrix Rivet for Mid Controllers
	# Drivers are Rig Joints (which are driven by Top/Bot Ctrls)
	bot_driver = spine_jnt_list[0].name 
	top_driver = spine_jnt_list[3].name 
	
	# Prepare Data
	rivet_data = [
		{
			'target': ctrl_mid_bot_zro.name,
			'weight': [(bot_driver, 0.666), (top_driver, 0.334)]
		},
		{
			'target': ctrl_mid_top_zro.name,
			'weight': [(bot_driver, 0.334), (top_driver, 0.666)]
		}
	]
	
	spineWtMatrixSpineLogger.info("Creating Matrix Rivets...")
	rwm.rivetMatrixWeight(data_list=rivet_data)
	
	# 5.3 Mid Ctrls drive Mid Rig Joints
	mtc.parentConMatrixGPT(spine_ctrl_list[1][2].name, spine_jnt_list[1].name, mo=True)
	mtc.parentConMatrixGPT(spine_ctrl_list[2][2].name, spine_jnt_list[2].name, mo=True)


	# --- 6. Hierarchy Setup (Bind Joints) ---
	for num, each in enumerate(bind_jnt_list):
		if num != 0:
			each.parent(bind_jnt_list[num-1])
		else:
			if priorJnt and mc.objExists(priorJnt):
				each.parent(priorJnt)


	# --- 7. Squash & Stretch Logic ---
	# ... [Squash Stretch Logic same as before] ...
	
	base_name = core.check_name_style(tmpJnt[1])[0]
	base_name_space = f'{nameSpace}{base_name}' if nameSpace else base_name
	distance = core.DistanceBetween(name=f'{base_name_space}_btw')
	
	inb01_ctrl = spine_ctrl_list[0][1] # Bot Ctrl
	inb02_ctrl = spine_ctrl_list[3][1] # Top Ctrl
	
	inb01_decom = core.DecomposeMatrix(f'{base_name_space}01WorldPosi')
	inb02_decom = core.DecomposeMatrix(f'{base_name_space}02WorldPosi')
	
	inb01_ctrl.attr('worldMatrix[0]') >> inb01_decom.attr('inputMatrix')
	inb02_ctrl.attr('worldMatrix[0]') >> inb02_decom.attr('inputMatrix')
	
	inb01_decom.attr('outputTranslate') >> distance.attr('point1')
	inb02_decom.attr('outputTranslate') >> distance.attr('point2')
	
	original_length = mc.getAttr(distance.name + '.distance')
	
	# Global Scale
	if mc.objExists(placement_ctrl):
		place_ctrl = core.Dag(placement_ctrl)
		global_scale_mdv = core.MultiplyDivine(f'{base_name_space}GlobalScale_mdv', operation=2)
		distance.attr('distance') >> global_scale_mdv.attr('input1X')
		
		global_store_pma = core.PlusMinusAverage(f'{base_name_space}StoreGlobalScale_pma')
		place_ctrl.attr('scaleX') >> global_store_pma.attr('input1D[0]')
		place_ctrl.attr('scaleY') >> global_store_pma.attr('input1D[1]')
		place_ctrl.attr('scaleZ') >> global_store_pma.attr('input1D[2]')
		
		avg_mdv = core.MultiplyDivine(f'{base_name_space}AvgGlobalScale_mdv', operation=2)
		avg_mdv.attr('input2X').value = 3
		global_store_pma.attr('output1D') >> avg_mdv.attr('input1X')
		avg_mdv.attr('outputX') >> global_scale_mdv.attr('input2X')
		
		stretch_src_attr = global_scale_mdv.attr('outputX')
	else:
		stretch_src_attr = distance.attr('distance')

	# Stretch Calculation
	baseValue_mdv = core.MultiplyDivine(f'{base_name_space}BaseValue', operation=2)
	stretch_src_attr >> baseValue_mdv.attr('input1X')
	baseValue_mdv.attr('input2X').value = original_length
	
	sqrt_mdv = core.MultiplyDivine(f'{base_name_space}SquareRootValue', operation=3)
	baseValue_mdv.attr('outputX') >> sqrt_mdv.attr('input1X')
	sqrt_mdv.attr('input2X').value = 0.5
	
	vol_mdv = core.MultiplyDivine(f'{base_name_space}oneDiv', operation=2)
	vol_mdv.attr('input1X').value = 1
	sqrt_mdv.attr('outputX') >> vol_mdv.attr('input2X')
	
	clamp_val = core.Clamp(f'{base_name_space}ClampValue')
	clamp_val.attr('minR').value = 0.001
	clamp_val.attr('maxR').value = 100.0
	vol_mdv.attr('outputX') >> clamp_val.attr('inputR')
	
	# Connect to Mid Joints
	inb01_jnt = spine_jnt_list[1]
	inb02_jnt = spine_jnt_list[2]
	
	clamp_val.attr('outputR') >> inb01_jnt.attr('scaleX')
	clamp_val.attr('outputR') >> inb02_jnt.attr('scaleX')
	clamp_val.attr('outputR') >> inb01_jnt.attr('scaleZ')
	clamp_val.attr('outputR') >> inb02_jnt.attr('scaleZ')


	# --- 8. Connect Bind Joints to Rig Joints ---
	for num, each_bind in enumerate(bind_jnt_list):
		mtc.parentConMatrixGPT(
			spine_jnt_list[num].name, 
			each_bind.name, 
			mo=True, translate=True, rotate=True, scale=True
		)

	# Follow Logic
	#... make hip move free from spine
	# mtc.parentConMatrixGPT(priorCtrl, spineRig_grp.name, mo=True)

	#... Use parent hierarchy instead
	spineRig_grp.parent(priorCtrl)


	spineWtMatrixSpineLogger.info(f'#### End of {partName} Rig (Matrix) ####')
	
	return spineRig_grp, bind_jnt_list, spine_ctrl_list