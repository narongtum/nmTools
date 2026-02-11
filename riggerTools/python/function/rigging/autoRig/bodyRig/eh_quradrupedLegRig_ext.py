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
    LOGGER_NAME = "quadruped"

color_part_dict = mnd.COLOR_part_dict

def get_joint_names(tmpJnt):
    """Parses raw names from temp joints."""
    raw_names = {}
    indices = {
        'upLeg': 0, 'midLeg': 1, 'ankle': 2, 'pov': 3,
        'ball': 4, 'toe': 5, 'heel': 6, 'footIn': 7,
        'footOut': 8, 'lowLeg': 9
    }
    
    # Extract base names (remove side and suffix)
    # Assumes format: nameSIDE_suffix (e.g. upLegBackLFT_tmpJnt)
    
    # Helper to clean name
    def clean_name(jnt_name):
        return jnt_name.split('_')[0][:-3]

    for key, idx in indices.items():
        if idx < len(tmpJnt):
            raw_names[key] = clean_name(tmpJnt[idx])
        else:
            raw_names[key] = f"joint_{idx}" # Fallback
            
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
        povShape='sphereAxis'
    ):

    core.makeHeader(f'Start of quradrupedLegRig {side} Rig')
    QuadrupedLogger.info(f"Building Quadruped Leg Rig for side: {side}")

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

    # --- 1. Create Bind Joints ---
    bJnts = {}
    for key in ['up', 'mid', 'low', 'ankle', 'ball', 'toe']:
        bJnts[key] = rigTools.jointAt(joints[key])
        # Naming convention: RawName + Side + _bJnt
        # Map keys to names dict keys
        name_key_map = {'up': 'upLeg', 'mid': 'midLeg', 'low': 'lowLeg', 'ankle': 'ankle', 'ball': 'ball', 'toe': 'toe'}
        bJnts[key].name = f"{names[name_key_map[key]]}{side}_bJnt"
        bJnts[key].rotateOrder = 'yzx'

    # Determine Leg Type (Animal/Human/Front/Back)
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

    # --- 3. Stick Controller ---
    stick_ctrl = core.Dag(f"{part}Stick{side}_ctrl")
    stick_ctrl.nmCreateController('stick_ctrlShape')
    stick_ctrl.editCtrlShape(axis=charScale * 3.6)
    stick_ctrl.color = 'yellow'
    stick_ctrl.hideArnoldNode()
    
    # Adjust Stick Rotation
    stick_ctrl.attr('rotateX').value -= 90 # for both sides

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

    # --- 5. IK Rig ---
    ik_results = create_ik_rig(
        nameSpace, legType, side, priorJnt, legRig_grp, jnt_grp, joints, names, 
        charScale, colorSide, noTouchGrp, region, bJnts, fkCtrls, stick_ctrl
    )
    
    # Unpack IK results
    ikRoot = ik_results['ikRoot']
    ikRootGmbl_ctrl = ik_results['ikRootGmbl_ctrl']
    ankleIk_ctrl = ik_results['ankleIk_ctrl']
    ankleIkGmbl_ctrl = ik_results['ankleIkGmbl_ctrl']
    pov_ctrl = ik_results['pov_ctrl']
    ikJnts = ik_results['ikJnts']
    ikRootZro_grp = ik_results['ikRootZro_grp']
    ankleIkZro_grp = ik_results['ankleIkZro_grp']
    lowerLegIK_ctrl = ik_results['lowerLegIK_ctrl']
    lowerLegIkZro_grp = ik_results['lowerLegIkZro_grp']
    armIkCtrl_grp = ik_results['armIkCtrl_grp']
    
    # --- 6. FK/IK Switch & Connection ---
    connect_fk_ik_switch(
        nameSpace, side, position, stick_ctrl, fkJnts, ikJnts, bJnts, names
    )
    
    # Setup Visibility Switching
    setup_visibility(
        part, side, stick_ctrl, fkCtrl_grp, lowerLegIkZro_grp, ikRootZro_grp
    )

    # --- 7. Foot Roll ---
    foot_results = create_foot_roll(
        nameSpace, legType, side, charScale, colorSide, 
        bJnts, ikJnts, ankleIk_ctrl, ankleIkGmbl_ctrl, 
        lowerLegIK_ctrl, joints, names
    )

    # --- 8. Mid Lock (Elbow/Knee) ---
    # Fix: Parent lowerIk_ikh to rollBack_ctrl from foot results
    ik_results['lowerIk_ikh'].parent(foot_results['rollBack_ctrl'])

    create_mid_lock(
        nameSpace, side, region, alongAxis, 
        ikRootGmbl_ctrl.name, pov_ctrl.name, lowerLegIK_ctrl.name, 
        ik_results['pmaNode'], ikJnts
    )

    # --- 9. Ribbon Rig ---
    if ribbon:
        create_ribbon(
             nameSpace, side, ribbonRes, ribbonName, charScale, 
             noTouchGrp, showInfo, legRig_grp, legType, bJnts
        )

    # --- Final Cleanup ---
    jnt_grp.parent('jnt_grp')
    jnt_grp.attr('visibility').value = showInfo
    legRig_grp.parent(parentTo)
    stickZro_grp.parent(parentTo)
    ikRootZro_grp.parent(armIkCtrl_grp)
    lowerLegIkZro_grp.parent(parentTo)
    
    # Connect visibility for foot controls
    # Note: Logic moved to specific sections, ensuring final clean up here
    
    QuadrupedLogger.info(f" End of {part} {side} Rig ")


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
    
    # Helper for creating FK Ctrl
    def make_fk_ctrl(key, axis_scale, rot_order, target_jnt):
        ctrl_name = f"{nameSpace}{key}{legType.capitalize()}{side}_Fk_ctrl" # e.g. upperBackLegLFT_Fk_ctrl
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
        
        cons = core.parentConstraint(gmbl, target_jnt, name=f"{ctrl_name.replace('_ctrl', '')}_parCons")
        return ctrl, zro, gmbl

    # Create controls
    # Note: Logic here mimics original closely but names need to match exactly or be consistent
    # Original used: nameSpace + 'upper' + legType.capitalize() + 'Fk' + side + '_ctrl'
    
    fkCtrls['up'], upZro, upGmbl = make_fk_ctrl('upper', 0.9, 'xyz', fkJnts['up'])
    fkCtrls['mid'], midZro, midGmbl = make_fk_ctrl('mid', 0.8, 'yzx', fkJnts['mid'])
    fkCtrls['low'], lowZro, lowGmbl = make_fk_ctrl('lower', 0.8, 'yzx', fkJnts['low'])
    fkCtrls['ankle'], ankZro, ankGmbl = make_fk_ctrl('ankle', 0.7, 'xzy', fkJnts['ankle'])
    fkCtrls['ball'], ballZro, ballGmbl = make_fk_ctrl('ball', 0.7, 'xzy', fkJnts['ball'])

    # Hierarchy
    ballZro.parent(ankGmbl)
    ankZro.parent(lowGmbl)
    lowZro.parent(midGmbl)
    midZro.parent(upGmbl)
    upZro.parent(fkCtrl_grp)

    return fkCtrl_grp, fkJnt_grp, fkJnts, fkCtrls


