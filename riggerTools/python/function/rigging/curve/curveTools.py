import pymel.core as pm

def create_curve_from_selected(obj1, obj2):
	"""
	Create a linear degree-1 curve between two objects.

	Args:
		obj1 (str or PyNode): First object
		obj2 (str or PyNode): Second object

	Returns:
		PyNode: The created curve
	"""
	obj1 = pm.PyNode(obj1)
	obj2 = pm.PyNode(obj2)

	pos1 = pm.xform(obj1, q=True, ws=True, t=True)
	pos2 = pm.xform(obj2, q=True, ws=True, t=True)

	curve = pm.curve(d=1, p=[pos1, pos2], name='twoPoint_crv')
	return curve


def rebuild_curve_to_degree3(curve, spans=8):
	"""
	Rebuild a curve to be degree 3 with a given number of spans.

	Args:
		curve (str or PyNode): Curve to rebuild
		spans (int): Number of spans to rebuild to (default is 8)

	Returns:
		PyNode: The rebuilt curve
	"""
	curve = pm.PyNode(curve)

	pm.rebuildCurve(curve,
		ch=True,
		rpo=True,
		rt=0,
		end=1,
		kr=0,
		kcp=False,
		kep=True,
		kt=False,
		s=spans,
		d=3,
		tol=0.01
	)

	return curve
	
import pymel.core as pm    
selected = pm.selected()
crv = create_curve_from_selected(selected[0], selected[1])