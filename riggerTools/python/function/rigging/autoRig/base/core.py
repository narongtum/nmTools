# -*- coding: utf-8 -*-
"""
:Date: 2021-04-08
:About: Core function of autorig
:Version: 1.4
"""



'''
# direct call
from function.rigging.autoRig.base import core
reload(core)
'''


from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc
import maya.mel as mm
import os
import math
from maya import OpenMaya as om

from function.pipeline import logger 
reload(logger)

MAYA_VERSION = mc.about(v=True)

class CoreLogger(logger.MayaLogger):
	LOGGER_NAME = "Core"

'''
import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)
'''



from function.enviroment import enviromentPath as env
reload(env)

SHAPE_LIBRARY_PATH = env.SHAPE_LIBRARY_PATH

# SHAPE_LIBRARY_PATH = 'D:\\sysTools\\nmTools\\riggerTools\\python\\function\\rigging\\ctrlSizeLibrary\\'

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)

from function.rigging.util import misc
reload(misc)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)



'''
# setup
obj_target.addAttribute( attributeType = 'message' , longName = 'mulmatrix')
obj_target.addAttribute( attributeType = 'message' , longName = 'm_quatToEuler')
# qury
mc.listConnections( obj_target.name + '.' + 'mulmatrix' )[0]
mc.listConnections( obj_target.name + '.' + 'm_quatToEuler' )[0]

'''



'''
1. can create null grp with specific name
2. can create controller with specific name and type 
2.1 can assign side of controller
2.2 can scale vertex of controller
2.3 can add gimbal
2.4 add desire type of attr
3. specify color
4. can lock and hide desire attr
5. create zro grp
6. specify what attr connected to which attr
7. set rotation order
8. add attr
'''





# Import module
'''
ASCII ART
URL: 
http://patorjk.com/software/taag/#p=display&f=Big&t=class%20%20%20Null

rigDir = r'D:/python'

if not rigDir in sys.path:
	sys.path.append( rigDir )


for each in sys.path:
	print each




'''





# =============================
# Inheritence Example:
# ex 1
'''
To use:

reload(core)
rig_grp = core.Null()
still_grp = core.Null()
rig_grp.add(ln = 'size' , k = True , dv = 1)
rig_grp.attr('size') >> still_grp.attr( 'sx' )
'''



# ex 2
'''
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc as misc
reload(misc)

cube = core.Dag('cube')
cube.nmCreateController('cube_ctrlShape')
cube.addAttribute(ln = 'size' , k = True , dv = 1)
# using auto suffix
misc.autoSuffix( cube.name )


# ex 3 how to use property
shape = self.shape




# ex 4 
# Create COG controller
name = 'cog'
cog_ctrl = core.Dag(name + '_ctrl')
cog_ctrl.nmCreateController('cog_ctrlShape')

cogZro_grp = rigTools.zeroGroup( cog_ctrl )
cogZro_grp.rename( name + 'Ctrl' + '_zroGrp' )
cogGmbl_ctrl = core.pkCreateGimbal( cog_ctrl )
cog_ctrl.rotateOrder = 'xzy' 
cogGmbl_ctrl.rotateOrder = 'xzy'
# parent constraint
neckJnt_parCons = core.parentConstraint( neckGmbl_ctrl , neck_bJnt )




# ex 5
rotateShape


# ex 6 : create null grp
rollBackAnkleIkZro_grp = core.Null( ctrlName + 'Aim' + side + 'Zro_grp' )

# ex 7 : aim constraint
lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = False , aimVector = (0,1,0) ,upVector = (0,0,-1)  , worldUpObject = lowerUpObj_loc.name)

# ex 7 : auto suffix
child = core.Null('Aimasdasda')
child.suffix



# ex 9 : parent
upperLeg_bJnt.parent( priorJnt )

# ex 10: Create node
mul = core.MultiDoubleLinear('null1')

# ex 11: Add attribute collection

cube.addAttribute( at = 'enum', keyable = True , en = '###:', longName = 'Eye_preset'  )
cube.addAttribute( at = 'enum', keyable = True , en = 'Green:Blue:Red', longName = 'rotate_Order'  )
stick_ctrl.addAttribute( longName = 'handScale' , defaultValue = 1 , keyable = True )
dynSwitch_ctrl.addAttribute( at = 'long'  , min = 0  , max = 1, longName = 'dynamic_blend', keyable = True, defaultValue = 1   )
dynSwitch_ctrl.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'dynamic_blend', keyable = True, defaultValue = 1   )
stick_ctrl.addAttribute( longName = 'startFrame', defaultValue = 1 ,at = 'long'  , min = 0  , keyable = True )
stick_ctrl.addAttribute( longName = 'startFrame', defaultValue = 1 ,at = 'float'  , min = 0  , keyable = True )
stick_ctrl.addAttribute( dataType = 'string' , longName = 'region')
stick_ctrl.addAttribute( attributeType = 'bool' , longName = 'fkVis' , minValue = 0 , maxValue = 1 , defaultValue = 1 , keyable = True )

# ex 12 :Set color
# gmblCtrl.color = 'white'
# self.attr('rotateOrder')

# ex 13 :Create zro grp
# gmblCtrl.color = 'white'

# ex 14 :lock and hide attr
# stick_ctrl.lockHideAttrLst( 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy' , 'sz' , 'v' )



# ex 15 :set drawing override
self.attr( 'overrideEnabled' ).value = 1
self.attr( 'overrideDisplayType' ).value = 2


# ex 16 :set rotation order of specific controller
cube = core.Dag('cube1')
cube.nmCreateController('cube_ctrlShape')
cube.addRotEnum('zxy')



# ex 17 :create joint
a = core.Joint()
a.name = 'asda'


# ex 18 : set spcial volume
a = core.Joint()
a.name = 'asda'


# ex 19 : create IK
twistAim_ikh = core.DoIk( startJoint = upperFollow01_jnt , endEffector = upperFollow02_jnt , solverType = 'ikRPsolver' )



# ex 20 :  createJntShape

some2 = core.Joint()
some2.name = 'someName_jnt'
some2.createJntShape(localScale = 4)


# ex 21 :  ParentConstraint
neckJnt_parCons = core.ParentConstraint( neckGmbl_ctrl , neck_bJnt ,mo=False, )






# ex 22 :  Using Store data to node
from function.rigging.autoRig.base import core
reload(core)


node = core.MetaClass(name='fread')
node.addAttribute( at = 'enum', keyable = True , en = "++++:", longName = 'Eye_preset'  )
node.addAttribute( at = 'long'  , min = 0  , max = 1, longName = 'dynamic_blend', keyable = True, defaultValue = 1   )
node.addAttribute( at = 'float'  , min = 0  , max = 10, longName = 'dynamic_float', keyable = True, defaultValue = 1   )
node.addAttribute( dataType = 'string' , longName = 'This_si_string_test')
node.addAttribute( attributeType = 'message' , longName = 'mulmatrix')
node.attr('This_si_string_test').value = 'noman'
node.addAttribute( dataType = 'string' , longName = 'Dict_test')

import json
noman = {'jsonFloat':1.05, 'Int':3, 'JsonString':'string says hello'}
# dump from dict to json
json_noman = json.dumps(noman)
# store value
node.attr('Dict_test').value = json_noman 
type(json_noman)



# Add a double3 attribute named Eye_preset with children x, y and z
node = core.MetaClass(name='fread')
node.addAttribute( at = 'double3', keyable = True, longName = 'Eye_preset'  )
node.addAttribute( longName='x',at = 'double', parent = 'Eye_preset'  )
node.addAttribute( longName='y',at = 'double', parent = 'Eye_preset'  )
node.addAttribute( longName='z',at = 'double', parent = 'Eye_preset'  )



# Example 23 :  Using lock attr
parentConMatrix_meta = core.MetaGeneric('matCon')
parentConMatrix_meta.attr('Base_Name').value = 'wp_ssr_miko'
parentConMatrix_meta.setLocked('Base_Name')

# Example 24: Link message


# Example 25: SetAttribute
stick_ctrl.setAttribute('location'  , region , type = 'string')

'''










def makeHeader(text):
	print ('\n')
	print ('# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n')
	print ('\t\t\t\t\t%s\n' %text)
	print ('# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n')




# property is looklike call function in side same class


# color dictionary
colorDict = {   'yellow'    : 17 ,          'red'           : 13 ,
				'softBlue'  : 18 ,          'blue'          : 6 ,
				'white'     : 16 ,          'brown'         : 11 ,
				'black'     : 1 ,           'gray'          : 2 ,
				'softGray'  : 3 ,           'darkRed'       : 4 ,
				'darkBlue'  : 5 ,           'darkGreen'     : 7 ,
				'green'     : 14 ,          'none'          : 0     }





#   _  _     ______                _   _             
#  _| || |_  |  ____|              | | (_)            
# |_  __  _| | |__ _   _ _ __   ___| |_ _  ___  _ __  
#  _| || |_  |  __| | | | '_ \ / __| __| |/ _ \| '_ \ 
# |_  __  _| | |  | |_| | | | | (__| |_| | (_) | | | |
#   |_||_|   |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|


#... This is duplicate function with adjustController not sure which one is latest
def createGimbal( obj = '' ):

	ctrl = Dag( obj )
	ctrlShape = Dag( ctrl.shape )
	# Duplicate parent shape
	tmpCtrl = mc.duplicate( ctrl , rr=True )[0]
	ctrlShape.addAttribute( ln = 'gimbal' , min = 0 , max = 1 , k = True )

	# Create gimbal object
	gmblCtrl = Null()
	parentShape( tmpCtrl , gmblCtrl )
	
	
	#print gmblCtrlShape

	#gmblCtrlShape.name = '%sShape' % gmblCtrl.name
	
	gmblCtrl.snap( ctrl )
	gmblCtrl.parent( ctrl )

	# reduce size to 75 percent
	gmblCtrl.editCtrlShape(axis =   0.75 )
	#... split name with underscore
	spName = ctrl.splitName()


	# Check naming condition
	if len(spName) == 2:
		gmblCtrl.rename(spName[0] + '_gmb' + 'Ctrl')
	elif len(spName) == 3:
		gmblCtrl.rename( spName[0] + '_' + spName[1] +'_gmb' + 'Ctrl' )
	elif len(spName) == 4:
		gmblCtrl.rename( spName[0] + '_' + spName[1] + '_' + spName[2] +'_gmb' + 'Ctrl' )
	elif len(spName) == 5:
		gmblCtrl.rename( spName[0] + '_' + spName[1] + '_' + spName[2] + spName[3] +'_gmb' + 'Ctrl' )
	else:
		mc.warning('\nelement is too much')
		gmblCtrl.rename( ctrl.name +'_gmbCtrl' )




	# gmblCtrl.rename(spName[0] + '_gmb' + 'Ctrl')

	# Not quite understand why recreate obj of gmblCtrl 
	gmblCtrlShape = Dag( gmblCtrl.shape )

	#print ctrlShape.attr( 'gimbal' )
	#print gmblCtrl.shape
	#print gmblCtrl.shape.attr('visibility')
	ctrl.hideArnoldNode()
	gmblCtrl.hideArnoldNode()

	
	ctrlShape.attr( 'gimbal' ) >> gmblCtrlShape.attr( 'v' ) 

	# hide attr
	gmblCtrl.attr( 'v' ).lockHide()
	gmblCtrl.color = 'white'
	'''
	attrs = ( 'sx' , 'sy' , 'sz' , 'v' )
	for attr in attrs :
		gmblCtrl.attr( attr ).lockHide()
	'''
	return gmblCtrl

