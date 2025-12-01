import maya.cmds as mc
from function.rigging.autoRig.base import core
from function.rigging.autoRig.base import rigTools
from function.rigging.util import misc
from function.rigging.util import generic_maya_dict as mnd

# --- 1. Import Modules (Updated) ---
# เรียกใช้ Module ที่เรา Refactor ไปแล้ว
from function.rigging.controllerBox import eh_controller as eh_adjust
from function.rigging.constraint import matrixConstraint as mtc
# (สมมติว่าคุณเซฟไฟล์ย่อยๆ เป็นชื่อ eh_ แล้ว ถ้ายังให้แก้ชื่อ import ตรงนี้ครับ)
from function.rigging.autoRig.components.limbRig import eh_twistRig as tr
from function.rigging.autoRig.components.limbRig import eh_midLockModule as midLockModule
from function.rigging.autoRig.components.limbRig import eh_createIKStretch as create
# Ribbon ใช้ของเดิมไปก่อน
from function.rigging.autoRig.bodyRig import ribbonRigExt as ribbonRig 

# --- 2. Mock Scene Data ---
mc.file(new=True, f=True)

# Create Groups
parentTo = 'ctrl_grp'
ikhGrp = 'ikh_grp'
noTouchGrp = 'noTouch_grp'
nullGrp = 'snapNull_grp'
jntGrp = 'jnt_grp'

for grp in [parentTo, ikhGrp, noTouchGrp, nullGrp, jntGrp]:
    if not mc.objExists(grp):
        mc.createNode('transform', n=grp)

# Create Joints (Template)
# Position: Arm (Shoulder -> Elbow -> Hand)
tmpJnt = ('upperArmLFT_tmpJnt', 'lowerArmLFT_tmpJnt', 'handLFT_tmpJnt', 'armPovLFT_tmpJnt')
priorJnt = 'clavLFT_bJnt'

if not mc.objExists(priorJnt):
    mc.joint(n=priorJnt, p=(2, 14, 0))
    mc.select(cl=True)

positions = [(4, 14, 0), (8, 14, -1), (12, 14, 0)] # Arm with slight bend for IK
prev = None
for i, jnt in enumerate(tmpJnt[:3]):
    if not mc.objExists(jnt):
        j = mc.joint(n=jnt, p=positions[i])
        mc.joint(j, e=True, oj='xzy', sao='yup', ch=True, zso=True)
        if prev:
            mc.parent(j, prev)
        prev = j
    else:
        prev = jnt

# Create POV Temp
if not mc.objExists(tmpJnt[3]):
    mc.spaceLocator(n=tmpJnt[3])
    mc.move(8, 14, -5, tmpJnt[3]) # Behind elbow

mc.select(cl=True)

# --- 3. Define Arguments (เหมือนส่งเข้า Function) ---
nameSpace = ''
charScale = 1.0
side = 'LFT'
region = 'arm'
ribbon = True
ribbonRes = 'low'
ribbonName = ('upLeg', 'lwrLeg') # ชื่อ Ribbon อาจจะไม่ตรงบริบทแขน แต่ใส่ไว้เทส
showInfo = True
linkRotOrder = False
ctrlShape = 'cube_ctrlShape' # เปลี่ยนเป็น shape ที่มีใน library คุณ
creTwistJnt = True
stickShape = 'stick_ctrlShape'
alongAxis = 'y' # Arm usually aligns X or Y depending on joint orient. Let's assume Y for standard bone.
povPosi = 'front'
keepFkIkBoth = True

print("#### Mock Setup Complete ####")



# --- Start of Refactored Logic ---

# 1. Setup Names & Colors
colorSide = mnd.COLOR_part_dict['left'] if side == 'LFT' else mnd.COLOR_part_dict['right']
rotOrder = 'xzy'
rawName = [tmp.split('_')[0][:-3] for tmp in tmpJnt] # ['upperArm', 'lowerArm', 'hand']

