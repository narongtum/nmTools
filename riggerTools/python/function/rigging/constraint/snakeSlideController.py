# Maya Python — Snake path "Ghost Follower" rig helper
# Converted: use maya.cmds (mc) for core rig logic
# Keep PyMEL (pm) only for UI

import maya.cmds as mc
import pymel.core as pm
import json
from maya.api import OpenMaya as om

RIG_NODE = "rig_grp"
SLIDE_LIST_ATTR = "slide_ctrls"
GHOST_GRP_NAME = "pathGhost_GRP"
MD_NAME = "SlideScale_MD"
SLIDE_ATTR = "pathSlide"
SCALE_ATTR = "pathScale"
SCALE_INIT_VAL = 0.01
TITLE_NAME = 'Snake Switch Path 0.9.6'

# ----------------------------- Utilities -----------------------------

def _namespaced(name, namespace):
	if namespace and namespace not in ("", "None"):
		return "{}:{}".format(namespace, name)
	return name

def _ghost_name(node):
	return node.replace(":", "_") + "_pathGhost"

def getRigNode(namespace=None):
	return _namespaced(RIG_NODE, namespace)

def get_slide_ctrls(namespace=None):
	rigNode = getRigNode(namespace)
	if not mc.objExists(rigNode):
		mc.error("Rig node not found: {}".format(rigNode))
	raw = mc.getAttr(rigNode + "." + SLIDE_LIST_ATTR)
	try:
		names = json.loads(raw)
	except Exception as e:
		mc.error("slide_ctrls is not valid JSON: {}".format(e))
	if namespace and namespace not in ("", "None"):
		names = ["{}:{}".format(namespace, n) for n in names]
	return names

def ensure_slide_attrs(curveField, namespace=None):
	"""
	Ensure shared slide attributes exist on the path curve specified by UI text field.
	Keeps v5 ranges/defaults: pathSlide [0..1], default 0.0; pathScale min 0.0, default 0.01
	"""
	# Read path curve name from the existing UI text field
	path_crv = pm.textField(curveField, q=True, text=True)
	if not mc.objExists(path_crv):
		om.MGlobal.displayError(f"[SlideAttr] Path curve not found: {path_crv}")
		return None

	# Create shared attributes on the path curve, not on controllers
	if not mc.attributeQuery(SLIDE_ATTR, node=path_crv, exists=True):
		mc.addAttr(path_crv, ln=SLIDE_ATTR, at="double", k=True)  #... no range
		mc.setAttr(f"{path_crv}.{SLIDE_ATTR}", 0.0)  # v5 default

	if not mc.attributeQuery(SCALE_ATTR, node=path_crv, exists=True):
		mc.addAttr(path_crv, ln=SCALE_ATTR, at="double", k=True, min=0.0)  # v5 range
		mc.setAttr(f"{path_crv}.{SCALE_ATTR}", 0.01)  # v5 default

	return path_crv


# ---------------------------------------------------------------------
# PATCH 2: get_or_create_shared_md
# - Connect MD to path_crv.pathSlide / path_crv.pathScale instead of controller attrs
# - Keep downstream network unchanged
# ---------------------------------------------------------------------
def get_or_create_shared_md(namespace=None, curveField=None):
	"""
	Create or fetch the shared multiplyDivide node and wire it to the path curve's shared attributes.
	"""
	# Resolve path curve from UI
	path_crv = pm.textField(curveField, q=True, text=True)
	if not mc.objExists(path_crv):
		mc.error("Path curve not found for multiplyDivide setup.")

	# Ensure shared attributes exist
	if not mc.attributeQuery(SLIDE_ATTR, node=path_crv, exists=True) or not mc.attributeQuery(SCALE_ATTR, node=path_crv, exists=True):
		mc.error(f"Missing {SLIDE_ATTR} or {SCALE_ATTR} on {path_crv}. Run ensure_slide_attrs first.")

	# Create or get shared MD
	if not mc.objExists(MD_NAME):
		md = mc.createNode("multiplyDivide", n=MD_NAME)
	else:
		md = MD_NAME

	# Set MD to multiply (1)
	try:
		mc.setAttr(md + ".operation", 1)
	except:
		pass

	# Wire shared attrs from path curve to MD
	try:
		mc.connectAttr(f"{path_crv}.{SLIDE_ATTR}", md + ".input1X", f=True)
	except:
		pass
	try:
		mc.connectAttr(f"{path_crv}.{SCALE_ATTR}", md + ".input2X", f=True)
	except:
		pass

	return md

def ensure_ghost_group():
	if mc.objExists(GHOST_GRP_NAME):
		return GHOST_GRP_NAME
	return mc.group(em=True, n=GHOST_GRP_NAME)

