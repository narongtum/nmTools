# Dode Rig Tool name as dc

# import dTool as dc
#reload dc

try:
	reload  # Python 2.7
	print('This might be python 2.7')
except NameError:
	try:
		from importlib import reload  # Python 3.4+
		print('Python 3.4+')
	except ImportError:
		from imp import reload  # Python 3.0 - 3.3
		print('Python 3.0 - 3.3')

import maya.cmds as mc
import pymel.core as pm

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)

# Primary Fuction

def parCon( src, tgt, mo=1, w=1 ):
	name = tgt + '_parCons'
	mc.parentConstraint( src, tgt, mo = mo, n = name, w=w)
	return name

def oriCon( src, tgt, mo=1, w=1 ):
	name = tgt + '_oriCons'
	mc.orientConstraint( src, tgt, mo = mo, n = name, w=w )
	return name

def pointCon( src, tgt, mo=1, w=1 ):
	name = tgt + '_pntCons'
	mc.pointConstraint( src, tgt, mo = mo, n = name, w=w )
	return name

def sclCon( src, tgt, mo=1, w=1 ):
	name = tgt + '_sclCons'
	mc.scaleConstraint( src, tgt, mo = mo, n = name, w=w )
	return name

def allMat( tgt, src ):
	mc.matchTransform( tgt, src, pos = True, rot = True)

def posMat( tgt, src ):
	mc.matchTransform( tgt, src, pos = True, rot = False)

def rotMat( tgt, src ):
	mc.matchTransform( tgt, src, pos = False, rot = True)	

def cons( mo = '', type = ''):
	sel = mc.ls(sl=1)
	tgt = sel[-1]
	src = sel
	src.remove(sel[-1])
	if type == 'parent':
		parCon( src, tgt, mo=mo )
	if type == 'orient':
		oriCon( src, tgt, mo=mo )
	if type == 'point':
		pointCon( src, tgt, mo=mo )
	if type == 'scale':
		sclCon( src, tgt, mo=mo )

# Secondary Function

def chainCtrl(): # by selected Jnt
	sel = mc.ls(sl=True)
	if mc.objExists ('ctrl'):

		for i in range(len(sel)):
			jnt = sel[i]
			bJnt = sel[i].split('_')[-1]
			name = sel[i].split('_'+ bJnt )[0]
			grp = name + 'Zro' + '_grp'
			off = name + 'Offset' + '_grp'
			ctrl = name + '_ctrl'
			ctrlShape = ctrl + 'Shape'
			gmblCtrl = name + 'Gmbl' + '_ctrl'
			
			# create
			mc.duplicate( 'ctrl', name = ctrl )
			mc.group( name = off, em=True)
			mc.group( name = grp, em=True )
			
			# gimbal
			shapes = wcd.getShape( ctrlShape )
			data = wcd.modifiyCtrlShape( shapes , axis = [0.75, 0.75, 0.75] )
			gmblCtrl = mc.curve( name = gmblCtrl, p = data[0]["points"], k = data[0]["knots"], d = data[0]["degree"], per = bool(data[0]["form"]) )
			ctrlColor( gmblCtrl, 'white' )

			# hide Vis for gimbal
			ctrlShp = mc.listRelatives( ctrl, shapes = True)
			gmblShp = mc.listRelatives( gmblCtrl, shapes = True)
			mc.addAttr ( ctrlShp[0], sn = 'gmb' ,ln = 'Gimbal', min = 0, max = 1, dv = 0, k = True)
			mc.connectAttr ( ctrlShp[0] + '.Gimbal',gmblShp[0] + '.visibility' )

			# lock and hide attr
			mc.setAttr( ctrl + '.v' , keyable = 0, lock = 1)
			mc.setAttr( gmblCtrl + '.v', keyable = 0, lock = 1)

			# adjust
			mc.parent( gmblCtrl, ctrl)
			mc.parent( ctrl, off )
			mc.parent( off, grp )
			allMat( grp, jnt )

			if i > 0:
				upBJnt = sel[i-1].split('_')[-1]
				upName = sel[i-1].split('_'+ upBJnt)[0]
				upGmblCtrl = upName + 'Gmbl' + '_ctrl'
				mc.parent( grp, upGmblCtrl )
				# connect
				mc.connectAttr( con + '.outColor', off + '.rotate' )

			elif i == 0:
				con = name + '_con'
				# add & create
				mc.addAttr( ctrl, sn = 'follow' ,ln = 'follow', min = 0, max = 1, dv = 0, k = True)
				mc.createNode( 'condition', name = name + '_con')
				# set
				mc.setAttr( con + '.secondTerm', 1)
				mc.setAttr( con + '.colorIfFalseR', 0 )
				mc.setAttr( con + '.colorIfFalseG', 0 )
				mc.setAttr( con + '.colorIfFalseB', 0 )
				# connect
				mc.connectAttr( ctrl + '.follow', con + '.firstTerm' )
				mc.connectAttr( ctrl + '.rotate', con + '.colorIfTrue' )

			parCon( ctrl, jnt, mo=1 )
	else:
		print (">>>>>   create ctrl in scene first  <<<<<")

