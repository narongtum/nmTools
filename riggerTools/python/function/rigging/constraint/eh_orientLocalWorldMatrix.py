# -*- coding: utf-8 -*-
"""
Module: eh_matrixConstraint
Description: Advanced Matrix Constraints and Space Switching using eh_core.
"""

'''
from function.rigging.constraint import eh_matrixConstraint as ehmtc
reload(ehmtc)
'''
import maya.cmds as mc
import maya.api.OpenMaya as om
from function.framework.reloadWrapper import reloadWrapper as reload

# --- Import Enhanced System ---
from function.rigging.autoRig.base import core
reload(core)

from function.pipeline import logger
reload(logger)

class MatrixConstraintLogger(logger.MayaLogger):
	LOGGER_NAME = "EHMatrixConstraint"

# ------------------------------------------------------------------------------
# Helper: Matrix Calculation
# ------------------------------------------------------------------------------
def _get_offset_matrix(source, target):
	"""
	Calculates the offset matrix: Target World * Inverse Source World.
	Returns a list of 16 floats (row-major).
	"""
	# Get MDagPaths
	sel = om.MSelectionList()
	sel.add(source)
	sel.add(target)
	
	source_path = sel.getDagPath(0)
	target_path = sel.getDagPath(1)
	
	# Get Inclusive Matrix (World Matrix)
	source_mat = source_path.inclusiveMatrix()
	target_mat = target_path.inclusiveMatrix()
	
	# Calculate Offset: Target * Inverse(Source)
	offset_mat = target_mat * source_mat.inverse()
	
	return list(offset_mat)

# ------------------------------------------------------------------------------
# Main Function: Orient Local/World Matrix
# ------------------------------------------------------------------------------
def orientLocalWorldMatrix(
		ctrl, 
		localObj, 
		worldObj, 
		target, 
		attrName='localWorld', 
		bodyPart=None
	):
	"""
	Creates a Matrix-based Orientation Space Switch (Local/World).
	Replaces the legacy 'orientLocalWorldCtrl' which used constraints and dummy groups.

	Args:
		ctrl (str/Dag): The controller that will hold the switch attribute.
		localObj (str/Dag): The driver object for 'Local' space (usually parent).
		worldObj (str/Dag): The driver object for 'World' space.
		target (str/Dag): The object to be constrained (usually ZroGrp).
		attrName (str): Name of the blend attribute (0=Local, 1=World).
		bodyPart (str): Prefix for naming nodes.

	Returns:
		dict: References to created nodes for debugging or organization.
	"""
	
	# --- 1. Setup Objects & Naming ---
	ctrl_obj = core.Dag(ctrl)
	local_obj = core.Dag(localObj)
	world_obj = core.Dag(worldObj)
	target_obj = core.Dag(target)
	
	# Determine base name
	if bodyPart:
		base_name = f"{bodyPart}_Space"
	else:
		base_name = core.check_name_style(target_obj.name)[0] + "_Space"
		
	MatrixConstraintLogger.info(f"Creating Matrix Space Switch for: {base_name}")

	# --- 2. Add Switch Attribute ---
	# if not ctrl_obj.attr(attrName).exists:
	ctrl_obj.addAttribute(ln=attrName, k=True, min=0, max=1, defaultValue=0)
	
	# --- 3. Calculate Initial Offsets (Maintain Offset) ---
	# We need the target to stay in place relative to both parents at the bind pose.
	# Local Offset = Target * Inv(LocalParent)
	# World Offset = Target * Inv(WorldParent)
	offset_local_val = _get_offset_matrix(local_obj.name, target_obj.name)
	offset_world_val = _get_offset_matrix(world_obj.name, target_obj.name)

	# --- 4. Build Matrix Network ---
	
	# 4.1 Local Branch (Offset * LocalObj World)
	# Using MultMatrix to combine Offset + Driver
	mat_local = core.MultMatrix(f"{base_name}_Local_mmx")
	mc.setAttr(f"{mat_local.name}.matrixIn[0]", offset_local_val, type="matrix")
	local_obj.attr('worldMatrix[0]') >> mat_local.attr('matrixIn[1]')
	
	# 4.2 World Branch (Offset * WorldObj World)
	mat_world = core.MultMatrix(f"{base_name}_World_mmx")
	mc.setAttr(f"{mat_world.name}.matrixIn[0]", offset_world_val, type="matrix")
	world_obj.attr('worldMatrix[0]') >> mat_world.attr('matrixIn[1]')
	
	# 4.3 Blending (WtAddMatrix)
	# This node blends the resulting World Matrices from both branches.
	mat_blend = core.WtAddMatrix(f"{base_name}_Blend_wtAdd")
	
	mat_local.attr('matrixSum') >> mat_blend.attr('wtMatrix[0].matrixIn')
	mat_world.attr('matrixSum') >> mat_blend.attr('wtMatrix[1].matrixIn')
	
	# --- 5. Drive Weights ---
	# Weight 0 (Local) = 1 - attr
	# Weight 1 (World) = attr
	
	rev_node = core.ReverseNam(f"{base_name}_Weight_rev")
	ctrl_obj.attr(attrName) >> rev_node.attr('inputX')
	
	# Connect
	rev_node.attr('outputX') >> mat_blend.attr('wtMatrix[0].weightIn') # Local
	ctrl_obj.attr(attrName) >> mat_blend.attr('wtMatrix[1].weightIn') # World
	
	# --- 6. Convert to Target Local Space ---
	# The result of mat_blend is a World Matrix.
	# To drive the target (Transform node), we must convert it to the target's Parent Space.
	# Calculation: ResultWorld * TargetParentInverse
	
	mat_final = core.MultMatrix(f"{base_name}_Final_mmx")
	mat_blend.attr('matrixSum') >> mat_final.attr('matrixIn[0]')
	target_obj.attr('parentInverseMatrix[0]') >> mat_final.attr('matrixIn[1]')
	
	# --- 7. Decompose & Apply Rotation ---
	# Since this is an "Orient" constraint logic, we extract Rotation only.
	
	decomp = core.DecomposeMatrix(f"{base_name}_Result_dcmp")
	mat_final.attr('matrixSum') >> decomp.attr('inputMatrix')
	
	# Connect Rotation
	# Note: Standard DecomposeMatrix outputs Euler rotations. 
	# For standard controllers (ZroGrps), this is usually sufficient.
	# If gimbal lock or flipping occurs, a Quaternion-to-Euler chain (like in matrixConstraint.py) might be needed.
	# For now, we implement the direct connection for efficiency.
	
	decomp.attr('outputRotate') >> target_obj.attr('rotate')
	
	# Ensure Rotation Order matches
	rot_order = target_obj.attr('rotateOrder').value
	decomp.attr('inputRotateOrder').value = rot_order

	MatrixConstraintLogger.info(f"Space Switch Complete. Attribute '{attrName}' on '{ctrl_obj.name}' controls orientation.")

	return {
		"mult_local": mat_local,
		"mult_world": mat_world,
		"blend": mat_blend,
		"reverse": rev_node,
		"final_mult": mat_final,
		"decompose": decomp
	}