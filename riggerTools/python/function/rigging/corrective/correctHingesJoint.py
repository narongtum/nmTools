
# dir
# rigging.corrective
# fixing -z RGT cause wrong orientation


import logging

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)


# ctrl + shift + r = to use PEP8 formata	

'''
# direct run

from function.rigging.corrective import correctHingesJoint as chj
reload(chj)

'''







def correctHingesJoint(side, parent, child, inAxis, outAxis, inPosVal=2, outPosVal=3, multiplyVal=1,initVal=0.25):
	"""Example function with PEP 484 type annotations.

	Args:
		side: is LFT of RGT only
		parent: name of the parent bindJoint such as upperArm in term of elbow
		child: name of the child bindJoint such as lowerArm
		inAxis: input axis in term of arm is blend the elbow , it should be 'rotateX'
		outAxis: output connection when blend arm so it will be translate 'translateZ'
		inPosVal: The initial position of the inner correctJoint when still not blend
		outPosVal: The initial position of the outter correctJoint when still not blend
		multiplyVal: The multiplier of correctJoint when blend the arm
	Returns:
		return zro_grp object

	"""




	if side == 'LFT':
		i = 1
	elif side == 'RGT':
		i = -1
	else:
		i = 1


	parent_jnt = core.Dag(parent)
	child_jnt = core.Dag(child)

	childNam = child_jnt.name

	if side:
		rawName = childNam.split(side)[0]
		logging.debug('Return rawName is: %s' %rawName)



	else:
		rawName = childNam.split('_')[0]



	# create inner joint
	innerCorrect_jnt = rigTools.jointAt(child)
	innerCorrect_jnt.name = rawName + 'Correct' + 'Inner'+ side + '_pxyJnt'
	# innerCorrect_jnt.parent(corrective_jnt)


	#innerCorrect_jnt.attr('%s' %outAxis).value = initVal * i
	# using move obj for translate 
	innerCorrect_jnt.moveObj( position=[ 0,0, initVal * i ] )



	# create outer joint
	outterCorrect_jnt = rigTools.jointAt( child )
	outterCorrect_jnt.name = rawName + 'Correct' + 'Outter' + side + '_pxyJnt'
	# outterCorrect_jnt.parent(corrective_jnt)



	if inAxis == 'rotateX':
		moveJntAxis = 'rotateZ'
	elif inAxis == 'rotateZ':
		moveJntAxis = 'rotateY'

	outterCorrect_jnt.attr('%s' %moveJntAxis).value = -180 * i
	#outterCorrect_jnt.attr('%s' %outAxis).value = initVal * i * -2
	outterCorrect_jnt.moveObj( position=[ 0,0, initVal * -i ] )



	outterCorrect_jnt.freeze()



	# make grp 
	zro_grp = core.Null(rawName + 'Correct' + side + 'Zro_grp')
	offset_grp = core.Null(rawName + 'Correct' + side + 'Offset_grp')
	offset_grp.parent(zro_grp)
	zro_grp.maSnap(child_jnt)

	# corrective_jnt.parent(offset_grp)


	innerCorrect_jnt.parent(offset_grp)
	outterCorrect_jnt.parent(offset_grp)


	parent_jnt_pointCons = core.pointConstraint(child_jnt, offset_grp, mo = True)
	parent_jnt_pointCons.name = rawName + 'Correct' + side + '_poiCons'

	offset_orientCons = core.orientConstraint(parent_jnt, child_jnt, offset_grp, mo = True)
	offset_orientCons.name = rawName + 'Correct' + side + '_orientCons'



	# multiplier = '%sMul%s' %(rawName,side)
	multiplier = 'Multiplier'

	child_jnt.addAttribute(at='float', keyable=True, ln=multiplier)
	child_jnt.attr(multiplier).value = multiplyVal

	dvDegree_mdl = core.MultiDoubleLinear(rawName + 'DivineDegree' + side + '_mdl')

	# this value come from 1/360 degree
	dvDegree_mdl.attr('input2').value = 0.003
	child_jnt.attr(multiplier) >> dvDegree_mdl.attr('input1')


	# collect value of dvDegree_mdl and and actual rotation
	collectDegree_mdl = core.MultiDoubleLinear(rawName + 'CollectVal' + side + '_mdl')

	dvDegree_mdl.attr('output') >> collectDegree_mdl.attr( 'input1' )
	child_jnt.attr( inAxis ) >> collectDegree_mdl.attr( 'input2' )

	# create condition
	degree_cnd = core.Condition(rawName + 'Degree' + side)
	degree_cnd.suffix

	# invert value (multiple*-1)
	invertVal_mdl = core.MultiDoubleLinear(rawName + 'InvertVal' + side + '_mdl')
	# invertVal_mdl.attr('input2').value = -1 * i
	invertVal_mdl.attr('input2').value = -1

	# connect
	collectDegree_mdl.attr('output') >> invertVal_mdl.attr('input1')

	# connect to condidion
	collectDegree_mdl.attr('output') >> degree_cnd.attr('firstTerm')
	collectDegree_mdl.attr('output') >> degree_cnd.attr('colorIfFalse.colorIfFalseR')
	invertVal_mdl.attr('output') >> degree_cnd.attr('colorIfTrue.colorIfTrueR')






	# # # # # # # # #
	# for Outter joint
	# # # # # # # # #

	section = 'Outter'
	outter_RotationRange_mdl = core.MDLWithMul(rawName + 'RotationRange' + section + side + '_mdl')
	outter_RotationRange_mdl.attr('multiply').value = -10 * i

	degree_cnd.attr('outColor.outColorR') >> outter_RotationRange_mdl.attr('input1')

	# get value of original
	# it shoulde be +2 for RGT
	# trans = abs(outterCorrect_jnt.attr(outAxis).value) # should be abs value
	trans = outterCorrect_jnt.attr(outAxis).value # should be abs value

	outter_oriTrans_adl = core.AddDoubleLinear( rawName + 'OriTrans' + section + side + '_adl' )

	# we will assign value via prior connection
	# outter_oriTrans_adl.attr('input2').value = outPosVal * -1
	# outter_oriTrans_adl.attr('input2').value = trans * 10

	print outter_oriTrans_adl.attr('input2').value

	outter_RotationRange_mdl.attr('output') >> outter_oriTrans_adl.attr('input1')



	# create resistance to make less sentitive
	outter_resistance_mdl = core.MDLWithMul( rawName + 'resisValue' + section + side )
	outter_resistance_mdl.attr('multiply').value = 0.1

	outter_oriTrans_adl.attr('output') >> outter_resistance_mdl.attr('input1')

	# drive to joint
	outter_resistance_mdl.attr('output') >> outterCorrect_jnt.attr(outAxis)




	# bind outter
	# bind multiply value to the middle correct joint
	# rotationRange = rawName + 'RotRange' + section + side
	rotationRange = 'RotationRange' + section
	offsetPosition = 'Position' + section
	# create attr first
	child_jnt.addAttribute(at = 'float', keyable = True, ln =  rotationRange)

	# create correct joint position to main attr
	child_jnt.addAttribute(at = 'float', keyable = True, ln =  offsetPosition)
	# assign value that 10x 
	child_jnt.attr(offsetPosition).value = trans * 10
	child_jnt.attr(offsetPosition) >> outter_oriTrans_adl.attr('input2')


	# get value from rotationRange
	intValue = outter_RotationRange_mdl.attr('multiply').value
	# get value from the old one
	child_jnt.attr(rotationRange).value = intValue
	# connect value
	child_jnt.attr(rotationRange) >> outter_RotationRange_mdl.attr('multiply')









	# set to less than
	if side == 'LFT':
		degree_cnd.attr('operation').value = 4
	elif side == 'RGT':
		degree_cnd.attr('operation').value = 4







	# # # # # # # # #
	# for Inner joint
	# # # # # # # # #

	section = 'Inner'
	inner_RotationRange_mdl = core.MDLWithMul(rawName + 'RotationRange' + section + side + '_mdl')
	inner_RotationRange_mdl.attr('multiply').value = 10 * i

	degree_cnd.attr('outColor.outColorR') >> inner_RotationRange_mdl.attr('input1')

	# get value of original
	# it shoulde be +2 for RGT
	# trans = abs(innerCorrect_jnt.attr(outAxis).value) # should be abs value
	trans = innerCorrect_jnt.attr(outAxis).value # should be abs value

	inner_oriTrans_adl = core.AddDoubleLinear( rawName + 'OriTrans' + section + side + '_adl' )

	# we will assign value via prior connection
	# inner_oriTrans_adl.attr('input2').value = outPosVal * -1
	# inner_oriTrans_adl.attr('input2').value = trans * 10

	print inner_oriTrans_adl.attr('input2').value

	inner_RotationRange_mdl.attr('output') >> inner_oriTrans_adl.attr('input1')



	# create resistance to make less sentitive
	inner_resistance_mdl = core.MDLWithMul( rawName + 'ResisValue' + section + side )
	inner_resistance_mdl.attr('multiply').value = 0.1

	inner_oriTrans_adl.attr('output') >> inner_resistance_mdl.attr('input1')

	# drive to joint
	inner_resistance_mdl.attr('output') >> innerCorrect_jnt.attr(outAxis)



	# bind inner
	# bind multiply value to the middle correct joint
	# rotationRange = rawName + 'RotRange' + section + side
	rotationRange = 'RotationRange' + section
	offsetPosition = 'Position' + section
	# create attr first
	child_jnt.addAttribute(at = 'float', keyable = True, ln =  rotationRange)

	# create correct joint position to main attr
	child_jnt.addAttribute(at = 'float', keyable = True, ln =  offsetPosition)
	# assign value that 10x 
	child_jnt.attr(offsetPosition).value = trans * 10
	child_jnt.attr(offsetPosition) >> inner_oriTrans_adl.attr('input2')


	# get value from rotationRange
	intValue = inner_RotationRange_mdl.attr('multiply').value
	# get value from the old one
	child_jnt.attr(rotationRange).value = intValue
	# connect value
	child_jnt.attr(rotationRange) >> inner_RotationRange_mdl.attr('multiply')




	# lock and hide
	# corrective_jnt.lockHideAttrLst('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')
	innerCorrect_jnt.lockHideAttrLst('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')
	outterCorrect_jnt.lockHideAttrLst('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')


	# create bind joint and snap to it parent
	innerCorrect_bJnt = rigTools.jointAt(innerCorrect_jnt)
	innerCorrect_bJnt.name = rawName + 'Correct' + 'Inner'+ side + '_bJnt'
	innerCorrect_bJnt.freeze()
	innerCorrect_bJnt.parent(child_jnt)
	innerCorrect_bJnt_psCons = core.parentConstraint(innerCorrect_jnt.name ,innerCorrect_bJnt.name , mo=True)
	innerCorrect_bJnt_psCons.name = rawName + 'Correct' + 'Inner' + side
	innerCorrect_bJnt_psCons.suffix


	outterCorrect_bJnt = rigTools.jointAt(outterCorrect_jnt)
	outterCorrect_bJnt.name = rawName + 'Correct' + 'Outter'+ side + '_bJnt'
	outterCorrect_bJnt.freeze()
	outterCorrect_bJnt.parent(child_jnt)
	outterCorrect_bJnt_psCons = core.parentConstraint(outterCorrect_jnt.name ,outterCorrect_bJnt.name , mo=True)
	outterCorrect_bJnt_psCons.name = rawName + 'Correct' + 'Outter'+ side
	outterCorrect_bJnt_psCons.suffix




	# clean up 
	zro_grp.attr('visibility').value = 0

	innerCorrect_bJnt.attr('radius').value = 1.5
	innerCorrect_bJnt.setJointColor('white')
	innerCorrect_jnt.attr('segmentScaleCompensate').value = 0
	innerCorrect_bJnt.attr('segmentScaleCompensate').value = 0

	outterCorrect_bJnt.attr('radius').value = 1.5
	outterCorrect_bJnt.setJointColor('white')
	outterCorrect_jnt.attr('segmentScaleCompensate').value = 0
	outterCorrect_bJnt.attr('segmentScaleCompensate').value = 0




	logging.debug('End of program')
	core.makeHeader( 'End of Correct segment %s %s function' %(rawName, side) )

	# return object
	return zro_grp