# this function is outdate
def nmCreateGimbal( obj = '' ):

	ctrlName = Dag( obj )

	ctrlShape = Dag( ctrlName.shape )

	if mc.nodeType(ctrlShape) == 'nurbsCurve':

		print ('This is might be Controller')
	
		shapes = wcd.getShape( ctrlShape )

		# change ctrl data 75 percent smaller
		data = wcd.modifiyCtrlShape( shapes , axis = [0.75, 0.75, 0.75] )

		#print data[0]

		# create new controller
		gmblCtrl = Null() # for test can delete

		# use [0] because value is list
		gmblCtrl = mc.curve( ctrlName, p = data[0]["points"], k = data[0]["knots"], d = data[0]["degree"], per = bool(data[0]["form"]) )

		# case if 
		#gmblCtrl = mc.curve(ctrlName, p = data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]))

		# add gimbal attr
		#mc.addAttr( ctrlName , ln = 'gimbal' , min = 0 , max = 1 , dv = 1 , k = True )
		mc.addAttr( ctrlShape , ln = 'gimbal' , min = 0 , max = 1 , dv = 1 , k = True )

		gmblShape = mc.listRelatives( gmblCtrl , s = True )[ 0 ]

		# set white color
		mc.setAttr( '%s.overrideEnabled' % gmblShape , 1 )
		mc.setAttr( '%s.overrideColor' % gmblShape , 16 )

		# snap
		misc.snapParentCon( ctrlName, gmblCtrl )
		mc.parent( gmblCtrl , ctrlName )

		# connect attr
		#print  ( '%s.gimbal' % ctrlName , '%s.v' %gmblCtrl )
		
		# mc.connectAttr( '%s.gmbl' % ctrlName , '%s.v' %gmblShape )
		# mc.setAttr( '%s.gmbl' % ctrlName , 0 )
		mc.connectAttr( '%s.gimbal' % ctrlShape , '%s.v' %gmblShape )
		mc.setAttr( '%s.gimbal' % ctrlShape , 0 )

		#split name
		spName = misc.splitName( ctrlName.name )

		# rename gmbl ctrl
		gmblName = mc.rename( gmblCtrl, spName[0] + 'Gmbl' + '_ctrl' )

		mc.select( deselect = True )

		ctrlName.hideArnoldNode()

		return gmblName

	else:
		mc.warning( "This is not Controller" )




# Cluster Node
def cluster( *args  , **kwargs ):
	# [0] is cluster shapeName
	# [1] is cluster handle
	return Dag(  mc.cluster(*args  , **kwargs)[1] ) 




#----------------------------------------------some vector caculation------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

# __  __          _______  __   __
#|  \/  |    /\  |__   __||  | |  |
#| \  / |   /  \    | |   |  |_|  |
#| |\/| |  / /\ \   | |   |   _   |
#| |  | | / ____ \  | |   |  | |  |
#|_|  |_|/_/    \_\ |_|   |__| |__|

def vPlus(vec1, vec2, operator):
	'''operator: +, -'''
	vec = []      
	for i in range(len(vec1)):
		if operator == '+':
			vec.append(vec1[i]+vec2[i])
		elif operator == '-':
			vec.append(vec1[i]-vec2[i])
	return vec

def vCross(vec1, vec2):
	vec = [vec1[1]*vec2[2] - vec1[2]*vec2[1],
		   vec1[2]*vec2[0] - vec1[0]*vec2[2],
		   vec1[0]*vec2[1] - vec1[1]*vec2[0]]
	return vec

def vDot(vec1, vec2):
	return sum([vec1[i]*vec2[i] for i in range(len(vec1))])

def vLength(vec1):
	return math.sqrt(vDot(vec1, vec1))

def vMultiply(vec1, m):
	vec = []
	for i in range(len(vec1)):
		vec.append(vec1[i] * m)
	return vec

def vNormal(vec1):
	vec1L = vLength(vec1)
	nVec1 = vMultiply(vec1, 1.0/vec1L)
	return nVec1

def vSum(vec1):
	return sum([vec1[i] for i in range(len(vec1))])

def vSquare(vec1):
	vec = []
	for i in range(len(vec1)):
		vec.append(vec1[i] * vec1[i])
	return vec

def vectorToAngle(aimVec, upVec=None, sideVec=None, aimAxis="x", upAxis=None, sideAxis=None):
	'''
	convert 2 vector to a rotation value, the first vector is the aim vector, the second vector is the up vector
	input:
		aimVec(double3): the vector will absolutely matching one of the joint's defined axis
		upVec(double3): if using upVec, then don't use sideVec
		sideVec(double3): if using sideVec, then don't use upVec
		aimAxis(string): valid value: x, y, z
		upAxis(string): valid value: x, y, z
		sideAxis(string): valid value: x, y, z
	'''
	axisDic = {"x": 0, "y": 1, "z": 2}

	#if both side vector and up vector are defined, then side vector will be None 
	if upVec and sideVec:
		sideVec = None
	elif not upVec and not sideVec:
		return False

	if upAxis and sideAxis:
		sideAxis = None
	elif not upAxis and not sideAxis:
		return False

	if not sideAxis:
		sideAxis = axisDic.keys()
		sideAxis.remove(aimAxis)
		sideAxis.remove(upAxis)
		sideAxis = sideAxis[0]
	if not upAxis:
		upAxis = axisDic.keys()
		upAxis.remove(aimAxis)
		upAxis.remove(sideAxis)
		upAxis = upAxis[0]

	if not sideVec:
		sideVec = vCross(aimVec, upVec)
		upVec = vCross(aimVec, sideVec)
	if not upVec:
		upVec = vCross(aimVec, sideVec)
		sideVec = vCross(aimVec, upVec)

	#using a list to represent a 4 * 4 matrix
	M16 = [0, 0, 0, 1, #axisX
		   0, 0, 0, 1, #axisY
		   0, 0, 0, 1, #axisZ
		   0, 0, 0, 1] #position

	#assign vector
	for i in range(3):
		M16[axisDic[aimAxis]*4+i] = aimVec[i]
		M16[axisDic[upAxis]*4+i] = upVec[i]
		M16[axisDic[sideAxis]*4+i] = sideVec[i]

	#convert matrix format    
	m = om.MMatrix(M16)              
	mTransformMtx = om.MTransformationMatrix(m)

	#decompose matrix to get a rotate value
	eulerRot = mTransformMtx.rotation().reorder(om.MEulerRotation.kXYZ)
	angle = [math.degrees(angle) for angle in (eulerRot.x, eulerRot.y, eulerRot.z)]

	return angle

#------------------------
def cleanAttrAnimationCurve(attribute, tols):
	#tols means tolerance
	values = cmds.keyframe(attribute, q = True, vc = True)
	times = cmds.keyframe(attribute, q = True, tc = True)
	inTnagent = cmds.keyTangent(attribute, q=True, inAngle=True)
	outTnagent = cmds.keyTangent(attribute, q=True, outAngle=True)
	
	#get a secondary value
	secValues = []  
	for i in range(len(values)-2):
		secValue = cmds.getAttr(attribute, t = times[i+1]+0.01)
		secValues.append(secValue)
	
	#a useless key is a key which after being deleted, does no change to the original animation curve
	for i in range(len(values)-2):
		cmds.cutKey(attribute, time=(times[i+1],times[i+1]))
		newValue = cmds.getAttr(attribute, t = times[i+1]+0.01)
		if abs(newValue - secValues[i])> tols:
			cmds.setKeyframe(attribute, t = times[i+1], v = values[i+1])
			cmds.keyTangent(attribute, edit=True, time=(times[i+1],times[i+1]), absolute=True, outAngle=outTnagent[i+1], ia=inTnagent[i+1])
			
def cleanObjAnimationCurve(tols=0.00001):
	#clean object's animation curve

	objects = cmds.ls(sl = True)
	if len(objects) > 0:
		for obj in objects:
			allAttrs = cmds.listAttr(obj, k=True)
		
			keyedAttrs = []
			for objAttr in allAttrs:
				keyNO = cmds.keyframe("{0}.{1}".format(obj, objAttr), q=True, kc=True)
				if keyNO > 0:
					keyedAttrs.append(objAttr)
					
			for keyedAttr in keyedAttrs:
				cleanAttrAnimationCurve("{0}.{1}".format(obj, keyedAttr), tols)






									
 #   ___   _   _   _ __  __   __   ___ 
 #  / __| | | | | | '__| \ \ / /  / _ \
 # | (__  | |_| | | |     \ V /  |  __/
 #  \___|  \__,_| |_|      \_/    \___|
									 

def curve( *args , **kwargs ):
	return Dag(  mc.curve(*args , **kwargs) )

def duplicateCurve( *args , **kwargs ):
	'''
	 takes a curve on a surface and and returns the 3D curve. 
	 The curve on a surface could be isoparam component, 
	 trimmed edge or curve on surface object.
	'''
	tmp = mc.duplicateCurve( *args , **kwargs )
	crv = Dag(tmp[0]) # make it object
	#cfs = Node( tmp[1] ) # return shapaName
	return crv


def nurbPlane( *args , **kwargs ):
	return Dag( mc.nurbsPlane( *args , **kwargs )[0] )




def duplicate( *args , **kwargs ):
	tmp = mc.duplicate( *args , **kwargs )
	crv = Dag(tmp[0]) 
	return crv













