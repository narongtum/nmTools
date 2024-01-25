# latest Use this (not in Rig tools)



from function.framework.reloadWrapper import reloadWrapper as reload

import pymel.core as pm

# need locator to pinpoint location


'''
Thank to : Chris Lesage, https://rigmarolestudio.com
This script is pin locator to nurbs this method prevend from flipping
https://tech-artists.org/t/flipping-follicles-in-ribbon-ik/11022/10?u=clesage


A script snippet for pinning an object to a nurbs surface in Autodesk Maya.
This results in a surface pin, much like a follicle, but I've found
follicles to be less stable, sometimes flipping since Maya 2018 or so. 
Details in this thread:
https://tech-artists.org/t/flipping-follicles-in-ribbon-ik/11022/10?u=clesage

sourceObj is an optional parameter. If you pass a PyNode object, it will place the "follicle"
as close to the object as possible. Otherwise, you can specify U and V coordinates.
'''






"""
from function.rigging.autoRig.addRig import pinLocatorToSurfac as pls
reload(pls)

 pls.pin_locator_surface(	# need pxy nrb to drive locator
							nurbs = 'glue_nrb',
							region = 'ribCage',
							side = '',
							source_loc = ('strapALFT_loc','strapARGT_loc'),
							locator_scale = 1
						)

"""



import maya.cmds as mc

from function.pipeline import logger 
reload(logger)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.autoRig.base import core
reload(core)

class PinLogger(logger.MayaLogger):
	LOGGER_NAME = "pin_locator_surface"

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

# TODO : create proxy joint follow locator that create
# no need to specified UV

#... this is redundance with rigTools (Use this instead)
#... create locator at specified uv coordinate
#... from Chris Lesage (Rigmarole Studio)

