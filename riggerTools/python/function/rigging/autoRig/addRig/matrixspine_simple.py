"""
Functions for generating spline weights by Cole O'Brien
https://coleobrien.medium.com/matrix-splines-in-maya-ec17f3b3741
01_matrixspine_01_breakdown.py

mc.setAttr('wtAddMatrix1.wtMatrix[0].weightIn', 0.5 )
mc.setAttr('wtAddMatrix1.wtMatrix[1].weightIn', 0.5 )

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
	print('\n***ATTENTION HERE***')
	print('This is cvs: {0}'.format(cvs))
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


count=4
pCount=None 
degree=3

pCount = pCount or count * 4
cRadius = 1.0
pRadius = 0.5
spacing = cRadius * 5



networkNode = cmds.createNode('network', name='pointMatrixWeights_meta')
networkNode_tangent = cmds.createNode('network', name='pointMatrixWeights_tangent_meta')

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
	# pNode = _creParentCtrl(size=2, color='white', name = '{0}_ChildCv{1:02d}'.format(side, num), ctrlShape = 'square_ctrlShape')

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

		#... create meta link to tangent
		linkAttrName = 'tangent_cv{}_{:03d}'.format((i+1), index)
		cmds.addAttr(networkNode_tangent, longName= linkAttrName, attributeType='float')
		cmds.connectAttr('%s.wtMatrix[%s].weightIn' % (tangentMatrixNode, index), '{0}.{1}'.format(networkNode_tangent, linkAttrName))



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