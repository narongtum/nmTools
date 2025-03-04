# module that create rig tools base from core

'''
from function.rigging.autoRig.base import rigTools
reload( rigTools )

maya generic rig tools
'''
from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

import maya.api.OpenMaya as om

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.tools import dTool as dc 
reload(dc)

import pymel.core as pm

from function.pipeline import logger 
reload(logger)

class RigToolsLogger(logger.MayaLogger):
	LOGGER_NAME = "RigTools"



def createFollicle(name, uVal, vVal):
	# num =  each + 1
	# Common name
	# name =  partElem + types + '%02d'%num + side

	# Create Follicle
	folicle = core.Null( name + '_flc')
	folicle.follicle( name = folicle.name + 'Shape', ss = True )
	folicleShape = core.Dag( folicle.shape )
	ribbon_nrb.attr('local') >> folicleShape.attr('inputSurface')
	ribbon_nrb.attr('worldMatrix[0]') >> folicleShape.attr('inputWorldMatrix')

	# Connected armALFTShape.outRotate to armALFT.rotate
	folicleShape.attr('outRotate') >> folicle.attr('rotate')
	folicleShape.attr('outTranslate') >> folicle.attr('translate')

	# hide visibility
	folicle.attr('v').value = 0
	
	# Inbetween formula
	uVal = ((0.5 / numJoints) * (each + 1) * 2) - ((0.5 / (numJoints * 2)) * 2)

	'''
	if side == 'RGT':
		print 'The offset value is %d' %abs(uVal -1)
		uVal= abs(uVal -1)
	'''

	# set value
	folicleShape.attr('parameterV').value = 0.5
	folicleShape.attr('parameterU').value = uVal



# this is (older)redundance with add rig
# create locator at specified uv coordinate
# from Chris Lesage (Rigmarole Studio)
def _pinToSurface(	oNurbs = 'strapCRbnLFT_nrb'		,
					side = 'LFT'					,
					region = 'strapC'				,
					uPos = 0.5						,
					vPos=0.5						,
					num = 1 						):
	

	
	if type(oNurbs) == str and pm.objExists(oNurbs):
		oNurbs = pm.PyNode(oNurbs)
	else:
		pm.warning('Invalid surface object specified.')
		#return False




	pointOnSurface = pm.createNode( 'pointOnSurfaceInfo', name = '{}{:02d}{}_poiInfo'.format(region,num,side) )
	oNurbs.getShape().worldSpace.connect(pointOnSurface.inputSurface) # conntet from oNurbs
	# follicles remap from 0-1, but closestPointOnSurface must take minMaxRangeV into account
	paramLengthU = oNurbs.getShape().minMaxRangeU.get()
	paramLengthV = oNurbs.getShape().minMaxRangeV.get()


	# vPos = paramLengthV[1]/2
	# length = paramLengthV[1]
	# divide = numJoints+1
	# distance =  float(length)/float(divide)
				
			
	'''
	vPos = paramLengthV[1] / 2
	uDistance = paramLengthU[1] / 4
	'''

	
	method = 'follicle'

	if method == 'follicle':
		ext = 'flc'
		pName = '{}{:02d}{}_{}'.format(region,num,side,ext)
		# method use follicle way
		fol = pm.createNode('transform', n=pName, ss=True)
		result = pm.createNode('follicle', n=fol.name()+'Shape', p=fol, ss=True)
		result.parameterU.connect(pointOnSurface.parameterU)
		result.parameterV.connect(pointOnSurface.parameterV)

	elif method == 'locator':
		ext = 'loc'
		pName = '{}{:02d}{}_{}'.format(region,num,side,ext)
		result = pm.spaceLocator(n=pName).getShape()
		result.addAttr('parameterU', at='double', keyable=True, dv=uPos)
		result.addAttr('parameterV', at='double', keyable=True, dv=vPos)
		# set min and max ranges for the follicle along the UV limits.
		result.parameterU.setMin(paramLengthU[0])
		result.parameterV.setMin(paramLengthV[0])
		result.parameterU.setMax(paramLengthU[1])
		result.parameterV.setMax(paramLengthV[1])
		result.parameterU.connect(pointOnSurface.parameterU)
		result.parameterV.connect(pointOnSurface.parameterV)
	else:
		pm.error('Error')


	# set value
	result.parameterV.set(vPos)
	result.parameterU.set(uPos)

	# Compose a 4x4 matrix
	mtx = pm.createNode('fourByFourMatrix',name ='{}{:02d}{}_fbfMat'.format(region,num,side)  )
	outMatrix = pm.createNode('decomposeMatrix', name = '{}{:02d}{}_deCom'.format(region,num,side) )
	mtx.output.connect(outMatrix.inputMatrix)
	outMatrix.outputTranslate.connect(result.getTransform().translate)
	outMatrix.outputRotate.connect(result.getTransform().rotate)


	# make locator pin to surface
	# tanU
	pointOnSurface.normalizedTangentUX.connect(mtx.in00)
	pointOnSurface.normalizedTangentUY.connect(mtx.in01)
	pointOnSurface.normalizedTangentUZ.connect(mtx.in02)
	mtx.in03.set(0)

	# normal
	pointOnSurface.normalizedNormalX.connect(mtx.in10)
	pointOnSurface.normalizedNormalY.connect(mtx.in11)
	pointOnSurface.normalizedNormalZ.connect(mtx.in12)
	mtx.in13.set(0)

	# tanV
	pointOnSurface.normalizedTangentVX.connect(mtx.in20)
	pointOnSurface.normalizedTangentVY.connect(mtx.in21)
	pointOnSurface.normalizedTangentVZ.connect(mtx.in22)
	mtx.in23.set(0)

	# world space position
	pointOnSurface.positionX.connect(mtx.in30)
	pointOnSurface.positionY.connect(mtx.in31)
	pointOnSurface.positionZ.connect(mtx.in32)
	mtx.in33.set(1)

	return pName


def find_pv( arm, elbow, wrist, poleVector, distance_scale = 1 ):
	# find poleVector position
	# please note poleVector must unparent to world space
	logger.AutoRigLogger.info('Start of find pole vector function')
	arm_pos = om.MVector(mc.xform(arm, q=True, rp=True, ws=True)		)
	elbow_pos = om.MVector(mc.xform(elbow, q=True, rp=True, ws=True)	)
	wrist_pos = om.MVector(mc.xform(wrist, q=True, rp=True, ws=True)	)

	# start with the last one and subtract
	arm_to_wrist = wrist_pos - arm_pos # get distance vector

	# divide 2 
	arm_to_wrist_scaled = arm_to_wrist * 0.5 # for get mid point

	# make it start on the arm_pos position
	mid_point = arm_pos + arm_to_wrist_scaled # it should be one the between arm and wrist now

	# now make vector to elbow point
	mid_point_to_elbow_vec = elbow_pos - mid_point
	mid_point_to_elbow_vec_scale = mid_point_to_elbow_vec * 2 * distance_scale
	mid_point_to_elbow_point = mid_point + mid_point_to_elbow_vec_scale

	# snap the object to pv point
	mc.xform( poleVector, t=mid_point_to_elbow_point)



