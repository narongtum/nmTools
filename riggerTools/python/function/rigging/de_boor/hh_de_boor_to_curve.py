"""
from function.rigging.de_boor import hh_de_boor_to_curve
reload(hh_de_boor_to_curve)

"""


#... distribute de boor weight value to curve

from maya import cmds as mc
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
import importlib
from function.rigging.de_boor import hh_de_boor_core as core
importlib.reload(core)

OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}

def split_curve_cvs_with_de_boor_v2(jnts, crv, d=None, tol=0.000001):

	print(mc.objExists(crv))

	for j in jnts:
		print(j, mc.objExists(j))
	
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

	# Get shape path
	sl = om.MSelectionList()
	sl.add(crv)
	crv_dag = sl.getDagPath(0)
	crv_dag.extendToShape()  # Go to the shape node

	# Get number of CVs
	fn_curve = om.MFnNurbsCurve(crv_dag)
	num_cvs = fn_curve.numCVs

	# Create component object for CVs
	comp_fn = om.MFnSingleIndexedComponent()
	crv_comps = comp_fn.create(om.MFn.kCurveCVComponent)
	comp_fn.addElements(list(range(num_cvs)))



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


def list_joints_from_skincluster(skincluster):
	
	if not mc.objExists(skincluster):
		raise RuntimeError(f"SkinCluster '{skincluster}' does not exist.")
	
	jnts = mc.skinCluster(skincluster, q=True, inf=True)
	print(f'This is joint in skinCluster: {jnts}')
	return jnts




# #... usege sample

# jnts = list_joints_from_skincluster('lip_upper_L01_skc')
# crv = 'lip_upper_L01_crv'  
# split_curve_cvs_with_de_boor_v2(jnts, crv)

