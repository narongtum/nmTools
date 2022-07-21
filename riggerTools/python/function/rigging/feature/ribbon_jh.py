"""
Modify from ribbon Jorn-Harald Paulsen
https://vimeo.com/108727407

"""


from function.rigging.autoRig.base import core 
reload(core)

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

from function.rigging.util import misc as misc
reload(misc)

import maya.cmds as mc
# move MID under Mid_flc if you want ribbon orient alone bind joint


'''
from function.rigging.feature import ribbon_jh 


firstRbn = ribbon_jh.runRbnRig( 	
				width = 4				,
				numJoints = 5 			,
				prefix = 'tentacleA'		, 
				side = 'RGT'			, 
				aim = 'y-'				,	
				jointTOP = 'joint1'			,
				jointEND = 'joint2'		
			)

'''
		






 #   __                  _   _             
 #  / _|                | | (_)            
 # | |_ _   _ _ __   ___| |_ _  ___  _ __  
 # |  _| | | | '_ \ / __| __| |/ _ \| '_ \ 
 # | | | |_| | | | | (__| |_| | (_) | | | |
 # |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|
                                         
                                         






# used keyword arg because it aceppt arg of addAttr
def addAttribute(objects = [] , longName = '' , niceName = '' , lock = False, **kwargs ):
	for obj in objects:
		# For each attribure if have many attr such as twist,roll
		for each in range(0, len(longName)):
			# if nicename was defined
			attrNice = '' if not niceName else niceName[each]

			#if the attribute does not exists
			if not mc.attributeQuery(longName[each], node = obj , exists = True ):
				mc.addAttr( obj, longName = longName[each], niceName = attrNice  ,**kwargs)
				# if lock was set to true
				mc.setAttr( obj+'.'+longName[each] , lock = 1) if lock else mc.setAttr(obj+'.'+longName[each] , lock = 0 )




def _nonlinearDeformer(objects=[], defType = None, lowBound = -1, highBound = 1, translate = None, rotate = None, name = 'nonLinear'):
	# Check if objects not in defType or in that list
	if not objects or defType not in ['bend','flare','sine','squash','twist','wave']:
		raise Exception, "make sure you specitied a valid deformer"

	# create and rename deformer
	nonLinearDef = mc.nonLinear( objects[0], type = defType, lowBound = lowBound, highBound = highBound )
	nonLinearDef[0] = mc.rename( nonLinearDef[0], (name  + '_def') 		)
	nonLinearDef[1] = mc.rename( nonLinearDef[1], (name  + '_Handle')	 )

	# set translate if neccceary
	if translate:
		mc.setAttr( nonLinearDef[1] + '.translate' ,  translate[0], translate[1], translate[2] )

	if rotate:
		print nonLinearDef
		mc.setAttr( nonLinearDef[1] + '.rotate' ,  rotate[0], rotate[1], rotate[2] )
	return nonLinearDef


# setpivot of cluster
def setPivot( 	objects = [], rotatePivot = 1, scalePivot = 1, pivot = (0,0,0) 	):
	# Make sure the input is passed on as a list
	# totally don't understand
	objects = [objects] if isinstance(	objects, (str, unicode)	) else objects
	#For each object
	for obj in objects:
		#If rotatePivot was set to True, set the rotatePivot
		if rotatePivot:
			mc.xform( obj, worldSpace=True, rotatePivot = pivot )
		#If scalePivot was set to True, set the scalePivot
		if scalePivot:
			mc.xform( obj, worldSpace=True, scalePivot = pivot )