def distanceNode(	name = 'something' ,
					startPoint = ''		,
					endPoint = ''			):

	logger.AutoRigLogger.info('Start of distanceNode function')
	# Modify for distance node that alway crashing with the locator in scene
	# return name of distance node
	if startPoint:
		dis = core.DistanceBetween(name = name )
		disObj = core.Dag(dis)
		disObj.suffix

		loc1 = core.Locator(name + '1_loc')
		loc2 = core.Locator(name + '2_loc')

		loc1.maSnap(startPoint)
		loc2.maSnap(endPoint)

		loc1shape = core.Dag(loc1.shape)
		loc2shape = core.Dag(loc2.shape)
		
		loc1shape.attr('worldPosition[0]') >> disObj.attr( 'point1' )
		loc2shape.attr('worldPosition[0]') >> disObj.attr( 'point2' )

		logger.AutoRigLogger.info('End of distanceNode function')
		return disObj.name , loc1.name , loc2.name

	else:
		mc.warning("Please specify startPoint and endPoint first.")




def _creControl( nameSpace, name, ctrlShape, rotateOrder = 'yzx', parentTo = '', charScale = 1, color = 'red', rotation = (0,0,0), needConstraint = True):
	''' create controller for fk controller autoRig'''
	logger.AutoRigLogger.info('Start of program')
	if not nameSpace:
		splitName = name.split('_')[0]
		# splitName = name.splitName[0]
		part = splitName


	elif nameSpace:
		splitName = name.split('_')[1]
		part = nameSpace + splitName
		
	print( part)

	controller_ctrl = core.Dag( part + '_ctrl' )
	controller_ctrl.nmCreateController( ctrlShape )
	controller_ctrl.rotateShape( rotation )
	controllerZro_grp = zeroGroup( controller_ctrl )
	controllerZro_grp.name = part + 'Zro_grp'
	controller_ctrl.editCtrlShape( axis = charScale * 0.9 ) 
	controllerGmbl_ctrl = core.createGimbal( controller_ctrl )
	controller_ctrl.color = color
	controller_ctrl.rotateOrder = rotateOrder
	controllerGmbl_ctrl.rotateOrder = rotateOrder

	# Parenting and positioning
	controllerZro_grp.matchPosition( name )
	controllerZro_grp.matchRotation( name )
	controller_ctrl.matchRotation( name )

	if needConstraint:
		# Constraint joint parent of controller
		controllerJnt_parCons = core.parentConstraint( controllerGmbl_ctrl , name )
		controllerJnt_parCons.name = part + 'Jnt_parCons'

		controllerJnt_parCons = core.scaleConstraint( controllerGmbl_ctrl , name )
		controllerJnt_parCons.name = part + 'Jnt_sacleCons'

	if parentTo:
		controllerZro_grp.parent( parentTo )

	print( 'Parent constraint : %s >>> %s ' %(controllerGmbl_ctrl, name))

	logger.AutoRigLogger.info('End of program')
	return controllerZro_grp.name  , controller_ctrl , controllerGmbl_ctrl.name 









# can list of all temp joint
# This is outdate move to add Rig module instead
def createFkRig(	nameSpace = ''  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'ear01LFT_tmpJnt','ear02LFT_tmpJnt'  ,'ear03LFT_tmpJnt')	,
					charScale = ''	, priorJnt = 'head01_bJnt' 			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = False	):

	

	part = name + side
	# Create main group
	rigGrp = core.Null()
	rigGrp.name = '%sFkRig%s_grp' % ( name , side )

	# Creatre empyt for append name
	ctrls = []
	jnts = []
	gmbls = []
	zGrps = []
	bJnts = []
	ofGrps = []

	# For loop in tmpJnt 
	for  num  in range( 0 , ( len( tmpJnt )  ) ):

		ctrl = core.Dag(     '%s%s%02dFk%s_ctrl'  %(nameSpace , name,( num +1),side)     )
		ctrl.nmCreateController( ctrlShape )
		ctrl.editCtrlShape( axis = charScale * 6.4 )
		ctrl.color = color
		
		gimbal = core.createGimbal( ctrl )
		tmp = core.Dag( tmpJnt[  num  ] )
		bJnt = jointAt( tmp )
		bJnt.name =  '%s%s%02dFk%s_bJnt'  %(nameSpace,	name,( num +1),side	)
		zroGrp,offsetGrp = zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%s%02dFk%sZro_grp'  %(nameSpace,	name,( num +1),side	)
		offsetGrp.name = '%s%s%02dFk%sOffset_grp'  %(nameSpace,	name,( num +1),side	)
		# parent joint to controller
		parCons = core.parentConstraint( gimbal , bJnt )
		parCons.name = '%s%s%02dFk%s_psCons'  %(nameSpace,	name,( num +1),side	)
		
		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		bJnts.append( bJnt )
		ofGrps.append( offsetGrp )
		
		if not  num  == 0:
			zroGrp.parent( gmbls[ num -1] )
			bJnt.parent( bJnts[ num -1] )
		else:
			rigGrp.maSnap(bJnts[0])
			zroGrp.parent( rigGrp )


	if priorJnt :
		rigGrp.parent( parentTo )
		bJnts[0].parent( priorJnt )

	# create local / world follwer arg #
	if localWorld:
		Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = orientLocalWorldCtrl( ctrls[0] , rigGrp.name , parentTo , zGrps[0] )
		Loc_grp.name = part + 'Local_grp'
		World_grp.name = part + 'World_grp'
		WorldGrp_orientCons.name = part + 'WorldGrp_orientCons'
		ZroGrp_orientCons.name = part + 'ZroGrp_orientCons'
		reverseNode_rev.name = part + 'ZroGrpOrientCons_rev'

	# Make curl controller 
	if curlCtrl:
		curl_ctrl = core.Dag('%s%s%s%s_ctrl'  %(nameSpace, name,'Curl',side))
		curl_ctrl.nmCreateController( ctrlShape )
		curl_ctrl.editCtrlShape( axis = charScale * 7.4 )
		curl_ctrl.color = 'white'
		zroGrpCurl = zeroGroupNam(curl_ctrl)
		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )
		curl_parCons = core.parentConstraint( bJnts[0],zroGrpCurl ,mo = False)
		# zroGrpCurl.maSnap(bJnts[0])
		curl_parCons.name = '%s%s%sFk%s_psCons'  %(nameSpace,	name,'Curl',side	)

		for eachObj in ofGrps:
			print( type( eachObj ))
			curl_ctrl.attr('rotate') >> eachObj.attr( 'rotate' )

		zroGrpCurl.parent( rigGrp )
		if priorJnt :
			mc.parentConstraint( priorJnt , rigGrp , name = '%sFkRig%s_psCons' % ( name,side )  ,mo = True )
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sFkRig%s_scaleCons' % ( name,side ) ,mo = True)


	# If having priorJnt but disable curl then just pa
	if priorJnt :
		if curlCtrl == False:
			mc.parentConstraint( priorJnt , rigGrp , name = '%sFkRig%s_psCons' % ( name,side )   ,mo = True)
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sFkRig%s_scaleCons' % ( name,side )   ,mo = True)


	return bJnt.name











