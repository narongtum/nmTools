import maya.cmds as mc
import maya.mel as mel
import logging

from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.autoRig.base import core
from function.rigging.autoRig.base import rigTools
from function.rigging.util import misc
from function.rigging.autoRig.bodyRig import ribbonRig
from function.rigging.autoRig.bodyRig import midLockModule
from function.rigging.autoRig.bodyRig import createIKStretch as create
from function.rigging.tools import proc as pc
from function.rigging.util import generic_maya_dict as mnd
from function.pipeline import logger as pipeLogger

# Reload modules
reload(core)
reload(rigTools)
reload(misc)
reload(ribbonRig)
reload(midLockModule)
reload(create)
reload(pc)
reload(mnd)
reload(pipeLogger)

# Logger Setup
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)

class QuadrupedLogger(pipeLogger.MayaLogger):
    LOGGER_NAME = "quadruped_v2"

color_part_dict = mnd.COLOR_part_dict

def get_joint_names(tmpJnt):
    """Parses raw names from temp joints."""
    raw_names = {}
    indices = {
        'upLeg': 0, 'midLeg': 1, 'ankle': 2, 'pov': 3,
        'ball': 4, 'toe': 5, 'heel': 6, 'footIn': 7,
        'footOut': 8, 'lowLeg': 9
    }
    
    def clean_name(jnt_name):
        return jnt_name.split('_')[0][:-3]

    for key, idx in indices.items():
        if idx < len(tmpJnt):
            raw_names[key] = clean_name(tmpJnt[idx])
        else:
            raw_names[key] = f"joint_{idx}"
            
    return raw_names, indices

