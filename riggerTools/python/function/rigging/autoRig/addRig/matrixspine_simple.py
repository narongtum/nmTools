#... 24.02.Feb.13.Tue.09_De boor matrix spine_Chris bag
#... 24.05.May.07.Tue.10_Change attr link to wtMatrix


"""
Functions for generating spline weights by Cole O'Brien
https://coleobrien.medium.com/matrix-splines-in-maya-ec17f3b3741
01_matrixspine_01_breakdown.py
"""

import math
import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

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




def _is2020():
	""" Determines whether the current maya version is 2020+ """
	if 'Preview' in mc.about(version=True):  # Consider the Maya Beta to be 2020+
		return True
	return int(mc.about(version=True).split('.')[0]) >= 2020



#... Child ctrl
def _testCube(radius=1.0, color=(1,1,1), name='cube', position=(0,0,0)):
	""" Creates a cube for testing purposes. """
	radius *= 2
	cube = mc.polyCube(name=name, h=radius, w=radius, d=radius)[0]
	shader = mc.shadingNode('lambert', asShader=True)
	mc.setAttr('%s.color' % shader, *color)
	mc.setAttr('%s.ambientColor' % shader, 0.1, 0.1, 0.1)
	shadingGroup = mc.sets(renderable=True, noSurfaceShader=True, empty=True)
	mc.connectAttr(shader + '.outColor', shadingGroup + ".surfaceShader", force=True)
	mc.sets(cube, fe=shadingGroup)
	mc.xform(cube, t=position)
	return cube

#... Parent ctrl
def _testSphere(radius=1.0, color=(1,1,1), name='sphere', position=(0,0,0)):
	""" Creates a sphere for testing purposes. """
	sphere = mc.polySphere(name=name, radius=radius)[0]
	shader = mc.shadingNode('lambert', asShader=True)
	mc.setAttr('%s.ambientColor' % shader, 0.1, 0.1, 0.1)
	mc.setAttr('%s.color' % shader, *color)
	shadingGroup = mc.sets(renderable=True, noSurfaceShader=True, empty=True)
	mc.connectAttr(shader + '.outColor', shadingGroup + ".surfaceShader", force=True)
	mc.sets(sphere, fe=shadingGroup)
	mc.xform(sphere, t=position)
	return sphere


def _creParentCtrl(size=1.0, color='yellow', name='main', ctrlShape = 'square_ctrlShape'):
	parent_ctrl = core.Dag(name + '_ctrl')
	parent_ctrl.nmCreateController(ctrlShape)
	parent_ctrl.rotateOrder = 'xzy' 
	parent_ctrl.color = color
	parent_ctrl.editCtrlShape( axis = size * 1.8 )
	parent_ctrl.color = color
	return parent_ctrl.name





# ------- EXAMPLES -------- #

#... must have locator first 
#... naming it like L_mainCv01 >>> L_mainCv016

#... number of Master control
count=6
#... number of Slave
pCount=13




degree=5

pCount = pCount or count * 4
cRadius = 1.0
pRadius = 0.5
spacing = cRadius * 5

charScale = 1.0

side = 'L'

network_resultNode_point = mc.createNode('network', name='{0}_pointMatrixWeights_meta'.format(side))
network_resultNode_tangent = mc.createNode('network', name='{0}_tangentMatrixWeights_meta'.format(side))

# Create the control points
cvMatrices = []
for num in range(count):
	startNum = num + 1
	# cv = _testSphere(cRadius, color=(0.7,1,1), name='cv%s' % i, position=(i * spacing, 0, 0))
	cv = _creParentCtrl(size=1, color='yellow', name = '{0}_mainCv{1:02d}'.format(side, startNum), ctrlShape = 'cube_ctrlShape')
	cvMatrices.append('%s.worldMatrix[0]' % cv)




from function.rigging.autoRig.base import core
reload(core)



#... snap parent control to the locator
from function.rigging.util import misc

num = 1
for num in range(count):
	num = num +1
	print(num)
	main_ctrl = '{0}_mainCv0{1}_ctrl'.format(side, num)
	source_temp_loc = '{1}_main0{0}'.format(num, side)
	misc.snapParentCon(source_temp_loc, main_ctrl)








