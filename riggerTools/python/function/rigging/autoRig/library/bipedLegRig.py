# ==================== # biped LegRig
# incluce 
# footRoll ankle roll
# fk/ik switch


'''
from function.rigging.autoRig.library import bipedLegRig
reload( bipedLegRig )
'''
import maya.cmds as mc

from function.rigging.util import misc as misc
reload( misc )

from function.rigging import core 
reload( core )

from function.rigging.readWriteCtrlSizeData import flipController as fip
reload( fip )

from function.rigging.controllerBox import adjustController as adjust
reload( adjust )



def bipedRig(

	jntList = ( 				'upLegFrontLFT_bind_jnt'				,
								'midLegFrontLFT_bind_jnt'				,
								'ankleFrontLFT_bind_jnt' 			)	,

	pov = 'legPovFrontLFT_tmpJnt'	,		
	side = 'LFT'					,				
	parentTo = ''		,
	placementAttr = 'IK_FK_Arm_L'	,
	part = 'frontLeg'

	):		


	mc.select (deselect = True)
	fkRootZroName = []
	namJnt = []


	# Kept raw name
	namJnt = []
	for each in jntList:
		rawJnt = misc.splitName(each)
		namJnt.append(rawJnt[0])



	rootName = namJnt[0]


	# ========== # Dup ik joint
	ikJntLst = []
	num = 0  
	for each in namJnt:
		ikJnt = mc.joint(name = each + '_IK_jnt' ,  radius = (2.5) )
		ikJntLst.append(ikJnt)
		misc.snapParentConst(jntList[num] , ikJnt)
		mc.makeIdentity( ikJnt , apply = True , jointOrient = False)
		# off scale seqment conpensate
		#print 'turn off scale seqment conpensate of %s' %ikJnt
		#mc.setAttr ("%s.segmentScaleCompensate" %ikJnt ,0) 
		num = num + 1

	print '#### return %s' %namJnt[0]
	uprJnt = namJnt[0]
	lwrJnt = namJnt[2]


	print '#### return %s' %namJnt[2]
	# add root uprLeg here   



	uprIK = namJnt[0]+'_IK'
	midIK = namJnt[1]+'_IK'
	lwrIK = namJnt[2]+'_IK'


	# Create IK handle for upr ankle
	ikhName = mc.ikHandle( name = lwrIK  + '_handle', startJoint = ikJntLst[0], endEffector = ikJntLst[2], solver = 'ikRPsolver' )
	mc.rename( ikhName[1] , lwrIK + '_eff')
	ikhNam = ikhName[0]


		
	misc.snapParentConst( ikJntLst[2]  , lwrIK+'_Zro_grp' )
	mc.parent( ikhName[0] , lwrIK+'_ctrl'  )
	mc.parent(lwrIK+'_Zro_grp' , w = True)




	# Create pov and parent
	rawPov = misc.splitName(pov)
	misc.snapParentConst( pov , rawPov[0] + '_Zro_grp' )
	mc.poleVectorConstraint ( rawPov[0] + '_ctrl' , ikhName[0] , w = 1 )
	mc.parent( rawPov[0] + '_Zro_grp' , lwrIK+'_ctrl')	
	# should return ikhName
	# return ikhName


	# ========== # dode create local / world for POV(Pole Vector)

	mc.select (deselect = True)
	type = 'pov' 
	nodeName = rawPov[0]
	sel = nodeName + '_ctrl'
	mc.select(sel)

	mc.pickWalk(d='up')
	upSel = mc.pickWalk(d='up')
	upGrp = upSel[0]
	preName = sel.split('_')
	name = preName[0]

	print upGrp

	type = 'pov'
	grp = name +'_Zro_grp'
	wor = name +'_Wor_grp'
	loc = name + '_Loc_grp'
	rev = name + '_rev'
	pov = nodeName + '_ctrl'
	world = 'fly_ctrl'

	pConAttr = grp + '_parentConstraint1'


			
	mc.group( em = 1 , n = wor )
	mc.group( em = 1 , n = loc )
	mc.parent( wor,loc,upGrp )

	misc.snapParentConst( grp,wor ) 
	misc.snapParentConst( grp,loc ) 



	if type == 'pov':
		mc.parentConstraint( world ,wor ,w=1,mo=1 ,name = name + 'wor'+'_psCon' )
		mc.parentConstraint( wor, loc, grp, w = 0, mo = 1,name = name + 'loc'+'_psCon' )




	mc.createNode('reverse',n=rev)
	# Connect povCtrl to rev to pCon
	mc.connectAttr( pov + '.localWorld', rev + '.inputX' )
	mc.connectAttr( pov + '.localWorld', name + 'loc'+'_psCon' +'.'+wor+ 'W0' )
	mc.connectAttr( rev + '.outputX', name + 'loc'+'_psCon'+'.'+loc+ 'W1' )
	# delete temp joint
	mc.delete(nodeName+'_tmpJnt')






	# ========== # create root IK Controller



	legIkRoot = core.Base()
	legIkRoot.nmCreateController('cube_ctrlShape')
	legIkRoot.setName(rootName + '_IK_ctrl')
	legIkRoot.setColor('blue')

	sel = mc.select( rootName + '_IK_ctrl' )
	ikRootzroName = adjust.createZroGrp()
	ikRootzroName = mc.rename(ikRootzroName , rootName + '_IK_Zro_grp')

	upSize = fip.buildUI()
	upSize.flipCtrlShapeZ(sel , axis=[9, 7, 9])

	legIkRoot.renameShape(rootName + 'Shape')
	misc.snapPointConst(ikJntLst[0] , ikRootzroName )
	mc.parentConstraint( rootName + '_IK_ctrl' , ikJntLst[0] , maintainOffset = True)
	mc.scaleConstraint( rootName + '_IK_ctrl' , ikJntLst[0] , maintainOffset = True)
	#### return ikRootzroName
	# parent afeter finish
	#mc.parent( ikJntLst[0] , rootCtrlName )














	# ========== #  FK part Dup joint
	mc.select (deselect = True)
	fkJntLst = []
	num = 0  
	for each in namJnt:
		fkJnt = mc.joint(name = each + '_FK_jnt' ,  radius = (2.5) )
		fkJntLst.append(fkJnt)
		misc.snapParentConst(jntList[num] , fkJnt)
		mc.makeIdentity( fkJnt , apply = True , jointOrient = False)


		print 'turnoff scale seqment conpensate %s' %fkJnt
		mc.setAttr ( "%s.segmentScaleCompensate" %fkJnt , 0 ) 

		num = num + 1


	for each in namJnt:
		misc.snapParentConst(each+'_FK_jnt' , each+'_FK_Zro_grp')
		mc.parentConstraint( each + '_FK_Gimbal_ctrl',each+'_FK_jnt' , w = 1, mo = 1 ,name = each +'_psCon' )
		mc.scaleConstraint( each + '_FK_Gimbal_ctrl',each+'_FK_jnt' , w = 1, mo = 1 ,name = each +'_scCon' )

	mc.parent(  namJnt[1]+'_FK_Zro_grp', namJnt[0]+'_FK_Gimbal_ctrl'   )
	mc.parent(  namJnt[2]+'_FK_Zro_grp', namJnt[1]+'_FK_Gimbal_ctrl'   )

	#### return fkJntLst[0]


	# constraint each of bind joint to FK and IK
	for each in namJnt:
		psCon = mc.parentConstraint( each + '_FK_jnt', each+'_IK_jnt' , each + '_bind_jnt'  ,name = each +'Switch'+'_psCon' )
		## Add scale constraint
		scCon = mc.scaleConstraint( each + '_FK_jnt', each+'_IK_jnt' , each + '_bind_jnt'  ,name = each +'Switch'+'_scCon' )

		
		revNode = mc.createNode('reverse' , name = each +'Switch' + '_rev')
		
		
		# Connection fk/ik switch to placement
		# IK = W1
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr , revNode+'.inputX'  )
		mc.connectAttr( revNode + '.outputX' ,  psCon[0]+'.'+ each + '_IK_jnt' + 'W1' )
		## Add scale constraint
		mc.connectAttr( revNode + '.outputX' ,  scCon[0]+'.'+ each + '_IK_jnt' + 'W1' )

		# FK = W0
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr , psCon[0]+'.'+ each + '_FK_jnt' + 'W0'  )
		## Add scale constraint
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr ,  scCon[0]+'.'+ each + '_FK_jnt' + 'W0' )


	# hide fk/ik joint
	#mc.setAttr(namJnt[0] + '_FK_jnt.visibility' , 0)
	#mc.setAttr(namJnt[0] + '_IK_jnt.visibility' , 0)













	# ==================== # Dode IK strerchy 

	

	strJnt = namJnt[0]  + '_IK_jnt'
	midJnt = namJnt[1]  + '_IK_jnt'
	endJnt = namJnt[2]  + '_IK_jnt'


	strJntTy = mc.getAttr( namJnt[1]+'_IK_jnt'+'.ty')
	endJntTy = mc.getAttr( namJnt[2]+'_IK_jnt'+'.ty')

	if side == 'LFT':
		disJnt = strJntTy + endJntTy
		ampVal = 0.1
	if side == 'RGT':
		disJnt = (strJntTy + endJntTy)*(-1)
		ampVal = (-0.1)

	# Ctrl Name
	strCtrl = namJnt[0] + '_FK_ctrl'
	endCtrl = namJnt[2] + '_IK_ctrl'

	# Start End Loc Name
	strLoc = part + 'StartDist' + side + '_loc'
	endLoc = part + 'EndDist' + side + '_loc'

	# Speicify Node Name System
	disNode 		= part + 'AutoStretch' + side + '_dtw'
	mdvAutoNode 	= part + 'AutoStretch' + side + '_mdv'
	mdvNode 		= part + 'Stretch' + side + '_mdv'
	mdvAmpNode 		= part + 'StretchAmp' + side + '_mdv'
	cndNode 		= part + 'AutoStretch' + side +  '_cnd'
	bcNode 			= part + 'AutoStretch' + side + '_bc'
	pmaNode 		= part + 'Stretch' + side + '_pma'
	minusNode 		= part + 'MinuseStretch' + side + '_mdv'

	# add mdvNode for scale compansate
	scaleNode = part + 'Compensate' + 'Stretch' + side + '_mdv' 



	# Create Locator
	mc.spaceLocator( n = strLoc )
	mc.spaceLocator( n = endLoc )
	# Set the distance
	mc.parent( strLoc, endLoc, 'NOTOUCH_grp')

	# SnapLocator to start and end point
	mc.pointConstraint( strCtrl, strLoc, mo = 0, w = 1)
	mc.pointConstraint( endCtrl, endLoc, mo = 0, w = 1)


	# Measurement distance
	mc.createNode('distanceBetween', n = disNode)
	mc.connectAttr( strLoc + 'Shape.worldPosition', disNode + '.point1')
	mc.connectAttr( endLoc + 'Shape.worldPosition', disNode + '.point2')
	mc.setAttr( strLoc + '.v', 0)
	mc.setAttr( endLoc + '.v', 0)


	# Create AutoStretch_mdv and Set
	mc.createNode('multiplyDivide', n = mdvAutoNode)
	mc.setAttr( mdvAutoNode + '.operation', 2)
	mc.setAttr( mdvAutoNode + '.input2.input2X', disJnt)
	# Connect
	mc.connectAttr( disNode + '.distance', mdvAutoNode + '.input1.input1X ')



	#Create legAutoStretch_cnd
	mc.createNode('condition', n = cndNode)
	mc.setAttr( cndNode + '.operation', 3)
	mc.setAttr( cndNode + '.secondTerm', disJnt)

	#connect
	mc.connectAttr( mdvAutoNode + '.output.outputX', cndNode + '.colorIfTrue.colorIfTrueR')
	mc.connectAttr( disNode + '.distance', cndNode + '.firstTerm')

	#Create legStretchLFT_mdv and Set
	mc.createNode('multiplyDivide', n = mdvNode)
	mc.setAttr ( mdvNode + '.operation', 1)
	mc.setAttr( mdvNode + '.input2.input2X', strJntTy)
	mc.setAttr( mdvNode + '.input2.input2Y', endJntTy)
	#connect
	mc.connectAttr( cndNode + '.outColor.outColorR', mdvNode + '.input1.input1X')
	mc.connectAttr( cndNode + '.outColor.outColorR', mdvNode + '.input1.input1Y')

	#Create legStretchLFT_mdv and Set
	mc.createNode('multiplyDivide', n = mdvAmpNode)
	mc.setAttr( mdvAmpNode + '.input2X', ampVal)
	mc.setAttr( mdvAmpNode + '.input2Y', ampVal)

	#connect
	mc.connectAttr( endCtrl + '.lowStretch', mdvAmpNode + '.input1.input1Y') # NEED TO BE FIX "lowLegStretch"
	mc.connectAttr( endCtrl + '.upStretch', mdvAmpNode + '.input1.input1X') # NEED TO BE FIX "upLegStretch"

	#Create blendColors
	mc.createNode('blendColors', n = bcNode)
	mc.setAttr( bcNode + '.color2R', strJntTy)
	mc.setAttr( bcNode + '.color2G', endJntTy)
	#connect
	mc.connectAttr( mdvNode + '.output', bcNode + '.color1')
	mc.connectAttr( endCtrl + '.autoStretch', bcNode + '.blender')

	#Create legStretchLFT_pma
	mc.createNode('plusMinusAverage', n = pmaNode)
	#connect KEY bc
	mc.connectAttr( bcNode + '.outputR', pmaNode + '.input2D[1].input2Dx')
	mc.connectAttr( bcNode + '.outputG', pmaNode + '.input2D[1].input2Dy')
	#connect KEY amp
	mc.connectAttr( mdvAmpNode + '.outputX', pmaNode + '.input2D[2].input2Dx')
	mc.connectAttr( mdvAmpNode + '.outputY', pmaNode + '.input2D[2].input2Dy')

	#export translante to Joint
	mc.connectAttr ( pmaNode + '.output2D.output2Dx', midJnt + '.ty')
	mc.connectAttr ( pmaNode + '.output2D.output2Dy', endJnt + '.ty')



	
	## Create AutoStretch_mdv for scale compensete
	# get the c lenge
	cLength = mc.getAttr( disNode + '.distance')
	mc.createNode('multiplyDivide', name = scaleNode)
	# set value to 1 prevent to unexpect error
	mc.setAttr( scaleNode + '.input1X', 1)
	# set lengte of c edge
	mc.setAttr( scaleNode + '.input2.input2X', cLength)
	# Connect
	mc.connectAttr( scaleNode + '.output.outputX', mdvAutoNode + '.input2.input2X')

	if mc.objExists('placement_ctrl'):
		mc.connectAttr( 'placement_ctrl.scale.scaleX' , '%s.input1.input1X' %scaleNode  )
	




	# = = = = =  parenting



	# expose grp
	mc.parent(  namJnt[0]+'_FK_Zro_grp' , w = True )
	mc.select (deselect = True)




	# parent to hirechy
	#mc.parent(  namJnt[0]+'_FK_Zro_grp' , parentTo)
	#mc.parent(  ikRootzroName , parentTo)



	# return name
	return uprJnt, lwrJnt, ikhName[0] ,parentTo









