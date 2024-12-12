"""
Functions for generating spline weights.

Usage:
	This modules functions each take curve parameters and output control point weights. The weights are generated using
	a modified version of de Boor's algorithm. These weights can be used to create a weighted sum to find a point or 
	tangent on a spline.
	
	While these functions are written for usage in Autodesk Maya, they don't actually have any Maya-specific libraries.
	Additionally none of these functions actually care about the data type of provided control points. This way these
	functions can support points or matrices or Maya attribute names. The output mapping will use the same control
	point that were provided.

Examples:
	This module does include some Maya examples at the very end. These example functions are intended to be used for 
	testing or serve as a starting point for use elsewhere. They are not designed to be functional auto-riggers.
"""


def defaultKnots(count, degree=3):
	"""
	Gets a default knot vector for a given number of cvs and degrees.

	Args:
		count(int): The number of cvs. 
		degree(int): The curve degree. 

	Returns:
		list: A list of knot values.
	"""
	knots = [0 for i in range(degree)] + [i for i in range(count - degree + 1)]
	knots += [count - degree for i in range(degree)]
	return [float(knot) for knot in knots]


def pointOnCurveWeights(cvs, t, degree, knots=None):
	"""
	Creates a mapping of cvs to curve weight values on a spline curve.
	While all cvs are required, only the cvs with non-zero weights will be returned.
	This function is based on de Boor's algorithm for evaluating splines and has been modified to consolidate weights.

	Args:
		cvs(list): A list of cvs, these are used for the return value.
		t(float): A parameter value. 
		degree(int): The curve dimensions. 
		knots(list): A list of knot values. 

	Returns:
		list: A list of control point, weight pairs.
	"""

	order = degree + 1  # Our functions often use order instead of degree
	if len(cvs) <= degree:
		raise CurveException('Curves of degree %s require at least %s cvs' % (degree, degree + 1))

	knots = knots or defaultKnots(len(cvs), degree)  # Defaults to even knot distribution
	if len(knots) != len(cvs) + order:
		raise CurveException('Not enough knots provided. Curves with %s cvs must have a knot vector of length %s. '
							 'Received a knot vector of length %s: %s. '
							 'Total knot count must equal len(cvs) + degree + 1.' % (len(cvs), len(cvs) + order,
																					 len(knots), knots))

	# Convert cvs into hash-able indices
	_cvs = cvs
	cvs = [i for i in range(len(cvs))]

	# Remap the t value to the range of knot values.
	min = knots[order] - 1
	max = knots[len(knots) - 1 - order] + 1
	t = (t * (max - min)) + min

	# Determine which segment the t lies in
	segment = degree
	for index, knot in enumerate(knots[order:len(knots) - order]):
		if knot <= t:
			segment = index + order

	# Filter out cvs we won't be using
	cvs = [cvs[j + segment - degree] for j in range(0, degree + 1)]

	# Run a modified version of de Boors algorithm
	cvWeights = [{cv: 1.0} for cv in cvs]
	for r in range(1, degree + 1):
		for j in range(degree, r - 1, -1):
			right = j + 1 + segment - r
			left = j + segment - degree
			alpha = (t - knots[left]) / (knots[right] - knots[left])

			weights = {}
			for cv, weight in cvWeights[j].items():
				weights[cv] = weight * alpha

			for cv, weight in cvWeights[j - 1].items():
				if cv in weights:
					weights[cv] += weight * (1 - alpha)
				else:
					weights[cv] = weight * (1 - alpha)

			cvWeights[j] = weights

	cvWeights = cvWeights[degree]
	return [[_cvs[index], weight] for index, weight in cvWeights.items()]