def quradrupedLegRig(
        nameSpace='',
        parentTo='ctrl_grp',
        side='LFT',
        tmpJnt=(
            'upLegBackLFT_tmpJnt', 'midLegBackLFT_tmpJnt', 'ankleBackLFT_tmpJnt',
            'legPovBackLFT_tmpJnt', 'ballRollBackLFT_tmpJnt', 'toeRollBackLFT_tmpJnt',
            'heelRollBackLFT_tmpJnt', 'footOutBackLFT_tmpJnt', 'footInBackLFT_tmpJnt', 
            'lowLegBackLFT_tmpJnt'
        ),
        priorJnt='hip_bJnt',
        ikhGrp='ikh_grp',
        noTouchGrp='noTouch_grp',
        nullGrp='snapNull_grp',
        showInfo=False,
        ribbon=True,
        ribbonRes='low',
        ribbonName=('upLeg', 'lwrLeg'),
        charScale=1,
        region='backLeg',
        alongAxis='y',
        povShape='sphereAxis',
        use_heel2=False # Option to enable advanced "heel2" logic
    ):

    core.makeHeader(f'Start of eh_quradrupedLegRig02 {side} Rig')
    QuadrupedLogger.info(f"Building Advanced Quadruped Leg Rig (Rear Paw Logic) for side: {side}")

    # Determine Color
    colorSide = color_part_dict['left'] if side == 'LFT' else color_part_dict['right']

    # Unpack Joint Names
    names, idx = get_joint_names(tmpJnt)
    
    # Initialize Core Dags
    joints = {
        'up': core.Dag(tmpJnt[idx['upLeg']]),
        'mid': core.Dag(tmpJnt[idx['midLeg']]),
        'low': core.Dag(tmpJnt[idx['lowLeg']]),
        'ankle': core.Dag(tmpJnt[idx['ankle']]),
        'pov': core.Dag(tmpJnt[idx['pov']]),
        'ball': core.Dag(tmpJnt[idx['ball']]),
        'toe': core.Dag(tmpJnt[idx['toe']]),
        'heel': core.Dag(tmpJnt[idx['heel']]),
        'footIn': core.Dag(tmpJnt[idx['footIn']]),
        'footOut': core.Dag(tmpJnt[idx['footOut']])
    }

    # --- 1. Create Bind Joints (Shared logic) ---
    bJnts = {}
    for key in ['up', 'mid', 'low', 'ankle', 'ball', 'toe']:
        bJnts[key] = rigTools.jointAt(joints[key])
        name_key_map = {'up': 'upLeg', 'mid': 'midLeg', 'low': 'lowLeg', 'ankle': 'ankle', 'ball': 'ball', 'toe': 'toe'}
        bJnts[key].name = f"{names[name_key_map[key]]}{side}_bJnt"
        bJnts[key].rotateOrder = 'yzx'

    # Determine Leg Type
    if 'Front' in tmpJnt[0]:
        legType = 'frontLeg'
        position = 'Front'
    elif 'Back' in tmpJnt[0]:
        legType = 'backLeg'
        position = 'Back'
    else:
        legType = 'leg'
        position = ''

    # Parent Bind Joints
    bJnts['mid'].parent(bJnts['up'])
    bJnts['low'].parent(bJnts['mid'])
    bJnts['ankle'].parent(bJnts['low'])
    bJnts['ball'].parent(bJnts['ankle'])
    bJnts['toe'].parent(bJnts['ball'])
    
    bJnts['ankle'].attr('segmentScaleCompensate').value = 0
    bJnts['up'].parent(priorJnt)

    # --- 2. Main Groups ---
    part = f"{nameSpace}{legType}"
    legRig_grp = core.Null(f"{part}Rig{side}_grp")
    core.parentConstraint(priorJnt, legRig_grp, name=f"{part}Rig{side}_parCons")
    jnt_grp = core.Null(f"{part}Jnt{side}_grp")
    jnt_grp.parent('jnt_grp')

    # --- 3. Stick Controller ---
    stick_ctrl = core.Dag(f"{part}Stick{side}_ctrl")
    stick_ctrl.nmCreateController('stick_ctrlShape')
    stick_ctrl.editCtrlShape(axis=charScale * 3.6)
    stick_ctrl.color = 'yellow'
    stick_ctrl.hideArnoldNode()
    stick_ctrl.attr('rotateX').value -= 90

    stickZro_grp = rigTools.zeroGroup(stick_ctrl)
    stickZro_grp.name = f"{part}Stick{side}Zro_grp"
    stickZro_grp.matchPosition(bJnts['ankle'])
    
    core.parentConstraint(bJnts['ankle'], stickZro_grp, mo=True, name=f"{part}{side}Stick_parCons")
    stick_ctrl.addAttribute(longName='legScale', defaultValue=1, keyable=True)
    stick_ctrl.lockHideAttrLst('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v')

    # --- 4. FK Rig ---
    fkCtrl_grp, fkJnt_grp, fkJnts, fkCtrls = create_fk_rig(
        nameSpace, legType, side, priorJnt, legRig_grp, jnt_grp, joints, names, charScale, colorSide
    )

    # --- 5. Advanced IK Rig (Rear Paw Logic) ---
    ik_results = create_advanced_ik_rig(
        nameSpace, legType, side, priorJnt, legRig_grp, jnt_grp, joints, names, 
        charScale, colorSide, noTouchGrp, region, bJnts, stick_ctrl, use_heel2
    )

    # Unpack common IK results for connections
    ikJnts = ik_results['ikJnts']
    
    # --- 6. FK/IK Switch ---
    connect_fk_ik_switch(
        nameSpace, side, position, stick_ctrl, fkJnts, ikJnts, bJnts, names
    )
    
    # Setup Visibility
    setup_visibility(
        part, side, stick_ctrl, fkCtrl_grp, ik_results['lowerLegIkZro_grp'], ik_results['ikRootZro_grp']
    )

    # --- 7. Foot Roll ---
    foot_results = create_foot_roll(
        nameSpace, legType, side, charScale, colorSide, 
        bJnts, ikJnts, ik_results['ankleIk_ctrl'], ik_results['ankleIkGmbl_ctrl'], 
        ik_results['lowerLegIK_ctrl'], joints, names
    )
    
    # Fix Parenting for IK Handles
    # Parent the main spring IK handle to the foot roll's rollback control
    ik_results['lowerIk_ikh'].parent(foot_results['rollBack_ctrl'])

    # --- 8. Mid Lock (Elbow/Knee) ---
    # Note: Mid lock typically connects to the middle joint.
    # In rear paw logic, the visual "knee" is separate from the functional "ankle".
    # We apply mid lock to the main IK chain for stability.
    create_mid_lock(
        nameSpace, side, region, alongAxis, 
        ik_results['ikRootGmbl_ctrl'].name, ik_results['pov_ctrl'].name, ik_results['lowerLegIK_ctrl'].name, 
        ik_results['pmaNode'], ikJnts
    )

    # --- 9. Ribbon Rig ---
    if ribbon:
        create_ribbon(
             nameSpace, side, ribbonRes, ribbonName, charScale, 
             noTouchGrp, showInfo, legRig_grp, legType, bJnts
        )

    # Cleanup
    jnt_grp.attr('visibility').value = showInfo
    legRig_grp.parent(parentTo)
    stickZro_grp.parent(parentTo)
    ik_results['ikRootZro_grp'].parent(ik_results['armIkCtrl_grp'])
    ik_results['lowerLegIkZro_grp'].parent(parentTo)

    QuadrupedLogger.info(f" End of {part} {side} Rig ")


