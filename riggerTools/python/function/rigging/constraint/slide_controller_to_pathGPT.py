# Maya Python (PyMEL) — attach one controller to a NURBS curve via motionPath
# Requirements: a controller transform and a NURBS curve shape/path exist.

import pymel.core as pm

def attach_controller_to_path(controller, curve, follow=True):
	"""
	Create an offset group for the controller and drive it by a motionPath.
	The controller remains parented under the offset group for fine animation.

	Args:
		controller (str/pm.nt.Transform): controller transform to attach
		curve (str/pm.nt.Transform/pm.nt.NurbsCurve): NURBS curve used as path
		follow (bool): whether motionPath should align orientation to the curve
	Returns:
		dict: {'offsetGrp': pm.nt.Transform, 'motionPath': pm.nt.MotionPath}
	"""

	# -- Normalize inputs to PyNodes
	ctrl = pm.PyNode(controller)
	crv = pm.PyNode(curve)
	crv_shape = crv.getShape() if crv.nodeType() == 'transform' else crv
	if crv_shape.nodeType() != 'nurbsCurve':
		pm.error('Provided "curve" must be a NURBS curve (shape or transform).')

	# -- Build an offset group snapped to controller's current transform
	#    This lets the controller stay keyable while the offset group follows the path.
	offset_grp = pm.group(em=True, n='{}_mpOffset'.format(ctrl.nodeName()))
	pm.parent(offset_grp, ctrl.getParent())
	tmp = pm.parentConstraint(ctrl, offset_grp, mo=False)  # snap
	pm.delete(tmp)

	# -- Create a motionPath node and connect the curve to it
	mp = pm.createNode('motionPath', n='{}_MP'.format(ctrl.nodeName()))
	crv_shape.worldSpace.connect(mp.geometryPath)

	# -- Find closest U on the curve from the offset group world position
	#    Use decomposeMatrix -> nearestPointOnCurve (NPOC) to get parameterU
	decomp = pm.createNode('decomposeMatrix', n='{}_DECOMP'.format(ctrl.nodeName()))
	npoc  = pm.createNode('nearestPointOnCurve', n='{}_NPOC'.format(ctrl.nodeName()))
	crv_shape.worldSpace.connect(npoc.inputCurve)
	offset_grp.worldMatrix.connect(decomp.inputMatrix)
	decomp.outputTranslate.connect(npoc.inPosition)

	# -- Initialize the motionPath's U value to that closest parameter
	u = npoc.result.parameter.get()
	mp.uValue.set(u)

	# -- Drive the offset group by the motionPath (position + orientation)
	#    NOTE: motionPath provides allCoordinates (vector) and rotate (Euler)
	mp.allCoordinates.connect(offset_grp.translate)
	mp.rotate.connect(offset_grp.rotate)
	mp.follow.set(bool(follow))

	# -- Parent controller under the offset group so animator can still key it
	pm.parent(ctrl, offset_grp)

	# -- Cleanup helper nodes (optional; we only needed them to compute initial U)
	pm.delete([decomp, npoc])

	return {'offsetGrp': offset_grp, 'motionPath': mp}

# Example usage:
# attach_controller_to_path('C_snakeCtrl_05', 'C_snakePath_CRV', follow=True)