def tangentOnCurveWeights(cvs, t, degree, knots=None):
	"""
	Creates a mapping of cvs to curve tangent weight values.
	While all cvs are required, only the cvs with non-zero weights will be returned.

	Args:
		cvs(list): A list of cvs, these are used for the return value.
		t(float): A parameter value. 
		degree(int): The curve dimensions. 
		knots(list): A list of knot values. 

	Returns:
		list: A list of control point, weight pairs.
	"""

	order = degree + 1  # Our functions often use order instead of degree
	if len(cvs) <= degree:
		raise CurveException('Curves of degree %s require at least %s cvs' % (degree, degree + 1))

	knots = knots or defaultKnots(len(cvs), degree)  # Defaults to even knot distribution
	if len(knots) != len(cvs) + order:
		raise CurveException('Not enough knots provided. Curves with %s cvs must have a knot vector of length %s. '
							 'Received a knot vector of length %s: %s. '
							 'Total knot count must equal len(cvs) + degree + 1.' % (len(cvs), len(cvs) + order,
																					 len(knots), knots))

	# Remap the t value to the range of knot values.
	min = knots[order] - 1
	max = knots[len(knots) - 1 - order] + 1
	t = (t * (max - min)) + min

	# Determine which segment the t lies in
	segment = degree
	for index, knot in enumerate(knots[order:len(knots) - order]):
		if knot <= t:
			segment = index + order

	# Convert cvs into hash-able indices
	_cvs = cvs
	cvs = [i for i in range(len(cvs))]

	# In order to find the tangent we need to find points on a lower degree curve
	degree = degree - 1
	qWeights = [{cv: 1.0} for cv in range(0, degree + 1)]

	# Get the DeBoor weights for this lower degree curve
	for r in range(1, degree + 1):
		for j in range(degree, r - 1, -1):
			right = j + 1 + segment - r
			left = j + segment - degree
			alpha = (t - knots[left]) / (knots[right] - knots[left])

			weights = {}
			for cv, weight in qWeights[j].items():
				weights[cv] = weight * alpha

			for cv, weight in qWeights[j - 1].items():
				if cv in weights:
					weights[cv] += weight * (1 - alpha)
				else:
					weights[cv] = weight * (1 - alpha)

			qWeights[j] = weights
	weights = qWeights[degree]

	# Take the lower order weights and match them to our actual cvs
	cvWeights = []
	for j in range(0, degree + 1):
		weight = weights[j]
		cv0 = j + segment - degree
		cv1 = j + segment - degree - 1
		alpha = weight * (degree + 1) / (knots[j + segment + 1] - knots[j + segment - degree])
		cvWeights.append([cvs[cv0], alpha])
		cvWeights.append([cvs[cv1], -alpha])

	return [[_cvs[index], weight] for index, weight in cvWeights]


def pointOnSurfaceWeights(cvs, u, v, uKnots=None, vKnots=None, degree=3):
	"""
	Creates a mapping of cvs to surface point weight values.

	Args:
		cvs(list): A list of cv rows, these are used for the return value.
		u(float): The u parameter value on the curve.
		v(float): The v parameter value on the curve.
		uKnots(list, optional): A list of knot integers along u.
		vKnots(list, optional): A list of knot integers along v.
		degree(int, optional): The degree of the curve. Minimum is 2.

	Returns:
		list: A list of control point, weight pairs.
	"""
	matrixWeightRows = [pointOnCurveWeights(row, u, degree, uKnots) for row in cvs]
	matrixWeightColumns = pointOnCurveWeights([i for i in range(len(matrixWeightRows))], v, degree, vKnots)
	surfaceMatrixWeights = []
	for index, weight in matrixWeightColumns:
		matrixWeights = matrixWeightRows[index]
		surfaceMatrixWeights.extend([[m, (w * weight)] for m, w in matrixWeights])

	return surfaceMatrixWeights


def tangentUOnSurfaceWeights(cvs, u, v, uKnots=None, vKnots=None, degree=3):
	"""
	Creates a mapping of cvs to surface tangent weight values along the u axis.

	Args:
		cvs(list): A list of cv rows, these are used for the return value.
		u(float): The u parameter value on the curve.
		v(float): The v parameter value on the curve.
		uKnots(list, optional): A list of knot integers along u.
		vKnots(list, optional): A list of knot integers along v.
		degree(int, optional): The degree of the curve. Minimum is 2.

	Returns:
		list: A list of control point, weight pairs.
	"""

	matrixWeightRows = [pointOnCurveWeights(row, u, degree, uKnots) for row in cvs]
	matrixWeightColumns = tangentOnCurveWeights([i for i in range(len(matrixWeightRows))], v, degree, vKnots)
	surfaceMatrixWeights = []
	for index, weight in matrixWeightColumns:
		matrixWeights = matrixWeightRows[index]
		surfaceMatrixWeights.extend([[m, (w * weight)] for m, w in matrixWeights])

	return surfaceMatrixWeights


