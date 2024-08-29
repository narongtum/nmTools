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

	for base_mesh_p, mesh_p, offset_v, base_mesh_v, i in zip(mesh_pa, offset_va, base_mesh_va, range(len(mesh_pa))):
		if not offset_v.isEquivalent(om.MVector.kZeroVector):
			_, t = crv_fn.closetPoint(base_mesh_p)
			t_n = t / crv_spans

			if kv_type ==  PERIODIC:
				t_n = kv[d+1] * (1-t_n) * (d * 0.5 + 0.5) + t_n * (1-kv[d+1]) * (d*0.5-0.5)

			#... get the de boor weight
			wts = core.de_boor_core(len(modified_output_names), d, t_n, kv)

			if kv_type == PERIODIC:

				consolidated_wts = {output_name: 0 for output_name in output_names}
				for j, wt in enumerate(wts):
					consolidated_wts[modified_output_names[j]] += wt

				wts = consolidated_wts.values()

			for output_pa, wt in zip(put_pas, wts):
				pt = om.MPoint(base_mesh_v + offset_v * wt)
				output_pa[i] = pt

	output_meshes = []
	for output_pa, output in zip(output_pas, output_names):
		output_meshe = cmds.duplicate(base_mesh, n=output)[0]

		output_sel = om.MGlobal.getSelectionListByName(output_meshe)
		output_dp = output_sel.getDagPath(0)
		output_fn = om.MFnMesh(output_dp)
		output_fn.setPoints(output_pa)


		output_meshes.append(output_mesh) 