# 2. Create Bind Joints
# ใช้ core.Dag และ rigTools แบบเดิม แต่จัดระเบียบใหม่
upper_bJnt = rigTools.jointAt(nameSpace + tmpJnt[0])
middle_bJnt = rigTools.jointAt(nameSpace + tmpJnt[1])
lower_bJnt = rigTools.jointAt(nameSpace + tmpJnt[2])

upper_bJnt.name = f"{nameSpace}{rawName[0]}{side}_bJnt"
middle_bJnt.name = f"{nameSpace}{rawName[1]}{side}_bJnt"
lower_bJnt.name = f"{nameSpace}{rawName[2]}{side}_bJnt"

middle_bJnt.parent(upper_bJnt)
lower_bJnt.parent(middle_bJnt)
upper_bJnt.parent(priorJnt)

# Freeze & Config (Standard)
for jnt in [upper_bJnt, middle_bJnt, lower_bJnt]:
    jnt.rotateOrder = rotOrder
    jnt.attr('segmentScaleCompensate').value = 0
    jnt.freeze()

# 3. Main Groups & Matrix Constraint
part = nameSpace + rawName[2] # hand
fkIkRig_grp = core.Null(f"{part}Rig{side}_grp")
mtc.parentConMatrixGPT(priorJnt, fkIkRig_grp.name, mo=True) # <-- Matrix Constraint

fkIkJnt_grp = core.Null(f"{part}Jnt{side}_grp")

# 4. Stick Controller (Switch)
stickName = rawName[2] + 'Stick'
# ใช้ eh_adjust.create แทน logic เดิมที่ยาวๆ
stickZro, stick_ctrl, stickGmbl = eh_adjust.create(
    nameSpace, f"{stickName}{side}", stickShape, rotOrder,
    charScale=charScale*1.8, color='yellow',
    parentTo=parentTo, constraint=False, matrixConstraint=False
)
stickZro.matchPosition(lower_bJnt)
stickZro.matchRotation(lower_bJnt)

# Orientation Fixes (Logic เดิม)
if region == 'arm':
    stick_ctrl.attr('rotateZ').value = 90 if side == 'LFT' else -90

# Matrix Constraint Stick -> Lower
mtc.parentConMatrixGPT(lower_bJnt.name, stickZro.name, mo=True)

# Add Attributes
attScaleName = f"{'hand' if region == 'arm' else region}Scale"
stick_ctrl.addAttribute(longName=attScaleName, defaultValue=1, keyable=True)
stick_ctrl.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz','v')

# 5. FK System
fkCtrl_grp = core.Null(f"{part}FkCtrl{side}_grp")
fkCtrl_grp.snap(priorJnt)
fkCtrl_grp.parent(fkIkRig_grp)

fkJnt_grp = core.Null(f"{part}FkJnt{side}_grp")
fkJnt_grp.snap(priorJnt)
fkJnt_grp.parent(fkIkJnt_grp)

# FK Joints
upper_fkJnt = rigTools.jointAt(upper_bJnt)
upper_fkJnt.name = f"{nameSpace}{rawName[0]}{side}_fkJnt"
middle_fkJnt = rigTools.jointAt(middle_bJnt)
middle_fkJnt.name = f"{nameSpace}{rawName[1]}{side}_fkJnt"
lower_fkJnt = rigTools.jointAt(lower_bJnt)
lower_fkJnt.name = f"{nameSpace}{rawName[2]}{side}_fkJnt"

middle_fkJnt.parent(upper_fkJnt)
lower_fkJnt.parent(middle_fkJnt)
upper_fkJnt.parent(fkJnt_grp)