def create_advanced_ik_rig(nameSpace, legType, side, priorJnt, legRig_grp, jnt_grp, joints, names, charScale, colorSide, noTouchGrp, region, bJnts, stick_ctrl, use_heel2):
    """
    Implements the 3-chain IK logic from Blender's rear_paw.py adapted for Maya.
    
    structure:
    - Main Chain (IK): Driven by IK Handles.
    - IK2 (Thigh Driver): Pre-drives the thigh/knee. Has its own solver.
    - IK3 (Heel Driver): Pre-drives the hock/heel.
    """
    ctrlType = 'Ik'
    part = f"{nameSpace}{legType}"
    
    # Groups
    armIkCtrl_grp = core.Null(f"{part}{ctrlType}Ctrl{side}_grp")
    armIkCtrl_grp.snap(priorJnt)
    armIkCtrl_grp.parent(legRig_grp)

    armIkJnt_grp = core.Null(f"{part}{ctrlType}Jnt{side}_grp")
    armIkJnt_grp.snap(priorJnt)
    armIkJnt_grp.parent(jnt_grp)
    
    # --- 1. Main IK Joints ---
    ikJnts = {}
    for key in ['up', 'mid', 'low', 'ankle', 'ball', 'toe']:
        ikJnts[key] = rigTools.jointAt(joints[key])
        name_key_map = {'up': 'upLeg', 'mid': 'midLeg', 'low': 'lowLeg', 'ankle': 'ankle', 'ball': 'ball', 'toe': 'toe'}
        ikJnts[key].name = f"{names[name_key_map[key]]}{side}_ikJnt"
    
    ikJnts['mid'].parent(ikJnts['up'])
    ikJnts['low'].parent(ikJnts['mid'])
    ikJnts['ankle'].parent(ikJnts['low'])
    ikJnts['ball'].parent(ikJnts['ankle'])
    ikJnts['toe'].parent(ikJnts['ball'])
    ikJnts['up'].parent(armIkJnt_grp)

    # --- 2. Main IK Handle (Spring) ---
    # Drives from Up -> Low (ignoring ankle for now in spring solver if standard)
    # But for Quadruped, we often want Up -> Mid -> Low -> Ankle flow.
    # Standard spring solver usually takes start and end.
    try:
        lowerIk_ikh = core.IkSpring(startJoint=ikJnts['up'].name, endEffector=ikJnts['low'].name)
    except:
        mc.error("Please enable Maya IkSpring solver.")
    
    lowerIk_ikh.name = f"{names['lowLeg']}{side}_ikSpring_handle"
    lowerIk_ikh.attr('v').value = 0

    # --- 3. IK2 Chain (Thigh Automation) ---
    # This chain mimics the 'mch_ik2' system in Blender
    # It solves from Up to Mid/Low to help drive the knee
    ik2_grp = core.Null(f"{part}Ik2Jnt{side}_grp")
    ik2_grp.snap(priorJnt)
    ik2_grp.parent(jnt_grp)
    
    ik2Jnts = []
    # Create 2 joints logic for IK2 (Thigh -> Knee)
    # Blender: make_ik2_mch_chain (from org 0 to 1)
    for j_src in [joints['up'], joints['mid'], joints['low']]:
        j = rigTools.jointAt(j_src)
        j.name = j_src.name.replace('_tmpJnt', f'{side}_ik2Jnt')
        ik2Jnts.append(j)
    
    ik2Jnts[1].parent(ik2Jnts[0])
    ik2Jnts[2].parent(ik2Jnts[1])
    ik2Jnts[0].parent(ik2_grp)

    # IK2 Handle (RP Solver)
    ik2_ikh = core.IkRp(startJoint=ik2Jnts[0].name, endEffector=ik2Jnts[2].name)
    ik2_ikh.name = f"{part}Ik2{side}_ikh"
    ik2_ikh.attr('v').value = 0
    
    # IK2 Target (Driven by Ankle/Heel Controller)
    # In Blender: ik2_target is driven by 'heel2' or 'toe_socket'
    # We will drive this by the main ankle controller later.
    
    # --- 4. IK3 Chain (Heel Automation) ---
    # This chain mimics 'mch_ik3'. It's parented to IK2 and drives the ankle.
    ik3_grp = core.Null(f"{part}Ik3Jnt{side}_grp")
    ik3_grp.parent(jnt_grp) # Temp, will parent to IK2
    
    # Map to Mid -> Ankle part
    ik3Jnts = []
    # Blender: ik3 chain uses org[1:3] (Mid to Ankle)
    for j_src in [joints['mid'], joints['low'], joints['ankle']]:
        j = rigTools.jointAt(j_src)
        j.name = j_src.name.replace('_tmpJnt', f'{side}_ik3Jnt')
        ik3Jnts.append(j)
        
    ik3Jnts[1].parent(ik3Jnts[0])
    ik3Jnts[2].parent(ik3Jnts[1])
    
    # Parent IK3 start to IK2 start of mid
    # Blender: set_bone_parent(mch.ik3_chain[0], mch.ik2_chain[0]) -> Wait, logic check
    # Actually IK3 sits on top of IK2. 
    # Let's simple constrain: ik3[0] parentConstraint to ik2[1] (the mid joint equivalent)
    core.parentConstraint(ik2Jnts[1], ik3Jnts[0], mo=True)
    
    # IK3 Handle
    ik3_ikh = core.IkRp(startJoint=ik3Jnts[0].name, endEffector=ik3Jnts[2].name)
    ik3_ikh.name = f"{part}Ik3{side}_ikh"
    ik3_ikh.attr('v').value = 0


    # --- 5. Controllers ---
    
    # Root IK
    rootName = f"{names['upLeg']}Ik{side}"
    ikRoot = core.Dag(f"{rootName}_ctrl")
    ikRoot.nmCreateController('cube_ctrlShape')
    ikRoot.editCtrlShape(axis=charScale * 5.5)
    ikRoot.setColor(colorSide)
    
    ikRootZro_grp = rigTools.zeroGroup(ikRoot)
    ikRootZro_grp.snap(bJnts['up'])
    ikRootGmbl_ctrl = core.createGimbal(ikRoot)
    
    # Parent IK2/Main Root to this
    core.parentConstraint(ikRootGmbl_ctrl, ikJnts['up'].name)
    core.parentConstraint(ikRootGmbl_ctrl, ik2Jnts[0].name)
    
    # Ankle IK
    footBehav = ['footOut','footIn','heelRoll','toeRoll','ballRoll','ankle' ,'rollBackAnkle']
    ctrlName = f"{nameSpace}{footBehav[5]}{legType}IK{side}"
    ankleIk_ctrl = core.Dag(f"{ctrlName}_ctrl")
    ankleIk_ctrl.nmCreateController('cube_ctrlShape')
    ankleIk_ctrl.rotateShape(rotate=(90, 90, 0))
    ankleIk_ctrl.editCtrlShape(axis=charScale * 10)
    ankleIk_ctrl.setColor(colorSide)
    
    ankleIkZro_grp = rigTools.zeroGroup(ankleIk_ctrl)
    ankleIkZro_grp.snapPoint(ikJnts['ankle'])
    ankleIkGmbl_ctrl = core.createGimbal(ankleIk_ctrl)

    # Lower Leg IK (Knee/Hock) - visualize main IK handle
    name = f"{nameSpace}{names['lowLeg']}"
    lowerLegIK_ctrl = core.Dag(f"{name}Ik{side}_ctrl")
    lowerLegIK_ctrl.nmCreateController('cube_ctrlShape')
    lowerLegIK_ctrl.editCtrlShape(axis=charScale * 1)
    lowerLegIK_ctrl.setColor(colorSide)
    lowerLegIK_ctrl.snapPoint(ikJnts['low'])
    lowerLegIkZro_grp = rigTools.zeroGroup(lowerLegIK_ctrl)

    # --- 6. Logic Connections (The "Rear Paw" magic) ---
    
    # Drive IK2 Handle
    # The IK2 handle target should track the Ankle Controller but allow for "heel" offset
    # Create a locator target for IK2
    ik2_target = core.Locator(f"{part}Ik2Target{side}_loc")
    ik2_target.snapPoint(ik2Jnts[2])
    ik2_target.parent(ankleIkGmbl_ctrl) # Initial parent
    
    ik2_ikh.parent(ik2_target)
    
    # Drive IK3 Handle
    # IK3 solves for the hock. Its target is also the ankle controller.
    # Blender: make_constraint(mch.ik3_chain[-1], 'IK', mch.ik2_target, chain_count=2)
    # In Maya, we just parent IK3 handle to the Ankle Ctrl
    ik3_ikh.parent(ankleIkGmbl_ctrl)
    
    # Standard Stretch (Applied to IK2 Chain - The Driver)
    # We apply stretch to IK2 because it's the main structural chain.
    # IK Jnts will follow IK2/IK3 via constraints.
    print('This maybe error')
    stretchNode = create.iKStretch(
        ikJnt=(ik2Jnts[0].name, ik2Jnts[1].name, ik2Jnts[2].name), # Apply to IK2
        ikCtrl=(ikRoot.name, ankleIk_ctrl.name),
        region=legType,
        side=side,
        scaleCtrl='placement_ctrl',
        noTouchGrp=noTouchGrp,
        lowNam=names['ankle'] # This helps internal naming in stretch func
    )
    pmaNode = stretchNode[0]
    
    # Drive Main Chain from IK2/IK3
    # The Main Chain (ikJnts) needs to follow the automation.
    # We constrain Main Mid to IK2 Mid
    core.parentConstraint(ik2Jnts[1], ikJnts['mid'], mo=True)
    # We constrain Main Low to IK3 Low (or IK2 End?) -> IK3 is cleaner for hock
    core.parentConstraint(ik3Jnts[1], ikJnts['low'], mo=True)
    
    # Orient constraint for the main ankle
    core.orientConstraint(ankleIkGmbl_ctrl, ikJnts['ankle'], mo=True)

    # --- 7. POV (Pole Vector) ---
    rawPov = names['pov']
    povZro_grp = core.Null(f"{nameSpace}knee{legType.capitalize()}{side}Zro_grp")
    pov_ctrl_name = f"{nameSpace}{rawPov}{legType.capitalize()}{side}"
    pov_ctrl = core.Dag(f"{pov_ctrl_name}_ctrl")
    pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')
    pov_ctrl.editCtrlShape(axis=charScale * 0.8)
    pov_ctrl.setColor('yellow')
    pov_ctrl.parent(povZro_grp)
    povZro_grp.snap(joints['pov'])

    # PV Constraints
    mc.poleVectorConstraint(pov_ctrl.name, lowerIk_ikh.name) # Main
    mc.poleVectorConstraint(pov_ctrl.name, ik2_ikh.name) # IK2
    mc.poleVectorConstraint(pov_ctrl.name, ik3_ikh.name) # IK3
    
    povZro_grp.parent(lowerLegIK_ctrl) # Following the knee control visual
    
    # Local/World POV setup
    partName = f"{nameSpace}knee"
    rigTools.parentLocalWorldCtrl(pov_ctrl, ankleIk_ctrl, 'ctrl_grp', povZro_grp, partName)

    # --- 8. Attributes & Stretch ---
    # Add attributes
    attr_list = [('toe_Aim', 'float', 0, 1), ('autoStretch', 'long', 0, 1), 
                 ('upStretch', 'float', None, None), ('lowStretch', 'float', None, None), 
                 ('Upper_IK', 'long', 0, 1)]
    for attr, typ, mn, mx in attr_list:
        # Use mc.addAttr directly to ensure it works
        if mc.attributeQuery(attr, node=ankleIk_ctrl.name, exists=True):
            continue
            
        args = {'longName': attr, 'attributeType': typ, 'k': True, 'defaultValue': 0}
        if mn is not None: args['minValue'] = mn
        if mx is not None: args['maxValue'] = mx
        
        mc.addAttr(ankleIk_ctrl.name, **args)
    
    ankleIk_ctrl.hideArnoldNode()
    
    # FK/IK Switch Attr
    stick_ctrl.addAttribute(attributeType='float', longName='FK_IK', minValue=0, maxValue=1, defaultValue=0, keyable=True)

    # Lock & Hide
    ikRoot.lockHideAttrLst('rx', 'ry', 'rz', 'sx', 'sy', 'sz')
    pov_ctrl.lockHideAttrLst('rx', 'ry', 'rz', 'sx', 'sy', 'sz')
    mc.connectAttr(f'{ankleIk_ctrl.name}.Upper_IK', f'{lowerLegIK_ctrl.shape}.visibility', f=True)

    return {
        'ikRoot': ikRoot, 'ikRootGmbl_ctrl': ikRootGmbl_ctrl, 'ikRootZro_grp': ikRootZro_grp,
        'ankleIk_ctrl': ankleIk_ctrl, 'ankleIkGmbl_ctrl': ankleIkGmbl_ctrl, 
        'lowerLegIK_ctrl': lowerLegIK_ctrl, 'lowerLegIkZro_grp': lowerLegIkZro_grp,
        'pov_ctrl': pov_ctrl, 'ikJnts': ikJnts, 'lowerIk_ikh': lowerIk_ikh,
        'armIkCtrl_grp': armIkCtrl_grp, 'pmaNode': pmaNode
    }