def tangentVOnSurfaceWeights(cvs, u, v, uKnots=None, vKnots=None, degree=3):
	"""
	Creates a mapping of cvs to surface tangent weight values along the v axis.

	Args:
		cvs(list): A list of cv rows, these are used for the return value.
		u(float): The u parameter value on the curve.
		v(float): The v parameter value on the curve.
		uKnots(list, optional): A list of knot integers along u.
		vKnots(list, optional): A list of knot integers along v.
		degree(int, optional): The degree of the curve. Minimum is 2.

	Returns:
		list: A list of control point, weight pairs.
	"""
	# Re-order the cvs
	rowCount = len(cvs)
	columnCount = len(cvs[0])
	reorderedCvs = [[cvs[row][col] for row in xrange(rowCount)] for col in xrange(columnCount)]
	return tangentUOnSurfaceWeights(reorderedCvs, v, u, uKnots=vKnots, vKnots=uKnots, degree=degree)


class CurveException(BaseException):
	""" Raised to indicate invalid curve parameters. """


# ------- EXAMPLES -------- #


import math
from maya import cmds


def _is2020():
	""" Determines whether the current maya version is 2020+ """
	if 'Preview' in cmds.about(version=True):  # Consider the Maya Beta to be 2020+
		return True
	return int(cmds.about(version=True).split('.')[0]) >= 2020


def _testCube(radius=1.0, color=(1,1,1), name='cube', position=(0,0,0)):
	""" Creates a cube for testing purposes. """
	radius *= 2
	cube = cmds.polyCube(name=name, h=radius, w=radius, d=radius)[0]
	shader = cmds.shadingNode('lambert', asShader=True)
	cmds.setAttr('%s.color' % shader, *color)
	cmds.setAttr('%s.ambientColor' % shader, 0.1, 0.1, 0.1)
	shadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
	cmds.connectAttr(shader + '.outColor', shadingGroup + ".surfaceShader", force=True)
	cmds.sets(cube, fe=shadingGroup)
	cmds.xform(cube, t=position)
	return cube


def _testSphere(radius=1.0, color=(1,1,1), name='sphere', position=(0,0,0)):
	""" Creates a sphere for testing purposes. """
	sphere = cmds.polySphere(name=name, radius=radius)[0]
	shader = cmds.shadingNode('lambert', asShader=True)
	cmds.setAttr('%s.ambientColor' % shader, 0.1, 0.1, 0.1)
	cmds.setAttr('%s.color' % shader, *color)
	shadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
	cmds.connectAttr(shader + '.outColor', shadingGroup + ".surfaceShader", force=True)
	cmds.sets(sphere, fe=shadingGroup)
	cmds.xform(sphere, t=position)
	return sphere


