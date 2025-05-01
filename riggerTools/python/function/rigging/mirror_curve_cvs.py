import maya.cmds as mc

def mirror_curve_cvs(curve, right_to_left=True):
	"""
	Mirrors CVs on one side of a curve to the opposite side across the center (X-axis).
	
	Args:
		curve (str): The name of the curve (e.g., 'curve1')
		right_to_left (bool): Direction of mirroring. True = R → L, False = L → R
	"""
	cvs = mc.ls(f'{curve}.cv[*]', flatten=True)
	cv_count = len(cvs)
	mid_index = cv_count // 2

	# Calculate mirror center X (average of center CVs if even)
	if cv_count % 2 == 0:
		x1 = mc.xform(f'{curve}.cv[{mid_index - 1}]', q=True, ws=True, t=True)[0]
		x2 = mc.xform(f'{curve}.cv[{mid_index}]', q=True, ws=True, t=True)[0]
		center_x = (x1 + x2) / 2.0
	else:
		center_x = mc.xform(f'{curve}.cv[{mid_index}]', q=True, ws=True, t=True)[0]

	# Mirror side
	for i in range(0, mid_index):
		src_i = mid_index + i if right_to_left else mid_index - 1 - i
		tgt_i = mid_index - 1 - i if right_to_left else mid_index + i

		source_cv = f'{curve}.cv[{src_i}]'
		target_cv = f'{curve}.cv[{tgt_i}]'

		pos = mc.xform(source_cv, q=True, ws=True, t=True)
		mirrored_x = center_x - (pos[0] - center_x)
		mirrored_pos = [mirrored_x, pos[1], pos[2]]

		mc.xform(target_cv, ws=True, t=mirrored_pos)