# ... Rest of helper functions (create_fk_rig, connect_fk_ik_switch, etc.) remain mostly same as version 1
# ... but included here for completeness of file

def create_fk_rig(nameSpace, legType, side, priorJnt, legRig_grp, jnt_grp, joints, names, charScale, colorSide):
    part = f"{nameSpace}{legType}"
    fkCtrl_grp = core.Null(f"{part}FkCtrl{side}_grp")
    fkCtrl_grp.snap(priorJnt)
    fkCtrl_grp.parent(legRig_grp)

    fkJnt_grp = core.Null(f"{part}FkJnt{side}_grp")
    fkJnt_grp.snap(priorJnt)
    fkJnt_grp.parent(jnt_grp)

    # Create FK Joints
    fkJnts = {}
    for key in ['up', 'mid', 'low', 'ankle', 'ball']:
        fkJnts[key] = rigTools.jointAt(joints[key])
        name_key_map = {'up': 'upLeg', 'mid': 'midLeg', 'low': 'lowLeg', 'ankle': 'ankle', 'ball': 'ball'}
        fkJnts[key].name = f"{names[name_key_map[key]]}{side}_fkJnt"
    
    # Hierarchy
    fkJnts['mid'].parent(fkJnts['up'])
    fkJnts['low'].parent(fkJnts['mid'])
    fkJnts['ankle'].parent(fkJnts['low'])
    fkJnts['ball'].parent(fkJnts['ankle'])
    fkJnts['up'].parent(fkJnt_grp)

    # Rotate Orders
    fkJnts['up'].rotateOrder = 'xyz'
    fkJnts['low'].rotateOrder = 'yzx'
    fkJnts['ankle'].rotateOrder = 'xzy'
    fkJnts['ball'].rotateOrder = 'yzx'

    # Create Controllers
    ctrl_shape = f"lowerLeg{side}_FK_ctrlShape"
    fkCtrls = {}
    
    def make_fk_ctrl(key, axis_scale, rot_order, target_jnt):
        ctrl_name = f"{nameSpace}{key}{legType.capitalize()}{side}_Fk_ctrl"
        if key == 'upper': ctrl_name = f"{nameSpace}upper{legType.capitalize()}Fk{side}_ctrl"
        if key == 'mid': ctrl_name = f"{nameSpace}mid{legType.capitalize()}Fk{side}_ctrl"
        if key == 'lower': ctrl_name = f"{nameSpace}lower{legType.capitalize()}Fk{side}_ctrl"
        if key == 'ankle': ctrl_name = f"{nameSpace}ankle{legType.capitalize()}Fk{side}_ctrl"
        if key == 'ball': ctrl_name = f"{nameSpace}ball{legType.capitalize()}Fk{side}_ctrl"

        ctrl = core.Dag(ctrl_name)
        ctrl.nmCreateController(ctrl_shape)
        zro = rigTools.zeroGroup(ctrl)
        zro.name = f"{ctrl_name.replace('_ctrl', '')}Zro_grp"
        ctrl.editCtrlShape(axis=charScale * axis_scale)
        gmbl = core.createGimbal(ctrl)
        ctrl.color = colorSide
        ctrl.rotateOrder = rot_order
        gmbl.rotateOrder = rot_order
        
        zro.matchPosition(target_jnt)
        zro.matchRotation(target_jnt)
        
        core.parentConstraint(gmbl, target_jnt, name=f"{ctrl_name.replace('_ctrl', '')}_parCons")
        return ctrl, zro, gmbl

    fkCtrls['up'], upZro, upGmbl = make_fk_ctrl('upper', 0.9, 'xyz', fkJnts['up'])
    fkCtrls['mid'], midZro, midGmbl = make_fk_ctrl('mid', 0.8, 'yzx', fkJnts['mid'])
    fkCtrls['low'], lowZro, lowGmbl = make_fk_ctrl('lower', 0.8, 'yzx', fkJnts['low'])
    fkCtrls['ankle'], ankZro, ankGmbl = make_fk_ctrl('ankle', 0.7, 'xzy', fkJnts['ankle'])
    fkCtrls['ball'], ballZro, ballGmbl = make_fk_ctrl('ball', 0.7, 'xzy', fkJnts['ball'])

    ballZro.parent(ankGmbl)
    ankZro.parent(lowGmbl)
    lowZro.parent(midGmbl)
    midZro.parent(upGmbl)
    upZro.parent(fkCtrl_grp)

    return fkCtrl_grp, fkJnt_grp, fkJnts, fkCtrls