def zeroGroup( obj = '' ):
	''' create zero group '''
	child = core.Dag( obj )
	grp = core.Null()
	grp.snap( child )
	child.parent( grp )

	return grp
	# If not retrun it will be can't use Dag object

def zeroGroupNam( obj = '' ):


	''' create zero group '''
	child = core.Dag( obj )
	if '_' in obj.name:
		rawNam = obj.name.split('_')


		if len(rawNam) == 2:
			name = rawNam[0]
		elif len(rawNam) == 3:
			name = rawNam[0] + '_' + rawNam[1] 
		elif len(rawNam) == 4:
			name = rawNam[0] + '_' + rawNam[1]  + '_' + rawNam[2]  
		else:
			mc.warning('element is too much')


		# name = obj.name.split('_')[0]
		# name = obj.name.split('_')


	else:
		name = obj.name

	grp = core.Null( name + 'Zro_grp' )
	grp.snap( child )
	child.parent(grp)

	return grp
	# If not retrun it will be can't use Dag object


#... add offset group
def zroNewGrpWithOffset( obj ):
	''' name naming '''

	child = core.Dag( obj )
	rawNam = child.name.split('_')

	name = core.check_name_style(name = child.name )[0]

	# #... extract name condition
	# if len(rawNam) == 2:
	# 		name = rawNam[0]
	# elif len(rawNam) == 3:
	# 		name = rawNam[0] + '_' + rawNam[1] 
	# elif len(rawNam) == 4:
	# 		name = rawNam[0] + '_' + rawNam[1]  + '_' + rawNam[2]  
	# else:
	# 	mc.warning('Too many element.')




	zro_grp = core.Null( name + 'Zro_grp' )
	offset_grp = core.Null( name + 'Offset_grp' )

	offset_grp.parent( zro_grp )
	zro_grp.snap( child )
	child.parent( offset_grp )

	return zro_grp, offset_grp



#... add offset group
def offset_locator_grp( obj ):

	child = core.Dag( obj )

	# rawNam = child.name.split('_')

	
	name = core.check_name_style(name = child.name)

	# #... extract name condition (need to update)
	# if len(rawNam) == 2:
	# 		name = rawNam[0]
	# elif len(rawNam) == 3:
	# 		name = rawNam[0] + '_' + rawNam[1] 
	# elif len(rawNam) == 4:
	# 		name = rawNam[0] + '_' + rawNam[1]  + '_' + rawNam[2]  
	# else:
	# 	mc.warning('Too many element.')

	zro_grp = core.Null( name[0] + 'Zro_grp' )
	offset_grp = core.Null( name[0] + 'Offset_grp' )
	offset_loc = core.Locator( name[0] + 'Offset_loc' )

	offset_grp.parent( zro_grp )
	zro_grp.snap( child )
	offset_loc.snap( child )
	
	offset_loc.parent( offset_grp )
	child.parent( offset_loc )
	
	return zro_grp, offset_grp



# Super Ultra Extreme Redundance function
def zroDoubleGrp( obj , zroNam = 'Zro_grp' , offNam = 'Offset_grp' ):
	''' create double grp '''

	child = core.Dag( obj )
	name = obj.name.split('_')
	

	zro_grp = core.Null( name[0] + zroNam )
	offset_grp = core.Null( name[0] + offNam )

	offset_grp.parent( zro_grp )
	zro_grp.snap( child )
	child.parent( offset_grp )

	return zro_grp,offset_grp





# add offset group
def zroGrpWithOffset( obj ):
	''' old naming '''

	child = core.Dag( obj )

	# mc.error(child.name)

	#... UPDATE for namming like 'R_upEyeLid01_GRP'
	if child.name.split('_')[0] == 'L' or child.name.split('_')[0] == 'R':
		if child.name.count('_') == 1:
			name = child.name
		elif child.name.count('_') > 1:
			parts  = child.name.split('_')
			name = '_'.join(parts[:-1])
	else:
		#... get rid of last prefix and underscore '_prefix'
		parts  = child.name.split('_')
		name = '_'.join(parts[:-1])





	zro_grp = core.Null( name + 'Zro_grp' )
	offset_grp = core.Null( name + 'Offset_grp' )

	offset_grp.parent( zro_grp )
	zro_grp.snap( child )
	child.parent( offset_grp )

	return zro_grp

# create joint at
def jointAt( obj ,orient = True):
	''' call Dag , Joint , snap '''
	target = core.Dag( obj )
	jnt = core.Joint()

	if orient:
		jnt.maSnap( target )
	else:# in case that want just to snap position
		jnt.maSnap( target ,pos = True , rot = False , scl = True)

	jnt.freeze( r = True , s = True )
	jnt.rotateOrder = target.rotateOrder

	jnt.attr('segmentScaleCompensate').value = 0

	
	'''if target.attr( 'radius' ).exists:
					# adjust the same radius of new joint
					#  'v' is visibility
			
					jnt.attr( 'radius' ).v = target.attr('radius').v'''
	mc.select( cl = True )

	return jnt




def nodeNaming( obj , charName = '' , elem = '' , side = '' ) :
	'''
	pkNodenameing
	Result:
	Auto-naming all attributes within the given object.

	find obj name and rename node  
	it will work when arg 'obj' is class object include all of component 

	'''
	# if having charname an not have '_'
	if charName and ( not '_' in charName ) :
		charName = '%s_' % charName

	# 'dir' is query list of member like dir in DOS ,is build in function of python
	'''
	example:
			'__weakref__',
			 '__doc__',
			 'anim_grp',
			 'charSize',
			 'findCharHeight',
			 'ikh_grp',
			 'jnt_grp',
			 'master_ctrl',
			 'offset_ctrl',
			 'placement_ctrl',
			 'rig_grp',
			 'skin_grp',
			 'still_grp'] 
	'''
	allAttrs = dir( obj )

	cnstrs = []
	
	# read the attr that create and rename
	for attr in allAttrs :

		# exclude base node such as '__weakref__' , '__doc__'
		if ( not '__' in attr ) and ( '_' in attr ) :

			# split 'rig' and 'grp' th each nodeName and nodeType
			# split is from standard
			print( attr )
			nodeName , nodeType = attr.split( '_' )
			print( nodeName , nodeType )
			# error because if more than 2

			# compose new name with given name 
			newName = '%s%s%s%s_%s' % ( charName , nodeName , elem , side , nodeType )

			# collect to cmd 
			# change node with object name
			# obj.still_grp.name = "still_grp"
			# example direct call
			# mainGroup.still_grp.name = "still_grp"
			# not sure .name can change name
			# may be it come from 'name property' in core
			
			print(  attr , newName )
			cmd = 'obj.%s.name = "%s"' % ( attr , newName )
			print( cmd )
			exec( cmd )
			'''
			 # if have any constraint in each newname
			 # do constraint
			if 'Constraint' in mc.nodeType( newName ) :
				cnstrs.append( newName )

	constrainAttributeNaming( cnstrs )'''

def orientLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , baseGrp = '' , bodyPart = None ):
	# Switching world and local object.
	locGrp = core.Null()
	worGrp = core.Null()
	locGrp.snap( baseGrp )
	worGrp.snap( baseGrp )
	# Store null1 null2
	oldLoc = str( locGrp.name )
	oldWor = str( worGrp.name )

	if bodyPart == None:
		# Assign new name
		locGrp.name =  'local'
		worGrp.name =  'world'
	else:
		locGrp.name = bodyPart +'_local'
		worGrp.name = bodyPart + '_world'



	# Orient constraint
	worldGrpCons = core.orientConstraint( worldObj , worGrp , mo = True )
	baseGrpBaseCons = core.orientConstraint(locGrp , worGrp , baseGrp )
	reverseNode_rev = core.Reverse()

	# Change name back to null1 null2 for return
	locGrp.name = oldLoc
	worGrp.name = oldWor

	controller = core.Dag( ctrl )
	print('This is CTRL:{0}'.format(ctrl))
	

	attr = 'localWorld'
	controller.addAttribute( ln = attr , k = True , min = 0 , max = 1 )
	controller.attr(attr) >> baseGrpBaseCons.attr('w1')
	# i = input , o = output
	controller.attr(attr) >> reverseNode_rev.attr('ix')
	reverseNode_rev.attr( 'ox' ) >> baseGrpBaseCons.attr( 'w0' )

	locGrp.parent( localObj )
	worGrp.parent( localObj )
	core.clearSel()

	return locGrp , worGrp , worldGrpCons , baseGrpBaseCons , reverseNode_rev



def parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , baseGrp = '' , bodyPart = None ,value = 0):

	# Switching world and local object.
	locGrp = core.Null()
	worGrp = core.Null()
	locGrp.snap( baseGrp )
	worGrp.snap( baseGrp )

	# Default name
	oldLoc = str( locGrp.name ) 
	oldWor = str( worGrp.name )

	if bodyPart == None:
		
		locGrp.name =  'local'
		worGrp.name =  'world'
	else:# Assign new name
		locGrp.name = bodyPart +'_local'
		worGrp.name = bodyPart + '_world'


	# Orient constraint
	worldGrpCons = core.parentConstraint( worldObj , worGrp , mo = True )
	baseGrpBaseCons = core.parentConstraint( locGrp , worGrp , baseGrp )
	reverseNode_rev = core.Reverse()

	# Return to Default name
	locGrp.name = oldLoc 
	worGrp.name = oldWor 



	controller = core.Dag( ctrl )

	attr = 'localWorld'
	controller.addAttribute( ln = attr , k = True , min = 0 , max = 1 )

	controller.attr(attr) >> baseGrpBaseCons.attr('w1')
	# i = input , o = output
	controller.attr(attr) >> reverseNode_rev.attr('ix')
	reverseNode_rev.attr( 'ox' ) >> baseGrpBaseCons.attr( 'w0' )

	controller.attr(attr).value = value
	
	locGrp.parent( localObj )
	worGrp.parent( localObj )
	core.clearSel()

	return locGrp , worGrp , worldGrpCons , baseGrpBaseCons , reverseNode_rev






def createConAtSelJnt(		charScale = 1	,
							ctrlShape = 'cube_ctrlShape'	,
							color = 'yellow'	,
							jntType = '_proxy_jnt'				):

	''' create controller at selected joint '''

	rawName = []
	nameLst = []
	


	selected = mc.ls(sl = True)

	if selected:
		for each in selected:
			print( each )
			rawName = each.split('_')[0]

			parent_jnt = rawName + jntType


			child_ctrl = core.Dag( rawName + '_ctrl' )
			child_ctrl.nmCreateController(ctrlShape)
			child_ctrl.editCtrlShape( axis = charScale * 1.2 )
			child_ctrl.color = color
			child_ctrl.rotateOrder = 'xzy'
			child_ctrl.hideArnoldNode()

			print( 'create gimbal controller')
			gimbal_ctrl = core.createGimbal( child_ctrl )
			gimbal_ctrl.hideArnoldNode()

			# Create zero group
			childZro_grp = zroNewGrpWithOffset( child_ctrl )

			# Match prosition
			childZro_grp.matchPosition( parent_jnt )
			childZro_grp.matchRotation( parent_jnt )

			# Making joint parent of controller
			joint_parCons = core.parentConstraint( gimbal_ctrl , parent_jnt )
			joint_parCons.name = rawName  + '_jntParCons'

			joint_ScalCons = core.scaleConstraint( gimbal_ctrl , parent_jnt )
			joint_ScalCons.name = rawName  + '_jntScalCons'
	else:
		print( 'Please select joint...')




def findCharScale(topJnt = 'head02_tmpJnt'):
	logger.AutoRigLogger.info('Start of %s function' %findCharScale.__name__)
	''' get charScale from topJoint height '''

	topGrp = 'top_grp'
	mc.group(em=1, n=topGrp)
	mc.matchTransform(topGrp,topJnt)
	cmHeight = mc.getAttr(topGrp+'.ty')
	mc.delete(topGrp)
	height = (cmHeight/100) # Already convert to meter
	charScale = (	"{:.{}f}".format(height,2)	)

	logger.AutoRigLogger.info(  'Character Scale is >>>>>>>>> ' + charScale )
	# charScale = float(charScale)
	logger.AutoRigLogger.info('End of findCharScale function')
	print('\n\n\n\n\n')
	return float(charScale)



#--------------------------------------------some useful tool--------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
def copyAttr():
	#clear data container first
	tmpAttr = {}
	ctrl = mc.ls(sl=True)
	if len(ctrl) == 1:
		if ctrl[0].rpartition('_')[2] == 'Ctrl':
			for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']:
				if mc.getAttr(ctrl[0] + '.' + attr, se=True):
					tmpAttr[attr] = mc.getAttr(ctrl[0] + '.' + attr)

			UDAttrs = mc.listAttr(ctrl[0], ud=True)
			if UDAttrs:
				for UDAttr in UDAttrs:                 
					if mc.getAttr(ctrl[0] + '.' + UDAttr, se=True):                                             
						ValueType = mc.addAttr(ctrl[0] + '.' + UDAttr, q=True, dt=True)[0]                       
						if ValueType != 'string':
							tmpAttr[UDAttr] = mc.getAttr(ctrl[0] + '.' + UDAttr)

			print( tmpAttr )

