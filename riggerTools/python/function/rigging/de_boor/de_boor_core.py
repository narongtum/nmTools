#... de_boor_core type follow tutor

'''
from function.rigging.de_boor import de_boor_core as de_boor
reload(de_boor)
'''









def get_open_uniform_kv(n, d):

	"""
	Get uniform knot vector
	Example:
		#... n is control vertex
		#... d is degree
		get_open_uniform_kv(4, 1)
		get_open_uniform_kv(4, 2)
		get_open_uniform_kv(4, 3)

	Attributes:
		n(integer): the number of control vertices
		d(integer): the degree of output
	"""

	return [0] * (d+1) + [(i-d) / (n-d) for i in range(d+1,n)] + [1]*(d+1)
	

def get_periodic_uniform_kv(n, d):

	"""
	Get periodic uniform knot vector. Append d values to the start and end

	Examples:
		get_periodic_uniform_kv(4,2)

	Attributes:
		n(integer): the number of control vertices
		d(integer): the degree of output

	"""
	i = 1.0 / (n+d)
	return [-i * a for a in range(d,0,-1)] + [i*a for a in range(n+d+1)] + [i*a+1 for a in range(1,d+1)]



def knot_vector(kv_type, cvs, d):
	cvs_copy = cvs[:]
	if kv_type == 'open':
			kv = get_open_uniform_kv(len(cvs), d)
	else:
		kv = get_periodic_uniform_kv(len(cvs), d)

		for i in range(d):
			cvs_copy.insert(0, cvs[len(cvs) - i - 1])
			cvs_copy.append(cvs[i])

	return kv, cvs_copy





def de_boor(n, d, t, kv, tol = 0.0000001):
	if t + tol > 1:
		return [0.0 if i != n-1 else 1.0 for i in range(n)]

	weights = [1.0 if kv[i] <= kv[i+1] else 0.0 for i in range(n+d)]

	basis_width = n + d - 1

	for degree in range(1, d+1):
		for i in range(basis_width):
			if weights[i] == 0 and weights[i+1] == 0:

				continue

			a_denom = kv[i+degree] - kv[i]
			b_denom = kv[i+degree+1] - kv[i+1]
			a = (t - kv[i]) * weights[i] / a_denom if a_denom != 0 else 0.0

			b = (kv[i + degree + 1] - t) * weights[i + 1] / b_denom if b_denom != 0 else 0.0

			weights[i] = a + b

		basis_width -= 1

	return weights[:n]
# hah