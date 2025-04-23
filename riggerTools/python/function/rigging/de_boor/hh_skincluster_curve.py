from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from function.rigging.de_boor import hh_de_boor_core as core

import importlib
importlib.reload(core)


OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}


def split_with_curve(verts, jnts, crv, d=None, tol=0.000001):
    """
    Procedurally set the skinCluster weights for the joints attached to the skinCluster deforming the verts using the
    curve and the de_boor function

    Examples:
        from maya import cmds
        import skincluster_curve
        import importlib
        importlib.reload(skincluster_curve)


        # ----- example 1, curve form = periodic
        cmds.file(new=True, f=True)

        msh = cmds.polyTorus()[0]
        crv = cmds.circle(normal=(0, 1, 0))[0]
        jnts = []
        for p in (0, 0, -1), (-1, 0, 0), (0, 0, 1), (1, 0, 0):
            cmds.select(cl=True)
            jnt = cmds.joint(p=p)
            jnts.append(jnt)

        cmds.skinCluster(jnts, msh)

        skincluster_curve.split_with_curve(msh, jnts, crv)

        # ----- example 2, curve form = open
        cmds.file(new=True, f=True)

        msh, msh_con = cmds.polyCube()
        for attr, val in zip(('hbl', 'h', 'sh'), (-1, 3, 30)):
            cmds.setAttr(f'{msh_con}.{attr}', val)
        crv = cmds.curve(p=[(0, 0, 0), (0, 3, 0)], d=1, k=(0, 1))
        jnts = []
        for p in (0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 3, 0):
            cmds.select(cl=True)
            jnt = cmds.joint(p=p)
            jnts.append(jnt)

        cmds.skinCluster(jnts, msh)

        skincluster_curve.split_with_curve(msh, jnts, crv)

    Args:
        verts (str, list): verts that will be affected
        jnts (list): joints whose weight will be set
        crv (str): curve used to get the parameter value for each vert which are then used in the de boor algorithm
        d (list): degree of the basis functions
        tol (float): tolerance used to optimization

    Returns:
        None
    """

    orginal_sel = om.MGlobal.getActiveSelectionList()

    verts = cmds.ls(cmds.polyListComponentConversion(verts, toVertex=True), fl=True)
    d = len(jnts) - 1 if d is None else d
    crv_spans = cmds.getAttr(f'{crv}.spans')

    kv_type = INDEX_TO_KNOT_TYPE[cmds.getAttr(f'{crv}.form')]
    kv, modified_jnts = core.knot_vector(kv_type, jnts, d)

    vert_pa = om.MPointArray([cmds.xform(v, q=True, ws=True, t=True) for v in verts])

    cmds.select(verts)
    vert_sl = om.MGlobal.getActiveSelectionList()
    dag, components = vert_sl.getComponent(0)

    skin_cluster = cmds.ls(cmds.listHistory(dag.fullPathName()), typ='skinCluster')[0]
    cmds.skinPercent(skin_cluster, pruneWeights=tol)

    skin_cluster_sl = om.MGlobal.getSelectionListByName(skin_cluster)
    skin_cluster_obj = skin_cluster_sl.getDependNode(0)
    skin_cluster_fn = oma.MFnSkinCluster(skin_cluster_obj)

    influence_dpa = skin_cluster_fn.influenceObjects()
    influences_names = [i.partialPathName() for i in influence_dpa]
    influences_ia = om.MIntArray(range(len(influence_dpa)))
    jnt_indices = [influences_names.index(jnt) for jnt in jnts]

    skin_wts = skin_cluster_fn.getWeights(dag, components, influences_ia)
    jnts_total_wts = [sum(skin_wts[jnt_index + i * len(influence_dpa)] for jnt_index in jnt_indices) for i in
                      range(len(verts))]

    crv_sl = om.MGlobal.getSelectionListByName(crv)
    crv_dp = crv_sl.getDagPath(0)
    crv_fn = om.MFnNurbsCurve(crv_dp)

    for vert_p, jnts_total_wt, i in zip(vert_pa, jnts_total_wts, range(len(verts))):

        if jnts_total_wt < tol:
            continue

        _, t = crv_fn.closestPoint(vert_p)
        t_n = t / crv_spans

        if kv_type == PERIODIC:
            t_n = (kv[d + 1] * (d * 0.5 + 0.5)) * (1 - t_n) + t_n * (1 - kv[d + 1] * (d * 0.5 - 0.5))

        wts = core.de_boor(len(modified_jnts), d, t_n, kv, tol=tol)

        if kv_type == PERIODIC:

            consolidated_wts = {jnt: 0 for jnt in jnts}
            for j, wt in enumerate(wts):
                consolidated_wts[modified_jnts[j]] += wt

            wts = consolidated_wts.values()

        jnts_wts = [wt * jnts_total_wt for wt in wts]

        for j, jnt_index in enumerate(jnt_indices):
            skin_wts[jnt_index + i * len(influence_dpa)] = jnts_wts[j]

    skin_cluster_fn.setWeights(dag, components, influences_ia, skin_wts)

    om.MGlobal.setActiveSelectionList(orginal_sel)