def connect_fk_ik_switch(nameSpace, side, position, stick_ctrl, fkJnts, ikJnts, bJnts, names):
    placementCtrl = stick_ctrl.name
    targets = [
        ('up', f"upLeg{position}"),
        ('low', f"lowLeg{position}"),
        ('mid', f"midLeg{position}"),
        ('ankle', f"ankle{position}"),
        ('ball', f"ballRoll{position}")
    ]
    for key, prefix in targets:
        fk = fkJnts[key].name
        ik = ikJnts[key].name
        bind = bJnts[key].name
        psCon = mc.parentConstraint(fk, ik, bind, name=f"{prefix}Switch_parentCons", mo=True)
        revNode = mc.createNode('reverse', name=f"{prefix}Switch{side}_rev")
        mc.connectAttr(f'{placementCtrl}.FK_IK', f'{revNode}.inputX')
        mc.connectAttr(f'{placementCtrl}.FK_IK', f'{psCon[0]}.{ik}W1')
        mc.connectAttr(f'{revNode}.outputX', f'{psCon[0]}.{fk}W0')

def setup_visibility(part, side, stick_ctrl, fk_grp, low_ik_grp, root_ik_grp):
    stickVis_rev = core.Reverse()
    stickVis_rev.name = f"{part}StickVis{side}_rev"
    stick_ctrl.attr('FK_IK') >> stickVis_rev.attr('inputX')
    stickVis_rev.attr('outputX') >> fk_grp.attr('visibility')
    stick_ctrl.attr('FK_IK').value = 1
    stick_ctrl.attr('FK_IK') >> low_ik_grp.attr('visibility')
    stick_ctrl.attr('FK_IK') >> root_ik_grp.attr('visibility')