# Clear selection
def clearSel():
	mc.select( deselect = True )



#### This is base class ####

 #       _                  _                    
 #      | |                | |                   
 #   ___| | __ _ ___ ___   | |__   __ _ ___  ___ 
 #  / __| |/ _` / __/ __|  | '_ \ / _` / __|/ _ \
 # | (__| | (_| \__ \__ \  | |_) | (_| \__ \  __/
 #  \___|_|\__,_|___/___/  |_.__/ \__,_|___/\___|
											  
											  

class Node( object ) :
	'''
	Template Base class for maya 
	'''
	# nodeId = 0
	def __init__( self , name ) :
		# self.nodeId = Node.nodeId
		# self.nodeId = +=1
		self.__name = str( name )
		print ('Creating Object name : ' + self.__name)
		# Clear selection
		mc.select( cl = True )

	# Return string name
	def __str__( self ):
		return str( self.name )

	# Show full internal module path
	def __repr__( self ):
		return str( self.name )

	'''
	def __del__( self ):
					self.deleteName()
	'''

	def deleteName( self , **kwargs ):
		''' maya delete node and delete constrution history '''
		print ('Deleting object {0} ...'.format(self.name))
		mc.delete( self.name , **kwargs)



	# property ask Name object
	# =============
	def getName( self ) :
		return self.__name
	
	def rename( self , newName ) :
		print ('Reseting name to %s' %newName)
		self.__name = str( mc.rename( self.__name , newName ) )

	name = property( getName , rename , None , None )


	# property ask type object
	# =============
	def getType( self ):
		return mc.nodeType( self.name )
	type = property( getType , None , None , None )


	# property ask this object exists
	# =============
	def getExists( self ):
		return mc.objExists(self)
	exists = property(getExists , None , None , None )










	def attr(self, attrName = ''):
		'''
		sent it to class Attribute
		'''

		return Attribute('%s.%s' %( self,attrName)  )


	def addAttribute( self , *args , **kwargs ):
		'''
		add attr to Node
		'''
		mc.addAttr(self , *args , **kwargs )
		CoreLogger.info("Attribute has been create.")


	def setAttribute( self ,attrName, *args , **kwargs ):
		'''
		i dunno how to add string to attr so i just create this
		'''
		mc.setAttr( self.name + '.' + attrName , *args , **kwargs )



	def setTranslation( self, value ):
		self._doTransform( mc.move, value[0] , value[1] , value[2] )

	def setRotation( self, x = None, y = None, z = None ):
		self._doTransform( mc.rotate, x, y, z )

	def setScale( self, x = None, y = None, z = None ):
		self._doTransform(mc.scale, x, y, z )

	def _doTransform( self, func, x, y, z, ):
		for name in ('x','y','z'):
			val = locals()[name]
			if val is not None:
				# what is this 
				opts = {name:True, 'objectSpace':True, 'absolute':True}
				func(val, self.name, **opts)


	def matchTransform( self , destination ):
		mc.matchTransform( self.name , destination )

	def matchPosition( self , destination ):
		mc.matchTransform( self.name  , destination , pivots = True , position = True , rotation = False , scale = False   )

	def matchRotation( self , destination ):
		mc.matchTransform( self.name  , destination , pivots = True , position = False , rotation = True , scale = False   )

	def matchScale( self , destination ):
		mc.matchTransform( self.name  , destination , pivots = True , position = False , rotation = False , scale = True   )

	def matchAll( self , destination ):
		mc.matchTransform( self.name  , destination , pivots = True , position = True , rotation = True , scale = True   )
	
	def splitName( self ): # split name with under score
		name = self.name

		if '_' in name:
			newName = []
			newName = name.split('_')
			return newName
		else:
			name

	def makeRawName( self ):
		''' for Test to make return raw name and extract side Example. spine01  '''

		rawName = self.name.split('_')[0]
		# if 'RGT' in rawName or 'LFT' in rawName or 'MID' in rawName: # if end with ['LFT','RGT','MID']

		if rawName.endswith('LFT') or rawName.endswith('RGT') or rawName.endswith('MID'):
			rawName = rawName[:-3]
			CoreLogger.info('slice text')
			return rawName
		else:
			print ('Can not find any of prosition.')
			return rawName


		

		


	# property add suffix exists
	# =============
	def _identifies( self ):
		''' ask what is node type '''
		isNode = mc.nodeType( self.name )

		if isNode == 'transform':
			# if transform node chek shapeNode 
			shapeName = self.shape
			print (self.name)
			isNode = mc.nodeType( shapeName )

		return isNode


	def _findExtension( self ):
		''' adding maya lastname string '''

		nodeDict = mnd.NODE_dict
		nodeType = str( self._identifies() )

		print ('nodeType is %s' %nodeType)
		# print type(nodeType).__name__

		node_exp = []
		if nodeType == 'None':
			

			for each in nodeDict:

				if each['longName'] == 'group':
					node_exp = each['shortName']
					break
				else:
					node_exp = 'unknown'
				continue


		elif nodeType:
		# for naming null group route
			for each in nodeDict:
				# for rest of node naming route
				if each['longName'] == nodeType:
					node_exp = each['shortName']

					# if found break the loop
					break
				else:
					node_exp = 'unknown'
				continue
	 

	
		# print 'This is shortName	:' +  node_exp

		return node_exp


	def autoSuffix( self ):
		CoreLogger.info('Inserting lastname...')

		# convert unicode to ascii (forgot why convert it so I turn it back)
		# each = self.name.encode('ascii')
		each = self.name

		lastname = self._findExtension()
		print ('this is suffix name: %s' %lastname)
		

		# if object already last name
		if each.endswith( lastname ):
			print ('This is already last name it will skip.\n')
			
		else:
			# newNam = mc.rename( each  , each +'_'+ lastname )
			self.name = each +'_'+ lastname
			print ('%s object has been rename' %each)


	suffix = property( autoSuffix , None , None , None )




	#... Set attr Lock 
	#... Redundance with lockHideAttrLst in Dag class
	def setLocked(self,attr):
		mc.setAttr(self.name + '.' + attr, lock = True ,keyable = True)




	# lock = property( setLocked , None , None , None)

	# END of class Node












#       _                   __  __      _          _   _           _      
#      | |                 |  \/  |    | |        | \ | |         | |     
#   ___| | __ _ ___ ___    | \  / | ___| |_ __ _  |  \| | ___   __| | ___ 
#  / __| |/ _` / __/ __|   | |\/| |/ _ \ __/ _` | | . ` |/ _ \ / _` |/ _ \
# | (__| | (_| \__ \__ \   | |  | |  __/ || (_| | | |\  | (_) | (_| |  __/
#  \___|_|\__,_|___/___/   |_|  |_|\___|\__\__,_| |_| \_|\___/ \__,_|\___|
# 
#                                                                                                                                      # 



class MetaRoot ( Node ):
	'''  create clamp object  '''
	def __init__( self, name ):
		Node.__init__( self , mc.createNode('network' , name = name) )
		self.addAttribute( longName = 'Version', at = 'float'  , min = 0  , keyable = True )
		self.addAttribute( dataType = 'string' , longName = 'Project')
		self.addAttribute( dataType = 'string' , longName = 'Meta_Type') #... Root
		self.addAttribute( dataType = 'string' , longName = 'Asset_Type') #... Character or Prop
		self.addAttribute( dataType = 'string' , longName = 'Base_Dir') #... Folder path
		self.addAttribute( dataType = 'string' , longName = 'Source_File_Path') #... Folder path to file specific
		self.addAttribute( dataType = 'string' , longName = 'Root_Joint')
		self.addAttribute( attributeType = 'message' , longName = 'rig_grp')
		self.addAttribute( attributeType = 'message' , longName = 'Meta_Children')







class MetaGeneric( Node ):
	def __init__( self, name ):
		Node.__init__(self, mc.createNode('network', name = name))
		self.suffix
		#... Header
		self.addAttribute( attributeType = 'message' , longName = 'Rig_Prior')
		self.addAttribute( dataType = 'string' , longName = 'Base_Name')
		self.addAttribute( dataType = 'string' , longName = 'Side')


		








 #       _                  _    _ _   _ _                    _      
 #      | |                | |  | | | (_) |                  | |     
 #   ___| | __ _ ___ ___   | |  | | |_ _| |   _ __   ___   __| | ___ 
 #  / __| |/ _` / __/ __|  | |  | | __| | |  | '_ \ / _ \ / _` |/ _ \
 # | (__| | (_| \__ \__ \  | |__| | |_| | |  | | | | (_) | (_| |  __/
 #  \___|_|\__,_|___/___/   \____/ \__|_|_|  |_| |_|\___/ \__,_|\___|







class CMuscleSmartConstraint ( Node ):
	'''  create plusMinusAverage object  '''
	def __init__( self , name, dv = 1):
		
		Node.__init__( self , mc.createNode('cMuscleSmartConstraint', name = name) )
		self.addAttribute( ln = 'multiply' , k = True , defaultValue = dv )
		self.suffix

class Clamp ( Node ):
	'''  create clamp object  '''
	def __init__( self, name ):
		Node.__init__( self , mc.createNode('clamp' , name = name) )
		self.suffix


class Reverse ( Node ):
	''' create reverse object '''
	def __init__( self ):
		Node.__init__( self ,  mc.createNode('reverse') )

# lazy to fix the rest so create new one
class ReverseNam ( Node ):
	''' create reverse object '''
	def __init__( self , name):
		Node.__init__( self ,  mc.createNode('reverse', name = name) )


'''
class MultiplyDivine ( Node ):
	"""docstring for MultiplyDivine """
	def __init__(self, arg):
		super(MultiplyDivine , self).__init__()
		self.arg = arg
'''     


class MultiplyDivine ( Node ):
	'''  create MultiplyDivine object  '''
	def __init__( self , name ):
		Node.__init__( self , mc.createNode('multiplyDivide', name = name) )
		


class PlusMinusAverage ( Node ):
	'''  create plusMinusAverage object  '''
	def __init__( self , name):
		Node.__init__( self , mc.createNode('plusMinusAverage', name = name) )
		


class BlendColors ( Node ):
	'''  create BlendColors object  '''
	def __init__( self, name ):
		Node.__init__( self , mc.createNode('blendColors', name = name)  )
		



class MultiplyDivineWithVal ( Node ):
	'''  create MultiplyDivine object  with regsinate operator '''
	def __init__( self, name, operator):
		Node.__init__( self , mc.createNode('multiplyDivide', name = name) )
		self.suffix
		self.attr('operation').value = operator
		print ('set value to %d' %operator)


	
