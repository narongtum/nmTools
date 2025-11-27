# -*- coding: utf-8 -*-
#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Pelvis rig module
# eh_hipRig.py

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

# --- Import Core Modules ---
from function.rigging.autoRig.base import core as core
reload(core)

from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

# --- NEW: Import Matrix Constraint (mtc) ---
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

from function.pipeline import logger 
reload(logger)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)


color_part_dict = mnd.COLOR_part_dict

class HipRigLogger(logger.MayaLogger):
	LOGGER_NAME = "hipRig"

def createHipRig( 	nameSpace = '' , 
				ctrl_grp = 'ctrl_grp'  ,
				tmpJnt = ( 'cog_tmpJnt','hip_tmpJnt' )	, 
				charScale = ''):

	
	
	part = nameSpace + 'cog'
	HipRigLogger.info('Start of %s rig' %part)
	core.makeHeader('Start of %s rig' %part)

	# core.makeHeader('Start of %s rig' %part)

	# ctrl_grp = '%s%s' %(nameSpace,ctrl_grp) 
	# Create joint and rename to root
	rootJnt = core.Joint()
	rootJnt.name = nameSpace + 'root'

	# seting joint label
	rootJnt.attr('side').value = 0
	rootJnt.attr('type').value = 1
		
	# Specify Group name
	# Specify temp joint name
	# find charscale
	# charScale = mc.getAttr( 'template_ctrl.scaleX' )
	# Template objects
	hip = core.Dag( tmpJnt[1] )
	# Create joint at Hip
	hip_bJnt = rigTools.jointAt( hip )
	hip_bJnt.parent( rootJnt.name )

	#hip_bJnt.rename('hip_bJnt')
	hip_bJnt.name = nameSpace + 'hip_bJnt'
	# add lable
	hip_bJnt.setLable('CEN','hip')

	# Create Main group
	name = nameSpace + 'hipRig'
	hipRig_grp = core.Null()
	hipRig_grp.rename( name + '_' + 'grp')

	# Create COG controller
	cog_ctrl = core.Dag( part + '_ctrl' )
	cog_ctrl.nmCreateController('cog_ctrlShape')
	
	# rigTools.zroNewGrpWithOffset returns (zro_grp, offset_grp)
	cogZro_grp, cogOffset_grp = rigTools.zroNewGrpWithOffset( cog_ctrl )

	# We use rename() instead of setting .name to avoid conflict if the object already exists
	cogZro_grp.rename( part + 'CtrlZro_grp' )
	cogOffset_grp.rename( part + 'CtrlOffset_grp' )
	# -----------------------------------------------------------------
	
	cog_ctrl.editCtrlShape( axis = charScale * 0.7 )
	cogGmbl_ctrl = core.createGimbal( cog_ctrl )
	cog_ctrl.color = color_part_dict['secondary'] #...'white'
	cog_ctrl.rotateOrder = 'xzy'
	cogGmbl_ctrl.rotateOrder = 'xzy'
	
	# Parenting cog controller to cog_tmpJnt
	cogZro_grp.matchPosition( tmpJnt[0] )
	cog_ctrl.matchRotation( tmpJnt[0]  )

	# Create hip ctrl
	part = nameSpace + 'hip'
	hip_ctrl = core.Dag( part + '_ctrl' )
	hip_ctrl.nmCreateController('hips_ctrlShape')
	hip_ctrl.editCtrlShape( axis = charScale * 0.9 )
	
	# --- FIX: Unpack Tuple for Hip Control ---
	hipZro_grp, hipOffset_grp = rigTools.zroNewGrpWithOffset( hip_ctrl )

	hipZro_grp.rename( part + 'Zro_grp' )
	hipOffset_grp.rename( part + 'Offset_grp' )
	# ----------------------------------------
	
	hipGmbl_ctrl = core.createGimbal( hip_ctrl )
	# shape adjustment
	hip_ctrl.color = color_part_dict['tertiary'] #... another 'red'

	# Parenting and positioning
	hipZro_grp.matchPosition( hip_bJnt )
	hip_ctrl.matchRotation( hip_bJnt )
	hip_ctrl.freeze()

	hipZro_grp.parent( cogGmbl_ctrl )

	# rotate order adjustment
	cog_ctrl.rotateOrder = 'xzy'
	hipGmbl_ctrl.rotateOrder = 'xzy'

	# =================================================================
	# --- NEW: Making joint parent to controller using Matrix Constraint ---
	# =================================================================
	
	# hipGmbl_ctrl (Source) -> hip_bJnt (Target)
	# Use mtc.parentConMatrixGPT to handle translate, rotate, and scale connections
	
	mtc.parentConMatrix(
		source=hipGmbl_ctrl.name, 
		target=hip_bJnt.name, 
		mo=True, 
		translate=True, 
		rotate=True, 
		scale=True
	)
	
	# Note: The matrix node setup automatically handles naming of the underlying nodes 
	# (multMatrix, decomposeMatrix, etc.) based on the target name (hip_bJnt).
	
	# =================================================================
	
	# move cog under tohipRig_grp
	cogZro_grp.parent( hipRig_grp )
	hipRig_grp.parent( ctrl_grp )


	meta_node = core.MetaGeneric(part)

	# meta_node.attr('Base_Name').value = part
	meta_node.setAttribute('Base_Name',part, type = 'string')

	# meta_node.attr('Side').value = 'Cen'
	meta_node.setAttribute('Side','Cen', type = 'string')

	meta_node.addAttribute( dataType = 'string' , longName = 'Prior_joint')
	meta_node.setAttribute('Prior_joint',hip_bJnt.name, type = 'string')
	# meta_node.attr('Prior_joint').value = hip_bJnt.name

	if mc.objExists('root_meta'):
		#... hook with message
		mc.connectAttr('root_meta'+ '.message', meta_node.name + '.Rig_Prior')
		# joint.attr('message') >> hook_node.attr('upJnt')

	HipRigLogger.info('\n#### End of %s Rig ####' %(part))
	core.makeHeader('End of %s Rig'%(part))
	return hip_bJnt.name