def _testMatrixOnCurve(count=4, pCount=None, degree=3):
	"""
	Creates an example curve with the given cv and point counts.
	
	Args:
		count(int): The amount of cvs. 
		pCount(int): The amount of points to attach to the curve.
		degree(int): The degree of the curve.
	"""

	pCount = pCount or count * 4
	cRadius = 1.0
	pRadius = 0.5
	spacing = cRadius * 5

	# Create the control points
	cvMatrices = []
	for i in range(count):
		cv = _testSphere(cRadius, color=(0.7,1,1), name='cv%s' % i, position=(i * spacing, 0, 0))
		cvMatrices.append('%s.worldMatrix[0]' % cv)

	# Attach the cubes
	for i in range(pCount):
		t = i / (float(pCount) - 1)
		pNode = _testCube(pRadius, color=(0,0.5,1), name='p%s' % i)

		# Create the position matrix
		pointMatrixWeights = pointOnCurveWeights(cvMatrices, t, degree=degree)
		pointMatrixNode = cmds.createNode('wtAddMatrix', name='pointMatrix0%s' % (i+1))
		pointMatrix = '%s.matrixSum' % pointMatrixNode
		for index, (matrix, weight) in enumerate(pointMatrixWeights):
			cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (pointMatrixNode, index))
			cmds.setAttr('%s.wtMatrix[%s].weightIn' % (pointMatrixNode, index), weight)

		# Create the tangent matrix
		tangentMatrixWeights = tangentOnCurveWeights(cvMatrices, t, degree=degree)
		tangentMatrixNode = cmds.createNode('wtAddMatrix', name='tangentMatrix0%s' % (i+1))
		tangentMatrix = '%s.matrixSum' % tangentMatrixNode
		for index, (matrix, weight) in enumerate(tangentMatrixWeights):
			cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (tangentMatrixNode, index))
			cmds.setAttr('%s.wtMatrix[%s].weightIn' % (tangentMatrixNode, index), weight)

		if _is2020():
			# Create an aim matrix node
			aimMatrixNode = cmds.createNode('aimMatrix', name='aimMatrix0%s' % (i+1))
			cmds.connectAttr(pointMatrix, '%s.inputMatrix' % aimMatrixNode)
			cmds.connectAttr(tangentMatrix, '%s.primaryTargetMatrix' % aimMatrixNode)
			cmds.setAttr('%s.primaryMode' % aimMatrixNode, 1)
			cmds.setAttr('%s.primaryInputAxis' % aimMatrixNode, 1, 0, 0)
			cmds.setAttr('%s.secondaryInputAxis' % aimMatrixNode, 0, 1, 0)
			cmds.setAttr('%s.secondaryMode' % aimMatrixNode, 0)
			aimMatrixOutput = '%s.outputMatrix' % aimMatrixNode

			# Remove scale
			pickMatrixNode = cmds.createNode('pickMatrix', name='noScale0%s' % (i+1))
			cmds.connectAttr(aimMatrixOutput, '%s.inputMatrix' % pickMatrixNode)
			cmds.setAttr('%s.useScale' % pickMatrixNode, False)
			cmds.setAttr('%s.useShear' % pickMatrixNode, False)
			outputMatrix = '%s.outputMatrix' % pickMatrixNode

			cmds.connectAttr(outputMatrix, '%s.offsetParentMatrix' % pNode)
		else:
			# Decompose the position matrix
			pointDecomposeNode = cmds.createNode('decomposeMatrix', name='pointDecompose0%s' % (i+1))
			cmds.connectAttr(pointMatrix, '%s.inputMatrix' % pointDecomposeNode)
			pointVector = '%s.outputTranslate' % pointDecomposeNode

			# Convert tangent matrix to vector
			tangentDecomposeNode = cmds.createNode('decomposeMatrix', name='tangentVectorDecompose0%s' % (i+1))
			cmds.connectAttr(tangentMatrix, '%s.inputMatrix' % tangentDecomposeNode)
			tangentVector = '%s.outputTranslate' % tangentDecomposeNode

			# Normalize the tangent vector
			tangentNormalizeNode = cmds.createNode('vectorProduct', name='tangentVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % tangentNormalizeNode, 0)
			cmds.setAttr('%s.normalizeOutput' % tangentNormalizeNode, True)
			cmds.connectAttr(tangentVector, '%s.input1' % tangentNormalizeNode)
			xVector = '%s.output' % tangentNormalizeNode

			# Get an up vector from the position matrix
			upVectorNode = cmds.createNode('vectorProduct', name='upVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % upVectorNode, 3)
			cmds.setAttr('%s.normalizeOutput' % upVectorNode, True)
			cmds.setAttr('%s.input1' % upVectorNode, 0, 1, 0)
			cmds.connectAttr(pointMatrix, '%s.matrix' % upVectorNode)
			upVector = '%s.output' % upVectorNode

			# Find the z vector by taking the cross product
			zVectorNode = cmds.createNode('vectorProduct', name='zVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % zVectorNode, 2)
			cmds.setAttr('%s.normalizeOutput' % zVectorNode, True)
			cmds.connectAttr(xVector, '%s.input1' % zVectorNode)
			cmds.connectAttr(upVector, '%s.input2' % zVectorNode)
			zVector = '%s.output' % zVectorNode

			# Find the y vector by taking the cross product
			yVectorNode = cmds.createNode('vectorProduct', name='yVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % yVectorNode, 2)
			cmds.setAttr('%s.normalizeOutput' % yVectorNode, True)
			cmds.connectAttr(xVector, '%s.input1' % yVectorNode)
			cmds.connectAttr(zVector, '%s.input2' % yVectorNode)
			yVector = '%s.output' % yVectorNode

			# Create an aim matrix from each axis
			outputMatrixNode = cmds.createNode('fourByFourMatrix', name='outputMatrix0%s' % (i+1))
			for row, vector in enumerate([xVector, yVector, zVector, pointVector]):
				for col, axis in enumerate(['X', 'Y', 'Z']):
					cmds.connectAttr('%s%s' % (vector, axis), '%s.i%s%s' % (outputMatrixNode, row, col))

			# Decompose the matrix transformations
			decomposeMatrixNode = cmds.createNode('decomposeMatrix', name='outputTransformations0%s' % (i+1))
			cmds.connectAttr('%s.output' % outputMatrixNode, '%s.inputMatrix' % decomposeMatrixNode)

			# Connect the outputs
			cmds.connectAttr('%s.outputTranslate' % decomposeMatrixNode, '%s.translate' % pNode)
			cmds.connectAttr('%s.outputRotate' % decomposeMatrixNode, '%s.rotate' % pNode)


def _testMatrixOnCircularCurve(count=4, pCount=None, degree=3):
	"""
	Creates an example circular curve with the given cv and point counts.
	
	Args:
		count(int): The amount of cvs. 
		pCount(int): The amount of points to attach to the curve.
		degree(int): The degree of the curve.
	"""

	pCount = pCount or count * 4
	cRadius = 1.0
	pRadius = 0.5
	spacing = cRadius * 5

	# Create the control points
	cvMatrices = []
	for i in range(count):
		t = i / (float(count))
		x = math.cos(t * math.pi * 2)
		y = math.sin(t * math.pi * 2)
		cv = _testSphere(cRadius, color=(0.7,1,1), name='cv%s' % i, position=(x * spacing, 0, y * spacing))
		cvMatrices.append('%s.worldMatrix[0]' % cv)

	# Modify the control point list so that they loop
	cvMatrices = cvMatrices + cvMatrices[:3]
	knots = [i for i in range(len(cvMatrices) + degree + 1)]
	knots = [float(knot) for knot in knots]

	# Attach the cubes
	for i in range(pCount):
		t = i / (float(pCount) - 1)
		pNode = _testCube(pRadius, color=(0,0.5,1), name='p%s' % i)

		# Create the position matrix
		pointMatrixWeights = pointOnCurveWeights(cvMatrices, t, degree=degree, knots=knots)
		pointMatrixNode = cmds.createNode('wtAddMatrix', name='pointMatrix0%s' % (i+1))
		pointMatrix = '%s.matrixSum' % pointMatrixNode
		for index, (matrix, weight) in enumerate(pointMatrixWeights):
			cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (pointMatrixNode, index))
			cmds.setAttr('%s.wtMatrix[%s].weightIn' % (pointMatrixNode, index), weight)

		# Create the tangent matrix
		tangentMatrixWeights = tangentOnCurveWeights(cvMatrices, t, degree=degree, knots=knots)
		tangentMatrixNode = cmds.createNode('wtAddMatrix', name='tangentMatrix0%s' % (i+1))
		tangentMatrix = '%s.matrixSum' % tangentMatrixNode
		for index, (matrix, weight) in enumerate(tangentMatrixWeights):
			cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (tangentMatrixNode, index))
			cmds.setAttr('%s.wtMatrix[%s].weightIn' % (tangentMatrixNode, index), weight)

		if _is2020():
			# Create an aim matrix node
			aimMatrixNode = cmds.createNode('aimMatrix', name='aimMatrix0%s' % (i+1))
			cmds.connectAttr(pointMatrix, '%s.inputMatrix' % aimMatrixNode)
			cmds.connectAttr(tangentMatrix, '%s.primaryTargetMatrix' % aimMatrixNode)
			cmds.setAttr('%s.primaryMode' % aimMatrixNode, 1)
			cmds.setAttr('%s.primaryInputAxis' % aimMatrixNode, 1, 0, 0)
			cmds.setAttr('%s.secondaryInputAxis' % aimMatrixNode, 0, 1, 0)
			cmds.setAttr('%s.secondaryMode' % aimMatrixNode, 1)
			aimMatrixOutput = '%s.outputMatrix' % aimMatrixNode

			# Remove scale
			pickMatrixNode = cmds.createNode('pickMatrix', name='noScale0%s' % (i+1))
			cmds.connectAttr(aimMatrixOutput, '%s.inputMatrix' % pickMatrixNode)
			cmds.setAttr('%s.useScale' % pickMatrixNode, False)
			cmds.setAttr('%s.useShear' % pickMatrixNode, False)
			outputMatrix = '%s.outputMatrix' % pickMatrixNode

			cmds.connectAttr(outputMatrix, '%s.offsetParentMatrix' % pNode)
		else:
			# Decompose the position matrix
			pointDecomposeNode = cmds.createNode('decomposeMatrix', name='pointDecompose0%s' % (i+1))
			cmds.connectAttr(pointMatrix, '%s.inputMatrix' % pointDecomposeNode)
			pointVector = '%s.outputTranslate' % pointDecomposeNode

			# Convert tangent matrix to vector
			tangentDecomposeNode = cmds.createNode('decomposeMatrix', name='tangentVectorDecompose0%s' % (i+1))
			cmds.connectAttr(tangentMatrix, '%s.inputMatrix' % tangentDecomposeNode)
			tangentVector = '%s.outputTranslate' % tangentDecomposeNode

			# Normalize the tangent vector
			tangentNormalizeNode = cmds.createNode('vectorProduct', name='tangentVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % tangentNormalizeNode, 0)
			cmds.setAttr('%s.normalizeOutput' % tangentNormalizeNode, True)
			cmds.connectAttr(tangentVector, '%s.input1' % tangentNormalizeNode)
			xVector = '%s.output' % tangentNormalizeNode

			# Get an up vector from the position matrix
			upVectorNode = cmds.createNode('vectorProduct', name='upVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % upVectorNode, 3)
			cmds.setAttr('%s.normalizeOutput' % upVectorNode, True)
			cmds.setAttr('%s.input1' % upVectorNode, 0, 1, 0)
			cmds.connectAttr(pointMatrix, '%s.matrix' % upVectorNode)
			upVector = '%s.output' % upVectorNode

			# Find the z vector by taking the cross product
			zVectorNode = cmds.createNode('vectorProduct', name='zVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % zVectorNode, 2)
			cmds.setAttr('%s.normalizeOutput' % zVectorNode, True)
			cmds.connectAttr(xVector, '%s.input1' % zVectorNode)
			cmds.connectAttr(upVector, '%s.input2' % zVectorNode)
			zVector = '%s.output' % zVectorNode

			# Find the y vector by taking the cross product
			yVectorNode = cmds.createNode('vectorProduct', name='yVector0%s' % (i+1))
			cmds.setAttr('%s.operation' % yVectorNode, 2)
			cmds.setAttr('%s.normalizeOutput' % yVectorNode, True)
			cmds.connectAttr(xVector, '%s.input1' % yVectorNode)
			cmds.connectAttr(zVector, '%s.input2' % yVectorNode)
			yVector = '%s.output' % yVectorNode

			# Create an aim matrix from each axis
			outputMatrixNode = cmds.createNode('fourByFourMatrix', name='outputMatrix0%s' % (i+1))
			for row, vector in enumerate([xVector, yVector, zVector, pointVector]):
				for col, axis in enumerate(['X', 'Y', 'Z']):
					cmds.connectAttr('%s%s' % (vector, axis), '%s.i%s%s' % (outputMatrixNode, row, col))

			# Decompose the matrix transformations
			decomposeMatrixNode = cmds.createNode('decomposeMatrix', name='outputTransformations0%s' % (i+1))
			cmds.connectAttr('%s.output' % outputMatrixNode, '%s.inputMatrix' % decomposeMatrixNode)

			# Connect the outputs
			cmds.connectAttr('%s.outputTranslate' % decomposeMatrixNode, '%s.translate' % pNode)
			cmds.connectAttr('%s.outputRotate' % decomposeMatrixNode, '%s.rotate' % pNode)


def _testMatrixOnSurface(uCount=4, vCount=4, degree=3):
	"""
	Tests matrixOnSurface with the given cv counts.

	Args:
		uCount(int): The amount of cvs in u. 
		vCount(int): The amount of cvs in v. 
		degree(int): The degree of the curve.
	"""

	pCountU = uCount * 3
	pCountV = vCount * 3
	cRadius = 1.0
	pRadius = 0.5
	spacing = cRadius * 5

	cvMatrices = []
	for i in range(uCount):
		row = []
		for j in range(vCount):
			cv = _testSphere(cRadius, color=(1, 1, 1), name='cv%s%s' % (i, j), position=(i * spacing, 0, j * spacing))
			row.append('%s.worldMatrix[0]' % cv)
		cvMatrices.append(row)

	for i in range(pCountU):
		for j in range(pCountV):
			u = i / (float(pCountU) - 1)
			v = j / (float(pCountV) - 1)
			pNode = _testCube(pRadius, color=(0, 0.5, 1), name='p%s%s' % (i, j))

			# Create the position matrix
			pointMatrixWeights = pointOnSurfaceWeights(cvMatrices, u, v, degree=degree)
			pointMatrixNode = cmds.createNode('wtAddMatrix', name='pointMatrix0%s' % (i+1))
			pointMatrix = '%s.matrixSum' % pointMatrixNode
			for index, (matrix, weight) in enumerate(pointMatrixWeights):
				cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (pointMatrixNode, index))
				cmds.setAttr('%s.wtMatrix[%s].weightIn' % (pointMatrixNode, index), weight)

			# Create the tangent u matrix
			tangentUMatrixWeights = tangentUOnSurfaceWeights(cvMatrices, u, v, degree=degree)
			tangentUMatrixNode = cmds.createNode('wtAddMatrix', name='tangentUMatrix0%s' % (i+1))
			tangentUMatrix = '%s.matrixSum' % tangentUMatrixNode
			for index, (matrix, weight) in enumerate(tangentUMatrixWeights):
				cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (tangentUMatrixNode, index))
				cmds.setAttr('%s.wtMatrix[%s].weightIn' % (tangentUMatrixNode, index), weight)

			# Create the tangent v matrix
			tangentVMatrixWeights = tangentVOnSurfaceWeights(cvMatrices, u, v, degree=degree)
			tangentVMatrixNode = cmds.createNode('wtAddMatrix', name='tangentVMatrix0%s' % (i+1))
			tangentVMatrix = '%s.matrixSum' % tangentVMatrixNode
			for index, (matrix, weight) in enumerate(tangentVMatrixWeights):
				cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (tangentVMatrixNode, index))
				cmds.setAttr('%s.wtMatrix[%s].weightIn' % (tangentVMatrixNode, index), weight)

			if _is2020():
				# Create an aim matrix node
				aimMatrixNode = cmds.createNode('aimMatrix', name='aimMatrix0%s' % (i+1))
				cmds.connectAttr(pointMatrix, '%s.inputMatrix' % aimMatrixNode)
				cmds.connectAttr(tangentUMatrix, '%s.primaryTargetMatrix' % aimMatrixNode)
				cmds.setAttr('%s.primaryMode' % aimMatrixNode, 1)
				cmds.connectAttr(tangentVMatrix, '%s.secondaryTargetMatrix' % aimMatrixNode)
				cmds.setAttr('%s.secondaryMode' % aimMatrixNode, 1)
				aimMatrixOutput = '%s.outputMatrix' % aimMatrixNode

				# Remove scale
				pickMatrixNode = cmds.createNode('pickMatrix', name='noScale0%s' % (i+1))
				cmds.connectAttr(aimMatrixOutput, '%s.inputMatrix' % pickMatrixNode)
				cmds.setAttr('%s.useScale' % pickMatrixNode, False)
				cmds.setAttr('%s.useShear' % pickMatrixNode, False)
				outputMatrix = '%s.outputMatrix' % pickMatrixNode

				cmds.connectAttr(outputMatrix, '%s.offsetParentMatrix' % pNode)
			else:
				# Decompose the position matrix
				pointDecomposeNode = cmds.createNode('decomposeMatrix', name='pointDecompose0%s' % (i+1))
				cmds.connectAttr(pointMatrix, '%s.inputMatrix' % pointDecomposeNode)
				pointVector = '%s.outputTranslate' % pointDecomposeNode

				# Convert tangent u matrix to vector
				tangentUDecomposeNode = cmds.createNode('decomposeMatrix', name='tangentUVectorDecompose0%s' % (i+1))
				cmds.connectAttr(tangentUMatrix, '%s.inputMatrix' % tangentUDecomposeNode)
				tangentUVector = '%s.outputTranslate' % tangentUDecomposeNode

				# Normalize the tangent u vector
				tangentUNormalizeNode = cmds.createNode('vectorProduct', name='tangentUVector0%s' % (i+1))
				cmds.setAttr('%s.operation' % tangentUNormalizeNode, 0)
				cmds.setAttr('%s.normalizeOutput' % tangentUNormalizeNode, True)
				cmds.connectAttr(tangentUVector, '%s.input1' % tangentUNormalizeNode)
				xVector = '%s.output' % tangentUNormalizeNode

				# Convert tangent v matrix to vector
				tangentVDecomposeNode = cmds.createNode('decomposeMatrix', name='tangentVVectorDecompose0%s' % (i+1))
				cmds.connectAttr(tangentVMatrix, '%s.inputMatrix' % tangentVDecomposeNode)
				tangentVVector = '%s.outputTranslate' % tangentVDecomposeNode

				# Normalize the tangent v vector
				tangentVNormalizeNode = cmds.createNode('vectorProduct', name='tangentVVector0%s' % (i+1))
				cmds.setAttr('%s.operation' % tangentVNormalizeNode, 0)
				cmds.setAttr('%s.normalizeOutput' % tangentVNormalizeNode, True)
				cmds.connectAttr(tangentVVector, '%s.input1' % tangentVNormalizeNode)
				zVector = '%s.output' % tangentVNormalizeNode

				# Find the y vector by taking the cross product
				yVectorNode = cmds.createNode('vectorProduct', name='yVector0%s' % (i+1))
				cmds.setAttr('%s.operation' % yVectorNode, 2)
				cmds.setAttr('%s.normalizeOutput' % yVectorNode, True)
				cmds.connectAttr(xVector, '%s.input1' % yVectorNode)
				cmds.connectAttr(zVector, '%s.input2' % yVectorNode)
				yVector = '%s.output' % yVectorNode

				# Create an aim matrix from each axis
				outputMatrixNode = cmds.createNode('fourByFourMatrix', name='outputMatrix0%s' % (i+1))
				for row, vector in enumerate([xVector, yVector, zVector, pointVector]):
					for col, axis in enumerate(['X', 'Y', 'Z']):
						cmds.connectAttr('%s%s' % (vector, axis), '%s.i%s%s' % (outputMatrixNode, row, col))

				# Decompose the matrix transformations
				decomposeMatrixNode = cmds.createNode('decomposeMatrix', name='outputTransformations0%s' % (i+1))
				cmds.connectAttr('%s.output' % outputMatrixNode, '%s.inputMatrix' % decomposeMatrixNode)

				# Connect the outputs
				cmds.connectAttr('%s.outputTranslate' % decomposeMatrixNode, '%s.translate' % pNode)
				cmds.connectAttr('%s.outputRotate' % decomposeMatrixNode, '%s.rotate' % pNode)



_testMatrixOnCurve(count=4, pCount=None, degree=3)