# NEED NURB ONLY
def pin_locator_surface(	# need pxy nrb to drive locator
							nurbs = 'glue_nrb',
							region = 'ribCage',
							side = '',
							source_loc = ('strapALFT_loc','strapARGT_loc'),
							locator_scale = 1,
							creJnt = False , suffixJnt = 'bJnt',
							creCtrl = False , ctrlShape = 'circle_ctrlShape',
							snapAtEnd = False,
							priorJnt = 'hip_bJnt',
							scale = 2
							):

	# need locator to guide flc

	jnt_list = []
	ctrl_list = []

	if not source_loc:
		mc.error('Need locator to pinpoint location.')

	# make nrb to object
	oNurbs = pm.PyNode(nurbs) 

	# if string convert to obj
	if type(oNurbs) == str and pm.objExists(oNurbs):
		oNurbs = pm.PyNode(oNurbs) 
	# if object already pass
	if type(oNurbs) == pm.nodetypes.Transform:
		pass
	# i dunno 
	elif type(oNurbs) == pm.nodetypes.NurbsSurface:
		oNurbs = oNurbs.getTransform()
	elif type(oNurbs) == list:
		pm.warning('Specify a NurbsSurface, not a list.')
		#return False
	else:
		pm.warning('Invalid surface object specified.')
		#return False



	locator_list=[]


	#for each in source_loc:

	for num in range(0,(len(source_loc))):
		print (source_loc[num])
		each = source_loc[num]


		pointOnSurface = pm.createNode( 'pointOnSurfaceInfo', name = '{}{:02d}{}_poiInfo'.format(region,num+1,side) )
		# pointOnSurface = pm.createNode( 'pointOnSurfaceInfo', name = region + num + side +'_poiInfo' )
		oNurbs.getShape().worldSpace.connect(pointOnSurface.inputSurface) # conntet from oNurbs

		# follicles remap from 0-1, but closestPointOnSurface must take minMaxRangeV into account
		paramLengthU = oNurbs.getShape().minMaxRangeU.get()
		paramLengthV = oNurbs.getShape().minMaxRangeV.get()



		sourceObj = pm.PyNode(each)
		# Place the follicle at the position of the sourceObj
		# Otherwise use the UV coordinates passed in the function
		if isinstance(sourceObj, str) and pm.objExists(sourceObj):
			sourceObj = pm.PyNode(sourceObj) # if sourceObj is str make an object
		if isinstance(sourceObj, pm.nodetypes.Transform):
			pass
		elif isinstance(sourceObj, pm.nodetypes.Shape):
			sourceObj = sourceObj.getTransform()
		elif type(sourceObj) == list:
			pm.warning('sourceObj should be a transform, not a list.')
			#return False
		else:
			pm.warning('Invalid sourceObj specified.')
			#return False  

		oNode = pm.createNode('closestPointOnSurface', name = '{}{:02d}{}_closePInfo'.format(region,num+1,side) )
		oNurbs.worldSpace.connect(oNode.inputSurface, force=True)
		oNode.inPosition.set(sourceObj.getTranslation(space='world'))# get world position
		uPos = oNode.parameterU.get() # copy value 
		vPos = oNode.parameterV.get() # copy value 
		pm.delete(oNode) # delete no need anymore

		pName = each
		pm.delete(each)
		# pName = '{}{:02d}glue{}_loc'.format(region,num+1,side) 

		# pName = '{}_loc#'.format(region + num + side)
		result = pm.spaceLocator(n=pName).getShape()

		result.addAttr('parameterU', at='double', keyable=True, dv=uPos)
		result.addAttr('parameterV', at='double', keyable=True, dv=vPos)

		# set locator scale
		result.setAttr('localScaleX', locator_scale)
		result.setAttr('localScaleY', locator_scale)
		result.setAttr('localScaleZ', locator_scale)


		# set min and max ranges for the follicle along the UV limits.
		result.parameterU.setMin(paramLengthU[0])
		result.parameterV.setMin(paramLengthV[0])
		result.parameterU.setMax(paramLengthU[1])
		result.parameterV.setMax(paramLengthV[1])
		result.parameterU.connect(pointOnSurface.parameterU)
		result.parameterV.connect(pointOnSurface.parameterV)

		# assign 'white color'
		result.setAttr('overrideEnabled', 1)
		result.setAttr('overrideColor', 16)






		# Compose a 4x4 matrix
		mtx = pm.createNode('fourByFourMatrix',name ='{}{:02d}{}_fbfMat'.format(region,num+1,side)  )
		outMatrix = pm.createNode('decomposeMatrix', name = '{}{:02d}{}_deCom'.format(region,num+1,side) )
		mtx.output.connect(outMatrix.inputMatrix)
		outMatrix.outputTranslate.connect(result.getTransform().translate)
		outMatrix.outputRotate.connect(result.getTransform().rotate)


		'''
		Thanks to kiaran at https://forums.cgsociety.org/t/rotations-by-surface-normal/1228039/4
		# Normalize these vectors
		[tanu.x, tanu.y, tanu.z, 0]
		[norm.x, norm.y, norm.z, 0]
		[tanv.x, tanv.y, tanv.z, 0]
		# World space position
		[pos.x, pos.y, pos.z, 1]
		'''

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

		locator_list.append(pName)
		# locator_list.reverse()

		# pm.delete(sourceObj)

		#... [ Update if use joint]
		#... create joint and parent under locator
		

		if creJnt:
			
			child_joint = core.Joint(scaleCompensate=False) #... not work why?
			child_joint.name = '{}{:02d}{}_{}'.format(region, num+1, side, suffixJnt)
			child_joint.maSnap( pName )
			#... no need to parent
			# child_joint.parent( pName )
			child_joint.freeze()
			# child_joint = mc.createNode('joint' , name =  )
			# child_joint = pm.createNode( 'joint', name = '{}{:02d}{}_jnt'.format(region,num+1,side) )
			child_joint.attr('segmentScaleCompensate').value = 0 #... work why?

			jnt_list.append(child_joint.name)
			print(jnt_list)

			#... Create controller
			gmbl_ctrl = adjust.creControllerFunc( 	selected = [each], scale = scale, ctrlShape = ctrlShape, color = 'yellow', 
							constraint = False, matrixConst = False, mo = False, translate=True, 
							rotate = True, scaleConstraint = True, rotateOrder = 'xzy', parentUnder = True)[2]

			ctrl_list.append(gmbl_ctrl)




			
		

			# child_joint = core.Joint()
			# child_joint.name = '{}{:02d}{}_{}'.format(region, num+1, side, suffixJnt)
			# child_joint.maSnap( pName )
			# child_joint.parent( gmbl_ctrl )
			# child_joint.freeze()



	# # # # # # # # # # # # # # # #
	# update function make constraint to controller
	# # # # # # # # # # # # # # # #

	#... 1. Parent joint to hierarchy
	if creJnt and snapAtEnd:	
		for num in range(len(jnt_list)):
			if num  != 0:
				mc.parent(jnt_list[num],jnt_list[num-1])
			else:
				continue

	

		#... 2. Parent it to prior joint that desinate
		mc.parent(jnt_list[0], priorJnt)

		#... 3. ParentConstraint from controller to joint
		print('\n')
		print(ctrl_list)
		print(jnt_list)
		print('\n')

		

		for num in range(len(jnt_list)):
			ctrl_to_jnt_parCons = core.parentConstraint( ctrl_list[num] , jnt_list[num] )
			ctrl_to_jnt_parCons.name = '{}{:02d}{}_parCons'.format(region,num+1,side)



		# mc.error('Ma tum tor tomorrow')



		

	PinLogger.info('Create {0} Locator glue Complete'.format(each))
	return locator_list