# FK Controllers (Using eh_adjust & Matrix)
# Upper
upr_zro, upr_ctrl, upr_gmbl = eh_adjust.create(
    nameSpace, f"{rawName[0]}{side}Fk", ctrlShape, rotOrder,
    parentTo=fkCtrl_grp.name, charScale=charScale*0.9, color=colorSide,
    constraint=False 
)
upr_zro.matchAll(upper_fkJnt)
mtc.parentConMatrixGPT(upr_gmbl.name, upper_fkJnt.name, mo=True) # Drive Joint

# Middle
mid_zro, mid_ctrl, mid_gmbl = eh_adjust.create(
    nameSpace, f"{rawName[1]}{side}Fk", ctrlShape, rotOrder,
    parentTo=upr_gmbl.name, charScale=charScale*0.8, color=colorSide,
    constraint=False
)
mid_zro.matchAll(middle_fkJnt)
mtc.parentConMatrixGPT(mid_gmbl.name, middle_fkJnt.name, mo=True)

# Lower
lwr_zro, lwr_ctrl, lwr_gmbl = eh_adjust.create(
    nameSpace, f"{rawName[2]}{side}Fk", ctrlShape, rotOrder,
    parentTo=mid_gmbl.name, charScale=charScale*0.7, color=colorSide,
    constraint=False
)
lwr_zro.matchAll(lower_fkJnt)
mtc.parentConMatrixGPT(lwr_gmbl.name, lower_fkJnt.name, mo=True)

# FK Space Switch (Matrix)
mtc.eh_orientLocalWorldMatrix(
    ctrl=upr_ctrl, localObj=fkCtrl_grp, worldObj=parentTo,
    target=upr_zro, attrName='localWorld', bodyPart=f"{nameSpace}{rawName[0]}Fk{side}"
)

# 6. IK System
ikCtrl_grp = core.Null(f"{part}IkCtrl{side}_grp")
ikCtrl_grp.snap(priorJnt)
ikCtrl_grp.parent(fkIkRig_grp)

ikJnt_grp = core.Null(f"{part}IkJnt{side}_grp")
ikJnt_grp.snap(priorJnt)
ikJnt_grp.parent(fkIkJnt_grp)

# IK Joints
upper_IkJnt = rigTools.jointAt(upper_bJnt)
upper_IkJnt.name = f"{nameSpace}{rawName[0]}{side}_ikJnt"
middle_IkJnt = rigTools.jointAt(middle_bJnt)
middle_IkJnt.name = f"{nameSpace}{rawName[1]}{side}_ikJnt"
lower_IkJnt = rigTools.jointAt(lower_bJnt)
lower_IkJnt.name = f"{nameSpace}{rawName[2]}{side}_ikJnt"

middle_IkJnt.parent(upper_IkJnt)
lower_IkJnt.parent(middle_IkJnt)
upper_IkJnt.parent(ikJnt_grp)

# IK Handle
ikhName = mc.ikHandle(n=f"{part}Ik{side}_ikh", sj=upper_IkJnt.name, ee=lower_IkJnt.name, sol='ikRPsolver')
ikhNam = ikhName[0]
mc.setAttr(f"{ikhNam}.visibility", 0)

# IK Controller
ikZro_grp, lowerIk_ctrl, ikGmbl_ctrl = eh_adjust.create(
    nameSpace, f"{rawName[2]}Ik{side}", 'cube_ctrlShape', rotOrder,
    charScale=charScale*1.5, color=colorSide, parentTo=ikCtrl_grp.name,
    constraint=False
)
# Match Orientation logic
if region == 'arm':
    misc.snapParentConst(lower_IkJnt.name, ikZro_grp.name)
else:
    misc.snapPointConst(lower_IkJnt.name, ikZro_grp.name)

# Constraint Joint (Matrix Orient)
mtc.orientConstraintMatrix(ikGmbl_ctrl.name, lower_IkJnt.name, mo=True)

# IKH Grouping
ikhZro_grp = mc.group(em=True, n=f"{part}Ikh{side}Zro_grp")
misc.snapParentConst(lower_bJnt.name, ikhZro_grp)
mc.parent(ikhZro_grp, ikGmbl_ctrl.name)
mc.parent(ikhNam, ikhZro_grp)

