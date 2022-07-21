'''
from function.rigging import fingerOffsetRig 
reload(fingerOffsetRig)
'''

import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.autoRig.base import core
reload(core)

# 0 return global necessary variable
def defineVariable( fingerbehavior, fingerName , side , numCtrl, zroNam , offsetNam ):
	
	return fingerName , fingerbehavior , side  , numCtrl , zroNam , offsetNam


'''
# 0 return neccery variable
defineVariable( finBehav = ('fist','roll','relax'), finNam = ('thumb','index','middle','ring','pinky') , sideNam = 'RGT' , ctrlNam = 'stickRGT_ctrl')
'''


# [1] create each offset group
def createOffsetGrp( side , fingerName , zroNam , offsetNam ):
	# create 'offset' group
	offsetLst = []
	for finger in fingerName:
		for num in range(1,4):
			print finger + '0' + str(num)+ side + offsetNam
			print finger + '0' + str(num)+ side + zroNam
			print finger + '0' + str(num)+ side + '_ctrl'
			print '\n'
			
			offsetName = finger + '0' + str(num)+ side + offsetNam
			zroName = finger + '0' + str(num)+ side + zroNam
			ctrlName = finger + '0' + str(num)+ side + '_ctrl'
			# create offset grp
			offsetGrp = mc.group(empty = True , name = offsetName )
			# print offsetGrp
			offsetLst.append(offsetGrp)
			# snap this grp to zroGrp position
			misc.snapParentConst( zroName , offsetName)
			# parent to under zro grp
			mc.parent(offsetName,zroName)
			mc.setAttr( "%s.scaleX" %offsetName  , 1)
			mc.setAttr( "%s.scaleY" %offsetName  , 1)
			mc.setAttr( "%s.scaleZ" %offsetName  , 1)
			# parent ctrlName to under offsetName grp
			mc.parent(ctrlName,offsetName)



	
	print '# Create offset grp...'
	return offsetLst


