
'''

from function.rigging.autoRig.module import fingerLocalCurlRig as finLocRig
reload(finLocRig)

'''
# =================================
# - Function for each local finger -
# =================================

import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import rigTools
reload(rigTools)









# [4.3]
def connect_LocOffGrp( fingerName , side, numCtrl   , axis , type ):
	store = _creLocStoVal( fingerName , numCtrl , side , axis , type )		
	print 'This is for ' + axis + ' axis.'

	if type == 'translate':
		type = 'translate'
	elif type == 'rotate':
		type = 'rotate'

	store.sort()

	fingerNum = 01,02,03

	for each , num in zip (store,fingerNum) :
		print 'Connecting ....'
									# "thumb 01	  LFT	.translateY"
		print (	'%s.output1D' %each , '%s'%fingerName + '0%d' %num + '%s' %side + 'Offset_grp' + '.'+ '%s.%s%s' %(type,type,axis ) )
		mc.connectAttr(	'%s.output1D' %each , '%s'%fingerName + '0%d' %num + '%s' %side + 'Offset_grp' + '.'+ '%s.%s%s' %(type,type,axis ) , force = True)




# index  01  LFT  Offset _pma

# [4.1]
# internal function
# create store value for each finger lib
def _creLocStoVal( fingerName , numCtrl , side , axis , type ):
	offset = []
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'


	# for num in range( len( fingerbehavior ) ):
	for num in range( numCtrl ):
		
		nameDriv = mc.createNode( 'plusMinusAverage', name = fingerName  + str( num + 1 ).zfill(2) + type + axis + side + 'Offset' + '_pma' )
		print 'Create Pma Node...' + nameDriv
		offset.append(nameDriv)
	print 'Create offset value.'
	return offset
	

			
# [2.5] create multiply divide for each individual finger behavior
def creaet_LocalPostStore( side , fingerName , fingerbehavior ):
	if side == 'LFT':
		i = 1
	else:
		i = -1
	nameNodeGrp = []

	nameNode = mc.createNode( 'multiplyDivide', name = fingerName + fingerbehavior + side + '_mdv')
	nameNodeGrp.append(nameNode)
	print nameNode
	print '\n'

	if fingerbehavior == 'stretch':
		print 'This is %s.' %fingerbehavior
		mc.setAttr ( nameNode + '.input2X', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Z', 0.5*i  )

	elif fingerbehavior == 'roll':
		print 'This is %s.' %fingerbehavior
		mc.setAttr ( nameNode + '.input2X', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Y', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Z', -1.2*i  )



# [7.5] for local finger
def _normalLocalCon(fingerName , side , ctrlName  , fingerbehavior=[]  ):
	for each in ('X','Y','Z'):	
		print '%s.%s'%(ctrlName,fingerbehavior )+' >>> '+ '%s%s%s_mdv.input1%s' %( fingerName,fingerbehavior,side,each )
		mc.connectAttr('%s.%s'%(ctrlName, fingerbehavior), '%s%s%s_mdv.input1%s' %( fingerName,fingerbehavior,side,each ), force = True)




# [9.5]
# connect Pma to local finger
# output x only
def connectLocalPma( fingerName , side , nameOfPost , numVal = None , axis = 'X' , type = 'translate'):

	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	offsetVal = 'Offset'
	numOfctrl = ('0','1','2')


	for np, nc in zip( nameOfPost , numOfctrl):
			print  np + '>>> connect '
			print ('%s%s%s_mdv.output.outputX' 			%( fingerName,np , side )	,	'%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName , numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
			mc.connectAttr('%s%s%s_mdv.output.outputX'	%( fingerName,np , side )	, 	'%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName , numVal , '%s'%type + axis , side , offsetVal , nc ), 	force = True)
	

# [9.55]
# connect Pma to local finger
# output x only
def conLocRollPma( fingerName , side , nameOfPost , numOfctrl = ['02','03'] , axis = 'X' , type = 'translate' , inIndex = '5'):

	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	offsetVal = 'Offset'

	
	for each in numOfctrl:																				#                        thumb    02          TY            LFT  Offset_pma
		print ( '%s%s%s_mdv.output.outputX' 		%( fingerName,nameOfPost , side )	,'%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName , each , '%s'%type + axis , side , offsetVal , inIndex) 		)
		mc.connectAttr( '%s%s%s_mdv.output.outputX' 		%( fingerName,nameOfPost , side )	,'%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName , each , '%s'%type + axis , side , offsetVal , inIndex) 		, 	force = True)



# [2.5] create multiply divide for each individual finger behavior
def creaeLocalPostStore( side , fingerName , fingerbehavior ):

	i = 1

	nameNodeGrp = []

	nameNode = mc.createNode( 'multiplyDivide', name = fingerName + fingerbehavior + side + '_mdv')
	nameNodeGrp.append(nameNode)
	print nameNode
	print '\n'

	if fingerbehavior == 'stretch':
		if side == 'RGT':
			i = -1
		print 'This is %s.' %fingerbehavior
		mc.setAttr ( nameNode + '.input2X', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Z', 0.5*i  )

	elif fingerbehavior == 'roll':
		print 'This is %s.' %fingerbehavior
		mc.setAttr ( nameNode + '.input2X', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Y', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Z', -1.2*i  )