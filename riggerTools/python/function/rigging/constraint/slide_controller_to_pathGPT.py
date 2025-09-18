# Maya Python (PyMEL)
# Attach MULTIPLE controllers to one curve + one shared slide_ctrl
# Each controller gets its own offsetGrp + motionPath + ADL
# All ADL.input2 connect to ONE shared multiplyDivide (slide_ctrl.pathSlide * pathScale)

import pymel.core as pm

def get_or_create_shared_scale_md(slide_ctrl, slide_attr='pathSlide', scale_attr='pathScale',
								  md_name='SlideScale_MD'):
	"""
	Ensure one shared multiplyDivide exists:
	  md.outputX = slide_ctrl.pathSlide * slide_ctrl.pathScale
	Returns the md node.
	"""
	slide = pm.PyNode(slide_ctrl)

	# Ensure attrs exist
	if not slide.hasAttr(slide_attr):
		slide.addAttr(slide_attr, at='double', k=True); slide.attr(slide_attr).set(0.0)
	if not slide.hasAttr(scale_attr):
		slide.addAttr(scale_attr, at='double', k=True, min=0.0); slide.attr(scale_attr).set(0.01)

	# Reuse if already present
	if pm.objExists(md_name):
		md = pm.PyNode(md_name)
	else:
		md = pm.createNode('multiplyDivide', n=md_name)

	# Wire: pathSlide * pathScale
	if not slide.attr(slide_attr).isConnectedTo(md.input1X):
		slide.attr(slide_attr).connect(md.input1X, f=True)
	if not slide.attr(scale_attr).isConnectedTo(md.input2X):
		slide.attr(scale_attr).connect(md.input2X, f=True)

	return md


def attach_ctrls_with_shared_scale(controllers, curve, slide_ctrl,
								   slide_attr='pathSlide', scale_attr='pathScale',
								   shared_md_name='SlideScale_MD', follow=True):
	"""
	Attach a LIST of controllers to the curve with one shared slide_ctrl.
	Returns dict of results for all controllers.
	"""
	crv = pm.PyNode(curve)
	crv_shape = crv.getShape() if crv.nodeType() == 'transform' else crv
	if crv_shape.nodeType() != 'nurbsCurve':
		pm.error('Argument "curve" must be a NURBS curve.')

	shared_md = get_or_create_shared_scale_md(slide_ctrl, slide_attr, scale_attr, shared_md_name)

	results = {}
	for controller in controllers:
		ctrl = pm.PyNode(controller)

		# Offset group
		offset_grp = pm.group(em=True, n='{}_mpOffset'.format(ctrl.nodeName()))
		pm.parent(offset_grp, ctrl.getParent())

		# Motion path
		mp = pm.createNode('motionPath', n='{}_MP'.format(ctrl.nodeName()))
		crv_shape.worldSpace.connect(mp.geometryPath)
		mp.fractionMode.set(True)
		mp.follow.set(bool(follow))
		mp.allCoordinates.connect(offset_grp.translate)
		mp.rotate.connect(offset_grp.rotate)

		# Closest U
		decomp = pm.createNode('decomposeMatrix', n='{}_DECOMP'.format(ctrl.nodeName()))
		npoc   = pm.createNode('nearestPointOnCurve', n='{}_NPOC'.format(ctrl.nodeName()))
		crv_shape.worldSpace.connect(npoc.inputCurve)
		ctrl.worldMatrix.connect(decomp.inputMatrix)
		decomp.outputTranslate.connect(npoc.inPosition)
		base_u = npoc.result.parameter.get()

		# Store baseU
		if not offset_grp.hasAttr('baseU'):
			offset_grp.addAttr('baseU', at='double', k=True)
		offset_grp.baseU.set(base_u)

		# ADL
		adl = pm.createNode('addDoubleLinear', n='{}_U_ADL'.format(ctrl.nodeName()))
		offset_grp.baseU.connect(adl.input1)
		shared_md.outputX.connect(adl.input2, f=True)

		# Drive mp.uValue
		adl.output.connect(mp.uValue)

		# Parent controller
		pm.parent(ctrl, offset_grp)

		# Cleanup
		pm.delete([decomp, npoc])

		results[ctrl.nodeName()] = {'offsetGrp': offset_grp, 'motionPath': mp, 'adl': adl}

	return results


# Example usage:
# attach_ctrls_with_shared_scale(
# 	['cv01_nrb','cv02_nrb','cv03_nrb','cv04_nrb','cv05_nrb','cv06_nrb','cv07_nrb','cv08_nrb'],
# 	'path01_crv',
# 	'slide_ctrl',
# 	slide_attr='pathSlide',
# 	scale_attr='pathScale',
# 	follow=True
# )



# for ctrl, nodes in res.items():
#     print("Controller:", ctrl)
#     print("  ADL:", nodes['adl'])
#     print("  MotionPath:", nodes['motionPath'])
#     print("  OffsetGrp:", nodes['offsetGrp'])
