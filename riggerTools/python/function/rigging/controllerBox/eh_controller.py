# -*- coding: utf-8 -*-
"""
Module: eh_controller
Description: Controller management module. 
			 - Ported logic from 'adjustController.py' (creControllerFunc).
			 - Returns core Objects instead of strings.
			 - Supports Matrix Constraints.
"""
'''
from function.rigging.controllerBox import eh_controller as eh_adjust
reload(eh_adjust)
'''

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

# --- Import Core ---
from function.rigging.autoRig.base import core
reload(core)

# --- Import Matrix Constraint ---
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

from function.pipeline import logger 
reload(logger)

class ControllerLogger(logger.MayaLogger):
	LOGGER_NAME = "EHController"


# -----------------------------------------------------------------------------
# Grouping Utilities
# -----------------------------------------------------------------------------

def createZeroGroupWithOffset(obj):
	"""
	Creates a standard Zero Group and Offset Group structure above the object.
	Structure: Zro_grp -> Offset_grp -> Obj
	
	Args:
		obj (str/Dag): The object to group.
		
	Returns:
		tuple: (core.Null zro_grp, core.Null offset_grp) as OBJECTS.
	"""
	child = core.Dag(obj)
	
	# Use core's naming logic to get a clean base name
	name = core.check_name_style(name=child.name)[0]

	zro_grp = core.Null(name + 'Zro_grp')
	offset_grp = core.Null(name + 'Offset_grp')

	offset_grp.parent(zro_grp)
	zro_grp.snap(child)
	child.parent(offset_grp)

	return zro_grp, offset_grp


def createZeroGroup(obj):
	"""
	Simple Zero Group (Single level).
	Structure: Zro_grp -> Obj
	
	Returns:
		core.Null: The zero group object.
	"""
	child = core.Dag(obj)
	
	# Update: Use check_name_style for consistent base name finding
	name = core.check_name_style(name=child.name)[0]

	grp = core.Null(name + 'Zro_grp')
	grp.snap(child)
	child.parent(grp)

	return grp


# -----------------------------------------------------------------------------
# Controller Creation
# -----------------------------------------------------------------------------

def create(
		nameSpace, 
		name, 
		ctrlShape, 
		rotateOrder='yzx', 
		parentTo=None, 
		charScale=1, 
		color='yellow', 
		rotation=(0,0,0), 
		constraint=True,
		matrixConstraint=True, 
		scaleConstraint=True
	):
	"""
	Creates a controller with Zro/Offset groups, Gimbal, and Constraints.
	Based on 'adjustController.creControllerFunc' logic.
	
	Returns:
		tuple: (zro_grp, ctrl, gmbl_ctrl) as OBJECTS.
	"""
	
	# 1. Resolve Naming
	if not nameSpace:
		part = core.check_name_style(name)[0]
	else:
		clean_name = name.split(':')[-1] if ':' in name else name
		base_name = core.check_name_style(clean_name)[0]
		part = f"{nameSpace}{base_name}"
		
	ControllerLogger.info(f"Creating Controller for: {part}")

	# 2. Create Controller & Shape
	controller_ctrl = core.Dag(part + '_ctrl')
	controller_ctrl.nmCreateController(ctrlShape)
	controller_ctrl.rotateShape(rotation)
	
	# 3. Attributes & Color
	controller_ctrl.editCtrlShape(axis=charScale * 1.2)
	controller_ctrl.color = color
	controller_ctrl.rotateOrder = rotateOrder
	controller_ctrl.hideArnoldNode()

	# 4. Create Gimbal
	controllerGmbl_ctrl = core.createGimbal(controller_ctrl)
	controllerGmbl_ctrl.rotateOrder = rotateOrder
	controllerGmbl_ctrl.hideArnoldNode()

	# 5. Create Hierarchy (Zro -> Offset -> Ctrl)
	# This uses the updated naming logic internally
	controllerZro_grp, offset_grp = createZeroGroupWithOffset(controller_ctrl)

	# 6. Positioning
	controllerZro_grp.matchPosition(name)
	controllerZro_grp.matchRotation(name)

	# 7. Constraints
	if constraint:
		target = name 
		
		if matrixConstraint:
			# Use Matrix Constraint Module
			mtc.parentConMatrixGPT(
				source=controllerGmbl_ctrl.name, 
				target=target, 
				mo=True, 
				translate=True, 
				rotate=True, 
				scale=scaleConstraint
			)
		else:
			# Standard Constraints
			par_cons = core.parentConstraint(controllerGmbl_ctrl, target)
			par_cons.name = part + '_parCons'
			
			if scaleConstraint:
				scl_cons = core.scaleConstraint(controllerGmbl_ctrl, target)
				scl_cons.name = part + '_scalCons'

	# 8. Parent to Hierarchy
	if parentTo:
		if mc.objExists(parentTo):
			controllerZro_grp.parent(parentTo)
		else:
			ControllerLogger.warning(f"Parent target '{parentTo}' does not exist.")

	return controllerZro_grp, controller_ctrl, controllerGmbl_ctrl