def create_foot_roll(nameSpace, legType, side, charScale, colorSide, bJnts, ikJnts, ankleIk_ctrl, ankleIkGmbl_ctrl, lowerLegIK_ctrl, joints, names):
    footBehav = ['footOut', 'footIn', 'heelRoll', 'toeRoll', 'ballRoll', 'ankle', 'rollBackAnkle']
    
    def create_foot_ctrl(behav_idx, shape):
        name = f"{nameSpace}{footBehav[behav_idx]}{legType}IK{side}"
        ctrl = core.Dag(f"{name}_ctrl")
        ctrl.nmCreateController(shape)
        ctrl.editCtrlShape(axis=charScale*1.25)
        ctrl.setColor('yellow')
        zro = rigTools.zeroGroup(ctrl)
        zro.name = f"{name}Zro_grp"
        return ctrl, zro

    ballRoll_ctrl, ballRollZro = create_foot_ctrl(4, f'ballRoll{side}_IK_ctrlShape')
    ballRollZro.snap(bJnts['ball'])
    
    footOut_ctrl, footOutZro = create_foot_ctrl(0, 'sphere_ctrlShape')
    footOutZro.snap(joints['footOut'])
    
    footIn_ctrl, footInZro = create_foot_ctrl(1, 'sphere_ctrlShape')
    footInZro.snap(joints['footIn'])

    footHeel_ctrl, footHeelZro = create_foot_ctrl(2, 'sphere_ctrlShape')
    footHeelZro.snap(joints['heel'])
    
    footToe_ctrl, footToeZro = create_foot_ctrl(3, 'sphere_ctrlShape')
    footToeZro.snap(bJnts['toe'])

    ballRollZro.parent(footToe_ctrl)
    
    # Hierarchy
    ankleIkZro_grp = ankleIk_ctrl.getParent()
    ankleIkZro_grp.parent(lowerLegIK_ctrl) # Parent Ankle under Knee (Standard hierarchy)
    
    footOutZro.parent(ankleIkGmbl_ctrl) # Changed to Gmbl for clean offset
    footInZro.parent(footOut_ctrl)
    footHeelZro.parent(footIn_ctrl)
    footToeZro.parent(footHeel_ctrl)

    # Rollback Ankle Mechanism
    rollCtrlName = f"{nameSpace}{footBehav[6]}{legType}IK{side}"
    rollBack_ctrl = core.Dag(f"{rollCtrlName}_ctrl")
    rollBackZro = core.Null(f"{rollCtrlName}AimZro_grp")
    rollBackOffset = core.Null(f"{rollCtrlName}AimOffset_grp")
    rollBack_ctrl.nmCreateController('orientAxisC_ctrlShape')
    rollBack_ctrl.editCtrlShape(axis=charScale*0.75)
    rollBack_ctrl.setColor(colorSide)
    
    rollBackOffset.parent(rollBackZro)
    rollBack_ctrl.parent(rollBackOffset)
    rollBackZro.snap(ikJnts['ankle'])
    rollBackZro.parent(ballRoll_ctrl)

    # Additional Foot IK Handles
    ankleIk_ikh = core.IkRp(startJoint=ikJnts['low'].name, endEffector=ikJnts['ankle'].name)
    ankleIk_ikh.name = f"{nameSpace}{footBehav[5]}{legType}{side}_ikh"
    ankleIk_ikh.attr('v').value = 0
    
    ballIk_ikh = core.IkRp(startJoint=ikJnts['ankle'].name, endEffector=ikJnts['ball'].name)
    ballIk_ikh.name = f"{nameSpace}{footBehav[4]}{legType}{side}_ikh"
    ballIk_ikh.attr('v').value = 0

    toeIk_ikh = core.IkRp(startJoint=ikJnts['ball'].name, endEffector=ikJnts['toe'].name)
    toeIk_ikh.name = f"{nameSpace}{footBehav[3]}{legType}{side}_ikh"
    toeIk_ikh.attr('v').value = 0

    # Parenting
    ankleIk_ikh.parent(rollBack_ctrl)
    ballIk_ikh.parent(ballRoll_ctrl)
    toeIk_ikh.parent(footToe_ctrl)

    # Rollback Aim constraint setup
    rollBackStill = core.Null(f"{rollCtrlName}Still_grp")
    rollBackStill.maSnap(bJnts['up'])
    rollBackStill.parent(ankleIk_ctrl)

    up_obj = core.Locator(f"{rollCtrlName}_loc")
    up_obj.maSnap(rollBackOffset)
    mc.move(0, 0, charScale*30, up_obj.name, r=True, os=True, wd=True)
    
    aimCons = core.aimConstraint(ikJnts['up'], rollBackStill, rollBackOffset, mo=True, 
                                 aimVector=(0, -1, 0), upVector=(0, 0, 1), 
                                 worldUpType='object', worldUpObject=up_obj.name)
    
    toeAnim_rev = core.Reverse()
    toeAnim_rev.name = f"{rollCtrlName}_rev"
    ankleIk_ctrl.attr('toe_Aim') >> toeAnim_rev.attr('inputY')
    ankleIk_ctrl.attr('toe_Aim') >> aimCons.attr(f"{rollBackStill.name}W1")
    toeAnim_rev.attr('outputY') >> aimCons.attr(f"{ikJnts['up'].name}W0")

    up_obj.parent(ankleIk_ctrl)
    up_obj.attr('v').value = 0

    return {'ankleIk_ikh': ankleIk_ikh, 'rollBack_ctrl': rollBack_ctrl}