# IK Attributes
lowerIk_ctrl.addAttribute(at='long', ln='autoStretch', k=True, min=0, max=1, dv=0)
lowerIk_ctrl.addAttribute(at='float', ln='upStretch', k=True, dv=0)
lowerIk_ctrl.addAttribute(at='float', ln='lowStretch', k=True, dv=0)

# Pole Vector
povZro_grp = mc.group(em=True, n=f"{nameSpace}{rawName[3]}{side}Zro_grp")
pov_ctrl = core.Dag(f"{nameSpace}{rawName[3]}{side}_ctrl")
pov_ctrl.nmCreateController('pyramid_ctrlShape')
pov_ctrl.rotateShape(rotate=(90, 0, 0))
pov_ctrl.editCtrlShape(axis=charScale*1.4)
pov_ctrl.setColor(colorSide)
mc.parent(pov_ctrl.name, povZro_grp)
misc.snapPointConst(tmpJnt[3], povZro_grp)

# PV Constraint (Standard is safer for PV, but can use Matrix if needed)
mc.poleVectorConstraint(pov_ctrl.name, ikhNam, w=1)
mc.parent(povZro_grp, ikGmbl_ctrl.name)

# PV Space Switch (Matrix - Parent Mode)
mtc.eh_orientLocalWorldMatrix(
    ctrl=pov_ctrl, localObj=ikGmbl_ctrl, worldObj=parentTo,
    target=povZro_grp, attrName='localWorld', parentMode='parent',
    bodyPart=f"{nameSpace}{rawName[0]}Pov{side}"
)

# IK Root Controller
ikRootZro, ikRoot_ctrl, ikRootGmbl = eh_adjust.create(
    nameSpace, f"{rawName[0]}IkRoot{side}", 'cube_ctrlShape', rotOrder,
    charScale=charScale*2.0, color='yellow', parentTo=ikCtrl_grp.name,
    constraint=False
)
ikRootZro.snap(upper_bJnt)
mtc.parentConMatrixGPT(ikRootGmbl.name, upper_IkJnt.name, mo=True)

# 7. IK Stretch (Refactored Call)
pmaNode, psStreEndName = create.iKStretch(
    ikJnt=(upper_IkJnt.name, middle_IkJnt.name, lower_IkJnt.name),
    ikCtrl=(ikRoot_ctrl.name, lowerIk_ctrl.name),
    side=side, scaleCtrl='placement_ctrl', # Assuming placement_ctrl exists or ignore
    region=region, noTouchGrp=noTouchGrp, nameSpace=nameSpace,
    lowNam=rawName[2], alongAxis=alongAxis, povPosi=povPosi
)

# 8. Blending (Matrix Mul)
stick_ctrl.addAttribute(attributeType='float', longName='FK_IK', min=0, max=1, dv=0, k=True)
if keepFkIkBoth:
    stick_ctrl.addAttribute(at='bool', ln='fkVis', dv=1, k=True)
    stick_ctrl.addAttribute(at='bool', ln='ikVis', dv=1, k=True)

buffJnt_grp = core.Null(f"{nameSpace}{region}BuffJnt{side}_grp")
buffJnt_grp.parent(fkIkJnt_grp)

# Buffer Joints Creation
buff_jnts = []
for j in [upper_bJnt, middle_bJnt, lower_bJnt]:
    bj = rigTools.jointAt(j)
    bj.name = j.name.replace('_bJnt', '_buffJnt')
    bj.setJointColor('softGray')
    buff_jnts.append(bj)

buff_jnts[1].parent(buff_jnts[0])
buff_jnts[2].parent(buff_jnts[1])
buff_jnts[0].parent(buffJnt_grp)