def quickCtrl():
	# Control MAPPING QUICK
	sel = mc.ls(sl=True)
	for i in range(len(sel)):
		jnt = sel[i]
		bJnt = sel[i].split('_')[-1]
		name = sel[i].split('_'+ bJnt )[0]
		grp = name + 'Zro' + '_grp'
		off = name + 'Offset' + '_grp'
		ctrl = name + '_ctrl'
		#ctrlShape = ctrl + 'Shape'
		#gmblCtrl = name + 'Gmbl' + '_ctrl'
		mc.group(em=1, n = grp)
		mc.duplicate('ctrl', n = ctrl)
		mc.parent(ctrl,grp)
		allMat( grp, jnt )
		parCon( ctrl, jnt, mo = 1)


def createCtrl( jnt , typ = 'circle', c = 'yellow', gmbl = True):
	name = jnt.split('_')[0]
	grp = name + 'Zro_grp'
	ctrl = name + '_ctrl'
	
	# Create Ctrl and Set Typ and Color
	ctrlType( ctrl, typ)
	ctrlColor( ctrl, c )

	# Create Group
	mc.group(n = grp, em = True)
	mc.parent(ctrl,grp)

	# Create Gimbal ctrl smaller than normal 0.75
	if gmbl == True:
		gmblCtrl = name + 'Gmbl_ctrl'
		ctrlType( gmblCtrl, typ, scale = charScale * 0.75)
		ctrlColor( gmblCtrl, 'white')
		mc.parent( gmblCtrl, ctrl )

		ctrlShp = mc.listRelatives( ctrl, shapes = True)
		gmblShp = mc.listRelatives( gmblCtrl, shapes = True)

		mc.addAttr ( ctrlShp[0], sn = 'gmb' ,ln = 'Gimbal', min = 0, max = 1, dv = 0, k = True)
		mc.connectAttr ( ctrlShp[0] + '.Gimbal',gmblShp[0] + '.visibility' )

		#return gmblCtrl , grp

	#else:
		#return ctrl , grp

	# Mat all
	allMat( grp, jnt)

	# parCon
	if gmbl == True:
		parCon( gmblCtrl, jnt)
	else:
		parCon( ctrl, jnt)

	return grp

'''
def ctrlType( name, typ , scale = charScale):
	if typ == 'circle':
		ctrl = mc.circle( nr = (0, 1, 0), c = (0, 0, 0), sw = 360, r = scale , n = name , ch = False)
	return ctrl
'''

def ctrlColor( name , color ):
	# Color Libary
	if color == 'yellow' :
		ctrlColor = 17
	elif color == 'red':
		ctrlColor = 13
	elif color == 'blue':
		ctrlColor = 6
	elif color == 'white':
		ctrlColor = 16

	ctrlShape = mc.listRelatives( name, shapes = True)
	mc.setAttr (ctrlShape[0] + '.overrideEnabled',True )
	mc.setAttr (ctrlShape[0] + '.overrideColor', ctrlColor)

	return ctrlShape


# count joint in scene and print shown thourgh the window
def count_bJnt():
	selSet = mc.ls('*_bJnt')
	jntCount = len(selSet)
	mc.confirmDialog( title='Joint Count ', message='             BIND JOINTS = {0}                '.format(jntCount), button=['Got It!'], cancelButton='No', dismissString='No' )

# unlock all Attrs [ select ]
def unlock_attrs():
	selObj = mc.ls(selection = 1)
	attrs = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	for i in xrange(len(selObj)):
		for attr in attrs:
			mc.setAttr('{0}.{1}'.format(selObj[i],attr), keyable = 1, lock = 0)