def bipedFootRollRig (
	rootNam = 'ankleFrontLFT_IK_jnt'	,													
	jntLst = ['ballRollFrontLFT_bind_jnt' ,'toeRollFrontLFT_bind_jnt']	,
	footBehav = ['footOutFront','footInFront','heelRollFront','toeRollFront','ballRollFront','ankleFront']	,	
	placementAttr = 'IK_FK_Arm_L'		,														
	side = 'LFT'						,																
	part = 'frontLeg'						,																
	uprIK = ''						,																		
	lwrIK = ''				):





	'''
	rootNam = 'ankleFrontLFT_IK_jnt'													
	jntLst = ['ballRollFrontLFT_bind_jnt' ,'toeRollFrontLFT_bind_jnt']	
	footBehav = ['footOutFront','footInFront','heelRollFront','toeRollFront','ballRollFront','ankleFront']		
	placementAttr = 'IK_FK_Arm_L'																
	side = 'LFT'																	
	part = 'frontLeg'																	
	uprIK = legGrpLFT[0]																		
	lwrIK = legGrpLFT[1]
	'''





	rootRawNam = misc.splitName(rootNam)[0]

	# Kept raw name
	namJnt = []
	for each in jntLst:
		rawJnt = misc.splitName(each)
		namJnt.append(rawJnt[0])
			
	# To prevent unexpect parent
	mc.select(deselect = True)

	# ========== # Dup ik joint
	ikJntLst = []
	num = 0  
	for each in namJnt:
		ikJnt = mc.joint(name = each + '_IK_jnt' ,  radius = (2.5) )
		ikJntLst.append(ikJnt)
		misc.snapParentConst(jntLst[num] , ikJnt)
		mc.makeIdentity( ikJnt , apply = True , jointOrient = False)
		num = num + 1



	ikJntLst.append(rootNam)


	# Parent it to ik root joint
	print 'parent %s to %s ' %( ikJntLst[0] , rootNam )
	mc.parent(ikJntLst[0] , rootNam )





	
	# create foot controller
	rawName = 'foot' + part + side
	ctrlName =  rawName + '_IK_ctrl'
	footIK = core.Base()
	footIK.nmCreateController( 'foot%s_IK_ctrlShape' %side )
	footIK.setName( ctrlName )
	footIK.setColor( 'yellow' )
	footIK.renameShape( ctrlName + 'Shape' )

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , rawName + '_IK' + '_Zro_grp')
	#footIK.addAttribute(ln = 'autoStretch' , k = True , dv = 1)
	#misc.snapMatArg(   footBehav[4] + side + '_bind_jnt'  , rawName + '_IK' + '_Zro_grp'   )

	# Child ---> parent
	mc.matchTransform(rawName + '_IK' + '_Zro_grp' , footBehav[4] + side + '_bind_jnt' , position = True )
	#footIK.rotateShape( ro = (90 , 0 , 0)  )




	# create brand new ball roll controller
	ctrlName = footBehav[4] + side + '_IK_ctrl'
	ballRoll = core.Base()
	ballRoll.nmCreateController( 'ballRoll%s_IK_ctrlShape' %side )
	ballRoll.setName(ctrlName)
	ballRoll.setColor('yellow')
	ballRoll.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[4] + side + '_IK' + '_Zro_grp')








	# create brand new foot out controller
	ctrlName = footBehav[0] + side + '_IK_ctrl'
	footOut = core.Base()
	footOut.nmCreateController('footOut%s_IK_ctrlShape' %side)
	footOut.setName(ctrlName)
	footOut.setColor('yellow')
	footOut.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[0] + side + '_IK' + '_Zro_grp')











	# create brand new footIn controller
	ctrlName = footBehav[1] + side + '_IK_ctrl'
	footIn = core.Base()
	footIn.nmCreateController( 'footIn%s_IK_ctrlShape' %side )
	footIn.setName(ctrlName)
	footIn.setColor('yellow')
	footIn.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[1] + side + '_IK' + '_Zro_grp')





	# create brand new foot heel controller
	ctrlName = footBehav[2] + side + '_IK_ctrl'
	footHeel = core.Base()
	footHeel.nmCreateController( 'heelRoll%s_IK_ctrlShape' %side )
	footHeel.setName(ctrlName)
	footHeel.setColor('yellow')
	footHeel.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[2] + side + '_IK' + '_Zro_grp')





	# create brand new foot toe controller
	ctrlName = footBehav[3] + side + '_IK_ctrl'
	footToe = core.Base()
	footToe.nmCreateController( 'toesRoll%s_IK_ctrlShape' %side )
	footToe.setName(ctrlName)
	footToe.setColor('yellow')
	footToe.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[3] + side + '_IK' + '_Zro_grp')



	# Create IK handle for ankle roll
	ikAnkle = mc.ikHandle( name = part +'Ankle' + side + '_IK_handle', startJoint = ikJntLst[-1], endEffector = ikJntLst[0], solver = 'ikRPsolver' )
	mc.rename( ikAnkle[1] , part +'Ankle' + side + '_eff')

	# Create IK handle for toe roll
	ikToe = mc.ikHandle( name = part +'Toe' + side + '_IK_handle', startJoint = ikJntLst[0], endEffector = ikJntLst[1], solver = 'ikRPsolver' )
	mc.rename( ikToe[1] , part +'Toe' + side + '_eff')






	# Snap each grp to joint
	for each in footBehav:
		print '\n### Filter the joint with condition'
		if each == 'ankleBack' or each == 'toeRollBack' or each == 'ballRollBack' or each == 'toeRollFront' or each == 'ballRollFront' or each == 'ankleFront':
			#misc.snapParentConst( each + side + '_bind_jnt' ,  each + side + '_IK_Zro_grp')
			misc.snapMatArg( each + side + '_bind_jnt' , each + side + '_IK_Zro_grp' )
			
		else:
			misc.snapMatArg( each + side + '_tmpJnt' ,  each + side + '_IK_Zro_grp')
			mc.delete(each + side + '_tmpJnt')
			
		





	  
	# Parenting 

	# Footin ---> footOut
	mc.parent(footBehav[1] + side + '_IK_Zro_grp'  , footBehav[0] + side + '_IK_ctrl' )

	# Heel roll ---> footIn
	mc.parent(footBehav[2] + side + '_IK_Zro_grp'  , footBehav[1] + side + '_IK_ctrl' )

	# Ankle ---> heelRoll  
	#mc.parent(footBehav[5] + side + '_IK_Zro_grp'  , footBehav[2] + side + '_IK_ctrl' )

	# Toe ---> Heel
	mc.parent(footBehav[3] + side + '_IK_Zro_grp'  , footBehav[2] + side + '_IK_ctrl' ) 
	 
	# Ball  ---> Toe
	mc.parent(footBehav[4] + side + '_IK_Zro_grp'  , footBehav[3] + side + '_IK_ctrl' ) 





	mc.parent(ikToe[0] , footBehav[3] + side + '_IK_ctrl'   ) 
	mc.parent(ikAnkle[0] , footBehav[5] + side + '_IK_ctrl'   )  


	# Should return from function
	mc.parent(  footBehav[5] + side  + '_IK_Zro_grp'  ,  footBehav[4] + side + '_IK_ctrl' )

	# Parent everthing to foot IK 
	mc.parent(footBehav[0] + side  + '_IK_Zro_grp', footIK.name )

















	# ========== #  FK part Dup joint
	#jntLst.remove(jntLst[-1])


	# Kept raw name
	namJnt = []
	for each in jntLst:
		rawJnt = misc.splitName(each)
		namJnt.append(rawJnt[0])

	fkJntLst = []
	num = 0
	mc.select(deselect = True)  
	for each in namJnt:
		fkJnt = mc.joint( name = each + '_FK_jnt' ,  radius = (2.5) )
		fkJntLst.append(fkJnt)
		misc.snapParentConst( jntLst[num] , fkJnt )
		mc.makeIdentity( fkJnt , apply = True , jointOrient = False)
		# turn off scale seqment conpensate
		print 'turn off scale seqment conpensate of %s' %fkJnt
		mc.setAttr ("%s.segmentScaleCompensate" %fkJnt ,0) 

		num = num + 1



	# create brand new ball roll controller
	print '\ncreate ball roll controller'
	ctrlName = footBehav[4] + side + '_FK_ctrl'
	ballRollFK = core.Base()
	ballRollFK.nmCreateController('toes%s_FK_ctrlShape' %side)
	ballRollFK.setName(ctrlName)
	if side == 'LFT':
		ballRollFK.setColor('red')
	else:
		ballRollFK.setColor('blue')

	ballRollFK.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[4] + side + '_FK' + '_Zro_grp')
	mc.select(ctrlName)
	gimbalName = adjust.createGimbal()
	mc.rename( gimbalName , footBehav[4] + side + '_FK_Gimbal_ctrl' )











	# constraint each of bind joint between FK and IK
	print namJnt
	for each in namJnt:
		psCon = mc.parentConstraint( each + '_FK_jnt', each+'_IK_jnt' , each + '_bind_jnt'  ,name = each +'Switch'+'_psCon' )
		## Add scale constraint
		scCon = mc.scaleConstraint( each + '_FK_jnt', each+'_IK_jnt' , each + '_bind_jnt'  ,name = each +'Switch'+'_scCon' )

		
		revNode = mc.createNode('reverse' , name = each +'Switch' + '_rev')
		
		
		# Connection fk/ik switch to placement
		# IK = W1
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr , revNode+'.inputX'  )
		mc.connectAttr( revNode + '.outputX' ,  psCon[0]+'.'+ each + '_IK_jnt' + 'W1' )
		## Add scale constraint
		mc.connectAttr( revNode + '.outputX' ,  scCon[0]+'.'+ each + '_IK_jnt' + 'W1' )
		# FK = W0
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr , psCon[0]+'.'+ each + '_FK_jnt' + 'W0'  )
		## Add scale constraint
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr ,  scCon[0]+'.'+ each + '_FK_jnt' + 'W0' )


	# ========================  parenting ctrl to leg fk 
	parentTo = '%s_FK_Gimbal_ctrl' %rootRawNam
	mc.parent(  namJnt[0]+'_FK_Zro_grp' , parentTo)


	# ========================  parenting JOINT to root leg fk 
	parentTo = '%s_FK_jnt' %rootRawNam
	mc.parent(  namJnt[0]+'_FK_jnt' , parentTo)


	# constraint toe FK joint to root FK joint shift it to the end
	for each in namJnt:
		# Skipt the last joint
		if each == namJnt[-1]:
			continue

		misc.snapParentConst( each +'_FK_jnt' , each + '_FK_Zro_grp' )
		mc.parentConstraint( each + '_FK_Gimbal_ctrl',each + '_FK_jnt' , w = 1, mo = 1 ,name = each +'_psCon' )
		mc.scaleConstraint( each + '_FK_Gimbal_ctrl',each + '_FK_jnt' , w = 1, mo = 1 ,name = each +'_scCon' )



	mc.select('*_IK_handle')
	ikhLst = mc.ls(sl=True)
	for each in ikhLst:
		mc.setAttr('%s.visibility' %each , 0)
	mc.select(deselect = True)



	mc.select(deselect = True)


	return rawName