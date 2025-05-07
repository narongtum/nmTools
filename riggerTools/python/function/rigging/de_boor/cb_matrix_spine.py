'''
from function.rigging.de_boor import cb_matrix_spine_core as cb
reload(cb)

'''
import maya.cmds as mc

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



def pointOnCurveWeights(cvs, t, degree, knots=None):
	"""
	Creates a mapping of cvs to curve weight values on a spline curve.
	While all cvs are required, only the cvs with non-zero weights will be returned.
	This function is based on de Boor's algorithm for evaluating splines and has been modified to consolidate weights.
	If there are not enough CVs for the specified degree, it will pad the list by repeating the last CV.

	Args:
		cvs(list): A list of cvs, these are used for the return value.
		t(float): A parameter value. 
		degree(int): The curve degree. 
		knots(list): A list of knot values. 

	Returns:
		list: A list of control point, weight pairs.
	"""
	order = degree + 1  # Our functions often use order instead of degree

	# --- CV Padding logic ---
	if len(cvs) < order:
		padding = [cvs[-1]] * (order - len(cvs))
		cvs += padding
		mc.warning('Not enough CVs for degree %s. Padded with last CV to meet requirement of %s.' % (degree, order))

	knots = knots or defaultKnots(len(cvs), degree)  # Defaults to even knot distribution
	if len(knots) != len(cvs) + order:
		raise CurveException(
			'Not enough knots provided. Curves with %s cvs must have a knot vector of length %s. '
			'Received a knot vector of length %s: %s. '
			'Total knot count must equal len(cvs) + degree + 1.' % (len(cvs), len(cvs) + order,
			                                                       len(knots), knots))

	# --- Debug Print ---
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