# Matrix Blending Loop
for i, base in enumerate(rawName[:3]):
    fk_j = f"{nameSpace}{base}{side}_fkJnt"
    ik_j = f"{nameSpace}{base}{side}_ikJnt"
    buff_j = f"{nameSpace}{base}{side}_buffJnt"
    
    # ใช้ parentMulMatrix เพื่อ blend 2 Matrix เข้า 1 เป้าหมาย
    wt_node = mtc.parentMulMatrix(src=[fk_j, ik_j], tgt=buff_j, mo=True)
    
    # Connect FK/IK Switch
    revNode = core.ReverseNam(f"{base}Switch{side}_rev")
    stick_ctrl.attr('FK_IK') >> revNode.attr('inputX')
    
    # Connect Weights (wtAddMatrix)
    # wt_node is the name of wtAddMatrix node returned by parentMulMatrix
    mc.connectAttr(revNode.name + '.outputX', wt_node + '.wtMatrix[0].weightIn', f=True) # FK
    mc.connectAttr(stick_ctrl.name + '.FK_IK', wt_node + '.wtMatrix[1].weightIn', f=True) # IK

# 9. Visibility Logic
if keepFkIkBoth:
    stick_ctrl.attr('ikVis') >> ikZro_grp.attr('visibility')
    stick_ctrl.attr('ikVis') >> ikRootZro.attr('visibility')
    stick_ctrl.attr('fkVis') >> fkCtrl_grp.attr('visibility')

# 10. Mid Lock (Elbow Lock)
rawNameUPR, distanceUPRName, povUPR_Ctrl, lowerUPR_loc, upperUPR_loc = midLockModule.createDistance(
    nameSpace, part='up', startP=ikRootGmbl.name, endP=pov_ctrl.name
)
rawNameLWR, distanceLWRName, povLWR_Ctrl, lowerLWR_loc, upperLWR_loc = midLockModule.createDistance(
    nameSpace, part='dn', startP=pov_ctrl.name, endP=ikGmbl_ctrl.name
)
blendName, invertNodeName = midLockModule.createBlendColor(
    nameSpace, uprDistance=distanceUPRName, lwrDistance=distanceLWRName, side=side, uprNam=rawNameUPR
)
attrName = midLockModule.doAddAttr(povUPR_Ctrl, region)
midLockModule.connectIkJnt(
    stretchNode=pmaNode, upperIKJnt=middle_IkJnt.name, lowerIKJnt=lower_IkJnt.name,
    blendName=blendName, namLock=attrName, povName=povUPR_Ctrl, alongAxis=alongAxis
)

# 11. Scale Connections (Hand Scale)
for axis in 'xyz':
    stick_ctrl.attr(attScaleName) >> buff_jnts[2].attr(f's{axis}')

# 12. Twist Rig (Matrix Aim)
# ใช้ eh_twistRig ที่แก้แล้ว
follow_grp, upperTwist01 = tr.twistRigAuto(
    nameSpace=nameSpace, parent_jnt=buff_jnts[0].name, child_jnt=buff_jnts[1].name,
    fk_shoulderCtrl=upr_ctrl.name, ik_shoulderCtrl=ikRoot_ctrl.name,
    side=side, region=region, priorJnt=priorJnt, stick_ctrl=stick_ctrl.name,
    charScale=charScale, showInfo=showInfo, alongAxis=alongAxis
)
mc.parent(follow_grp, noTouchGrp)

# 13. Final Drive (Buffer -> Bind)
# Twist ขับ Upper
mtc.parentConMatrixGPT(upperTwist01, upper_bJnt.name, mo=True)
# Buffer ขับ Middle & Lower
mtc.parentConMatrixGPT(buff_jnts[1].name, middle_bJnt.name, mo=True)
mtc.parentConMatrixGPT(buff_jnts[2].name, lower_bJnt.name, mo=True)

print(f"#### Gen Rig {region}{side} Matrix Refactor Completed ####")