# ---------------------------- Ghost Builder ---------------------------

# ---------------------------------------------------------------------
# PATCH 3: build_path_ghosts
# - Merge "create slide attrs" + "build/update" into a single call
# - Keep v5 ghost build logic intact, only change MD sourcing
# ---------------------------------------------------------------------
def build_path_ghosts(curveField, namespace=None):
	"""
	Build or update path ghosts using a shared MD driven by attributes on the path curve.
	This function now also ensures the shared attributes on the path curve.
	"""
	# Resolve curve from UI
	name = pm.textField(curveField, q=True, text=True)
	if not mc.objExists(name):
		om.MGlobal.displayError(f"[Build] Path curve not found: {name}")
		return
	crv_shapes = mc.listRelatives(name, s=True) or []
	if not crv_shapes:
		om.MGlobal.displayError(f"[Build] No shape under: {name}")
		return
	crv_shape = crv_shapes[0]

	# Ensure shared attributes and MD on path curve
	ensure_slide_attrs(curveField, namespace)
	md = get_or_create_shared_md(namespace, curveField)

	# Host group for ghosts (uses existing v5 helper)
	host = ensure_ghost_group()

	# Iterate controllers from v5 rig data
	ctrls = get_slide_ctrls(namespace)
	if not ctrls:
		om.MGlobal.displayWarning("[Build] No slide controllers found on rig. Check slide_ctrls attr.")
		return

	for ctrl in ctrls:
		# Ghost name
		gname = _ghost_name(ctrl)

		# Create or fetch ghost
		if not mc.objExists(gname):
			ghost = mc.spaceLocator(n=gname)[0]
		else:
			ghost = gname

		# Parent ghost under host group if needed
		if mc.listRelatives(ghost, p=True) != [host]:
			try:
				mc.parent(ghost, host)
			except:
				pass

		# Snap ghost to controller (v5 behavior)
		try:
			mc.delete(mc.parentConstraint(ctrl, ghost, mo=False))
		except:
			pass

		# Compute nearest U on curve from ghost world position
		npoc = mc.createNode("nearestPointOnCurve")
		mc.connectAttr(crv_shape + ".worldSpace[0]", npoc + ".inputCurve", f=True)
		pos = mc.xform(ghost, q=True, ws=True, t=True)
		mc.setAttr(npoc + ".inPosition", *pos)
		u = mc.getAttr(npoc + ".parameter")
		mc.delete(npoc)

		# Ensure baseU on ghost and set initial value
		if not mc.attributeQuery("baseU", node=ghost, exists=True):
			mc.addAttr(ghost, ln="baseU", at="double", k=True)
		mc.setAttr(ghost + ".baseU", u)

		# Motion path setup (keep v5 logic)
		mp_name = ghost + "_MP"
		if not mc.objExists(mp_name):
			mp = mc.createNode("motionPath", n=mp_name)
		else:
			mp = mp_name
		mc.connectAttr(crv_shape + ".worldSpace[0]", mp + ".geometryPath", f=True)
		mc.setAttr(mp + ".fractionMode", True)
		mc.setAttr(mp + ".follow", True)
		mc.setAttr(mp + ".uValue", u)
		mc.connectAttr(mp + ".allCoordinates", ghost + ".translate", f=True)
		mc.connectAttr(mp + ".rotate", ghost + ".rotate", f=True)

		# AddDoubleLinear for baseU + (slide*scale)
		adl_name = ghost + "_U_ADL"
		if not mc.objExists(adl_name):
			adl = mc.createNode("addDoubleLinear", n=adl_name)
		else:
			adl = adl_name

		# Wire baseU and shared MD to ADL
		mc.connectAttr(ghost + ".baseU", adl + ".input1", f=True)
		mc.connectAttr(md + ".outputX", adl + ".input2", f=True)

		# Drive motionPath.uValue by ADL output
		mc.connectAttr(adl + ".output", mp + ".uValue", f=True)

		om.MGlobal.displayInfo(f"[Info] Built/updated path ghost for: {ctrl}")

	# ---------------------------------------------------------------------
	#... build another block for make stretchy
	# ---------------------------------------------------------------------
	# mc.error(ctrls)

	
	CTRL = ctrls[0]
	base_oldName = CTRL.split(':')[1].split('_')[0][:-2]

	valueStretch = 1.5

	NS = getSelectedNamespace()
	base_full_listName = core.generate_named_pattern(f'{base_oldName}##', len(ctrls))
	base_name = base_full_listName[1:] #... cut member index 0
	print(crv_shape)

	loc_ghost_full_name = core.generate_named_pattern(f'{NS}_{base_oldName}##_hook_loc_pathGhost', len(ctrls))
	# mc.error(loc_ghost_full_name)	
	loc_ghost = loc_ghost_full_name[1:] #... cut member index 0
	stick_obj = core.Dag(crv_shape)

	stick_obj.addAttribute( at = 'float', longName = SLIDE_STRETCHY_ATTR, keyable = True)
	stick_obj.addAttribute( at = 'float', longName = SCALE_STRETCHY_ATTR, keyable = True, defaultValue = SCALE_INIT_VAL)

	


	for idx, each in enumerate(base_name):
		print(idx, each)
		loc_obj = core.Dag(loc_ghost[idx])
		init_val = loc_obj.attr('baseU').value
		print(init_val)
		scale_mdl = core.MultiDoubleLinear(f'{base_name[idx]}_scale')
		init_stretch_mdl = core.MultiDoubleLinear(f'{base_name[idx]}_initValueStretch')
		init_stretch_mdl.attr('input2').value = valueStretch
		storeVal_pma = core.PlusMinusAverage(f'{base_name[idx]}_storeVal')
		scale_mdl.attr('output') >> init_stretch_mdl.attr('input1')
		init_stretch_mdl.attr('output') >> storeVal_pma.attr('input1D[0]')
		init_stretch_mdl.attr('output') >> storeVal_pma.attr('input1D[1]')
		init_stretch_mdl.attr('output') // storeVal_pma.attr('input1D[0]')
		storeVal_pma.attr('input1D[0]').value = init_val
		valueStretch = valueStretch + 0.5
		stick_obj.attr(SLIDE_STRETCHY_ATTR) >> scale_mdl.attr('input1')
		stick_obj.attr(SCALE_STRETCHY_ATTR) >> scale_mdl.attr('input2')
		storeVal_pma.attr('output1D') >> loc_obj.attr('baseU')


	om.MGlobal.displayInfo("[Done] Build/Update complete. Shared attrs are on the path curve.")
