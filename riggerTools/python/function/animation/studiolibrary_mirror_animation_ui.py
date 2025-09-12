# Mirror Animation UI (Studio Library–style)
# - UI fields: Mirror plane, Left token, Right token, Controller pattern, Respect namespace
# - Buttons: Select all controller, Swap
# - Defaults: plane=YZ, left='L_*', right='R_*', controller='*_ctrl',
#             direction='swap', keys='All Keys'
#
# Comments are in English as requested.

import re
import maya.cmds as mc
from function.animation.studiolibrary_mirrortable import MirrorTable, MirrorPlane, MirrorOption, KeysOption



# -----------------------------
# Helpers: names & matching
# -----------------------------
def split_namespace(name):
	"""Return (namespace, short_name)."""
	ns, _, short = name.rpartition(':')
	return ns, short

def short_name(node):
	"""Return node name without namespace."""
	return split_namespace(node)[1]

def match_token(short, token):
	"""
	Match a short name against a side token.
	Token semantics:
	  - 'L_*' => prefix 'L_'
	  - '*LFT' => suffix 'LFT'
	  - 'L' (no *) => substring 'L'
	"""
	if not token:
		return False
	if token.endswith('*'):                 # prefix style e.g. 'L_*'
		pref = token[:-1]
		return short.startswith(pref)
	if token.startswith('*'):               # suffix style e.g. '*LFT'
		suf = token[1:]
		return short.endswith(suf)
	return token in short                   # fallback: contains

def match_pattern(short, pattern):
	"""
	Controller pattern matching with simple wildcard support:
	  '*_ctrl' => endswith '_ctrl'
	  'C_*'    => startswith 'C_'
	  '*fk*'   => contains 'fk'
	  'exact'  => exact
	"""
	if pattern.startswith('*') and pattern.endswith('*') and len(pattern) > 2:
		return pattern[1:-1] in short
	if pattern.startswith('*'):
		return short.endswith(pattern[1:])
	if pattern.endswith('*'):
		return short.startswith(pattern[:-1])
	return short == pattern

def to_mirror_plane(label):
	"""Map string label to MirrorPlane constant."""
	label = (label or 'YZ').upper()
	return {'YZ': MirrorPlane.YZ, 'XZ': MirrorPlane.XZ, 'XY': MirrorPlane.XY}.get(label, MirrorPlane.YZ)


# -----------------------------
# Core ops
# -----------------------------
def select_all_controllers(ctrl_pattern='*_ctrl', respect_namespace=False):
	"""
	Select all controllers that match ctrl_pattern for the same asset(s) as current selection.
	- Ignores left/right tokens entirely.
	- If respect_namespace=True, restrict to namespaces found in the current selection.
	- If respect_namespace=False, match across the whole scene.
	"""
	sel = mc.ls(sl=True, type='transform') or []
	if not sel:
		mc.warning("Select any controller(s) of the asset first, then press 'Select all controller'.")
		return []

	# Gather namespaces from current selection
	selected_ns = set()
	for n in sel:
		ns, _ = split_namespace(n)
		selected_ns.add(ns)  # '' means no namespace

	# Collect all transform nodes and filter by pattern
	all_transforms = mc.ls(type='transform') or []
	hits = []
	for n in all_transforms:
		s = short_name(n)
		if match_pattern(s, ctrl_pattern):
			if respect_namespace:
				ns, _ = split_namespace(n)
				if ns in selected_ns:       # only namespaces present in selection
					hits.append(n)
			else:
				hits.append(n)

	# Deduplicate while preserving order
	hits = list(dict.fromkeys(hits))

	if hits:
		mc.select(hits, r=True)
	else:
		mc.select(clear=True)
		mc.warning("No controllers matched the pattern in the current context.")
	return hits


