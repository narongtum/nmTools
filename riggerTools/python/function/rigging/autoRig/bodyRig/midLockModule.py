'''
from function.rigging.autoRig.bodyRig import midLockModule
reload( midLockModule )

for elbow and knee lock

# Log
# please check line 142
# update function for fix scaleable controller 
# create compensate knee/elbow 



'''

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import core
reload(core)

from function.pipeline import logger 
reload(logger)

class MidLockLogger(logger.MayaLogger):
	LOGGER_NAME = "MidLock"

# feature create elbow knee lock					
#uprDistance = mc.distanceDimension( startPoint = (0, 0, 0), endPoint = (0.2, 0.2, 0.2) )
def createDistance( nameSpace , part , startP = None , endP = None , noTouchGrp = 'noTouch_grp' 	):

	core.makeHeader('Start of %s ' %'createDistance')

	# RenameSpace
	rawNameUPR =   startP.split('_')
	MidLockLogger.info('rawNameUPR is %s' %rawNameUPR)


	rawNameLWR =  endP.split('_')
	MidLockLogger.info('rawNameLWR is %s' %rawNameLWR)




	if len(rawNameUPR) == 2:
		rawNameUPR = rawNameUPR[0]

	elif len(rawNameUPR) == 3:
		rawNameUPR = rawNameUPR[0] + '_' + rawNameUPR[1]

	elif len(rawNameUPR) == 4:
		rawNameUPR = rawNameUPR[0] + '_' + rawNameUPR[1]  + '_' + rawNameUPR[2]  



	if len(rawNameLWR) == 2:
		rawNameLWR = rawNameLWR[0]

	elif len(rawNameLWR) == 3:
		rawNameLWR = rawNameLWR[0] + '_' + rawNameLWR[1]

	elif len(rawNameLWR) == 4:
		rawNameLWR = rawNameLWR[0] + '_' + rawNameLWR[1]  + '_' + rawNameLWR[2]  


	else:
		mc.warning('Too many element please check naming.')



	# nameSpace = nameSpace + elem
	# Create distance with locator already connect

	if part =='up':
		uprLoc = nameSpace + 'lockUp' + rawNameUPR + '_loc' 
		lwrLoc = nameSpace + 'lockUp' + rawNameLWR + '_loc' 
	elif part == 'dn':
		uprLoc = nameSpace + 'lockDn' + rawNameUPR + '_loc' 
		lwrLoc = nameSpace + 'lockDn' + rawNameLWR + '_loc' 
	else:
		uprLoc = nameSpace + 'lock' + rawNameUPR + '_loc' 
		lwrLoc = nameSpace + 'lock' + rawNameLWR + '_loc' 


	uprDistanceName = nameSpace + 'lock' + rawNameUPR  +  '_dtw' 


	# for prevent already locator name
	# if mc.objExists('locator1'):
	# 	mc.rename('locator1','replaceName_1')
	# 	MidLockLogger.info('Rename locator1 to replaceName_1')
	# if mc.objExists('locator2'):
	# 	mc.rename('locator2','replaceName_2')
	# 	MidLockLogger.info('Rename locator2 to replaceName_2')

	# distance = core.DistanceDimension( uprLoc ,lwrLoc , uprDistanceName ,startPoint = (0.8, 0.8, 0.8), endPoint = (0.5, 0.5, 0.5) )
	
	try:
		# misc.renameAllLocator(suffix='_tempLoc') # VERY SENSITIVE PROCEED WITH CUATION
		# instancing 
		distance = core.DistanceDimension( uprLoc ,lwrLoc , uprDistanceName ,startPoint = (0.8, 0.8, 0.8), endPoint = (0.5, 0.5, 0.5) )	
	except :
		mc.error('There are more than locator1 than one Please change name.')

		# MidLockLogger.info(__name__)
		# mc.error('locator1 is more than one Please change name')

	MidLockLogger.info(startP)
	MidLockLogger.info(uprLoc)

	# Snap and Constraint
	# misc.snapPointConstr(startP, 'locator1' , mo = False )
	mc.pointConstraint( startP, uprLoc , mo = False , name = nameSpace  + 'lock' + part.capitalize() + rawNameUPR +  '_poinCon' )
	# set the name for both
	# misc.snapPointConstr(endP, 'locator2', mo = False)
	mc.pointConstraint( endP, lwrLoc, mo = False , name = nameSpace + 'lock' + part.capitalize() + rawNameLWR  +  '_poinCon' )

	# Just make locator larger
	for axis in ('X','Y','Z'):
		mc.setAttr('%sShape.localScale%s'%( uprLoc ,axis ) , 0.15 )
		mc.setAttr('%sShape.localScale%s'%( lwrLoc ,axis ) , 0.15 )

	'''
	for axis in ('X','Y','Z'):
		for shape in (1,2):
			print 'set %s and %d' %( axis,shape )
			mc.setAttr('Shape%d.localScale%s'%( shape,axis ) , 0.15 )'''




	# upperArmFkLFT elbowLFT elbowLFT_distance upperArmFkLFT elbowLFT ctrl elbowLFT_ctrl upperArmFkLFT_loc elbowLFTPov_loc
	# print rawNameUPR[0], rawNameLWR[0], uprDistanceName, rawNameUPR[-2], rawNameLWR[-2] ,rawNameLWR[-1] ,endP ,uprLoc ,lwrLoc

				# rawNameUPR	rawNameLWR						uprDistance	 nameUPR									 ctrl			ctrl
	# return rawNameUPR[0], rawNameLWR[0], uprDistanceName, rawNameUPR[-2], rawNameLWR[-2] ,rawNameLWR[-1] ,endP ,uprLoc ,lwrLoc

			# rawnameUPR      rawnameLWR    uprDistanceName 


	elbowKneeLock_grp = core.Null( nameSpace + 'lock' + rawNameUPR  +  '_grp' )
	mc.parent( uprLoc , elbowKneeLock_grp )
	mc.parent( lwrLoc , elbowKneeLock_grp )
	mc.parent( uprDistanceName , elbowKneeLock_grp )

	if noTouchGrp:
		mc.parent( elbowKneeLock_grp , noTouchGrp )
		



	elbowKneeLock_grp.attr('visibility').value = 0
	MidLockLogger.info('End')


	print (rawNameUPR, uprDistanceName ,endP ,uprLoc ,lwrLoc)
	return rawNameUPR, uprDistanceName,endP ,uprLoc ,lwrLoc