class AddDoubleLinear( Node ):
	'''  create AddDoubleLinear object  '''
	def __init__( self, name, input2=0):
		Node.__init__( self , mc.createNode( 'addDoubleLinear' , name = name) )
		self.attr('input2').value = input2
		# self.suffix


class MultiDoubleLinear( Node ):
	'''  create multDoubleLinear object  '''
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'multDoubleLinear' , name = name) )
		self.suffix


class MDLWithMul( Node ):
	'''  create multDoubleLinear object with multiple val'''
	def __init__( self, name , dv = 1 ):
		Node.__init__( self , mc.createNode( 'multDoubleLinear' , name = name) )
		# Create attr name "multiply" and connect it to input2 and we adjust this value from "multipy" for convenience reason
		self.addAttribute( ln = 'multiply' , k = True , defaultValue = dv )
		self.attr('multiply') >> self.attr('input2')
		# self.attr('input1').value = 1
		self.suffix


class Condition( Node ):
	'''  create DisctanceBetween object  '''
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'condition' , name = name) ) 
		# self.suffix


class Loft( Node ):
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'loft' , name = name) )
		# self.suffix


class PointOnCurveInfo( Node ):
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'pointOnCurveInfo' , name = name) )
		self.suffix 


class CurveInfo( Node ):
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'curveInfo' , name = name) )
		self.suffix 






 #      _                   __  __       _        _      
 #      | |                 |  \/  |     | |      (_)     
 #   ___| | __ _ ___ ___    | \  / | __ _| |_ _ __ ___  __
 #  / __| |/ _` / __/ __|   | |\/| |/ _` | __| '__| \ \/ /
 # | (__| | (_| \__ \__ \   | |  | | (_| | |_| |  | |>  < 
 #  \___|_|\__,_|___/___/   |_|  |_|\__,_|\__|_|  |_/_/\_\
														


# Matrix Node

class DecomposeMatrix( Node ):
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'decomposeMatrix' , name = name) )
		self.suffix

class MultMatrix( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('multMatrix', name = name))
		self.suffix

class ComposeMatrix( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('composeMatrix', name = name))	
		self.autoSuffix()

class VectorProduct( Node ):
	def __init__(self,name,operator = 0):
		Node.__init__(self, mc.createNode('vectorProduct', name = name))
		self.autoSuffix()
		self.attr('operation').value = operator

class FourByFourMatrix( Node ):
	def __init__(self,name):
		Node.__init__(self, mc.createNode('fourByFourMatrix', name = name))
		self.autoSuffix()

class AimMatrix( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('aimMatrix', name = name))
		self.autoSuffix()


# Add a weighted list of matrices together. 
# https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2022/ENU/Maya-Basics/files/GUID-B290C3E6-95BC-4299-BC0D-169EADDE6319-htm.html
class WtAddMatrix( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('wtAddMatrix', name = name))
		self.autoSuffix()

class EulerToQuat( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('eulerToQuat', name = name))
		self.autoSuffix()

class QuatInvert( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('quatInvert', name = name))
		self.autoSuffix()

class QuatProd( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('quatProd', name = name))
		self.autoSuffix()
	
class QuatToEuler( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('quatToEuler', name = name))
		self.autoSuffix()

class BlendMatrix( Node ):
	def __init__(self, name):
		Node.__init__(self, mc.createNode('blendMatrix', name = name))
		self.autoSuffix()

class PointMatrixMult(Node):
	def __init__(self, name, enable = True, inPoint = (0,0,0)):
		Node.__init__(self, mc.createNode('pointMatrixMult', name = name))
		self.attr('vectorMultiply').value = enable
		self.attr('inPointX').value = inPoint[0]
		self.attr('inPointY').value = inPoint[1]
		self.attr('inPointZ').value = inPoint[2]



'''
	mc.createNode( 'quatInvert', n = quaInv )
	mc.createNode( 'quatProd', n = quaPro )
	mc.createNode( 'quatToEuler', n = quaEul )
'''













# It will cause maya crash when instanceing i dunno why
# Because of you insert self as args so it init arg and recusive 

class SkinCluster( Node ):
	""" skinCluster Node Object """
	def __init__( self , *args , **kwargs):
		Node.__init__(self , mc.skinCluster( *args , **kwargs )[0] )





class DistanceBetween( Node ):
	'''  create DisctanceBetween   '''
	def __init__( self , *args , **kwargs):
		Node.__init__( self , mc.createNode( 'distanceBetween' , *args , **kwargs) )




class DistanceDimension( Node ):
	# Older but still use
	def __init__( self , loc1 , loc2 , distanceNam ,*args , **kwargs):
		Node.__init__(self , mc.distanceDimension( *args , **kwargs ) )

		# if mc.objExists('locator1'):
		# 	mc.rename('locator1','something1')
		# if mc.objExists('locator2'):
		# 	mc.rename('locator2','something2')			

		if loc1:
			mc.rename( 'locator1' , loc1 ) 
			mc.rename( 'locator2' , loc2 ) 
			mc.rename( 'distanceDimension1' , distanceNam )
		else:
			pass





class DistanceNode( Node ):
	# Newer
	# Create distance object for connect value manual
	def __init__( self , *args , **kwargs):
		Node.__init__(self , mc.createNode('distanceDimShape', *args , **kwargs) ) 





class MotionPath( Node ):
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'motionPath' , name = name) )
		self.suffix 



class MultiplyDivide( Node ):
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'multiplyDivide' , name = name) )
		self.suffix 



''' Fail
class MotionPath( _motionPath ):
	def __init__( self , name ):
		_motionPath.__init__( self , name )
		motion = self._motionPath(name)
		tX_adl = self.AddDoubleLinear(name+'tX_adl')
'''





 #   _____ _                      _____                             _____                     
 #  / ____| |                    |  __ \                           / ____|                    
 # | |    | | __ _ ___ ___       | |__) |___ _ __ ___   __ _ _ __ | |    _   _ _ ____   _____ 
 # | |    | |/ _` / __/ __|      |  _  // _ \ '_ ` _ \ / _` | '_ \| |   | | | | '__\ \ / / _ \
 # | |____| | (_| \__ \__ \      | | \ \  __/ | | | | | (_| | |_) | |___| |_| | |   \ V /  __/
 #  \_____|_|\__,_|___/___/      |_|  \_\___|_| |_| |_|\__,_| .__/ \_____\__,_|_|    \_/ \___|
 #                                                          | |                               
 #                                                          |_|                                                       |_|                               


# remap plus multi-double linear new method for drive blendshape



class RemapCurve(Node):
	def __init__(self, name, positive = True, defaultValue = (0,1,0,1),value_Position = 1,value_FloatValue = 1):
		Node.__init__(self, mc.createNode('remapValue', name = name))
		self.attr('inputMin').value = defaultValue[0]
		self.attr('inputMax').value = defaultValue[1]
		self.attr('outputMin').value = defaultValue[2]
		self.attr('outputMax').value = defaultValue[3]

		self.attr('value[1].value_Position').value = value_Position
		self.attr('value[1].value_FloatValue').value = value_FloatValue

		self.attr('value[2].value_FloatValue').value = 1
		self.attr('value[2].value_Position').value = 1

		self.suffix

		if positive:
			CoreLogger.info('The value is positive it end here')


		else:
			CoreLogger.info('The value is negative create MultiDoubleLinear')
			mdl_node = MultiDoubleLinear(name)
			mdl_node.suffix
			mdl_node.attr('input2').value = -1
			mdl_node.attr('output') >> self.attr('inputValue')

















 #       _                                 _            _____                     
 #      | |                    /\         (_)          / ____|                    
 #   ___| | __ _ ___ ___      /  \   _ __  _ _ __ ___ | |    _   _ _ ____   _____ 
 #  / __| |/ _` / __/ __|    / /\ \ | '_ \| | '_ ` _ \| |   | | | | '__\ \ / / _ \
 # | (__| | (_| \__ \__ \   / ____ \| | | | | | | | | | |___| |_| | |   \ V /  __/
 #  \___|_|\__,_|___/___/  /_/    \_\_| |_|_|_| |_| |_|\_____\__,_|_|    \_/ \___|


# animcurve class
class AnimCurveUU( Node ):
	'''  create animcurve for connect value to object  '''
	def __init__( self, name ):
		Node.__init__( self , mc.createNode( 'animCurveUU' , name = name) )

		# disable because of purpose of each value has require dif of set key frame
		# mc.setKeyframe( self , float = 0.0 ,value = 0.0 )
		# mc.setKeyframe( self , float = 1.0 ,value = 1.0 )
		# mc.keyTangent( self , index = (0,0), itt = 'linear' , ott = 'linear' )
		# mc.keyTangent( self , index = (1,1), itt = 'linear' , ott = 'linear' )

		print ('Change pre infinity.')
		self.attr('preInfinity').value = 1
		self.attr('postInfinity').value = 1

		self.suffix
		print ('%s adding suffix. ' %self.name)

	def setKeyValue( self, time = 1.0 , value = 1.0  ):
		mc.setKeyframe( self , float = time ,value = value )
		print ('Change time and frame to %0.2f and %0.2f.' %(time,value))

	def keyTangent( self , indx , inTan = 'linear' , outTan = 'linear'):
		mc.keyTangent( self , index = indx, itt = inTan , ott = outTan )
		print ('Change type to %s ...' %inTan)


class AnimCurvePos( AnimCurveUU ):
	'''
	# find the way to make an arg insted create 2 class
	animCurve for Positive value
	'''
	def __init__( self , name ):
		AnimCurveUU.__init__( self , name )
		mc.setKeyframe( self , float = 0.0 ,value = 0.0 )
		mc.setKeyframe( self , float = 1.0 ,value = 1.0 )
		mc.keyTangent( self , index = (0,0), itt = 'linear' , ott = 'linear' )
		mc.keyTangent( self , index = (1,1), itt = 'linear' , ott = 'linear' )
		print ('%s Initiaion complete. ' %self.name )


class AnimCurveNeg( AnimCurveUU ):
	'''
	animCurve for Negative value
	'''
	def __init__( self , name):
		AnimCurveUU.__init__( self , name)
		mc.setKeyframe( self , float = -1.0 ,value = 1.0 )
		mc.setKeyframe( self , float = 0.0 ,value = 0.0 )
		mc.keyTangent( self , index = (0,0), itt = 'linear' , ott = 'linear' )
		mc.keyTangent( self , index = (1,1), itt = 'linear' , ott = 'linear' )
		print ('%s Initiaion complete. ' %self.name)