def run_swap(mirror_plane='YZ',
			 left_token='L_*',
			 right_token='R_*',
			 ctrl_pattern='*_ctrl',
			 respect_namespace=False):
	"""
	Mirror ANIMATION (All Keys) using MirrorTable, option='swap'.
	- If respect_namespace is False, we pass namespaces=[] so matching ignores namespaces.
	"""
	sel = mc.ls(sl=True, type='transform') or []
	if not sel:
		mc.error("Please select controllers or press 'Select all controller' first.")

	# Filter current selection by controller pattern
	sel = [n for n in sel if match_pattern(short_name(n), ctrl_pattern)]
	if not sel:
		mc.error("Selected items do not match controller pattern.")

	# Build MirrorTable from selection using user-provided tokens and plane.
	mt = MirrorTable.fromObjects(
		sel,
		leftSide=left_token,
		rightSide=right_token,
		mirrorPlane=to_mirror_plane(mirror_plane)
	)

	# When not respecting namespaces, explicitly pass namespaces=[]
	kwargs = dict(
		objects=sel,
		option=MirrorOption.Swap,       # direction='swap'
		keysOption=KeysOption.All       # keys='All Keys'
	)
	if not respect_namespace:
		kwargs['namespaces'] = []

	# Execute mirror transfer
	mt.load(**kwargs)

	# Lightweight feedback in Script Editor
	print("[Mirror] Done.",
		  "Plane:", mirror_plane,
		  "| Direction: swap | Keys: All Keys",
		  "| Left token:", left_token,
		  "| Right token:", right_token)


# -----------------------------
# UI
# -----------------------------
def mirror_anim_ui():
	"""Build the requested UI."""
	win = 'MirrorAnimUI'
	if mc.window(win, exists=True):
		mc.deleteUI(win)

	mc.window(win, title='Mirror Animation', sizeable=False, mnb=False, mxb=False)
	mc.columnLayout(adj=True, rs=6, cw=380)

	# Mirror plane (drop down)
	mc.rowLayout(nc=2, cw2=(110, 250))
	mc.text(l='Mirror plane', al='right')
	mc.optionMenu('ui_plane')
	for lbl in ('YZ', 'XZ', 'XY'):
		mc.menuItem(l=lbl)
	mc.optionMenu('ui_plane', e=True, v='YZ')   # default
	mc.setParent('..')

	# Left / Right token
	mc.rowLayout(nc=3, cw3=(110, 220, 50))
	mc.text(l='Left token', al='right')
	mc.textField('ui_left', tx='L_*')          # default
	mc.text(l='(text field)')
	mc.setParent('..')

	mc.rowLayout(nc=3, cw3=(110, 220, 50))
	mc.text(l='Right token', al='right')
	mc.textField('ui_right', tx='R_*')         # default
	mc.text(l='(text field)')
	mc.setParent('..')

	# Controller pattern
	mc.rowLayout(nc=3, cw3=(110, 220, 50))
	mc.text(l='Controller', al='right')
	mc.textField('ui_ctrl', tx='*_ctrl')       # default
	mc.text(l='(text field)')
	mc.setParent('..')

	# Respect namespace
	mc.checkBox('ui_ns', l='Respect namespace', v=False)  # default unchecked as in sketch

	mc.separator(h=8, style='in')

	# Select all controller
	def _on_select_all(*_):
		ctrl  = mc.textField('ui_ctrl',  q=True, tx=True).strip()
		respect_ns = mc.checkBox('ui_ns', q=True, v=True)
		select_all_controllers(ctrl_pattern=ctrl or '*_ctrl',
											  respect_namespace=respect_ns)


	mc.button(l='Select all controller', h=34, bgc=(0.55, 0.55, 0.55), c=_on_select_all)

	# Swap (mirror All Keys)
	def _on_swap(*_):
		plane = mc.optionMenu('ui_plane', q=True, v=True)
		left  = mc.textField('ui_left',  q=True, tx=True).strip()
		right = mc.textField('ui_right', q=True, tx=True).strip()
		ctrl  = mc.textField('ui_ctrl',  q=True, tx=True).strip()
		respect_ns = mc.checkBox('ui_ns', q=True, v=True)
		run_swap(mirror_plane=plane,
				 left_token=left,
				 right_token=right,
				 ctrl_pattern=ctrl,
				 respect_namespace=respect_ns)

	mc.button(l='Swap', h=34, bgc=(0.35, 0.55, 0.85), c=_on_swap)

	mc.separator(h=4, style='none')
	mc.showWindow(win)


# Build UI immediately
mirror_anim_ui()
