'''
from function.rigging import fingerOffsetRig 
reload(fingerOffsetRig)
'''

# exe at file
'''
fingerCurl
'''

# Change from specific finger name to use index in list
# Adding finger preset 'cup'

# =================================
# - Store Function for main stick finger -
# =================================

import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.autoRig.base import core
reload(core)

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)



# 0 return global necessary variable
def defineVariable( fingerbehavior, fingerName , side , numCtrl, zroNam , offsetNam , stickNam ):
	# rawHand = misc.splitName( handNam )[0]
	# rawHand = rawHand.replace(side,'')
	
	return fingerName , fingerbehavior , side  , numCtrl , zroNam , offsetNam , stickNam 


'''
# 0 return neccery variable
defineVariable( finBehav = ('fist','roll','relax'), finNam = ('thumb','index','middle','ring','pinky') , sideNam = 'RGT' , ctrlNam = 'stickRGT_ctrl')
'''


# [1] create each offset group
def createOffsetGrp( side , fingerName , numCtrl  , zroNam , offsetNam ):
	print ('''\n
		# = = = = = = = = = createOffsetGrp Rig = = = = = = = = = #
		''')
	if numCtrl == 3:
		numOfctrl = (1,2,3)

	elif numCtrl == 2:
		numOfctrl = (1,2)

	else:
		mc.error('Too many element.')

	i = 1
	numOfctrl = []
	while i <= numCtrl :
		numOfctrl.append(i)
		i = i + 1



	# create 'offset' group
	offsetLst = []
	for finger in fingerName:
		# for num in range(1,4):
		for num in numOfctrl :


			logger.info(finger + '0' + str(num)+ side + offsetNam)
			logger.info(finger + '0' + str(num)+ side + zroNam)
			logger.info(finger + '0' + str(num)+ side + '_ctrl')
			print ('\n')
			

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
def creaePostStore(  nameSpace , side , fingerbehavior ):
	if side == 'LFT':
		i = 1
	elif side == 'RGT':
		i = -1
	else:
		i = -1






	nameNodeGrp = []
	for each in fingerbehavior:
		if each != 'relax' and each != 'cup':
			nameNode = mc.createNode( 'multiplyDivide', name = nameSpace  + each + side + '_mdv')
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

			elif each == 'baseSpread':
				mc.setAttr ( nameNode + '.input2X', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Z', 0.5*i  )

			elif each == 'wide':
				if side == 'LFT':
					i = 1
				elif side == 'RGT':
					i = -1
				mc.setAttr ( nameNode + '.input2X', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Z', 0.5*i  )

			# Adding new condition
			else:
				mc.setAttr ( nameNode + '.input2X', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Y', 0.5*i  )
				mc.setAttr ( nameNode + '.input2Z', 0.5*i  )












# [3] crerate relax node
# create function for relax  behavior
def creRelax( side, finName  ,amp ):
	nameNode = mc.createNode( 'multiplyDivide', name = finName + 'Relax' + side + '_mdv')
	mc.setAttr ( nameNode + '.input2X', 1	*-1	*amp	)
	mc.setAttr ( nameNode + '.input2Y', 1.2	*-1	*amp	)
	mc.setAttr ( nameNode + '.input2Z', 1.4	*-1	*amp	)
	print nameNode
		

# [3.1] crerate cup node
# create function for cup behavior
def creCup( side, finName  ,amp ):
	nameNode = mc.createNode( 'multiplyDivide', name = finName + 'Cup' + side + '_mdv')
	# reduce value for finger behavior
	mc.setAttr ( nameNode + '.input2X', -1*amp	)
	mc.setAttr ( nameNode + '.input2Y', -1*amp	)
	mc.setAttr ( nameNode + '.input2Z', -1*amp	)
	print nameNode



# [4.1]
# internal function
# create PMA for store value for each finger lib
def _creStoVal( fingerName , numCtrl , side , axis , type ):
	offsetGrp = []
	ampGrp = []

	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	# Change upperCase to lowerCase
	axis = axis.lower()

	for finger in fingerName:
		# for num in range( len( fingerbehavior ) ):
		for num in range( numCtrl ):

			nameDriv = mc.createNode( 'plusMinusAverage', name = finger  + str( num + 1 ).zfill(2) + type + axis + side + 'Offset' + '_pma' )
			print 'Create Pma Node...' + nameDriv
			offsetGrp.append(nameDriv)

			# create amplify for tune rotation value
			# amplify = mc.createNode( 'multDoubleLinear', name = finger  + str( num + 1 ).zfill(2) + type + axis + side + 'Amp' + '_mdl' )

			# Try to use class MDL instead
			amplify = core.MDLWithMul( finger  + str( num + 1 ).zfill(2) + type + axis + side + 'Amp' + '_mdl' )

			# Set amp of mdl value here
			# Change the condition a little about using namespace
			if num == 0: # is mean the first controller 
				if 'thumb' in finger:
					# why this is zero at first ?
					mc.setAttr('%s.multiply' %amplify.name, 0.25)
				elif 'index'in finger:
					mc.setAttr('%s.multiply' %amplify.name, 0.42)
				elif 'middle'in finger:
					mc.setAttr('%s.multiply' %amplify.name, 0.3)
				elif 'ring'in finger:
					mc.setAttr('%s.multiply' %amplify.name, 0.38)
				elif 'pinky'in finger:
					mc.setAttr('%s.multiply' %amplify.name, 0.68)
			else:
				mc.setAttr('%s.multiply' %amplify.name, 1)


			


			ampGrp.append(amplify.name)


	print 'Create offset value.'
	return offsetGrp,ampGrp
	

			

# [4.2] pma >>> offset_grp
def connectToOffGrp( fingerName , fingerbehavior , numCtrl , side , offsetNam , axis , type ):
	# return pma and amp 
	# store == pma
	# amp == double linear
	store,ampGrp = _creStoVal( fingerName, numCtrl , side , axis , type )		
	print 'This is for ' + axis + ' axis.'

	if type == 'translate':
		type = 'translate'
	elif type == 'rotate':
		type = 'rotate'

	offsetNam.sort()
	store.sort()
	ampGrp.sort()


	# Connect together
	for sto , off , amp in zip( store, offsetNam ,ampGrp ):

		print 'Connecting PMA >>> double ....'
		print (	'%s.output1D' %sto , '%s.%s' %(amp, 'input1')  )
		mc.connectAttr(	'%s.output1D' %sto , '%s.%s' %(amp, 'input1')  )

		# add for keep adjustable fingle control
		print 'Connecting double >>> offset group ....'
		print (	'%s.%s' %(amp, 'output')  , '%s.%s.%s%s' %( off,type,type,axis ) )
		mc.connectAttr(	'%s.%s' %(amp, 'output')  , '%s.%s.%s%s' %( off,type,type,axis ) )



	return ampGrp


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

##-----------------------------------  connection 1st for roll and fist 
def _normalCon( nameSpace , ctrlName  , name , side):
	# nameSpace = charName + elem
	for each in ('X','Y','Z'):	
		print '%s.%s'%(ctrlName,name )+' >>> '+ '%s%s%s_mdv.input1%s' %(nameSpace,name,side,each)
		mc.connectAttr('%s.%s'%(ctrlName, name), '%s%s%s_mdv.input1%s' %(nameSpace,name,side,each), force = True)






# [7.1]
# Connect mdv for normal finger behavior
# export value from ctrl to mdv
def normalConnect( nameSpace , ctrlName , fingerbehavior , side ):
	for name in fingerbehavior:
		if name != 'relax' and name != 'cup':
			_normalCon( nameSpace , ctrlName  , name ,side)






# [8]
# connection for relax finger
def conxAdv( ctrlName, side , finger = None, position = None):
	for axis in ('X','Y','Z'):  
		print 'conecting: %s.%s'%(ctrlName,finger) ,  '%s%s_mdv.input1%s' %(position,side,axis)
		mc.connectAttr('%s.%s'%(ctrlName,finger), '%s%s_mdv.input1%s' %(position,side,axis), force = True)
		



# [9]
# it shouln't specifiy each finger need to fix later
##-----------------------------------  connection 2dn  to store value just for roll and fist
def connectPma( 	nameSpace 							, 
					fingerName , side , numCtrl , nameOfPost 	, 
					numVal = None , axis = 'X' 					, 
					type = 'rotate'  								):
	# MDV >>> PMA
	print '''\n
	# = = = = = = = = = connect Plus minus average  = = = = = = = = = #
	'''


	numOfctrl = []
	i = 0
	while i <= numCtrl:
		numOfctrl.append(i)
		i = i + 1




	# nameSpace = charName + elem

	if type == 'translate':
		type = 'T'
	elif type == 'rotate':
		type = 'R'

	# 'indexStoreVal01LFT_pma.input1D[0]'
	# 'index01LFTOffset_pma'									having (01,02,03)
	# [_ctrl] >>> [   [ each finger behav ]_mdv  ] >>>  [   [ each offset grp ]_pma  ]
	offsetVal = 'Offset'
	# numOfctrl = ('0','1','2')
	print '####################'
	print numOfctrl
	print '####################'
	# 5 finger case
	if len(fingerName) == 5:
		print 'this is five finger'
		for np, nc in zip( nameOfPost , numOfctrl):
			print '####################'
			print np
			print nc
			print '####################'
			if np != 'relax':

				# design here what amp to pick					index_01_Rx_LFT
				print  np + ' >>> connect '
				print ('%s%s%s_mdv.output.outputX' %(nameSpace,np,side) ,  '%sindex%s%s%s%s_pma.input1D[%s]' 	%( nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputY' %(np,side) ,  '%smiddle%s%s%s%s_pma.input1D[%s]' %( nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%sthumb%s%s%s%s_pma.input1D[%s]' 	%( nameSpace,numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%sring%s%s%s%s_pma.input1D[%s]' 	%( nameSpace,numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%spinky%s%s%s%s_pma.input1D[%s]' 	%( nameSpace,numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				
				axis = axis.lower()
				mc.connectAttr('%s%s%s_mdv.output.outputX' %(nameSpace,np,side) ,  '%sindex%s%s%s%s_pma.input1D[%s]' %(  nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s%s_mdv.output.outputY' %(nameSpace,np,side) ,  '%smiddle%s%s%s%s_pma.input1D[%s]' %(  nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace,np,side) ,  '%sthumb%s%s%s%s_pma.input1D[%s]' %(  nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace,np,side) ,  '%sring%s%s%s%s_pma.input1D[%s]' %(  nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace,np,side) ,  '%spinky%s%s%s%s_pma.input1D[%s]' %(  nameSpace, numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)

			

	
	# middle 01 RX LFT Offset_pma
	elif len(fingerName) == 3:
		for np, nc in zip( nameOfPost , numOfctrl):
			if np != 'relax':
				print np
				print fingerName
				print np
				print  'Connect %s finger here..' %np
				print ( '%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 		%( fingerName[0],numVal , '%s' %type + axis , side , offsetVal , nc ) 		)
				print ( '%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 		%( fingerName[1],numVal , '%s' %type + axis , side , offsetVal , nc ) 		)
				print ( '%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 		%( fingerName[2],numVal , '%s' %type + axis , side , offsetVal , nc ) 		)
				axis = axis.lower()
				mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName[0],numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[1],numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName[2],numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				# OLD NAME NOTE HERE
				# mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)

	elif len(fingerName) == 2:
		for np, nc in zip( nameOfPost , numOfctrl):
			if np != 'relax':
				print numOfctrl
				print 'connect %s%s each finger here' %(np,nc)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%(fingerName[0], numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%(fingerName[1], numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				axis = axis.lower()
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[0],numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[1],numVal , '%s'%type + axis , side , offsetVal , nc ), force = True)


	print '######   connect complete  ######   '
		









# [10]
##-----------------------------------  connection 2.2dn for relax

def _connectForRelax( side, figName, finPst,  numVal, inputIndex, axis = 'X' ):
	offsetVal = 'Offset'
	axis = axis.lower()																	
	mc.connectAttr( '%s%s%s_mdv.outputX' %(figName,finPst,side), '%s%s%s%s%s_pma.input1D[%i]' %( figName , numVal , 'R' + axis , side , offsetVal ,inputIndex[0]) , force = True )
	mc.connectAttr( '%s%s%s_mdv.outputY' %(figName,finPst,side), '%s%s%s%s%s_pma.input1D[%i]' %( figName , numVal , 'R' + axis , side , offsetVal ,inputIndex[1]) , force = True )
	mc.connectAttr( '%s%s%s_mdv.outputZ' %(figName,finPst,side), '%s%s%s%s%s_pma.input1D[%i]' %( figName , numVal , 'R' + axis , side , offsetVal ,inputIndex[2]) , force = True )

	
# 'index01LFTOffset_pma'	
# 10.1
def doConnectRelax( side, figName, numCtrl, finPst = None , inputIndex = (2,3,4) ):
	print '''\n
	# = = = = = = = = = doConnect Relax = = = = = = = = = #
	'''



	# using new condition
	numOfctrl = []
	i = 1
	while i <= numCtrl:
		io ='{:02d}'.format(i)
		numOfctrl.append(io)
		i = i + 1


	for number in numOfctrl:



		print number

		_connectForRelax( side,figName, finPst, number ,inputIndex)
		print 'connecting... %s ' %figName
	
	print '##### END of script ####'
	


# [10.5]
# pma to offset axis z grp
def connectSpreadPma( 	nameSpace 		, 
						fingerName , side 	, nameOfPost , 
						numVal = None , axis = 'X' , numCtrl = 3):
	# nameSpace = charName + elem 
	offsetVal = 'Offset'
	

	# numOfctrl = ('0','1','2')

	i = 0
	numOfctrl = []
	while i < numCtrl :
		numOfctrl.append(i)
		i = i + 1


	axis = axis.lower()
	# 'thumb','index','middle','ring','pinky' 
	if len(fingerName) == 5:
		print "	''thumb','index','middle','ring','pinky' ,   finger'	"
		# except middle fingle
		for np, nc in zip( nameOfPost , numOfctrl):	
			print  np + 'spreadLFT_mdv >>> connect thumb01RzLFTOffset_pma'
			print ('%s%s%s_mdv.output.outputZ' %(nameSpace ,np,side) , 	'%s%s%s%s%s%s_pma.input1D[%s]' 	%(nameSpace, fingerName[0],numVal , 'R'+ axis , side , offsetVal , nc ) 		)
			print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s%s_pma.inxxput1D[%s]' 	%(nameSpace, fingerName[1],numVal , 'R'+ axis , side , offsetVal , nc ) 		)
			print ('%s%s_mdv.output.outputY' %(np,side) ,  '%s%s%s%s%s%s_pma.inxxxput1D[%s]' 	%( nameSpace,fingerName[2],numVal , 'R'+ axis , side , offsetVal , nc ) 		)
			print ('%s%s_mdv.output.outputX' %(np,side) ,  '%s%s%s%s%s%s_pma.inxxxxxxxxput1D[%s]' 	%( nameSpace,fingerName[3],numVal , 'R'+ axis , side , offsetVal , nc ) 		)
			print ('%s%s_mdv.output.outputX' %(np,side) ,  '%s%s%s%s%s%s_pma.inxxxxxput1D[%s]' 	%( nameSpace,fingerName[4],numVal , 'R'+ axis , side , offsetVal , nc ) 		)

			
			# noneed to add namespaer because it add earalyer
			mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace ,np,side) , 	'%s%s%s%s%s_pma.input1D[%s]' %( fingerName[0], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace ,np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[1], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s%s_mdv.output.outputY' %(nameSpace ,np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[2], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s%s_mdv.output.outputX' %(nameSpace ,np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[3], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			mc.connectAttr('%s%s%s_mdv.output.outputX' %(nameSpace ,np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[4], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			# mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace ,np,side) , 	'%s%s%s%s%s%s_pma.input1D[%s]' %(nameSpace, fingerName[0], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			# mc.connectAttr('%s%s%s_mdv.output.outputZ' %(nameSpace ,np,side) ,  '%s%s%s%s%s%s_pma.input1D[%s]' %(nameSpace, fingerName[1], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			# mc.connectAttr('%s%s%s_mdv.output.outputY' %(nameSpace ,np,side) ,  '%s%s%s%s%s%s_pma.input1D[%s]' %(nameSpace, fingerName[2], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			# mc.connectAttr('%s%s%s_mdv.output.outputX' %(nameSpace ,np,side) ,  '%s%s%s%s%s%s_pma.input1D[%s]' %(nameSpace, fingerName[3], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			# mc.connectAttr('%s%s%s_mdv.output.outputX' %(nameSpace ,np,side) ,  '%s%s%s%s%s%s_pma.input1D[%s]' %(nameSpace, fingerName[4], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
			#									 ^^^ notice axis here is up to finger behavior


	elif len(fingerName) == 3:
		# 'thumb','index','middle'
		print 'This is 3 finger.'
		for np, nc in zip( nameOfPost , numOfctrl):	
				
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName[0],numVal , '%s'%type + axis , side , offsetVal , nc ) 		)
				print ('%s%s_mdv.output.outputY' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName[1],numVal , '%s'%type + axis , side , offsetVal , nc )		)
				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName[2],numVal , '%s'%type + axis , side , offsetVal , nc ) 		)

				axis = axis.lower()
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[0], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[1], numVal , 'R'+axis , side , offsetVal , nc ), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[2], numVal , 'R'+ axis , side , offsetVal , nc ), force = True)


	elif len(fingerName) == 2:
		# 'thumb'
		for np, nc in zip( nameOfPost , numOfctrl):	
				
				print  'connect thumb only spread finger here'

				print '###%s%s###' 	%(fingerName[0],numVal)

				print ('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' 	%( fingerName[0], numVal , 'R'+ axis , side , offsetVal , nc ) 		)

				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  '%s%s%s%s%s_pma.input1D[%s]' %( fingerName[0], numVal ,'R'+ axis , side , offsetVal , nc ), force = True)





