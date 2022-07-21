import maya
from function.rigging.util import misc as misc
reload(misc)

'''
from function.rigging.feature import textureSwitch as switch
reload(switch)
'''

def findFaceMat():
	# enable material
	matList = mc.ls( '*_mat' )
	for name in matList:
		if 'face' in name:
			print name
			return name
		else:
			print 'Not have any face material in scene'

def findFileTexture( materialName ):
	# [1]  because 'file' is alway there
	spName = None
	fileTex = mc.listConnections ( materialName , connections = True )[1]
	spName = misc.splitName(fileTex)
	spName = spName[1] + '_' +spName[2]
	return fileTex,spName

def doEnableSeq( fileTex ):
	mc.setAttr( '%s.useFrameExtension' %fileTex , 1)
	
	print 'Please fix texture name and browse it by manual'
	# for active expression
	mc.select( fileTex, replace = True )
	maya.mel.eval(evalDeferred('ToggleAttributeEditor'))


def creaAttr( ctrlName , faceNum , fileTex ):
	mc.addAttr( ctrlName , longName = 'Face' , attributeType = 'long' , min = 1, max = faceNum, defaultValue = 1 , keyable = True )
	expNam = mc.rename( 'expression1' , '%s'%fileTex  + '_exp'  )
	mc.connectAttr( '%s.Face' %ctrlName , '%s.time' %expNam , force = True)






'''
# run command
materialName = switch.findFaceMat()
fileName = switch.findFileTexture(materialName)
switch.doEnableSeq(fileName[0])
switch.creaAttr(ctrlName = 'neck_ctrl',faceNum =  4, fileTex = fileName[1])
'''