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






def parentConMatrixSpaceSwitchGPT(source,
							   target,
							   mo=True,
							   create_attr=True,
							   attr_name='spaceSwitch',
							   default_space='LOCAL'):
	"""
	Matrix-based Parent/World (no-rotation) space switch.

	What you get
	------------
	- LOCAL space (parent space): behaves like a normal parentConstraint
	  -> follows parent's translation AND rotation
	- WORLD space (head-up / no-rotation): follows world translation of source
	  -> keeps rotation identity (0,0,0) in world, so the head stays upright

	How it works (nodes)
	--------------------
	LOCAL branch:
		local_mmx = multMatrix( [offset?] * source.worldMatrix * target.parentInverseMatrix )
		local_dcmp = decomposeMatrix(local_mmx.matrixSum)

	WORLD branch (no-rotation):
		tmp_mmx   = multMatrix( [offset?] * source.worldMatrix )               # world matrix with offset
		tmp_dcmp  = decomposeMatrix(tmp_mmx.matrixSum)                         # extract world translate (T_w)
		world_cmp = composeMatrix( translate = tmp_dcmp.outputTranslate,       # rotation=0, scale=1
								   rotate=(0,0,0), scale=(1,1,1) )
		world_mmx = multMatrix( world_cmp.outputMatrix * target.parentInverseMatrix )
		(no dcmp here; it blends at matrix-level)

	Switch/blend:
		wt = wtAddMatrix()  # or blendMatrix if you prefer/available
		- wt.wtMatrix[0].matrixIn = local_mmx.matrixSum
		- wt.wtMatrix[1].matrixIn = world_mmx.matrixSum
		- drive weights with a single float attribute on target: 0=LOCAL, 1=WORLD
		  (use a 'reverse' node to get (1 - space) for the LOCAL weight)

	Output:
		final_dcmp = decomposeMatrix(wt.matrixSum)
		- final_dcmp.outputTranslate -> target.translate
		- final_dcmp.outputScale     -> target.scale
		- rotation:
			* if target is a joint: compensate jointOrient
				q = final_dcmp.outputQuat * inverse( jointOrient )
				euler(q) -> target.rotate
			* else (transform): final_dcmp.outputRotate -> target.rotate

	Parameters
	----------
	source : str
		Driver transform.
	target : str
		Driven transform or joint.
	mo : bool
		Maintain offset at creation time.
	create_attr : bool
		Create user control attribute on target to switch spaces.
	attr_name : str
		Name of the switch attribute (0..1). 0=LOCAL, 1=WORLD.
	default_space : str
		'LOCAL' or 'WORLD' (initial attribute value).

	Returns
	-------
	dict of node names for debugging.
	"""

	if not source:
		print('Source is not selected.')
		return {}

	# -- Core wrappers
	obj_tgt = core.Dag(target)
	obj_src = core.Dag(source)
	base    = core.check_name_style(name=target)[0]

	# -- Compute local offset (target in source local space)
	#    NOTE: we reuse your GPT version (row-major extraction)
	local_offset = _getLocalOffsetGPT(source, target)
	offMat = [local_offset(i, j) for i in range(4) for j in range(4)]

	# ------------------------------------------------------------------
	# LOCAL branch
	# ------------------------------------------------------------------
	local_mmx  = core.MultMatrix(base + '_Local')
	local_dcmp = core.DecomposeMatrix(base + '_Local')

	if mo:
		mc.setAttr(local_mmx.name + '.matrixIn[0]', offMat, type='matrix')
		obj_src.attr('worldMatrix[0]')                >> local_mmx.attr('matrixIn[1]')
		obj_tgt.attr('parentInverseMatrix[0]')       >> local_mmx.attr('matrixIn[2]')
	else:
		obj_src.attr('worldMatrix[0]')                >> local_mmx.attr('matrixIn[0]')
		obj_tgt.attr('parentInverseMatrix[0]')       >> local_mmx.attr('matrixIn[1]')

	local_mmx.attr('matrixSum')                       >> local_dcmp.attr('inputMatrix')

	# ------------------------------------------------------------------
	# WORLD (no-rotation) branch
	#   1) Build a world-space matrix with the SAME world translation as LOCAL,
	#      but zero rotation, unit scale.
	#   2) Convert it into target's parent space via parentInverseMatrix.
	# ------------------------------------------------------------------
	tmp_mmx   = core.MultMatrix(base + '_WorldTmp')     # [offset?]*source.world
	tmp_dcmp  = core.DecomposeMatrix(base + '_WorldTmp')

	if mo:
		mc.setAttr(tmp_mmx.name + '.matrixIn[0]', offMat, type='matrix')
		obj_src.attr('worldMatrix[0]')                 >> tmp_mmx.attr('matrixIn[1]')
	else:
		obj_src.attr('worldMatrix[0]')                 >> tmp_mmx.attr('matrixIn[0]')

	tmp_mmx.attr('matrixSum')                          >> tmp_dcmp.attr('inputMatrix')

	world_cmp = core.ComposeMatrix(base + '_WorldCMP')  # build identity-rot/sca in WORLD, with T_w
	tmp_dcmp.attr('outputTranslate')                    >> world_cmp.attr('inputTranslate')
	# rotation stays (0,0,0); scale stays (1,1,1)

	world_mmx = core.MultMatrix(base + '_World')
	world_cmp.attr('outputMatrix')                      >> world_mmx.attr('matrixIn[0]')
	obj_tgt.attr('parentInverseMatrix[0]')              >> world_mmx.attr('matrixIn[1]')

	# ------------------------------------------------------------------
	# Switch / Blend
	#   wtAddMatrix with two inputs:
	#     - index 0: LOCAL matrix (weight = 1 - space)
	#     - index 1: WORLD matrix (weight = space)
	#   Use a 'reverse' node to generate (1 - space)
	# ------------------------------------------------------------------
	wt = core.WtAddMatrix(base + '_SpaceBlend')

	# pipe matrices
	local_mmx.attr('matrixSum')                         >> wt.attr('wtMatrix[0].matrixIn')
	world_mmx.attr('matrixSum')                         >> wt.attr('wtMatrix[1].matrixIn')

	# target attribute 0..1
	if create_attr and not mc.objExists(obj_tgt.name + '.' + attr_name):
		mc.addAttr(obj_tgt.name, ln=attr_name, at='double', min=0, max=1, dv=0.0, k=True)

	# default value
	if default_space.upper() == 'WORLD':
		mc.setAttr(obj_tgt.name + '.' + attr_name, 1.0)
	else:
		mc.setAttr(obj_tgt.name + '.' + attr_name, 0.0)

	# reverse node -> (1 - space)
	rev = mc.createNode('reverse', n=base + '_SpaceRev')
	mc.connectAttr(obj_tgt.name + '.' + attr_name, rev + '.inputX', f=True)

	# drive weights
	# LOCAL weight = (1 - space)
	mc.connectAttr(rev + '.outputX', wt.name + '.wtMatrix[0].weightIn', f=True)
	# WORLD weight = space
	mc.connectAttr(obj_tgt.name + '.' + attr_name, wt.name + '.wtMatrix[1].weightIn', f=True)

	# ------------------------------------------------------------------
	# Final decompose → connect to target
	# ------------------------------------------------------------------
	final_dcmp = core.DecomposeMatrix(base + '_SpaceResult')
	wt.attr('matrixSum')                                >> final_dcmp.attr('inputMatrix')

	# Translate / Scale (same for joint & transform)
	final_dcmp.attr('outputTranslate')                  >> obj_tgt.attr('translate')
	final_dcmp.attr('outputScale')                      >> obj_tgt.attr('scale')

	# Rotation (joint needs jointOrient compensation)
	if obj_tgt.type == 'joint':
		q_e2q  = core.EulerToQuat(base + '_JO')
		q_inv  = core.QuatInvert(base + '_JO')
		q_prod = core.QuatProd(base + '_JO')
		q_q2e  = core.QuatToEuler(base + '_JO')

		# convert jointOrient (Euler) to quat and invert
		mc.connectAttr(obj_tgt.name + '.jointOrient', q_e2q.name + '.inputRotate', f=True)
		q_e2q.attr('outputQuat')                        >> q_inv.attr('inputQuat')

		# decompose quat * inv(jointOrient)
		final_dcmp.attr('outputQuat')                   >> q_prod.attr('input1Quat')
		q_inv.attr('outputQuat')                        >> q_prod.attr('input2Quat')

		# back to Euler
		q_prod.attr('outputQuat')                       >> q_q2e.attr('inputQuat')
		q_q2e.attr('outputRotate')                      >> obj_tgt.attr('rotate')

		# keep rotate order consistent (match source)
		src_ro = mc.getAttr(str(source) + '.rotateOrder')
		obj_tgt.attr('rotateOrder').value = src_ro
		if not mc.listConnections(obj_tgt.attr('rotateOrder'), d=False, s=True):
			obj_tgt.attr('rotateOrder') >> q_q2e.attr('inputRotateOrder')
	else:
		# simple transforms: use euler directly
		final_dcmp.attr('outputRotate')                 >> obj_tgt.attr('rotate')
		src_ro = mc.getAttr(str(source) + '.rotateOrder')
		obj_tgt.attr('rotateOrder').value = src_ro

	# --- Optional: message links for clean-up tools
	if not mc.objExists(obj_tgt.name + '.m_spaceSwitch'):
		obj_tgt.addAttribute(attributeType='message', longName='m_spaceSwitch')
		final_dcmp.attr('message') >> obj_tgt.attr('m_spaceSwitch')

	Constraint.info('Space switch (LOCAL/WORLD) setup complete.')
	return {
		'local_mmx': local_mmx.name,
		'local_dcmp': local_dcmp.name,
		'tmp_mmx': tmp_mmx.name,
		'tmp_dcmp': tmp_dcmp.name,
		'world_cmp': world_cmp.name,
		'world_mmx': world_mmx.name,
		'wt_add': wt.name,
		'final_dcmp': final_dcmp.name,
	}



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
    """
    Matrix-based parent constraint (joint/transform safe).

    Key points
    ----------
    - multMatrix order: [offset] * source.worldMatrix * target.parentInverseMatrix
    - Joint targets: remove jointOrient via quaternion math:
        finalQuat = dcmp.outputQuat * inverse( jointOrient )
        euler(finalQuat) -> target.rotate
    - Transform targets: use dcmp.outputRotate directly (no quat chain).
    """
    if not source:
        print('Source is not selected.')
        return False

    # Wrappers
    obj_tgt = core.Dag(target)
    obj_src = core.Dag(source)
    base    = core.check_name_style(name=target)[0]

    # Match rotate order from source to target first
    src_ro = mc.getAttr(obj_src.name + ".rotateOrder")
    mc.setAttr(obj_tgt.name + ".rotateOrder", src_ro)

    # Compute local offset (target in source local space)
    local_offset = _getLocalOffsetGPT(source, target)
    offMat = [local_offset(i, j) for i in range(4) for j in range(4)]

    # Nodes
    dcmp = core.DecomposeMatrix(base)   # decomposeMatrix
    mmx  = core.MultMatrix(base)        # multMatrix

    Constraint.info('This is between [ {0} ] and [ {1} ]'.format(obj_tgt.type, obj_src.type))

    # multMatrix wiring: [0]=offset, [1]=source.world, [2]=target.parentInverse
    if mo:
        mc.setAttr(mmx.name + '.matrixIn[0]', offMat, type='matrix')
        obj_src.attr('worldMatrix[0]')         >> mmx.attr('matrixIn[1]')
        obj_tgt.attr('parentInverseMatrix[0]') >> mmx.attr('matrixIn[2]')
    else:
        obj_src.attr('worldMatrix[0]')         >> mmx.attr('matrixIn[0]')
        obj_tgt.attr('parentInverseMatrix[0]') >> mmx.attr('matrixIn[1]')

    # Send matrix to decompose
    mmx.attr('matrixSum') >> dcmp.attr('inputMatrix')

    # Translate / Scale
    if translate:
        dcmp.attr('outputTranslate') >> obj_tgt.attr('translate')
    if scale:
        dcmp.attr('outputScale')     >> obj_tgt.attr('scale')

    # Rotate handling
    if rotate:
        if obj_tgt.type == 'joint':
            # Joint: remove jointOrient with quaternion chain
            q_e2q   = core.EulerToQuat(base + '_JO')   # Euler (jointOrient) -> Quat
            q_inv   = core.QuatInvert(base + '_JO')    # inverse(jointOrient quat)
            q_prod  = core.QuatProd(base + '_JO')      # dcmp.quat * inv(jo)
            q_q2e   = core.QuatToEuler(base + '_JO')   # back to Euler

            # jointOrient -> quat -> invert
            mc.connectAttr(obj_tgt.name + '.jointOrient', q_e2q.name + '.inputRotate', f=True)
            q_e2q.attr('outputQuat')  >> q_inv.attr('inputQuat')

            # combine with decomposed rotation
            dcmp.attr('outputQuat')   >> q_prod.attr('input1Quat')
            q_inv.attr('outputQuat')  >> q_prod.attr('input2Quat')

            # back to Euler -> target.rotate
            q_prod.attr('outputQuat') >> q_q2e.attr('inputQuat')
            q_q2e.attr('outputRotate') >> obj_tgt.attr('rotate')

            # keep rotate order consistent
            if not mc.listConnections(obj_tgt.attr('rotateOrder'), d=False, s=True):
                obj_tgt.attr('rotateOrder') >> q_q2e.attr('inputRotateOrder')

        else:
            # Transform: use decompose rotate directly (no quat chain)
            dcmp.attr('outputRotate') >> obj_tgt.attr('rotate')

    # Optional bookkeeping
    if not mc.objExists(obj_tgt.name + '.m_deComp'):
        obj_tgt.addAttribute(attributeType='message', longName='m_deComp')
        dcmp.attr('message') >> obj_tgt.attr('m_deComp')

    mc.select(target, r=True)
    Constraint.info(' # # # Parent matrix (GPT) Complete # # #\n')
    return obj_tgt, obj_src






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