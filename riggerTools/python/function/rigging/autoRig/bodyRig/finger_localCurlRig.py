
'''

from function.rigging.autoRig.module import fingerLocalCurlRig as finLocRig
reload(finLocRig)

'''
# =================================
# - Store Function for each finger(local) -
# =================================

import maya.cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import rigTools
reload(rigTools)









# [4.3]
def connect_LocOffGrp( nameSpace, fingerName, side, numCtrl, axis, type ):
	print ('\n###### connect to Loccal Offset group #######')
	store = _creLocStoVal( nameSpace , fingerName , numCtrl , side , axis , type )
	# nameSpace = charName + elem		
	print ('This is for ' + axis + ' axis.')

	if type == 'translate':
		type = 'translate'
	elif type == 'rotate':
		type = 'rotate'

	store.sort()

	if numCtrl == 3:
		fingerNum = (1, 2, 3)
	elif numCtrl == 2:
		fingerNum = (1, 2)
	else:
		mc.error('There are something wrong with number')

	

	for each , num in zip (store,fingerNum) :
		print ('Connecting ....')
									# "thumb 01	  LFT	.translateY"
		print (	'%s.output1D' %each ,  '%s%s'%(nameSpace,fingerName) + '0%d' %num + '%s' %side + 'Offset_grp' + '.'+ '%s.%s%s' %(type,type,axis ) )
		mc.connectAttr(	'%s.output1D' %each , '%s%s'%(nameSpace,fingerName) + '0%d' %num + '%s' %side + 'Offset_grp' + '.'+ '%s.%s%s' %(type,type,axis ) , force = True)




# index  01  LFT  Offset _pma

# [4.1]
# internal function
# create store value for each finger lib
def _creLocStoVal( nameSpace , fingerName , numCtrl , side , axis , type ):
	# nameSpace = charName + elem
	print ('\n###### _creLocStoVal #######')
	offset = []
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	# make it lowercase for readable
	axis = axis.lower()

	# for num in range( len( fingerbehavior ) ):
	for num in range( numCtrl ):
		
		nameDriv = mc.createNode( 'plusMinusAverage', name = nameSpace + fingerName  + str( num + 1 ).zfill(2) + type + axis + side + 'Offset' + '_pma' )

		offset.append(nameDriv)
	print ('Create offset value.')
	return offset
	

			
# [2.5] create multiply divide for each individual finger behavior
def creaet_LocalPostStore( nameSpace ,side , fingerName , fingerbehavior ):
	# nameSpace = charName + elem
	print ('\n######creaeting local Post Store #######')


	if side == 'LFT':
		i = 1
	else:
		i = -1
	nameNodeGrp = []

	nameNode = mc.createNode( 'multiplyDivide', name = nameSpace + fingerName + fingerbehavior + side + '_mdv')
	nameNodeGrp.append(nameNode)
	print (nameNode)
	print ('\n')

	if fingerbehavior == 'stretch':
		print ('This is %s.' %fingerbehavior)
		mc.setAttr ( nameNode + '.input2X', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Z', 0.5*i  )

	elif fingerbehavior == 'roll':
		print ('This is %s.' %fingerbehavior)
		mc.setAttr ( nameNode + '.input2X', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Y', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Z', -1.2*i  )



# [7.5] for local finger
def _normalLocalCon( nameSpace , fingerName , side , ctrlName  , fingerbehavior = []  ):
	# nameSpace = charName + elem
	print ('\n###### _normalLocalCon #######')
	for each in ('X','Y','Z'):	
		print ('%s.%s'%(ctrlName,fingerbehavior )+' >>> '+ '%s%s%s%s_mdv.input1%s' %( nameSpace,fingerName,fingerbehavior,side,each ))
		mc.connectAttr('%s.%s'%(ctrlName, fingerbehavior), '%s%s%s%s_mdv.input1%s' %( nameSpace,fingerName,fingerbehavior,side,each ), force = True)




# [9.5]
# connect Pma to local finger
# output x only
def connectLocalPma( nameSpace ,fingerName , side , nameOfPost , numVal = None , axis = 'X' , type = 'translate', numCtrl = 3):
	print ('\n###### connectLocalPma #######')
	# nameSpace = charName + elem
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	offsetVal = 'Offset'

	if numCtrl == 3:
		numOfctrl = ('0','1','2')
	elif numCtrl == 2:
		numOfctrl = ('0','1')

	axis = axis.lower()
	for np, nc in zip( nameOfPost , numOfctrl):
			print  (np + '>>> connect ')
			

			print ('%s%s%s%s_mdv.output.outputX' 			%( nameSpace,fingerName,np , side )	,	'%s%s%s%s%s%s_pma.input1D[%s]' 	%(nameSpace, fingerName , numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
			mc.connectAttr('%s%s%s%s_mdv.output.outputX'	%( nameSpace,fingerName,np , side )	, 	'%s%s%s%s%s%s_pma.input1D[%s]' 	%(nameSpace, fingerName , numVal , '%s'%type + axis , side , offsetVal , nc ), 	force = True)
	

# [9.55]
# connect Pma to local finger stick
# output x only
def conLocRollPma( nameSpace , fingerName , side , nameOfPost , numOfctrl = ['02','03'] , axis = 'X' , type = 'translate' , inIndex = '5'):
	# nameSpace = charName + elem
	print ('\n###### conLocRollPma #######')
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	# Change upperCase to lowerCase
	axis = axis.lower()

	offsetVal = 'Offset'

	
	for each in numOfctrl:
		print ('This might be a problem')

		print ( '%s%s%s%s_mdv.output.outputX' 				%( nameSpace, fingerName, nameOfPost, side )	,'%s%s%s%s%s%s_pma.input1D[%s]' 	%( nameSpace,fingerName , each , '%s'%type + axis , side , offsetVal , inIndex) 		)
		mc.connectAttr( '%s%s%s%s_mdv.output.outputX' 		%( nameSpace, fingerName, nameOfPost, side )	,'%s%s%s%s%s%s_pma.input1D[%s]' 	%( nameSpace,fingerName , each , '%s'%type + axis , side , offsetVal , inIndex) 		, 	force = True)



# [2.5] create multiply divide for each individual finger behavior
def creaeLocalPostStore( nameSpace , side , fingerName , fingerbehavior ):

	# nameSpace = charName + elem

	print ('\n###### creaeLocalPostStore #######')


	i = 1

	nameNodeGrp = []

	nameNode = mc.createNode( 'multiplyDivide', name = nameSpace + fingerName + fingerbehavior + side + '_mdv')
	nameNodeGrp.append(nameNode)
	print (nameNode)
	print ('\n')

	if fingerbehavior == 'stretch':
		if side == 'RGT':
			i = -1
		print ('This is %s.' %fingerbehavior)
		mc.setAttr ( nameNode + '.input2X', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
		mc.setAttr ( nameNode + '.input2Z', 0.5*i  )

	elif fingerbehavior == 'roll':
		print ('This is %s.' %fingerbehavior)
		mc.setAttr ( nameNode + '.input2X', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Y', -1.2*i  )
		mc.setAttr ( nameNode + '.input2Z', -1.2*i  )

		