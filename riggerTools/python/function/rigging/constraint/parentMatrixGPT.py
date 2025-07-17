'''
from function.rigging.constraint import parentMatrixGPT as mtG
reload(mtG)

sel = mc.ls(sl=True)
mtG.parentConMatrixGPT( sel[0], sel[1], mo = True, translate = True, rotate = True, scale = True)
'''





from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc
import maya.mel as mm
import os
import math
from maya import OpenMaya as om

from function.rigging.autoRig.base import core
reload(core)

from function.pipeline import logger 
reload(logger)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

class Constraint(logger.MayaLogger):
	LOGGER_NAME = "ConstraintGPTLog"



from function.rigging.util import misc
reload(misc)



def _getDagPath(node=None):
	sel = om.MSelectionList()
	sel.add(node)
	dagPath = om.MDagPath()
	sel.getDagPath(0, dagPath)
	return dagPath

def _getLocalOffset(parent, child):
	
	parentWorldMatrix = _getDagPath(parent).inclusiveMatrix()
	childWorldMatrix = _getDagPath(child).inclusiveMatrix()
	#... child World Matrix * invert parent World Matrix = child local matrix
	#... return child local matrix
	return childWorldMatrix * parentWorldMatrix.inverse()



	
def parentConMatrixGPT(source, target, mo=True, translate=True, rotate=True, scale=True):
	"""
	Connects matrix-based parent constraint from source to target with optional translate, rotate, scale
	"""
	if not source:
		print('Source is not selected.')
		return False

	obj_target = core.Dag(target)
	obj_source = core.Dag(source)
	base_name = core.check_name_style(name=target)[0]

	# Match rotate order from source to target
	# (Before connecting anything else)
	source_ro = mc.getAttr(obj_source.name + ".rotateOrder")
	mc.setAttr(obj_target.name + ".rotateOrder", source_ro)

	# Matrix offset setup
	localOffset = _getLocalOffset(source, target)
	offMat = [localOffset(i, j) for i in range(4) for j in range(4)]

	decomposeMatrix = core.DecomposeMatrix(base_name)
	multMatrix = core.MultMatrix(base_name)
	
	Constraint.info(f'This is between [{obj_target.type}] and [{obj_source.type}]')

	if mo:
		mc.setAttr(multMatrix.name + '.matrixIn[0]', offMat, type='matrix')

	if rotate:
		_setup_quaternion_rotation(obj_source, obj_target, base_name, decomposeMatrix)

	obj_source.attr('worldMatrix[0]') >> multMatrix.attr('matrixIn[2]')
	multMatrix.attr('matrixSum') >> decomposeMatrix.attr('inputMatrix')

	_connect_inverse_parent(target, multMatrix)

	if translate:
		decomposeMatrix.attr('outputTranslate') >> obj_target.attr('translate')
	if scale:
		decomposeMatrix.attr('outputScale') >> obj_target.attr('scale')

	decomposeMatrix.attr('message') >> obj_target.attr('m_deComp')

	mc.select(target, r=True)
	Constraint.info('# Parent matrix Complete #')

	return obj_target, obj_source

def _setup_quaternion_rotation(obj_source, obj_target, base_name, decomposeMatrix):
	eulerToQuat = core.EulerToQuat(base_name)
	quatInvert = core.QuatInvert(base_name)
	quatProd = core.QuatProd(base_name)
	quatToEuler = core.QuatToEuler(base_name)

	if obj_target.type == 'joint' and obj_source.type == 'transform':
		Constraint.info(f'Joint->Transform case')
		mc.connectAttr(obj_target.name + '.jointOrient', eulerToQuat.name + '.inputRotate')
	else:
		Constraint.info(f'Generic transform case')
		obj_target.attr('rotate') >> eulerToQuat.attr('inputRotate')

	eulerToQuat.attr('outputQuat') >> quatInvert.attr('inputQuat')
	decomposeMatrix.attr('outputQuat') >> quatProd.attr('input1Quat')
	quatInvert.attr('outputQuat') >> quatProd.attr('input2Quat')
	quatProd.attr('outputQuat') >> quatToEuler.attr('inputQuat')

	quatToEuler.attr('outputRotate') >> obj_target.attr('rotate')
	obj_target.attr('rotateOrder') >> quatToEuler.attr('inputRotateOrder')

	source_rotOrder = mc.getAttr(str(obj_source.name) + '.rotateOrder')
	obj_target.attr('rotateOrder').value = source_rotOrder

	# Clean nodes after connection
	quatInvert.attr('outputQuat') // quatProd.attr('input2Quat')
	eulerToQuat.deleteName()
	quatToEuler.attr('message') >> obj_target.attr('m_quatToEuler')

def _connect_inverse_parent(target, multMatrix):
	parent = mc.pickWalk(target, d='up')[0]
	if parent and parent != target:
		Constraint.warning(f'Checking inverse matrix from parent: {parent}')
		if not mc.listConnections(multMatrix.name + '.matrixIn[2]', s=True, d=False):
			mc.connectAttr(parent + '.worldInverseMatrix[0]', multMatrix.name + '.matrixIn[3]')


