import maya.cmds as mc
import re

# --- NEW ---
# We import MirrorTable to mirror ANIMATION curves (Studio Library–style).
from function.animation.studiolibrary_mirrortable import MirrorTable, MirrorPlane, MirrorOption, KeysOption



# -------------------------
# UI callbacks
# -------------------------
def _mirror_ctrl_do():
	"""Collect UI values and call mirror_selection()."""
	# Axes toggles (used to infer the mirror plane)
	tX = mc.checkBox('mc_tX', q=True, v=True)
	tY = mc.checkBox('mc_tY', q=True, v=False)
	tZ = mc.checkBox('mc_tZ', q=True, v=False)
	rX = mc.checkBox('mc_rX', q=True, v=False)
	rY = mc.checkBox('mc_rY', q=True, v=False)
	rZ = mc.checkBox('mc_rZ', q=True, v=False)
	sX = mc.checkBox('mc_sX', q=True, v=False)
	sY = mc.checkBox('mc_sY', q=True, v=False)
	sZ = mc.checkBox('mc_sZ', q=True, v=False)

	include_hierarchy       = mc.checkBox('mc_hie', q=True, v=True)
	prefer_left             = mc.checkBox('mc_prefL', q=True, v=True)
	skip_if_target_selected = mc.checkBox('mc_skipT', q=True, v=True)
	only_ctrl_suffix        = mc.textField('mc_suffix', q=True, text=True).strip() or None

	# Infer mirror plane from Translate axis toggles (simple heuristic).
	mirror_plane = infer_mirror_plane_from_axes(tX, tY, tZ)

	try:
		result = mirror_selection(
			mirror_plane=mirror_plane,               # <-- NEW: pass plane
			mirror_translate=(tX, tY, tZ),           # kept for UI parity (not used by MirrorTable math)
			mirror_rotate=(rX, rY, rZ),              # kept for UI parity
			mirror_scale=(sX, sY, sZ),               # kept for UI parity
			prefer_left=prefer_left,
			skip_if_target_selected=skip_if_target_selected,
			include_hierarchy=include_hierarchy,
			only_ctrl_suffix=only_ctrl_suffix
		)
		# Pretty print to UI log
		lines = []
		lines.append("=== Mirror Summary ===")
		lines.append(f"Plane: {result.get('plane_label','YZ')}  | Option: swap  | Keys: All Keys")
		lines.append(f"Left token:  {result.get('left_token','')}")
		lines.append(f"Right token: {result.get('right_token','')}")
		if result['done']:
			lines.append("Done:")
			lines += [f"  {s} -> {t}" for s, t in result['done']]
		if result['skipped']:
			lines.append("Skipped:")
			lines += [f"  {s} ({reason})" for s, reason in result['skipped']]
		if result['errors']:
			lines.append("Errors:")
			lines += [f"  {s} -> {t} [{reason}]" for s, t, reason in result['errors']]
		mc.scrollField('mc_log', e=True, tx="\n".join(lines))
	except Exception as e:
		mc.scrollField('mc_log', e=True, it=True, ip=True)
		mc.scrollField('mc_log', e=True, a=True, tx=f"\nException: {e}\n")
		raise


# -------------------------
# Build UI
# -------------------------
def mirror_ctrl_ui():
	"""Create the 'Mirror Ctrl' window."""
	win = 'MirrorCtrlWin'
	if mc.window(win, exists=True):
		mc.deleteUI(win)

	mc.window(win, title='Mirror Ctrl', sizeable=False, mnb=False, mxb=False)
	mc.columnLayout(adj=True, rs=6)

	# Hierarchy toggle
	mc.checkBox('mc_hie', l='Hierarchy (scan under selection & family-match)', v=True)

	# Axes group (Translate is used to infer mirror plane)
	mc.frameLayout(l='Axes to Invert (Translate decides mirror plane)', collapsable=True, cl=False, mw=6, mh=6)
	mc.rowLayout(nc=10, adj=1)
	mc.text(l='Translate:', al='right', w=120)
	mc.checkBox('mc_tX', l='X', v=True)
	mc.checkBox('mc_tY', l='Y', v=False)
	mc.checkBox('mc_tZ', l='Z', v=False)
	mc.setParent('..')
	mc.rowLayout(nc=10, adj=1)
	mc.text(l='Rotate:', al='right', w=120)
	mc.checkBox('mc_rX', l='X', v=False)
	mc.checkBox('mc_rY', l='Y', v=False)
	mc.checkBox('mc_rZ', l='Z', v=False)
	mc.setParent('..')
	mc.rowLayout(nc=10, adj=1)
	mc.text(l='Scale:', al='right', w=120)
	mc.checkBox('mc_sX', l='X', v=False)
	mc.checkBox('mc_sY', l='Y', v=False)
	mc.checkBox('mc_sZ', l='Z', v=False)
	mc.setParent('..')
	mc.setParent('..')  # end frame

	# Options
	mc.frameLayout(l='Options', collapsable=True, cl=False, mw=6, mh=6)
	mc.checkBox('mc_prefL', l='Prefer Left → Right (skip R when both sides selected)', v=True)
	mc.checkBox('mc_skipT', l='Skip if target is also selected', v=True)
	mc.rowLayout(nc=2, cw2=(140, 200))
	mc.text(l='Only names ending with:')
	mc.textField('mc_suffix', text='_ctrl')
	mc.setParent('..')
	mc.setParent('..')

	# Mirror button
	mc.button(l='Mirror Ctrl', h=36, bgc=(0.35, 0.55, 0.85), c=lambda *_: _mirror_ctrl_do())

	# Log field
	mc.scrollField('mc_log', ed=False, ww=True, h=160,
				   tx='Ready.\nSelect controllers and press "Mirror Ctrl".\n'
					  '- Translate X only ⇒ YZ plane (typical for L/R)\n'
					  '- Translate Y only ⇒ XZ plane\n'
					  '- Translate Z only ⇒ XY plane\n'
					  '- Otherwise ⇒ YZ plane')

	mc.showWindow(win)


