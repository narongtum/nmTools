"""
Functions for generating spline weights by Cole O'Brien
https://coleobrien.medium.com/matrix-splines-in-maya-ec17f3b3741
01_matrixspine_01_breakdown.py
"""



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


class CurveException(BaseException):
	""" Raised to indicate invalid curve parameters. """


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

	#... print out arg
	print('\nThis is cvs: {0}'.format(cvs))
	print('This is t: {0}'.format(t))
	print('This is degree: {0}'.format(degree))
	print('This is knots: {0}'.format(knots))

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





count=3
pCount=None 
degree=2

pCount = pCount or count * 4
cRadius = 1.0
pRadius = 0.5
spacing = cRadius * 5



networkNode = cmds.createNode('network', name='pointMatrixWeights_meta')

# Create the control points
cvMatrices = []
for i in range(count):
	cv = _testSphere(cRadius, color=(0.7,1,1), name='cv%s' % i, position=(i * spacing, 0, 0))
	cvMatrices.append('%s.worldMatrix[0]' % cv)

# Attach the cubes
for i in range(pCount):
	t = i / (float(pCount) - 1)
	print('\nThis is "T" {0} at loop of {1}'.format(t,i))
	pNode = _testCube(pRadius, color=(0,0.5,1), name='p%s' % i)

	#... Create the position matrix
	#... Give 1. cvMatrices, 2. t value 3. degree
	pointMatrixWeights = pointOnCurveWeights(cvMatrices, t, degree=degree)
	pointMatrixNode = cmds.createNode('wtAddMatrix', name='pointMatrix0%s' % (i+1))
	#... create network node for read
	
	pointMatrix = '%s.matrixSum' % pointMatrixNode
	for index, (matrix, weight) in enumerate(pointMatrixWeights):
		print('Weight is {0}'.format(weight))
		cmds.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (pointMatrixNode, index))
		cmds.setAttr('%s.wtMatrix[%s].weightIn' % (pointMatrixNode, index), weight)
		linkAttrName = 'point_cv{}_{:03d}'.format((i+1), index)
		cmds.addAttr(networkNode, longName= linkAttrName, attributeType='float')
		cmds.connectAttr('%s.wtMatrix[%s].weightIn' %(pointMatrixNode, index), '{0}.{1}'.format(networkNode, linkAttrName))

	#cmds.error('break')

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