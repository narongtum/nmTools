# -*- coding: utf-8 -*-
"""
This module is create spine IK hybride with FK  
source : nomanTools/21.03.Mar.29.Mon_ikSpinePart2
UPDATED: to use zroNewGrpWithOffset and matrixConstraint
"""

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

# --- Import Core Modules ---
from function.rigging.autoRig.base import core
reload(core)

# --- Import ENHANCED rigTools ---
from function.rigging.autoRig.base import eh_rigTools as rigTools
reload(rigTools)

# --- Import Matrix Constraint ---
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

from function.pipeline import logger 
reload(logger)

class spineHybridLog(logger.MayaLogger):
	LOGGER_NAME = "SpineIKRig"

def spineHybridIK(
				nameSpace = '' 		,
				# --- FIX 3: Inputs are now objects ---
				parentTo_grp = None 						,		
				tmpJnt = (		'spine01_tmpJnt' 			,
								'spine02_tmpJnt' 			,
								'spine03_tmpJnt' 			,
								'spine04_tmpJnt'			),
				prior_ctrl = None					, # Was 'cog_gmbCtrl'
				prior_jnt = None					, # Was 'hip_bJnt'				
				charScale = 1.0								,							
				linkRotOrder = True							,
				rotateOrder = 'yzx'								):

	# --- Validate Inputs ---
	if not parentTo_grp or not prior_ctrl or not prior_jnt:
		mc.error("spineHybridIK: Missing critical object inputs (parentTo_grp, prior_ctrl, prior_jnt).")
		return None

	core.makeHeader('Create spineHybridIK Rig')

	partName = 'spine'
	if nameSpace:
		partName = nameSpace + partName.capitalize()

	spine1 = core.Dag( tmpJnt[ 0 ] )
	spine2 = core.Dag( tmpJnt[ 1 ] )
	spine3 = core.Dag( tmpJnt[ 2 ] )
	spine4 = core.Dag( tmpJnt[ 3 ] )

	# Create joint at each spine
	spine1_bJnt = rigTools.jointAt( spine1 )
	spine2_bJnt = rigTools.jointAt( spine2 )
	spine3_bJnt = rigTools.jointAt( spine3 )
	spine4_bJnt = rigTools.jointAt( spine4 )

	# Parent each 
	spine4_bJnt.parent( spine3_bJnt )
	spine3_bJnt.parent( spine2_bJnt )
	spine2_bJnt.parent( spine1_bJnt )

	# Naming 
	spine1_bJnt.name = nameSpace + 'spine' + '01' + '_bJnt'
	spine2_bJnt.name = nameSpace + 'spine' + '02' + '_bJnt'
	spine3_bJnt.name = nameSpace + 'spine' + '03' + '_bJnt'
	spine4_bJnt.name = nameSpace + 'spine' + '04' + '_bJnt'

	# freeze
	spine1_bJnt.freeze()
	spine2_bJnt.freeze()
	spine3_bJnt.freeze()
	spine4_bJnt.freeze()

	# joint label
	spine1_bJnt.setLable('CEN','spine')
	spine2_bJnt.setLable('CEN','spine')
	spine3_bJnt.setLable('CEN','spine')
	spine4_bJnt.setLable('CEN','spine')

	start_jnt = spine1_bJnt.name
	end_jnt = spine4_bJnt.name
	partName = 'spineIK'
	if nameSpace:
		partName = nameSpace + partName.capitalize()

	# create spine ik
	oSpine_ik = core.DoIk(startJoint = start_jnt , endEffector = end_jnt ,solverType = 'ikSplineSolver'  , parentCurve = False)
	oSpine_ik.name = partName + '_ikh'
	oSpine_ik.crv = partName + '_crv'

	# create joint top 
	upr_pxyJnt = core.Joint(partName + 'Upr' +'_pxyJnt')
	upr_pxyJnt.setLable('CEN','none')
	upr_pxyJnt.attr('segmentScaleCompensate').value = 0
	upr_pxyJnt.attr('rotateOrder').value = 1 # 'yzx'

	# create joint  bottom
	lwr_pxyJnt = core.Joint(partName + 'Lwr' +'_pxyJnt')
	lwr_pxyJnt.setLable('CEN','none')
	lwr_pxyJnt.attr('rotateOrder').value = 1 # 'yzx'
	lwr_pxyJnt.attr('segmentScaleCompensate').value = 0

	# snap position
	upr_pxyJnt.snapPoint(spine4_bJnt)
	lwr_pxyJnt.snapPoint(spine1_bJnt)

	# skin it with spine IK curve
	core.SkinCluster( upr_pxyJnt.name , lwr_pxyJnt.name , oSpine_ik.crv , maximumInfluences = 2 , name = partName + '_skc')

	# Upr
	spineUpr_ctrl = core.Dag( partName + 'Upr' + '_ctrl' )
	spineUpr_ctrl.nmCreateController('cube_ctrlShape')
	spineUpr_ctrl.editCtrlShape( axis = charScale * 4.0 )
	
	# --- FIX 1: Use zroNewGrpWithOffset ---
	spineUprZro_grp, spineUprOffset_grp = rigTools.zroNewGrpWithOffset( spineUpr_ctrl )
	spineUprZro_grp.name = partName + 'Upr' + 'Zro_grp'
	
	spineUpr_ctrl.color = 'softBlue'
	spineUpr_ctrl.rotateOrder = rotateOrder
	spineUprGmbl_ctrl = core.createGimbal( spineUpr_ctrl )
	spineUprZro_grp.matchPosition( upr_pxyJnt )
	
	# --- FIX 2: Use Matrix Constraint ---
	mtc.parentConMatrix( source=spineUprGmbl_ctrl, target=upr_pxyJnt, mo=True )

	# Lower
	spineLwr_ctrl = core.Dag( partName + 'Lwr' + '_ctrl' )
	spineLwr_ctrl.nmCreateController('cube_ctrlShape')
	spineLwr_ctrl.editCtrlShape( axis = charScale * 3.5 )

	# --- FIX 1: Use zroNewGrpWithOffset ---
	spineLwrZro_grp, spineLwrOffset_grp = rigTools.zroNewGrpWithOffset( spineLwr_ctrl )
	spineLwrZro_grp.name = partName + 'Lwr' + 'Zro_grp'
	
	spineLwr_ctrl.color = 'softBlue'
	spineLwr_ctrl.rotateOrder = rotateOrder
	spineLwrGmbl_ctrl = core.createGimbal( spineLwr_ctrl )
	spineLwrZro_grp.matchPosition( lwr_pxyJnt )

	# --- FIX 2: Use Matrix Constraint ---
	mtc.parentConMatrix( source=spineLwrGmbl_ctrl, target=lwr_pxyJnt, mo=True )

	# ... (IK Twist setup remains the same) ...
	ik_handle = core.Dag(oSpine_ik.name)
	ik_handle.attr('dTwistControlEnable').value = 1
	ik_handle.attr('dForwardAxis').value = 2
	ik_handle.attr('dWorldUpAxis').value = 4
	upUpr_loc = core.Locator( partName + 'Upr' + '_loc' )
	upUpr_loc.snapPoint(spineUpr_ctrl)
	upUpr_loc.moveObj([0, 0, 12.5*charScale])
	upUpr_loc.parent(spineUprGmbl_ctrl)
	upUpr_loc.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz','v')
	upLwr_loc = core.Locator( partName + 'Lwr' + '_loc' )
	upLwr_loc.snapPoint(spineLwr_ctrl)
	upLwr_loc.moveObj([0, 0, 12.5*charScale])
	upLwr_loc.parent(spineLwrGmbl_ctrl)
	upLwr_loc.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz','v')
	ik_handle.attr('dWorldUpType').value = 2
	mc.connectAttr(upLwr_loc.name + '.worldMatrix[0]' , oSpine_ik.name + '.dWorldUpMatrix')
	mc.connectAttr(upUpr_loc.name + '.worldMatrix[0]' , oSpine_ik.name + '.dWorldUpMatrixEnd')

	# Create FK joints
	spine1_fkJnt = rigTools.jointAt( spine1 )
	spine2_fkJnt = rigTools.jointAt( spine2 )
	spine3_fkJnt = rigTools.jointAt( spine3 )
	spine4_fkJnt = rigTools.jointAt( spine4 )

	spine1_fkJnt.name = nameSpace + 'spine' + '01' + '_fkJnt'
	spine2_fkJnt.name = nameSpace + 'spine' + '02' + '_fkJnt'
	spine3_fkJnt.name = nameSpace + 'spine' + '03' + '_fkJnt'
	spine4_fkJnt.name = nameSpace + 'spine' + '04' + '_fkJnt'

	spine1_fkJnt.rotateOrder = rotateOrder
	spine2_fkJnt.rotateOrder = rotateOrder
	spine3_fkJnt.rotateOrder = rotateOrder
	spine4_fkJnt.rotateOrder = rotateOrder

	spine4_fkJnt.parent( spine3_fkJnt )
	spine3_fkJnt.parent( spine2_fkJnt )
	spine2_fkJnt.parent( spine1_fkJnt )
	
	spine1_fkJnt.attr('v').value = 0 # Hide FK chain

	# --- FIX 2: Use Matrix Constraint (FK Jnts -> IK Ctrl Zro Grps) ---
	mtc.parentConMatrix( source=spine1_fkJnt, target=spineLwrZro_grp, mo=True )
	mtc.parentConMatrix( source=spine4_fkJnt, target=spineUprZro_grp, mo=True )

	# fk spine 02
	spineFk02_ctrl = core.Dag( partName + '02' + 'Fk' + '_ctrl' )
	spineFk02_ctrl.nmCreateController('circle_ctrlShape')
	spineFk02_ctrl.editCtrlShape( axis = charScale * 1.6 )
	
	# --- FIX 1: Use zroNewGrpWithOffset ---
	spineFk02Zro_grp, spineFk02Offset_grp = rigTools.zroNewGrpWithOffset( spineFk02_ctrl )
	spineFk02Zro_grp.name = partName + '02' + 'Fk' + 'Zro_grp'

	spineFk02_ctrl.color = 'softBlue'
	spineFk02_ctrl.rotateOrder = rotateOrder
	spineFk02Gmbl_ctrl = core.createGimbal( spineFk02_ctrl )
	spineFk02Zro_grp.matchPosition( spine2_fkJnt )
	
	# --- FIX 2: Use Matrix Constraint ---
	mtc.parentConMatrix( source=spineFk02Gmbl_ctrl, target=spine2_fkJnt, mo=True )

	# fk spine 03
	spineFk03_ctrl = core.Dag( partName + '03' + 'Fk' + '_ctrl' )
	spineFk03_ctrl.nmCreateController('circle_ctrlShape')
	spineFk03_ctrl.editCtrlShape( axis = charScale * 1.65 )

	# --- FIX 1: Use zroNewGrpWithOffset ---
	spineFk03Zro_grp, spineFk03Offset_grp = rigTools.zroNewGrpWithOffset( spineFk03_ctrl )
	spineFk03Zro_grp.name = partName + '03' + 'Fk' + 'Zro_grp'

	spineFk03_ctrl.color = 'softBlue'
	spineFk03_ctrl.rotateOrder = rotateOrder
	spineFk03Gmbl_ctrl = core.createGimbal( spineFk03_ctrl )
	spineFk03Zro_grp.matchPosition( spine3_fkJnt )

	# --- FIX 2: Use Matrix Constraint (Corrected target to spine3_fkJnt) ---
	# Original code had a bug linking to spine2_fkJnt
	mtc.parentConMatrix( source=spineFk03Gmbl_ctrl, target=spine3_fkJnt, mo=True )

	# parent fk spine03 to fk spine02
	spineFk03Zro_grp.parent(spineFk02Gmbl_ctrl)

	# ... (Squash & Stretch logic remains the same) ...
	# ... (Note: This logic is hardcoded to 3 joints and names)
	curveInfo = core.CurveInfo( partName + 'CurveInfo')
	spine_crv = core.Dag(partName + '_crv')
	divider = 3 
	for num in range(1,4):
		spStretch_mdv = core.MultiplyDivineWithVal(partName + 'SpStretch%02d' %num, 2)
		spStretch_mdv.attr('input2X').value = divider
		spineUpr_ctrl.attr('translateY') >> spStretch_mdv.attr('input1X')
		spStretchDef_add = core.AddDoubleLinear(partName + 'SpStretchDef%02d' %num )
		spStretchDef_add.suffix
		defaultVal = mc.getAttr('spine%02d_bJnt' %num + '.translateY')
		spStretchDef_add.attr('input2').value = defaultVal
		spStretch_mdv.attr('outputX') >> spStretchDef_add.attr('input1')
		mc.connectAttr(spStretchDef_add.name + '.output' , 'spine%02d_bJnt.translateY' %num)

	# --- FIX 3: Use Object Inputs for Parenting ---
	spine1_bJnt.parent(prior_jnt) # Was priorJnt (string)

	spineIK_grp = core.Null(partName + 'Rig_grp')

	# parent local grp
	spineFk02Zro_grp.parent(spineIK_grp)
	spine1_fkJnt.parent(spineIK_grp)
	spineUprZro_grp.parent(spineIK_grp)
	spineLwrZro_grp.parent(spineIK_grp)

	mc.setAttr(spine_crv.name + '.' + 'inheritsTransform' , 0)
	spine_crv.parent(spineIK_grp)

	# --- FIX 2 & 3: Use Matrix Constraint and Object Input ---
	mtc.parentConMatrix( source=prior_ctrl, target=spineIK_grp, mo=True )
	
	spineIK_grp.parent(parentTo_grp) # Was parentTo (string)

	ik_handle.parent('ikh_grp')

	spineJnt_grp = core.Null(partName + 'Jnt_grp')
	upr_pxyJnt.parent(spineJnt_grp)
	lwr_pxyJnt.parent(spineJnt_grp)
	spineJnt_grp.parent('jnt_grp')

	# hide visibility
	spine_crv.attr('v').value = 0
	spineJnt_grp.attr('v').value = 0
	ik_handle.attr('v').value = 0

	# add link rotate order
	if linkRotOrder:
		spineLwr_ctrl.addRotEnum()
		spineLwrGmbl_ctrl.addRotEnum()
		spineUpr_ctrl.addRotEnum()
		spineUprGmbl_ctrl.addRotEnum()	
		spineFk02_ctrl.addRotEnum()
		spineFk02Gmbl_ctrl.addRotEnum()
		spineFk03_ctrl.addRotEnum()
		spineFk03Gmbl_ctrl.addRotEnum()

	spineHybridLog.info('return: '+spine4_bJnt.name)
	
	# --- FIX 3: Return Objects ---
	return {
		'jnt_start': spine1_bJnt,
		'jnt_end': spine4_bJnt,
		'ctrl_lwr': spineLwr_ctrl,
		'ctrl_upr': spineUpr_ctrl,
		'ctrl_fk02': spineFk02_ctrl,
		'ctrl_fk03': spineFk03_ctrl
	}