"""side = 'LFT' 
parent = 'upperArmLFT_bJnt'
child = 'lowerArmLFT_bJnt'
inAxis = 'rotateX'
outAxis = 'translateZ'
inPosVal = 0.2
outPosVal = 0.3
multiplyVal = 0.15
initVal = 0.25"""






'''
from function.rigging.corrective import correctHingesJoint as chj
reload(chj)

oElbowLFT = chj.correctHingesJoint(side = 'LFT', parent='upperArmLFT_bJnt', child='lowerArmLFT_bJnt', 
			inAxis='rotateX', outAxis='translateZ', inPosVal=0.2, outPosVal=0.3, multiplyVal=1.2,initVal = 0.25)
oElbowRGT = chj.correctHingesJoint(side = 'RGT', parent='upperArmRGT_bJnt', child='lowerArmRGT_bJnt', 
			inAxis='rotateX', outAxis='translateZ', inPosVal=0.2, outPosVal=0.3, multiplyVal=1.2,initVal = 0.25)

oBottonLFT = chj.correctHingesJoint(side = 'LFT', parent='hip_bJnt', child='upperLegLFT_bJnt', 
			inAxis='rotateX', outAxis='translateZ', inPosVal=0.2, outPosVal=0.3, multiplyVal=1.2,initVal = 0.25)
oBottonRGT = chj.correctHingesJoint(side = 'RGT', parent='hip_bJnt', child='upperLegRGT_bJnt', 
			inAxis='rotateX', outAxis='translateZ', inPosVal=0.2, outPosVal=0.3, multiplyVal=1.2,initVal = 0.25)

oKneeLFT = chj.correctHingesJoint(side = 'LFT', parent='upperLegLFT_bJnt', child='lowerLegLFT_bJnt', 
			inAxis='rotateX', outAxis='translateZ', inPosVal=0.2, outPosVal=0.3, multiplyVal=1.2,initVal = 0.25)
oKneeRGT = chj.correctHingesJoint(side = 'RGT', parent='upperLegRGT_bJnt', child='lowerLegRGT_bJnt', 
			inAxis='rotateX', outAxis='translateZ', inPosVal=0.2, outPosVal=0.3, multiplyVal=1.2,initVal = 0.25)
'''