def pasteAttr():
	if tmpAttr:
		ctrls = mc.ls(sl=True)
		for ctrl in ctrls:
			if ctrl.rpartition('_')[2] == 'Ctrl':
				attrs = tmpAttr.keys()
				for attr in attrs:
					if mc.objExists(ctrl + '.' + attr):
						if mc.getAttr(ctrl + '.' + attr, se=True):
							mc.setAttr(ctrl + '.' + attr, tmpAttr[attr])

def deleteKey():
	ctrls = mc.ls(sl=True)

	if ctrls:
		try:
			mel.eval('timeSliderClearKey')
		except:
			return False

#--------------------------------------------IKFK SWITCH V3 --------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def ikfkSwitchV4( selCtrl =  '' ):

	# naming
	stick = selCtrl
	# get Jnt name
	upJnt = mc.listConnections( stick + '.' + 'upJnt' )[0]
	midJnt = mc.listConnections( stick + '.' + 'midJnt' )[0]
	lowJnt = mc.listConnections( stick + '.' + 'lowJnt' )[0]

	if mc.objExists(stick + '.' + 'ballJnt'):
		ballJnt = mc.listConnections( stick + '.' + 'ballJnt' )[0]
	if mc.objExists(stick + '.' + 'kunckJnt'):
		kunckJnt = mc.listConnections( stick + '.' + 'kunckJnt' )[0]
	if mc.objExists(stick + '.' + 'toeFkJnt'): # toeFkJnt is the fk joint that in fkJnt set to refer to position of IK that want to aim
		toeJnt = mc.listConnections( stick + '.' + 'toeFkJnt' )[0]

	# get Ctrl name
	upFkCtrl = mc.listConnections( stick + '.' + 'upFkCtrl' )[0]
	midFkCtrl = mc.listConnections( stick + '.' + 'midFkCtrl' )[0]
	lowFkCtrl = mc.listConnections( stick + '.' + 'lowFkCtrl' )[0]
	if mc.objExists(stick + '.' + 'ballFkCtrl'):
		ballFkCtrl = mc.listConnections( stick + '.' + 'ballFkCtrl' )[0]
	if mc.objExists(stick + '.' + 'kunckFkCtrl'):
		kunckFkCtrl = mc.listConnections( stick + '.' + 'kunckFkCtrl' )[0]
	if mc.objExists(stick + '.' + 'toeFkCtrl'):
		toeFkCtrl = mc.listConnections( stick + '.' + 'toeFkCtrl' )[0]

	# get Special thing
	region = mc.getAttr( stick + '.' + 'region' )
	pov = mc.listConnections( stick + '.' + 'pov' )[0]
	ikCtrl = mc.listConnections( stick + '.' + 'ikCtrl' )[0]
	ikOffset = mc.listConnections( stick + '.' + 'offset' )[0]
	ikfkAttr = stick + '.FK_IK'
	ikValue = 1
	fkValue = 0
	pvAxisDic = {"arm": "-z", "leg": "z", "frontLeg": "-z", "backLeg": "z"}
	pvAxis = pvAxisDic[str(region)]

	# leg
	if mc.objExists( stick + '.' + 'location' ):

		getPos = mc.getAttr( stick + '.' + 'location' )
		position = str(getPos)
	# ----------- FUNCTION Fkctrl to Ikctrl
	if mc.getAttr(ikfkAttr) == ikValue: # bJnt ---> FkCtrl

		print( '( snap Fkctrl to Ikctrl : {0} )'.format(region) )

		# BASE up - mid - low
		jnts = [upJnt, midJnt, lowJnt]
		fkCtrls = [upFkCtrl, midFkCtrl, lowFkCtrl]

		# ------------------------------------------------------ Foot and below -----------------------------------------------#
		# add foot if exists
		if mc.objExists(stick + '.' + 'ballJnt'):
			jnts.extend([ballJnt])
			fkCtrls.extend([ballFkCtrl])
			# add toe if exists
			if mc.objExists(stick + '.' + 'toeJnt'):
				jnts.extend([toeJnt])
				fkCtrls.extend([toeFkCtrl])
				# add kunck if exists
				if mc.objExists(stick + '.' + 'kunckJnt'):
					jnts.extend([kunckJnt])
					fkCtrls.extend([kunckFkCtrl])

		poss = []
		oris = []
		print( jnts )
		for jnt in jnts:
			pos = mc.xform( jnt, q=True, t=True, ws=True)
			ori = mc.xform( jnt, q=True, ro=True, ws=True)
			poss.append(pos)
			oris.append(ori)
		
		#mc.setAttr( ikfkAttr, fkValue) # big Change

		for i, ctrl in enumerate(fkCtrls):
			if mc.objExists(ctrl):
				mc.xform(ctrl, t=poss[i], ro=oris[i], ws=True, a=True)


	# ----------- FUNCTION Fkctrl to Ikctrl
	# HARD STUFF ------------------------------------------------------------------------------------
	elif mc.getAttr( ikfkAttr) == fkValue:   # bJnt ---> FK
		print( '( snap Ikctrl to Fkctrl : {0} )'.format(region))

		if region == 'leg':
			if position == 'foot':
				ikNowPos = ballJnt
			elif position == 'ankle':
				ikNowPos = lowJnt
			else:
				ikNowPos = lowJnt
		else:
			ikNowPos = ikOffset

		ikPos = mc.xform( ikNowPos, q=True, t=True, ws=True) #if alias in ["HindLeg"] else mc.xform(lowJnt, q=True, t=True, ws=True) 
		ikOri = mc.xform( ikOffset, q=True, ro=True, ws=True) #if alias in ["HindLeg"] else mc.xform(lowJnt, q=True, ro=True, ws=True)
		pvPos = findPV( upJnt, midJnt, lowJnt, pvAxis) 


		if region in ["leg", "frontLeg", "backLeg"]:

			footMX = mc.xform( ballJnt, q=True, m=True, ws=True)
			upVec = footMX[4:7]
			if 'LFT' in selCtrl:
				print( 'left ctrl')
				upVec = core.vMultiply(upVec, -1)

			ballPos = mc.xform( ballJnt, q=True, t=True, ws=True)
			toePos = mc.xform( toeJnt, q=True, t=True, ws=True)

			aimVec = core.vPlus(ballPos, toePos, "-")
			#toeOri = core.vectorToAngle(aimVec, upVec=upVec, sideVec=None, aimAxis="z", upAxis="x", sideAxis=None)

		#get foot ik's orientation
		if region in ["backLeg"]:
			lowMX = mc.xform( lowJnt, q=True, m=True, ws=True)
			upVec = lowMX[4:7]
			if 'LFT' in selCtrl:
				upVec = core.vMultiply(upVec, -1)
			lowPos = mc.xform( lowJnt, q=True, t=True, ws=True)
			aimVec = core.vPlus(lowPos, ballPos, "-")
			#footOri = core.vectorToAngle(aimVec, upVec=upVec, sideVec=None, aimAxis="z", upAxis="x", sideAxis=None)

		#mc.setAttr( ikfkAttr, ikValue) # big change
		
		mc.xform( ikCtrl, t=ikPos, ro=ikOri, ws=True, a=True)
		mc.xform( pov, t=pvPos, ws=True, a=True)

		if region in ["leg", "frontLeg", "backLeg"]:
			#mc.xform( ikCtrl, ro=ikOri, a=True, ws=True)
			#mc.xform( toeIkCtrl, ro=toeOri, a=True, ws=True)

			if region in ["hindLeg"]:
				logger.AutoRigLogger.info("I'm A DOG")
				#mc.xform( footIkCtrl, ro=footOri, a=True, ws=True)
			else:
				#mc.xform( footIkCtrl, ro=(0, 0, 0), a=True, os=True)
				logger.AutoRigLogger.info("I'm A Man")

		if region in ["frontLeg", "backLeg"]:
			if mc.objExists( kunckIKCtrl):
				mc.setAttr("{0}.r".format( kunckIKCtrl), 0, 0, 0, type="double3")

			if mc.objExists(toeSubIKCtrl):
				mc.setAttr("{0}.r".format( toeSubIKCtrl), 0, 0, 0, type="double3")
		## ------------------------------------------------HOLY CRAP------------------------------------------------------------##

	return True

