# -*- coding: utf-8 -*-
import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

# --- Import Refactored Modules ---
# Note: Assuming you save the new gen rig as 'eh_fkIkTwistGenRig.py'
# or you can rename the function inside the original file. 
# Here I will point to 'eh_fkIkTwistGenRig' for clarity.
from function.rigging.autoRig.bodyRig import eh_fkIkTwistGenRig as fitr
reload(fitr)

from function.rigging.autoRig.bodyRig import eh_createSoftIk as softIkfunc
reload(softIkfunc)

import logging
logger = logging.getLogger('eh_armRig')
logger.setLevel(logging.DEBUG)

def armRigExt(	
			nameSpace='',
			charScale=1.0,
			parentTo='ctrl_grp',
			side='LFT',
			region='arm',
			tmpJnt=('upperArmLFT_tmpJnt', 'lowerArmLFT_tmpJnt', 'handLFT_tmpJnt', 'armLFT_pov_tmpJnt'),
			priorJnt='clavLFT_bJnt',
			ikhGrp='ikh_grp',
			noTouchGrp='noTouch_grp',
			nullGrp='snapNull_grp',
			jnt_grp='jnt_grp',
			showInfo=False,
			ribbon=False,
			ribbonRes='high',
			ribbonName=('upLeg', 'lwrLeg'),
			propCtrl=False,
			keepFkIkBoth=True,
			povShape='pyramid',
			linkRotOrder=False,
			ctrlShape='fk_ctrlShape',
			creTwistJnt=True,
			softIk=True,
			softIkPrimaryAxis=2,
			softIkUpAxis=2,
			alongAxis='y',
			stickShape='stick_ctrlShape'
			):

	core.makeHeader(f'Start of {region}{side} Rig (EH Matrix Version)')

	# ----------------------------------------------------------------------
	# Call Gen Rig (Refactored)
	# ----------------------------------------------------------------------
	if creTwistJnt:
		result = fitr.fkIkTwistGenRig(
					nameSpace=nameSpace,
					charScale=charScale,
					parentTo=parentTo,
					side=side,
					region=region,
					tmpJnt=tmpJnt,
					priorJnt=priorJnt,
					ikhGrp=ikhGrp,
					noTouchGrp=noTouchGrp,
					nullGrp=nullGrp,
					jnt_grp=jnt_grp,
					povShape=povShape,
					keepFkIkBoth=keepFkIkBoth,
					ribbon=ribbon,
					ribbonRes=ribbonRes,
					ribbonName=ribbonName,
					showInfo=showInfo,
					linkRotOrder=linkRotOrder,
					ctrlShape=ctrlShape,
					creTwistJnt=creTwistJnt,
					alongAxis=alongAxis,
					stickShape=stickShape
		)
		
		# Unpack return values
		stickNam = result[0]
		hand_bJnt = result[1]
		# middle_bJnt = result[2]
		# upper_bJnt = result[3]
		ikhAll_name = result[4]
		# psStreEndName = result[5]
		softIk_name = result[6]
		priorMeta = result[7]

		# ------------------------------------------------------------------
		# Matcher Setup (Offset Null)
		# ------------------------------------------------------------------
		logger.info('Creating Null Snap group for matcher...')
		part = nameSpace + region
		offset_null = core.Null(f"{part}Offset{side}_null")
		
		# Use Matrix Constraint for Snap Null
		# Note: Using standard parentConMatrixGPT for full transform following
		from function.rigging.constraint import matrixConstraint as mtc
		reload(mtc)
		mtc.parentConMatrixGPT(hand_bJnt, offset_null.name, mo=False, translate=True, rotate=True, scale=True)
		
		offset_null.parent(nullGrp)

		stick_ctrl = core.Dag(stickNam)
		offset_null.attr('message') >> stick_ctrl.attr('offset')
		
		stick_ctrl.lockHideAttrLst('location')

		# ------------------------------------------------------------------
		# Soft IK
		# ------------------------------------------------------------------
		if softIk:
			softIkfunc.softIK(
				nameSpace=nameSpace, 
				priorMeta=priorMeta, 
				region=region, 
				side=side, 
				ctrlName=softIk_name[0],
				upAxis=softIkUpAxis, 
				primaryAxis=softIkPrimaryAxis, 
				ikhName=ikhAll_name[0], 
				inputMax=40, 
				outputMax=4, 
				debug=False
			)

		logger.info(f'#### End of {region}{side} Rig ####')
		return stickNam, hand_bJnt

	else:
		mc.error("This version requires creTwistJnt=True (Twist Rig is mandatory for this setup).")