def createFollicle( inputSurface = [] , scaleGrp = '', uVal = 0.5, vVal = 0.5, hide = 1, name = 'follicle' ):
	# create follicle
	follicleShape = mc.createNode( 'follicle' )
	print 'follicleShape is %s' %follicleShape
	# get the transition for follicle
	follicleTrans = mc.listRelatives(follicleShape, parent = True)[0]
	# rename
	follicleTrans = mc.rename(follicleTrans, name)
	# rename shapeNode
	follicleShape = mc.rename( mc.listRelatives( follicleTrans, c = True)[0], (name+'Shape')	)

	# if type is nurb 
	if mc.objectType(inputSurface[0]) == 'nurbsSurface':
		print 'This is nurbsSurface.'
		print 'connect inputSurface[0] is' + inputSurface[0] + '.local'
		mc.connectAttr( inputSurface[0] + '.local' , follicleShape + '.inputSurface' )

	# if type is mesh
	if mc.objectType(inputSurface[0]) == 'mesh':
		print 'This is mesh.'
		mc.connectAttr( inputSurface[0] + '.outMesh' , follicleShape + '.inputMesh' )


	# connect attr
	mc.connectAttr( inputSurface[0] + '.worldMatrix[0]'	,	follicleShape + '.inputWorldMatrix' )

	# connect follicle to transform
	mc.connectAttr( follicleShape + '.outRotate' , follicleTrans + '.rotate'	)
	mc.connectAttr(  follicleShape + '.outTranslate' , follicleTrans + '.translate'	)
	# set the U and V to current follicle
	mc.setAttr( follicleShape + '.parameterU' , uVal )
	mc.setAttr( follicleShape + '.parameterV' , vVal )
	# lock the transition and rotation
	mc.setAttr(follicleTrans + '.translate' , lock = True )
	mc.setAttr( follicleTrans + '.rotate' , lock = True )

	# that is hide why hide
	if hide:
		mc.setAttr( follicleShape + '.visibility' , 0 )

	return follicleTrans , follicleShape






                                                                                               