def gen_locator_surface( ribbon_nrb = '', numJoints = 3, side='',region ='generic',upPlana='z+',showInfo=False,charScale=1,ctrlShape = 'circle_ctrlShape'):
	# # # # # # # # # # # # # # # # # # # # 
	# same function as ribbon rig ext but no need locator guide just put numJoints to scarctter the value along the surface
	# result: generate locator at specified
	# # # # # # # # # # # # # # # # # # # #

	oNurbs = ribbon_nrb

	oNurbs = pm.PyNode(oNurbs)
	pointOnSurface = pm.createNode( 'pointOnSurfaceInfo', name = '{}_poiInfo'.format('temp') )
	oNurbs.getShape().worldSpace.connect(pointOnSurface.inputSurface) 
	paramLengthU = oNurbs.getShape().minMaxRangeU.get()
	paramLengthV = oNurbs.getShape().minMaxRangeV.get()
	pm.delete(pointOnSurface)



	# divide to equal cell
	uPos = paramLengthU[1]/2
	vPos = paramLengthV[1]/2
	# length is U
	length = paramLengthU[1]
	divide = numJoints+1
	distance =  float(length)/float(divide)


	uPos_cell_list = []
	for each in range (0 , divide ):
		if each == 0:
			pass
		else:
			uPos_cell_list.append( round(distance*each, 3) )


	# follicle grp
	flc_grp = core.Null( region +'Flc' + side +'_grp')
	# detail controller
	detail_grp = core.Null( region +'Detail' + side + '_grp')
	proxyJntList = []
	# start for loop
	for each in range (0 , numJoints ):

		num =  each + 1
		# Common name
		name =  region + '%02d'%num + side
		#       [region] + [Rbn] +     [01]   + [LFT]

		# using pin to surface to pin flc to desire UV cooordinate
		# TODO: want to move _pinToSurface to proper location
		flc_name = rigTools._pinToSurface(
						oNurbs = ribbon_nrb 	,
						side = side 				,
						region = region   ,
						uPos = uPos_cell_list[each] ,
						vPos = vPos 				,
						num = num)
		folicle = core.Dag(flc_name)
		# End of create folicle


		ribbon_jnt = core.Joint()
		ribbon_jnt.name = name + '_pxyJnt'
		ribbon_jnt.maSnap( folicle )


		if upPlana == 'z+':
			# should not set rotate before freeze
			ribbon_jnt.freeze()
			ribbon_jnt.setRotate( (-90,90,0) )
		elif upPlana == 'x+':
			ribbon_jnt.freeze()
			ribbon_jnt.setRotate( (0,180,0) )
		elif upPlana == 'z-':
			ribbon_jnt.freeze( translate= True,rotate= True,scale= True,normal= False,preserveNormals=True,jointOrient=False)
			ribbon_jnt.setRotate( (-90,90,0) )
			ribbon_jnt.freeze()
			

				
		
		
		# display axis
		ribbon_jnt.attr('displayLocalAxis').value = showInfo


		
		# Insert can delete if not work
		#ribbon_jnt.freeze()
		ribbon_jnt.attr('radius').value = 0.25
		ribbon_jnt.attr('overrideEnabled').value = 1
		# Make it gray
		ribbon_jnt.attr('overrideColor').value = 3
		ribbon_jnt.attr('v').value = showInfo

		ribbon_ctrl = core.Dag( name + '_ctrl' )
		ribbon_ctrl.nmCreateController(ctrlShape)
		ribbonZro_grp = rigTools.zeroGroupNam( ribbon_ctrl )
		ribbon_ctrl.editCtrlShape( axis = charScale * 1.8 )





		if upPlana == 'z+':
			ribbon_ctrl.rotateShape( rotate = ( 0 , 0 , 0 ) )
		elif upPlana == 'x-':
			ribbon_ctrl.rotateShape( rotate = ( 0 , 0 , -90 ) )
		elif upPlana == 'x+':
			pass
				#ribbon_ctrl.rotateShape( rotate = ( 0 , 0 , -90 ) )






		ribbon_ctrl.color = 'softBlue'

		# freeze number 2, i dunnno why
		ribbon_jnt.freeze(jointOrient=False) # long disable again
		ribbonZro_grp.maSnap( ribbon_jnt )

		'''
		if side == 'RGT':
			ribbonZro_grp.setRotate( (90,0,0) )
		'''
		
		
		folicle_parCons = core.parentConstraint( folicle , ribbonZro_grp ,mo = True)
		folicle_parCons.name = name + '_parCons'

		# Lock and hide
		# ribbon_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' ,  'v' )
		ribbon_ctrl.lockHideAttrLst( 'v' )
		ribbon_jnt.parent( ribbon_ctrl )

		# Parenting Group
		folicle.parent( flc_grp )
		ribbonZro_grp.parent( detail_grp )

		proxyJntList.append( ribbon_jnt.name )


	PinLogger.info('Complete...')
	return proxyJntList


	# # # # # # # # # # # # # # # # # # # # 
	# ending collecion data for new method follicle
	# # # # # # # # # # # # # # # # # # # #







