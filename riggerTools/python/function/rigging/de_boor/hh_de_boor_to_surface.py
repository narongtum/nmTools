'''

from function.rigging.de_boor import hh_de_boor_to_surface as srf_deboor
reload(srf_deboor)

srf_deboor.split_with_surface(msh, [jnts], nrb)

# accept in 2D list [V][U]
# U herizontal
# V verticle
# jnts[V][U]
jnts = [
    ['j00', 'j01', 'j02'],  # V = 0
    ['j10', 'j11', 'j12'],  # V = 1
    ['j20', 'j21', 'j22']   # V = 2
]


'''




from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
from function.rigging.de_boor import hh_de_boor_core as de_core

OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}


def split_with_surface(mesh, jnt_grid, surface, d=None, tol=0.000001, visualize=True):
	original_sel = om.MGlobal.getActiveSelectionList()

	verts = cmds.ls(cmds.polyListComponentConversion(mesh, toVertex=True), fl=True)
	jnts_copy = jnt_grid[:]

	if d is None:
		d_u = len(jnts_copy) - 1
		d_v = min([len(j) for j in jnts_copy]) - 1
		d = [d_u, d_v]
	else:
		d_u, d_v = d

	max_val_u = cmds.getAttr(f'{surface}.maxValueU')
	max_val_v = cmds.getAttr(f'{surface}.maxValueV')
	form_u = cmds.getAttr(f'{surface}.formU')
	form_v = cmds.getAttr(f'{surface}.formV')
	kv_type = [INDEX_TO_KNOT_TYPE[form_u], INDEX_TO_KNOT_TYPE[form_v]]

	vert_pa = om.MPointArray([cmds.xform(v, q=True, ws=True, t=True) for v in verts])

	cmds.select(verts)
	vert_sl = om.MGlobal.getActiveSelectionList()
	dag, components = vert_sl.getComponent(0)

	try:
		skin_cluster = cmds.ls(cmds.listHistory(dag.fullPathName()), typ='skinCluster')[0]
	except:
		raise RuntimeError('No skinCluster found on mesh.')

	cmds.skinPercent(skin_cluster, pruneWeights=tol)

	skin_cluster_sl = om.MGlobal.getSelectionListByName(skin_cluster)
	skin_cluster_obj = skin_cluster_sl.getDependNode(0)
	skin_cluster_fn = oma.MFnSkinCluster(skin_cluster_obj)

	influences_dpa = skin_cluster_fn.influenceObjects()
	influences_names = [i.partialPathName() for i in influences_dpa]
	influence_ia = om.MIntArray(range(len(influences_dpa)))

	skin_wts = skin_cluster_fn.getWeights(dag, components, influence_ia)

	# Consolidate row weights
	for v_jnts in jnts_copy:
		v_jnt_0_index = influences_names.index(v_jnts[0])
		for i, v_jnt in enumerate(v_jnts):
			if i == 0:
				continue
			v_jnt_index = influences_names.index(v_jnt)
			for j in range(len(verts)):
				wt = skin_wts[j * len(influences_dpa) + v_jnt_index]
				skin_wts[j * len(influences_dpa) + v_jnt_0_index] += wt
				skin_wts[j * len(influences_dpa) + v_jnt_index] = 0

	srf_sl = om.MGlobal.getSelectionListByName(surface)
	srf_dp = srf_sl.getDagPath(0)
	srf_fn = om.MFnNurbsSurface(srf_dp)

	u_jnts = [jnts_v[0] for jnts_v in jnts_copy]
	jnts_copy.insert(0, u_jnts)

	for i, _jnts in enumerate(jnts_copy):
		if len(_jnts) < 2:
			continue

		_d = d[0] if i == 0 else d[1]
		_kv_type = kv_type[0] if i == 0 else kv_type[1]
		kv, modified_jnts = de_core.knot_vector(_kv_type, _jnts, _d)
		max_val = max_val_u if i == 0 else max_val_v

		jnt_indices = [influences_names.index(jnt) for jnt in _jnts]
		jnts_total_wts = [sum(skin_wts[jnt_index + j * len(influences_dpa)] for jnt_index in jnt_indices) for j in range(len(verts))]

		for j, (vert_p, jnt_total_wt) in enumerate(zip(vert_pa, jnts_total_wts)):
			if jnt_total_wt < tol:
				continue

			cp = srf_fn.closestPoint(vert_p)
			t = cp[1] if i == 0 else cp[2]
			t_n = t / max_val

			if _kv_type == PERIODIC:
				t_n = (kv[_d + 1] * (_d * 0.5 + 0.5)) * (1 - t_n) + t_n * (1 - kv[_d + 1] * (_d * 0.5 - 0.5))

			# Debug: Create locator at closest point
			if i == 0 and visualize:
				name = f'debug_uv_loc_{j:03d}'
				if not cmds.objExists(name):
					loc = cmds.spaceLocator(name=name)[0]
					cmds.xform(loc, ws=True, t=cp[0])
					cmds.setAttr(f"{loc}.localScaleX", 0.05)
					cmds.setAttr(f"{loc}.localScaleY", 0.05)
					cmds.setAttr(f"{loc}.localScaleZ", 0.05)

			wts = de_core.de_boor(len(modified_jnts), _d, t_n, kv, tol=tol)

			if _kv_type == PERIODIC:
				consolidated_wts = {jnt: 0 for jnt in _jnts}
				for k, wt in enumerate(wts):
					consolidated_wts[modified_jnts[k]] += wt
				wts = consolidated_wts.values()

			jnts_wts = [wt * jnt_total_wt for wt in wts]
			for k, jnt_index in enumerate(jnt_indices):
				skin_wts[jnt_index + j * len(influences_dpa)] = jnts_wts[k]

	skin_cluster_fn.setWeights(dag, components, influence_ia, skin_wts)
	om.MGlobal.setActiveSelectionList(original_sel)



'''






jnts = []
flat_jnts = []
for i in range(3):
	v_jnts = []
	for j in range(3):
		mc.select(cl=True)
		# we choose the x and z position values to align with the U and V directions of the nurbs plane
		jnt = mc.joint(p=(i - 1, 0, 1 - j))
		v_jnts.append(jnt)
		flat_jnts.append(jnt)
	jnts.append(v_jnts)

msh, msh_con = mc.polyPlane()
mc.setAttr(f'{msh_con}.width', 2)
mc.setAttr(f'{msh_con}.height', 2)
mc.setAttr(f'{msh_con}.subdivisionsWidth', 30)
mc.setAttr(f'{msh_con}.subdivisionsHeight', 40)

nrb, nrb_con = mc.nurbsPlane(ax=(0, 1, 0))
mc.setAttr(f'{nrb_con}.width', 2)

mc.skinCluster(flat_jnts, msh)
mc.skinCluster(flat_jnts, nrb)


'''