#... Attach the cubes
for i in range(pCount):
	num = i + 1
	
	t = i / (float(pCount) - 1)

	print('\nThis is "T" {0} at loop of {1}'.format(t,i))

	# pNode = _testCube(pRadius, color=(0,0.5,1), name='p%s' % i)
	pNode = _creParentCtrl(size=0.02, color='white', name = '{0}_childCV{1:02d}'.format(side, num), ctrlShape = 'plainSphereB_ctrlShape')

	#
	# Create the point matrix
	#

	#... Give 1. cvMatrices, 2. t value 3. degree
	pointMatrixWeights = pointOnCurveWeights(cvMatrices, t, degree=degree)

	# pointMatrixNode = core.WtAddMatrixWithVal('%s_pointMatrix%s' % (side, str(i+1).zfill(2)))
	pointMatrixNode = core.WtAddMatrixWithChannal('%s_pointMatrix%s' % (side, str(i+1).zfill(2)), count)

	# pointMatrixNode = mc.createNode('wtAddMatrix', name='%s_pointMatrix0%s_wtAddMat' % (side, i+1))

	#... create network node for read
	pointMatrix = '%s.matrixSum' % pointMatrixNode

	for index, (matrix, weight) in enumerate(pointMatrixWeights):
		# print('Weight is {0}'.format(weight))
		print('\nThis is index >>> {0}'.format(index))

		#... connect pointMatrixNode
		mc.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (pointMatrixNode, index))


		#
		#... Change connection line for make easy to debug
		#

		# connectAttr -f L_pointMatrix01_wtAddMatrix.wt_0 L_pointMatrix01_wtAddMatrix.wtMatrix[0].weightIn;

		#... set attr to themself channel
		mc.setAttr('{0}.wt_{1}'.format(pointMatrixNode, index), weight)

		#... link this back to weight matrix that has to be
		mc.connectAttr('{0}.wt_{1}'.format(pointMatrixNode, index), '{0}.wtMatrix[{1}].weightIn'.format(pointMatrixNode, index))

		#... set attr
		# mc.setAttr('%s.wtMatrix[%s].weightIn' % (pointMatrixNode, index), weight)





		#... observe  value
		linkAttrName = 'point_cv{}_{:03d}'.format((i+1), index)
		mc.addAttr(network_resultNode_point, longName= linkAttrName, attributeType='float')
		mc.connectAttr('%s.wtMatrix[%s].weightIn' %(pointMatrixNode, index), '{0}.{1}'.format(network_resultNode_point, linkAttrName))
		






	#
	# Create the tangent matrix
	#

	tangentMatrixWeights = tangentOnCurveWeights(cvMatrices, t, degree=degree)

	tangentMatrixNode = core.WtAddMatrixWithChannal('%s_tangentMatrix%s' % (side, str(i+1).zfill(2)), count+4)
	# tangentMatrixNode = core.WtAddMatrixWithVal('%s_tangentMatrix%s' % (side, str(i+1).zfill(2)))
	# tangentMatrixNode = mc.createNode('wtAddMatrix', name='%s_tangentMatrix0%s_wtAddMat' % (side, i+1))

	tangentMatrix = '%s.matrixSum' % tangentMatrixNode
	for index, (matrix, weight) in enumerate(tangentMatrixWeights):

		print('\nThis is matrix >>> {0}'.format(matrix))


		#
		#... Change connection line for make easy to debug
		#

		

		
		mc.setAttr('{0}.wt_{1}'.format(tangentMatrixNode, index), weight)
		#... link this back to weight matrix that has to be
		mc.connectAttr('{0}.wt_{1}'.format(tangentMatrixNode, index), '{0}.wtMatrix[{1}].weightIn'.format(tangentMatrixNode, index))
		

		#... connect main ctrl to wtMatrix
		mc.connectAttr(matrix, '%s.wtMatrix[%s].matrixIn' % (tangentMatrixNode, index))
		# mc.setAttr('%s.wtMatrix[%s].weightIn' % (tangentMatrixNode, index), weight)
		# mc.error('501')

		#... observe tangent value
		linkAttrName = 'point_cv{}_{:03d}'.format((i+1), index)
		mc.addAttr(network_resultNode_tangent, longName= linkAttrName, attributeType='float')
		mc.connectAttr('%s.wtMatrix[%s].weightIn' %(tangentMatrixNode, index), '{0}.{1}'.format(network_resultNode_tangent, linkAttrName))



	

	# Create an aim matrix node
	aimMatrixNode = mc.createNode('aimMatrix', name='%s_aimMatrix%s_aimMat' % (side, str(i+1).zfill(2)))
	#... connect pointMatrix here
	mc.connectAttr(pointMatrix, '%s.inputMatrix' % aimMatrixNode)
	mc.connectAttr(tangentMatrix, '%s.primaryTargetMatrix' % aimMatrixNode)

	mc.setAttr('%s.primaryMode' % aimMatrixNode, 1)
	mc.setAttr('%s.primaryInputAxis' % aimMatrixNode, 1, 0, 0)
	mc.setAttr('%s.secondaryInputAxis' % aimMatrixNode, 0, 1, 0)
	mc.setAttr('%s.secondaryMode' % aimMatrixNode, 0)
	aimMatrixOutput = '%s.outputMatrix' % aimMatrixNode

	# Remove scale
	# pickMatrixNode = mc.createNode('pickMatrix', name='%s_noScale0%s_pickMat' % (side, i+1))
	pickMatrixNode = mc.createNode('pickMatrix', name='%s_noScale%s_pickMat' % (side, str(i+1).zfill(2)))
	

	mc.connectAttr(aimMatrixOutput, '%s.inputMatrix' % pickMatrixNode)
	mc.setAttr('%s.useScale' % pickMatrixNode, False)
	mc.setAttr('%s.useShear' % pickMatrixNode, False)
	outputMatrix = '%s.outputMatrix' % pickMatrixNode

	mc.connectAttr(outputMatrix, '%s.offsetParentMatrix' % pNode)
	# mc.error('Break si wa')
	print('\nDONE')