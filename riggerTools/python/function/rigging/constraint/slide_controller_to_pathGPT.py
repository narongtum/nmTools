# Maya Python (PyMEL) — attach one controller to a NURBS curve via motionPath
# Snap the offset group to the nearest point on the path immediately (no maintain offset).

import pymel.core as pm

def attach_ctrl_snap_to_path(controller, curve, follow=True):
	"""
	Create an offset group above the controller and drive it by a motionPath.
	The offset group snaps to the nearest U on the curve immediately (no maintain offset).
	"""
	# -- Normalize inputs
	ctrl = pm.PyNode(controller)
	crv  = pm.PyNode(curve)
	crv_shape = crv.getShape() if crv.nodeType() == 'transform' else crv
	if crv_shape.nodeType() != 'nurbsCurve':
		pm.error('Provided "curve" must be a NURBS curve (shape or transform).')

	# -- Build an empty offset group under the controller's current parent
	offset_grp = pm.group(em=True, n='{}_mpOffset'.format(ctrl.nodeName()))
	pm.parent(offset_grp, ctrl.getParent())  # no snapping to the controller (we want snap to the curve)

	# -- Create a motionPath and connect the curve to it
	mp = pm.createNode('motionPath', n='{}_MP'.format(ctrl.nodeName()))
	crv_shape.worldSpace.connect(mp.geometryPath)

	# -- Find closest parameterU on the curve from the controller's world position
	#    (decomposeMatrix -> nearestPointOnCurve), then set motionPath.uValue
	decomp = pm.createNode('decomposeMatrix', n='{}_DECOMP'.format(ctrl.nodeName()))
	npoc  = pm.createNode('nearestPointOnCurve', n='{}_NPOC'.format(ctrl.nodeName()))
	crv_shape.worldSpace.connect(npoc.inputCurve)
	ctrl.worldMatrix.connect(decomp.inputMatrix)           # use controller's world position as query point
	decomp.outputTranslate.connect(npoc.inPosition)
	u = npoc.result.parameter.get()
	mp.uValue.set(u)

	# -- Drive the offset group by the motionPath (position + orientation)
	mp.allCoordinates.connect(offset_grp.translate)        # vector -> translate
	mp.rotate.connect(offset_grp.rotate)                   # euler  -> rotate
	mp.follow.set(bool(follow))                            # align to curve tangent/normal

	# -- Parent the controller under the offset group so animator can still key it
	pm.parent(ctrl, offset_grp)

	# -- Cleanup helper nodes (only needed for initial U computation)
	pm.delete([decomp, npoc])

	return {'offsetGrp': offset_grp, 'motionPath': mp}

# Example:
# attach_ctrl_snap_to_path('C_snakeCtrl_05', 'C_snakePath_CRV', follow=True)