def create_mid_lock(nameSpace, side, region, alongAxis, start_ctrl, mid_ctrl, end_ctrl, pmaNode, ikJnts):
    rawNameUPR, distUPR, povUPR, lowUPR, upUPR = midLockModule.createDistance(
        nameSpace, part='up', startP=start_ctrl, endP=mid_ctrl
    )
    rawNameLWR, distLWR, povLWR, lowLWR, upLWR = midLockModule.createDistance(
        nameSpace, part='dn', startP=mid_ctrl, endP=end_ctrl
    )
    blendName, invertNode = midLockModule.createBlendColor(
        nameSpace, uprDistance=distUPR, lwrDistance=distLWR, side=side, uprNam=rawNameUPR
    )
    attrName = midLockModule.doAddAttr(povUPR, region)
    midLockModule.connectIkJnt(
        stretchNode=pmaNode, upperIKJnt=ikJnts['mid'].name, lowerIKJnt=ikJnts['low'].name,
        blendName=blendName, namLock=attrName, povName=povUPR, alongAxis=alongAxis
    )

def create_ribbon(nameSpace, side, ribbonRes, ribbonName, charScale, noTouchGrp, showInfo, legRig_grp, legType, bJnts):
    numJoints = 5 if ribbonRes == 'high' else 3
    hingesUpr = ribbonRig.ribbonRig(
        nameSpace=nameSpace, width=10, numJoints=numJoints, side=side,
        jointTop=bJnts['up'], jointBtm=bJnts['mid'], part=ribbonName[0],
        charScale=charScale, noTouch_grp=noTouchGrp, showInfo=showInfo, ctrl_grp=legRig_grp.name
    )
    hingesLwr = ribbonRig.ribbonRig(
        nameSpace=nameSpace, width=10, numJoints=numJoints, side=side,
        jointTop=bJnts['mid'], jointBtm=bJnts['low'], part=ribbonName[1],
        charScale=charScale, noTouch_grp=noTouchGrp, showInfo=showInfo, ctrl_grp=legRig_grp.name
    )
    ribbonRig.makeHigesMover(
        part=legType, nameSpace=nameSpace, side=side,
        btmName=hingesUpr, topName=hingesLwr, charScale=charScale,
        moverPosition=bJnts['mid'].name, ctrl_grp='ctrl_grp'
    )
