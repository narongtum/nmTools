from maya import cmds
from maya.api import OpenMaya as om

from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.de_boor import hh_de_boor_core as core
reload(core)

OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}


def split_with_curve(mesh, base_mesh, crv, output_names, d=None):
    """
    Procedurally create blendShape targets by extracting the offset vectors between the mesh and base mesh; getting the
    closest point parameter from each point on the base mesh to curve; generating de boor weights using the number of
    outputs, degree and knot vector type; multiplying the offset vectors by the weights and duplicating the base mesh
    and applying the modified offset vectors

    Examples:
        from maya import cmds
        import blendshape
        import importlib
        importlib.reload(blendshape)


        # ----- example 1, curve form = open
        cmds.file(new=True, f=True)

        base_msh, base_msh_con = cmds.polyCube()
        cmds.setAttr(f'{base_msh_con}.subdivisionsWidth', 50)

        msh = cmds.duplicate(base_msh)[0]
        cmds.setAttr(f'{msh}.sy', 2)
        cmds.makeIdentity(msh, a=True)

        crv = cmds.curve(p=((-0.5, 0, 0), (0.5, 0, 0)), k=(0, 1), d=1)

        blendshape.split_with_curve(
            msh, base_msh, crv, ['left_blendShape', 'centre_blendShape', 'right_blendShape'])

        # ----- example 2, closed curve with linear degree
        cmds.file(new=True, f=True)

        base_msh, base_msh_con = cmds.polyTorus()

        msh = cmds.duplicate(base_msh)[0]
        cmds.setAttr(f'{msh}.sy', 2)
        cmds.makeIdentity(msh, a=True)

        crv = cmds.circle(normal=(0, 1, 0))[0]

        blendshape.split_with_curve(
            msh, base_msh, crv, [f'blendShape_{i}' for i in range(4)])

    Args:
        mesh (str): deformed mesh that will be split
        base_mesh (str): undeformed mesh that the offset vectors will be applied to
        crv (str): curve used to get the parameter value for each vert which are then used in the de boor algorithm
        output_names (list): defines the number and names of outputs
        d (int): degree of the basis functions

    Returns:
        list: names of the created meshes
    """

    num_outputs = len(output_names)
    crv_form = cmds.getAttr(f'{crv}.form')
    crv_spans = cmds.getAttr(f'{crv}.spans')

    d = num_outputs - 1 if d is None else d
    kv_type = INDEX_TO_KNOT_TYPE[crv_form]
    kv, modified_output_names = core.knot_vector(kv_type, output_names, d)

    mesh_sel = om.MGlobal.getSelectionListByName(mesh)
    base_mesh_sel = om.MGlobal.getSelectionListByName(base_mesh)
    crv_sel = om.MGlobal.getSelectionListByName(crv)

    mesh_dp = mesh_sel.getDagPath(0)
    base_mesh_dp = base_mesh_sel.getDagPath(0)

    mesh_fn = om.MFnMesh(mesh_dp)
    base_mesh_fn = om.MFnMesh(base_mesh_dp)

    mesh_pa = mesh_fn.getPoints()
    base_mesh_pa = base_mesh_fn.getPoints()

    base_mesh_va = om.MVectorArray(base_mesh_pa)
    offset_va = om.MVectorArray([mesh_p - base_mesh_p for mesh_p, base_mesh_p in zip(mesh_pa, base_mesh_pa)])

    crv_dp = crv_sel.getDagPath(0)
    crv_fn = om.MFnNurbsCurve(crv_dp)

    output_pas = [base_mesh_pa[:] for i in range(num_outputs)]

    for base_mesh_p, offset_v, base_mesh_v, i in zip(base_mesh_pa, offset_va, base_mesh_va, range(len(mesh_pa))):

        if not offset_v.isEquivalent(om.MVector.kZeroVector):

            _, t = crv_fn.closestPoint(base_mesh_p)
            t_n = t / crv_spans

            if kv_type == PERIODIC:
                t_n = kv[d + 1] * (1 - t_n) * (d * 0.5 + 0.5) + t_n * (1 - kv[d + 1] * (d * 0.5 - 0.5))

            wts = core.de_boor(len(modified_output_names), d, t_n, kv)

            if kv_type == PERIODIC:

                consolidated_wts = {output_name: 0 for output_name in output_names}
                for j, wt in enumerate(wts):
                    consolidated_wts[modified_output_names[j]] += wt

                wts = consolidated_wts.values()

            for output_pa, wt in zip(output_pas, wts):

                pt = om.MPoint(base_mesh_v + offset_v * wt)
                output_pa[i] = pt

    output_meshes = []

    for output_pa, output in zip(output_pas, output_names):

        output_mesh = cmds.duplicate(base_mesh, n=output)[0]

        output_sel = om.MGlobal.getSelectionListByName(output_mesh)
        output_dp = output_sel.getDagPath(0)
        output_fn = om.MFnMesh(output_dp)
        output_fn.setPoints(output_pa)

        output_meshes.append(output_mesh)

    return output_meshes
