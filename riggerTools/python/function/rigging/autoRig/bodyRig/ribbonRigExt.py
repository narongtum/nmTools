# Ribbon rig another version

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc
reload(misc)

import maya.cmds as mc

from function.pipeline import logger 
reload(logger)

import pymel.core as pm

class RibbonLogger(logger.MayaLogger):
	LOGGER_NAME = "Ribbon"






def ribbonRigExt(	nameSpace = ''	,		
					width = 10		,							
					numJoints = 5	,								
					side = 'LFT'	,
					jointTop = 'upperLegLFT_tmpJnt'	,
					jointBtm = 'lowerLegLFT_tmpJnt'	,
					part = 'upLeg'	,#'upArm','lwrArm','upLeg','lwrLeg'	,		
					charScale = 1	,							
					noTouch_grp = 'noTouch_grp'	,		
					showInfo = True 			,
					upPlana = ''	,
					ctrl_grp = 'ribbon_grp' ):


	# new arg
	# upPlana = 'z+'   # 'y+' or 'z+' only


	part_list = ('upArm','lwrArm','upLeg','lwrLeg')


	if part in part_list:
		if side == 'LFT':
			if part  == 'upArm' or part  == 'lwrArm':
				upPlana = 'x-'
			elif part  == 'upLeg' or part  == 'lwrLeg':
				upPlana = 'z+'
		elif side == 'RGT':
			if part  == 'upArm' or part  == 'lwrArm':
				upPlana = 'x+'
			elif part  == 'upLeg' or part  == 'lwrLeg':
				upPlana = 'z-'


	else:
		RibbonLogger.info('No corrective list. This might be a spine ribbon.')
		if not upPlana:
			RibbonLogger.critical('Please specific the up axis.')
			return False
		





	RibbonLogger.info('start of Ribbon function')
	noTouch_grp = '%s%s' %(	nameSpace , noTouch_grp	) 
	ribbonCollect_grp = core.Null('%sRibbon%s_grp' %(part,side) )

	armRotOrder = 'yxz'

	# inside function
	partElem = nameSpace + part
	types = 'Rbn'
	position = ( 'Top' , 'Mid' ,'Btm' )




	# for right side
	# if rbnType == 'limb':
	# RGT arm
	if upPlana == 'x+': 
		topPart = core.Dag( jointBtm )
		btmPart = core.Dag( jointTop )
		topPart_pxyJnt = rigTools.jointAt( btmPart )

		# For Fix twist fail using prosition only no orient
		btmPart_pxyJnt = rigTools.jointAt( btmPart )
		btmPart_pxyJnt.matchPosition(topPart)

	# LFT arm
	elif upPlana == 'x-':
		topPart = core.Dag( jointTop )
		btmPart = core.Dag( jointBtm )
		topPart_pxyJnt = rigTools.jointAt( topPart )

		# For Fix twist fail using prosition only no orient
		btmPart_pxyJnt = rigTools.jointAt( topPart )
		btmPart_pxyJnt.matchPosition(btmPart)

	# elif rbnType == 'spine': # 'z+'
	elif upPlana == 'z+': # 'z+'
		topPart = core.Dag( jointTop )
		btmPart = core.Dag( jointBtm )
		topPart_pxyJnt = rigTools.jointAt( topPart )

		# For Fix twist fail using prosition only no orient
		btmPart_pxyJnt = rigTools.jointAt( topPart )
		btmPart_pxyJnt.matchPosition(btmPart)


	# elif rbnType == 'spine': # 'z+'
	elif upPlana == 'z-': # 'z+'
		topPart = core.Dag( jointTop )
		btmPart = core.Dag( jointBtm )
		topPart_pxyJnt = rigTools.jointAt( topPart )

		# For Fix twist fail using prosition only no orient
		btmPart_pxyJnt = rigTools.jointAt( topPart )
		btmPart_pxyJnt.matchPosition(btmPart)




	topPart_pxyJnt.name = partElem + types + position[0] + side + '_pxyJnt'
	topPart_pxyJnt.attr('radius').value = 5
	topPart_pxyJnt.attr('overrideEnabled').value = 1
	topPart_pxyJnt.attr('overrideColor').value = 3
	topPart_pxyJnt.attr('v').value = showInfo

	btmPart_pxyJnt.name = partElem + types + position[2] + side + '_pxyJnt'
	btmPart_pxyJnt.attr('radius').value = 5
	btmPart_pxyJnt.attr('overrideEnabled').value = 1
	btmPart_pxyJnt.attr('overrideColor').value = 3
	btmPart_pxyJnt.attr('v').value = showInfo

	topPart_pxyJnt.rotateOrder = armRotOrder
	btmPart_pxyJnt.rotateOrder = armRotOrder

	topPoint  = (width/2*-1)
	endPoint  = (width/2)


	# if rbnType == 'limb':
	if upPlana == 'x-': # LFT arm
		aimVector = 	( 0,1,0 )
		upVector = 		( -1,0,0 )
		midUpValue = 	( -10,0,0 )
		supUpValue = 	( -10,0,0 )

	elif upPlana == 'x+':# RGT arm
		aimVector = 	( 0,-1,0 )
		upVector = 		( 0,0,-1 )
		midUpValue = 	( 0,10,0 )
		supUpValue = 	( 10,0,0 )

	elif upPlana == 'z+': # spine, LFT leg
		aimVector = 	 ( 0,1,0 ) 
		upVector = 		 ( 0,0,1 ) 
		midUpValue = 	 ( 0,0,10 ) 
		supUpValue = 	 ( 0,0,10 )

	elif upPlana == 'z-': # spine, LFT leg
		aimVector = 	 ( 0,1,0 ) 
		upVector = 		 ( 0,0,-1 ) 
		midUpValue = 	 ( 0,0,10 ) 
		supUpValue = 	 ( 0,0,-10 )

	#
	# create top btm joint
	#

	topName = part + 'TopRbnMov' + side
	btmName = part + 'BtmRbnMov' + side

	# Create proxy upper lower Mover
	ribbonTopMov_ctrl = core.Dag(   topName  + '_ctrl' )
	ribbonTopMov_ctrl.nmCreateController('plus_ctrlShape')
	ribbonTopMov_ctrl.editCtrlShape( axis = charScale * 2 )
	ribbonTopMov_ctrl.color = 'yellow'

	tempA_jnt = rigTools.jointAt( jointTop )
	tempA_jnt.freeze()

	# if rbnType == 'limb':
	if upPlana == 'x+' or upPlana == 'x-':
		tempA_jnt.setRotate( ( 0 , 0 , 90 ) )



	ribbonTopMov_ctrl.maSnap( tempA_jnt )
	tempA_jnt.deleteName()
	ribbonTopMovZro_grp = rigTools.zroNewGrpWithOffset( ribbonTopMov_ctrl )
	ribbonTopMov_parCons = core.parentConstraint( jointTop , ribbonTopMovZro_grp[0] , mo = True)
	ribbonTopMov_parCons.name =   topName + '_parCons'


	# Create proxy upper lower mover
	ribbonBtmMov_ctrl = core.Dag( btmName + '_ctrl' )
	ribbonBtmMov_ctrl.nmCreateController('plus_ctrlShape')
	ribbonBtmMov_ctrl.editCtrlShape( axis = charScale * 1.8 )
	ribbonBtmMov_ctrl.color = 'yellow'

	tempB_jnt = rigTools.jointAt( jointBtm )
	tempB_jnt.freeze()


	# if rbnType == 'limb':
	if upPlana == 'x+' or upPlana == 'x-':
		tempB_jnt.setRotate( ( 0 , 0 , 90 ) )





	ribbonBtmMov_ctrl.maSnap( tempB_jnt )
	tempB_jnt.deleteName()
	ribbonBtmMovZro_grp = rigTools.zroNewGrpWithOffset( ribbonBtmMov_ctrl )
	ribbonBtmMov_parCons = core.parentConstraint( jointBtm , ribbonBtmMovZro_grp[0] , mo = True)
	ribbonBtmMov_parCons.name =   btmName + '_parCons'


	# Create grp for collect all MovGrp
	hinges_grp = core.Null( partElem + 'Rbn' + 'AllMov' + side + '_grp' )
	hinges_grp.parent( ribbonCollect_grp )
	mc.parent( ribbonTopMovZro_grp[0] ,  hinges_grp.name )
	mc.parent( ribbonBtmMovZro_grp[0] ,  hinges_grp.name )


	# naming
	name = partElem + types + side

	# Create temp base NURBS-plane
	# rbnPlane_nrb = core.nurbPlane(name = name + '_nrb', axis = axis , width = width, lengthRatio = (1.0/width) , u = 2 , v = 1,  degree = 3 , ch = 0)
	deformCrv = core.curve( n = name + 'Tmp_crv' , p = [( topPart_pxyJnt.worldSpace ) , ( btmPart_pxyJnt.worldSpace )], degree = 1	)


	sourceObj = btmPart_pxyJnt.name
	targetObj = deformCrv.name

	pivotTranslate = mc.xform (sourceObj, q = True, ws = True, rotatePivot = True)
	mc.parent(targetObj, sourceObj)
	mc.makeIdentity(targetObj, a = True, t = True, r = True, s = True)
	mc.xform (targetObj, ws = True, pivots = pivotTranslate)
	mc.parent(targetObj, world = True)



	# use duplicate instead
	crvA = core.duplicate( deformCrv.name ,  name =  name + 'TmpA_crv', rr=True )
	crvB = core.duplicate( deformCrv.name ,  name =  name + 'TmpB_crv', rr=True )


	if upPlana == 'x+' or upPlana == 'x-':
		mc.move( 0, 0,  0.5, crvA.name, relative=True,objectSpace=True, worldSpaceDistance = True )
		mc.move( 0, 0, -0.5, crvB.name, relative=True,objectSpace=True, worldSpaceDistance = True )
	elif upPlana == 'z+':
		if part == 'upLeg' or part == 'lwrLeg':
			mc.move( 0.5, 0, 0, crvA.name, relative=True,objectSpace=True, worldSpaceDistance = True )
			mc.move(-0.5, 0, 0, crvB.name, relative=True,objectSpace=True, worldSpaceDistance = True )
		else: # RGT Leg
			mc.move( -0.5, 0, 0, crvA.name, relative=True,objectSpace=True, worldSpaceDistance = True )
			mc.move(  0.5, 0, 0, crvB.name, relative=True,objectSpace=True, worldSpaceDistance = True )
	elif upPlana == 'z-':
		mc.move(  0.5, 0, 0, crvA.name, relative=True,objectSpace=True, worldSpaceDistance = True )
		mc.move( -0.5, 0, 0, crvB.name, relative=True,objectSpace=True, worldSpaceDistance = True )




	mc.loft( crvA.name , crvB.name , ch = False , uniform = False , 
	close = False , autoReverse = True,degree = 1 ,sectionSpans = 1 ,range = False , 
	polygon = 0 , reverseSurfaceNormals = True ,name = name + '_nrb')



	rbnPlane_nrb = core.Dag(name + '_nrb')

	crvA.deleteName()
	crvB.deleteName()
	deformCrv.deleteName()
	mc.rebuildSurface( rbnPlane_nrb.name , constructionHistory = False ,  replaceOriginal = True ,
						rebuildType = 0, end = True ,  keepRange = 1 ,  keepControlPoints = False, 
						keepCorners = False,spansU  = 3 ,  degreeU =  3, spansV =  1 ,degreeV = 3 , 
						tolerance = 0 ,fitRebuild = 0 ,   direction =  2	)




	# makeTheNurb to object
	ribbon_nrb = core.Dag( name + '_nrb' )
	name = partElem + types
	# Create group and Parenting to Main grp
	# follicle grp
	flc_grp = core.Null( name +'Flc' + side +'_grp')
	# detail controller
	detail_grp = core.Null( name +'Detail' + side + '_grp')
	# nurb grp
	nrb_grp = core.Null( name +'Nrb' + side + '_grp')
	# For main ribbon
	rbnCtrl_grp = core.Null( name +'Ctrl' + side + '_grp')








	# Create inbetween flc and joint

	# For main ribbon
	proxyJntList = []

	if numJoints == 5:
		midJnt = 3
	elif numJoints == 3:
		midJnt = 2
	else:
		mc.error('You can use only 5 or 3 joint.')
		


	# # # # # # # # # # # # # # # # # # # # 
	# starting collecion data for new method follicle
	# # # # # # # # # # # # # # # # # # # #

	oNurbs = ribbon_nrb.name

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



	# start for loop

	for each in range (0 , numJoints ):


		num =  each + 1
		# Common name
		name =  partElem + types + '%02d'%num + side
		#       [region] + [Rbn] +     [01]   + [LFT]

		# using pin to surface to pin flc to desire UV cooordinate
		flc_name = rigTools._pinToSurface(
						oNurbs = ribbon_nrb.name 	,
						side = side 				,
						region = partElem + types   ,
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
			

				
			
			

		# Insert can delete if not work
		# ribbon_jnt.freeze()

		# Adjust rotation for proper Axis
		# ribbon_jnt.setRotate( upAxis )
		
		# try to ignore it
		#ribbon_jnt.setRotate( upAxis )
		
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
		ribbon_ctrl.nmCreateController('circle_ctrlShape')
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
		RibbonLogger.info('It okay?')
		
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



	# # # # # # # # # # # # # # # # # # # # 
	# ending collecion data for new method follicle
	# # # # # # # # # # # # # # # # # # # #





	#									#
	# 	Create Middle ribbon joint 		#
	#									#


	ribbon_nrb.parent( nrb_grp )
	name =  partElem + types + '%02d'%midJnt + side
	middle_ctrl = core.Dag( name + '_ctrl' )
	middle_pxyJnt = core.Joint()

	# edit move to here don't know why it break when adjust last
	middle_pxyJnt.rotateOrder = armRotOrder
	middle_pxyJnt.name = partElem + 'Mid' + side + '_pxyJnt'
	middle_pxyJnt.maSnap( middle_ctrl )
	middle_pxyJnt.attr('radius').value = 5
	middle_pxyJnt.attr('overrideEnabled').value = 1
	middle_pxyJnt.attr('overrideColor').value = 3
	middle_pxyJnt.attr('visibility').value = showInfo
	# edit add freeze
	middle_pxyJnt.freeze()


	name = partElem + 'Mid'
	ribbonMid_ctrl = core.Dag( name + types + side + '_ctrl')
	ribbonMid_ctrl.nmCreateController('squarePlain_ctrlShape')
	ribbonMid_ctrl.editCtrlShape( axis = charScale * 2.3 )
	ribbonMid_ctrl.rotateOrder = armRotOrder


	# Lock and hide attr
	for attr in ('sx','sy','sz') :
		ribbonMid_ctrl.attr( attr ).lockHide()


	# Add attr
	ribbonMid_ctrl.addAttribute( longName = 'Bar' , niceName = '-'   , at ='enum', en = 'Twist' , keyable = True )
	ribbonMid_ctrl.addAttribute( longName = 'Upper_Twist' , defaultValue = 0 , keyable = True )
	ribbonMid_ctrl.addAttribute( longName = 'Lower_Twist' , defaultValue = 0 , keyable = True )
	ribbonMid_ctrl.addAttribute( attributeType = 'short' , longName = 'Detail' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )
	ribbonMid_ctrl.addAttribute( attributeType = 'short' , longName = 'Auto_Twist' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )
	ribbonMid_ctrl.color = 'yellow'








	#								#
	#	 Create mid aim locator  	#
	#								#

	ribbonMidLocate_loc = core.Locator( name + types + side + '_loc' )
	ribbonMidAim_grp = core.Null( name + types + 'Aimed' + side + '_grp')

	# Test here if error can delete
	ribbonMidAim_grp.maSnap( ribbonMidLocate_loc )
	ribbonMidAim_grp.parent( ribbonMidLocate_loc )
	ribbonMid_ctrl.parent( ribbonMidAim_grp )
	ribbonMidLocate_loc.maSnap( middle_pxyJnt )


	# Use parent insted ParCon
	middle_pxyJnt.parent( ribbonMid_ctrl )
	# Create up aim for middle ribbon Error here
	midAimUp_loc = core.Locator( name + types + 'AimUp' + side + '_loc' )
	midAimUp_loc.snap( middle_pxyJnt )
	aimUpZro_grp = rigTools.zeroGroupNam( midAimUp_loc )







	if upPlana == 'x+' or upPlana == 'x-':
		midUpValue = 	( 0,10,0 )
		midAimUp_loc.setTranslate( midUpValue )

	elif upPlana == 'z+'  or upPlana == 'z-' :
		midUpValue = 	( 0,0,10 )
		midAimUp_loc.setTranslate( midUpValue )











	# hide visibility
	midAimUp_loc.attr('v').value = showInfo

	# Hide this locator
	# mc.setAttr( '%s'%ribbonMidLocate_loc.name + 'Shape' + '.' + 'visibility' , 0 )
	mc.setAttr( ribbonMidLocate_loc.shape + '.' + 'visibility' , showInfo )



	# aim constraint this work for RGT
	# upperLeg_aimCons = core.aimConstraint( upperLeg_ikJnt , rollBackAnkleIkStill_grp  , rollBackAnkleIkOffset_grp , mo = True ,  aimVector = ( 0,-1,0 ) , upVector = ( 0,0,1 ), worldUpType='object', worldUpObject = up_obj.name )


	if upPlana == 'x+':
		# aimCon 01
		logic = False
		#middle_aimCons = core.aimConstraint( ribbonTopMov_ctrl , ribbonMidAim_grp ,  mo = True , worldUpObject = midAimUp_loc.name )
		middle_aimCons = core.aimConstraint( ribbonTopMov_ctrl , ribbonMidAim_grp ,  mo = True , aimVector = (-1,0,0) ,upVector = (0,1,0), worldUpType='object', worldUpObject = midAimUp_loc.name )
		# middle_aimCons.attr('worldUpType').value = 1
		#middle_aimCons.attr('offsetX').value = 0
		#middle_aimCons.attr('offsetY').value = 0
		#middle_aimCons.attr('offsetZ').value = 0
		ribbonMid_ctrl.rotateShape( rotate = ( 0 , 0 , 90) )
		middle_aimCons.name = name + types + '_AimUp' + side + '_aimCons'


	# aimCon 02
	elif upPlana == 'x-':
		logic = False
		middle_aimCons = core.aimConstraint( ribbonTopMov_ctrl , ribbonMidAim_grp ,  mo = True , aimVector = (1,0,0) ,upVector = (0,1,0) , worldUpType='object', worldUpObject = midAimUp_loc.name )
		# middle_aimCons.attr('worldUpType').value = 1
		#middle_aimCons.attr('offsetX').value = 0
		#middle_aimCons.attr('offsetY').value = 0
		#middle_aimCons.attr('offsetZ').value = 0
		ribbonMid_ctrl.rotateShape( rotate = ( 0 , 0 , 90) )
		middle_aimCons.name = name + types + '_AimUp' + side + '_aimCons'


	elif upPlana == 'z+':
		middle_aimCons = core.aimConstraint( ribbonTopMov_ctrl , ribbonMidAim_grp ,  mo = True , aimVector = (-1,0,0) ,upVector = (0,1,0), worldUpType='object', worldUpObject = midAimUp_loc.name )
		middle_aimCons.name = name + types + '_AimUp' + side + '_aimCons'


	elif upPlana == 'z-':
		middle_aimCons = core.aimConstraint( ribbonTopMov_ctrl , ribbonMidAim_grp ,  mo = True , aimVector = (1,0,0) ,upVector = (0,1,0), worldUpType='object', worldUpObject = midAimUp_loc.name )
		middle_aimCons.name = name + types + '_AimUp' + side + '_aimCons'



	#										#
	# 	Create Up aim for upper ribbon 		#
	#										#

	name = partElem + position[0]
	topLocate_loc = core.Locator(  name + types + side + '_loc' )
	topAimed_grp = core.Null( name + types +'Aimed'+ side + '_grp' )
	topUpObj_loc = core.Locator( name + types + 'UpObj' + side + '_loc' )

	topAimed_grp.parent( topLocate_loc )
	topUpObj_loc.parent( topLocate_loc )
	topLocate_loc.maSnap( jointTop )


	if upPlana == 'x+' or upPlana == 'x-':
		topUpObj_loc.setTranslate( supUpValue )

	elif upPlana == 'z+':
		topUpObj_loc.setTranslate( supUpValue )

	elif upPlana == 'z-':
		topUpObj_loc.setTranslate( supUpValue )





	topPart_pxyJnt.parent( topAimed_grp )
	# hide visibility
	topUpObj_loc.attr('v').value = showInfo

	# Hide this locator
	# mc.setAttr( '%s'%topLocate_loc.shape + '.' + 'visibility' , 0 )
	mc.setAttr( topLocate_loc.shape + '.' + 'visibility' , showInfo )




	#											#
	# 	Create Lower aim for upper ribbon 		#
	#											#

	name = partElem + position[2]
	lowerLocate_loc = core.Locator( name + types + side + '_loc' )
	lowerAimed_grp = core.Null( name + types +'Aimed'+ side + '_grp' )
	lowerUpObj_loc = core.Locator( name + types + 'UpObj' + side + '_loc' )

	lowerAimed_grp.parent( lowerLocate_loc )
	lowerUpObj_loc.parent( lowerLocate_loc )

	lowerLocate_loc.snap( jointBtm )


	# because it orient from (use one line instead)
	lowerUpObj_loc.setTranslate( supUpValue )





	# lowerUpObj_loc.setTranslate( upValue )

	# hide visibility
	lowerUpObj_loc.attr('v').value = showInfo
	#lowerLocate_loc.attr('v').value = showInfo

	# Hide this locator
	# mc.setAttr( ribbonMidLocate_loc.shape + '.' + 'visibility' , 0 )
	mc.setAttr( ribbonMidLocate_loc.shape + '.' + 'visibility' , showInfo )
	btmPart_pxyJnt.parent( lowerAimed_grp )



	# Point constraint Point for make locate  it follow
	# rbnUpper_poinCons = core.pointConstraint(  jointTop , topLocate_loc , mo = True )
	rbnUpper_poinCons = core.pointConstraint(  ribbonTopMov_ctrl , topLocate_loc , mo = True )
	rbnUpper_poinCons.name = partElem + types + position[0] + side + '_pointCons'
	# Point constraint Point for make locate  it follow
	# rbnLower_poinCons = core.pointConstraint(  jointBtm , lowerLocate_loc , mo = True )
	rbnLower_poinCons = core.pointConstraint(  ribbonBtmMov_ctrl , lowerLocate_loc , mo = True )
	rbnLower_poinCons.name = partElem + types + position[2] + side + '_pointCons'







	# # # # # # # # # # 
	# LFT arm
	# # # # # # # # # # 

	if upPlana == 'x-':
		upper_aimCons = core.aimConstraint(  lowerLocate_loc , topAimed_grp ,  mo = True , aimVector = aimVector ,upVector = upVector, worldUpType='object', worldUpObject = topUpObj_loc.name )
		# upper_aimCons.attr('worldUpType').value = 1
		# upper_aimCons.attr('offsetX').value = 0
		# upper_aimCons.attr('offsetY').value = 90
		# upper_aimCons.attr('offsetZ').value = 0

		lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = True , aimVector = aimVector ,upVector = upVector, worldUpType='object'  , worldUpObject = lowerUpObj_loc.name)
		# lower_aimCons.attr('worldUpType').value = 1
		# lower_aimCons.attr('offsetY').value = 90

		# ribbonMid_ctrl.rotateShape( rotate = ( 0 , 0 , 90) )

	# # # # # # # # # # 
	# RGT arm
	# # # # # # # # # # 

	# upper
	if upPlana == 'x+':
		upper_aimCons = core.aimConstraint(  lowerLocate_loc , topAimed_grp ,  mo = True , aimVector = (0, -1, 0) ,upVector = (1, 0, 0), worldUpType ='object', worldUpObject = topUpObj_loc.name )
		# upper_aimCons = core.aimConstraint(  lowerLocate_loc , topAimed_grp ,  mo = True , aimVector = aimVector ,upVector = upVector, worldUpObject = topUpObj_loc.name )
		# upper_aimCons.attr('worldUpType').value = 1
		# upper_aimCons.attr('offsetX').value = 0
		# upper_aimCons.attr('offsetY').value = 90
		# upper_aimCons.attr('offsetZ').value = 0
		
		lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = True , aimVector = (0, 1, 0) ,upVector = (1, 0, 0)  , worldUpType ='object' , worldUpObject = lowerUpObj_loc.name)
		#lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = True , worldUpType='object', worldUpObject = lowerUpObj_loc.name)
		# lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = True , aimVector = aimVector ,upVector = upVector  , worldUpObject = lowerUpObj_loc.name)
		# lower_aimCons.attr('worldUpType').value = 1
		# lower_aimCons.attr('offsetY').value = 90


	# # # # # # # # # # 
	# LFT leg 
	# # # # # # # # # # 
			
	elif upPlana == 'z+':
		upper_aimCons = core.aimConstraint(  lowerLocate_loc , topAimed_grp , mo = True , aimVector = (0, -1, 0) ,upVector = upVector, worldUpType='object', worldUpObject = topUpObj_loc.name )
		lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = True , aimVector = (0, 1, 0) ,upVector = upVector, worldUpType='object'  , worldUpObject = lowerUpObj_loc.name)

	elif upPlana == 'z-':
		upper_aimCons = core.aimConstraint(  lowerLocate_loc , topAimed_grp , mo = True , aimVector = (0, -1, 0) ,upVector = upVector, worldUpType='object', worldUpObject = topUpObj_loc.name )
		lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp , mo = True , aimVector = (0, 1, 0) ,upVector = upVector, worldUpType='object'  , worldUpObject = lowerUpObj_loc.name)
		
	upper_aimCons.name = partElem + types + position[0] + side + '_aimCons'
	lower_aimCons.name = partElem + types + position[1] + side + '_aimCons'





	# Make Middle follower for both upper and lower

	# middleRbn_poinCons = core.pointConstraint( jointTop , jointBtm , ribbonMidLocate_loc,mo = True)
	middleRbn_poinCons = core.pointConstraint( ribbonTopMov_ctrl , ribbonBtmMov_ctrl , ribbonMidLocate_loc,mo = True)
	middleRbn_poinCons.name = partElem + types + position[1] + side + '_pointCons'
	# middleRbn_poinCons.attr( '%s'%jointTop + 'W0'  ).value = 0.5
	# middleRbn_poinCons.attr( '%s'%jointBtm + 'W1'  ).value = 0.5
	middleRbn_poinCons.attr( '%s'%ribbonTopMov_ctrl + 'W0'  ).value = 0.5
	middleRbn_poinCons.attr( '%s'%ribbonBtmMov_ctrl + 'W1'  ).value = 0.5
	aimUpZro_grp.parent( ribbonMidLocate_loc )






	#							#
	#	Skin joint to nurb 		#
	#							#

	# Write just two case five and three joint but acually use any num joint 
	ribbon_skc = core.SkinCluster( topPart_pxyJnt.name , middle_pxyJnt.name ,btmPart_pxyJnt.name , ribbon_nrb.name ,dr = 7 , mi = 2 )
	ribbon_skc.name =  name + types + side + '_skc'



	if numJoints == 5 or numJoints == 3:

		# because of the UV coordinate correction must change all of naming and index of skinCluster according to new UV
		maxValue = 1
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[0][0]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue)]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[0][1]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue)]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[0][2]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue)]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[0][3]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue)]	)

		maxValue = 0.8
		minValue = 0.2
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[1][0]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[1][1]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[1][2]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[1][3]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)

		maxValue = 0.5
		minValue = 0.5
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[2][0]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[2][1]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[2][2]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[2][3]'  , transformValue = [ ( topPart_pxyJnt.name , maxValue ), ( middle_pxyJnt.name, minValue )]	)
		
		maxValue = 0.5
		minValue = 0.5
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[3][0]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[3][1]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[3][2]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[3][3]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)

		maxValue = 0.8
		minValue = 0.2
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[4][0]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[4][1]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[4][2]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[4][3]'  , transformValue = [ ( middle_pxyJnt.name , minValue ), ( btmPart_pxyJnt.name, maxValue )]	)

		maxValue = 1
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[5][0]'  , transformValue = [ ( btmPart_pxyJnt.name , maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[5][1]'  , transformValue = [ ( btmPart_pxyJnt.name , maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[5][2]'  , transformValue = [ ( btmPart_pxyJnt.name , maxValue )]	)
		mc.skinPercent( ribbon_skc.name, ribbon_nrb.name + '.cv[5][3]'  , transformValue = [ ( btmPart_pxyJnt.name , maxValue )]	)


	else:
		mc.error('Please choose 3 or 5 joint.')




	#							#
	#	connect attributeType 	#
	#							#

	# Parent  Parent
	flc_grp.parent( ribbonCollect_grp )
	detail_grp.parent( ctrl_grp )
	nrb_grp.parent(ribbonCollect_grp)


	# ribbonCollect_grp.parent(noTouch_grp)
	if noTouch_grp:
		mc.parent( ribbonCollect_grp.name , noTouch_grp )

	# snap grp
	rbnCtrl_grp.maSnap( jointTop )
	topLocate_loc.parent( rbnCtrl_grp )
	lowerLocate_loc.parent( rbnCtrl_grp )
	ribbonMidLocate_loc.parent( rbnCtrl_grp )


	rbnCtrl_grp.parent( ctrl_grp )
	# rbnCtrl_parCons = core.parentConstraint( jointTop , rbnCtrl_grp , mo = True )
	rbnCtrl_parCons = core.parentConstraint( ribbonTopMov_ctrl , rbnCtrl_grp , mo = True )
	rbnCtrl_parCons.name = partElem + types + 'Ctrl' + side + '_parCons'

	# Connect Upper Attr
	ribbonMid_ctrl.attr('Upper_Twist') >> topPart_pxyJnt.attr('rotateY')
	# Connection Detail to visibility
	ribbonMid_ctrl.attr('Detail') >> detail_grp.attr('visibility')

	# Connect Lower twsit
	addTwistVal = core.AddDoubleLinear( partElem + 'Twist' + side + '_adl' )
	ribbonMid_ctrl.attr('Lower_Twist') >> addTwistVal.attr('input1')
	addTwistVal.attr('output') >> btmPart_pxyJnt.attr('rotateY')

	# Create condition
	condTwistVal = core.Condition( partElem + 'Twist' + side + '_cond' )
	ribbonMid_ctrl.attr('Auto_Twist') >> condTwistVal.attr('firstTerm')
	condTwistVal.attr('secondTerm').value = 1
	condTwistVal.attr('colorIfFalseR').value = 0


	if side == 'LFT':
		btmPart.attr('rotateY') >> condTwistVal.attr('colorIfTrueR')
	elif side == 'RGT':
		topPart.attr('rotateY') >> condTwistVal.attr('colorIfTrueR')
	condTwistVal.attr('outColorR') >> addTwistVal.attr('input2')


	# rawNam = misc.splitName(each)[0]


	bindJntList = []
	for each in  proxyJntList :
		rawNam = misc.splitName(each)

		# Naming Condition
		if len(rawNam) == 2:
			rawNam = rawNam[0] 
		elif len(rawNam) == 3:
			rawNam = rawNam[0] + '_' + rawNam[1] 
		elif len(rawNam) == 4:
			rawNam = rawNam[0] + '_' + rawNam[1]  + '_' + rawNam[2]
		else:
			mc.error('Something wrong with element.')


		# bind_jnt = mc.joint( name = rawNam + '_rbnBJnt' )
		subBind_jnt = core.Joint()
		subBind_jnt.name = rawNam + '_rbnBJnt'
		subBind_jnt.attr('radius').value = 2.5
		subBind_jnt.attr('overrideEnabled').value = 1
		subBind_jnt.attr('overrideColor').value = 3
		subBind_jnt.rotateOrder = armRotOrder

		# Turn off segmentScaleCompensate for make it scalable
		subBind_jnt.attr('segmentScaleCompensate').value = 0

		subBind_jnt.maSnap(each)



		mc.select( deselect = True )

		# move parent sub bind joint to here
		mc.parent( subBind_jnt.name , jointTop)

		# edit add freeze
		subBind_jnt.freeze()


		# misc.snapParentConstr( each ,  subBind_jnt.name , mo = False , name = rawNam + '_parCons')
		# edit change to 'True' instead
		core.parentConstraint( each ,  subBind_jnt.name , mo = True , name = rawNam + '_parCons')
		# Add scale parent for make controller scalable
		core.scaleConstraint( each ,  subBind_jnt.name , mo = True , name = rawNam + '_scalCons') 

		# misc.snapParentConstr( each ,  subBind_jnt.name , mo = False)

		bindJntList.append( subBind_jnt.name )



		print (rawNam)




	allRibbonGrp = []
	allRibbonGrp.append( ribbonTopMovZro_grp )
	allRibbonGrp.append( ribbonBtmMovZro_grp )


	subRbnJnt = [] # for parent each sub ribbon joint to one chain

	# Make Hinges all mover
	# Check what element is
	# if part == 'upArm' or part == 'upLeg':
	# solid method will cause troble for sure
	if part[:2] == 'up':
		makeHingesParent = ribbonBtmMovZro_grp
		subRbnJnt = bindJntList[-1]
	# elif part == 'lwrArm' or part == 'lwrLeg':
	elif part[:3] == 'lwr':
		makeHingesParent = ribbonTopMovZro_grp
		subRbnJnt = bindJntList[0]
	else:
		RibbonLogger.warning("Can't'return value up or lwr please check.")
		# mc.error('Can't'return value up or lwr please check')
		makeHingesParent = None

	# hide nrb
	ribbon_nrb.attr('v').value = showInfo


	# mc.parent( bindJntList[0] , jointTop )
	# Change parent under bind joint
	# mc.parent( bindJntList[0] , jointTop )
	mc.select( deselect = True )

	print ('\n')
	print ('part is %s' %part)
	print ('side is %s' %side  )
	print ('aimVector is {0}'.format(aimVector)  )
	print ('upVector is {0}'.format(upVector))
	print ('midUpValue is ' + str(midUpValue))
	print ('supUpValue is ' + str(supUpValue)  )
	print ( '\nmakeHingesParent')

	RibbonLogger.info('End of RibbonRig function.')
	print(makeHingesParent , allRibbonGrp ,subRbnJnt)
	return makeHingesParent , allRibbonGrp ,subRbnJnt









# Benefical of ribbon functon for make elbow or knee move
def makeHigesMover( 	nameSpace = ''	,
						part = ''		, 
						side = 'LFT' 	, 
						btmName = ''	, 
						topName = ''  	, 
						charScale = '' 	, 
						noTouch_grp = 'noTouch_grp' 	,
						moverPosition = 'lowerArmLFT_bJnt'	,
						ctrl_grp = 'ctrl_grp'		,

					 ):

	# naming = charName + elem


	# ctrl_grp = '%s%s' %(	naming , ctrl_grp	) 
	noTouch_grp = '%s%s' %(	nameSpace , noTouch_grp	) 


	name = nameSpace + part + 'Hinges' + 'Rbn'
	rbnHinges_ctrl = core.Dag( name + side + '_ctrl' )
	rbnHinges_ctrl.nmCreateController('squarePlain_ctrlShape')
	rbnHinges_ctrl.editCtrlShape( axis = charScale * 2.1 )
	rbnHinges_ctrl.color = 'softBlue'



	#							#
	#	set ctrl orientation	#
	#							#

	if part == 'arm':
		print ('\nThis is maybe Arm.')

		if side == 'LFT':
			upAxis = ( 0,0,90 )
		elif side == 'RGT':
			upAxis = ( 180,0,90 )

	elif part == 'leg' or part == 'frontLeg' or part == 'backLeg' or part == 'upLeg' or part == 'lwrLeg'  :
		print ('\nThis is maybe Leg.')

		if side == 'LFT':
			# upAxis = ( 0,0,180 )	default value
			upAxis = ( 0,0,180 )
		elif side == 'RGT':
			# upAxis = ( 0,180,0 ) default value
			upAxis = ( 0,0,0 )
	else:
		mc.error('What part is it?')





	hinges_jnt = core.Joint()
	hinges_jnt.maSnap( moverPosition )
	# Translate elbow or knee a bit for solve weight error
	hinges_jnt.moveObj(position = (0,charScale*0.01,0))

	hinges_jnt.freeze()
	hinges_jnt.setRotate( upAxis )
	hinges_jnt.freeze()

	rbnHinges_ctrl.maSnap( hinges_jnt ) 
	hinges_jnt.name = name + side + '_rbnBJnt'

	if part == 'leg':
		rbnHinges_ctrl.rotateShape( rotate = ( 0 , 0 , 0 )	)
	elif part == 'arm':
		rbnHinges_ctrl.rotateShape( rotate = ( 0 , 0 , 90 )	)


	# Parent to bind joint for exporting
	# hinges_jnt.parent( moverPosition )
	hinges_jnt.attr('radius').value = 1.5
	hinges_jnt.attr('overrideEnabled').value = 1
	# Make it gray
	hinges_jnt.attr('overrideColor').value = 3
	# For make controller scalable
	hinges_jnt.attr('segmentScaleCompensate').value = 0

	# Make it follow
	rbnHingesMid_parCons = core.parentConstraint( rbnHinges_ctrl  , hinges_jnt  , mo = True )
	rbnHingesMid_parCons.name = name +'Mid'+ side + '_parCons'
	# For make controller scalable
	rbnHingesMid_parCons = core.scaleConstraint( rbnHinges_ctrl  , hinges_jnt  , mo = True )
	rbnHingesMid_parCons.name = name +'Mid'+ side + '_scalCons'
	rbnhingesZro_grp = rigTools.zroNewGrpWithOffset( rbnHinges_ctrl )

	# Parent constraint  with Offset grp
	print ('\n**THIS IS A upper bJnt ---------------------------------**')
	print (btmName[0][1])

	rbnHingesTop_parCons = core.parentConstraint( rbnHinges_ctrl  , btmName[0][1]  , mo = True )
	rbnHingesTop_parCons.name = name +'Top'+ side + '_parCons'
	rbnHingesBtm_parCons = core.parentConstraint( rbnHinges_ctrl , topName[0][1]   , mo = True )
	rbnHingesBtm_parCons.name = name +'Btm'+ side + '_parCons'

	# Make Hinges follow bJnt
	rbnHinges_parCons = core.parentConstraint( moverPosition , rbnhingesZro_grp[0] , mo = True ) 
	rbnHinges_parCons.name = name +'BJnt'+ side + '_parCons'
	mc.parent( rbnhingesZro_grp[0] , ctrl_grp  )

	print ('\n**THIS IS A upper bJnt ---------------------------------**')
	print (btmName[2])

	print ('\n**THIS IS A lower bJnt ---------------------------------**')
	print (topName[2])

	bJntMoverPos = moverPosition.replace( 'buffJnt' , 'bJnt')

	mc.parent( hinges_jnt.name ,  bJntMoverPos )
	# mc.parent( topName[2] ,  bJntMoverPos )

	mc.select( deselect = True )

	print (topName)
	print (btmName)