
# Mirror animation for selected controllers (Studio Library–style)
# Comments are in English as requested.

import maya.cmds as mc
from function.animation.studiolibrary_mirrortable import MirrorTable, MirrorPlane, MirrorOption, KeysOption

def mirror_animation_timeRange(
	mirror_plane='YZ',                 # 'YZ', 'XZ', or 'XY'
	direction='swap',                  # 'swap' | 'left to right' | 'right to left'
	keys='All Keys',             # 'Selected Range' | 'All Keys'
	left_token=None,                   # e.g. 'L' or 'LFT*' (prefix add *; suffix put * at start: '*LFT')
	right_token=None,                  # e.g. 'R' or 'RGT*'
	respect_namespaces=True            # keep namespaces as-is
):
	"""
	Mirror animation keys for the currently selected controllers using mutils.MirrorTable.
	- Auto-detects left/right tokens if not provided.
	- Uses mirror plane to compute axis sign-flips per-controller.
	- Honors 'Selected Range' or 'All Keys' just like Studio Library.

	Usage:
		# 1) Select your L/R controls (you can select both sides).
		# 2) Call:
		mirror_animation_timeRange(
			mirror_plane='YZ',
			direction='swap',
			keys='Selected Range',
			left_token='L', right_token='R'        # or left_token='LFT*', right_token='RGT*'
		)
	"""

	sel = mc.ls(sl=True) or []
	if not sel:
		mc.error("Please select one or more controllers to mirror.")

	# Resolve mirror plane constant
	plane = {'YZ': MirrorPlane.YZ, 'XZ': MirrorPlane.XZ, 'XY': MirrorPlane.XY}.get(mirror_plane.upper(), MirrorPlane.YZ)

	# Auto-detect left/right tokens if not provided (same helpers Studio Library uses)
	if not left_token:
		left_token = MirrorTable.findLeftSide(sel)     # detects prefix/suffix and returns token with '*' if needed
	if not right_token:
		right_token = MirrorTable.findRightSide(sel)

	# Build a MirrorTable directly from the current selection and metadata
	mt = MirrorTable.fromObjects(
		sel,
		leftSide=left_token,
		rightSide=right_token,
		mirrorPlane=plane
	)

	# Prepare load() options (same surface as Studio Library’s load dialog)
	opt = direction                       # accepts string 'swap'/'left to right'/'right to left'
	keys_opt = KeysOption.SelectedRange if keys == 'Selected Range' else KeysOption.All

	# If you want to restrict mirroring to selection and keep namespaces untouched,
	# just pass 'objects=sel' and don't pass 'namespaces'.
	kwargs = {'objects': sel, 'option': opt, 'keysOption': keys_opt}
	if not respect_namespaces:
		# You could supply custom namespaces here; leaving empty keeps them as-is.
		kwargs['namespaces'] = []

	# Do the actual mirror transfer (animation or pose) — this is the heavy lifting.
	mt.load(**kwargs)

	print("[Mirror] Done.",
		  "Plane:", mirror_plane,
		  "| Direction:", direction,
		  "| Keys:", keys,
		  "| Left token:", left_token,
		  "| Right token:", right_token)




mirror_animation_timeRange(
	mirror_plane='YZ',                 # 'YZ', 'XZ', or 'XY'
	direction='swap',                  # 'swap' | 'left to right' | 'right to left'
	keys='All Keys',             # 'Selected Range' | 'All Keys'
	left_token='L_*',                   # e.g. 'L' or 'LFT*' (prefix add *; suffix put * at start: '*LFT')
	right_token='R_*',                  # e.g. 'R' or 'RGT*'
	respect_namespaces=True            # keep namespaces as-is
)