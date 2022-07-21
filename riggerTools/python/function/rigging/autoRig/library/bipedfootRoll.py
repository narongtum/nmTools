# bipedFootRollRig  
import maya.cmds as mc

from function.rigging import core 
reload(core)

from function.rigging.readWriteCtrlSizeData import flipController as fip
reload(fip)

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

from function.rigging.util import misc as misc
reload(misc)




def bipedFootRollRig (
	rootNam = 'ankleFrontLFT_IK_jnt'	,													
	jntLst = ['ballRollFrontLFT_bind_jnt' ,'toeRollFrontLFT_bind_jnt']	,
	footBehav = ['footOutFront','footInFront','heelRollFront','toeRollFront','ballRollFront','ankleFront']	,	
	placementAttr = 'IK_FK_Arm_L'			,														
	side = 'LFT'							,																
	part = 'frontLeg'						,																
	uprIK = ''								,																		
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
	rawName= 'foot' + part + side
	ctrlName =  rawName + '_IK_ctrl'
	footIK = core.Base()
	footIK.createController( 'foot%s_IK_ctrlShape' %side )
	footIK.setName(ctrlName)
	footIK.setColor('yellow')
	footIK.renameShape(ctrlName + 'Shape')

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
	ballRoll.createController( 'ballRoll%s_IK_ctrlShape' %side )
	ballRoll.setName(ctrlName)
	ballRoll.setColor('yellow')
	ballRoll.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[4] + side + '_IK' + '_Zro_grp')








	# create brand new foot out controller
	ctrlName = footBehav[0] + side + '_IK_ctrl'
	footOut = core.Base()
	footOut.createController('footOut%s_IK_ctrlShape' %side)
	footOut.setName(ctrlName)
	footOut.setColor('yellow')
	footOut.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[0] + side + '_IK' + '_Zro_grp')











	# create brand new footIn controller
	ctrlName = footBehav[1] + side + '_IK_ctrl'
	footIn = core.Base()
	footIn.createController( 'footIn%s_IK_ctrlShape' %side )
	footIn.setName(ctrlName)
	footIn.setColor('yellow')
	footIn.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[1] + side + '_IK' + '_Zro_grp')





	# create brand new foot heel controller
	ctrlName = footBehav[2] + side + '_IK_ctrl'
	footHeel = core.Base()
	footHeel.createController( 'heelRoll%s_IK_ctrlShape' %side )
	footHeel.setName(ctrlName)
	footHeel.setColor('yellow')
	footHeel.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[2] + side + '_IK' + '_Zro_grp')





	# create brand new foot toe controller
	ctrlName = footBehav[3] + side + '_IK_ctrl'
	footToe = core.Base()
	footToe.createController( 'toesRoll%s_IK_ctrlShape' %side )
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
		if each == 'ankleFront' or each == 'toeRollFront' or each == 'ballRollFront' :
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




	# Parent ikh to controller
	mc.parent(ikToe[0] , footBehav[3] + side + '_IK_ctrl'   ) 
	mc.parent(ikAnkle[0] , footBehav[5] + side + '_IK_ctrl'   )  


	# Should return from function
	mc.parent(  footBehav[5] + side  + '_IK_Zro_grp'  ,  footBehav[4] + side + '_IK_ctrl' )
	mc.parent(footBehav[0] + side  + '_IK_Zro_grp', footIK.name )

















	#=======================  foot FK conctroller
	# Remove Tip joint
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
		fkJnt = mc.joint(name = each + '_FK_jnt' ,  radius = (2.5) )
		fkJntLst.append(fkJnt)
		misc.snapParentConst( jntLst[num] , fkJnt )
		mc.makeIdentity( fkJnt , apply = True , jointOrient = False)
		num = num + 1



	# create brand new ball roll controller
	ctrlName = footBehav[4] + side + '_FK_ctrl'
	ballRollFK = core.Base()
	ballRollFK.createController('toes%s_FK_ctrlShape' %side)
	ballRollFK.setName(ctrlName)
	ballRollFK.setColor('yellow')
	ballRollFK.renameShape(ctrlName + 'Shape')

	mc.select(ctrlName)
	zroName = adjust.createZroGrp()
	mc.rename( zroName , footBehav[4] + side + '_FK' + '_Zro_grp')
	mc.select(ctrlName)
	gimbalName = adjust.createGimbal()
	mc.rename( gimbalName , footBehav[4] + side + '_FK_Gimbal_ctrl' )



	for each in namJnt:
		misc.snapParentConst( each +'_FK_jnt' , each + '_FK_Zro_grp' )
		mc.parentConstraint( each + '_FK_Gimbal_ctrl',each + '_FK_jnt' , w = 1, mo = 1 ,name = each +'_psCon' )








	# constraint each of bind joint between FK and IK
	print 'constraint %s of bind joint between FK and IK ' %namJnt

	for each in namJnt:
		psCon = mc.parentConstraint( each + '_FK_jnt', each + '_IK_jnt' , each + '_bind_jnt'  ,name = each +'Switch'+'_psCon' )

		
		revNode = mc.createNode('reverse' , name = each +'Switch' + '_rev')
		
		
		# Connection fk/ik switch to placement
		# IK = W1
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr , revNode+'.inputX'  )
		mc.connectAttr( revNode + '.outputX' ,  psCon[0]+'.'+ each + '_IK_jnt' + 'W1' )
		# FK = W0
		mc.connectAttr( 'placement_ctrl.%s' %placementAttr , psCon[0]+'.'+ each + '_FK_jnt' + 'W0'  )


	# ========================  parenting ctrl to leg fk 
	parentTo = '%s_FK_Gimbal_ctrl' %rootRawNam
	mc.parent(  namJnt[0]+'_FK_Zro_grp' , parentTo)


	# ========================  parenting JOINT to root leg fk 
	parentTo = '%s_FK_jnt' %rootRawNam
	mc.parent(  namJnt[0]+'_FK_jnt' , parentTo)



	mc.select('*_IK_handle')
	ikhLst = mc.ls(sl=True)
	for each in ikhLst:
		mc.setAttr('%s.visibility' %each , 0)
	mc.select(deselect = True)



	mc.select(deselect = True)


	return rawName


