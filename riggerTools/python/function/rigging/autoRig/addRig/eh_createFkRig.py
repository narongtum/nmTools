# -*- coding: utf-8 -*-
from function.framework.reloadWrapper import reloadWrapper as reload
import maya.cmds as mc

# ... Import Core
from function.rigging.autoRig.base import core
reload(core)

# ... Import Enhanced Rig Tools [Updated]
from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

from function.rigging.util import misc
reload(misc)

# ... Import Matrix Constraint
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

def create_fk_chain(
		nameSpace='',
		parentCtrlTo='head_gmblCtrl',
		jntLst=('ear01LFT_bJnt', 'ear02LFT_bJnt', 'ear03LFT_bJnt'),
		charScale=1,
		priorJnt='head01_bJnt',
		side='LFT',
		ctrlShape='circle_ctrlShape',
		localWorld=False,
		color='red',
		curlCtrl=False,
		curlPosiAtFirst=True,
		rotateOrder='zxy',
		parentToPriorJnt=False,
		parentMatrix=False,
		curlCtrlShape='stick_ctrlShape',
		constraintCurl=True,
		segmentScaleCompensate=False
	):
	"""
	Creates an FK chain with optional Curl controller and Matrix-based Local/World switch.
	Uses eh_rigTools for object-based return values.
	
	Returns:
		dict: Containing keys 'ctrls', 'jnts', 'zroGrps', 'rigGrp', 'curlCtrl', 'metaNode', 'localWorldNode'
	"""

	# ------------------------------------------------------------------
	# 1. Naming & Preparation
	# ------------------------------------------------------------------
	# Analyze the first joint to determine naming convention
	name_info = core.check_name_style(name=jntLst[0])
	base_name_raw = name_info[0] # Full base name (e.g. 'L_ear01')
	is_default_style = name_info[3] # True if side is suffix (ear01LFT)
	name_no_side = name_info[4] # Name without side (ear01)

	# Determine Rig Group Name
	if is_default_style:
		# Old Style: ear01CurlLFT
		part_name = f"{nameSpace}{name_no_side}{side}"
	else:
		# New Style: L_ear01Curl
		# Construct prefix based on side presence
		prefix = f"{side}_" if side else ""
		part_name = f"{prefix}{nameSpace}{name_no_side}"

	rigGrp = core.Null(f'{part_name}Rig_grp')

	# Data Containers
	data = {
		'ctrls': [],
		'jnts': [],
		'gmbls': [],
		'zroGrps': [],
		'offsetGrps': [],
		'bJnts': [],
		'curlCtrl': None,
		'metaNode': None,
		'localWorld': None
	}

	# ------------------------------------------------------------------
	# 2. Main FK Loop
	# ------------------------------------------------------------------
	for num, jnt in enumerate(jntLst):
		# Clean name for this specific joint
		jnt_base_name = core.check_name_style(name=jnt)[0]
		
		# Create Controller
		ctrl = core.Dag(f'{jnt_base_name}_ctrl')
		ctrl.nmCreateController(ctrlShape)
		ctrl.editCtrlShape(axis=charScale * 6.4)
		ctrl.color = color
		ctrl.rotateOrder = rotateOrder

		# Create Gimbal
		gimbal = core.createGimbal(ctrl)
		gimbal.rotateOrder = rotateOrder

		# Reference Bind Joint
		bJnt = core.Dag(jnt)
		
		# Disable Segment Scale Compensate (Essential for FK chains)
		if not segmentScaleCompensate:
			if mc.attributeQuery('segmentScaleCompensate', node=bJnt.name, exists=True):
				bJnt.attr('segmentScaleCompensate').value = 0

		# Create Hierarchy (Zro -> Offset -> Ctrl) using eh_rigTools
		# eh_rigTools returns Objects, so we can access .name or methods directly
		zroGrp, offsetGrp = rigTools.zroNewGrpWithOffset(ctrl)
		
		# Snap & Rename
		zroGrp.snap(bJnt)
		zroGrp.name = f'{jnt_base_name}Zro_grp'
		offsetGrp.name = f'{jnt_base_name}Offset_grp'

		# Store Data
		data['ctrls'].append(ctrl)
		data['jnts'].append(jnt)
		data['gmbls'].append(gimbal)
		data['zroGrps'].append(zroGrp)
		data['offsetGrps'].append(offsetGrp)
		data['bJnts'].append(bJnt)

		# Parenting Logic
		if num > 0:
			# Parent to previous gimbal
			zroGrp.parent(data['gmbls'][num - 1])
		else:
			# Parent root control to Rig Group
			rigGrp.maSnap(bJnt)
			zroGrp.parent(rigGrp)

	# ------------------------------------------------------------------
	# 3. External Parenting
	# ------------------------------------------------------------------
	if parentCtrlTo and mc.objExists(parentCtrlTo):
		rigGrp.parent(parentCtrlTo)
	
	if priorJnt and mc.objExists(priorJnt):
		# Parent the first joint to the prior joint structure
		if parentToPriorJnt:
			 data['bJnts'][0].parent(priorJnt)

	# ------------------------------------------------------------------
	# 4. Curl Controller (Optional)
	# ------------------------------------------------------------------
	if curlCtrl:
		# Naming for Curl
		if is_default_style:
			curl_base_name = f'{nameSpace}{name_no_side}Curl{side}'
		else:
			prefix = f"{side}_" if side else ""
			curl_base_name = f'{prefix}{nameSpace}{name_no_side}Curl'

		# Create Curl Ctrl
		curl_ctrl = core.Dag(f'{curl_base_name}_ctrl')
		curl_ctrl.nmCreateController(curlCtrlShape)
		curl_ctrl.editCtrlShape(axis=charScale * 7.4)
		curl_ctrl.color = color
		curl_ctrl.rotateOrder = rotateOrder

		# Use eh_rigTools for grouping
		zroGrpCurl, offsetCurl = rigTools.zroNewGrpWithOffset(curl_ctrl)

		# Snap Position (Root or Tip)
		target_snap_jnt = data['bJnts'][0] if curlPosiAtFirst else data['bJnts'][-1]
		zroGrpCurl.maSnap(target_snap_jnt)

		# Lock & Hide Attributes (Clean Loop)
		curl_ctrl.lockHideAttrLst('tx', 'ty', 'tz', 'sx', 'sy', 'sz', 'v')

		# Add 'Detail' Attribute to toggle FK chain visibility
		curlShape = core.Dag(curl_ctrl.shape)
		curlShape.addAttribute(at='long', min=0, max=1, longName='Detail', keyable=True, defaultValue=0)
		
		# Connect Detail -> FK Root Visibility
		try:
			mc.connectAttr(f'{curlShape.name}.Detail', f"{data['zroGrps'][0].name}.visibility", f=True)
		except:
			print(f"Warning: Could not connect visibility to {data['zroGrps'][0].name}")

		# Drive FK Offsets using Curl Rotation (Multiplied)
		# Create Nodes
		pma_node = core.PlusMinusAverage(f'{curl_base_name}_pma')
		mdv_node = core.MultiplyDivine(f'{curl_base_name}_mdv')

		# Connect: Curl.rotate -> PMA -> MDV -> OffsetGrp.rotate
		curl_ctrl.attr('rotate') >> pma_node.attr('input3D[0]')
		pma_node.attr('output3D') >> mdv_node.attr('input1')

		for offGrp in data['offsetGrps']:
			mdv_node.attr('output') >> offGrp.attr('rotate')

		# Parent Curl Group
		zroGrpCurl.parent(rigGrp)

		# Optional Constraint for Curl itself
		if constraintCurl:
			curl_psCon = core.parentConstraint(target_snap_jnt, zroGrpCurl, mo=False)
			curl_psCon.name = f'{curl_base_name}_psCon'

		# Store Data
		data['curlCtrl'] = curl_ctrl

		# --- Meta Node Creation ---
		meta_name = f'{curl_base_name}_meta'
		fkRig_meta = core.MetaGeneric(meta_name)
		fkRig_meta.addAttribute(attributeType='message', longName='baseName')
		
		# Connections
		curl_ctrl.attr('message') >> fkRig_meta.attr('Rig_Prior')
		pma_node.attr('message') >> fkRig_meta.attr('passValue') 
		
		# Set Meta Data
		fkRig_meta.setAttribute('Color', color, type='string')
		fkRig_meta.setAttribute('Side', side, type='string')
		fkRig_meta.setAttribute('Base_Name', rigGrp.name, type='string')
		
		data['metaNode'] = fkRig_meta

		# Define attribute holder for Local/World
		localWorld_attr_holder = curlShape.name

	else:
		# If no curl, use the first controller shape for Local/World attr
		localWorld_attr_holder = misc.shapeName(data['ctrls'][0])

	# ------------------------------------------------------------------
	# 5. Matrix Local/World Switch
	# ------------------------------------------------------------------
	if localWorld:
		# Target to drive: The Zero Group of the first controller
		target_grp = data['zroGrps'][0]
		
		print(f"Creating Matrix Local/World for {target_grp.name}")
		
		# Use matrixConstraint module (mtc)
		# Note: eh_orientLocalWorldMatrix handles the matrix logic internally
		
		lw_nodes = mtc.eh_orientLocalWorldMatrix(
			ctrl=data['curlCtrl'].name if curlCtrl else data['ctrls'][0].name,
			localObj=parentCtrlTo,
			worldObj='ctrl_grp', # Ensure this exists in scene
			target=target_grp.name,
			attrName='localWorld',
			parentMode='orient', 
			bodyPart=name_no_side
		)
		data['localWorld'] = lw_nodes

	# ------------------------------------------------------------------
	# 6. Drive Joints (Constraint or Matrix)
	# ------------------------------------------------------------------
	for i, jnt in enumerate(jntLst):
		driver = data['gmbls'][i]
		driven = data['bJnts'][i]
		
		# Check Name
		base_jnt_name = core.check_name_style(name=jnt)[0]

		if parentMatrix:
			# Use Matrix Constraint
			mtc.parentConMatrix(
				driver.name, 
				driven.name, 
				mo=True, 
				translate=True, 
				rotate=True, 
				scale=True
			)
		else:
			# Standard Constraints (Direct core usage for simple constraints)
			psCon = core.parentConstraint(driver, driven)
			psCon.name = f'{base_jnt_name}_psCons'
			
			sclCon = core.scaleConstraint(driver, driven)
			sclCon.name = f'{base_jnt_name}_scalCons'

	print(f'\n# FK Chain Creation Complete: {part_name}')
	
	return data