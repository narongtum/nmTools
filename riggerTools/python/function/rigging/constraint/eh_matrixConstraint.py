# ... parentConMatrix by Fully Generative AI


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
	LOGGER_NAME = "EH_MatrixConstraintLog"

from function.rigging.util import misc
reload(misc)



def _getLocalOffsetGPT(source, target):

	source_world = _getDagPath(source).inclusiveMatrix()
	target_world = _getDagPath(target).inclusiveMatrix()

	# offset matrix: transforms target into local space of source
	offset_matrix = target_world * source_world.inverse()
	return offset_matrix



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




	



# ... inside matrixConstraint.py

def parentConMatrix(source, target, mo = True, translate = True, rotate = True, scale = True):

	if not source:
		print('Source is not selected.')
		return False

	#... rotate offset function
	obj_target = core.Dag(target)
	obj_source = core.Dag(source)

	#... find base name
	base_name = core.check_name_style(name = target)[0]

	#...Got call maya API for get local offset position  
	localOffset =  _getLocalOffset( source, target )
	offMat = [localOffset(i,j) for i in range(4) for j in range(4)]

	#... Create
	decomposeMatrix = core.DecomposeMatrix(base_name)
	multMatrix = core.MultMatrix(base_name)

	#... Notice
	Constraint.info('This is between [ {0} ] and [ {1} ]'.format(obj_target.type, obj_source.type))

	#... Set and Connect
	if mo == True:
		mc.setAttr( multMatrix.name + '.matrixIn[0]', offMat, type = 'matrix')

	#... START OF ROTATE CONNECTION
	if rotate == True:
		
		#... Create Rotation Calculation Nodes
		target_eulerToQuat = core.EulerToQuat(base_name)
		target_quatInvert = core.QuatInvert(base_name)
		target_quatProd = core.QuatProd(base_name)
		target_quatToEuler = core.QuatToEuler(base_name)

		# -----------------------------------------------------------------------
		# [FIX] Cycle Check Logic
		# -----------------------------------------------------------------------
		if obj_target.type == 'joint': 
			# If target is a JOINT, we MUST compensate for jointOrient.
			# Joint Orient is static, so it won't cause a cycle.
			Constraint.info(f'Compensating Joint Orient for [ {obj_target.name} ]')
			mc.connectAttr( obj_target.name + '.jointOrient', target_eulerToQuat.name + '.inputRotate' )

		else:
			# If target is TRANSFORM (or anything else), we relies entirely on the Matrix Offset (matrixIn[0]).
			# DO NOT connect obj_target.rotate here. It causes a Cycle Warning.
			# We leave inputRotate as (0,0,0) effectively bypassing the compensation.
			Constraint.info(f'Transform Target [ {obj_target.name} ]: Using Matrix Offset. No Quat compensation needed.')
			pass

		# -----------------------------------------------------------------------

		#... Connect the rest of the Quat chain
		target_eulerToQuat.attr('outputQuat') >> target_quatInvert.attr('inputQuat')
		decomposeMatrix.attr('outputQuat') >> target_quatProd.attr('input1Quat')
			
		target_quatInvert.attr('outputQuat') >> target_quatProd.attr('input2Quat')	
		target_quatProd.attr('outputQuat') >> target_quatToEuler.attr('inputQuat')

		#... Force the rotateOrder
		source_rotOrder = mc.getAttr( str(source) + '.rotateOrder' )
		obj_target.attr('rotateOrder').value = source_rotOrder

		target_quatToEuler.attr('outputRotate') >> obj_target.attr('rotate')

		#... Connect rotate order
		obj_target.attr('rotateOrder') >> target_quatToEuler.attr('inputRotateOrder')
	
	#... END OF ROTATE CONNECTION

	obj_source.attr('worldMatrix[0]') >> multMatrix.attr('matrixIn[2]')

	#... Insert pickmatrix for make it more option
	pickMatrix = core.PickMatrix(base_name)

	multMatrix.attr('matrixSum') >> pickMatrix.attr('inputMatrix')
	pickMatrix.attr('outputMatrix') >> decomposeMatrix.attr('inputMatrix')

	#... Find out Origin Parent
	if mc.pickWalk( target , d = 'up')[0] == target:
		logger.MayaLogger.info("I'm World Already")
	elif mc.pickWalk( target, d = 'up')[0] != target:
		world = mc.pickWalk( target, d = 'up')[0]
		# Constraint.warning('Warning .matrixIn[2] may occupire. consider to fix it.')
		if mc.listConnections(multMatrix.name + '.matrixIn[2]')[0]:
			mc.connectAttr( world + '.worldInverseMatrix[0]', multMatrix.name + '.matrixIn[3]' )
		else:
			mc.connectAttr( world + '.worldInverseMatrix[0]', multMatrix.name + '.matrixIn[2]' )


	#... Connect TS
	if translate == True:
		decomposeMatrix.attr('outputTranslate') >> obj_target.attr('translate')
		
	if scale == True:
		decomposeMatrix.attr('outputScale') >> obj_target.attr('scale')
		

	#... Clear Node
	if rotate:
		target_quatInvert.attr('outputQuat') // target_quatProd.attr('input2Quat')
		target_eulerToQuat.deleteName()

	#... [Fix] Create Message Attributes if they don't exist
	if not mc.attributeQuery('m_deComp', node=obj_target.name, exists=True):
		obj_target.addAttribute( attributeType = 'message' , longName = 'm_deComp')
	
	if not mc.attributeQuery('m_quatToEuler', node=obj_target.name, exists=True):
		obj_target.addAttribute( attributeType = 'message' , longName = 'm_quatToEuler')

	#... Connect Message
	decomposeMatrix.attr('message') >> obj_target.attr('m_deComp')
	if rotate:
		target_quatToEuler.attr('message') >> obj_target.attr('m_quatToEuler')

	mc.select(target, r=True)

	Constraint.info(' # # # # # # # # # Parent matrix Complete # # # # # # # # # # # #  \n')
	return obj_target, obj_source