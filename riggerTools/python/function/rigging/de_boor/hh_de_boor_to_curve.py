"""
from function.rigging.de_boor import hh_de_boor_to_curve
reload(hh_de_boor_to_curve)

"""


#... distribute de boor weight value to curve

import math
from maya import cmds as mc
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
import importlib
from function.rigging.de_boor import hh_de_boor_core as core
importlib.reload(core)

OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}



def ramp_style_falloff_A(t_n):
	"""
	Custom falloff to match sculpted ramp curve in lip rig.
	- Flat start
	- Steep rise mid way
	- Level out
	"""
	t_n = max(0.0, min(1.0, t_n))
	if t_n < 0.3:
		return 0.0
	elif t_n < 0.6:
		# Smooth ramp up using cubic transition
		return ((t_n - 0.3) / 0.3) ** 2.5
	else:
		# Ease to 1.0
		return 1.0 - ((1.0 - t_n) ** 2.5)

def ramp_style_falloff(t_n):
	t_n = max(0.0, min(1.0, t_n))
	
	# Stay flat until about 30%
	if t_n < 0.3:
		return 0.0

	# Sharp rise between 30% and 60%
	elif t_n < 0.6:
		x = (t_n - 0.3) / 0.3  # normalize to 0-1
		return x ** 3  # control steepness here

	# Hold plateau after 60%
	else:
		return 1.0


def ease_in_out_sine(t):
	return -0.5 * (math.cos(math.pi * t) - 1)

def ease_in_cubic(t):
	return t ** 3

def ease_out_cubic(t):
	return 1 - (1 - t) ** 3

def custom_falloff_t(t_n, method='ease_in_out_sine'):
	t_n = max(0.0, min(1.0, t_n))
	if method == 'ease_in_out_sine':
		return ease_in_out_sine(t_n)
	elif method == 'ease_in_cubic':
		return ease_in_cubic(t_n)
	elif method == 'ease_out_cubic':
		return ease_out_cubic(t_n)
	return t_n  # fallback to linear

def shape_weights(weights, jnts, shape='corner_bias'):
	if shape == 'corner_bias':
		shaped = []
		for jnt, w in zip(jnts, weights):
			if 'corner' in jnt.lower():
				w *= 1.2
			elif 'center' in jnt.lower() or 'mid' in jnt.lower():
				w *= 1.1
			shaped.append(w)
		return shaped
	return weights


def skin_curve_with_de_boor(jnts, crv, d=None, tol=0.000001, falloff_mode='ease_in_out_sine'):
	import math
	from maya.api import OpenMaya as om
	from maya.api import OpenMayaAnim as oma
	from maya import cmds

	def ease_in_out_sine(t): return -0.5 * (math.cos(math.pi * t) - 1)
	def ease_in_cubic(t): return t ** 3
	def ease_out_cubic(t): return 1 - (1 - t) ** 3
	def custom_falloff_t(t_n, mode):
		t_n = max(0.0, min(1.0, t_n))
		return {
			'ease_in_out_sine': ease_in_out_sine,
			'ease_in_cubic': ease_in_cubic,
			'ease_out_cubic': ease_out_cubic,
		}.get(mode, lambda x: x)(t_n)

	# Step 1: Setup
	d = len(jnts) - 1 if d is None else d
	spans = cmds.getAttr(f'{crv}.spans')
	kv_type = INDEX_TO_KNOT_TYPE[cmds.getAttr(f'{crv}.form')]
	kv, modified_jnts = core.knot_vector(kv_type, jnts, d)

	# Step 2: Create skinCluster if it doesn't exist
	if not cmds.ls(cmds.listHistory(crv), type='skinCluster'):
		skin_cluster = cmds.skinCluster(jnts, crv, tsb=True)[0]
	else:
		skin_cluster = cmds.ls(cmds.listHistory(crv), type='skinCluster')[0]

	crv_sl = om.MGlobal.getSelectionListByName(crv)
	crv_dag = crv_sl.getDagPath(0)
	crv_dag.extendToShape()
	fn_curve = om.MFnNurbsCurve(crv_dag)
	num_cvs = fn_curve.numCVs

	# Step 3: Access skin cluster and influences
	skin_sl = om.MGlobal.getSelectionListByName(skin_cluster)
	skin_obj = skin_sl.getDependNode(0)
	skin_fn = oma.MFnSkinCluster(skin_obj)
	infls = skin_fn.influenceObjects()
	infl_names = [i.partialPathName() for i in infls]
	infl_ia = om.MIntArray(range(len(infls)))
	jnt_indices = [infl_names.index(jnt) for jnt in jnts]

	# Step 4: Component for CVs
	comp_fn = om.MFnSingleIndexedComponent()
	crv_comps = comp_fn.create(om.MFn.kCurveCVComponent)
	comp_fn.addElements(list(range(num_cvs)))

	# Step 5: Init weight array
	weights = om.MDoubleArray(len(infls) * num_cvs, 0.0)

	# Step 6: Loop and apply De Boor weights to each CV
	for i in range(num_cvs):
		pos = om.MPoint(cmds.pointPosition(f'{crv}.cv[{i}]', w=True))
		_, t = fn_curve.closestPoint(pos)
		t = float(t) if not isinstance(t, complex) else float(t.real)
		
		if falloff_mode == 'ramp_custom':
			t_n = ramp_style_falloff(t / spans)
		else:
			t_n = custom_falloff_t(t / spans, falloff_mode)


		if kv_type == PERIODIC:
			t_n = (kv[d + 1] * (d * 0.5 + 0.5)) * (1 - t_n) + t_n * (1 - kv[d + 1] * (d * 0.5 - 0.5))

		wts = core.de_boor(len(modified_jnts), d, t_n, kv, tol=tol)

		if kv_type == PERIODIC:
			consolidated_wts = {jnt: 0 for jnt in jnts}
			for j, wt in enumerate(wts):
				consolidated_wts[modified_jnts[j]] += wt
			wts = list(consolidated_wts.values())

		total = sum(wts)
		wts = [w / total for w in wts]

		for j, jnt_index in enumerate(jnt_indices):
			weights[jnt_index + i * len(infls)] = wts[j]

	# Step 7: Apply weights
	skin_fn.setWeights(crv_dag, crv_comps, infl_ia, weights, False)







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


