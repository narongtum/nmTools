'''
from function.rigging import fingerOffsetRig 
reload(fingerOffsetRig)

This is for EH or Hope naming version it should be delete soon
'''

import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)


# 0 return global necessary variable
def defineVariable( fingerbehavior, fingerName , side , ctrlName , numCtrl , zroNam , offsetNam ):
	
	return fingerName,fingerbehavior,side,ctrlName,numCtrl,zroNam, offsetNam


'''
# 0 return neccery variable
defineVariable( finBehav = ('fist','roll','relax'), finNam = ('thumb','index','middle','ring','pinky') , sideNam = 'RGT' , ctrlNam = 'stickRGT_ctrl')
'''


# 1 create each offset group
def createOffsetGrp( side ,fingerName):
	# create 'offset' group
	for finger in fingerName:
		for num in range(1,4):
			print finger + '0' + str(num)+ side + '_Offset_grp'
			print finger + '0' + str(num)+ side + '_Zro_grp'
			print finger + '0' + str(num)+ side + '_ctrl'
			print '\n'
			
			offsetName = finger + '0' + str(num)+ side + '_Offset_grp'
			zroName = finger + '0' + str(num)+ side + '_Zro_grp'
			ctrlName = finger + '0' + str(num)+ side + '_ctrl'
			# create offset grp
			mc.group(empty = True , name = offsetName )
			# snap this grp to zroGrp position
			misc.snapParentConst( zroName , offsetName)
			# parent to under zro grp
			mc.parent(offsetName,zroName)
			# parent ctrlName to under offsetName grp
			mc.parent(ctrlName,offsetName)

			print '# Create %s' %offsetName

				
	


# 2
# create multiply divide for each finger behavior except relax 
def creaePostStore(side,fingerbehavior):
	if side == 'LFT':
		i = -1
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
				mc.setAttr ( nameNode + '.input2X', 10*i)
				mc.setAttr ( nameNode + '.input2Y', 11*i)
				mc.setAttr ( nameNode + '.input2Z', 12*i)

			elif each == 'roll':
				mc.setAttr ( nameNode + '.input2X', 1.2*i)
				mc.setAttr ( nameNode + '.input2Y', 1.2*i)
				mc.setAttr ( nameNode + '.input2Z', 1.2*i)


'''
# 2
# create multiply divide
# store   post finger except relax
creaePostStore(side)

'''




# 3 crerate relax node
# create for relax behavior
# create function for relax only
def creRelax( side, finName  ,amp ):
	nameNode = mc.createNode( 'multiplyDivide', name = finName + 'Relax' + side + '_mdv')
	mc.setAttr ( nameNode + '.input2X', 1	*-1	*amp)
	mc.setAttr ( nameNode + '.input2Y', 1.2	*-1	*amp)
	mc.setAttr ( nameNode + '.input2Z', 1.4	*-1	*amp)
	print nameNode
		
	
'''# 3
# create function for relax only
creRelax( finName = 'thumb', amp = 1.1)
creRelax( finName = 'index', amp = 2.1)
creRelax( finName = 'middle',  amp = 3.1)
creRelax( finName = 'ring',  amp = 4.1)
creRelax( finName = 'pinky',  amp = 5.1)'''









# 4.1
# internal function
# create store value for each finger lib
def _creStoVal(fingerName,fingerbehavior,side):
	store = []
	for finger in fingerName:
		for num in range(len(fingerbehavior)):
			print finger + 'StoreVal' + str(num) + side + '_pma'
			nameDriv = mc.createNode( 'plusMinusAverage',  name = finger + 'StoreVal'  + str(num+1).zfill(2) +  side + '_pma' )
			store.append(nameDriv)
	print 'create store value'
	return store
	


			

