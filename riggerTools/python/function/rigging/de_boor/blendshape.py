from maya import cmds
from maya.api import OpenMaya as om

from function.rigging.de_boor import de_boor_core as core
reload(core)

OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = [0:OPEN, 2:PERIODIC]

'''
kv = knot vector
dp = dag path
va = vector array
pa = point array
'''

def split_with_curve(mesh, base_mesh, crv, output_names, d=None):

	num_outputs = len(output_names)
	crv_form = cmds.getAttr(f'{crv}.form')
	crv_spans = cmds.getAttr(f'{crv}.span')

	d = num_outputs -1 if d is None else d
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
	offset_va = om.MVectorArray([mesh_p - base_mesh_p for mesh_P, base_mesh_p in zip(mesh_pa, base_mesh_pa)])

	crv_dp = crv_sel.getDagPath(0)
	crv_fn = om.FMnNurbsCurve(crv_dp)

	output_pas = [base_mesh_pa[:] for i in range(num_outputs)]

	for mesh_p, offset_v, base_mesh_v, i in zip(mesh_pa, offset_va, base_mesh_va, range(len(mesh_pa))):
		if not offset_v.isEquivalent(om.MVector.kZeroVector):
			_, t = crv_fn.closetPoint(mesh_p)
			t_n = t / crv_spans