# create multiply and blendColor  
def createBlendColor(  nameSpace  ,  uprDistance = None, lwrDistance = None , side = None , uprNam = None , placementNam = 'placement_ctrl'):
	'''
	Copy shape to a specified target transform.
	@param shape: Shape or copy to target transform
	@type shape: str
	'''
	# nameSpace = nameSpace + elem

	# create invert value for RGT side (if RGT side invert the value)
	invertNode = mc.createNode('multiplyDivide' , name =  uprNam +'Invert' + '_mdv')

	multiply = None
	if side == 'LFT':
		multiply = 1
	elif side == 'RGT':
		multiply = -1
	else:
		multiply = 1
	for axis in ('X','Y','Z'):
		mc.setAttr('%s.input2%s' %(invertNode, axis ), multiply * 1)


	# create blendColor
	blendName = mc.createNode('blendColors', name = nameSpace + 'choice' + uprNam  +'_blc')

	MidLockLogger.info('{0}Shape.distance , {1}.color1R'.format(uprDistance,blendName))
	MidLockLogger.info('{0}Shape.distance , {1}.color1R'.format(lwrDistance,blendName))



	# connect distance >> invertNode
	mc.connectAttr( uprDistance + 'Shape.distance' , invertNode +  '.input1X', force = True )
	mc.connectAttr( lwrDistance + 'Shape.distance' , invertNode +  '.input1Y', force = True )

	# connect invertNode >> color
	mc.connectAttr( invertNode +  '.outputX' , blendName +  '.color1R', force = True )
	mc.connectAttr( invertNode +  '.outputY' , blendName +  '.color1G', force = True )

	# please check
	# update function for fix scaleable controller 
	# create compensate knee/elbow 

	compenNode = mc.createNode('multiplyDivide' , name =  uprNam +'Compen' + '_mdv')

	# set to divie
	mc.setAttr('%s.operation' %compenNode , 2)
	# make value positive or negative following side
	mc.setAttr('%s.input1X' %compenNode, multiply * 1)
	# connection value
	mc.connectAttr( placementNam +  '.scaleX' , compenNode +  '.input2.input2X', force = True )
	mc.connectAttr( compenNode +  '.outputX' , invertNode +  '.input2X', force = True )
	mc.connectAttr( compenNode +  '.outputX' , invertNode +  '.input2Y', force = True )

	print ('Create compensate value for lock complete...')

	return blendName , invertNode


def doAddAttr ( povName ,  region ):
	'''
	add attribute to pov
	@return attr name
	'''

	if region:
		MidLockLogger.info(region)

		kind = ''
		if region == 'arm':
			kind = 'elbow'

		elif region == 'leg':
			kind = 'knee'

		else:
			# kind == None
			kind = region
			mc.warning('Unknow type of name. Maybe animal limb return original region name.')


	else :
		kind = region
		
	MidLockLogger.info('>>> This is a %s and POV is %s' %( kind, povName ))
	mc.addAttr( povName , longName = '%sLock' %kind, attributeType = 'double' , min = 0.0, max = 1.0, defaultValue = 0 ,keyable = True)
	return '%sLock' %kind




def connectIkJnt( stretchNode , upperIKJnt , lowerIKJnt , blendName , namLock , povName, alongAxis ):
	'''
	Connect node to ik joint
	'''

	MidLockLogger.info(blendName)
	MidLockLogger.info(upperIKJnt)
	MidLockLogger.info(stretchNode)
	MidLockLogger.info(lowerIKJnt)


	mc.connectAttr (	'%s.output2Dx'	%stretchNode	,  '%s.color2R' 	%blendName	,	force = True)
	mc.connectAttr (	'%s.output2Dy'	%stretchNode	,  '%s.color2G' 	%blendName	,	force = True)
	if alongAxis == 'y':
		mc.connectAttr (	'%s.outputR'	%blendName		,  '%s.translateY'  %upperIKJnt	,	force = True) 
		mc.connectAttr (	'%s.outputG'	%blendName		,  '%s.translateY'  %lowerIKJnt	,	force = True)
	elif alongAxis == 'x'   :
		mc.connectAttr (	'%s.outputR'	%blendName		,  '%s.translateX'  %upperIKJnt	,	force = True) 
		mc.connectAttr (	'%s.outputG'	%blendName		,  '%s.translateX'  %lowerIKJnt	,	force = True)
	elif alongAxis == 'z'   :
		mc.connectAttr (	'%s.outputR'	%blendName		,  '%s.translateZ'  %upperIKJnt	,	force = True) 
		mc.connectAttr (	'%s.outputG'	%blendName		,  '%s.translateZ'  %lowerIKJnt	,	force = True)
	# connect blend value to POV
	MidLockLogger.info('%s.%s'  %(povName,namLock))
	mc.connectAttr (	'%s.%s'  %(povName,namLock)	,	'%s.blender'	%blendName 	,	force = True)