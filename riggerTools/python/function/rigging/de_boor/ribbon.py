import maya.cmds as cmds
from maya.api import OpenMaya as om
import de_boor_core as core
import importlib
importlib.reload(core)


OPEN = 'open'
PERIODIC = 'periodic'
AXIS_VECTOR = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}
KNOT_TO_FORM_INDEX = {OPEN: om.MFnNurbsCurve.kOpen, PERIODIC: om.MFnNurbsCurve.kPeriodic}


def de_boor_ribbon(cvs, aim_axis='x', up_axis='y', num_joints=10, tangent_offset=0.001, d=None, kv_type=OPEN,
                   param_from_length=True, tol=0.000001, name='ribbon', use_position=True, use_tangent=True,
                   use_up=True, use_scale=False):
    """
    Use controls and de_boor function to get position, tangent and up values for joints.  The param_from_length can
    be used to get the parameter values using a fraction of the curve length, otherwise the parameter values will be
    equally spaced

    To optimize the setup we change the nodes and connections if different combinations of position, tangent and up are
    used:
        use_position=True, use_tangent=True, use_up=True
            create 3 wtAddMatrix nodes and connect to aimMatrix

        use_position=False, use_tangent=True, use_up=True
            wtAddMatrix for tangent only created if use_position=True
            use wts and tangent_wts to set matrix values for aimMatrix
            create wtAddMatrix for up and connect to aimMatrix

        use_position=True, use_tangent=False, use_up=True
            create offset matrices in the aim direction for each joint
            use offset matrices to set the primaryTargetMatrix of aimMatrix
            create wtAddMatrix nodes for position and up and connect to aimMatrix

        use_position=True, use_tangent=True, use_up=False
            use module group matrix as the secondaryTargetMatrix of aimMatrix
            create wtAddMatrix nodes for position and tangent and connect to aimMatrix

        use_position=False, use_tangent=False, use_up=True
            same as use_position=False, use_tangent=True, use_up=True

        use_position=False, use_tangent=True, use_up=False
            translation and rotation of joints set

        use_position=True, use_tangent=False, use_up=False
            no aimMatrix needed, connect the wtAddMatrix for translation to the joints

        use_position=False, use_tangent=False, use_up=False
            translation and rotation of joints set

        aimMatrix not created when use_tangent=False and use_up=False, otherwise it is

        Examples:
        from maya import cmds
        import ribbon
        from importlib import reload
        reload(ribbon)


        # ----- example 1, open knot vector type with linear degree
        cmds.file(new=True, f=True)

        cvs = []
        for i in range(4):
            loc = cmds.spaceLocator()[0]
            cvs.append(loc)
            cmds.setAttr(f'{loc}.t', i, 0, 0)

        jnts = ribbon.de_boor_ribbon(cvs)
        for jnt in jnts:
            cmds.setAttr(f'{jnt}.displayLocalAxis', True)

        # ----- example 2, periodic knot vector type with quadratic degree
        cmds.file(new=True, f=True)

        cvs = []
        ts = ((1, 0, 1), (-1, 0, 1), (-1, 0, -1), (1, 0, -1))
        rys = (-135, 135, 45, -45)
        for t, ry in zip(ts, rys):
            loc = cmds.spaceLocator()[0]
            cvs.append(loc)
            cmds.setAttr(f'{loc}.t', *t)
            cmds.setAttr(f'{loc}.ry', ry)

        jnts = ribbon.de_boor_ribbon(cvs, kv_type='periodic', d=2, num_joints=13)
        for jnt in jnts:
            cmds.setAttr(f'{jnt}.displayLocalAxis', True)

        Args:
            cvs (list): transforms that will act as the curve cvs
            aim_axis (str): aim axis of the output joints
            up_axis (str): up axis of the output joints
            num_joints (int): number of output joints to be created
            tangent_offset (float): tolerance used to optimization
            d (int): degree of the basis functions
            kv_type (str): 'open' or 'periodic', 'periodic' will create a closed curve
            param_from_length (bool): evenly distributes joints along the curve if cvs are not evenly spaced
            tol (float): tolerance used to optimization
            name (str): prefix given to all node created
            use_position (bool): if True then create position setup else set position
            use_tangent (bool): if True (and use_position is True) then create tangent setup else set tangent
            use_up (bool): if True then create up setup else set up
            use_scale (bool): if True then create scale setup

    Returns:
        list: joints
    """

    mod_grp = cmds.createNode('transform', n=f'{name}_MOD_GRP')
    ctls_grp = cmds.createNode('transform', n=f'{name}_CTLS_GRP')
    jnts_grp = cmds.createNode('transform', n=f'{name}_JNTS_GRP')
    cmds.parent((ctls_grp, jnts_grp), mod_grp)
    cmds.matchTransform(mod_grp, cvs[0])

    ctls = []

    for i, cv in enumerate(cvs):
        ctl = cmds.createNode('transform', n=f'{name}_{i}_CTL')
        ctls.append(ctl)

        for j, axis in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
            cir = cmds.circle(nr=axis, n=f'{name}_{i}_CTL{j}')
            cir_shp = cmds.listRelatives(cir, c=True, s=True)[0]
            cmds.parent(cir_shp, ctl, s=True, r=True)
            cmds.delete(cir)

        cmds.parent(ctl, ctls_grp)
        cmds.matchTransform(ctl, cv)

    num_cvs = len(cvs)
    original_cvs = cvs[:]

    d = num_cvs - 1 if d is None else d

    if kv_type == OPEN:

        kv, _ = core.knot_vector(OPEN, cvs, d)

        m_kv = kv[1:-1]
        m_cvs = cvs[:]

    else:  # kv_type is PERIODIC

        m_cvs = [cvs[i - 1 % len(cvs)] for i in range(len(cvs))]
        for i in range(d):
            m_cvs.append(m_cvs[i])

        m_kv_len = len(m_cvs) + d - 1
        m_kv_interval = 1 / (m_kv_len - 2 * (d - 1) - 1)
        m_kv = [-m_kv_interval * (d - 1) * (1 - t / (m_kv_len - 1)) +
                (1 + m_kv_interval * (d - 1)) * t / (m_kv_len - 1) for t in range(m_kv_len)]

        kv, cvs = core.knot_vector(PERIODIC, cvs, d)

    m_cv_poss = om.MPointArray([cmds.xform(obj, q=True, ws=True, t=True) for obj in m_cvs])
    form = KNOT_TO_FORM_INDEX[kv_type]
    is_2d = False
    rational = True
    data_creator = om.MFnNurbsCurveData()
    parent = data_creator.create()

    crv_fn = om.MFnNurbsCurve()
    crv_fn.create(m_cv_poss, m_kv, d, form, is_2d, rational, parent)

    if param_from_length:

        crv_len = crv_fn.length()
        params = []

        for i in range(num_joints):

            sample_len = crv_len * i / (num_joints - 1)

            if kv_type == PERIODIC:
                t = crv_fn.findParamFromLength((sample_len + crv_len * m_kv[2] * 0.5) % crv_len)
                params.append(t - m_kv[2] * 0.5)
            else:
                t = crv_fn.findParamFromLength(sample_len)
                params.append(t)

    else:
        params = [i / (num_joints - 1) for i in range(num_joints)]

    if kv_type == PERIODIC:

        params = [(kv[d + 1] * (d * 0.5 + 0.5)) * (1 - t) + t * (1 - kv[d + 1] * (d * 0.5 - 0.5))
                  for i, t in enumerate(params)]

    par_off_plugs = []
    trans_off_plugs = []
    sca_off_plugs = []

    for i, ctl in enumerate(ctls):

        par_off = cmds.createNode('multMatrix', n=f'{name}_parentOffset_{i}_MM')
        cmds.connectAttr(f'{ctl}.worldMatrix', f'{par_off}.matrixIn[0]')
        cmds.connectAttr(f'{mod_grp}.worldInverseMatrix', f'{par_off}.matrixIn[1]')

        par_off_plugs.append(f'{par_off}.matrixSum')

        trans_off = cmds.createNode('pickMatrix', n=f'{name}_translation_{i}_PM')
        cmds.connectAttr(f'{par_off}.matrixSum', f'{trans_off}.inputMatrix')
        for attr in 'useRotate', 'useScale', 'useShear':
            cmds.setAttr(f'{trans_off}.{attr}', False)

        trans_off_plugs.append(f'{trans_off}.outputMatrix')

        if use_scale and use_tangent or use_up:

            sca_off = cmds.createNode('pickMatrix', n=f'{name}_scaleOffset_{i}_PM')
            cmds.connectAttr(f'{par_off}.matrixSum', f'{sca_off}.inputMatrix')
            for attr in 'useRotate', 'useShear', 'useTranslate':
                cmds.setAttr(f'{sca_off}.{attr}', False)

            sca_off_plugs.append(f'{sca_off}.outputMatrix')

    jnts = []

    for i, param in enumerate(params):

        # print(param)
        cmds.select(cl=True)
        jnt = cmds.joint(n=f'{name}_{i}_JNT')
        cmds.parent(jnt, jnts_grp)
        cmds.setAttr(f'{jnt}.jo', 0, 0, 0)
        cmds.xform(jnt, m=om.MMatrix.kIdentity)

        jnts.append(jnt)

        wts = core.de_boor(len(cvs), d, param, kv, tol=tol)
        if kv_type == PERIODIC:
            wts = get_consolidated_wts(wts, original_cvs, cvs)

        tangent_param = param + tangent_offset
        aim_vector = om.MVector(AXIS_VECTOR[aim_axis])
        if tangent_param > 1:
            tangent_param = param - 2 * tangent_offset
            aim_vector *= -1

        tangent_wts = core.de_boor(len(cvs), d, tangent_param, kv, tol=tol)
        if kv_type == PERIODIC:
            tangent_wts = get_consolidated_wts(tangent_wts, original_cvs, cvs)

        position_plug = None
        tangent_plug = None

        # ----- position setup
        if use_position:

            position = create_wt_add_matrix(trans_off_plugs, wts, f'{name}_position_{i}_WAM', tol=tol)
            position_plug = f'{position}.matrixSum'

            if not use_tangent and not use_up:  # no aimMatrix necessary, connect wtAddMatrix to joint

                cmds.connectAttr(position_plug, f'{jnt}.offsetParentMatrix')

                if use_scale:

                    for trans_off_plug in trans_off_plugs:

                        trans_off = trans_off_plug.split('.')[0]
                        cmds.setAttr(f'{trans_off}.useScale', True)

                continue

            # ----- tangent setup
            if use_tangent:

                tangent = create_wt_add_matrix(trans_off_plugs, tangent_wts, f'{name}_tangent_{i}_WAM', tol=tol)
                tangent_plug = f'{tangent}.matrixSum'

        up_plug = f'{mod_grp}.worldMatrix'

        # ----- up setup
        if use_up:

            temp = cmds.createNode('transform')
            cmds.parent(temp, mod_grp)
            ori_con = cmds.orientConstraint(original_cvs, temp)[0]
            cmds.setAttr(f'{ori_con}.interpType', 2)
            for j, wt in enumerate(wts):
                cmds.setAttr(f'{ori_con}.{original_cvs[j]}W{j}', wt)

            up = create_wt_add_matrix(par_off_plugs, wts, f'{name}_up_{i}_WAM', tol=tol)

            temp_mat = om.MMatrix(cmds.getAttr(f'{temp}.matrix'))
            up_inverse = om.MMatrix(cmds.getAttr(f'{up}.matrixSum')).inverse()
            up_off_val = temp_mat * up_inverse

            up_off = cmds.createNode('multMatrix', n=f'{name}_upOffset_{i}_MM')
            cmds.setAttr(f'{up_off}.matrixIn[0]', list(up_off_val), type='matrix')
            cmds.connectAttr(f'{up}.matrixSum', f'{up_off}.matrixIn[1]')

            up_plug = f'{up_off}.matrixSum'

            cmds.delete(temp)

        aim = cmds.createNode('aimMatrix', n=f'{name}_pointOnCurve_{i}_AM')

        if position_plug:
            cmds.connectAttr(position_plug, f'{aim}.inputMatrix')
        else:
            matrices = [om.MMatrix(cmds.getAttr(top)) for top in trans_off_plugs]
            trans_wt_mat = get_weighted_translation_matrix(matrices, wts)
            cmds.setAttr(f'{aim}.inputMatrix', trans_wt_mat, type='matrix')

        if tangent_plug:
            cmds.connectAttr(f'{tangent}.matrixSum', f'{aim}.primaryTargetMatrix')
        else:
            matrices = [om.MMatrix(cmds.getAttr(top)) for top in trans_off_plugs]
            trans_wt_mat = get_weighted_translation_matrix(matrices, tangent_wts)

            if position_plug:

                position_m = om.MMatrix(cmds.getAttr(position_plug))
                tangent_offset_val = trans_wt_mat * position_m.inverse()

                tangent_off = cmds.createNode('multMatrix', n=f'{name}_tangentOffset_{i}_MM')
                cmds.setAttr(f'{tangent_off}.matrixIn[0]', tangent_offset_val, type='matrix')
                cmds.connectAttr(position_plug, f'{tangent_off}.matrixIn[1]')

                cmds.connectAttr(f'{tangent_off}.matrixSum', f'{aim}.primaryTargetMatrix')

            else:

                cmds.setAttr(f'{aim}.primaryTargetMatrix', trans_wt_mat, type='matrix')

        if up_plug == f'{mod_grp}.worldMatrix':
            mod_mat = cmds.getAttr(up_plug)
            cmds.setAttr(f'{aim}.secondaryTargetMatrix', mod_mat, type='matrix')
        else:
            cmds.connectAttr(up_plug, f'{aim}.secondaryTargetMatrix')

        output_plug = f'{aim}.outputMatrix'

        cmds.setAttr(f'{aim}.primaryInputAxis', *aim_vector)
        cmds.setAttr(f'{aim}.secondaryInputAxis', *AXIS_VECTOR[up_axis])
        cmds.setAttr(f'{aim}.secondaryMode', 2)
        cmds.setAttr(f'{aim}.secondaryTargetVector', *AXIS_VECTOR[up_axis])

        if use_scale:
            scale_wam = create_wt_add_matrix(sca_off_plugs, wts, f'{name}_scale_{i}_WAM', tol=tol)

            scale_mm = cmds.createNode('multMatrix', n=f'{name}_scale_{i}_MM')
            cmds.connectAttr(f'{scale_wam}.matrixSum', f'{scale_mm}.matrixIn[0]')
            cmds.connectAttr(output_plug, f'{scale_mm}.matrixIn[1]')

            output_plug = f'{scale_mm}.matrixSum'

        cmds.connectAttr(output_plug, f'{jnt}.offsetParentMatrix')

    return jnts


def get_consolidated_wts(wts, original_cvs, cvs):

    consolidated_wts = {cv: 0 for cv in original_cvs}
    for j, wt in enumerate(wts):
        consolidated_wts[cvs[j]] += wt

    return [consolidated_wts[cv] for cv in original_cvs]


def create_wt_add_matrix(matrix_attrs, wts, name, tol=0.000001):

    wam = cmds.createNode('wtAddMatrix', n=name)

    for matrix_attr, wt, i in zip(matrix_attrs, wts, range(len(matrix_attrs))):

        if wt < tol:
            continue

        cmds.connectAttr(matrix_attr, f'{wam}.wtMatrix[{i}].matrixIn')
        cmds.setAttr(f'{wam}.wtMatrix[{i}].weightIn', wt)

    return wam

def get_weighted_translation_matrix(matrices, wts):

    translation_m = om.MMatrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))

    for m, wt in zip(matrices, wts):
        for i in 12, 13, 14:
            translation_m[i] += m[i] * wt

    return translation_m