'''
def snapFromSel():
	sel = mc.ls(sl=True)
	for each in sel:
		ikfkSwitchV4( selCtrl =  each)
'''


def ikfkSwitch( selCtrl , namespace="", longAlias = "" , item=None):
	
	longAlias = selCtrl
	firstName = longAlias.split("_")[0]
	side = firstName[-3:]
	alias = firstName.split("Stick")[0]
	left = "LFT"
	right = "RGT"
	aliasListDic = {"arm": ["upperArm", "lowerArm", "hand","elbow"], 
					"leg": ["upperLeg", "lowerLeg", "ankle", "ball"],
					"foreLeg": ["hip", "knee", "ankle", "foot", "knuckle", "toe"], 
					"hindLeg": ["hip", "knee", "ankle", "foot", "knuckle", "toe"]}

	aliasList = aliasListDic[alias]


	ikCtrl = "{0}Ik{1}_ctrl".format(aliasList[2],side)
	#ikNull = "{0}{1}_bJnt".format(aliasList[2],side)
	ikNull = "{0}Offset{1}_null".format(alias,side)  # DodeOldStyle
	
	if alias == "arm":
		pvCtrl = "{0}{1}_ctrl".format(aliasList[3],side)

	elif alias == "leg":
		pvCtrl = "knee{0}_ctrl".format(side)

	else:
		pvCtrl = "{0}{1}_ctrl".format(aliasList[3],side)

	upFkCtrl = "{0}Fk{1}_ctrl".format(aliasList[0], side)
	midFkCtrl = "{0}Fk{1}_ctrl".format(aliasList[1], side)
	lowFkCtrl = "{0}Fk{1}_ctrl".format(aliasList[2], side)

	upJnt = "{0}{1}_bJnt".format(aliasList[0],side)
	midJnt = "{0}{1}_bJnt".format(aliasList[1],side)
	lowJnt = "{0}{1}_bJnt".format(aliasList[2],side)

	if alias in ["leg", "foreLeg", "hindLeg"]:
		system = "leg"
		footJnt = "{0}{1}_bJnt".format(aliasList[3], side)
		toeJnt = "{0}{1}_bJnt".format(aliasList[-1], side)
		
		footIkCtrl = "{0}Ik{1}_ctrl".format(aliasList[2], side)
		footFkCtrl = "{0}Fk{1}_ctrl".format(aliasList[3], side)
		
		toeIkCtrl = "{0}Ik{1}_ctrl".format(aliasList[-1], side)
		toeFkCtrl = "{0}Fk{1}_ctrl".format(aliasList[-1], side)


		if alias in ["foreLeg", "hindLeg"]:
			system = "leg"
			kunckJnt = "{0}{1}_bJnt".format(aliasList[4], side)
			kunckIKCtrl = "{0}Ik{1}_ctrl".format(aliasList[4], side)
			kunckFKCtrl = "{0}Fk{1}_ctrl".format(liasList[4], side)
			
			toeSubIKCtrl = "{0}Ik_Sub{1}ctrl".format(aliasList[-1], side)

	ikfkCtrlAttr = selCtrl + '.FK_IK'  # exp. armStickLFT_ctrl 
	fkValue = 0
	ikValue = 1

	pvAxisDic = {"arm": "-z", "leg": "z", "foreLeg": "-z", "hindLeg": "z"}
	pvAxis = pvAxisDic[alias]
	
	'''
	in my setup right side fk ctrls have (180, 0, 0) <<< ( we need to change it to 0,180,0 )
	ik ctrls' offset is stored in their UD attributes
	'''

	if mc.getAttr(namespace+ikfkCtrlAttr) == ikValue: # IK -----> FK


		jnts = [upJnt, midJnt, lowJnt]
		fkCtrls = [upFkCtrl, midFkCtrl, lowFkCtrl]
		
		if alias in ["leg"]:
			jnts.extend([footJnt])#, toeJnt])
			fkCtrls.extend([footFkCtrl])#, toeFkCtrl])

		if alias in ["foreLeg", "hindLeg"]:
			jnts.extend([footJnt, kunckJnt, toeJnt])
			fkCtrls.extend([footFkCtrl, kunckFKCtrl, toeFkCtrl])

		poss = []
		oris = []
		for jnt in jnts:
			pos = mc.xform(namespace+jnt, q=True, t=True, ws=True)
			ori = mc.xform(namespace+jnt, q=True, ro=True, ws=True)
			poss.append(pos)
			oris.append(ori)
		
		mc.setAttr(namespace+ikfkCtrlAttr, fkValue)

		for i, ctrl in enumerate(fkCtrls):
			if mc.objExists(namespace+ctrl):
				mc.xform(namespace+ctrl, t=poss[i], ro=oris[i], ws=True, a=True)
				#if side == right:
					#print( "I'm right")
					#mc.xform(ctrl, ro=(180, 0, 0), os=True, r=True)  # Studing here


	#--------------------------------------------	FIND IK FROM FK NA JA	--------------------------------------------#


	elif mc.getAttr(namespace+ikfkCtrlAttr) == fkValue:   # FK -----> IK
		print( 'do switch from fk to ik for {0} :)'.format(longAlias) )
		#item.setText("{0}:-->IK".format(longAlias))

		# NOTE THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		locName = namespace + 'rig_grp.legik' + side + 'location'
		if mc.objExists( locName ):
			legLoc = mc.getAttr( locName )
		if alias == 'leg':
			if legLoc == 'foot':
				ikNowPos = footJnt
			elif legLoc == 'ankle':
				ikNowPos = ikNull
			else:
				ikNowPos = ikNull
		else:
			ikNowPos = ikNull

		ikPos = mc.xform(namespace+ikNowPos, q=True, t=True, ws=True) #if alias in ["HindLeg"] else mc.xform(lowJnt, q=True, t=True, ws=True) 
		ikOri = mc.xform(namespace+ikNull, q=True, ro=True, ws=True) #if alias in ["HindLeg"] else mc.xform(lowJnt, q=True, ro=True, ws=True)
		pvPos = findPV(namespace+upJnt, namespace+midJnt, namespace+lowJnt, pvAxis) 

		## ------------------------------------------------HOLY CRAP------------------------------------------------------------##
		# DODE DONT UNDERSTAND    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

		if alias in ["leg", "foreLeg", "hindLeg"]:
			footMX = mc.xform(namespace+footJnt, q=True, m=True, ws=True)
			print('footMX')
			print(footMX)
			upVec = footMX[4:7]
			print('upVector')
			print(upVec)

			if side == left:
				upVec = core.vMultiply(upVec, -1)

			footPos = mc.xform(namespace+footJnt, q=True, t=True, ws=True)
			toePos = mc.xform(namespace+toeJnt, q=True, t=True, ws=True)

			aimVec = core.vPlus(footPos, toePos, "-")
			#toeOri = core.vectorToAngle(aimVec, upVec=upVec, sideVec=None, aimAxis="z", upAxis="x", sideAxis=None)

		#get foot ik's orientation
		if alias in ["hindLeg"]:
			lowMX = mc.xform(namespace+lowJnt, q=True, m=True, ws=True)
			upVec = lowMX[4:7]
			if side == left:
				upVec = core.vMultiply(upVec, -1)
			lowPos = mc.xform(namespace+lowJnt, q=True, t=True, ws=True)
			aimVec = core.vPlus(lowPos, footPos, "-")
			#footOri = core.vectorToAngle(aimVec, upVec=upVec, sideVec=None, aimAxis="z", upAxis="x", sideAxis=None)

		mc.setAttr(namespace+ikfkCtrlAttr, ikValue)
		
		mc.xform(namespace+ikCtrl, t=ikPos, ro=ikOri, ws=True, a=True)
		mc.xform(namespace+pvCtrl, t=pvPos, ws=True, a=True)

		if alias in ["leg", "foreLeg", "hindLeg"]:
			#mc.xform(namespace+ikCtrl, ro=ikOri, a=True, ws=True)
			#mc.xform(namespace+toeIkCtrl, ro=toeOri, a=True, ws=True)

			if alias in ["hindLeg"]:
				print("I'm A DOG")
				#mc.xform(namespace+footIkCtrl, ro=footOri, a=True, ws=True)
			else:
				#mc.xform(namespace+footIkCtrl, ro=(0, 0, 0), a=True, os=True)
				print("I'm A GOD")

		if alias in ["foreLeg", "hindLeg"]:
			if mc.objExists(namespace+kunckIKCtrl):
				mc.setAttr("{0}.r".format(namespace+kunckIKCtrl), 0, 0, 0, type="double3")

			if mc.objExists(toeSubIKCtrl):
				mc.setAttr("{0}.r".format(namespace+toeSubIKCtrl), 0, 0, 0, type="double3")
		## ------------------------------------------------HOLY CRAP------------------------------------------------------------##

	return True
	