# result: create bJnt and controller parent it to Father 
# location: rigging.autoRig.addRig.pinLocatorToSurface

from function.rigging.util import misc
reload(misc)

def _create_ctrl_bJnt_for_glue(
								loc_list = ['armorUprRGT_guide_loc', 'armorLwrLRGT_guide_loc'],
								priorJnt = 'clavLFT_bJnt',
								charScale = 5,
								ctrlShape = 'cube_ctrlShape',
								color = 'red',
								parentTo = 'ctrl_grp' ):

	for loc in loc_list:
		locator = core.Dag(loc)
		spName = locator.name
		baseName = spName.split('_')[0]
		bind_jnt = core.Joint()
		bind_jnt.name = baseName + '_bJnt'
		bind_jnt.maSnap( locator )
		bind_jnt.freeze()
		# parent to 
		bind_jnt.parent( priorJnt )

		# create controller
		bind_ctrl = core.Dag( baseName + '_ctrl' )
		bind_ctrl.nmCreateController( ctrlShape )

		bindCtrlZro_grp = rigTools.zeroGroupNam( bind_ctrl )
		bind_ctrl.editCtrlShape( axis = charScale * 1.8 )
		bind_ctrl.color = color
		bindGmbl_ctrl = core.createGimbal( bind_ctrl )

		# bindGmbl_ctrl = core.Dag( baseName + 'Gmbl_ctrl' )
		# bindGmbl_ctrl.nmCreateController( ctrlShape )
		# bindGmbl_ctrl.editCtrlShape( axis = charScale * 1.4 )
		# bindGmbl_ctrl.parent(bind_ctrl)

		bindCtrlZro_grp.maSnap( bind_jnt )

		# try to use matrice but fail
		# misc.parentMatrix( locator.name , bindCtrlZro_grp.name, mo = False, t = True, r = True, s = True)

		locator_parCons = core.parentConstraint( locator , bindCtrlZro_grp ,mo = True)
		locator_parCons.name = 'locator'+ baseName + '_parCons'

		# parent and scale con to the bind joint
		bindGmbl_parCons = core.parentConstraint( bindGmbl_ctrl , bind_jnt ,mo = True)
		bindGmbl_parCons.name = baseName + '_parCons'
		bindGmbl_scaleCons = core.scaleConstraint( bindGmbl_ctrl , bind_jnt ,mo = True)
		bindGmbl_scaleCons.name = baseName + '_scaleCons'

		if parentTo:
			bindCtrlZro_grp.parent(parentTo)






