# -*- coding: utf-8 -*-

from __future__ import division

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc as misc
reload(misc)


"""
1. Function create locator attatch at curve
it will create at 3 point start mid end point

 [+]-----[+]------[+]

 2. For support blendshape deformation

 move to Feature module

"""







def jointAttchToCurve(numJoints = 3, nurbSize = 0.5):
	"""
	Args:
		numJoints (int): Number of joint.
		nurbSize (int): Size of the nurb controller(use nurb instead curve).

	Returns:
		None

	"""
	# Curve Length are alway 1
	length = 1

	select  = mc.ls(sl=True)[0]

	if select:

		side = misc.findSide(select)
		#part = 'lwrLip'
		subText = side + '_crv'

		part = select.split(subText)[0]


		#	for each in range (0 , numJoints ):
		#   uVal = ((0.5 / numJoints) * (each + 1) * 2) - ((0.5 / (numJoints * 2)) * 2)

		value = length / (numJoints-1)

		# for each in range (0 , region):
		# for each in region:

		for each in range (0 , numJoints ):

			curve = core.Dag( '%s%s_crv' %(part,side) )
			ctrlShape = core.Dag( curve.shape )
			pointOnCurve = core.PointOnCurveInfo('%s%02d%s' %(part,each+1,side) )
			locator = core.Locator('%s%02d%s_loc' %(part,each+1,side) )
			locatorShape = core.Dag( locator.shape )

			# make locator smaller
			for axis in 'XYZ':
				print axis
				locatorShape.attr('localScale%s' %axis).value = 0.01


			ctrlShape.attr('worldSpace[0]') >> pointOnCurve.attr( 'inputCurve' )
			pointOnCurve.attr( 'result.position' ) >> locator.attr('translate')
			pointOnCurve.attr( 'turnOnPercentage' ).value = 1


			val = each * value

			print 'percnet is %d' %val
			pointOnCurve.attr( 'parameter' ).value = val

			'''
			jointOffset = core.Joint()
			jointOffset.name = '%s%d%s_jnt' %(part,each,side)
			jointOffset.attr('radius').value = nurbSize
			'''


			jointCtrl = core.Joint()
			jointCtrl.name = '%s%02d%s_pxyJnt' %(part,each+1,side)
			jointCtrl.attr('radius').value = nurbSize
			# make them gray
			jointCtrl.attr('overrideEnabled').value = 1
			jointCtrl.attr('overrideColor').value = 3


			# jointCtrl.parent( jointOffset )
			
			# jointOffset.snap(locator)


			nurb = core.Nurb( '%s%02d%s_ctrl' %(part,each+1,side) )
			nurb.sphere( r = nurbSize )

			nurb.snap(locator)
			nurb.parent(locator)
			
			
			jointCtrl.snap(locator)
			jointCtrl.parent(nurb)
			#nurb.deleteName(constructionHistory = True)

			#core.parentShape( parent = nurb.name , child = jointCtrl.name  )
	else:
		mc.error('Curve Source not found.')



# make nrb big or smaller
# mc.select('*_nrb' , r = True)
# freeze transform
# delete history