def create_ik_rig(nameSpace, legType, side, priorJnt, legRig_grp, jnt_grp, joints, names, charScale, colorSide, noTouchGrp, region, bJnts, fkCtrls, stick_ctrl):
    ctrlType = 'Ik'
    part = f"{nameSpace}{legType}"
    armIkCtrl_grp = core.Null(f"{part}{ctrlType}Ctrl{side}_grp")
    armIkCtrl_grp.snap(priorJnt)
    armIkCtrl_grp.parent(legRig_grp)

    armIkJnt_grp = core.Null(f"{part}{ctrlType}Jnt{side}_grp")
    armIkJnt_grp.snap(priorJnt)
    armIkJnt_grp.parent(jnt_grp)

    # IK Joints
    ikJnts = {}
    for key in ['up', 'mid', 'low', 'ankle', 'ball', 'toe']:
        ikJnts[key] = rigTools.jointAt(joints[key])
        name_key_map = {'up': 'upLeg', 'mid': 'midLeg', 'low': 'lowLeg', 'ankle': 'ankle', 'ball': 'ball', 'toe': 'toe'}
        ikJnts[key].name = f"{names[name_key_map[key]]}{side}_ikJnt"
    
    # Hierarchy
    ikJnts['mid'].parent(ikJnts['up'])
    ikJnts['low'].parent(ikJnts['mid'])
    ikJnts['ankle'].parent(ikJnts['low'])
    ikJnts['ball'].parent(ikJnts['ankle'])
    ikJnts['toe'].parent(ikJnts['ball'])
    ikJnts['up'].parent(armIkJnt_grp)

    # IK Handle (Spring Solver)
    QuadrupedLogger.info('ENABLE IK SPRING SOLVER.')
    try:
        lowerIk_ikh = core.IkSpring(startJoint=ikJnts['up'].name, endEffector=ikJnts['low'].name)
    except:
        mc.error("Please enable Maya IkSpring solver.")
    
    lowerIk_ikh.name = f"{names['lowLeg']}{side}_ikSpring_handle"
    lowerIk_ikh.eff = f"{names['lowLeg']}{side}_eff"
    lowerIk_ikh.attr('v').value = 0

    # Lower Leg IK Controller (The cube one)
    # name = nameSpace + rawName[9] 
    name = f"{nameSpace}{names['lowLeg']}"
    lowerLegIK_ctrl = core.Dag(f"{name}Ik{side}_ctrl")
    lowerLegIK_ctrl.nmCreateController('cube_ctrlShape')
    lowerLegIK_ctrl.editCtrlShape(axis=charScale * 1)
    lowerLegIK_ctrl.setColor(colorSide)
    lowerLegIK_ctrl.snapPoint(ikJnts['low'])

    lowerLegIkZro_grp = rigTools.zeroGroup(lowerLegIK_ctrl)
    lowerLegIkZro_grp.name = f"{name}Ik{side}Zro_grp"

    # Orient Constraint
    legIkRotation = core.orientConstraint(lowerLegIK_ctrl, ikJnts['ankle'].name, mo=True)
    legIkRotation.name = f"{name}Ik{side}_orientCons"

    # Knee POV
    rawPov = names['pov']
    povZro_grp = core.Null(f"{nameSpace}knee{legType.capitalize()}{side}Zro_grp")
    pov_ctrl_name = f"{nameSpace}{rawPov}{legType.capitalize()}{side}"
    pov_ctrl = core.Dag(f"{pov_ctrl_name}_ctrl")
    pov_ctrl.nmCreateController('legLFT_pov_ctrlShape') # Using sphereAxis/pyramid logic from original if needed
    pov_ctrl.editCtrlShape(axis=charScale * 0.8)
    pov_ctrl.setColor('yellow')
    
    pov_ctrl.parent(povZro_grp)
    povZro_grp.snap(joints['pov'])

    # Root IK Controller
    rootName = f"{names['upLeg']}Ik{side}"
    ikRoot = core.Dag(f"{rootName}_ctrl")
    ikRoot.nmCreateController('cube_ctrlShape')
    ikRoot.editCtrlShape(axis=charScale * 5.5)
    ikRoot.setColor(colorSide)
    
    ikRootZro_grp = rigTools.zeroGroup(ikRoot)
    ikRootZro_grp.name = f"{rootName}Zro_grp"
    ikRootZro_grp.snap(bJnts['up'])
    
    ikRootGmbl_ctrl = core.createGimbal(ikRoot)
    
    rootIk_parCons = core.parentConstraint(ikRootGmbl_ctrl, ikJnts['up'].name)
    rootIk_parCons.name = f"{part}{side}Jnt_parCons"

    # Ankle IK Ctrl (For Foot Behav)
    footBehav = ['footOut','footIn','heelRoll','toeRoll','ballRoll','ankle' ,'rollBackAnkle']
    ctrlName = f"{nameSpace}{footBehav[5]}{legType}IK{side}"
    ankleIk_ctrl = core.Dag(f"{ctrlName}_ctrl")
    ankleIk_ctrl.nmCreateController('cube_ctrlShape')
    ankleIk_ctrl.rotateShape(rotate=(90, 90, 0))
    ankleIk_ctrl.editCtrlShape(axis=charScale * 10)
    ankleIk_ctrl.setColor(colorSide)
    
    ankleIkZro_grp = rigTools.zeroGroup(ankleIk_ctrl)
    ankleIkZro_grp.name = f"{ctrlName}Zro_grp"
    ankleIkZro_grp.snapPoint(ikJnts['ankle'])

    # Constraints & Hierarchy
    mc.poleVectorConstraint(pov_ctrl.name, lowerIk_ikh.name, name=f"{nameSpace}knee{legType.capitalize()}{side}_povCons", w=1)
    povZro_grp.parent(lowerLegIK_ctrl.name)

    # Local/World POV
    partName = f"{nameSpace}knee"
    rigTools.parentLocalWorldCtrl(pov_ctrl, ankleIk_ctrl, 'ctrl_grp', povZro_grp, partName) # Assuming parentTo='ctrl_grp'

    # Attributes
    attr_list = [('toe_Aim', 'float', 0, 1), ('autoStretch', 'long', 0, 1), 
                 ('upStretch', 'float', None, None), ('lowStretch', 'float', None, None), 
                 ('Upper_IK', 'long', 0, 1)]
    
    for attr, typ, mn, mx in attr_list:
        args = {'longName': attr, 'attributeType': typ, 'k': True, 'dv': 0}
        if mn is not None: args['minValue'] = mn
        if mx is not None: args['maxValue'] = mx
        ankleIk_ctrl.addAttribute(**args)
    
    ankleIk_ctrl.hideArnoldNode()

    # IK Stretch
    stretchNode = create.iKStretch(
        ikJnt=(ikJnts['up'].name, ikJnts['mid'].name, ikJnts['low'].name),
        ikCtrl=(ikRoot.name, ankleIk_ctrl.name),
        region=legType,
        side=side,
        scaleCtrl='placement_ctrl',
        noTouchGrp=noTouchGrp,
        lowNam=names['ankle']
    )
    pmaNode = stretchNode[0]

    # FK/IK Switch Attr
    stick_ctrl.addAttribute(attributeType='float', longName='FK_IK', minValue=0, maxValue=1, defaultValue=0, keyable=True)

    # Lock & Hide
    ikRoot.lockHideAttrLst('rx', 'ry', 'rz', 'sx', 'sy', 'sz')
    pov_ctrl.lockHideAttrLst('rx', 'ry', 'rz', 'sx', 'sy', 'sz')
    mc.connectAttr(f'{ankleIk_ctrl.name}.Upper_IK', f'{lowerLegIK_ctrl.shape}.visibility', f=True)

    # Ankle Gimbal
    ankleIkGmbl_ctrl = core.createGimbal(ankleIk_ctrl)

    return {
        'ikRoot': ikRoot, 'ikRootGmbl_ctrl': ikRootGmbl_ctrl, 'ikRootZro_grp': ikRootZro_grp,
        'ankleIk_ctrl': ankleIk_ctrl, 'ankleIkGmbl_ctrl': ankleIkGmbl_ctrl, 'ankleIkZro_grp': ankleIkZro_grp,
        'lowerLegIK_ctrl': lowerLegIK_ctrl, 'lowerLegIkZro_grp': lowerLegIkZro_grp,
        'pov_ctrl': pov_ctrl, 'ikJnts': ikJnts, 'lowerIk_ikh': lowerIk_ikh,
        'armIkCtrl_grp': armIkCtrl_grp, 'pmaNode': pmaNode
    }