# -------------------------
# Helpers (naming)
# -------------------------
def split_namespace(name):
	"""
	Split namespace from node.
	Example:
	  "char1:sub:L_arm_ctrl" -> ("char1:sub", "L_arm_ctrl")
	  "L_arm_ctrl"           -> ("", "L_arm_ctrl")
	"""
	ns, _, short = name.rpartition(':')
	return ns, short

def join_namespace(ns, short):
	"""Join namespace and short name back."""
	return f"{ns}:{short}" if ns else short

def strip_side_tokens(short):
	"""Remove side markers (L/R/C or LFT/RGT) for family key creation."""
	parts = short.split('_')
	if len(parts) == 1:
		return parts
	if parts[0] in {'L', 'R', 'C'}:
		return parts[1:]
	out = parts[:]
	for i, tk in enumerate(out):
		if tk.endswith('LFT'):
			out[i] = re.sub(r'LFT$', '', tk); break
		if tk.endswith('RGT'):
			out[i] = re.sub(r'RGT$', '', tk); break
	return out

def family_key(name):
	"""
	Build family key ignoring side and digits.
	Example:
	  "char1:L_tenFRT02_masterFk_ctrl" -> "tenFRT##_masterFk_ctrl"
	"""
	_, short = split_namespace(name)
	tokens = strip_side_tokens(short)
	norm = [re.sub(r'\d+', '##', t) for t in tokens]
	return '_'.join(norm)

def check_name_style(name):
	"""
	Detect side and build opposite name (short name only, no namespace).
	"""
	_, short = split_namespace(name)
	parts = short.split('_')
	if len(parts) == 1:
		mc.error(f"Naming must contain underscores: {short}")

	base_name = '_'.join(parts[:-1])
	side, reverse_side, name_reverse_side = None, None, None

	# Capital-lead
	if parts[0] in {'L', 'R', 'C'}:
		side = parts[0]
		reverse_side = {'L':'R','R':'L','C':'C'}[side]
		swapped = [reverse_side] + parts[1:]
		name_reverse_side = '_'.join(swapped)

	# Suffix style
	else:
		token_idx = -1
		for i, tk in enumerate(parts):
			if tk.endswith('LFT'): side,reverse_side,token_idx='LFT','RGT',i; break
			if tk.endswith('RGT'): side,reverse_side,token_idx='RGT','LFT',i; break
		if token_idx>=0:
			new_parts=parts[:]
			new_parts[token_idx]=re.sub(side+'$',reverse_side,new_parts[token_idx])
			name_reverse_side='_'.join(new_parts)

	return base_name, side, reverse_side, name_reverse_side


# -------------------------
# Plane inference
# -------------------------
def infer_mirror_plane_from_axes(tx, ty, tz):
	"""
	Decide mirror plane from Translate axis toggles.
	- X only  -> YZ (typical left/right)
	- Y only  -> XZ
	- Z only  -> XY
	- Others  -> YZ (fallback)
	"""
	if tx and not ty and not tz:
		return 'YZ'
	if ty and not tx and not tz:
		return 'XZ'
	if tz and not tx and not ty:
		return 'XY'
	return 'YZ'