# --------------------------- Constrain & Toggle -----------------------

def _get_parent_handle(node):
	if node.endswith("_loc"):
		node = node[:-4]
	return node + "_PH"

def _get_snap_group(node):
	if node.endswith("_loc"):
		node = node[:-4]
	return node + "_SN"

def attach_all(namespace=None):
	ctrls = get_slide_ctrls(namespace)
	if not ctrls:
		mc.warning("No controllers found to attach.")
		return

	cur = mc.currentTime(q=True)
	start_frame = mc.playbackOptions(q=True, ast=True)

	for node in ctrls:
		ghost = _ghost_name(node)
		ph = _get_parent_handle(node)
		sn = _get_snap_group(node)

		if not mc.objExists(ph) or not mc.objExists(sn):
			mc.warning("Missing PH/SN for {}".format(node))
			continue

		con_name = node.replace(":", "_") + "_followPath_PC"
		if not mc.objExists(con_name):
			# con = mc.parentConstraint(ghost, ph, mo=True, n=con_name)[0]
			con = mc.parentConstraint(ghost, ph, mo=False, n=con_name)[0]
		else:
			con = con_name


		# query weight aliases
		wattrs = mc.parentConstraint(con, q=True, weightAliasList=True)[0]
		print(wattrs)
		# mc.error(wattrs)
		
		# plug = "{}.{}".format(con, wattrs)
		plug = f'{con}.{wattrs}'
		print(plug)
		print(plug)
		print(plug)

		if cur > start_frame:
			mc.setAttr(plug, 0)
			mc.setKeyframe(plug, t=start_frame)
			mc.keyTangent(plug, t=(start_frame,), itt="step", ott="step")


		# weight = 1 at current frame
		if wattrs:
			plug = "{}.{}".format(con, wattrs)
			mc.setAttr(plug, 1)
			mc.setKeyframe(plug, t=cur)
			mc.keyTangent(plug, t=(cur,), itt="step", ott="step")

		# snap SN
		world_pos = mc.xform(node, q=True, ws=True, t=True)
		world_rot = mc.xform(node, q=True, ws=True, ro=True)
		mc.xform(sn, ws=True, t=world_pos)
		mc.xform(sn, ws=True, ro=world_rot)
		mc.setKeyframe(sn, at=["tx","ty","tz","rx","ry","rz"], t=cur)
		mc.keyTangent(sn, at=["tx","ty","tz","rx","ry","rz"], t=(cur,), itt="step", ott="step")

		if mc.attributeQuery("followPath", node=node, exists=True):
			mc.setAttr(node + ".followPath", 1)

		print("[Attach] {} attached at frame {}".format(node, cur))

	print("[Attach] Done: ALL controllers attached at current frame.")