# 4.2
def connectToOffGrp(fingerName, fingerbehavior, side):
	store = _creStoVal(fingerName, fingerbehavior,side)		
	mc.select('*%s_Offset_grp' %side)
	offGrp = mc.ls(sl=True)

	offGrp.sort()
	# beware store grp it will be bug for sure
	store.sort()


	for s, o in zip(store,offGrp):
		mc.connectAttr(	'%s.output1D' %s , '%s.rotate.rotateZ' %o)
		print (	'%s.output1D' %s , '%s.rotate.rotateZ' %o)
		print '\n'


# 4.2
'''connectToOffGrp()'''






'''
# 5
# try to use OOP
# my  OOP so confuse
from function.rigging import core
reload(core)

# LFT Stick
stickRGT = core.Base()
stickRGT.createController('stick_ctrlShape')
stickRGT.setName(ctrlName)






from function.rigging.readWriteCtrlSizeData import flipController as fip
reload(fip)

# RGT Stick
sel = mc.select(ctrlName)
upSize = fip.buildUI()
upSize.flipCtrlShape(sel , axis=[3, 3, 3])

'''










# 6
def doCreateAttr( ctrlName ,fingerbehavior):
	for each in fingerbehavior:
		print '%s %s' %(ctrlName,each)
		mc.addAttr(ctrlName , longName = each, attributeType = 'double', defaultValue = 0)
		mc.setAttr('%s.%s' %(ctrlName, each), keyable = True)
	# lock and hide the translation,rotation attr
	for each in ('x','y','z') :
		mc.setAttr ("%s.t%s" %(ctrlName,each),lock = True, keyable = False, channelBox = False )
		mc.setAttr ("%s.r%s" %(ctrlName,each),lock = True, keyable = False, channelBox = False )
		mc.setAttr ("%s.s%s" %(ctrlName,each),lock = True, keyable = False, channelBox = False )





'''# 6
doCreateAttr( ctrlName  )'''







# 7
# #  stickLFT_ctrl.relax middleRelaxLFT_mdv.input1Z
##-----------------------------------  connection 1st for roll and fist 
def _normalCon( ctrlName  , name , side):
	for each in ('X','Y','Z'):	
		print '%s.%s'%(ctrlName,name )+' >>> '+ '%s%s_mdv.input1%s' %(name,side,each)
		mc.connectAttr('%s.%s'%(ctrlName, name), '%s%s_mdv.input1%s' %(name,side,each), force = True)


#7.1
def normalConnect( ctrlName , fingerbehavior , side):
	for name in fingerbehavior:
	    if name != 'relax':
		    _normalCon( ctrlName  , name ,side)


'''#7.1 
normalConnect( ctrlName , fingerbehavior )'''





# 8
# connection for relax
def conxAdv( ctrlName, side , finger = None, position = None):
	for axis in ('X','Y','Z'):  
		print 'conecting: %s.%s'%(ctrlName,finger) ,  '%s%s_mdv.input1%s' %(position,side,axis)
		mc.connectAttr('%s.%s'%(ctrlName,finger), '%s%s_mdv.input1%s' %(position,side,axis), force = True)
		



'''# 8
# connection for relax
conxAdv(string = 'stickRGT_ctrl', finger = 'relax', position = 'middleRelax')
conxAdv(string = 'stickRGT_ctrl', finger = 'relax', position = 'indexRelax')
conxAdv(string = 'stickRGT_ctrl', finger = 'relax', position = 'thumbRelax')
conxAdv(string = 'stickRGT_ctrl', finger = 'relax', position = 'ringRelax')
conxAdv(string = 'stickRGT_ctrl', finger = 'relax', position = 'pinkyRelax')'''





