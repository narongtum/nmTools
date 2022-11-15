#... Finger value preservation use name as Auxiliary joint
#... Source 22.10.Oct.03.Mon.11_Finger Rig Value Preservation\version
#... Reference https://www.youtube.com/watch?v=kX87iTaRyhs

#... how to use #
#... 1. adjust orientation y along 
#... 2. spectify the joint that

'''
# Direct run
from function.rigging.corrective import valuePreservation as vpa
reload(vpa)
'''
import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)

#... default value
# middleJnt = 'lwrArmLFT_bJnt'
# side = 'LFT'
# auxPosiWeight = 0.95
# baseName = 'elbow'
# sensitiveOut = 1.2
# sensitiveInn = 0.2
# intial_posIn = 2.2
# intial_posOut = 3

def valuePreservation(		middleJnt = 'lwrArmLFT_bJnt',
							side = 'LFT'				,
							auxPosiWeight = 0.95		,
							baseName = 'elbow'			,
							sensitiveOut = 1.2			,
							sensitiveInn = 0.2			,
							intial_posIn = 2.2			,
							intial_posOut = 3			,
							moveAxis = 'x'	):

	core.makeHeader('START of function.')

	if side:
	    side = misc.findSide(middleJnt)
	    index = middleJnt.index(side)
	    baseName = middleJnt[:index]



	#... find parent and child
	mc.select(middleJnt, r=True)
	mc.pickWalk(direction='up')
	prior_jnt = mc.ls(sl=True)[0]

	prior_jnt = core.Dag(prior_jnt)
	middle_jnt = core.Dag(middleJnt)

	translate_blend_mat = core.BlendMatrix('{0}_translate{1}'.format(baseName,side))
	rotate_blend_mat = core.BlendMatrix('{0}_rotate{1}'.format(baseName,side))

	middle_jnt.attr('matrix') >> translate_blend_mat.attr('target[0].targetMatrix')
	middle_jnt.attr('matrix') >> rotate_blend_mat.attr('target[0].targetMatrix')

	#... set attr for blend matrix translate
	translate_blend_mat.attr('target[0].weight').value = auxPosiWeight
	translate_blend_mat.attr('target[0].scaleWeight').value = 0
	translate_blend_mat.attr('target[0].translateWeight').value = 1
	translate_blend_mat.attr('target[0].rotateWeight').value = 0
	translate_blend_mat.attr('target[0].shearWeight').value = 0

	#...set attr for blend matrix rotate
	rotate_blend_mat.attr('target[0].scaleWeight').value = 0
	rotate_blend_mat.attr('target[0].translateWeight').value = 0
	rotate_blend_mat.attr('target[0].rotateWeight').value = 0.5
	rotate_blend_mat.attr('target[0].shearWeight').value = 0


	collect_mat = core.MultMatrix('{0}_collect{1}'.format(baseName,side))
	rotate_blend_mat.attr('outputMatrix') >> collect_mat.attr('matrixIn[0]')
	translate_blend_mat.attr('outputMatrix') >> collect_mat.attr('matrixIn[1]')

	#...create aux joint
	middle_auxJnt = core.Joint('{0}_auxJnt'.format(baseName))
	middle_auxJnt.setJointOutlineColor('white')
	#...parent under father joint
	middle_auxJnt.parent(prior_jnt)
	middle_auxJnt.setJointColor('white')
	middle_auxJnt.attr('radius').value = 2

	#... reset position
	middle_auxJnt.attr('translateX').value = 0
	middle_auxJnt.attr('translateY').value = 0
	middle_auxJnt.attr('translateZ').value = 0
	middle_auxJnt.attr('jointOrientZ').value = 0
	collect_mat.attr('matrixSum') >> middle_auxJnt.attr('offsetParentMatrix')


	#... create Inner Outer aux joint
	eulerToQuat = core.EulerToQuat('{0}Rot{1}'.format(baseName,side))
	quatToEuler = core.QuatToEuler('{0}Rot{1}'.format(baseName,side))
	multiplyRotValue = core.MDLWithMul('{0}MulVal{1}'.format(baseName,side), dv=-1)
	remapRotValue = core.RemapCurve('{0}_MulVal{1}'.format(baseName,side), True, defaultValue = (0,90,0,1))
	middle_jnt.attr('rotate') >> eulerToQuat.attr('inputRotate')


	#... use for RotZ only
	eulerToQuat.attr('outputQuatZ') >> quatToEuler.attr('inputQuatZ')
	eulerToQuat.attr('outputQuatW') >> quatToEuler.attr('inputQuatW')

	quatToEuler.attr('outputRotate.outputRotateZ') >> multiplyRotValue.attr('input1')
	multiplyRotValue.attr('output')>> remapRotValue.attr('inputValue')

	mulPosiInn_mdl = core.MDLWithMul('{0}Sensitive_Inn{1}'.format(baseName,side), dv = sensitiveInn )
	mulPosiOut_mdl = core.MDLWithMul('{0}Sensitive_Out{1}'.format(baseName,side), dv = sensitiveOut )

	remapRotValue.attr('outValue') >> mulPosiInn_mdl.attr('input1')
	remapRotValue.attr('outValue') >> mulPosiOut_mdl.attr('input1')

	#... inticial position
	intial_pos_Inn_adl = core.AddDoubleLinear('{0}intialPos_Inn{1}_adl'.format(baseName,side), input2 = intial_posIn)
	intial_pos_Out_adl = core.AddDoubleLinear('{0}intialPos_Out{1}_adl'.format(baseName,side), input2 = intial_posOut)

	mulPosiInn_mdl.attr('output') >> intial_pos_Inn_adl.attr('input1')
	mulPosiOut_mdl.attr('output') >> intial_pos_Out_adl.attr('input1')

	inner_auxJnt = core.Joint('{0}Inn{1}_auxJnt'.format(baseName,side))
	inner_auxJnt.setJointOutlineColor('white')
	outer_auxJnt = core.Joint('{0}Outer{1}_auxJnt'.format(baseName,side))
	outer_auxJnt.setJointOutlineColor('white')

	inner_auxJnt.parent(middle_auxJnt)
	inner_auxJnt.attr('translateX').value = 0
	inner_auxJnt.attr('translateY').value = 0
	inner_auxJnt.attr('translateZ').value = 0

	outer_auxJnt.parent(middle_auxJnt)
	outer_auxJnt.attr('translateX').value = 0
	outer_auxJnt.attr('translateY').value = 0
	outer_auxJnt.attr('translateZ').value = 0

	#... create invert value for outer
	reverseVal_mdl = core.MDLWithMul('{0}ReverseVal{1}'.format(baseName,side), -1)
	intial_pos_Out_adl.attr('output') >> reverseVal_mdl.attr('input1')
	reverseVal_mdl.attr('output') >> outer_auxJnt.attr('translate{0}'.format(moveAxis.capitalize()		))
	intial_pos_Inn_adl.attr('output')>> inner_auxJnt.attr('translate{0}'.format(moveAxis.capitalize()	))

	#... create attr at middle aux joint
	middle_auxJnt.addAttribute(at = 'enum', keyable = True , en = '###:', longName = 'Setting'  )
	middle_auxJnt.addAttribute(at = 'float', longName = 'auxPosiWeight', keyable = True, defaultValue = auxPosiWeight )
	middle_auxJnt.addAttribute(at = 'float', longName = 'sensitive_out', keyable = True, defaultValue = sensitiveOut )
	middle_auxJnt.addAttribute(at = 'float', longName = 'sensitive_in', keyable = True, defaultValue = sensitiveInn )
	middle_auxJnt.addAttribute(at = 'float', longName = 'intial_pos_in', keyable = True, defaultValue = intial_posIn )
	middle_auxJnt.addAttribute(at = 'float', longName = 'intial_pos_out', keyable = True, defaultValue = intial_posOut )

	#... connect value

	middle_auxJnt.attr('auxPosiWeight') >> translate_blend_mat.attr('target[0].weight')
	middle_auxJnt.attr('sensitive_out') >> mulPosiOut_mdl.attr('multiply')
	middle_auxJnt.attr('sensitive_in') >>  mulPosiInn_mdl.attr('multiply')
	middle_auxJnt.attr('intial_pos_in') >> intial_pos_Inn_adl.attr('input2')
	middle_auxJnt.attr('intial_pos_out') >> intial_pos_Out_adl.attr('input2')

	core.makeHeader('END')