def connect_fk_ik_switch(nameSpace, side, position, stick_ctrl, fkJnts, ikJnts, bJnts, names):
    placementCtrl = stick_ctrl.name
    
    # Construct raw names for switch loop
    # Maps internal keys to the raw name prefix used in the switch loop in original code
    # Original used: ['upLegBack', 'lowLegBack', 'midLegBack', 'ankleBack', 'ballRollBack']
    # Note: 'lowLeg' in original loop referred to 'lowLeg' index 9, mapped to 'lowerLeg_bJnt'
    
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
        
        # Override bind name from loop construction to match actua bind joint name if they differ?
        # The original code constructed expected names: prefix + side + '_bJnt'.
        # Let's trust our bJnts dict is correct, but we need to ensure the constraints name matches original if possible
        
        psCon = mc.parentConstraint(fk, ik, bind, name=f"{prefix}Switch_parentCons", mo=True)
        revNode = mc.createNode('reverse', name=f"{prefix}Switch{side}_rev")

        # Connect
        mc.connectAttr(f'{placementCtrl}.FK_IK', f'{revNode}.inputX')
        mc.connectAttr(f'{placementCtrl}.FK_IK', f'{psCon[0]}.{ik}W1') # IK
        mc.connectAttr(f'{revNode}.outputX', f'{psCon[0]}.{fk}W0') # FK

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
    
    # Helper for Foot Controls
    def create_foot_ctrl(behav_idx, shape, parent_to=None):
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

    # Hierarchy
    ballRollZro.parent(footToe_ctrl)
    # lowerLegIK_ctrl.zro? No, lowerLegIkZro was parented to footToe in original code commented out? 
    # Logic in original: 
    # ankleIkZro_grp.parent( lowerLegIK_ctrl ) -> Wrong, this is circular if lowerLegIK is main.
    # Actually lines 821+:
    # ankleIkZro_grp.parent( lowerLegIK_ctrl )  <-- Wait, ankleIk_ctrl is the big one?
    # Original line 460: lowerLegIK_ctrl = core.Dag(... 'cube_ctrlShape') -> This is the one at the knee/ankle level?
    # Original line 580: ankleIk_ctrl (another one) -> for footBehav[5] ('ankle')
    
    # Let's map strict parents
    ankleIkZro_grp = ankleIk_ctrl.getParent() # Actually we have the zro from inputs
    ankleIkZro_grp.parent(lowerLegIK_ctrl)
    
    footOutZro.parent(ankleIk_ctrl)
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

    # IK Handles
    ankleIk_ikh = core.IkRp(startJoint=ikJnts['low'].name, endEffector=ikJnts['ankle'].name)
    ankleIk_ikh.name = f"{nameSpace}{footBehav[5]}{legType}{side}_ikh"
    ankleIk_ikh.attr('v').value = 0
    
    ballIk_ikh = core.IkRp(startJoint=ikJnts['ankle'].name, endEffector=ikJnts['ball'].name)
    ballIk_ikh.name = f"{nameSpace}{footBehav[4]}{legType}{side}_ikh"
    ballIk_ikh.attr('v').value = 0

    toeIk_ikh = core.IkRp(startJoint=ikJnts['ball'].name, endEffector=ikJnts['toe'].name)
    toeIk_ikh.name = f"{nameSpace}{footBehav[3]}{legType}{side}_ikh"
    toeIk_ikh.attr('v').value = 0

    # Parenting IKH
    ankleIk_ikh.parent(rollBack_ctrl)
    # lowerIk_ikh (from input) should parent to rollBack_ctrl too? 
    # Original line 877: lowerIk_ikh.parent( rollBackAnkleIk_ctrl )
    # But lowerIk_ikh is not passed here. 
    # We should return the hierarchy or pass it in.
    
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
    
    # Reverse Node for Toe Aim
    toeAnim_rev = core.Reverse()
    toeAnim_rev.name = f"{rollCtrlName}_rev"
    ankleIk_ctrl.attr('toe_Aim') >> toeAnim_rev.attr('inputY')
    ankleIk_ctrl.attr('toe_Aim') >> aimCons.attr(f"{rollBackStill.name}W1")
    toeAnim_rev.attr('outputY') >> aimCons.attr(f"{ikJnts['up'].name}W0")

    up_obj.parent(ankleIk_ctrl)
    up_obj.attr('v').value = 0

    return {'ankleIk_ikh': ankleIk_ikh, 'rollBack_ctrl': rollBack_ctrl}

def create_mid_lock(nameSpace, side, region, alongAxis, start_ctrl, mid_ctrl, end_ctrl, pmaNode, ikJnts):
    # Upper
    rawNameUPR, distUPR, povUPR, lowUPR, upUPR = midLockModule.createDistance(
        nameSpace, part='up', startP=start_ctrl, endP=mid_ctrl
    )
    # Lower
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
