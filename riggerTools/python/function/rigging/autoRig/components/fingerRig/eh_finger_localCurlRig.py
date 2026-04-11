import maya.cmds as mc
import logging

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


# [4.3]
def connect_LocOffGrp( nameSpace, fingerName, side, numCtrl, axis, type ):
	print ('\n###### connect to Loccal Offset group #######')
	store = _creLocStoVal( nameSpace, fingerName, numCtrl, side, axis, type )
	
	print (f'This is for {axis} axis.')

	if type == 'translate':
		type = 'translate'
	elif type == 'rotate':
		type = 'rotate'

	store.sort()
	fingerNum = list(range(1, numCtrl + 1))

	for each, num in zip(store, fingerNum):
		print ('Connecting ....')
		# "thumb01LFT.translateY"
		targetAttr = f"{nameSpace}{fingerName}{num:02d}{side}Offset_grp.{type}.{type}{axis}"
		print (f'{each}.output1D >>> {targetAttr}')
		mc.connectAttr( f'{each}.output1D', targetAttr, force=True )


# [4.1]
# create store value for each finger lib
def _creLocStoVal( nameSpace, fingerName, numCtrl, side, axis, type ):
	print ('\n###### _creLocStoVal #######')
	offset = []
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	# make it lowercase for readable
	axis = axis.lower()

	for num in range( numCtrl ):
		nameDriv = mc.createNode( 'plusMinusAverage', name = f"{nameSpace}{fingerName}{num + 1:02d}{type}{axis}{side}Offset_pma" )
		offset.append(nameDriv)
	print ('Create offset value.')
	return offset


# [2.5] create multiply divide for each individual finger behavior
def creaeLocalPostStore( nameSpace, side, fingerName, fingerbehavior ):
	print ('\n###### creaeLocalPostStore #######')

	i = 1
	nameNodeGrp = []

	nameNode = mc.createNode( 'multiplyDivide', name = f"{nameSpace}{fingerName}{fingerbehavior}{side}_mdv" )
	nameNodeGrp.append(nameNode)
	print (nameNode)
	print ('\n')

	if fingerbehavior == 'stretch':
		if side == 'RGT':
			i = -1
		print (f'This is {fingerbehavior}.')
		mc.setAttr ( f'{nameNode}.input2X', 0.5 * i )
		mc.setAttr ( f'{nameNode}.input2Y', 0.5 * i )
		mc.setAttr ( f'{nameNode}.input2Z', 0.5 * i )

	elif fingerbehavior == 'roll':
		print (f'This is {fingerbehavior}.')
		mc.setAttr ( f'{nameNode}.input2X', -1.2 * i )
		mc.setAttr ( f'{nameNode}.input2Y', -1.2 * i )
		mc.setAttr ( f'{nameNode}.input2Z', -1.2 * i )


# [7.5] for local finger
def _normalLocalCon( nameSpace, fingerName, side, ctrlName, fingerbehavior=[] ):
	print ('\n###### _normalLocalCon #######')
	for each in ('X','Y','Z'):	
		print (f'{ctrlName}.{fingerbehavior} >>> {nameSpace}{fingerName}{fingerbehavior}{side}_mdv.input1{each}')
		mc.connectAttr(f'{ctrlName}.{fingerbehavior}', f'{nameSpace}{fingerName}{fingerbehavior}{side}_mdv.input1{each}', force=True)


# [9.5]
# connect Pma to local finger
# output x only
def connectLocalPma( nameSpace, fingerName, side, nameOfPost, numVal=None, axis='X', type='translate', numCtrl=3 ):
	print ('\n###### connectLocalPma #######')
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	offsetVal = 'Offset'
	numOfctrl = [str(i) for i in range(numCtrl)]

	axis = axis.lower()
	for np, nc in zip( nameOfPost, numOfctrl ):
		print (f'{np} >>> connect ')
		source = f"{nameSpace}{fingerName}{np}{side}_mdv.outputX"
		dest = f"{nameSpace}{fingerName}{numVal}{type}{axis}{side}{offsetVal}_pma.input1D[{nc}]"
		print (f'{source} >>> {dest}')
		mc.connectAttr(source, dest, force=True)


# [9.55]
# connect Pma to local finger stick
# output x only
def conLocRollPma( nameSpace, fingerName, side, nameOfPost, numOfctrl=['02','03'], axis='X', type='translate', inIndex='5' ):
	print ('\n###### conLocRollPma #######')
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	axis = axis.lower()
	offsetVal = 'Offset'

	for each in numOfctrl:
		source = f"{nameSpace}{fingerName}{nameOfPost}{side}_mdv.outputX"
		dest = f"{nameSpace}{fingerName}{each}{type}{axis}{side}{offsetVal}_pma.input1D[{inIndex}]"
		print (f"{source} >>> {dest}")
		mc.connectAttr(source, dest, force=True)