def findPV( obj1, obj2, obj3, axis, scale=10): ### We found Pole Vector for you. NICE !!??
	neg = 1
	if axis[0] == '-':
		neg = -1
		axis = axis[1]

	row = {'x': 0, 'y': 1, 'z': 2}

	P = [mc.xform(obj, q=True, t=True, ws=True) for obj in [obj1, obj2, obj3]]

	V0 = core.vPlus(P[2], P[0], '-')
	V1 = core.vPlus(P[1], P[0], '-')
	w = core.vDot(V0, V1) / core.vDot(V0, V0)
	Vp = core.vMultiply(V0, w)
	Pp = core.vPlus(P[0], Vp, '+') 

	if 1 - core.vDot(V0, V1)/(core.vLength(V0)*core.vLength(V1)) < 0.0001:
		M16 = mc.xform(obj1, q=True, matrix=True, ws=True)
		M3x3 = []
		for i in range(3):
			M3x3.append([M16[i*4], M16[i*4+1], M16[i*4+2]])
		Vperp = core.vMultiply(M3x3[row[axis]], neg)
	else:
		Vperp = core.vPlus(P[1], Pp, '-')

	Vperp = core.vNormal(Vperp)
	Vperp = core.vMultiply(Vperp, scale)
	V0 = core.vMultiply(V0, 0.5)
	Pmid = core.vPlus(P[0], V0, '+')
	pvPos = core.vPlus(Pmid, Vperp, '+')

	return pvPos


def addSpace( nameSpace = '' ,	giveStick =  'armStickLFT_ctrl'  , spaces = ['world'] , piors = ['placement_ctrl']):

	# head group
	headGrp = 'space_IK_grp'
	if mc.objExists(headGrp) == True:
		logger.AutoRigLogger.info( 'We already have' + headGrp)
	elif mc.objExists(headGrp) == False:
		mc.group(n= headGrp, em=1)
		mc.parent(headGrp,'ikh_grp')


	stick = giveStick
	side = (stick.split('_')[0])[-3:]
	sys = mc.getAttr( stick + '.' + 'region' )
	ikCtrl = mc.listConnections( stick + '.' + 'ikCtrl' )[0]
	ikGrp = (ikCtrl.split('_')[0]) + 'Zro_grp'

	# emty name
	eName = ''
	for e in range(len(spaces)):
		if e == (len(spaces)-1):
			addSpaceName = spaces[e]
			eName += addSpaceName
		else:
			addSpaceName = spaces[e] + ':'
			eName += addSpaceName

	mc.addAttr( ikCtrl, longName = "space", at = 'enum', keyable=True , en = eName)

	for i in range(len(spaces)):
		# Create Name
		localGrp = spaces[i]
		name = nameSpace + sys + side + '_IK_' + localGrp
		master = piors[i]
		grp = name + '_grp'
		con = name + '_con'



		#pCon = ikGrp + '_parCons'
		#pConAttr = pCon + '.' + grp + 'W%d' %i

		# Function
		mc.group(n=grp, em=1)
		mc.parent(grp,headGrp)

		# snap
		dc.allMat( grp, ikGrp )
		# master_bJnt -> masterGrp
		dc.parCon( master, grp, mo=1, w=1 )
		# masterGrp -> ikGrp
		pCon = dc.parCon( grp, ikGrp, mo=1, w=0 )
		# name conAttr
		pConAttr = pCon + '.' + grp + 'W%d' %i
		# Create Node and connect
		mc.createNode('condition',n=con)
		
		mc.setAttr(con + '.firstTerm',i)
		mc.setAttr(con + '.colorIfTrueR',1)
		mc.setAttr(con + '.colorIfFalseR',0)
		mc.connectAttr(ikCtrl + '.space' ,con + '.secondTerm')
		mc.connectAttr(con + '.outColor.outColorR', pConAttr)


	print( ' ')
	print( ' ')
	print( ' >>>>>>>>>  Now ' + sys + ' have there own space THANK YOU RIGGER<<<<<<<<<<')
	print( ' ')
	print( ' ')
	print( ' ')



