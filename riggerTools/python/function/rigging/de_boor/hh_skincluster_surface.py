'''
from function.rigging.de_boor import de_boor_skincluster_surface
reload(de_boor_skincluster_surface)
'''




from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.de_boor import hh_de_boor_core as core
reload(core)










OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}


def split_with_surface(verts, jnts, srf, d=None, tol=0.000001):
    """
    Procedurally set the skinCluster weights for the joints attached to the skinCluster deforming the verts using the
    surface and the Cox-deBoor algorith

    Examples:
        from maya import cmds
        import skincluster_surface
        from importlib import reload
        reload(skincluster_surface)


        # ----- example 1, surface form = open, open
        cmds.file(new=True, f=True)

        jnts = []
        flat_jnts = []
        for i in range(3):
            v_jnts = []
            for j in range(3):
                cmds.select(cl=True)
                # we choose the x and z position values to align with the U and V directions of the nurbs plane
                jnt = cmds.joint(p=(i - 1, 0, 1 - j))
                v_jnts.append(jnt)
                flat_jnts.append(jnt)
            jnts.append(v_jnts)

        msh, msh_con = cmds.polyPlane()
        cmds.setAttr(f'{msh_con}.width', 2)
        cmds.setAttr(f'{msh_con}.height', 2)
        cmds.setAttr(f'{msh_con}.subdivisionsWidth', 30)
        cmds.setAttr(f'{msh_con}.subdivisionsHeight', 40)

        nrb, nrb_con = cmds.nurbsPlane(ax=(0, 1, 0))
        cmds.setAttr(f'{nrb_con}.width', 2)

        cmds.skinCluster(flat_jnts, msh)

        skincluster_surface.split_with_surface(msh, jnts, nrb)

        # ----- example 2, UV form = periodic, periodic
        cmds.file(new=True, f=True)

        JNT_POS_LISTS = [[[1.0, -0.5, 0.0], [0.0, -0.5, 1.0], [-1.0, -0.5, 0.0], [0.0, -0.5, -1.0]],
                         [[1.5, 0.0, 0.0], [0.0, 0.0, 1.5], [-1.5, 0.0, 0.0], [0.0, 0.0, -1.5]],
                         [[1.0, 0.5, 0.0], [0.0, 0.5, 1.0], [-1.0, 0.5, 0.0], [0.0, 0.5, -1.0]],
                         [[0.5, 0.0, 0.0], [0.0, 0.0, 0.5], [-0.5, 0.0, 0.0], [0.0, 0.0, -0.5]]]

        jnts = []
        flat_jnts = []
        for i, jnt_pos_list in enumerate(JNT_POS_LISTS):
            v_jnts = []
            for jnt_pos in jnt_pos_list:
                cmds.select(cl=True)
                jnt = cmds.joint(p=jnt_pos)
                v_jnts.append(jnt)
                flat_jnts.append(jnt)
            jnts.append(v_jnts)

        msh, msh_con = cmds.polyTorus()

        nrb, nrb_con = cmds.torus(ax=(0, 1, 0))
        cmds.setAttr(f'{nrb_con}.heightRatio', 0.5)

        cmds.skinCluster(flat_jnts, msh)

        skincluster_surface.split_with_surface(msh, jnts, nrb)

    Args:
        verts (str, list): verts that will be affected
        jnts (list): joints whose weight will be set
        srf (str): surface used to get the UV values for each vert which are then used in the de boor algorithm
        d (list): degree of the basis functions in the U and V directions
        tol (float): tolerance used to optimization

    Returns:
        None
    """

    original_sel = om.MGlobal.getActiveSelectionList()

    verts = cmds.ls(cmds.polyListComponentConversion(verts, toVertex=True), fl=True)

    jnts_copy = jnts[:]

    if d is None:
        d_u = len(jnts_copy) - 1
        d_v = min([len(j) for j in jnts_copy]) - 1
        d = [d_u, d_v]

    max_val_u = cmds.getAttr(f'{srf}.maxValueU')
    max_val_v = cmds.getAttr(f'{srf}.maxValueV')

    print(f'this is vluse of max_val_u: {max_val_u}')
    print(f'this is vluse of max_val_v: {max_val_v}')

    form_u = cmds.getAttr(f'{srf}.formU')
    form_v = cmds.getAttr(f'{srf}.formV')
    kv_type = [INDEX_TO_KNOT_TYPE[form_u], INDEX_TO_KNOT_TYPE[form_v]]

    vert_pa = om.MPointArray([cmds.xform(v, q=True, ws=True, t=True) for v in verts])

    cmds.select(verts)
    vert_sl = om.MGlobal.getActiveSelectionList()
    dag, components = vert_sl.getComponent(0)
    try:
        skin_cluster = cmds.ls(cmds.listHistory(dag.fullPathName()), typ='skinCluster')[0]
    except:
        print ('You maybe forget skinweight.')

    cmds.skinPercent(skin_cluster, pruneWeights=tol)

    skin_cluster_sl = om.MGlobal.getSelectionListByName(skin_cluster)
    skin_cluster_obj = skin_cluster_sl.getDependNode(0)
    skin_cluster_fn = oma.MFnSkinCluster(skin_cluster_obj)

    influences_dpa = skin_cluster_fn.influenceObjects()
    influences_names = [i.partialPathName() for i in influences_dpa]
    influence_ia = om.MIntArray(range(len(influences_dpa)))

    skin_wts = skin_cluster_fn.getWeights(dag, components, influence_ia)

    for v_jnts in jnts_copy:
        print (f' this is v_jnts: {v_jnts}')
        v_jnt_0_index = influences_names.index(v_jnts[0])

        for i, v_jnt in enumerate(v_jnts):
            if i != 0:
                v_jnt_index = influences_names.index(v_jnt)

                for j in range(len(verts)):
                    v_jnt_wt = skin_wts[len(influences_dpa) * j + v_jnt_index]
                    skin_wts[len(influences_dpa) * j + v_jnt_0_index] += v_jnt_wt
                    skin_wts[len(influences_dpa) * j + v_jnt_index] = 0

    srf_sl = om.MGlobal.getSelectionListByName(srf)
    srf_dp = srf_sl.getDagPath(0)
    srf_fn = om.MFnNurbsSurface(srf_dp)

    u_jnts = [jnts_v[0] for jnts_v in jnts_copy]
    jnts_copy.insert(0, u_jnts)

    for i, _jnts in enumerate(jnts_copy):

        if len(_jnts) < 2:
            continue

        _d = d[0] if i == 0 else d[1]
        _kv_type = kv_type[0] if i == 0 else kv_type[1]
        kv, modified_jnts = core.knot_vector(_kv_type, _jnts, _d)

        max_val = max_val_u if i == 0 else max_val_v
        print(f'this is vluse of U: {i}')

        jnt_indices = [influences_names.index(jnt) for jnt in _jnts]
        jnts_total_wts = [sum(skin_wts[jnt_index + j * len(influences_dpa)] for jnt_index in jnt_indices) for j in
                          range(len(verts))]

        for vert_p, jnts_total_wt, j in zip(vert_pa, jnts_total_wts, range(len(verts))):

            if jnts_total_wt < tol:
                continue

            cp = srf_fn.closestPoint(vert_p)
            t = cp[1] if i == 0 else cp[2]
            t_n = t / max_val

            if _kv_type == PERIODIC:
                t_n = (kv[_d + 1] * (_d * 0.5 + 0.5)) * (1 - t_n) + t_n * (1 - kv[_d + 1] * (_d * 0.5 - 0.5))



            print(f'This is de boor: {modified_jnts}, {_d}, {t_n}, {kv}')
            wts = core.de_boor(len(modified_jnts), _d, t_n, kv, tol=tol)

            if _kv_type == PERIODIC:

                consolidated_wts = {jnt: 0 for jnt in _jnts}
                for k, wt in enumerate(wts):
                    consolidated_wts[modified_jnts[k]] += wt

                wts = consolidated_wts.values()

            jnts_wts = [wt * jnts_total_wt for wt in wts]

            for k, jnt_index in enumerate(jnt_indices):
                skin_wts[jnt_index + j * len(influences_dpa)] = jnts_wts[k]

    skin_cluster_fn.setWeights(dag, components, influence_ia, skin_wts)

    om.MGlobal.setActiveSelectionList(original_sel)
