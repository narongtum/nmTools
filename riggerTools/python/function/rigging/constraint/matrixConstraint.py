#... All about matrix constraint


# D:\narongtum\research_and_developement\22.08.Aug.19.Fri.14_Imprement Parent Matrix

'''
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)
sel = mc.ls(sl=True)
mtc.parentConMatrix( sel[0], sel[1], mo = True, translate = True, rotate = True, scale = True)

'''




'''
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

'''







'''
from function.rigging.util import misc as misc
from function.framework.reloadWrapper import reloadWrapper as reload
reload(misc)
sel = mc.ls(sl=True)
misc.parentMatrix( sel[0], sel[1], mo = True, translate = True, rotate = True, scale = True)
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
	LOGGER_NAME = "ConstraintLog"



from function.rigging.util import misc
reload(misc)

'''
from function.rigging.util import misc as misc
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)
sel = mc.ls(sl=True)
mtc.del_selected_matrix(selected = sel)
'''


#.... Cut from Util.Misc

def del_selected_matrix(selected = []):
	#... Get short name
	mulMtx = mnd.get_short_name('multMatrix')
	quat = mnd.get_short_name('quatToEuler')
	deComp = mnd.get_short_name('decomposeMatrix')

	for each in selected:
		list_sel = mc.listConnections(each, destination=True)

		for each in list_sel:
			try:
				# .. because after delete it will can't find the rest
				# if each.endswith('_dmpMtx'):
					# logger.MayaLogger.info('Delete %s' %each)
					# mc.delete(each)
				if each.endswith(mulMtx):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)
				if each.endswith(quat):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)
				if each.endswith(deComp):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)

			except:
				print('There are no matrix node to delete.')
	print('Delete Done...')


def delMatrixConst(selected):
	name = rawName(selected)
	mc.delete('{0}_bJnt_mulMtx'.format(name[0]))
	print (' # # # # # # # # #  Delete matrix parent complete # # # # # # # # # # # #  \n')






# misc.parentSufficMatrix( child = 'bJnt' , parent = 'pxyJnt' , mo = True, w = 1, t = True, r = True, s = True )
def parentSufficMatrix( child = '' , parent = '' , mo = True, w = 1, t = True, r = True, s = True):
	logger.MayaLogger.info('Start of %s module' %__name__)
	# constraint use prefix suffix only #
	naming = '*_' + parent
	proxyList = mc.ls( naming )

	for each in proxyList:
		#... using condition
		baseName = misc.check_name_style(each)[0]
		# spEach = each.split('_')
		
		childNam = baseName + '_' + child
		parentConMatrix( each , childNam, mo = mo, translate = t, rotate = r, scale = s)
		print ('parent %s >>> %s' %(each , childNam))

	print ('\t\t\t### constraint matrix complete ###')

# parent multi martix
def parentMulMatrix( src, tgt, mo = True, t = True, r = True, s = True):
	''' parent constraint one source but multiple target matrix'''
	
	# Name
	mulMtx = tgt + '_mulMtx'
	dmpMtx = tgt + '_dmpMtx'
	wtMtx = tgt + '_wtMtx'

	# Create
	mc.createNode( 'multMatrix', n = mulMtx )
	mc.createNode( 'decomposeMatrix', n = dmpMtx )
	mc.createNode( 'wtAddMatrix', n = wtMtx )

	# For many parent
	for p in range(len(src)):
		parent = src[p]
		#parentName = parent.split('_')[0]
		offsetMtx = tgt + '_' + parent + 'Offset_mulMtx'

		# Create
		mc.createNode( 'multMatrix', n = offsetMtx )

		# preFUNC
		localOffset =  getLocalOffset( parent, tgt )
		offMat = [localOffset(i,j) for i in range(4) for j in range(4)]

		#  Set and Connect
		if mo == True:

			mc.setAttr( offsetMtx + '.matrixIn[0]', offMat , type = 'matrix')

		mc.connectAttr( parent + '.worldMatrix[0]', offsetMtx + '.matrixIn[1]' )
		mc.connectAttr( offsetMtx + '.matrixSum', wtMtx + '.wtMatrix[%d].matrixIn'%(p))
		if p == 0:
			mc.setAttr( wtMtx + '.wtMatrix[%d].weightIn'%(p), 1)


	# Main wt connect
	mc.connectAttr( wtMtx + '.matrixSum',  mulMtx + '.matrixIn[0]' )

	# Find out Origin Parent
	if mc.pickWalk( tgt , d = 'up')[0] == tgt:
		print ("I'm World Already")
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[1]' )

	# Final Connect
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	# 
	if r == True:
		rotateOffset(tgt, dmpMtx, mulMtx)
	if t == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if s == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale') 
	
	return wtMtx


# ex: parentThis()
def parentThis( mo = True, t = True, r = True, s = True):
	''' select source and targer '''
	sel = mc.ls(sl=1)
	if len(sel) > 2:
		child = sel[-1]        
		del sel[-1]
		parentMulMatrix( src = sel , tgt = child,  mo = mo, t = t, r = r, s = s)
		print (sel)
	elif len(sel) == 2:
		print (sel)
		parentMatrix( sel[0] , sel[-1],  mo = mo, t = t, r = r, s = s)
























#... Util for qury offset matrix


#... Create mult matrix that contain offsetMatrix just create for demonstrate not connect anywhere
def create_offset_matrix(source, target, mo = True, translate = True, rotate = True, scale = True):

	# createMatrixAttr()

	if not source:
		print('source is not selected.')
		return 0

	#... rotate offset function
	obj_target = core.Dag(target)
	obj_source = core.Dag(source)

	#...Got call maya API for get local offset position  
	localOffset =  _getLocalOffset( source, target )
	offMat = [localOffset(i,j) for i in range(4) for j in range(4)]

	#... Create
	decomposeMatrix = core.DecomposeMatrix(target)
	multMatrix = core.MultMatrix(target)


	#... Notice
	Constraint.info('This is between [ {0} ] and [ {1} ]'.format(obj_target.type, obj_source.type))

	#... Set and Connect
	if mo == True:
		attrNam = 'destination'
		mc.addAttr(multMatrix.name, ln = 'offsetMatrix_{0}'.format(attrNam), at='matrix')
		mc.setAttr('{0}.offsetMatrix_{1}'.format(multMatrix.name, attrNam), offMat, type = 'matrix')

	Constraint.info('done')









#... constraint parent suffix name to bind suffix name
def matrixConListJnt( namJntList = [] , child = 'bind_jnt', parent = 'proxy_jnt' ):
	namLst = []
	for each in namJntList:
		fitstNam = misc.splitName( each )[0]
		namLst.append( fitstNam )

	
	for each in namLst:
		parentNam = each + '_' + parent
		childNam = each + '_' + child

		print('This is parentNam >>> {}'.format(parentNam))
		print('This is childNam >>> {}'.format(childNam))

		parentConMatrix(parentNam, childNam, mo = True, translate = True, rotate = True, scale = True)














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



def createMatrixAttr(selected, attrNam = 'destination'):
	mc.addAttr(selected, ln = 'offsetMatrix_{0}'.format(attrNam), at='matrix')








def parentConMatrixGPT(source, target, mo=True, translate=True, rotate=True, scale=True):
	if not source:
		print('Source is not selected.')
		return False

	# Setup core object references
	obj_target = core.Dag(target)
	obj_source = core.Dag(source)
	base_name = core.check_name_style(name=target)[0]

	# Compute offset matrix
	localOffset = _getLocalOffsetGPT(source, target)
	offMat = [localOffset(i, j) for i in range(4) for j in range(4)]

	# Create necessary nodes
	decomposeMatrix = core.DecomposeMatrix(base_name)
	multMatrix = core.MultMatrix(base_name)

	Constraint.info('This is between [ {0} ] and [ {1} ]'.format(obj_target.type, obj_source.type))

	# Maintain Offset: use multMatrix slot 0 for offset, 1 for worldMatrix, 2 for inverse
	if mo:
		mc.setAttr(multMatrix.name + '.matrixIn[0]', offMat, type='matrix')
		obj_source.attr('worldMatrix[0]') >> multMatrix.attr('matrixIn[1]')
		obj_target.attr('parentInverseMatrix[0]') >> multMatrix.attr('matrixIn[2]')
	else:
		obj_source.attr('worldMatrix[0]') >> multMatrix.attr('matrixIn[0]')
		obj_target.attr('parentInverseMatrix[0]') >> multMatrix.attr('matrixIn[1]')

	# Rotation setup
	if rotate:
		target_eulerToQuat = core.EulerToQuat(base_name)
		target_quatInvert = core.QuatInvert(base_name)
		target_quatProd = core.QuatProd(base_name)
		target_quatToEuler = core.QuatToEuler(base_name)

		#  alway jointOrient if target is joint
		if obj_target.type == 'joint':
			mc.connectAttr(obj_target.name + '.jointOrient', target_eulerToQuat.name + '.inputRotate')
			target_eulerToQuat.attr('outputQuat') >> target_quatInvert.attr('inputQuat')
		else:
			obj_source.attr('rotate') >> target_eulerToQuat.attr('inputRotate')
			obj_source.attr('rotateOrder') >> target_eulerToQuat.attr('inputRotateOrder')
			target_eulerToQuat.attr('outputQuat') >> target_quatInvert.attr('inputQuat')

		decomposeMatrix.attr('outputQuat') >> target_quatProd.attr('input1Quat')
		target_quatInvert.attr('outputQuat') >> target_quatProd.attr('input2Quat')
		target_quatProd.attr('outputQuat') >> target_quatToEuler.attr('inputQuat')
		target_quatToEuler.attr('outputRotate') >> obj_target.attr('rotate')

		if not mc.listConnections(obj_target.attr('rotateOrder'), d=False, s=True):
			obj_target.attr('rotateOrder') >> target_quatToEuler.attr('inputRotateOrder')

		source_rotOrder = mc.getAttr(str(source) + '.rotateOrder')
		obj_target.attr('rotateOrder').value = source_rotOrder


	# Connect matrix calculation
	multMatrix.attr('matrixSum') >> decomposeMatrix.attr('inputMatrix')

	# Translate
	if translate:
		decomposeMatrix.attr('outputTranslate') >> obj_target.attr('translate')

	# Scale
	if scale:
		decomposeMatrix.attr('outputScale') >> obj_target.attr('scale')

	if not mc.objExists(obj_target.name + '.m_deComp'):
		obj_target.addAttribute(attributeType='message', longName='m_deComp')
		decomposeMatrix.attr('message') >> obj_target.attr('m_deComp')



	mc.select(target, r=True)
	Constraint.info(' # # # # # # # # # Parent matrix Complete # # # # # # # # # # # #  \n')
	return obj_target, obj_source





#... parant constraint using matrix use this Mainly	
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

	#... Just in case for add manual attr
	#obj_source.addAttribute( ln = 'localOffset' , k = False, at = 'matrix' )
	#mc.setAttr( obj_source.name + '.localOffset', offMat, type = 'matrix')


	#... START OF ROTATE CONNECTION
	if rotate == True:
		pass

	#... START HERE
	target_eulerToQuat = core.EulerToQuat(base_name)
	target_quatInvert = core.QuatInvert(base_name)
	target_quatProd = core.QuatProd(base_name)
	target_quatToEuler = core.QuatToEuler(base_name)


	if obj_target.type == 'joint' and obj_source.type == 'transform': #... if between transform to joint must add value from orient
		Constraint.info('\nThis is between [ {1} ] and [ {0} ]'.format(obj_target.type, obj_source.type))
		#... YOU MISS THIS LINE EVERYTHING WILL FALL
		mc.connectAttr( obj_target.name + '.jointOrient', target_eulerToQuat.name + '.inputRotate' )


	elif obj_target.type == 'transform' and obj_source.type == 'transform':

		print('\n')
		Constraint.info('\nThis is between [ {1} ] and [ {0} ]'.format(obj_target.type, obj_source.type))
		print('\n')

		#... Add compose matrix for get offset orientation
		# target_composeMat = core.ComposeMatrix(target)
		#... Update more arttr for case joint(freezed) is parent grp is child
		# obj_target.attr('rotate') >> target_composeMat.attr('inputRotate')
		# obj_target.attr('rotate') // target_composeMat.attr('inputRotate')
		# target_composeMat.attr('outputMatrix') >> multMatrix.attr('matrixIn[1]')
		obj_target.attr('rotate') >> target_eulerToQuat.attr('inputRotate')		

	else:
		Constraint.info("\nThis is maybe something I don't know.")
		obj_target.attr('rotate') >> target_eulerToQuat.attr('inputRotate')
		
		
	#... Connect the rest
	target_eulerToQuat.attr('outputQuat') >> target_quatInvert.attr('inputQuat')
	decomposeMatrix.attr('outputQuat') >> target_quatProd.attr('input1Quat')
		
	target_quatInvert.attr('outputQuat') >> target_quatProd.attr('input2Quat')	
	target_quatProd.attr('outputQuat') >> target_quatToEuler.attr('inputQuat')


	#... Force the rotateOrder of target to the same as source
	# rotOrder = mc.getAttr( target + '.rotateOrder' )

	Constraint.info(type(source))
	source_rotOrder = mc.getAttr( str(source) + '.rotateOrder' )
	obj_target.attr('rotateOrder').value = source_rotOrder

	#target_quatToEuler.attr('inputRotateOrder').value = source_rotOrder

	# mc.setAttr( obj_target + '.rotateOrder' )

	#... can't remember why put this.
	#... Assign value by manual(not use now)
	'''
	allChanel = ['X','Y','Z','W']
	for chanel in allChanel:
		target_quatInvert.attr('outputQuat.outputQuatX').value
		quaVar = mc.getAttr( target_quatInvert.name + '.outputQuat.outputQuat' + chanel )
		mc.setAttr( target_quatProd.name + '.input2Quat.input2Quat' + chanel, quaVar)
	 
	'''


	target_quatToEuler.attr('outputRotate') >> obj_target.attr('rotate')
	#return target_quatToEuler

	#... Connnect rotate order from target to quat to euler 
	obj_target.attr('rotateOrder') >> target_quatToEuler.attr('inputRotateOrder')
	# END HERE


	obj_source.attr('worldMatrix[0]') >> multMatrix.attr('matrixIn[2]')
	multMatrix.attr('matrixSum') >> decomposeMatrix.attr('inputMatrix')


	#... END OF ROTATE CONNECTION



	#...Find out Origin Parent
	if mc.pickWalk( target , d = 'up')[0] == target:
		logger.MayaLogger.info("I'm World Already")
	elif mc.pickWalk( target, d = 'up')[0] != target:
		world = mc.pickWalk( target, d = 'up')[0]
		Constraint.warning('Warning .matrixIn[2] may occupire. consider to fix it.')
		if mc.listConnections(multMatrix.name + '.matrixIn[2]')[0]:
			mc.connectAttr( world + '.worldInverseMatrix[0]', multMatrix.name + '.matrixIn[3]' )
		else:
			mc.connectAttr( world + '.worldInverseMatrix[0]', multMatrix.name + '.matrixIn[2]' )


	# multMatrix.attr('matrixSum') >> decomposeMatrix.attr('inputMatrix')
	# mc.connectAttr( multMatrix + '.matrixSum', decomposeMatrix + '.inputMatrix' )

	#... Connect TS
	if translate == True:
		decomposeMatrix.attr('outputTranslate') >> obj_target.attr('translate')
		# mc.connectAttr( decomposeMatrix + '.outputTranslate', tgt + '.translate')
	if scale == True:
		decomposeMatrix.attr('outputScale') >> obj_target.attr('scale')
		# mc.connectAttr( decomposeMatrix + '.outputScale', tgt + '.scale')

	#... Clear Node (Cause error I dunno why)
	target_quatInvert.attr('outputQuat') // target_quatProd.attr('input2Quat')
	target_eulerToQuat.deleteName()
	#target_quatInvert.deleteName()



	decomposeMatrix.attr('message') >> obj_target.attr('m_deComp')
	target_quatToEuler.attr('message') >> obj_target.attr('m_quatToEuler')


	#... Connect message for incase want to delete
	# obj_target.addAttribute( attributeType = 'message' , longName = 'm_deComp')
	# obj_target.addAttribute( attributeType = 'message' , longName = 'm_quatToEuler')
	# mc.listConnections( obj_target.name + '.' + 'm_deComp')[0]
	# mc.listConnections( obj_target.name + '.' + 'm_quatToEuler')[0]




	#... still not work disable for now
	#... link variable to Network node
	# parentConMatrix_meta = core.MetaGeneric('matCon')
	 
	# mc.select(target, r=True)
	
	# meta_node = core.MetaGeneric(obj_source.name)

	# #... connect message
	# obj_target.attr('message') >> meta_node.attr('Rig_Prior')
	# meta_node.attr('Base_Name').value = obj_target.name
	# meta_node.attr('Side').value = 'None'
	
	# meta_node.addAttribute( dataType = 'string' , longName = 'node')
	# meta_node.attr('node').value = f'{decomposeMatrix},{target_quatToEuler},{multMatrix}'

	# meta_node.addAttribute( dataType = 'string' , longName = 'Target')
	# meta_node.addAttribute( dataType = 'string' , longName = 'Source')
	# meta_node.attr('Target').value = obj_target.name
	# meta_node.attr('Source').value = obj_source.name

	mc.select(target, r=True)

	Constraint.info(' # # # # # # # # # Parent matrix Complete # # # # # # # # # # # #  \n')
	return obj_target, obj_source


#... for delete
'''
mc.delete(mc.listConnections( obj_target.name + '.' + 'm_deComp')[0])
'''


#... delete martix node by selection the target
def deleteMartixNode():
	selection = mc.ls(sl=True)[0]
	decomposeMatrix = mc.listConnections( selection,type = 'decomposeMatrix')[0]
	quatToEuler = mc.listConnections( selection,type = 'quatToEuler')[0]

	if decomposeMatrix:
		mc.delete(decomposeMatrix)
	if quatToEuler:
		mc.delete(quatToEuler)


#... delete martix node by selection list
def del_sel_matrix(selected = []):
	#... Get short name
	mulMtx = mnd.get_short_name('multMatrix')
	quat = mnd.get_short_name('quatToEuler')
	deComp = mnd.get_short_name('decomposeMatrix')

	for each in selected:
		list_sel = mc.listConnections(each, destination=True)

		for each in list_sel:
			try:
				# .. because after delete it will can't find the rest
				# if each.endswith('_dmpMtx'):
					# logger.MayaLogger.info('Delete %s' %each)
					# mc.delete(each)
				if each.endswith(mulMtx):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)
				if each.endswith(quat):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)
				if each.endswith(deComp):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)

			except:
				print('There are no matrix node to delete.')
	print('Delete Done...')



def aimConMatrix(	baseName = 'aimMax',
					aim = 'aim',
					up = 'up',
					target = 'axis'	):

	obj_aim = core.Dag(aim)
	obj_up = core.Dag(up)
	obj_target = core.Dag(target)

	# connectAttr -f aim.matrix aimMatrix1.primaryTargetMatrix;

	aim_mat = core.AimMatrix(baseName)

	aim_mat.attr('secondaryMode').value = 1

	obj_aim.attr('matrix') >> aim_mat.attr('primaryTargetMatrix')
	obj_up.attr('matrix') >> aim_mat.attr('secondaryTargetMatrix')

	mult_mat = core.MultMatrix(baseName+'Mult')
	mult_mat.attr('matrixSum') >> aim_mat.attr('inputMatrix')

	decompose_mat = core.DecomposeMatrix(baseName)
	aim_mat.attr('outputMatrix') >> decompose_mat.attr('inputMatrix')

	decompose_mat.attr('outputRotate') >> obj_target.attr('rotate')

	composeOffset_mat = core.ComposeMatrix(baseName+'Offset')
	obj_target.attr('translate') >> composeOffset_mat.attr('inputTranslate')

	composeOffset_mat.attr('outputMatrix') >> mult_mat.attr('matrixIn[0]')
	obj_target.attr('parentMatrix') >> mult_mat.attr('matrixIn[1]')

	Constraint.info(' # # # # # # # # # Aim matrix Complete# # # # # # # # # # # #  \n')

	return obj_target