def release_all_detach_current_frame(namespace=None):
	ctrls = get_slide_ctrls(namespace)
	if not ctrls:
		mc.warning("No controllers found to release.")
		return

	cur = mc.currentTime(q=True)

	for node in ctrls:
		# 1) snapshot world pose ของ ctrl ก่อนดีด
		world_pos = mc.xform(node, q=True, ws=True, t=True)
		world_rot = mc.xform(node, q=True, ws=True, ro=True)

		# bake ctrl at current frame
		mc.bakeResults(node, t=(cur, cur),
					   at=["tx","ty","tz","rx","ry","rz"],
					   simulation=True)

		# 3) disable constraint weight
		con_name = node.replace(":", "_") + "_followPath_PC"
		if mc.objExists(con_name):
			wattrs = mc.parentConstraint(con_name, q=True, weightAliasList=True) or []
			for w in wattrs:
				plug = "{}.{}".format(con_name, w)
				mc.setAttr(plug, 0)
				mc.setKeyframe(plug, t=cur)
				mc.keyTangent(plug, t=(cur,), itt="step", ott="step")

		# 3) snap SN back to world position that kept before
		sn = _get_snap_group(node)
		if mc.objExists(sn):
			mc.xform(sn, ws=True, t=world_pos)
			mc.xform(sn, ws=True, ro=world_rot)
			mc.setKeyframe(sn, at=["tx","ty","tz","rx","ry","rz"], t=cur)
			mc.keyTangent(sn, at=["tx","ty","tz","rx","ry","rz"], t=(cur,), itt="step", ott="step")


		# 4) followPath = 0
		if mc.attributeQuery("followPath", node=node, exists=True):
			mc.setAttr(node + ".followPath", 0)

		print("[Release] {} detached at frame {}".format(node, cur))

	print("[Release] Done: Detached ALL controllers at current frame (weights & SN keyed).")




# ------------------------------- UI bits ------------------------------

def snakePathUI():
	win = "snakePathGhostUI"
	if pm.window(win, q=True, exists=True):
		pm.deleteUI(win)
	with pm.window(win, title=F"{TITLE_NAME}", 	widthHeight=(380, 320),
												sizeable=False,
												minimizeButton=False,
												maximizeButton=False):
		with pm.columnLayout(adjustableColumn=True, rowSpacing=8):
			with pm.rowLayout(nc=3, adjustableColumn=1, columnAlign=(1, "left")):
				pm.text(label="Reference")
				refMenu = pm.optionMenu("refNamespaceMenu", label="")
				pm.button(label="Refresh", c=lambda *_: refreshNamespaces(refMenu))
			pm.separator(h=10, style="in")
			with pm.rowLayout(nc=3, adjustableColumn=1, columnAlign=(1, "left")):
				pm.text(label="Curve Path Name")
				curveField = pm.textField("curvePathField", text="")
				pm.button(label="Set", c=lambda *_: setCurveField(curveField))
			pm.separator(h=10, style="in")
			# pm.button(label="Create Slide Attr", h=26,
			# 		  c=lambda *_: ensure_slide_attrs(getSelectedNamespace()))
			pm.button(label="Build/Update Path Ghosts", h=32,
					  c=lambda *_: build_path_ghosts(curveField, getSelectedNamespace()))
			pm.separator(h=10, style="in")
			pm.button(label="Snap (Follow ON: all ctrls)", h=28,
					  c=lambda *_: attach_all(getSelectedNamespace()))
			with pm.rowLayout(nc=2, adjustableColumn=1, columnAlign=(1, "left")):
				pm.button(label="Release (Detach ALL • Bake Current Frame)", h=30,
						  c=lambda *_: release_all_detach_current_frame(getSelectedNamespace()))

	pm.showWindow(win)


def refreshNamespaces(refMenu):
	pm.optionMenu(refMenu, e=True, dai=True)
	for ns in pm.namespaceInfo(listOnlyNamespaces=True, recurse=False):
		if ns not in ("UI", "shared"):
			pm.menuItem(label=ns, parent=refMenu)

def getSelectedNamespace():
	try:
		return pm.optionMenu("refNamespaceMenu", q=True, v=True)
	except:
		return None

def setCurveField(curveField):
	sel = mc.ls(sl=True, type="transform")
	if not sel: return
	shp = mc.listRelatives(sel[0], s=True) or []
	if not shp: return
	if mc.nodeType(shp[0]) != "nurbsCurve":
		return
	pm.textField(curveField, e=True, text=sel[0])
	print("Curve set:", sel[0])

# ------------------------------ Launch UI -----------------------------
snakePathUI()