def runRbnRig( 	
				width = 20				,
				numJoints = 3 			,
				prefix = 'uprAnim' 		, 
				side = 'LFT'			, 
				aim = 'y+'				,	
				jointTOP = ''			,
				jointEND = ''			
			):

	# global gather infomation
	scaleGrp	=	[]



	if aim == 'y+':
		# start from LFT > RGT
		topPoint  = (width/2*-1)
		endPoint  = (width/2)

	elif aim == 'y-':
		endPoint  = (width/2*-1)
		topPoint  = (width/2)





	# Create group for rig
	stillGrp       = mc.group(  empty = True, name = (	prefix + 'StillAll' + side + '_grp'	)   	)
	grpTransform   = mc.group(  empty = True, name = (	prefix + 'Transform' + side + '_grp')	)
	grpCtrl        = mc.group(  empty = True, name = (	prefix + 'Ctrl' + side + '_grp'), parent	= grpTransform)
	grpSurface     = mc.group(  empty = True, name = (	prefix + 'Surface' + side + '_grp'), parent	= grpTransform)
	grpSurfaces    = mc.group(  empty = True, name = (	prefix + 'Surfaces' + side + '_grp'), parent	= stillGrp)
	grpDeformers   = mc.group(  empty = True, name = (	prefix + 'Deformer' + side + '_grp'), parent	= stillGrp)
	grpFollMain    = mc.group(  empty = True, name = (	prefix + 'Follicles_skin' + side + '_grp'), parent	= stillGrp)
	grpFollVolume  = mc.group(  empty = True, name = (	prefix + 'Follicles_volume' + side + '_grp'), parent	= stillGrp)
	grpCluster     = mc.group(  empty = True, name = (	prefix + 'Cluster' + side + '_grp'), parent	= stillGrp)
	grpMisc        = mc.group(  empty = True, name = (	prefix + 'Misc' + side + '_grp'), parent	= stillGrp)

	grpMainSurfece = mc.group(  empty = True, name = (	prefix + 'MainCtrl' + side + '_grp'), parent	= grpTransform) 

	# Create temp base NURBS-plane 
	tmpPlane = mc.nurbsPlane( axis = (0,1,0), width = width, lengthRatio = (1.0/width) , u = numJoints, v = 1,  degree = 3 , ch = 0)[0]

	# Duplicate plane to use in another option
	nrbMain		=	mc.duplicate( tmpPlane, name = (  	prefix + 'Main'+side +'_nrb') 											)
	nrbTwist	=	mc.duplicate( tmpPlane, name = (   	prefix + 'Twist_blnd' + side +'_nrb'			) 									)
	nrbSine		=	mc.duplicate( tmpPlane, name = (  	prefix + 'Sine_blnd' + side +'_nrb'		)		)
	nrbWire		=	mc.duplicate( tmpPlane, name = (  	prefix + 'Wire_blnd' + side +'_nrb'		)		)
	nrbVolume	=	mc.duplicate( tmpPlane, name = (  	prefix + 'Volume' + side +'_nrb'		) 		)

	# offset value plane for volume function purpose
	mc.setAttr((nrbVolume[0] + '.translateZ'), -0.5)
	mc.delete(tmpPlane)












	# Point TOP
	# Create controller
	####### ctrl Top plus
	topName = prefix +'TOP'+ 'rbn' + side + '_ctrl'
	ctrlTop = core.Dag(topName)
	ctrlTop.nmCreateController( 'plus_ctrlShape' )
	ctrlTop.renameShape(  topName +'Shape' )
	ctrlTop.setTranslation( (topPoint, 0, 0))

	'''if aim == 'y+':
		ctrlTop.setRotation( x = 0, y = 0, z = -90 )
	elif aim == 'y-':
		ctrlTop.setRotation( x = 0, y = 180, z = 90 )'''

	mc.select( topName , r=True )
	grpTop = adjust.createZroGrp(offset = True)
	# grpTop is  return zro and offset grp
	# [0] is zro
	# [1] is offset





	####### ctrl mid regtangle
	midName = prefix +'MID'+ 'rbn' + side + '_ctrl'
	ctrlMid = core.Dag(midName)
	ctrlMid.nmCreateController( 'sphere_ctrlShape')
	ctrlMid.renameShape(  midName + 'Shape')
	ctrlMid.setColor('red')
	ctrlMid.setScale(x = 2.5, y = 2.5, z = 2.5 )

	if aim == 'y+':
		ctrlMid.setRotation( x = 180, y = -180, z = 90 )
	elif aim == 'y-':
		ctrlMid.setRotation( x = 180, y = 0, z = 90 )


	grpMid = adjust.createZroGrp(offset = True)
	mc.select( midName , r=True )
	adjust.createGimbal()
	#print 'create MID ctrl %s' %grpMid








	####### ctrl End plus
	endName = prefix + 'END' + 'rbn' + '3' + side + '_ctrl'
	ctrlEnd = core.Dag( endName )
	ctrlEnd.nmCreateController( 'plus_ctrlShape' )
	
	ctrlEnd.renameShape( endName + 'Shape' )
	ctrlEnd.setTranslation( (endPoint,0, 0) )

	'''if aim == 'y+':
		ctrlEnd.setRotation( x = 0, y = 0, z = -90 )
	elif aim == 'y-':
		ctrlEnd.setRotation( x = 0, y = 180, z = 90 )'''

	mc.select( endName , r=True )
	grpEnd = adjust.createZroGrp(offset = True)




	# PointConstraint the midCtrl between the top/end
	midConst = mc.pointConstraint(str(ctrlTop), str(ctrlEnd), grpMid[1])








	#create deformet call funcetion
	twistDef = _nonlinearDeformer(	objects = [	nrbTwist[0]	], defType = 'twist',	name = nrbTwist[0], lowBound = -1, highBound = 1, rotate = (0,0,90)	)
	sineDef = _nonlinearDeformer(	objects = [	nrbSine[0]	], defType = 'sine',	name = nrbSine[0], lowBound = -1, highBound = 1, rotate = (0,0,90)	)
	squashDef = _nonlinearDeformer(	objects = [	nrbVolume[0]	], defType = 'squash',	name = nrbVolume[0], lowBound = -1, highBound = 1, rotate = (0,0,90)	)
	# set sine dropoff to 1 for what?
	mc.setAttr( (sineDef[0] + '.dropoff'), 1 )

	# Create wire deformer
	deformCrv = mc.curve( p = [(topPoint , 0 , 0) , (0,0,0), (endPoint, 0, 0)], degree = 2	)
	deformCrv = mc.rename(	deformCrv, (prefix+side + 'ribbon_wire_crv')		)
	wireDef = mc.wire(	nrbWire, dds = (0,15), wire = deformCrv	)
	wireDef[0] = mc.rename(	wireDef[0], (nrbWire[0] + '_wire')	)



	# Create Clusters : 
	clsTop = mc.cluster(	(deformCrv + '.cv[0:1]'),	 relative=1)
	clsMid = mc.cluster(	(deformCrv + '.cv[1]'), 	relative=1)
	clsEnd = mc.cluster(	(deformCrv + '.cv[1:2]'), 	relative=1)

	clsTop[0] = mc.rename(	clsTop[0], (str(ctrlTop) + '_top_cluster')				)
	clsTop[1] = mc.rename(	clsTop[1], (str(ctrlTop) + '_top_clusterHandle')		)
	clsMid[0] = mc.rename(	clsMid[0], (str(ctrlMid) + '_mid_cluster')				)
	clsMid[1] = mc.rename(	clsMid[1], (str(ctrlMid) + '_mid_clusterHandle')		)
	clsEnd[0] = mc.rename(	clsEnd[0], (str(ctrlEnd) + '_end_cluster')				)
	clsEnd[1] = mc.rename(	clsEnd[1], (str(ctrlEnd) + '_end_clusterHandle')		)

	# what and why but the result is set the position of cluster
	mc.setAttr(		(mc.listRelatives(clsTop[1], type="shape")[0] + '.originX'), topPoint		)
	mc.setAttr(		(mc.listRelatives(clsEnd[1], type="shape")[0] + '.originX'), endPoint		)

	# set new pivot to the edge of nurb
	setPivot(	objects = [clsTop[1]], rotatePivot = 1, scalePivot = 1, pivot = (topPoint,0,0)	)
	setPivot(	objects = [clsEnd[1]], rotatePivot = 1, scalePivot = 1, pivot = (endPoint,0,0)	)


	# but the result is make the tangent flat
	mc.percent(	clsTop[0], (deformCrv + '.cv[1]'), v=0.5	)
	mc.percent(	clsEnd[0], (deformCrv + '.cv[1]'), v=0.5	)



	# TOP
	# make it y along
	# Create PMA top group connect value from ctrl and zro grp
	# input 3d then no need to specify 'XYZ'
	posTopPma = mc.shadingNode(	'plusMinusAverage', asUtility = 1 , name = prefix +side+ 'TopCtrl_pma'	)
	mc.connectAttr( str(ctrlTop) + '.translate'	, 	posTopPma + '.input3D[0]'	)
	mc.connectAttr( grpTop[1] + '.translate'	, 	posTopPma + '.input3D[1]'		)


	# make it follow controller
	# add this for recorrective orientation instead
	mulTopMdv = mc.shadingNode( 'multiplyDivide', asUtility=1, name = prefix + side + 'Top_mdv'	)
	mc.setAttr(mulTopMdv+'.input2X' , 1)

	mc.connectAttr( posTopPma + '.output3Dx' , 	mulTopMdv + '.input1X'    )
	mc.connectAttr( posTopPma + '.output3Dy' , 	clsTop[1] + '.translateY'    )
	mc.connectAttr( posTopPma + '.output3Dz' , 	clsTop[1] + '.translateZ'    )
	mc.connectAttr( mulTopMdv + '.outputX' ,  	clsTop[1] + '.translateX'   )

	# connectAttr cluster to follow translation 
	#mc.connectAttr(		posTopPma + 	'.output3D'		, 	clsTop[1] + '.translate'	)




	# MID
	# make it follow mid controller
	# make it y along
	#mc.connectAttr(		str(ctrlMid) + 	'.translate'	, 	clsMid[1] + '.translate'	)
	mulMidMdv = mc.shadingNode( 'multiplyDivide', asUtility = 1, name = prefix + side + 'Mid_mdv'	)

	
	# Change value higher for make controller follow mid rib more accurate


	if aim == 'y+':
		mc.setAttr( mulMidMdv+'.input2X' , -5 )
		mc.setAttr( mulMidMdv+'.input2Y' , 5 )
		mc.setAttr( mulMidMdv+'.input2Z' , 5  )


	elif aim == 'y-':
		mc.setAttr( mulMidMdv+'.input2X' , 5 )
		mc.setAttr( mulMidMdv+'.input2Y' , 5 )
		mc.setAttr( mulMidMdv+'.input2Z' , -5 )


	


	'''mc.connectAttr( str(ctrlMid) + '.translateX' , 	mulMidMdv + '.input1X'    )
	mc.connectAttr( str(ctrlMid) + '.translateY' , 	clsMid[1] + '.translateX'    )
	mc.connectAttr( str(ctrlMid) + '.translateZ' , 	clsMid[1] + '.translateZ'    )
	mc.connectAttr( 	mulMidMdv + '.outputX' ,  	clsMid[1] + '.translateY'   )'''


		
	mc.connectAttr( str(ctrlMid) + '.translateX' , 	mulMidMdv + '.input1X'    )
	mc.connectAttr( str(ctrlMid) + '.translateY' , 	mulMidMdv + '.input1Y'    )
	mc.connectAttr( str(ctrlMid) + '.translateZ' , 	mulMidMdv + '.input1Z'    )

	mc.connectAttr( 	mulMidMdv + '.outputX' ,  	clsMid[1] + '.translateY'   )
	mc.connectAttr( 	mulMidMdv + '.outputY' ,  	clsMid[1] + '.translateX'   )
	mc.connectAttr( 	mulMidMdv + '.outputZ' ,  	clsMid[1] + '.translateZ'   )


	



	# END
	# make it y along
	# Create PMA end group connect value from ctrl and zro grp
	posEndPma = mc.shadingNode( 'plusMinusAverage', asUtility=1, name = prefix + side +'EndCtrl_pma'	)
	mc.connectAttr(		str(ctrlEnd) + '.translate', 	posEndPma + '.input3D[0]'	)
	mc.connectAttr(		grpEnd[1] + '.translate', 		posEndPma + '.input3D[1]'	)

	# make it follow controller
	# add this for recorrective orientation instead
	mulEndMdv = mc.shadingNode( 'multiplyDivide', asUtility=1, name = prefix + side +'End_mdv'	)
	mc.setAttr(mulEndMdv+'.input2X' , 1)

	mc.connectAttr( posEndPma + '.output3Dx' , 	mulEndMdv + '.input1X'    )
	mc.connectAttr( posEndPma + '.output3Dy' , 	clsEnd[1] + '.translateY'    )
	mc.connectAttr( posEndPma + '.output3Dz' , 	clsEnd[1] + '.translateZ'    )
	mc.connectAttr( 	mulEndMdv + '.outputX' ,  	clsEnd[1] + '.translateX'   )




	# Create blendshape
	blndDef = mc.blendShape( nrbWire[0], nrbTwist[0], nrbSine[0], nrbMain[0] , name = prefix + side +'_bsh' , weight = [	(0,1),(1,1),(2,1)]	)







	# CREATE ATTRIBUTE
	# Create Twist/Roll attr for controller
	addAttribute( objects = [  str(ctrlMid) ] , longName = ['twistBar'], niceName = ['-'] , at ='enum' , en = 'Twist' , lock = True , keyable = True)
	addAttribute( objects = [	str(ctrlTop), str(ctrlEnd) ]	, longName = ['twist'] , 		at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlTop), str(ctrlEnd) ]	, longName = ['twistOffset'] , 	at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['roll'] , 		at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['rollOffset'] , 	at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlTop), str(ctrlEnd) ]	, longName = ['affectToMid'] , 	min = 0, max = 10 , dv = 10 , k = True)


	# Volume Attr
	addAttribute( objects = [ str(ctrlMid) ] , longName = ['volumeBar'], niceName = ['-'] , at ='enum' , en = 'volume' , lock = True , keyable = True)
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['volume'] , 				at = 'float' ,	min = -1 ,	 max = 1 ,  keyable = True )
	# dv = defaultValue
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['volumeMultiplier'] , 	at = 'float' ,	min = 1 , 	defaultValue = 3 ,  keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['startDropoff'] , 		at = 'float' ,	min = 0 ,	max = 1, defaultValue = 1 ,  keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['endDropoff'] , 			at = 'float' ,	min = 0 ,	max = 1, defaultValue = 1 ,  keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['volumeScale'] , 			at = 'float' ,	min = endPoint*0.9 ,	max = topPoint*0.9,  keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['volumePosition'] , 		at = 'float' ,	min = endPoint ,	max = topPoint, defaultValue = 0 ,  keyable = True )


	# Sine Attr
	addAttribute( objects = [ str(ctrlMid) ] , longName = ['sineBar'], niceName = ['-'] , at ='enum' , en = 'sine' , lock = True , keyable = True)
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['amplitude'] , 	at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['offset'] , 	at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['twist'] , 	at = 'float' , keyable = True )
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['sineLength'] , 	at = 'float' , min = 0.1 ,	defaultValue = True, keyable = True )

	# Visibility Detail
	addAttribute( objects = [ str(ctrlMid) ] 	, longName = ['DetailBar'], niceName = ['-'] , at ='enum' , en = 'Detail' , lock = True , keyable = True)
	addAttribute( objects = [	str(ctrlMid) ]	, longName = ['Detail'] , at = 'long' , min = 0 ,	max = 1 , keyable = True )


	# connect to ctrl top
	# sum the twist and roll
	sumTopPma = mc.shadingNode( 'plusMinusAverage' , asUtility = True , name = prefix + side + 'twist_top_sum_pma' )
	mc.connectAttr( str(ctrlTop) + '.twist' , sumTopPma + '.input1D[0]' )
	mc.connectAttr( str(ctrlTop) + '.twistOffset' , sumTopPma + '.input1D[1]' )
	mc.connectAttr( str(ctrlMid) + '.roll' , sumTopPma + '.input1D[2]' )
	mc.connectAttr( str(ctrlMid) + '.rollOffset' , sumTopPma + '.input1D[3]' )
	# Since i reverse alone path there for change start to endAngle
	mc.connectAttr( sumTopPma + '.output1D' , twistDef[0] + '.endAngle' )

	# connect to ctrl end
	# Sum End  twist PMA
	sumEndPma = mc.shadingNode( 'plusMinusAverage' , asUtility = True , name = prefix + side + 'twist_low_sum_pma' )
	mc.connectAttr( str(ctrlEnd) + '.twist' , sumEndPma + '.input1D[0]' )
	mc.connectAttr( str(ctrlEnd) + '.twistOffset' , sumEndPma + '.input1D[1]' )
	mc.connectAttr( str(ctrlMid) + '.roll' , sumEndPma + '.input1D[2]' )
	mc.connectAttr( str(ctrlMid) + '.rollOffset' , sumEndPma + '.input1D[3]' )
	# Since i reverse alone path there for change start to endAngle
	mc.connectAttr( sumEndPma + '.output1D' , twistDef[0] + '.startAngle' )


	# connect twist  affectToMid to  controller
	# multDoubleLinear is 2 channel for multiply
	topAffMdl = mc.shadingNode('multDoubleLinear' , asUtility = True , name = prefix + side+ 'twist_top_affect_mdl')
	mc.setAttr( topAffMdl + '.input1' , -0.1 )
	mc.connectAttr( str(ctrlTop) + '.affectToMid' , topAffMdl + '.input2'  )
	mc.connectAttr( topAffMdl + '.output' , twistDef[0] + '.lowBound' ) 

	endAffMdl = mc.shadingNode('multDoubleLinear' , asUtility = True , name = prefix+ side + 'twist_end_affect_mdl')
	mc.setAttr( endAffMdl + '.input1' , -0.1 )
	mc.connectAttr( str(ctrlEnd) + '.affectToMid' , endAffMdl + '.input2'  )
	mc.connectAttr( endAffMdl + '.output' , twistDef[0] + '.highBound' ) 



	# setup connection for Squash deformer 
	volumeRevfMdl = mc.shadingNode( 'multDoubleLinear' , asUtility = True , name = prefix + side + 'volume_reverse_mdl' )
	# reverse value by multiply 1
	mc.setAttr( volumeRevfMdl + '.input1' , -1 )
	mc.connectAttr( str(ctrlMid) + '.volume' , volumeRevfMdl + '.input2' 	)
	mc.connectAttr( volumeRevfMdl + '.output' , squashDef[0] + '.factor'		)
	mc.connectAttr( str(ctrlMid) + '.startDropoff' , squashDef[0] + '.startSmoothness'		)
	mc.connectAttr( str(ctrlMid) + '.endDropoff', squashDef[0] + '.endSmoothness'		)
	mc.connectAttr( str(ctrlMid) + '.volumePosition', squashDef[1] + '.translateX'		)


	# Setup volume scaling
	sumScalePma = mc.shadingNode( 'plusMinusAverage' , asUtility = True , name = prefix + side + 'volume_scale_sum_pma' )
	mc.setAttr( sumScalePma + '.input1D[0]' , topPoint )
	mc.connectAttr( str(ctrlMid) + '.volumeScale' , sumScalePma + '.input1D[1]' )
	mc.connectAttr( sumScalePma + '.output1D' , squashDef[1] + '.scaleY' )


	# setup sine deformer
	mc.connectAttr( str(ctrlMid) + '.amplitude' , sineDef[0] + '.amplitude' )
	mc.connectAttr( str(ctrlMid) + '.offset' 	, sineDef[0] + '.offset' )
	mc.connectAttr( str(ctrlMid) + '.twist' 	, sineDef[1] + '.rotateY' )
	mc.connectAttr( str(ctrlMid) + '.sineLength' , sineDef[0] + '.wavelength' )


		
	# Move object to grp
	mc.parent( nrbMain[0] ,nrbTwist[0], nrbSine[0], nrbWire[0], nrbVolume[0], grpSurface)
	mc.parent( nrbMain[0] , grpMainSurfece)

	mc.parent(twistDef[1], sineDef[1], squashDef[1], grpDeformers)
	mc.parent(clsTop[1], clsMid[1], clsEnd[1], grpCluster)
	mc.parent(grpTop[0], grpMid[0], grpEnd[0], grpCtrl)
	mc.parent(deformCrv, (mc.listConnections(wireDef[0] + '.baseWire[0]')[0]), grpMisc)

	# Hide obj
	mc.hide(  grpDeformers, grpCluster, grpMisc, grpSurface )


	# What is isHistoricallyInteresting and why set to zero



	storeFolicleJnt = []

	for each in range (0, numJoints ):
		num = str( each + 1 )

		# create follicle for u position 
		# not  quite understand this formula
		# but the result if create inbetween of TOP to END
		uVal = ((0.5 / numJoints) * (each + 1) * 2) - ((0.5 / (numJoints * 2)) * 2)

		# create follicle for the bind plane 
		follicleS = createFollicle( scaleGrp = scaleGrp, inputSurface = mc.listRelatives( nrbMain[0], 		type = 'shape'), uVal = uVal, 		name = prefix + num +  side + '_normal_flc' )
		# create follicle for the volume plane
		follicleV = createFollicle( scaleGrp = None , inputSurface = mc.listRelatives( nrbVolume[0], 		type = 'shape'), uVal = uVal, vVal = 0, 	name = prefix + num + side+ '_volume_flc' )


		mc.parent(follicleS[0], grpFollMain)
		mc.parent(follicleV[0], grpFollVolume)


		# create joint 
		mc.select( clear = True)




		if aim == 'y+':
			follicleJoint = mc.joint( name = prefix + num + side + '_proxy_jnt' ,orientation = (0,0,-90), radius = 1.5 )

		elif aim == 'y-':
			follicleJoint = mc.joint( name = prefix + num + side + '_proxy_jnt' ,orientation = (0,-180,90), radius = 1.5 )
		
		misc.snapPointConst( follicleS[0], follicleJoint )

		follicleZroGrp = mc.group( name=  prefix + num + side + '_zro_grp' , empty=True)
		misc.snapParentConst( follicleJoint, follicleZroGrp )
		

		# create detail controller

		adjust.createController('circle_ctrlShape')
		adjust.assignColor(color = 'white')
		follicleCtrl = mc.rename( 'curve1', prefix + num + side + '_ctrl'  )
		print 'Create sub controller...'


		#follicleCtrl = mc.circle(name= prefix + num + '_ctrl' , c = (0,0,0), nr = (1,0,0), sw = 360, r = 0.5, d = 3, s = 8, ch = 0)[0]
		misc.snapParentConst( follicleJoint, follicleCtrl )
		
		mc.parent(follicleZroGrp, follicleS[0])
		mc.parent(follicleCtrl, follicleZroGrp)
		mc.parent(follicleJoint, follicleCtrl)
		
		# connect to detail for mid controller
		mc.connectAttr(		str(ctrlMid) + '.Detail', (	mc.listRelatives(follicleCtrl, shapes = True)[0] + '.visibility')	)

		multMdv = mc.shadingNode( 'multiplyDivide' , asUtility = True , name = prefix + num + side + '_multiplier_mdv' )
		mc.connectAttr( str(ctrlMid) + '.volumeMultiplier' , multMdv + '.input1Z' )
		mc.connectAttr( follicleV[0] + '.translate' , multMdv + '.input2' )

		sumPma = mc.shadingNode('plusMinusAverage' , asUtility = True , name = prefix + num + side + '_volume_sum_pma')
		mc.connectAttr( multMdv + '.outputZ'  , sumPma  + '.input1D[0]')

		mc.setAttr( sumPma + '.input1D[1]' , 1 )
		# difference from JH because we use y along insted x alone like him
		mc.connectAttr(sumPma + '.output1D' , follicleZroGrp + '.scaleX')
		mc.connectAttr(sumPma + '.output1D' , follicleZroGrp + '.scaleZ')

		storeFolicleJnt.append(follicleJoint)


	# snap to top end joint
	misc.snapParentConstr( jointTOP , grpTop[1] , maintainOffset = False)
	misc.snapParentConstr( jointEND , grpEnd[1] , maintainOffset = False)

	print 'Return detail joint name'
	return storeFolicleJnt , stillGrp , grpTransform





 #                                                _ 
 #                                               | |
 #   ___ ___  _ __ ___  _ __ ___   __ _ _ __   __| |
 #  / __/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
 # | (_| (_) | | | | | | | | | | | (_| | | | | (_| |
 #  \___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|




'''	

from function.rigging.feature import ribbon_jh as rbnRig
reload(rbnRig)



rbnRig.runRbnRig( 	
				width = 20				,
				numJoints = 3 			,
				prefix = 'uprAnim' 		, 
				side = 'LFT'			, 
				aim = 'y+'				,	
				jointTOP = 'joint1'			,
				jointEND = 'joint2'			
			)



	



'''








	






