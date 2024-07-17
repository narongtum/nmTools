import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc as misc
reload( misc )

from function.rigging.autoRig.bodyRig import ribbonRig
reload( ribbonRig )

from function.rigging.autoRig.bodyRig import midLockModule
reload( midLockModule )

from function.rigging.autoRig.bodyRig import createIKStretch as create
reload( create )


def armRig(
			nameSpace = '' 						,
			charScale = ''						,
			parentTo = 'ctrl_grp' 				,
			side = 'LFT',
			tmpJnt = (	'upperArmLFT_tmpJnt'  , 'lowerArmLFT_tmpJnt' ,  
						'handLFT_tmpJnt' , 'armLFT_pov_tmpJnt' ),
			priorJnt = 'clavLFT_bJnt'			,
			ikhGrp = 'ikh_grp'					,
			noTouchGrp = 'noTouch_grp' 			,
			nullGrp = 'snapNull_grp'			,
			jnt_grp =  'jnt_grp'				,
			showInfo = False 					,
			ribbon = False 						,
			ribbonRes = 'high'		

	):

	print '''\n

	# = = = = = = = = = Create Arm Rig = = = = = = = = = #
	
	'''

	# nameSpace = charName + elem
	# parentTo = '%s%s' %(nameSpace,parentTo) 
	# ikhGrp = '%s%s' %(nameSpace,ikhGrp) 
	# noTouchGrp = '%s%s' %(nameSpace,noTouchGrp)
	# jnt_grp = '%s%s' %( nameSpace,'jnt_grp')

	part = nameSpace + 'arm'
	if side == 'LFT':
		colorSide = 'red'
	else:
		colorSide = 'blue'

	armRotOrder = 'yxz'

	upperArm = core.Dag( tmpJnt[ 0 ] )
	lowerArm = core.Dag( tmpJnt[ 1 ] )
	hand = core.Dag( tmpJnt[ 2 ] )
	povArm = core.Dag( tmpJnt[ 3 ] )


	# Naming bind joint
	upperArm_bJnt = rigTools.jointAt( upperArm )
	lowerArm_bJnt = rigTools.jointAt( lowerArm )
	#povArm_bJnt = rigTools.jointAt( povArm )
	hand_bJnt = rigTools.jointAt( hand )


	upperArm_bJnt.name = nameSpace + 'upperArm' + side + '_bJnt'
	lowerArm_bJnt.name = nameSpace + 'lowerArm' + side + '_bJnt'
	#povArm_bJnt.name = 'povArm' + side + '_bJnt' # don wanna create POV
	hand_bJnt.name = nameSpace + 'hand' + side + '_bJnt'


	# Adjust rotate order
	upperArm_bJnt.rotateOrder = armRotOrder
	lowerArm_bJnt.rotateOrder = armRotOrder
	hand_bJnt.rotateOrder = armRotOrder

	lowerArm_bJnt.parent( upperArm_bJnt )
	hand_bJnt.parent( lowerArm_bJnt )
	hand_bJnt.attr('segmentScaleCompensate').value = 0

	# Parent it to prior joint
	upperArm_bJnt.parent( priorJnt )



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Store raw name
	# Result : extract side for name
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	rawName = []
	for each in tmpJnt:
		tmp = each.split('_')[0][:-3]
		rawName.append(tmp)
		

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create main rig grp
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	armRig_grp = core.Null( part + 'Rig' + side + '_grp' )
	armRigGrp_parCons = core.parentConstraint( priorJnt , armRig_grp )
	armRigGrp_parCons.name = part + 'Rig' + side + '_parCons'

	# Create joint grp
	armJnt_grp = core.Null( part + 'Jnt' + side + '_grp' )
	# i think it no need to constraint
	#armJntGrp_parCons = core.parentConstraint( priorJnt , armJnt_grp )
	#armJntGrp_parCons.name = part + 'Jnt' + side + '_parCons'


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Fk 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #


	part = nameSpace + 'arm'
	type = 'Fk'
	stick_ctrl = core.Dag( part + 'Stick' + side + '_ctrl' )
	stick_ctrl.nmCreateController('stick_ctrlShape')
	stick_ctrl.editCtrlShape( axis = charScale * 1.8 )

	stick_ctrl.color = 'yellow'
	stick_ctrl.hideArnoldNode()

	stickZro_grp = rigTools.zeroGroup( stick_ctrl )
	stickZro_grp.name = part + 'Stick'+ side + 'Zro_grp'

	stickZro_grp.matchPosition( hand_bJnt )
	stickZro_grp.matchRotation( hand_bJnt)

	print'Set rotation to %s controller...' %stick_ctrl.name

	if side == 'LFT':
		stick_ctrl.attr('rotateZ').value +=90

	else:
		stick_ctrl.attr('rotateZ').value -=90
	
	
	# Make stick control follow hand
	armCtrlGrp_parCons = core.parentConstraint( hand_bJnt , stickZro_grp , mo = False)
	armCtrlGrp_parCons.name = part + side + 'Stick'+ '_parCons'
	stick_ctrl.addAttribute( longName = 'handScale' , defaultValue = 1 , keyable = True )

	
	stick_ctrl.attr( 'handScale' ) >> hand_bJnt.attr( 'sx' )
	stick_ctrl.attr( 'handScale' ) >> hand_bJnt.attr( 'sy' )
	stick_ctrl.attr( 'handScale' ) >> hand_bJnt.attr( 'sz' )
	


	# Loch and hide
	stick_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )

	# = = = = = = create Fk  = = = = = = = = #

	# Create fk rig grp
	armFkCtrl_grp = core.Null( part + 'FkCtrl' + side + '_grp' )
	armFkCtrl_grp.snap( priorJnt )
	armFkCtrl_grp.parent( armRig_grp )



	# Create Fk joint grp
	armFkJnt_grp = core.Null( part + 'FkJnt' + side + '_grp' )
	armFkJnt_grp.snap( priorJnt )
	armFkJnt_grp.parent( armJnt_grp )


	# create FK joint
	upperArm_fkJnt = rigTools.jointAt( upperArm )
	lowerArm_fkJnt = rigTools.jointAt( lowerArm )
	hand_fkJnt	 = rigTools.jointAt( hand )

	upperArm_fkJnt.name = nameSpace + 'upperArm' + side + '_fkJnt' 
	lowerArm_fkJnt.name = nameSpace + 'lowerArm' + side + '_fkJnt'
	hand_fkJnt.name = nameSpace + 'hand' + side + '_fkJnt'

	# Set Rotation Axis
	upperArm_fkJnt.rotateOrder = armRotOrder
	upperArm_fkJnt.rotateOrder = armRotOrder
	upperArm_fkJnt.rotateOrder = armRotOrder

	# Parent
	lowerArm_fkJnt.parent( upperArm_fkJnt )
	hand_fkJnt.parent( lowerArm_fkJnt )
	upperArm_fkJnt.parent( armFkJnt_grp )


	# Set rotation order
	upperArm_fkJnt.rotateOrder = armRotOrder
	lowerArm_fkJnt.rotateOrder = armRotOrder
	hand_fkJnt.rotateOrder = armRotOrder




	# Create upperArm
	part = nameSpace + 'upperArm'
	type = 'Fk'
	upperArm_ctrl = core.Dag( part + type + side + '_ctrl' )
	upperArm_ctrl.nmCreateController('fk_ctrlShape')
	upperArmZro_grp = rigTools.zeroGroup( upperArm_ctrl )
	upperArmZro_grp.name = part + type + side + 'Zro_grp'
	upperArm_ctrl.editCtrlShape( axis = charScale * 0.9 )

	if side == 'RGT':
		upperArm_ctrl.flipCtrlShape(axis = 'Y')

	upperArmGmbl_ctrl = core.createGimbal( upperArm_ctrl )

	

	upperArm_ctrl.color = colorSide
	upperArm_ctrl.rotateOrder = armRotOrder
	upperArmGmbl_ctrl.rotateOrder = armRotOrder

	# Parenting and positioning
	upperArmZro_grp.matchPosition( upperArm_fkJnt )
	upperArmZro_grp.matchRotation( upperArm_fkJnt )

	# Parent Constraint 
	upperArmFkJnt_parCons = core.parentConstraint( upperArmGmbl_ctrl , upperArm_fkJnt )
	upperArmFkJnt_parCons.name = part + type + side + '_parCons'
	# Scale Constraint 
	upperArmFkJnt_scaleCons = core.scaleConstraint( upperArmGmbl_ctrl , upperArm_fkJnt )
	upperArmFkJnt_scaleCons.name = part + type + side + '_scaleCons'



	# Create upperArm
	part = nameSpace + 'lowerArm'
	lowerArm_ctrl = core.Dag( part + type + side + '_ctrl' )
	lowerArm_ctrl.nmCreateController('fk_ctrlShape')
	lowerArmZro_grp = rigTools.zeroGroup( lowerArm_ctrl )
	lowerArmZro_grp.name = part + type + side + 'Zro_grp'
	lowerArm_ctrl.editCtrlShape( axis = charScale * 0.8 )

	if side == 'RGT':
		lowerArm_ctrl.flipCtrlShape(axis = 'Y')

	lowerArmGmbl_ctrl = core.createGimbal( lowerArm_ctrl )
	
	lowerArm_ctrl.color = colorSide
	lowerArm_ctrl.rotateOrder = armRotOrder
	lowerArmGmbl_ctrl.rotateOrder = armRotOrder

	# Parenting and positioning
	lowerArmZro_grp.matchPosition( lowerArm_fkJnt )
	lowerArmZro_grp.matchRotation( lowerArm_fkJnt )

	# Constraint
	lowerArmFkJnt_parCons = core.parentConstraint( lowerArmGmbl_ctrl , lowerArm_fkJnt )
	lowerArmFkJnt_parCons.name = part + type + side + '_parCons'
	# Scale Constraint 
	lowerArmFkJnt_scaleCons = core.scaleConstraint( lowerArmGmbl_ctrl , lowerArm_fkJnt )
	lowerArmFkJnt_scaleCons.name = part + type + side + '_scaleCons'



	# Create upperArm
	part = nameSpace + 'hand'
	hand_ctrl = core.Dag( part + type + side + '_ctrl' )
	hand_ctrl.nmCreateController('fk_ctrlShape')
	handZro_grp = rigTools.zeroGroup( hand_ctrl )
	handZro_grp.name = part + type + side + 'Zro_grp'
	hand_ctrl.editCtrlShape( axis = charScale * 0.7 )
	
	if side == 'RGT':
		hand_ctrl.flipCtrlShape(axis = 'Y')

	handGmbl_ctrl = core.createGimbal( hand_ctrl )
	hand_ctrl.color = colorSide
	hand_ctrl.rotateOrder = armRotOrder
	handGmbl_ctrl.rotateOrder = armRotOrder

	# Parenting and positioning
	handZro_grp.matchPosition( hand_fkJnt )
	handZro_grp.matchRotation( hand_fkJnt )

	# Constraint
	handFkJnt_parCons = core.parentConstraint( handGmbl_ctrl , hand_fkJnt )
	handFkJnt_parCons.name = part + type + side + 'Jnt_parCons'
	# Scale Constraint 
	handFkJnt_scaleCons = core.scaleConstraint( handGmbl_ctrl , hand_fkJnt )
	handFkJnt_scaleCons.name = part + type + side + 'Jnt_scaleCons'

	# Parent upper ,lower and hand
	handZro_grp.parent( lowerArmGmbl_ctrl )
	lowerArmZro_grp.parent( upperArmGmbl_ctrl )
	# Parent UpperArm to All fk ctrl 
	upperArmZro_grp.parent( armFkCtrl_grp )


	# Add local world to upper arm
	# = = = = = = = = = = = = = #
	#  Local / World setup 
	# = = = = = = = = = = = = = #
	# [0] controller itself
	# [1] local group space
	# [2] world group space
	# [3] zero group of controller
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( upperArm_ctrl , armFkCtrl_grp , parentTo , upperArmZro_grp.name )
	# Set name
	Loc_grp.name = part  + type + side+ 'Local_grp'
	World_grp.name = part  + type + side+ 'World_grp'
	WorldGrp_orientCons.name = part  + type + side+ 'WorldGrp_orientCons'
	ZroGrp_orientCons.name = part  + type + side+ 'ZroGrp_orientCons'
	reverseNode_rev.name = part  + type + side+ 'ZroGrpOrientCons_rev'


	#upperArm_fkJnt.parent( armFkJnt_grp )



	print '\n # = = = = = = = = End of %s %s %s Rig = = = = = = = = = = # ' %(type,part,side)




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  ik 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	# = = = = = = create IK rig grp = = = = = = = = #
	part = nameSpace + 'arm'
	ctrlType = 'Ik'

	# Create ik rig grp
	armIkCtrl_grp = core.Null( part + ctrlType + 'Ctrl' + side + '_grp' )
	armIkCtrl_grp.snap( priorJnt )
	armIkCtrl_grp.parent( armRig_grp )

	# Create ik joint grp
	armIkJnt_grp = core.Null( part + ctrlType + 'Jnt' + side + '_grp' )
	armIkJnt_grp.snap( priorJnt )
	armIkJnt_grp.parent( armJnt_grp )

	# create ik joint
	upperArm_IkJnt = rigTools.jointAt( upperArm )
	lowerArm_IkJnt = rigTools.jointAt( lowerArm )
	hand_IkJnt	 = rigTools.jointAt( hand )

	upperArm_IkJnt.name = nameSpace + 'upperArm' + side + '_ikJnt' 
	lowerArm_IkJnt.name = nameSpace + 'lowerArm' + side + '_ikJnt'
	hand_IkJnt.name = nameSpace + 'hand' + side + '_ikJnt'

	# Parent
	lowerArm_IkJnt.parent( upperArm_IkJnt )
	hand_IkJnt.parent( lowerArm_IkJnt )
	upperArm_IkJnt.parent( armIkJnt_grp )

	# Set rotation order
	upperArm_IkJnt.rotateOrder = armRotOrder
	lowerArm_IkJnt.rotateOrder = armRotOrder
	hand_IkJnt.rotateOrder = armRotOrder

	# assign this to old name to the old procress
	uprIK = upperArm_IkJnt.name
	midIK = lowerArm_IkJnt.name
	lwrIK = hand_IkJnt.name

	ikJntLst = (uprIK,midIK,lwrIK)

	# Create IK handle 
	ikhName = mc.ikHandle( name = part + side + '_handle', startJoint = ikJntLst[0], endEffector = ikJntLst[2], solver = 'ikRPsolver' )
	mc.rename( ikhName[1] , lwrIK + '_eff')
	ikhNam = ikhName[0]
	# hide Ik handle
	mc.setAttr( ikhNam + ".visibility" ,0)



	# ===== Create ik controller
	name = nameSpace + 'hand'
	handIk_ctrl = core.Dag( name +'Ik'+ side + '_ctrl' )
	handIk_ctrl.nmCreateController('cube_ctrlShape')
	handIk_ctrl.editCtrlShape( axis = charScale * 4.6 )
	handIk_ctrl.setColor(colorSide)
	# Create Attr
	handIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'autoStretch' 	, k = True , minValue = 0 , maxValue = 1 ,dv = 0 )
	handIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True  ,dv = 0 )
	# handIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True , minValue = -500 ,dv = 0 )
	handIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'lowStretch' 	, k = True  ,dv = 0 )
	handIk_ctrl.hideArnoldNode()


	ikGmbl_ctrl = core.createGimbal( handIk_ctrl )

	# Create zero grp
	ikZro_grp = rigTools.zeroGroup( handIk_ctrl )
	ikZro_grp.name = ( name +'Ik'+ side + 'Zro_grp' )

	# Parent under zro grp
	#mc.parent( handIk_ctrl.name , ikZro_grp.name  )

	# Fix to point prosition cause of this is ik handle it should be world orientation
	
	# waiting for animator summary
	misc.snapParentConst( ikJntLst[2]  , ikZro_grp.name )
	# misc.snapPointConst( ikJntLst[2]  , ikZro_grp.name )

	# Make ikJnt rotation following  hand ik controll     
	# handIkRotation = core.orientConstraint( handIk_ctrl , hand_IkJnt  , mo = True )
	handIkRotation = core.orientConstraint( ikGmbl_ctrl , hand_IkJnt  , mo = True )
	handIkRotation.name = name + ctrlType + side + '_orientCons'

	# Parent ik handle under ik ctrl
	mc.parent( ikhNam ,  ikGmbl_ctrl.name )



	# Pole vector
	tmpPov = tmpJnt[3]
	# Create pov and parent
	rawPov = misc.splitName( tmpPov )
	print   rawPov[1]
	povZro_grp = mc.group(em = True , name = nameSpace + 'elbow' +'Pov'+ side + 'Zro_grp' )	
	# Create POV Controller
	name = nameSpace + rawPov[1]
	pov_ctrl = core.Dag( nameSpace + 'elbow' +'Pov'+ side + '_ctrl' )
	pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')
	pov_ctrl.editCtrlShape( axis = charScale * 0.8 )
	pov_ctrl.setColor('yellow')

	mc.parent( pov_ctrl.name , povZro_grp  )
	misc.snapParentConst( tmpPov , povZro_grp )
	# misc.snapPointConst( tmpPov , povZro_grp )

	mc.poleVectorConstraint ( pov_ctrl.name , ikhName[0] , w = 1 ,name = nameSpace + 'elbow' + side + '_povCons')
	mc.parent( povZro_grp , ikGmbl_ctrl.name )	




	# ========== # create local / world for Pole Vector
	partName = nameSpace + 'elbow'
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.parentLocalWorldCtrl( pov_ctrl , ikGmbl_ctrl , parentTo , povZro_grp , partName )
	Loc_grp.name = partName + side + 'Local_grp'
	World_grp.name = partName + side + 'World_grp'
	WorldGrp_orientCons.name = partName + side + 'WorldGrp_parCons'
	ZroGrp_orientCons.name = partName + side + 'ZroGrp_parCons'
	reverseNode_rev.name = partName + side + 'ZroGrpParCons_rev'


	
	# ========== # create root IK Controller
	# rootName = upperArm_bJnt.name.split('_')[0][:-3]

	rootName = upperArm_bJnt.name.split('_')


	# Split name condition
	if len(rootName) == 2:
		rootName = rootName[0]
	elif len(rootName) == 3:
		rootName = rootName[0] + '_' + rootName[1]
	elif len(rootName) == 4:
		rootName = rootName[0] + '_' + rootName[1] + '_' + rootName[2]


	rootName = nameSpace + 'upperArm' + 'Ik' + side 
	# rootName =  rootName + 'Ik' 
	# rootName = rootName + 'Ik' + side + 'testTest'

	ikRoot_ctrl = core.Dag(rootName + '_ctrl')
	ikRoot_ctrl.nmCreateController('cube_ctrlShape')
	# ikRoot_ctrl.setColor(colorSide)
	ikRoot_ctrl.setColor('yellow')
	ikRoot_ctrl.editCtrlShape( axis = charScale * 5.5 )

	ikRootGmbl_ctrl = core.createGimbal( ikRoot_ctrl )

	IkRootZro_grp = rigTools.zeroGroup( ikRoot_ctrl )
	IkRootZro_grp.name = rootName + 'Zro_grp'
	IkRootZro_grp.snap(upperArm_bJnt)


	# ========== # constraint to bind joint
	part = nameSpace + 'arm'
	rootIk_parCons = core.parentConstraint( ikRootGmbl_ctrl , upperArm_IkJnt.name   )
	rootIk_parCons.name = part + side + 'Jnt_parCons'



	# Create ik stretchy
	pmaNode = create.iKStretch(	ikJnt = (    upperArm_IkJnt.name , lowerArm_IkJnt.name , hand_IkJnt.name )  , ikCtrl = ( ikRoot_ctrl.name , handIk_ctrl.name ) , part = name	,  
								side = side, scaleCtrl = 'placement_ctrl', noTouchGrp = noTouchGrp, povPosi = povPosi  )


	

	# Create attr FK/Ik switch attr
	stick_ctrl.addAttribute( attributeType = 'float' , longName = 'FK_IK' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )
	# Exclude POV joint

	print rawName
	namJnt = rawName[:-1]
	placementCtrl = stick_ctrl.name

	print ''' \n
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create parentMulMatrix
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	'''
	# Pair constraint each of bind joint to FK and IK
	for each in namJnt:

		print '### Naming joint'
		print  each + side +'_fkJnt\n'
		print  each + side +'_ikJnt\n'
		print  each + side +'_bJnt\n'
		matrixWt_node = misc.parentMulMatrix( [ each + side +'_fkJnt' , each + side +'_ikJnt' ] ,  each + side +'_bJnt' ,w = True, mo = False, t = True, r = True, s = True)
		revNode = mc.createNode('reverse' , name = each + 'Switch' + side + '_rev')
		
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , revNode + '.inputX'  )
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , matrixWt_node + '.wtMatrix[1].weightIn'  ) 
		mc.connectAttr( revNode + '.outputX'  , matrixWt_node + '.wtMatrix[0].weightIn'   ) 




	
	# Parent to main grp
	armJnt_grp.parent( jnt_grp )
	armJnt_grp.attr('visibility').value = 0
	armRig_grp.parent( parentTo )
	stickZro_grp.parent( parentTo )
	ikZro_grp.parent( ikhGrp )
	IkRootZro_grp.parent( armIkCtrl_grp )


	# Switch visibility each FK/IK
	stickVis_rev = core.Reverse()
	stickVis_rev.name = part + 'StickVis' + side + '_rev'

	# Fk switch
	stick_ctrl.attr('FK_IK') >> stickVis_rev.attr('inputX')
	stickVis_rev.attr('outputX') >> armFkCtrl_grp.attr('visibility')


	stick_ctrl.attr('FK_IK') >> ikZro_grp.attr('visibility')
	stick_ctrl.attr('FK_IK') >> IkRootZro_grp.attr('visibility')

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Lock and hide attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	handIk_ctrl.lockHideAttrLst( 'sx' , 'sy' , 'sz' , 'v' )
	ikRoot_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	ikRootGmbl_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	ikRoot_ctrl.setColor(colorSide)
	pov_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	ikGmbl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'v')

	print ''' \n
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create Null Snap group for matcher
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	'''

	offset_null = core.Null( part + 'Offset' + side + '_null')
	# offset_null.maSnap( hand_bJnt , rotation = False)
	offset_null.maSnap( hand_bJnt, position = True , rotation = True , scale = True )
	offset_parCons = core.parentConstraint( hand_bJnt , offset_null , mo = True)
	offset_parCons.name = part + 'Offset' + side + '_parCons'

	offset_null.parent( nullGrp )



	print ''' \n
	# = = = = = = Create elbow knee Lock Rig function
	'''
	rawNameUPR , distanceUPRName , povUPR_Ctrl , lowerUPR_loc , upperUPR_loc = midLockModule.createDistance( nameSpace , startP = ikRootGmbl_ctrl.name , endP = pov_ctrl.name )
	rawNameLWR , distanceLWRName , povLWR_Ctrl , lowerLWR_loc , upperLWR_loc = midLockModule.createDistance( nameSpace , startP = pov_ctrl.name , endP = ikGmbl_ctrl.name )
	blendName,invertNodeName  = midLockModule.createBlendColor(         nameSpace ,
										uprDistance = distanceUPRName		, 
										lwrDistance = distanceLWRName 	,
										side 		=  side   ,
										uprNam 		= rawNameUPR	           )

	attrName = midLockModule.doAddAttr( povUPR_Ctrl , rawNameUPR  )
	midLockModule.connectIkJnt(	stretchNode = pmaNode , upperIKJnt = lowerArm_IkJnt.name , lowerIKJnt = hand_IkJnt.name , blendName = blendName , namLock = attrName	, povName = povUPR_Ctrl )



	print ''' \n
	# = = = = = = Create ribbon Rig function
	'''



	if ribbon == True:
		if ribbonRes == 'high':
			numJoints = 5
		else:
			numJoints = 3

		hingesUprBtm = ribbonRig.ribbonRig(
			nameSpace = nameSpace		,
			width = 10								,
			numJoints = numJoints							,
			side = side								,
			jointTop = upperArm_bJnt.name			,
			jointBtm = lowerArm_bJnt.name			,
			part = 'upArm'							,
			charScale = charScale					,
			noTouch_grp = noTouchGrp				,
			showInfo = showInfo  					,
			ctrl_grp = armRig_grp.name )

	

		hingesLwrTop = ribbonRig.ribbonRig(
				nameSpace = nameSpace		,
				width = 10								,
				numJoints = numJoints							,
				side = side								,
				jointTop = lowerArm_bJnt.name			,
				jointBtm = hand_bJnt.name				,
				part = 'lwrArm'							,
				charScale = charScale					,
				noTouch_grp = noTouchGrp				,
				showInfo = showInfo  					,
				ctrl_grp = armRig_grp.name )

		
		ribbonRig.makeHigesMover( part = 'arm', 		nameSpace = nameSpace		,
														side = side 				, 
														btmName = hingesUprBtm		, 
														topName = hingesLwrTop 		 , 
														charScale = charScale		,
														moverPosition = lowerArm_bJnt.name	,
														ctrl_grp = 'ctrl_grp'		
															)
		




	print '\n\n\n\n\n\n #### End of %s %s Rig ####' %(part,side)


	return stick_ctrl.name , hand_bJnt.name
	#return armRig_grp.name
	