#... can adjust falloff for make it sharp or smooth
def split_curve_cvs_with_de_boor_v4(joints, curve, degree=3, falloff_mode='ramp_custom', falloff_width=0.25):
	import maya.api.OpenMaya as om
	import maya.cmds as cmds
	import math

	def ease_in_out_sine(x):
		return -(math.cos(math.pi * x) - 1) / 2

	def ramp_custom(x):
		return ease_in_out_sine(x)

	# Get curve function and parameter range
	sel = om.MSelectionList()
	sel.add(curve)
	dagPath = sel.getDagPath(0)
	curveFn = om.MFnNurbsCurve(dagPath)

	min_u, max_u = curveFn.knotDomain

	cvs = [curveFn.cvPosition(i, om.MSpace.kWorld) for i in range(curveFn.numCVs)]
	weights = [[0.0 for _ in joints] for _ in cvs]

	# Find connected skinCluster if exists
	skinClusters = cmds.ls(cmds.listHistory(curve), type='skinCluster')
	skinCluster = skinClusters[0] if skinClusters else None

	# Step 1: Get normalized u position of each joint on the curve
	joint_u_normalized = []
	for joint in joints:
		sel.clear()
		sel.add(joint)
		joint_path = sel.getDagPath(0)
		joint_pos = om.MPoint(om.MFnTransform(joint_path).translation(om.MSpace.kWorld))
		param = curveFn.closestPoint(joint_pos, space=om.MSpace.kWorld)[1]
		joint_u_norm = (param - min_u) / (max_u - min_u) if max_u > min_u else 0.0
		joint_u_normalized.append(joint_u_norm)

	# Step 2: Loop through CVs and calculate weights
	for i, cv in enumerate(cvs):
		cv_u = curveFn.closestPoint(cv, space=om.MSpace.kWorld)[1]
		u_normalized = (cv_u - min_u) / (max_u - min_u) if max_u > min_u else 0.0

		for j, u_j in enumerate(joint_u_normalized):
			distance = abs(u_normalized - u_j)

			if distance > falloff_width:
				weight = 0.0
			else:
				t = distance / falloff_width
				if falloff_mode == 'ramp_custom':
					weight = ramp_custom(1.0 - t)
				elif falloff_mode == 'linear':
					weight = 1.0 - t
				else:
					weight = 1.0 - t

			weights[i][j] = weight

		# Normalize weights per CV so they sum to 1
		total = sum(weights[i])
		if total > 0.0:
			weights[i] = [w / total for w in weights[i]]

		# Always apply to skinCluster if one is found
		if skinCluster:
			for j, joint in enumerate(joints):
				cmds.skinPercent(skinCluster, f'{curve}.cv[{i}]', transformValue=[(joint, weights[i][j])])

	return weights




	
# #... Example Usage:

# jnts = list_joints_from_skincluster('lip_upper_L01_skc')
# crv = 'lip_upper_L01_crv'  
# split_curve_cvs_with_de_boor_v2(jnts, crv)


# msh = 'upper02'
# crv = 'lip_upper_L03_crv'
# jnts = [f'lip_upper_L03_skin_{str(i).zfill(2)}_jnt' for i in range(1, 22)]

# mc.skinCluster(jnts, msh, tsb=True)
# split_with_curve_v3(msh, jnts, crv, falloff_mode='ease_in_out_sine')