class AnimCurveSomeThing( AnimCurveUU ):
	'''
	animCurve for Negative value Still Fail try it later
	'''
	def __init__( self  ,time , value , indx ):
		AnimCurveUU.__init__( self ,time , value , indx )
		self.time = time
		self.value = value
		self.indx = indx
		mc.setKeyframe( self , float = time[0] ,value = 1.0 )
		mc.setKeyframe( self , float = time[1] ,value = 0.0 )
		mc.keyTangent( self , index = indx[0], itt = 'linear' , ott = 'linear' )
		mc.keyTangent( self , index = indx[1], itt = 'linear' , ott = 'linear' )


 #      _                           _   _        _ _                    
 #      | |                     /\  | | | |      (_) |                   
 #   ___| | __ _ ___ ___       /  \ | |_| |_ _ __ _| |__  _   _ _ __ ___ 
 #  / __| |/ _` / __/ __|     / /\ \| __| __| '__| | '_ \| | | | '__/ _ \
 # | (__| | (_| \__ \__ \    / ____ \ |_| |_| |  | | |_) | |_| | | |  __/
 #  \___|_|\__,_|___/___/   /_/    \_\__|\__|_|  |_|_.__/ \__,_|_|  \___|




class Attribute( object ) :
	''' 
	Template maya attr for class Attributes 
	'''

	def __init__( self , attrName = '' ) :
		self.name = str( attrName )

	
	def __str__( self ) :
		return str( self.name )
	
	def __repr__( self ) :
		return str( self.name )
	
	def __floordiv__( self , attr = '' ) :
		mc.disconnectAttr( self , attr )
	
	def __rshift__( self , target = '' ) :

		'''
		connect value from attr in class Node
		ex:
		ctrlShape.attr( 'gimbalControl' ) >> gmblCtrlShape.attr( 'v' )
		[parent] >> [child]
		'''

		try :
			print ('connect %s to %s' %( self , target ))
			mc.connectAttr( self , target , f = True )
		except RuntimeError :
			mc.warning(	'Connection failed, %s and %s has something went wrong.' % ( self , target )	)





	# Lock and hide attribute
	def lockHide( self ):
		mc.setAttr( self , lock = True , keyable = False )
		
	def editAttrManual( self, lock = False , keyable = True ,channelBox = True):
		''' do some edit lock or unlock hide or unhide'''
		mc.setAttr( self , lock = lock , keyable = keyable ,channelBox = channelBox)



	#... Set attr value property
	def getVal( self ):
		val = mc.getAttr(self)
		# filter the condition
		if type(val) is None :
			return val[0]
		else:
			return val

	def setVal( self , val ):

		# filter the condition
		# if this value is tuple or list
		if type(val) == type(()) or type(val) == type([]):
			node , attr = self.name.split('.')
			child = mc.attributeQuery( attr , node = node , listChildren = True)

			for ix in range( 0 , len(child)):
				mc.setAttr('%s.%s' %( node , child[ix] ) , val[ix])
		else:
			# Use another method for ask what type
			if MAYA_VERSION >= '2023':
				if isinstance(val, str):
					CoreLogger.info('This is string.')
					mc.setAttr(self, val, type='string')
				else:
					CoreLogger.info('This is number.')
					mc.setAttr( self , val )
					CoreLogger.info('set value of %s to %f' %(self.name , val))
			else:
				if type(val) == 'str':
					CoreLogger.info('This is string.')
					mc.setAttr(self, val, type='string')
				else:
					print ('This is number.')
					mc.setAttr( self , val )
					CoreLogger.info('set value of %s to %f' %(self.name , val))




	value = property( getVal , setVal , None , None)

	# get value
	# ikCtrlDist = stick_ctrl.attr('regionnair').value
	# set value













 #       _                   _____              
 #      | |                 |  __ \             
 #   ___| | __ _ ___ ___    | |  | | __ _  __ _ 
 #  / __| |/ _` / __/ __|   | |  | |/ _` |/ _` |
 # | (__| | (_| \__ \__ \   | |__| | (_| | (_| |
 #  \___|_|\__,_|___/___/   |_____/ \__,_|\__, |
 #                                         __/ |
 #                                        |___/ 





