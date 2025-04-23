def split_curve_cvs_with_de_boor_v2(jnts, crv, d=None, tol=0.000001):
    from maya import cmds as mc
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaAnim as oma
    import importlib
    from function.rigging.de_boor import hh_de_boor_core as core
    importlib.reload(core)

    OPEN = 'open'
    PERIODIC = 'periodic'
    INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}

    orginal_sel = om.MGlobal.getActiveSelectionList()

    d = len(jnts) - 1 if d is None else d
    crv_spans = mc.getAttr(f'{crv}.spans')

    kv_type = INDEX_TO_KNOT_TYPE[mc.getAttr(f'{crv}.form')]

    kv, modified_jnts = core.knot_vector(kv_type, jnts, d)

    # Get CV positions
    cvs = [f'{crv}.cv[{i}]' for i in range(mc.getAttr(f'{crv}.spans') + mc.getAttr(f'{crv}.degree'))]
    cv_pa = om.MPointArray([mc.pointPosition(cv, w=True) for cv in cvs])

    # Skin the curve if not already skinned
    existing_skin = mc.ls(mc.listHistory(crv), type='skinCluster')
    if not existing_skin:
        skin_cluster = mc.skinCluster(jnts, crv)[0]
    else:
        skin_cluster = existing_skin[0]

    # Access skin cluster function set
    crv_sl = om.MGlobal.getSelectionListByName(crv)
    crv_dag = crv_sl.getDagPath(0)
    crv_dag.extendToShape()  # Get shape node

    skin_sl = om.MGlobal.getSelectionListByName(skin_cluster)
    skin_obj = skin_sl.getDependNode(0)
    skin_fn = oma.MFnSkinCluster(skin_obj)

    # Get influences
    infls = skin_fn.influenceObjects()
    infl_names = [i.partialPathName() for i in infls]
    infl_ia = om.MIntArray(range(len(infls)))
    jnt_indices = [infl_names.index(jnt) for jnt in jnts]

    # Prepare components for curve CVs
    cv_sl = om.MSelectionList()
    cv_sl.add(','.join(cvs))
    crv_dag = cv_sl.getDagPath(0)
    crv_dag.extendToShape()
    _, crv_comps = cv_sl.getComponent(0)


    # Start calculating weights
    skin_wts = skin_fn.getWeights(crv_dag, crv_comps, infl_ia)

    for i, pt in enumerate(cv_pa):
        _, t = om.MFnNurbsCurve(crv_dag).closestPoint(pt)
        t_n = t / crv_spans

        if kv_type == PERIODIC:
            t_n = (kv[d + 1] * (d * 0.5 + 0.5)) * (1 - t_n) + t_n * (1 - kv[d + 1] * (d * 0.5 - 0.5))

        wts = core.de_boor(len(modified_jnts), d, t_n, kv, tol=tol)

        if kv_type == PERIODIC:
            consolidated_wts = {jnt: 0 for jnt in jnts}
            for j, wt in enumerate(wts):
                consolidated_wts[modified_jnts[j]] += wt
            wts = consolidated_wts.values()

        for j, jnt_index in enumerate(jnt_indices):
            skin_wts[jnt_index + i * len(infls)] = wts[j]

    skin_fn.setWeights(crv_dag, crv_comps, infl_ia, skin_wts)
    om.MGlobal.setActiveSelectionList(orginal_sel)


#... usege

# Your joints and curve
jnts = ['joint1', 'joint2', 'joint3', 'joint4']  # Example joint list
crv = 'curve1'  # Your curve name

# Call the function
split_curve_cvs_with_de_boor_v2(jnts, crv)