# create null group from name n:
def null_grp(n):
	mc.group(name = n, em = 1)
	return n

# lock and hide group that name n:
def lock_grp(n):
	grp = null_grp(n=n)
	attrs = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	for attr in attrs:
		mc.setAttr('{0}.{1}'.format(grp,attr), keyable = 0, lock = 1)
	return n

# lock add hide all Attr for ctrl
def blankCtrl( ctrl ):
	attrs = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
	for attr in attrs:
		mc.setAttr('{0}.{1}'.format(ctrl,attr), keyable = 0, lock = 1)
	return ctrl

# lock obj
def lock( obj ):
	attrs = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	for attr in attrs:
		mc.setAttr('{0}.{1}'.format(obj,attr), keyable = 0, lock = 1)
	return obj

# hide
def lockHideVis( obj ):
	lock = mc.getAttr( obj + '.v',l=1)
	if lock == True:
		print( obj + ' is locked')
	elif lock == False:
		print( obj + ' is now lock')
		mc.setAttr( obj + '.v', 0, k = 0, l = 1 )

# hide
def hide( obj ):
	lock = mc.getAttr( obj + '.v',l=1)
	if lock == True:
		print( obj + ' is locked')
	elif lock == False:
		print( obj + ' is now lock')
		mc.setAttr( obj + '.v', 0 )

# lock and hide obj
def lockVis( obj ):
	lock = mc.getAttr( obj + '.v',l=1)
	if lock == True:
		print( obj + ' is locked')
	elif lock == False:
		print( obj + ' is now lock')
		mc.setAttr( obj + '.v', k = 0, l = 1 )

# create Zro_grp in the and parent the selectOne in the grp # [ input ]
def zro_grp(n,src):
	grp = n + 'Zro_grp'
	null_grp(n=grp)
	snap_all(tgt = grp, src = src)
	mc.parent(src,grp)
	return grp

# create Zro_grp in the and parent the selectOne in the grp # [ select ]
def create_zrogrp():
	selObj = mc.ls(selection = 1)
	for i in xrange(len(selObj)):
		src = selObj[i]
		if 'ctrl' in src:
			name = selObj[i].split('_')[0]
		else:
			name =selObj[i]
		grp = name + 'Zro_grp'
		null_grp(n=grp)
		snap_all(tgt = grp, src = src)
		mc.parent(src,grp)


def renameShd( overideName = '' ):
	# Auto rename from mat
	# you have to select mat fist
	sel = mc.ls(sl=True)
	for each in sel:
		if overideName == '':
			name = each.split('_')[-1]
		else:
			name = overideName
		#print( name)
		shd = name + '_shd'
		mat = name + '_mat'
		file = name + '_file'
		bmp = name + '_bmp'
		bmpFile = name + '_bmp_file'
		# List connect of select
		connects = mc.listConnections( each , p = True )
		for plug in connects:
			node = plug.split('.')[0]
			nt = mc.nodeType( node )

			if nt == 'shadingEngine':
				print( node)
				mc.rename( node, shd )
			elif nt == 'bump2d':
				bmpConnected = mc.listConnections( node, p = True )
				for con in bmpConnected:
					if 'outAlpha' in con:
						print( con)
						bmpFileNode = con.split('.')[0]
						mc.rename( bmpFileNode, bmpFile )
				mc.rename( node, bmp )
			elif nt == 'file':
				print( node)
				mc.rename( node, file )
		mc.rename( each, mat )


def displayColorOverride( ctrl = [], color = '' ):
	if len(ctrl) == 0:
		sel = mc.ls( sl = 1 )
		print( '>>   We will do from select   <<')
	elif len(ctrl) > 0:
		sel = ctrl
		print( '>>   We will do from %s   <<' %( ctrl ))

	for obj in sel:
		shapes = mc.listRelatives( obj, shapes = True )
		shp = shapes[0]
		mc.setAttr( shp + '.overrideEnabled', 1 )
	
		if color == 'yellow' :
			mc.setAttr( shp + '.overrideColor', 17)
		elif color == 'red' :
			mc.setAttr( shp + '.overrideColor', 13)
		elif color == 'green' :
			mc.setAttr( shp + '.overrideColor', 14)
		elif color == 'blue' :
			mc.setAttr( shp + '.overrideColor', 6)
		elif color == 'white' :
			mc.setAttr( shp + '.overrideColor', 16)

		print( obj , 'change to %s and it AWESOME' %( color ))