# [2]
# create multiply divide for each finger behavior except relax 
def creaePostStore( side , fingerbehavior ):
	if side == 'LFT':
		i = 1
	else:
		i = -1
	nameNodeGrp = []
	for each in fingerbehavior:
		if each != 'relax':
			nameNode = mc.createNode( 'multiplyDivide', name = each + side + '_mdv')
			nameNodeGrp.append(nameNode)
			print nameNode
			print '\n'

			# if this side is LFT
			# this is hardcode but i dunno what to do
			if each == 'fist':
				i = 1
				mc.setAttr ( nameNode + '.input2X', -10*i  )
				mc.setAttr ( nameNode + '.input2Y', -11*i  )
				mc.setAttr ( nameNode + '.input2Z', -12*i  )

			elif each == 'roll':
				i = 1
				mc.setAttr ( nameNode + '.input2X', -1.2*i  )
				mc.setAttr ( nameNode + '.input2Y', -1.2*i  )
				mc.setAttr ( nameNode + '.input2Z', -1.2*i  )

			elif each == 'spread':
				i = 1
				mc.setAttr ( nameNode + '.input2X', 1.3*i  )
				mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Z', -0.5*i  )

			elif each == 'stretch':
				mc.setAttr ( nameNode + '.input2X', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Z', 0.5*i  )








# [3] crerate relax node
# create function for relax  behavior
def creRelax( side, finName  ,amp ):
	nameNode = mc.createNode( 'multiplyDivide', name = finName + 'Relax' + side + '_mdv')
	mc.setAttr ( nameNode + '.input2X', 1	*-1	*amp)
	mc.setAttr ( nameNode + '.input2Y', 1.2	*-1	*amp)
	mc.setAttr ( nameNode + '.input2Z', 1.4	*-1	*amp)
	print nameNode
		



# index  01  LFT  Offset _pma

# [4.1]
# internal function
# create store value for each finger lib
def _creStoVal( fingerName , numCtrl , side , axis , type ):
	offset = []
	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	for finger in fingerName:
		# for num in range( len( fingerbehavior ) ):
		for num in range( numCtrl ):
			
			nameDriv = mc.createNode( 'plusMinusAverage', name = finger  + str( num + 1 ).zfill(2) + type + axis + side + 'Offset' + '_pma' )
			print 'Create Pma Node...' + nameDriv
			offset.append(nameDriv)
	print 'Create offset value.'
	return offset
	

			

# [4.2]
def connectToOffGrp( fingerName , fingerbehavior , numCtrl , side , offsetNam , axis , type ):
	store = _creStoVal( fingerName, numCtrl , side , axis , type )		
	print 'This is for ' + axis + ' axis.'

	if type == 'translate':
		type = 'translate'
	elif type == 'rotate':
		type = 'rotate'

	offsetNam.sort()
	store.sort()

	for sto , off in zip( store,offsetNam ):
		print 'Connecting ....'
		print (	'%s.output1D' %sto , '%s.%s.%s%s' %( off,type,type,axis ) )
		# For spread fingerbehavior is should connect in z axis i will find the solution
		mc.connectAttr(	'%s.output1D' %sto , '%s.%s.%s%s' %( off,type,type,axis ) )


# [4.3] Create connect pma >>> offset group




# [6]
def doCreateAttr( ctrlName , fingerbehavior ):
	for each in fingerbehavior:
		print '%s %s' %(ctrlName,each)
		mc.addAttr(ctrlName , longName = each, attributeType = 'double', defaultValue = 0)
		mc.setAttr('%s.%s' %(ctrlName, each), keyable = True)
	# lock and hide the translation,rotation attr
	for each in ('x','y','z') :
		mc.setAttr ("%s.t%s" %(ctrlName,each),lock = True, keyable = False, channelBox = False )
		mc.setAttr ("%s.r%s" %(ctrlName,each),lock = True, keyable = False, channelBox = False )
		mc.setAttr ("%s.s%s" %(ctrlName,each),lock = True, keyable = False, channelBox = False )







# 7
# #  stickLFT_ctrl.relax middleRelaxLFT_mdv.input1Z
##-----------------------------------  connection 1st for roll and fist 
def _normalCon( ctrlName  , name , side):
	for each in ('X','Y','Z'):	
		print '%s.%s'%(ctrlName,name )+' >>> '+ '%s%s_mdv.input1%s' %(name,side,each)
		mc.connectAttr('%s.%s'%(ctrlName, name), '%s%s_mdv.input1%s' %(name,side,each), force = True)

'''
# [7.5] for local finger
def _normalLocalCon( ctrlName  , fingerbehavior , fingerName , side ):
	for each in ('X','Y','Z'):	
		print '%s.%s'%(ctrlName,fingerbehavior )+' >>> '+ '%s%s%s_mdv.input1%s' %( fingerName,fingerbehavior,side,each )
		mc.connectAttr('%s.%s'%(ctrlName, fingerbehavior), '%s%s%s_mdv.input1%s' %( fingerName,fingerbehavior,side,each ), force = True)
'''




# [7.1]
# Connect normal finger behavior
# export value from ctrl to mdv
def normalConnect( ctrlName , fingerbehavior , side ):
	for name in fingerbehavior:
		if name != 'relax':
			_normalCon( ctrlName  , name ,side)






# [8]
# connection for relax finger
def conxAdv( ctrlName, side , finger = None, position = None):
	for axis in ('X','Y','Z'):  
		print 'conecting: %s.%s'%(ctrlName,finger) ,  '%s%s_mdv.input1%s' %(position,side,axis)
		mc.connectAttr('%s.%s'%(ctrlName,finger), '%s%s_mdv.input1%s' %(position,side,axis), force = True)
		



# [9]
# it shouln't specifiy each finger need to fix later
##-----------------------------------  connection 2dn  to store value just for roll and fist
def connectPma( 	charName  , elem  					, 
					fingerName , side , nameOfPost 		, 
					numVal = None , axis = 'X' 			, 
					type = 'rotate'  						):


	naming = charName + elem

	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	# 'indexStoreVal01LFT_pma.input1D[0]'
	# 'index01LFTOffset_pma'									having (01,02,03)
	# [_ctrl] >>> [   [ each finger behav ]_mdv  ] >>>  [   [ each offset grp ]_pma  ]
	offsetVal = 'Offset'
	numOfctrl = ('0','1','2')

	# 5 finger case
	if len(fingerName) == 5:
		print 'this is five finger'
		for np, nc in zip( nameOfPost , numOfctrl):
			if np != 'relax':

				
				print  np + '>>> connect '
				print ('%s%s_mdv.output.outputX' %(np,side) ,  '%sindex%s%s%s%s_pma.input1D[%s]' 	%( naming, numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputY' %(np,side) ,  '%smiddle%s%s%s%s_pma.input1D[%s]' %( naming, numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%sthumb%s%s%s%s_pma.input1D[%s]' 	%( naming,numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%sring%s%s%s%s_pma.input1D[%s]' 	%( naming,numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%spinky%s%s%s%s_pma.input1D[%s]' 	%( naming,numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				# fix what
				mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  '%sindex%s%s%s%s_pma.input1D[%s]' %(  naming, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  '%smiddle%s%s%s%s_pma.input1D[%s]' %(  naming, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%sthumb%s%s%s%s_pma.input1D[%s]' %(  naming, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%sring%s%s%s%s_pma.input1D[%s]' %(  naming, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%spinky%s%s%s%s_pma.input1D[%s]' %(  naming, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)

			

	
	# middle 01 RX LFT Offset_pma
	elif len(fingerName) == 3:
		for np, nc in zip( nameOfPost , numOfctrl):
			if np != 'relax':
				
				print  'connect each finger here'
				print ( '%s%s_mdv.output.outputZ' %(np,side) ,  'index%s%s%s%s_pma.input1D[%s]' 		%( numVal , '%s' %type + axis , side , offsetVal , nc ) 		)
				print ( '%s%s_mdv.output.outputZ' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' 		%( numVal , '%s' %type + axis , side , offsetVal , nc ) 		)
				print ( '%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' 		%( numVal , '%s' %type + axis , side , offsetVal , nc ) 		)

				mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'index%s%s%s%s_pma.input1D[%s]' 	%( numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' %( numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' 	%( numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				# OLD NAME NOTE HERE
				# mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)

	elif len(fingerName) == 2:
		for np, nc in zip( nameOfPost , numOfctrl):
			if np != 'relax':
				
				print  'connect each finger here'
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' 	%( numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' 	%( numVal , '%s'%type + axis , side , offsetVal , nc ) 		)

				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' %( numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' %( numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)


	print '######   connect complete  ######   '
		









# [10]
##-----------------------------------  connection 2.2dn for relax

def _connectForRelax( side,figName, finPst,  numVal , axis = 'X'):
	offsetVal = 'Offset'
																			#middle 01 RX LFT Offset_pma
	mc.connectAttr( '%s%s%s_mdv.outputX' %(figName,finPst,side), '%s%s%s%s%s_pma.input1D[2]' %( figName , numVal , 'R' + axis , side , offsetVal ) , force = True )
	mc.connectAttr( '%s%s%s_mdv.outputY' %(figName,finPst,side), '%s%s%s%s%s_pma.input1D[3]' %( figName , numVal , 'R' + axis , side , offsetVal ) , force = True )
	mc.connectAttr( '%s%s%s_mdv.outputZ' %(figName,finPst,side), '%s%s%s%s%s_pma.input1D[4]' %( figName , numVal , 'R' + axis , side , offsetVal ) , force = True )

	
# 'index01LFTOffset_pma'	
# 10.1
def doConnectRelax( side,figName ,finPst = None , numOfctrl = ('01','02','03') ):
	for number in numOfctrl:
		 _connectForRelax( side,figName, finPst, number )
		 print 'connecting... %s ' %figName
	
	print '##### END of script ####'
	


# [10.5]
# pma to offset axis z grp
def connectSpreadPma( fingerName , side , nameOfPost , numVal = None , axis = 'X'):
	offsetVal = 'Offset'
	numOfctrl = ('0','1','2')

	# 5 finger case
	if len(fingerName) == 5:
		print 'this is five finger'
		# except middle fingle
		for np, nc in zip( nameOfPost , numOfctrl):	
			print  np + '>>> connect '
			print ('%s%s_mdv.output.outputX' %(np,side) ,  'index%s%s%s%s_pma.input1D[%s]' 	%( numVal , 'R'+ axis , side , offsetVal , nc ) 		)
			print ('%s%s_mdv.output.outputY' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ) 		)
			print ('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' 	%( numVal , 'R'+ axis , side , offsetVal , nc ) 		)

			mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'index%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'ring%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'pinky%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			#									 ^^^ notice axis here is up to finger behavior


	elif len(fingerName) == 3:
		# index and thumb only
		print 'this is three finger'
		for np, nc in zip( nameOfPost , numOfctrl):	
				
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  'index%s%s%s%s_pma.input1D[%s]' 	%( numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputY' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' %( numVal , '%s'%type + axis , side , offsetVal , nc )		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' 	%( numVal , '%s'%type + axis , side , offsetVal , nc ) 		)

				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'index%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'middle%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' %( numVal , 'R'+ axis , side , offsetVal , nc ), force = True)


	elif len(fingerName) == 2:
		# thumb only
		for np, nc in zip( nameOfPost , numOfctrl):	
				
				print  'connect each spread finger here'
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' 	%( numVal , 'R'+ axis , side , offsetVal , nc , nc ) 		)

				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumb%s%s%s%s_pma.input1D[%s]' %( numVal ,'R'+ axis , side , offsetVal , nc ), force = True)