class Dag( Node ) :
	''' Template DAG class  '''
	def __init__( self , nodeName = '' ) :
		Node.__init__( self , nodeName )
	
	# shape properties
	def getShape( self ) :
		shapes = mc.listRelatives( self.name , shapes = True )
		if shapes :
			if len( shapes ) > 1 :
				return shapes[ 0 ]
			else :
				return shapes[ 0 ]
	
	def renameShape( self , newName ) :
		shapes = mc.listRelatives( self.name , shapes = True )
		if shapes :
			for shape in shapes :
				mc.rename( shape , newName )
	
	shape = property( getShape , None , None , None )


	'''
	rocker_grp = core.Dag('hahayo')
	rocker_grp.nmCreateController('placement_ctrlShape')
	rocker_grp.shape
	'''











	# =================
	# Color part
	# =================

	def getColor( self ):
		# Use shape property
		# return number
		return mc.getAttr( '%s.overrideColor' %self.shape )

	def setColor( self, color ):
		# use property from line 101 to getshape
		shape = self.shape
		print ('shapename is %s' %shape)
		
		
		# color dictionary
		colorDict = {   'yellow'    : 17 ,          'red'           : 13 ,
						'softBlue'  : 18 ,          'blue'          : 6 ,
						'white'     : 16 ,          'brown'         : 11 ,
						'black'     : 1 ,           'gray'          : 2 ,
						'softGray'  : 3 ,           'darkRed'       : 4 ,
						'darkBlue'  : 5 ,           'darkGreen'     : 7 ,
						'green'     : 14 ,          'none'          : 0     }
		

		if color in colorDict.keys():
			# if color is string Ex. 'green'
			if type (color) == type( str() ):
				print ('This is string.')
				colorId = colorDict[color]
				print ('Change color to %s.' %color)
				''' 
				elif type (color) == type( int() ):
				print 'This is int.'
				colorId = color
				print colorId
				'''
			else:
				colorId = 0



		if type( shape ) is type( [] ) :
			mc.setAttr( '%s.overrideEnabled'    % shape[0] , 1 )
			mc.setAttr( '%s.overrideColor'      % shape[0] , colorId )

		else :  
			mc.setAttr( '%s.overrideEnabled'    % shape , 1 )
			mc.setAttr( '%s.overrideColor'      % shape , colorId )
	



	color = property( getColor , setColor , None , None )


	def setOutlineColor( self,color ):
		RGB_dict = mnd.rgbCode

		if color in RGB_dict.keys():
			
				colorId = RGB_dict[color]
				mc.setAttr(   	 '%s.useOutlinerColor' %self.name ,True   )
				mc.setAttr (	 '%s.outlinerColor' %self.name , colorId[0],colorId[1],colorId[2]	)

				try:
					mm.eval('AEdagNodeCommonRefreshOutliners();')
				except:
					mc.warning('Please enable plugins for AEdagNodeCommonRefreshOutliners.')




	# =================
	# Rotation order
	# =================

	def getRotateOrder( self ):
		roDict = {  'xyz' : 0   ,
					'yzx'  : 1  ,
					'zxy'  : 2  ,
					'xzy'  : 3  ,
					'yxz'  : 4  ,
					'zyx'  : 5          }

		roID = mc.getAttr( '%s.rotateOrder' %self.name )

		for key in roDict.keys():
			if roID == roDict[key]:
				print ('Setting rotation order id to %s ' %roID)
				return roID
		else:
			mc.error('Something went wrong with getRotateOrder.')

	def setRotationOrder( self , rotationOrder ):
		roDict = {  'xyz' : 0   ,
					'yzx'  : 1  ,
					'zxy'  : 2  ,
					'xzy'  : 3  ,
					'yxz'  : 4  ,
					'zyx'  : 5          }

		if rotationOrder in roDict.keys():
			val = roDict[ rotationOrder ]
		else:
			val = rotationOrder

		mc.setAttr( '%s.rotateOrder' %self.name , val )
		print ('set rotation order of %s to %s' %(self.name , rotationOrder))

	rotateOrder = property( getRotateOrder , setRotationOrder , None , None  )










	# =================

	# All aboit Adjust controller 

	# =================


	def editCtrlShape( self  , axis = 1 ):
		# is the same output of scaleShape method
		# be causion this function is will destory old attr in shapeNode (fixed it use diff method)
		# use in create gimbal in tai menu
		# 'axis' arg is mean scale my bad


		print ('Edit axis is %s' %axis)
		shapes = self.getCurveData()    
		#shapes = self.shape
		newShapes = []

		# this is mean
		# for each of point [i] 1,2,3,4,5,..... number of point
		# for each is value ( -0.12 3.93, 12.53 )
		for i , each in enumerate( shapes["points"] ):
			shapes["points"][i] = [ each[0] * axis, each[1] * axis, each[2] * axis ]
		# Append new value to shape
		newShapes.append(shapes)
		# that mean make this multiply with input
		# and append that to new shape

		# specifiy the shape that u went to make
		print ('Adjust new shape...')
		self.setShape( newShapes )



	def nmCreateController( self , shapeName = '' ):
		'''inside Class Dag create controller from lib'''
		data = wcd.loadData ( path = SHAPE_LIBRARY_PATH + shapeName + '.json')
		curveName = mc.curve ( name = self.name,  p = data["points"], k = data["knots"], d = data["degree"], per = bool(data["form"]))
		
		# Still error fix later
		curveShape = mc.listRelatives( self.name,  shapes = True )[ 0 ]
		return mc.rename( curveShape , '%sShape' % self.name )



	def createParentController( self , data ):
		curveName = mc.curve ( name = self.name,  p = data["points"], k = data["knots"], d = data["degree"], per = bool(data["form"]))



	# 2.5 get knot  , what is knot  ?
	def getKnots(self ,  crvShape = None ):
		mObj = om.MObject()
		sel = om.MSelectionList()
		sel.add(crvShape)
		sel.getDependNode(0, mObj)

		fnCurve = om.MFnNurbsCurve(mObj)
		tmpKnots = om.MDoubleArray()
		fnCurve.getKnots(tmpKnots)

		return [tmpKnots[i] for i in range(tmpKnots.length())]



	



	def setShape( self , crvShapeList ):
		''' Creates a new shape on the crv transform, by using the properties in the crvShapeDict. 
		return new ctrl name'''
		crvShapes = Dag.validateCurve( self )

		print ('Reseting new shape of %s' %self.name)

		oldColour = mc.getAttr(crvShapes[0] + ".overrideColor")
		mc.delete(crvShapes)

		for i, crvShapeDict in enumerate(crvShapeList):
			tmpCrv = mc.curve( p = crvShapeDict["points"], k = crvShapeDict["knots"], d = crvShapeDict["degree"], per = bool(crvShapeDict["form"] ) )
			
			newShape = mc.listRelatives( tmpCrv, s=1 )[0]
			mc.parent(newShape, self.name, r=1, s=1)

			mc.delete(tmpCrv)

			# assign name by the object and +'Shape'
			newShape = mc.rename( newShape, self.name + "Shape"  )

			mc.setAttr(newShape + ".overrideEnabled", 1)


			'''

			if "colour" in crvShapeDict.keys():

				print 'This is already having a color.'
				self.setColor(crvShapeDict["colour"])
				print newShape
				print crvShapeDict["colour"]


				#setColour(newShape, crvShapeDict["colour"])
			else:
				print 'yoo'
				print newShape
				print oldColour

				#setColour(newShape, oldColour)
			'''

	def setShapeExt( self , crvShapeList ):
		''' Creates a new shape on the crv transform, by using the properties in the crvShapeDict. 
			and transfer the attr before delete by set shape '''

		''' found out copyCtrlShape tools is can replace curve with another shape of curve with command 
		mc.curve( sel[1], replace ) arg  may be this method it not nesseary any more '''

		


		crvShapes = Dag.validateCurve( self )



		print ('Reseting new shape of %s' %self.name)

		oldColour = mc.getAttr(crvShapes[0] + ".overrideColor")

		temp_old_shape = mc.rename( crvShapes, self.name + "ShapeTemp"  )
		

		for i, crvShapeDict in enumerate(crvShapeList):
			tmpCrv = mc.curve( p = crvShapeDict["points"], k = crvShapeDict["knots"], d = crvShapeDict["degree"], per = bool(crvShapeDict["form"] ) )
			
			newShape = mc.listRelatives( tmpCrv, s=1 )[0]
			mc.parent(newShape, self.name, r=1, s=1)


			# insert function here
			self.transferAttr(temp_old_shape,newShape)


			mc.delete(tmpCrv)

			# assign name by the object and +'Shape'
			newShape = mc.rename( newShape, self.name + "Shape"  )
			mc.delete(temp_old_shape)


			# set to old color
			mc.setAttr(newShape + ".overrideEnabled",1)
			mc.setAttr(newShape + ".overrideColor", oldColour )
				


	def replaceControllerShape(self, shapesData):

		# replace controller to another shape 
		# using with getCurveData method
		# example
		'''
		ctrl_new = core.Dag('curve2')
		data = ctrl_new.getCurveData()
		ctrl_new.replaceControllerShape(data)
		'''

		mc.curve( self.name , replace = True, p=shapesData["points"], k=shapesData["knots"], d=shapesData["degree"], per=bool(shapesData["form"]) )



	def transferAttr(self , sourceShape ,destinationShape ):
		# intend create for transferAttr when use copy shape controller tools 
		# but it no neet anymore use mc.curve instead

		# qury source shape node
		old_shapeName = sourceShape
		
		new_shapeName = Dag(destinationShape)

		print ('Transfer attribute of %s' %self.name)


		
		# get latest attr
		lstAttr = mc.listAttr(old_shapeName)

		# 'maxValue' is the last know default attr os I assume is the suit for find another extra attr
		default_attr = lstAttr.index('maxValue')

		# make it to number
		attrNum = default_attr + 1
		# some number that hide arNold node
		attrDefNum = 206


		print ('the number of %s is %d' %(old_shapeName,len(lstAttr)))
		if len(lstAttr) == attrNum or len(lstAttr) == attrDefNum:
			print ('This is no additional attribute Ending na.')
			return False

		elif len(lstAttr) > attrNum:
			print ('This value is more than default.')
			extraAttr = len(lstAttr) - attrNum
			print (extraAttr)
			for i in range (0,extraAttr):
				print ('\n')

				# print attr name
				attrName = lstAttr[attrNum + i]
				print (attrName)

				# now we got the attr name
				# get value
				attrValue = mc.getAttr('%s.%s' %(old_shapeName,lstAttr[attrNum + i]))
				print (attrValue)

				# get type
				typeAttr = mc.getAttr('%s.%s' %(old_shapeName,lstAttr[attrNum + i]),type=True)
				CoreLogger.info(typeAttr)
				print ('\n')

				if typeAttr == 'enum':
					CoreLogger.info('this is Enum.')
					enumStr = mc.attributeQuery( lstAttr[attrNum + i] , node = old_shapeName , listEnum=True )[0]
					new_attr = new_shapeName.addAttribute( at = 'enum', keyable = True , en = enumStr , ln = attrName  )
					# got the connection
					relink_connection = mc.listConnections(old_shapeName + '.' + attrName, p=True)[0]
					mc.connectAttr( new_shapeName.name + '.' + lstAttr[attrNum + i], relink_connection , f = True)
					
				else:
					CoreLogger.info('this is not Enum.')
					# check if having min max value 
					if mc.attributeQuery( lstAttr[attrNum + i] , node = old_shapeName, minExists = True):
						min = mc.attributeQuery( lstAttr[attrNum + i] , node = old_shapeName, min = True)[0]
						max = mc.attributeQuery( lstAttr[attrNum + i] , node = old_shapeName, max = True)[0]
						new_attr = new_shapeName.addAttribute( at = typeAttr ,min = min ,max = max , ln = lstAttr[attrNum + i] ,k = True ,dv = attrValue )
					else:
						# if no min max cap
						new_attr = new_shapeName.addAttribute(at = typeAttr , ln = lstAttr[attrNum + i] , k = True , dv = attrValue )


					# got the connection
					relink_connection = mc.listConnections(old_shapeName + '.' + attrName, p=True)[0]
					mc.connectAttr( new_shapeName.name + '.' + lstAttr[attrNum + i], relink_connection , f = True)
					print (relink_connection)



		else:
			print ('There are no suit condition maybe number of attribure is mismatch(%d)' %(len(lstAttr)))






	def validateCurve( self ):
		'''Checks whether the transform we are working with is actually a curve and returns it's shapes'''

		
		if mc.nodeType(self) == "transform" and mc.nodeType(mc.listRelatives(self, c=1, s=1)[0]) == "nurbsCurve":
			crvShapes = mc.listRelatives(self, c=1, s=1)

		elif mc.nodeType(self) == "nurbsCurve":
			crvShapes = mc.listRelatives(mc.listRelatives(self, p=1)[0], c=1, s=1)

		elif mc.nodeType(self) == "transform":
			crvShapes = mc.listRelatives(self, shapes=True)

		else:
			mc.error("The object " + self.name  + " passed to validateCurve() is not a curve")
		return crvShapes








	# 2 getshape
	# create dictionary template
	# is a getShape from wcd
	def getCurveData( self ):
		'''Returns a dictionary containing all the necessery information for rebuilding the passed in crv.
			convert from  wcd.getShape change it becasue getShape is confuse name       '''
		ctrlName = self.name
		print ('ctrl name is : %s' %ctrlName)
		crvShapes = self.shape 
		print ('shape name is : %s' %self.shape )

		crvShapeList = []

		#for crvShape in crvShapes:
		crvShapeDict = {
			"name":ctrlName,
			"points": [],
			"knots": [],
			"form": mc.getAttr(crvShapes + ".form"),
			"degree": mc.getAttr(crvShapes + ".degree"),
			"colour": mc.getAttr(crvShapes + ".overrideColor")
		}
		points = []
		# get CV point data
		for i in range(mc.getAttr(crvShapes + ".controlPoints", s=1)):
			points.append(mc.getAttr(crvShapes + ".controlPoints[%i]" % i)[0])

		crvShapeDict["points"] = points
		# get knots , what is knots
		crvShapeDict["knots"] = self.getKnots(crvShapes)

		crvShapeList.append(crvShapeDict)

		#return crvShapeDist instead
		return crvShapeDict

	
	def modifiyCtrlShape( self , getCurveData , axis = [-1, -1, -1] ):
		# inner method for change shape to another 
		# redundance with editCtrlShape
		# using in nmCreate gimbal
		newShapes = []
		for i, each in enumerate( getCurveData["points"] ):
			getCurveData["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
		newShapes.append( getCurveData )
		return newShapes
	
		

	def scaleShape( self , scale = ( 1,1,1 ) ):
		''' scale object controller '''
		print ('Scale %s Controller.' %self.name)
		# shapes = wcd.getShape( self.name )
		
		# shapesData = Dag(self)
		dictData = self.getCurveData()  
		newShapes = []
		for i, each in enumerate( dictData["points"] ):
			dictData["points"][i] = [each[0] * scale[0], each[1] * scale[1], each[2] * scale[2]]
		newShapes.append( dictData )
		self.setShape(  newShapes  )


	def rotateShape( self , rotate = ( 0 , 0 , 0) ):
		''' rotation CV curve '''
		if self.shape:
			print (self.name + 'is might be a curve.')
			cvsNo = mc.getAttr('%s.spans' %self.shape) + mc.getAttr('%s.degree' %self.shape) 
			cvs = '%s.cv[%s:%s]' %(self.name , str(0) , str(cvsNo) )

			mc.rotate( rotate[0] , rotate[1] , rotate[2] , cvs , r = True , os = True)


	def moveShape( self , move = ( 0 , 0 , 0 ) ):
		''' move CV curve  '''
		if self.shape:
			print (self.name + 'is might be a curve.')
			cvsNo = mc.getAttr('%s.spans' %self.shape) + mc.getAttr('%s.degree' %self.shape) 
			cvs = '%s.cv[%s:%s]' %(self.name , str(0) , str(cvsNo) )

			mc.move( move[0] , move[1] , move[2] , cvs , relative = True , objectSpace = True)


	def flipCtrlShape( self , axis = 'Y' ):
		''' flip control shape '''
		if axis == 'Y':
			mul =  (-1, -1, 1) 
		elif axis == 'Z':
			mul =  (-1, 1, -1) 
		else:
			mul =  (1, -1, -1) 
		
		print ('flip %s Controller' %self.name )
		# instancing 
		shapes = Dag.getCurveData( self )   
		newShapes = []


		for i, each in enumerate(shapes["points"]):
			shapes["points"][i] = [each[0] * mul[0], each[1] * mul[1], each[2] * mul[2]]
		newShapes.append( shapes )
		Dag.setShape( self , newShapes )




	def getWorldSpace( self ):
		''' return world space positon '''
		validTypes = ( 'transform' , 'joint' )

		if self.type in validTypes :
			pos = mc.xform( self , query = True , worldSpace = True , translation = True )
			return ( float( pos[0]) , float(pos[1]) , float(pos[2] ) )

		else:
			mc.warning('There is no input.')
	worldSpace = property( getWorldSpace , None , None , None  )


	# =================
	# Transformation attribure
	# =================

	def getParent(self):
		obj = mc.listRelatives(self , parent = True)

		if obj:
			return Dag( obj[0] )
		else:
			return None

	def parent( self , target = '' ):
		if target:
			mc.parent( self , target )
			print ('Parent %s to %s.' %( self , target ) )
		else:
			mc.parent( self , world = True )
			print ('There are no object to parent than parent to world.' )
		mc.select( clear = True )






	# =================
	# snap tool
	# =================

	def maSnap( self , target , *args,**kwargs ) :
		'''
		in case don't want to snap all of attr use this arg
		pos = False
		rot = False
		scl = False
		
		'''
		mc.matchTransform( self.name , target  , *args,**kwargs ) 

	# cmds.matchTransform('cylinder1','cone1')

	def freeze( self , **kwargs ) :
		mc.makeIdentity( self , apply = True , **kwargs )

	def snap( self , target ) :
		# Match current position and orientation to target
		mc.delete( mc.parentConstraint( target , self.name , mo=False ) )

	def snapPoint( self , target , *args,**kwargs) :
		# Match current position to target
		mc.delete( mc.pointConstraint( target , self.name , mo=False , *args,**kwargs) )
	
	def snapOrient( self , target ) :
		# Match current orientation to target
		mc.delete( mc.orientConstraint( target , self.name , mo=False ) )
	
	def snapScale( self , target ) :
		# Match current scale to target
		mc.delete( mc.scaleConstraint( target , self.name , mo=False ) )




	# =================
	# Hide arnold node Must select curve first
	# =================

	def hideArnoldNode( self , attr = ['rcurve' ,' cwdth' , 'srate' , 'ai_curve_shaderr' ,'ai_curve_shaderg' , 'ai_curve_shaderb' ]  ):

		if self.name :
			CoreLogger.info('Hide arnold node.')
			shape = self.shape
			for each in attr:
				try:
					mc.setAttr( shape + '.' + each , keyable = False ,  channelBox = False )

				except:
					CoreLogger.info('There are no arnold node.')
					pass


	'''def setTranslation(self, x = None, y = None, z = None):
					self._doTransform(mc.move, x,y,z)'''

	def setTranslate( self, value ):
		self._doTransform( mc.move, value[0] , value[1] , value[2] )


	def setRotate( self, value ):
		self._doTransform( mc.rotate, value[0] , value[1] , value[2] )


	def _doTransform(self, func, x, y, z,):
		for name in ('x','y','z'):
			val = locals()[name]
			if val is not None:
				# what is this 
				opts = { name:True, 'objectSpace':True, 'absolute':True }
				func(val, self.name, **opts)



	def lockHideAttrLst( self , *args ):
		'''
		# = = = = = = = = = = = = = = = = = 
		# lock and hide attr, i don't know how to use this attr in attribute class then i copy it here
		# = = = = = = = = = = = = = = = = = 
		'''
		for each in args:
			mc.setAttr( '%s.%s' %( self, each ) , lock = True , keyable = False )
			print ('Lock %s attribute of %s object.' %( each ,self  ))

	def unLockHideAttrLst(self , *args ):
		for each in args:
			mc.setAttr( '%s.%s' %( self, each ) , lock = False , keyable = True )
			print ('Unlock %s attribute of %s object.' %( each ,self  ))







	# Set attr value property
	def getPosVal( self , dist):
		'''
		# = = = = = = = = = = = = = = = = = 
		# lock and hide attr, i don't know how to use this attr in attribute class then i copy it here
		# = = = = = = = = = = = = = = = = = 
		'''
		val = mc.getAttr(self , self.name + dist)
		# filter the condition
		if type(val) is None :
			return val[0]
		else:
			return val


	# add attr limit translate
	def limitTrans( self , *args  , **kwargs ):
		mc.transformLimits(  self.name , *args,**kwargs  )




	'''
	def addRotEnum( self ):
		ctrl = Dag(self.name)
		rotOrderLst = 'xyz:yzx:zxy:xzy:yxz:zyx'
		ctrlShape = ctrl.shape
		
		ctrlShape = Dag( ctrlShape )
		ctrlShape.addAttribute( at = 'enum', keyable = True , en = rotOrderLst , ln = 'rotate_Order'  )
		ctrlShape.attr('rotate_Order') >> ctrl.attr('rotateOrder')
		
		print 'Connect rotation order to shapeNode'
	'''

	def addRotEnum( self ):
		''' add rotation order attr to controller object '''
		rotOrderLst = 'xyz:yzx:zxy:xzy:yxz:zyx'
		ctrlShape = self.shape
		ctrlShape = Dag( ctrlShape )
		ctrlShape.addAttribute( at = 'enum', keyable = True , en = rotOrderLst , ln = 'rotate_Order'  )
		# get the original rotation order number from the transform node
		rotNum = self.rotateOrder

		CoreLogger.info('\n')
		CoreLogger.info('This is %s' %rotNum)
		CoreLogger.info('\n')

		if rotNum:
			roDict = mnd.rotOrder_dict

			if rotNum in roDict.keys():
				val = roDict[ rotNum ]
			else:
				val = rotNum

			
			mc.setAttr( '%s.rotate_Order' %self.name , val )
			print ('set rotation order of %s to %s' %(self.name , rotNum))


		
		print ('Connect rotation order to shapeNode')


		ctrlShape.attr('rotate_Order') >> self.attr('rotateOrder')

		
		
		






	def duplicateObj( self, *args , **kwargs ):
		tmpDup = mc.duplicate( self.name , *args , **kwargs)[0]
		# return as object
		return Dag(tmpDup)

	# for moving geo with relative value
	def moveObj( self, position ):
		mc.move( position[0], position[1], position[2], self.name, relative=True, objectSpace=True, worldSpaceDistance=True )



	# for curve edit
	# not sure will crash or not so change name little
	def curveFe( self, *args , **kwargs ):
		return Dag(  mc.curve(*args , **kwargs) )


	def rebuildCurve(self ,constructionHistory = False , replaceOriginal = True, rebuildType = 0, endKnots = 1, keepRange = 0, 
					keepControlPoints = False, keepEndPoints = False, keepTangents = False , spans = 4, degree = 3, 
					tol = 0.0001):
		try:
			mc.rebuildCurve( self.name ,ch = constructionHistory , rpo = replaceOriginal, rt = rebuildType, end = endKnots, kr = keepRange, 
							kcp = keepControlPoints, kep = keepEndPoints, kt = keepTangents , s = spans, d = degree, tol = tol  )
		except:
			mc.warning('The object maybe not Curve. Please check')




class Follicle( Node ):
	def __init__( self ):
		Node.__init__(self , mc.createNode( 'follicle' ) , parent = self.name )












 #       _                   _   _       _ _ 
 #      | |                 | \ | |     | | |
 #   ___| | __ _ ___ ___    |  \| |_   _| | |
 #  / __| |/ _` / __/ __|   | . ` | | | | | |
 # | (__| | (_| \__ \__ \   | |\  | |_| | | |
 #  \___|_|\__,_|___/___/   |_| \_|\__,_|_|_|                                         
 #                                           


class Null( Dag ) :
	''' 
	for create Object empty group in maya
	'''
	def __init__( self , name = '' ) :
		'''in case if u want name of group'''
		Dag.__init__( self , mc.group( em = True , name = name) )

	def follicle(self   , **kwargs ):
		"""Special method for parent follicle shapeNode to previous transfromNode that create earilor """
		mc.createNode( 'follicle' , parent = self.name , **kwargs)



'''class NurbSphere( Dag ):
	def __init__( self ) :
		Dag.__init__( self , mc.sphere() )
'''


 #      _                   _   _            _     
 #      | |                 | \ | |          | |    
 #   ___| | __ _ ___ ___    |  \| |_   _ _ __| |__  
 #  / __| |/ _` / __/ __|   | . ` | | | | '__| '_ \ 
 # | (__| | (_| \__ \__ \   | |\  | |_| | |  | |_) |
 #  \___|_|\__,_|___/___/   |_| \_|\__,_|_|  |_.__/ 
												  
												  

class Nurb( Dag ):
	def __init__(self, name ):
		Dag.__init__( self , name )

	def sphere(self, **kwargs):
		mc.sphere(name = self.name , **kwargs )




class Locator( Dag ):
	""" Create Locator Object """
	def __init__( self , name ):
		Dag.__init__( self , mc.spaceLocator(name = name)[0] )
		# lock drawing override
		# this lock is cause problem that child will can not select
		# self.attr( 'overrideEnabled' ).value = 1
		# self.attr( 'overrideDisplayType' ).value = 2










#       _                         _       _       _   
#      | |                       | |     (_)     | |  
#   ___| | __ _ ___ ___          | | ___  _ _ __ | |_ 
#  / __| |/ _` / __/ __|     _   | |/ _ \| | '_ \| __|
# | (__| | (_| \__ \__ \    | |__| | (_) | | | | | |_ 
#  \___|_|\__,_|___/___/     \____/ \___/|_|_| |_|\__|




class Joint( Dag ):
	''' 
	WARNING !!! joint object adjust for assign name when create
	no need name it will cause error
	'''
	''' 
	def __init__( self  , name = '' ):
		Dag.__init__( self , mc.createNode('joint' , name = name )  )'''

	def __init__( self , name = 'joint_1'):
		Dag.__init__( self , mc.createNode('joint' , name = name )  )
		#... Disable seqment scale compensage as a default (Disable here if anythin wrong.)






	def setLable( self, jSide , jType  ):
		'''
		Set joint label 
		@param jType: joint type
		@type jType: string
		@param jSide: joint side
		@type jSide: string
		'''
	
		# color dictionary
		sideDict = {	'CEN'		: 0 ,
						'LFT'		: 1 ,
						'RGT'		: 2 ,
						'none'		: 3		} 


		typeDict = {	'none'		: 0 ,	'finger'			: 13 ,    	'mid toe'		: 26 ,
						'root'  	: 1 ,	'thumb'				: 14 ,    	'ring toe'		: 27 , 
						'hip'		: 2 ,	'propA'				: 15 ,    	'pinky toe'		: 28 , 
						'knee'		: 3 ,	'propB'				: 16 ,   	'foot thumb'	: 29 ,  
						'foot'		: 4 ,	'propC'				: 17 ,      
						'toe'		: 5 , 	'other'				: 18 ,
						'spine'     : 6 ,	'index finger'		: 19 ,
						'neck'   	: 7 ,	'mid finger'		: 20 ,
						'head'		: 8 ,	'ring finger'		: 21 ,
						'collar'	: 9 ,	'pinky finger'		: 22 ,
						'shoulder'	: 10 ,	'extra finger'		: 23 ,
						'elbow'		: 11 ,	'big toe'			: 24 ,
						'hand'		: 12 ,	'index toe'			: 25 ,										}


		if jType in typeDict.keys():

			if type ( jType ) == type( str() ):
				print ('This is string.')
				typeId = typeDict[jType]
				print ('Change joint type to %s.' %jType)
				
			elif type (jType) == type( int() ):
				print ('This is int.')
				typeId = jType
				print (typeId)
				
		else:
			typeId = 0



		if jSide in sideDict.keys():

			if type ( jSide ) == type( str() ):
				print ('This is string.')
				sideId = sideDict[jSide]
				print ('Change joint side to %s.' %jSide)
				
			elif type (jSide) == type( int() ):
				print ('This is int.')
				sideId = jSide
				print (sideId)
				
		else:
			sideId = 0



		mc.setAttr( '%s.side'	%self.name , sideId )
		mc.setAttr( '%s.type'	%self.name , typeId )






	label = property( setLable , None , None , None )

	# set joint color
	def setJointColor( self , color ):
		COLOR_dict = mnd.COLOR_dict

		if color in COLOR_dict.keys():
			colorId = COLOR_dict[color]
			mc.setAttr( '%s.overrideEnabled'    % self.name , 1 )
			mc.setAttr( '%s.overrideColor'      % self.name, colorId )

		else:
			colorId = 0
			mc.error("Insert string keyword such as yellow")

	
	# why disable
	def setJointOutlineColor( self,color ):
		RGB_dict = mnd.rgbCode

		if color in RGB_dict.keys():
			colorId = RGB_dict[color]
			mc.setAttr(   	 '%s.useOutlinerColor' %self.name ,True   )
			mc.setAttr (	 '%s.outlinerColor' %self.name , colorId[0],colorId[1],colorId[2]	)
			mm.eval('AEdagNodeCommonRefreshOutliners();')
	


	def createJntShape( self , localScale = 1 ):
		# for parent this under to shape node
		self.tmpLoc = Locator('tmpName')

		mc.parent( self.tmpLoc.shape , self.name , s = True , r = True )
		mc.rename( self.tmpLoc.name + 'Shape' , self.name + 'Shape')
		mc.delete( self.tmpLoc.name)
		self.setOutlineColor('white')
		self.setJointColor('white')
		self.attr( 'localScaleX' ).value = localScale
		self.attr( 'localScaleY' ).value = localScale
		self.attr( 'localScaleZ' ).value = localScale

		mc.select( deselect = True )













 #       _                     _____                _             _       _   
 #      | |                   / ____|              | |           (_)     | |  
 #   ___| | __ _ ___ ___     | |     ___  _ __  ___| |_ _ __ __ _ _ _ __ | |_ 
 #  / __| |/ _` / __/ __|    | |    / _ \| '_ \/ __| __| '__/ _` | | '_ \| __|
 # | (__| | (_| \__ \__ \    | |___| (_) | | | \__ \ |_| | | (_| | | | | | |_ 
 #  \___|_|\__,_|___/___/     \_____\___/|_| |_|___/\__|_|  \__,_|_|_| |_|\__|



class Constraint( Dag ):
	""" base class for constraint """
	def __init__(self, nodeName = ''):
		Dag.__init__( self , nodeName )

	def getTargets( self ):
		return mc.listConnections('%s.target' %self.name , source = True )

	target = property( getTargets , None , None , None )






 #    _____                _             _       _   
 #  / ____|              | |           (_)     | |  
 # | |     ___  _ __  ___| |_ _ __ __ _ _ _ __ | |_ 
 # | |    / _ \| '_ \/ __| __| '__/ _` | | '_ \| __|
 # | |___| (_) | | | \__ \ |_| | | (_| | | | | | |_ 
 #  \_____\___/|_| |_|___/\__|_|  \__,_|_|_| |_|\__|




def parentConstraint( *args , **kwargs ):
	return Constraint( mc.parentConstraint ( *args , **kwargs)[0] )

def scaleConstraint( *args , **kwargs ):
	return Constraint( mc.scaleConstraint ( *args , **kwargs)[0] )

def orientConstraint( *args , **kwargs ):
	return Constraint( mc.orientConstraint( *args , **kwargs)[0] )

def pointConstraint( *args , **kwargs ):
	return Constraint( mc.pointConstraint( *args , **kwargs)[0] )

def aimConstraint( *args , **kwargs ):
	return Constraint(mc.aimConstraint( *args , **kwargs )[0] )
	
def poleVectorConstraint( *args , **kwargs ):
	return Constraint( mc.poleVectorConstraint ( *args , **kwargs)[0] )

def parentShape( parent = '' , child = '' ):
	''' parent shapeNode of child to transformNode of parent '''
	par = Dag( parent )
	chd = Dag( child )

	mc.parent( par.shape , chd , s = True , r = True )
	mc.delete( par )






#       
#	EXPERIMENT: try to use classmethod instead
#

class Constr( Constraint ):
	""" base class for constraint """
	def __init__( self ,nodeName = ''):
		Constraint.__init__( self , nodeName )

	@classmethod
	def psConstr(cls, *args , **kwargs):
		return Constraint( mc.parentConstraint (*args , **kwargs)[0] )








class ParentConstraint( Constraint ):
	""" inherit from Constraint """
	def __init__( self ):
		Constraint.__init__( self , mc.createNode('parentConstraint')   )


class AimConstraint( Constraint ):
	""" inherit from Constraint """
	def __init__( self ):
		Constraint.__init__( self , mc.createNode('aimConstraint')   )


class PoleVectorConstraint( Constraint ):
	""" inherit from Constraint """
	def __init__( self ):
		Constraint.__init__( self , mc.createNode('poleVectorConstraint')   )


class ScaleConstraint( Constraint ):
	""" inherit from Constraint """
	def __init__( self ):
		Constraint.__init__( self , mc.createNode('scaleConstraint')   )









#         _                          _____   _    
#        | |                        |_   _| | |   
#   ___  | |   __ _   ___   ___       | |   | | __
#  / __| | |  / _` | / __| / __|      | |   | |/ /
# | (__  | | | (_| | \__ \ \__ \     _| |_  |   < 
#  \___| |_|  \__,_| |___/ |___/    |_____| |_|\_\
												

class Ik( Dag ):
	'''Template class for IK object'''
	def __init__( self , name = '' ):
		Dag.__init__( self , name )

		# name overriding (for what why not used direcly)
		self.__name = name

	# Name properties
	def getName( self ):
		return self.__name

	def rename( self , newName ):
		self.__name = mc.rename( self.__name , newName )
		# call eff property for change eff name stimulation
		self.eff = '%s_eff' %newName
	name = property( getName , rename , None , None)






	# Eff properties
	def getEff(self):
		return mc.listConnections( '%s.endEffector' %self.__name , source = True , destination = False )[0]
	def setEff(self , newName = ''):
		print ('Effector has been change to %s' %newName)
		mc.rename( self.eff , newName )
	eff = property( getEff , setEff , None , None )







	# curve properties
	def getCrv(self):
		return mc.listConnections( '%s' %self.__name , source = True , destination = False )[-1]
	def reCrv(self , newName = ''):
		print ('Curve has been change to %s' %newName)
		mc.rename( self.crv , newName )

	crv = property( getCrv , reCrv , None , None )



class IkRp( Ik ):
	''' Class ik rotate plane '''
	def __init__( self , startJoint = '' , endEffector = ''  ):
		Ik.__init__( self , mc.ikHandle( startJoint = startJoint , endEffector = endEffector ,  solver = 'ikRPsolver') [0] )


class DoIk( Ik ):
	''' Newer than IkRp 
	ikRPsolver, ikSCsolver and ikSplineSolver
	armIk_ikh = core.DoIk( startJoint = upArmIk_jnt , endEffector = self.wristIk_jnt , solver = solverType )

	'''
	def __init__( self , startJoint = '' , endEffector = '' ,solverType = '' , parentCurve = False ):
		Ik.__init__( self , mc.ikHandle( startJoint = startJoint , endEffector = endEffector , parentCurve = parentCurve,  solver = solverType) [0] )


# it make break auto rig so create the new one instead	
class DoIkSpline( Ik ):
	 
	'''
	# Newer than IkRp put the solver in to attr instead

	[solverType]
	ikRPsolver, ikSCsolver , ikSplineSolver

	[in case using ikSplineSolver with specific crv]
	spineIK_spinCrv= core.DoIk( startJoint = bind_jnt[0] ,endEffector = bind_jnt[-1] ,solverType = 'ikSplineSolver',createCurve = False,curvName =  spine_crv ,parentCurve = False )

	armIk_ikh = core.DoIk( startJoint = upArmIk_jnt , endEffector = self.wristIk_jnt , solver = solverType )

	'''
	def __init__( self , startJoint = '' ,endEffector = '' ,solverType = ''  ,createCurve = False, parentCurve = False):# cut the "name" attr because it will crash dunno why
		Ik.__init__( self , mc.ikHandle( startJoint = startJoint , endEffector = endEffector ,  solver = solverType ,createCurve = createCurve,parentCurve = parentCurve) [0] )


class IkSpring( Ik ):
	''' Class ik spring solver  '''
	# Enable ikSpringSolver
	mm.eval('ikSpringSolver;')
	def __init__( self , startJoint = '' , endEffector = ''  ):
		Ik.__init__( self , mc.ikHandle( startJoint = startJoint , endEffector = endEffector ,  solver = 'ikSpringSolver') [0] )