'''
charScale = 1
#createCtrl( 'jnt01_bJnt', typ = 'circle', c = 'yellow' , gmbl = True)

sel = mc.ls(sl=1)
for each in sel:
	jnt = each
	createCtrl( jnt, typ = 'circle', c = 'yellow' , gmbl = True)




import maya.OpenMaya as om


def getDagPath(node=None):
	sel = om.MSelectionList()
	sel.add(node)
	d = om.MDagPath()
	sel.getDagPath(0, d)
	return d

def getLocalOffset(parent, child):
	parentWorldMatrix = getDagPath(parent).inclusiveMatrix()
	childWorldMatrix = getDagPath(child).inclusiveMatrix()

	return childWorldMatrix * parentWorldMatrix.inverse()

def rotateOffset(tgt, dmpMtx):
	# Create name 
	eulQua = tgt + '_eulQua'
	quaInv = tgt + '_quaInv'
	quaPro = tgt + '_quaPro'
	quaEul = tgt + '_quaEul'

	# Create More Node
	mc.createNode( 'eulerToQuat', n = eulQua )
	mc.createNode( 'quatInvert', n = quaInv )
	mc.createNode( 'quatProd', n = quaPro )
	mc.createNode( 'quatToEuler', n = quaEul )

	# Rotate Part
	mc.connectAttr( tgt + '.jointOrient', eulQua + '.inputRotate' )
	mc.connectAttr( eulQua + '.outputQuat', quaInv + '.inputQuat' )
	mc.connectAttr( dmpMtx + '.outputQuat', quaPro + '.input1Quat' )

	# get Inverse Quat from Child Rotate Order
	mc.connectAttr( quaInv + '.outputQuat', quaPro + '.input2Quat' )
	mc.connectAttr( quaPro + '.outputQuat', quaEul + '.inputQuat' )

	allChanel = ['X','Y','Z','W']
	for chanel in allChanel:
		quaVar = mc.getAttr( quaInv + '.outputQuat.outputQuat' + chanel )
		mc.setAttr( quaPro + '.input2Quat.input2Quat' + chanel )

	# Clear Node
	mc.delete( eulQua )
	#mc.delete( quaInv ) 

	# Final Connect
	mc.connectAttr( quaEul + '.outputRotate', tgt + '.rotate')


def parentMatrix( src, tgt, mo = True, t = True, r = True, s = True):
	# Create Name
	mulMtx = tgt + '_mulMtx'
	dmpMtx = tgt + '_dmpMtx'
	# FUNC
	localOffset =  getLocalOffset( src, tgt )
	offMat = [localOffset(i,j) for i in range(4) for j in range(4)]
	# Create
	mc.createNode( 'multMatrix', n = mulMtx )
	mc.createNode( 'decomposeMatrix', n = dmpMtx )
	#  Set and Connect
	if mo == True:
		mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')
	mc.connectAttr( src + '.worldMatrix[0]', mulMtx + '.matrixIn[1]' )
	
	#  Find out Origin Parent
	if mc.pickWalk( tgt , d = 'up')[0] == tgt:
		print "I'm World Already"
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[2]' )

	# Fist Connect
	mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')
	
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	if r == True:
		rotateOffset(tgt, dmpMtx)
	# Final Connect
	if t == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if s == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale') 


def parentMulMatrix( src, tgt, mo = True, w = 1, t = True, r = True, s = True):
	
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
		parentName = parent.split('_')[0]
		offsetMtx = tgt + '_' + parentName + 'Offset_mulMtx'

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
	mc.connectaAttr( wtMtx + '.matrixSum',  mulMtx + '.matrixIn[0]' )

	# Find out Origin Parent
	if mc.pickWalk( tgt , d = 'up')[0] == tgt:
		print "I'm World Already"
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[1]' )

	# Final Connect
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	# 
	if r == True:
		rotateOffset(tgt, dmpMtx)
	if t == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if s == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale') 




def parentThis( mo = True, w = 1, t = True, r = True, s = True):
	sel = mc.ls(sl=1)
	if len(sel) > 2:
		child = sel[-1]        
		del sel[-1]
		parentMulMatrix( src = sel , tgt = child,  mo = mo, w = w, t = t, r = r, s = s)
		print sel
	elif len(sel) == 2:
		print sel
		parentMatrix( sel[0] , sel[-1],  mo = mo, t = t, r = r, s = s)






parentThis( mo = True, t = True, r = True, s = True)






import maya.cmds as mc
sel = mc.ls('*_ctrl')
for i in range(len(sel)):
	name = sel[i]
	attr = 'tx','ty','tz','rx','ry','rz','sx','sy','sz'
	for a in range(len(attr)):
		attrName = name + '.' + attr[a]
		lock = mc.getAttr(attrName,l=1)
		if lock == False:
			if attr[a] == 'sx':
				mc.setAttr(attrName,1)
			elif attr[a] == 'sy':
				mc.setAttr(attrName,1)
			elif attr[a] == 'sz':
				mc.setAttr(attrName,1)
			else:
				mc.setAttr(attrName,0)
mc.select(cl=True)
print "RESET CTRL VALUE"

def rotateOffset(tgt, dmpMtx):
	# Create name 
	eulQua = tgt + '_eulQua'
	quaInv = tgt + '_quaInv'
	quaPro = tgt + '_quaPro'
	quaEul = tgt + '_quaEul'

	# Create More Node
	mc.createNode( 'eulerToQuat', n = eulQua )
	mc.createNode( 'quatInvert', n = quaInv )
	mc.createNode( 'quatProd', n = quaPro )
	mc.createNode( 'quatToEuler', n = quaEul )

	# Rotate Part
	mc.connectAttr( tgt + '.jointOrient', eulQua + '.inputRotate' )
	mc.connectAttr( eulQua + '.outputQuat', quaInv + '.inputQuat' )
	mc.connectAttr( dmpMtx + '.outputQuat', quaPro + '.input1Quat' )

	# get Inverse Quat from Child Rotate Order
	mc.connectAttr( quaInv + '.outputQuat', quaPro + '.input2Quat' )
	mc.connectAttr( quaPro + '.outputQuat', quaEul + '.inputQuat' )

	# get Rotate Order for quaEul
	rotOrder = mc.getAttr( tgt + '.rotateOrder' )
	mc.setAttr( quaEul + '.inputRotateOrder', rotOrder)
	
	allChanel = ['X','Y','Z','W']
	for chanel in allChanel:
		quaVar = mc.getAttr( quaInv + '.outputQuat.outputQuat' + chanel )
		mc.setAttr( quaPro + '.input2Quat.input2Quat' + chanel )

	# Clear Node
	mc.delete( eulQua )

	# Final Connect
	mc.connectAttr( quaEul + '.outputRotate', tgt + '.rotate')


def parentMatrix( src, tgt, mo = True, t = True, r = True, s = True):
	# Create Name
	mulMtx = tgt + '_mulMtx'
	dmpMtx = tgt + '_dmpMtx'
	# FUNC
	localOffset =  getLocalOffset( src, tgt )
	offMat = [localOffset(i,j) for i in range(4) for j in range(4)]
	# Create
	mc.createNode( 'multMatrix', n = mulMtx )
	mc.createNode( 'decomposeMatrix', n = dmpMtx )
	#  Set and Connect
	if mo == True:
		mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')
	mc.connectAttr( src + '.worldMatrix[0]', mulMtx + '.matrixIn[1]' )
	
	#  Find out Origin Parent
	if mc.pickWalk( tgt , d = 'up')[0] == tgt:
		print "I'm World Already"
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[2]' )

	# Fist Connect
	mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')
	
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	if r == True:
		rotateOffset(tgt, dmpMtx)
	# Final Connect
	if t == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if s == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale') 

	return wtMtx

def parentMulMatrix( src, tgt, mo = True, w = 1, t = True, r = True, s = True):
	
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
		print "I'm World Already"
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[1]' )

	# Final Connect
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	# 
	if r == True:
		rotateOffset(tgt, dmpMtx)
	if t == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if s == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale') 
	
	return wtMtx


# ex: parentThis()
def parentThis( mo = True, w = 1, t = True, r = True, s = True):
	sel = mc.ls(sl=1)
	if len(sel) > 2:
		child = sel[-1]        
		del sel[-1]
		parentMulMatrix( src = sel , tgt = child,  mo = mo, w = w, t = t, r = r, s = s)
		print sel
	elif len(sel) == 2:
		print sel
		parentMatrix( sel[0] , sel[-1],  mo = mo, t = t, r = r, s = s)
		
'''