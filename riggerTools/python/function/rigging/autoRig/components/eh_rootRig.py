# -*- coding: utf-8 -*-
# ...
# ... DESCRIPTION: Core function for creating the root rig groups and master controls.
# ...

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc
import logging

# ... Import necessary modules
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

# --- GLOBAL CONFIGURATION ---
color_part_dict = mnd.COLOR_part_dict

# set logging for debug mode
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)
# logging.disable(logging.CRITICAL)

# --- FUNCTION START ---
def createMasterGrp(nameSpace='', charScale=1.0, PROJECT_DICT={}):
	"""
	# ... Creates the main master control groups and controls for the rig hierarchy.
	
	# ... Args:
	# ...     nameSpace (str): Optional namespace for the character.
	# ...     charScale (float): Global scale factor for controls.
	# ...     PROJECT_DICT (dict): Dictionary containing project metadata.
	
	# ... Returns:
	# ...     core.Dag: The top-level rig group (rig_grp).
	"""

	part = 'Master controller'
	core.makeHeader(f'Start of {part} rig')
	
	# --- 1. Create Core Groups (Prefix 'C_' removed) ---
	rig_grp = core.Null('rig_grp') # The top-level container group
	noTouch_grp = core.Null('noTouch_grp') # For utility nodes/locators
	jnt_grp = core.Null('jnt_grp') # Container for final bind joints
	ikh_grp = core.Null('ikh_grp') # Container for IK handles
	ctrl_grp = core.Null('ctrl_grp') # Container for all controllers
	loc_grp = core.Null('loc_grp') # Container for utility locators
	
	# ... Group for objects constrained by matrix nodes
	ctrlStill_grp = core.Null('ctrlStill_grp')
	ctrlStill_grp.lockAllAttr(attrs=['t', 'r', 's', 'v']) # Lock and hide T, R, S, V attributes
	ctrlStill_grp.parent(noTouch_grp)
	
	# ... Group for snap functionality
	snapNull_grp = core.Null('snapNull_grp')

	# ... Master Control (Global Scale)
	master_ctrl = core.Dag('Master_ctrl')
	master_ctrl.nmCreateController('placement_ctrlShape')
	master_ctrl.editCtrlShape(axis=charScale * 1.4)
	master_ctrl.setColor(color_part_dict.get('primary', 'yellow'))
	
	# ... Placement/Root Control (Global Movement)
	placement_ctrl = core.Dag('Placement_ctrl')
	placement_ctrl.nmCreateController('fly_ctrlShape')
	placement_ctrl.editCtrlShape(axis=charScale * 1.0)
	placement_ctrl.setColor(color_part_dict.get('secondary', 'white'))
	
	# --- 3. Establish Hierarchy ---
	
	# ... Master Control Hierarchy
	master_ctrl.parent(rig_grp)
	placement_ctrl.parent(master_ctrl) # Master -> Placement/Root
	
	# ... Group Hierarchy (All functional groups under Placement/Root)
	ctrl_grp.parent(placement_ctrl)
	jnt_grp.parent(placement_ctrl)
	ikh_grp.parent(placement_ctrl)
	loc_grp.parent(placement_ctrl)
	
	# ... Utility Groups under rig_grp
	noTouch_grp.parent(rig_grp)
	snapNull_grp.parent(noTouch_grp)
	
	# --- 4. Set Rotation Order and Lock/Hide Attributes ---

	master_ctrl.rotateOrder = 'xzy'
	placement_ctrl.rotateOrder = 'xzy'

	# ... Lock unused attributes on Master Control
	for attr in ('sx', 'sy', 'sz'):
		master_ctrl.attr(attr).lockHide()
		
	# ... Lock and Hide all transform attributes on core groups
	for attr in ('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'):
		rig_grp.attr(attr).lockHide()
		jnt_grp.attr(attr).lockHide()
		ikh_grp.attr(attr).lockHide()
		noTouch_grp.attr(attr).lockHide()
		loc_grp.attr(attr).lockHide()

	# --- 5. Add Metadata Attributes to rig_grp ---
	
	rig_grp.addAttribute(attributeType='bool', longName='enable', defaultValue=0, keyable=False)
	rig_grp.addAttribute(attributeType='enum', en='Player:Enemy:Weapon', longName='asset_type', keyable=False)
	rig_grp.addAttribute(dataType='string', longName='asset_name', keyable=False)
	rig_grp.addAttribute(dataType='string', longName='logmsg', keyable=False)

	# --- 6. Create MetaRoot Node and Connect ---
	
	metaNode = core.MetaRoot('root_meta')

	if PROJECT_DICT:
		# ... Set Metadata for rig grp
		asset_name = PROJECT_DICT.get('asset_name', 'defaultAsset')
		version = PROJECT_DICT.get('version', 1.0)
		
		rig_grp.setAttribute('asset_name', asset_name, type='string')
		
		# ... Set metadata for MetaRoot node
		metaNode.setAttribute('Project', PROJECT_DICT.get('project', 'unknown'), type='string')
		metaNode.setAttribute('Version', version)
		metaNode.setAttribute('Base_Dir', PROJECT_DICT.get('Base_Dir', 'unknown'), type='string')
		
		# ... Connect rig_grp message to MetaRoot
		rig_grp.attr('message') >> metaNode.attr('rig_grp')

	logger.info(f'#### End of {part} Rig ####')
	
	# --- Return the main rig group ---
	return rig_grp