# -------------------------
# Core: mirror animation using MirrorTable
# -------------------------
def mirror_selection(mirror_plane='YZ',
					 mirror_translate=(True, True, True),
					 mirror_rotate=(False, False, False),
					 mirror_scale=(False, False, False),
					 prefer_left=True,
					 skip_if_target_selected=True,
					 include_hierarchy=False,
					 only_ctrl_suffix='_ctrl'):
	"""
	Mirror ANIMATION KEYS for all selected controllers (Studio Library–style).
	- Builds a MirrorTable from current selection (plus hierarchy if requested).
	- Auto-detects left/right tokens from names (supports L/R or LFT/RGT).
	- Uses KeysOption.All to ensure real animation mirroring (not static pose).
	- Respects namespace; swapping is done via MirrorTable.load(option='swap').
	"""
	sel = mc.ls(sl=True, type='transform') or []
	if not sel:
		mc.error("Please select one or more controllers.")

	# Expand hierarchy if requested, and filter by suffix if provided.
	if include_hierarchy:
		expanded = []
		for root in sel:
			if not mc.objExists(root):
				continue
			nodes = mc.listRelatives(root, ad=True, type="transform") or []
			nodes.append(root)
			for n in nodes:
				if only_ctrl_suffix and not n.endswith(only_ctrl_suffix):
					continue
				expanded.append(n)
		sel = list(dict.fromkeys(expanded))
	else:
		if only_ctrl_suffix:
			sel = [n for n in sel if n.endswith(only_ctrl_suffix)]

	# Auto-detect tokens for left/right once from the working set.
	left_token  = MirrorTable.findLeftSide(sel)
	right_token = MirrorTable.findRightSide(sel)

	# Build MirrorPlane constant
	plane_label = (mirror_plane or 'YZ').upper()
	plane_map = {'YZ': MirrorPlane.YZ, 'XZ': MirrorPlane.XZ, 'XY': MirrorPlane.XY}
	plane_const = plane_map.get(plane_label, MirrorPlane.YZ)

	# Construct MirrorTable from selection.
	mt = MirrorTable.fromObjects(
		sel,
		leftSide=left_token,
		rightSide=right_token,
		mirrorPlane=plane_const
	)

	# Optional: filter selection to prefer left when both sides are selected.
	filtered = list(sel)
	if prefer_left or skip_if_target_selected:
		# Map each selected node to its opposite (namespace-aware).
		selected_set = set(filtered)
		to_skip = set()
		for src in filtered:
			# Compute opposite by asking the table (uses detected tokens)
			opp = mt.mirrorObject(src) or src
			if skip_if_target_selected and opp in selected_set and src in selected_set:
				# If both sides selected, drop the "target" to avoid double-processing
				# Prefer dropping the right-hand side when both present.
				_, side, _, _ = check_name_style(src)
				if prefer_left and side in ('R', 'RGT'):
					to_skip.add(src)
		filtered = [n for n in filtered if n not in to_skip]

	# Perform the actual animation mirroring:
	# - option='swap' (can be 'left to right' or 'right to left' if you prefer)
	# - keysOption=All to ensure real animation curves are mirrored
	mt.load(
		objects=filtered,
		option=MirrorOption.Swap,
		keysOption=KeysOption.All
	)

	# Compose a lightweight summary (we don't get per-curve results from MirrorTable).
	done = []
	skipped = []
	errors = []
	for src in filtered:
		opp = mt.mirrorObject(src) or src
		if mc.objExists(opp):
			done.append((src, opp))
		else:
			errors.append((src, opp, "Opposite not found"))

	# Anything we filtered out due to options is considered "skipped".
	for src in set(sel) - set(filtered):
		skipped.append((src, "Skipped by prefer_left/skip_target_selected"))

	return {
		"done": done,
		"skipped": skipped,
		"errors": errors,
		"left_token": left_token,
		"right_token": right_token,
		"plane_label": plane_label
	}


# -------------------------
# (Old) simple pose mirror kept here for reference (not used anymore)
# -------------------------
def mirror_simple(ctrl,
				  mirror_translate=(True, True, True),
				  mirror_rotate=(False, False, False),
				  mirror_scale=(False, False, False)):
	"""
	Legacy: Mirror transform values from a source controller to its opposite-side controller.
	Kept for reference; current pipeline uses MirrorTable for animation keys.
	"""
	if not mc.objExists(ctrl):
		return False, None, f"Not found: {ctrl}"

	ns, short = split_namespace(ctrl)
	_, side, _, short_target = check_name_style(ctrl)

	if side == 'C':
		return False, None, f"Center object skipped: {ctrl}"
	if not short_target:
		return False, None, f"No opposite name computed: {ctrl}"

	target = join_namespace(ns, short_target)
	if not mc.objExists(target):
		return False, target, f"Opposite not found: {target}"

	try:
		for i, axis in enumerate("XYZ"):
			val = mc.getAttr(f"{ctrl}.translate{axis}")
			if mirror_translate[i]: val *= -1.0
			mc.setAttr(f"{target}.translate{axis}", val)
		for i, axis in enumerate("XYZ"):
			val = mc.getAttr(f"{ctrl}.rotate{axis}")
			if mirror_rotate[i]: val *= -1.0
			mc.setAttr(f"{target}.rotate{axis}", val)
		for i, axis in enumerate("XYZ"):
			val = mc.getAttr(f"{ctrl}.scale{axis}")
			if mirror_scale[i]: val *= -1.0
			mc.setAttr(f"{target}.scale{axis}", val)

		return True, target, f"Mirror {ctrl} >>> {target}"
	except Exception as e:
		return False, target, f"Failed: {ctrl} -> {target} ({e})"


# Build UI on import (same behavior as your original file)
mirror_ctrl_ui()