# specifiy each finger need to fix later
##-----------------------------------  connection 2dn  to store value just for roll and fist
def connectPma(   fingerbehavior , fingerName , side , nameOfPost , numVal = None ):
	numOfctrl = ('0','1','2')
	if len(fingerName) == 5:
		print 'this is five finger'
		for np, nc in zip(fingerbehavior , numOfctrl):
			if np != 'relax':
				
				print  'connect each finger here'
				print  '%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc)
				print  '%s%s_mdv.output.outputY' %(np,side) ,  'middleStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc) 
				print  '%s%s_mdv.output.outputZ' %(np,side) ,  'thumbStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc)
				print  'it seem must to fix here'
				mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'middleStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumbStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'ringStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'pinkyStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
	

	elif len(fingerName) == 3:
		for np, nc in zip(fingerbehavior , numOfctrl):
			if np != 'relax':
				
				print  'connect each finger here'
				print  '%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc)
				print  '%s%s_mdv.output.outputY' %(np,side) ,  'middleStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc) 
				print  '%s%s_mdv.output.outputZ' %(np,side) ,  'thumbStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc)
				print  'it seem must to fix here'
				mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'middleStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumbStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				#mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'ringStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				#mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'pinkyStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)

	elif len(fingerName) == 2:
		for np, nc in zip(fingerbehavior , numOfctrl):
			if np != 'relax':
				
				print  'connect each finger here'
				print  '%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc)
				#print  '%s%s_mdv.output.outputY' %(np,side) ,  'middleStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc) 
				print  '%s%s_mdv.output.outputZ' %(np,side) ,  'thumbStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc)
				print  'it seem must to fix here'
				mc.connectAttr('%s%s_mdv.output.outputX' %(np,side) ,  'indexStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				#mc.connectAttr('%s%s_mdv.output.outputY' %(np,side) ,  'middleStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'thumbStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				#mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'ringStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)
				#mc.connectAttr('%s%s_mdv.output.outputZ' %(np,side) ,  'pinkyStoreVal%s%s_pma.input1D[%s]' %(numVal,side,nc), force = True)

	print '######   connect complete  ######   '
		



'''# 9
connectPma(  nameOfPost = ('fist','roll'),numVal = '01')	
connectPma(  nameOfPost = ('fist','roll'),numVal = '02')
connectPma(  nameOfPost = ('fist','roll'),numVal = '03')'''




	

# 10
##-----------------------------------  connection 2.2dn for relax

def _connectForRelax( side,figName, finPst,  numVal ):
	mc.connectAttr( '%s%s%s_mdv.outputX' %(figName,finPst,side), '%sStoreVal%s%s_pma.input1D[2]' %(figName,numVal,side) , force = True )
	mc.connectAttr( '%s%s%s_mdv.outputY' %(figName,finPst,side), '%sStoreVal%s%s_pma.input1D[3]' %(figName,numVal,side) , force = True )
	mc.connectAttr( '%s%s%s_mdv.outputZ' %(figName,finPst,side), '%sStoreVal%s%s_pma.input1D[4]' %(figName,numVal,side) , force = True )
	
	
# 10.1

def doConnectRelax( side,figName ,finPst = None , numOfctrl = ('01','02','03') ):
    for number in numOfctrl:
         _connectForRelax( side,figName, finPst, number )
         print 'connecting... %s ' %figName

        


'''doConnectRelax(figName = 'index' , finPst = 'Relax', numOfctrl = ('01','02','03'))
doConnectRelax(figName = 'thumb' , finPst = 'Relax', numOfctrl = ('01','02','03'))	
doConnectRelax(figName = 'middle' , finPst = 'Relax', numOfctrl = ('01','02','03'))
doConnectRelax(figName = 'ring' , finPst = 'Relax', numOfctrl = ('01','02','03'))	
doConnectRelax(figName = 'pinky' , finPst = 'Relax', numOfctrl = ('01','02','03'))'''









'''from function.rigging.controllerBox import adjustController as adjust
reload(adjust)


mc.select(ctrlName)
zroName = adjust.createZroGrp()



misc.snapPointConst('hand%s_bind_jnt' %side,zroName)
misc.snapParentConstrMo('hand%s_bind_jnt' %side,zroName)

mc.parent(zroName,'fly_ctrl')		'''
	