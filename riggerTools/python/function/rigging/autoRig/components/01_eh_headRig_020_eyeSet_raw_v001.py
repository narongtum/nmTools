

nameSpace=nameSpace
side='RGT'
eyeJnt = eyeRGT
headJnt =head01_bJnt.name
charScale = charScale
parentTo=headGmbl_ctrl.name
eyeCenCtrl =eyeCen_ctrl.name
eyeTarget=eyeTargetRGT

"""
Internal helper to create Eye Rig.
Logic follows headRig.py _eyeCtrl strictly.
"""
# naming logic from original
part = nameSpace + 'eye' + side

# 1. Create Bind Joint
# eyeSide_bJnt = rigTools.jointAt( eyeJntNam )
eyeSide_bJnt = rigTools.jointAt(eyeJnt)
eyeSide_bJnt.name = part + '_bJnt'
eyeSide_bJnt.parent(headJnt)
eyeSide_bJnt.freeze() # Add freeze transform to get rid orientation

# 2. Create Controller (Manual Step to match hierarchy: Zro -> Aim -> Ctrl)
eyeSide_ctrl = core.Dag(part + '_ctrl')
eyeSide_ctrl.nmCreateController('sphere_ctrlShape')
eyeSide_ctrl.editCtrlShape(axis=charScale * 1.01)
eyeSide_ctrl.color = 'softBlue'
eyeSide_ctrl.rotateOrder = 'zxy'

# Create Aim Group (Legacy logic: zeroGroup(ctrl) -> name it Aim)
eyeAimSide_grp = eh_adjust.createZeroGroup(eyeSide_ctrl)
eyeAimSide_grp.name = part + 'Aim_grp'

# Create Zero Group (Legacy logic: zeroGroup(aim) -> name it Zro)
eyeSideZro_grp = eh_adjust.createZeroGroup(eyeAimSide_grp)
eyeSideZro_grp.name = part + 'Zro_grp'

# Gimbal
eyeSideGmbl_ctrl = core.createGimbal(eyeSide_ctrl)
eyeSideGmbl_ctrl.rotateOrder = 'zxy'

# Positioning
eyeSideZro_grp.matchPosition(eyeSide_bJnt)
#eyeSideZro_grp.matchRotation(eyeSide_bJnt) #... match only position because of RGT side will make alway flip

# 3. Create Eye Target
# targetPart = nameSpace + 'eyeTarget' + side

mc.parent(eyeSideZro_grp.name, parentTo)



# Use eh_adjust for standard controller creation here
# Target hierarchy: Zro -> Ctrl -> Gimbal (Standard)
target_zro, target_ctrl, target_gmbl = eh_adjust.create(
	nameSpace=None,
	name=eyeTarget,
	ctrlShape='sphere_ctrlShape',
	rotateOrder='zxy',
	charScale=charScale * 0.8,
	color='softBlue',
	constraint=False,
	parentTo=eyeCenCtrl, # Move zro grp under eyeCenter grp
	rotation=(0,0,0),
	matrixConstraint=False
)

# Snap to Target Temp
# target_zro.maSnap(eyeTarget) #.. no need to snap

# 4. Aim Constraint (Matrix Optimized)
# Original: aimVector = (0,0,1) , upVector = (0,1,0) , worldUpType = "objectrotation", worldUpObject = headJnt
mtc.aimConstraintMatrix(
	source=target_ctrl.name,
	target=eyeAimSide_grp.name,
	aimVector=(0, 0, 1),
	upVector=(0, 1, 0),
	worldUpObject='', # Object Rotation mode
	maintainOffset=True
)





# 5. Joint Constraint (Matrix Optimized)
# Original: parentConstraint( eyeSideGmbl_ctrl , eyeSide_bJnt , mo = True)
mtc.parentConMatrixGPT(
	source=eyeSideGmbl_ctrl.name,
	target=eyeSide_bJnt.name,
	mo=False,
	translate=True, rotate=True, scale=True
)

# Final Parent
#eyeSideZro_grp.parent(parentTo)

# Lock attributes
for attr in ('rx','ry','rz','sx','sy','sz','v'):
	target_ctrl.attr(attr).lockHide()

#return eyeSide_bJnt