# ... imports ...
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

def createDistance(nameSpace, part, startP=None, endP=None, noTouchGrp='noTouch_grp'):
	# ... (Naming logic same as original) ...
	
	if part =='up':
		uprLoc = nameSpace + 'lockUp' + rawNameUPR + '_loc' 
		lwrLoc = nameSpace + 'lockUp' + rawNameLWR + '_loc' 
	# ... (naming logic) ...

	# Refactored Constraints
	# Using Point Constraint Matrix (Parent Matrix without Rotate/Scale)
	mtc.parentConMatrixGPT(startP, uprLoc, mo=False, translate=True, rotate=False, scale=False)
	mtc.parentConMatrixGPT(endP, lwrLoc, mo=False, translate=True, rotate=False, scale=False)

	# ... (Distance Dimension & Grouping logic same as original) ...
	
	return rawNameUPR, uprDistanceName, endP, uprLoc, lwrLoc