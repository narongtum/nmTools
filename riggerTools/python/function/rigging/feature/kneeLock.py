'''
from function.rigging.version import kneeLock_v001 
'''
import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)

from function.pipeline import fileTools as fileTools 
reload(fileTools)



def createDistance( startP = None , endP = None ):
	uprDistance = mc.distanceDimension( startPoint = (0, 0, 0), endPoint = (0.2, 0.2, 0.2) )

	misc.snapPointCon(startP, 'locator1')
	misc.snapPointConstr(startP, 'locator1')

	misc.snapPointCon(endP, 'locator2')
	misc.snapPointConstr(endP, 'locator2')

	for axis in ('X','Y','Z'):
		for shape in (1,2):
			print 'set %s and %d' %(axis,shape)
			
			mc.setAttr('locatorShape%d.localScale%s'%(shape,axis) , 0.15)


	newnameUPR = fileTools.splitName( name = startP , splitwith = '_' )
	print 'newnameUPR is %s' %newnameUPR

	newnameLWR = fileTools.splitName( name = endP , splitwith = '_' )
	print 'newnameLWR is %s' %newnameLWR

	uprLoc = mc.rename( 'locator1', newnameUPR[0] + '_loc')
	lwrLoc = mc.rename( 'locator2', newnameLWR[3] +'Pov'+ newnameLWR[4] + '_loc' )
	uprDistance = mc.rename( 'distanceDimension1', newnameLWR[0] +  '_distance' )
	print newnameUPR[0], newnameLWR[0], uprDistance, newnameUPR[-2], newnameLWR[-2]  ,newnameLWR[-1] ,endP ,uprLoc ,lwrLoc
	return newnameUPR[0], newnameLWR[0], uprDistance, newnameUPR[-2], newnameLWR[-2] ,newnameLWR[-1] ,endP ,uprLoc ,lwrLoc


# create multiply and blendColor  
def createBlendColor( name = None, uprDistance = None, lwrDistance = None , side = None , uprNam = None):
	# create invert value for RGT side
	invertNode = mc.createNode('multiplyDivide' , name = uprNam +'Invert'+ side + '_mdv')

	multiply = None
	if side == 'LFT':
		multiply = 1
	elif side == 'RGT':
		multiply = -1
	for axis in ('X','Y','Z'):
		mc.setAttr('%s.input2%s' %(invertNode, axis ), multiply * 1)
	#return invertNode



	# create blendColor
	blendName = mc.createNode('blendColors', name = 'choice' + name  +'_blc')
	print uprDistance + 'Shape.distance' , blendName +  '.color1R'
	print lwrDistance + 'Shape.distance' , blendName + '.color2R'
	# distance >> invertNode
	mc.connectAttr( uprDistance + 'Shape.distance' , invertNode +  '.input1X', force = True )
	mc.connectAttr( lwrDistance + 'Shape.distance' , invertNode +  '.input1Y', force = True )

	# invertNode >> color
	mc.connectAttr( invertNode +  '.outputX' , blendName +  '.color1R', force = True )
	mc.connectAttr( invertNode +  '.outputY' , blendName +  '.color1G', force = True )

	# mc.connectAttr( uprDistance + 'Shape.distance' , blendName +  '.color1R', force = True )
	# mc.connectAttr( lwrDistance + 'Shape.distance' , blendName +  '.color1G', force = True )
	return blendName , invertNode


def doAddAttr (povName , type):
	kind = None
	if type == 'foot':
		kind = 'knee'
	elif type == 'hand':
		kind = 'elbow'
	else:
		pass
	print 'this is a %s and POV is %s' %( kind, povName )
	mc.addAttr( povName , longName = '%sLock' %kind, attributeType = 'double' , min = 0.0, max = 1.0, defaultValue = 0 ,keyable = True)
	return '%sLock' %kind




def distJnt(	stretchNode , upperJnt , lowerJnt , blendName , namLock	, povName ):
	
	print blendName
	print upperJnt
	print stretchNode
	print lowerJnt

	mc.connectAttr (	'%s.output2Dx'	%stretchNode	,  '%s.color2R' 	%blendName	,	force = True)
	mc.connectAttr (	'%s.output2Dy'	%stretchNode	,  '%s.color2G' 	%blendName	,	force = True)
	mc.connectAttr (	'%s.outputR'	%blendName		,  '%s.translateY'  %upperJnt	,	force = True) 
	mc.connectAttr (	'%s.outputG'	%blendName		,  '%s.translateY'  %lowerJnt	,	force = True)   
	
	# connect blend value to POV
	print  '%s.%s'  %(povName,namLock)
	mc.connectAttr (	'%s.%s'  %(povName,namLock)	,	'%s.blender'	%blendName 	,	force = True)




def arrangeGrp(nameGrp , side , uprLoc , lwrLoc , distanceName ):
	grpName = mc.group( empty = True , name = nameGrp + 'distance' + side + '_grp')

	print nameGrp , side , uprLoc , lwrLoc , distanceName
	print nameGrp + side +'distance' 

	mc.parent( uprLoc, grpName)
	mc.parent( lwrLoc, grpName)
	mc.parent( distanceName, grpName)

	# move distance grp to DO NOT TOUCH Grp
	mc.parent( grpName , 'NOTOUCH_grp' )



'''

mc.connectAttr('legStretchLFT_pma.output2Dx' , choiceupperLegLFT_blc.color2R, r=True)

connectAttr -f legStretchLFT_pma.output2Dy choiceupperLegLFT_blc.color2G;

connectAttr -f choiceupperLegLFT_blc.outputR lowerLegLFT_IK_jnt.translateY;

connectAttr -f legStretchLFT_pma.output2Dx choiceupperLegLFT_blc.color2R

connectAttr -f legStretchLFT_pma.output2Dy choiceupperLegLFT_blc.color2G

connectAttr -f choiceupperLegLFT_blc.outputR lowerLegLFT_IK_jnt.translateY

connectAttr -f choiceupperLegLFT_blc.outputG footLFT_IK_jnt.translateY











def disconnectJnt( namePart , side ): #use name nameUPR[0]
	if side == 'LFT':
		if namePart == 'leg':
			print 'this is LFT leg part1 lowerLegLFT_IK_jnt '
		elif namePart == 'arm':
			print 'something2 lowerArmLFT_IK_jnt'
	if side == 'RGT':
		if namePart == 'leg':
			print 'this is LFT leg part3'
		elif namePart == 'arm':
			print 'something4'




#def printMe( uprDistance = None, lwrDistance = None ):
	




connectAttr -f legStretchLFT_pma.output2Dx choiceupperLegLFT_blc.color2R;

connectAttr -f legStretchLFT_pma.output2Dy choiceupperLegLFT_blc.color2G;

connectAttr -f choiceupperLegLFT_blc.outputR lowerLegLFT_IK_jnt.translateY;



'''	