def fkChainFolow( 	nameSpace = '',
					tmpJnt = ['upLegLFT_tmpJnt', 'midLegLFT_tmpJnt'], 
					ctrl_grp = 'ctrl_grp'  ,
					parentTo = '' ,
					charScale = ''	):

	# head grp create
	findChainName = tmpJnt[0].split('_')[0]
	chainHead = findChainName + 'Rig_grp'
	chainHeadRig_grp = core.Null( chainHead )
	chainHeadRig_grp.parent( ctrl_grp )
	side = findChainName[-3:] 

	

	for i in range(len(tmpJnt)):
		name = nameSpace + tmpJnt[i].split('_')[0]
		ctrl = name + '_ctrl'
		bJnt = name + '_bJnt'
		

		# create joint
		chain = core.Dag( tmpJnt[i] )
		chain_bJnt = jointAt( chain )
		chain_bJnt.name = nameSpace + bJnt

		# create ctrl
		chain_ctrl = core.Dag( name + '_ctrl' )
		chain_ctrl.nmCreateController('circle_ctrlShape')
		chain_ctrl.editCtrlShape( axis = charScale * 3 )

		chainOff_grp = zeroGroup( chain_ctrl )
		chainOff_grp.name = name + 'Offset_grp'

		chainZro_grp = zeroGroup( chainOff_grp )
		chainZro_grp.name = name + 'Zro_grp'

		chainGmbl_ctrl = core.createGimbal( chain_ctrl )

		# parenting and positioning
		chainZro_grp.matchPosition( chain_bJnt )
		chainZro_grp.matchRotation( chain_bJnt )
		chain_ctrl.freeze()

		# color adjustment
		if side == 'LFT':
			print( 'LFT')
			chain_ctrl.color = 'red'
		elif side == 'FNT':
			print( 'FNT')
			chain_ctrl.color = 'yellow'
		elif side == 'CNT':
			print( 'CNT')
			chain_ctrl.color = 'yellow'
		elif side == 'BCK':
			print( 'BCK')
			chain_ctrl.color = 'yellow'
		elif side == 'RGT':
			print( 'RGT')
			chain_ctrl.color = 'blue'
		else:
			print( 'Normal')
			chain_ctrl.color = 'yellow' 

		# parent to upJnt and upCtrl
		if i == 0:	

			condition = name + '_con'
			
			chain_bJnt.parent( parentTo )
			chainZro_grp.parent( chainHeadRig_grp )
			dc.parCon( parentTo, chainZro_grp.name )

			# addAttr & createNode
			mc.addAttr( chain_ctrl.name, sn = 'follow' ,ln = 'follow', min = 0, max = 1, dv = 0, k = True)
			mc.createNode( 'condition', name = name + '_con')
			# set
			mc.setAttr( condition + '.secondTerm', 1)
			mc.setAttr( condition + '.colorIfFalseR', 0 )
			mc.setAttr( condition + '.colorIfFalseG', 0 )
			mc.setAttr( condition + '.colorIfFalseB', 0 )
			# connect
			mc.connectAttr( chain_ctrl.name + '.follow', condition + '.firstTerm' )
			mc.connectAttr( chain_ctrl.name + '.rotate', condition + '.colorIfTrue' )


		else:
			up_name = tmpJnt[i-1].split('_')[0]
			up_bJnt = up_name + '_bJnt'
			up_ctrl = up_name + '_ctrl'
			# parent 
			chain_bJnt.parent( up_bJnt )
			chainZro_grp.parent( up_ctrl )
			# connect
			mc.connectAttr( condition + '.outColor', chainOff_grp.name + '.rotate' )

		# do parent Constrain
		dc.parCon( chain_ctrl.name, chain_bJnt.name )
		dc.sclCon( chain_ctrl.name, chain_bJnt.name )

	return chainHeadRig_grp.name

# EXAMPLE #
'''	
fkChainFolow( 		nameSpace = '',
					tmpJnt = ['dragonTail01_tmpJnt', 'dragonTail02_tmpJnt', 'dragonTail03_tmpJnt', 'dragonTail04_tmpJnt', 'dragonTail05_tmpJnt' , 'dragonTail06_tmpJnt']	,
					ctrl_grp = 'ctrl_grp', parentTo = 'hip_bJnt', charScale = 1)
'''





def cleanForExport(	 ): # bake root delete key and export

	if mc.objExists('Root'):
		logger.AutoRigLogger.info('Root')
		root = 'Root'
	elif mc.objExists('root'):
		logger.AutoRigLogger.info('root')
		root = 'root'
		
	mc.select( root, hi = True )
	sel = mc.ls(sl=True)
	#sel = mc.ls( sl = True )

	mc.currentTime(0)
	mc.setKeyframe()

	if mc.objExists('rig_grp'):
		mc.delete( 'rig_grp' )
		print('Deleting rig_grp...')
		
	mc.select( cl = True )

	mc.delete( timeAnimationCurves = True ,staticChannels = True )
	print('Deleting all Keys')
	print( ' ')
	print( ' ')
	print('Rig Ready For Export')

	#example
	#from function.rigging.autoRig.base import rigTools
	#reload( rigTools )
	#dc.cleanForExport()



# create new jnt at the position of tmp Jnt
def duplicateTmpJnt(	nameSpace = '', name = 'tail', side = '',ext='bJnt'	,
						tmpJnt = 	( 	'tail01_tmpJnt'	,
											'tail02_tmpJnt' ,
											'tail03_tmpJnt' ,
											'tail04_tmpJnt' ,
											'tail05_tmpJnt' ,
											'tail06_tmpJnt' ,
											'tail07_tmpJnt' ,
											'tail08_tmpJnt'	
											)
				):


	
	

	jnts = []
	bJnts = []

	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		tmp = core.Dag( tmpJnt[  num  ] )
		bJnt = jointAt( tmp )
		bJnt.name =  '%s%s%02d%s_%s'  %(nameSpace, name, (num +1), side ,ext	)

		jnts.append( tmpJnt[ num ] )
		bJnts.append( bJnt )


		if not  num  == 0:
			bJnt.parent( bJnts[ num -1] )

	return bJnts