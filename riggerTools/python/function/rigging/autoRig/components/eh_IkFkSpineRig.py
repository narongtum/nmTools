# -*- coding: utf-8 -*-
"""
Module: eh_ikfkSpineRig
Description: Spine Rig generator using 4-joint method with Squash & Stretch, 
			 Volume Preservation, and Proxy Mesh Skinning.
"""

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

# --- Import Dependencies (Using Original Core/RigTools as requested) ---
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

from function.rigging.constraint import pin_locator_polygon as plp
reload(plp)

from function.pipeline import logger
reload(logger)

class IkFkSpineLogger(logger.MayaLogger):
	LOGGER_NAME = "IkFkSpineLogger"

def createIkFkSpineRig(
		nameSpace='',
		parentTo='ctrl_grp',
		priorJnt='hip_bJnt',
		priorCtrl='cog_gmbCtrl',
		hipCtrl = 'hip_gmbCtrl',
		charScale=1.0,
		# Specific Arguments for this method
		polyplane_L02='spine01_L02_ply',
		placement_ctrl='Placement_ctrl', # Needed for Global Scale Logic
		tmpJnt=['lwrSpine_tmpJnt', 'spineBtw01_tmpJnt', 'spineBtw02_tmpJnt', 'uprSpine_tmpJnt'],
		vtx_ids=['11', '10', '9', '8'], # Order: Bottom to Top
		# Constants
		rotateOrder = 'zxy',
		primary_ctrl_shape = 'cube_ctrlShape',
		secondary_ctrl_shape = 'ring_ctrlShape',
		between_ctrl_shape = 'circle_ctrlShape'
	):

	# --- 1. Header & Naming Setup ---
	partName = 'spine'
	if nameSpace:
		partName = f"{nameSpace}{partName.capitalize()}"
		
	core.makeHeader(f'Start of {partName} Rig')

	# --- Validation ---
	# Construct full mesh name with namespace if needed
	full_polyplane = f'{nameSpace}{polyplane_L02}' if nameSpace else polyplane_L02
	
	if not mc.objExists(full_polyplane):
		IkFkSpineLogger.error(f'Proxy poly plane "{full_polyplane}" not found. Cannot proceed.')
		return None

	if not mc.objExists(placement_ctrl):
		# Fallback search with namespace
		if nameSpace and mc.objExists(f'{nameSpace}{placement_ctrl}'):
			placement_ctrl = f'{nameSpace}{placement_ctrl}'
		else:
			IkFkSpineLogger.warning(f'Placement Ctrl "{placement_ctrl}" not found. Global Scale feature might fail.')


	# --- 2. Create Main Group ---
	spineRig_grp = core.Null(f'{partName}Rig_grp')

	# Internal lists
	spine_jnt_list = []
	spine_ctrl_list = []
	bind_jnt_list = []
	

	
	
	# --- 3. Joints & Controllers Creation ---
	
	# Loop create joints/ctrls based on vertex/temp joint input
	for num, vtx_idx in enumerate(vtx_ids):
		
		# 3.1 Naming
		raw_name = core.check_name_style(tmpJnt[num])[0]
		# Handle namespace for new objects
		full_name = f'{nameSpace}{raw_name}' if nameSpace else raw_name
		
		# 3.2 Create Joints (Using Snap to Temp Joint instead of Vertex Pos for safer rotation)
		temp_jnt_name = f'{nameSpace}{tmpJnt[num]}' if nameSpace else tmpJnt[num]
		
		if not mc.objExists(temp_jnt_name):
			 IkFkSpineLogger.error(f'Temp Joint "{temp_jnt_name}" not found.')
			 return None

		temp_jnt_obj = core.Dag(temp_jnt_name)

		# Create Bind Joint
		bind_jnt = core.Joint(name=f'{full_name}_bJnt')
		bind_jnt.snap(temp_jnt_obj)
		bind_jnt.setRotationOrder(rotateOrder)
		bind_jnt.setLable('CEN', 'spine')
		bind_jnt_list.append(bind_jnt)

		# Create Rig Joint
		rig_jnt = core.Joint(name=f'{full_name}_jnt')
		rig_jnt.snap(temp_jnt_obj)
		rig_jnt.attr('radius').value = 2.0
		rig_jnt.setRotationOrder(rotateOrder)
		spine_jnt_list.append(rig_jnt)

		# 3.3 Determine Control Shape
		if num == 0:
			ctrlShape = secondary_ctrl_shape
		elif num == 1 or num == 2:
			ctrlShape = between_ctrl_shape
		elif num == 3:
			ctrlShape = primary_ctrl_shape

		# 3.4 Create Controller
		# Using adjust.creControllerFunc as requested (returns list of strings: [zro, ctrl, gmbl])
		ctrl_objs = adjust.creControllerFunc(
			selected=[rig_jnt.name], 
			scale=charScale * 15, 
			ctrlShape=ctrlShape, 
			color='yellow', 
			constraint=True, 
			matrixConst=True, 
			mo=False, 
			translate=True, 
			rotate=True, 
			scaleConstraint=False, 
			rotateOrder=rotateOrder, 
			parentUnder=False
		)
		
		# Add Rotation Order Enum (Pattern Requirement)
		ctrl_node = core.Dag(ctrl_objs[1])
		ctrl_node.addRotEnum()

		spine_ctrl_list.append(ctrl_objs)


	# --- 4. Hierarchy Setup ---
	
	# 4.1 Parent Bind Joints
	for num, each in enumerate(bind_jnt_list):
		if num != 0:
			each.parent(bind_jnt_list[num-1])
		else:
			if priorJnt and mc.objExists(priorJnt):
				each.parent(priorJnt)

	
	# --- 5. Skinning Proxy Mesh ---
	
	# Define Joints to bind (Head and Tail)
	joints_to_bind = [spine_jnt_list[0], spine_jnt_list[3]]
	
	# Validation
	vtx_set_01 = [4, 5, 10]
	vtx_set_02 = [6, 7, 9]
	all_required_vtx = vtx_set_01 + vtx_set_02
	
	for vtx_id in all_required_vtx:
		vtx_check = '{}.vtx[{}]'.format(full_polyplane, vtx_id)
		if not mc.objExists(vtx_check):
			 IkFkSpineLogger.error(f'Mesh Topology Mismatch: Vertex "{vtx_check}" not found.')

	# Create SkinCluster
	try:
		skin_cluster_obj = core.SkinCluster(
			joints_to_bind, 
			full_polyplane, 
			toSelectedBones=True, 
			bindMethod=0,         
			skinMethod=0,          
			normalizeWeights=1, 
			maximumInfluences=2, 
			name='{}_skinCluster'.format(full_polyplane)
		)
	except Exception as e:
		IkFkSpineLogger.error(f'Failed to create SkinCluster: {e}')

	# Assign Hard-coded Weights
	weights_01 = [(spine_jnt_list[0].name, 0.666), (spine_jnt_list[3].name, 0.334)]
	for vtx_id in vtx_set_01:
		vtx_full_path = '{}.vtx[{}]'.format(full_polyplane, vtx_id)
		skin_cluster_obj.setWeight(item=vtx_full_path, transformValue=weights_01)

	weights_02 = [(spine_jnt_list[0].name, 0.334), (spine_jnt_list[3].name, 0.666)]
	for vtx_id in vtx_set_02:
		vtx_full_path = '{}.vtx[{}]'.format(full_polyplane, vtx_id)
		skin_cluster_obj.setWeight(item=vtx_full_path, transformValue=weights_02)

	IkFkSpineLogger.info('Skin weights assigned.')


	# --- 6. Pin In-between Controllers ---
	
	inbetween_locs = plp.pin_locator_polygon(
		poly_mesh=full_polyplane,
		vtx_list=[10, 9], # Hardcoded based on provided logic
		locator_scale=1.0,
		side='',   
		normalAxis='Z',
		tangentAxis='Y'
	)

	# Parent Controllers to Locators
	# spine_ctrl_list structure: [ [zro, ctrl, gmbl], ... ]
	# Index 1 is In-between 01, Index 2 is In-between 02
	# Inbetween locs: [loc_vtx10, loc_vtx9]
	
	# Note: Source script logic: 
	# mc.parent(spine_ctrl_list[2][0], inbetween_loc[1]) -> Ctrl Index 2 to Loc Index 1 (Top mid)
	# mc.parent(spine_ctrl_list[1][0], inbetween_loc[0]) -> Ctrl Index 1 to Loc Index 0 (Bottom mid)
	
	# Make objects for clean parenting
	ctrl_mid_bot_zro = core.Dag(spine_ctrl_list[1][0])
	ctrl_mid_top_zro = core.Dag(spine_ctrl_list[2][0])
	
	# plp returns list of strings
	loc_mid_bot = core.Dag(inbetween_locs[0])
	loc_mid_top = core.Dag(inbetween_locs[1])
	
	ctrl_mid_bot_zro.parent(loc_mid_bot)
	ctrl_mid_top_zro.parent(loc_mid_top)


	# --- 7. Squash & Stretch Logic ---

	# Setup Naming
	base_name = core.check_name_style(tmpJnt[1])[0]
	base_name_space = f'{nameSpace}{base_name}'
	
	# Distance Node
	distance = core.DistanceBetween(name=f'{base_name_space}_btw')

	# Controllers for distance
	inb01_ctrl = core.Dag(spine_ctrl_list[0][1]) # Bottom Ctrl
	inb02_ctrl = core.Dag(spine_ctrl_list[3][1]) # Top Ctrl (Fixed index from 1 to 3 based on source list logic: 0=Bot, 3=Top)
	
	# Decompose Matrix
	inb01_decom = core.DecomposeMatrix(f'{base_name_space}01WorldPosi')
	inb02_decom = core.DecomposeMatrix(f'{base_name_space}02WorldPosi')

	inb01_ctrl.attr('worldMatrix[0]') >> inb01_decom.attr('inputMatrix')
	inb02_ctrl.attr('worldMatrix[0]') >> inb02_decom.attr('inputMatrix')

	inb01_decom.attr('outputTranslate') >> distance.attr('point1')
	inb02_decom.attr('outputTranslate') >> distance.attr('point2')

	original_length = mc.getAttr(distance.name + '.distance')

	# Global Scale Adjustment
	place_ctrl = core.Dag(placement_ctrl)
	global_scale_mdv = core.MultiplyDivine(f'{base_name_space}GlobalScale_mdv', operation=2)
	distance.attr('distance') >> global_scale_mdv.attr('input1X')

	# Prevent infinity scale
	global_store_scale_pma = core.PlusMinusAverage(f'{base_name_space}StoreGlobalScale_pma')
	place_ctrl.attr('scaleX') >> global_store_scale_pma.attr('input1D[0]')
	place_ctrl.attr('scaleY') >> global_store_scale_pma.attr('input1D[1]')
	place_ctrl.attr('scaleZ') >> global_store_scale_pma.attr('input1D[2]')

	avg_value_mdv = core.MultiplyDivine(f'{base_name_space}AvgGlobalScale_mdv', operation=2)
	avg_value_mdv.attr('input2X').value = 3
	global_store_scale_pma.attr('output1D') >> avg_value_mdv.attr('input1X')
	avg_value_mdv.attr('outputX') >> global_scale_mdv.attr('input2X')

	# Stretch Factor
	baseValue_mdv = core.MultiplyDivine(f'{base_name_space}BaseValue', operation=2)
	global_scale_mdv.attr('outputX') >> baseValue_mdv.attr('input1X')
	baseValue_mdv.attr('input2X').value = original_length

	# Volume Preservation (1 / sqrt(Stretch))
	squareRootValue_mdv = core.MultiplyDivine(f'{base_name_space}SquareRootValue', operation=3)
	baseValue_mdv.attr('outputX') >> squareRootValue_mdv.attr('input1X')
	squareRootValue_mdv.attr('input2X').value = 0.5

	volume_preservation_mdv = core.MultiplyDivine(f'{base_name_space}oneDiv', operation=2)
	volume_preservation_mdv.attr('input1X').value = 1
	squareRootValue_mdv.attr('outputX') >> volume_preservation_mdv.attr('input2X')

	# Clamp Value
	value_clamp = core.Clamp(f'{base_name_space}ClampValue')
	value_clamp.attr('minR').value = 0.001
	value_clamp.attr('maxR').value = 100.00
	volume_preservation_mdv.attr('outputX') >> value_clamp.attr('inputR')

	# Connect to Mid Joints (Rig Joints)
	# spine_jnt_list indices: 0=Bot, 1=MidBot, 2=MidTop, 3=Top
	inb01_jnt = core.Dag(spine_jnt_list[1].name)
	inb02_jnt = core.Dag(spine_jnt_list[2].name)

	# Apply Volume Preservation
	value_clamp.attr('outputR') >> inb01_jnt.attr('scaleX')
	value_clamp.attr('outputR') >> inb02_jnt.attr('scaleX')
	value_clamp.attr('outputR') >> inb01_jnt.attr('scaleZ')
	value_clamp.attr('outputR') >> inb02_jnt.attr('scaleZ')

	IkFkSpineLogger.info('Squash & Stretch Setup Complete.')


	# --- 8. Connect Bind Joints to Rig Joints ---
	
	for num, each_bind in enumerate(bind_jnt_list):
		# Using parentConMatrixGPT from mtc (matrixConstraint)
		# Note: mtc.parentConMatrixGPT returns (obj_target, obj_source)
		# We need to ensure we pass names or objects correctly
		mtc.parentConMatrixGPT(
			spine_jnt_list[num].name, 
			each_bind.name,
			nameSpace = 'pairBJnt_', 
			mo=True, 
			translate=True, 
			rotate=True, 
			scale=True
		)


	# --- 9. Final Organization ---

	# Position Main Group
	spineRig_grp.matchPosition(bind_jnt_list[0])
	spineRig_grp.matchRotation(bind_jnt_list[0])

	# Parent Main Group
	if parentTo and mc.objExists(parentTo):
		parent_obj = core.Dag(parentTo)
		spineRig_grp.parent(parent_obj)

	#... Parent Controllers to hip controller grp for make hip move more natheral
	#... Lower Ctrl Zro
	# ctrl_lower_zro = core.Dag(spine_ctrl_list[0][0])
	# ctrl_lower_zro.parent(spineRig_grp)

	mc.parent(spine_ctrl_list[0][0], hipCtrl)



	
	# Upper Ctrl Zro
	ctrl_upper_zro = core.Dag(spine_ctrl_list[3][0])
	ctrl_upper_zro.parent(spineRig_grp)

	# Organize Joints and Locators
	# Assuming we want to hide them or put them in jntStill_grp

	jntStill_grp = core.Dag('jntStill_grp')
	for each_jnt in spine_jnt_list:
		each_jnt.parent(jntStill_grp)

	for each_loc in inbetween_locs:
		# These are strings, need casting or direct use
		mc.parent(each_loc, jntStill_grp.name)

	# Setup Following
	if priorCtrl and mc.objExists(priorCtrl):
		mtc.parentConMatrixGPT(
			priorCtrl, 
			spineRig_grp.name, 
			mo=True, 
			translate=True, 
			rotate=True, 
			scale=True
		)

	IkFkSpineLogger.info(f'#### End of {partName} Rig ####')
	
	# Return useful objects
	return spineRig_grp, bind_jnt_list, spine_ctrl_list