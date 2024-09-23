#... 
#... Create FK/IK switch 


import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc
reload( misc )

# from function.rigging.autoRig.bodyRig import ribbonRig
# reload( ribbonRig )

from function.rigging.autoRig.bodyRig import ribbonRigExt as ribbonRig
reload( ribbonRig )

from function.rigging.autoRig.bodyRig import midLockModule
reload( midLockModule )

from function.rigging.autoRig.bodyRig import createIKStretch as create
reload( create )

from function.rigging.autoRig.bodyRig import createSoftIk as softIkfunc
reload( softIkfunc )

from function.rigging.tools import proc as pc
reload(pc)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

from function.rigging.autoRig.bodyRig import twistRig as tr
reload(tr)

import sys

import logging

logger = logging.getLogger('fkIkTwistRig')
logger.setLevel(logging.DEBUG)

hastag = '# '*20







def fkIkTwistGenRig(

				nameSpace = '' 	,				
				charScale = 1	,			
				parentTo = 'ctrl_grp' 	,			
				side = 'LFT'	,
				region = 'arm'		,							
				tmpJnt = (	'upperArmLFT_tmpJnt' ,	
						'lowerArmLFT_tmpJnt', 	 
						'handLFT_tmpJnt' ,	
						'armPovLFT_tmpJnt' ),
				priorJnt = 'clavLFT_bJnt'	,	
				ikhGrp = 'ikh_grp'		,			
				noTouchGrp = 'noTouch_grp' ,			
				nullGrp = 'snapNull_grp',			
				jnt_grp =  'jnt_grp'	,
				showInfo = False ,
				ribbon = True,	
				ribbonRes = 'low',
				ribbonName = ('upLeg', 'lwrLeg'),
				propCtrl = False,
				keepFkIkBoth = False,	
				povShape = 'sphereAxis',
				ikPosi = None ,
				linkRotOrder = False ,
				#... creTwistJnt is obsolete it cause fk <> ik pair not work
				ctrlShape = 'fk_ctrlShape', #... ctrl shape for fk ctrl only
				creTwistJnt = True ,
				# softIk = False ,
				stickShape = 'stickCircle_Y_long_ctrlShape',
				alongAxis = 'y' ,
				pinMethod = 'matrix',
				povPosi = 'front'
				):	#... stick_ctrlShape , 	gear_ctrlShape	
				
				
	core.makeHeader(	'Start of %s%s Rig' %(region,side)	)		
	# 	Define name of each three section
	#	Warning do not change joint index 
	# 
	#	up			mid 		low
	#	[0]==========[1]=========[2] >> hand or ankle
	#				  :
	#				  :
	#				  :
	#				 [3]
	#				 pov




	#... Define prior meta node
	root_meta = 'root_meta'

	if side == 'LFT':
		colorSide = 'red'
	elif side == 'RGT':
		colorSide = 'blue'
	else:
		colorSide = 'yellow'


	# rotOrder = 'yxz'
	# change because of auto twist having flip problem
	rotOrder = 'xzy'

	if tmpJnt:
		upper = core.Dag( nameSpace + tmpJnt[ 0 ] )
		mid = core.Dag(   nameSpace + tmpJnt[ 1 ] )
		low = core.Dag(  nameSpace + tmpJnt[ 2 ] )
		poleVec = core.Dag(  nameSpace + tmpJnt[ 3 ] )


		# Naming bind joint
		upper_bJnt = rigTools.jointAt( upper )
		middle_bJnt = rigTools.jointAt( mid )
		# There is no need to make pov joint just passing name of template joint
		#poleVec_bJnt = rigTools.jointAt( poleVec )
		lower_bJnt = rigTools.jointAt( low )

		if region == 'arm':
			# Set joint label
			upper_bJnt.setLable( side,'shoulder')
			middle_bJnt.setLable( side,'elbow')
			lower_bJnt.setLable( side ,'hand')
			
		elif region == 'leg':
			upper_bJnt.setLable( side ,'none')
			middle_bJnt.setLable( side ,'none')
			lower_bJnt.setLable( side ,'foot')

		else:
			pass


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Store raw name
	# Result : extract side for name
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	rawName = []
	# if having side 
	if side:
		for each in tmpJnt:
				tmp = each.split('_')[0][:-3]
				rawName.append(tmp)





		upper_bJnt.name = nameSpace + rawName[0] + side + '_bJnt'
		middle_bJnt.name = nameSpace + rawName[1]  + side + '_bJnt'
		#poleVec_bJnt.name = 'poleVec' + side + '_bJnt' # don wanna create POV
		lower_bJnt.name = nameSpace + rawName[2]  + side + '_bJnt'


	else:
		mc.error('Not Enought Arg to Process...')
		# return None
















	#... Adjust rotate order
	upper_bJnt.rotateOrder = rotOrder
	middle_bJnt.rotateOrder = rotOrder
	lower_bJnt.rotateOrder = rotOrder

	#... Parent joint
	middle_bJnt.parent( upper_bJnt )
	lower_bJnt.parent( middle_bJnt )



	# Parent it to prior joint
	upper_bJnt.parent( priorJnt )
















	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create main rig grp
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# change name of rig grp that use region to variable name
	# part = nameSpace + region
	part = nameSpace + rawName[2]

	fkIkRig_grp = core.Null( part + 'Rig' + side + '_grp' )
	fkIkRigGrp_parCons = core.parentConstraint( priorJnt , fkIkRig_grp )
	fkIkRigGrp_parCons.name = part + 'Rig' + side + '_parCons'

	# Create joint grp
	fkIkJnt_grp = core.Null( part + 'Jnt' + side + '_grp' )






	type = 'Fk'


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create stick controller
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #




	stickName = rawName[2] + 'Stick'
	stick_ctrl = core.Dag( nameSpace + stickName + side + '_ctrl' )
	stick_ctrl.nmCreateController(stickShape)
	stick_ctrl.editCtrlShape( axis = charScale * 1.8 )

	stick_ctrl.color = 'yellow'
	stick_ctrl.hideArnoldNode()

	stickZro_grp = rigTools.zeroGroup( stick_ctrl )
	stickZro_grp.name = nameSpace + stickName + side + 'Zro_grp'

	stickZro_grp.matchPosition( lower_bJnt )
	stickZro_grp.matchRotation( lower_bJnt)

	print ('Set rotation to %s controller...' %stick_ctrl.name)



	logger.info(hastag)
	logger.info(region)

	# Condition for create orientation of stick ctrl
	if region == 'leg' or region == 'frontLeg' or region == 'backLeg':
		if side == 'LFT':
			stick_ctrl.attr('rotateX').value = -90
		elif side == 'RGT':
			stick_ctrl.attr('rotateX').value = 90


	elif region == 'arm':
		if side == 'LFT':
			stick_ctrl.attr('rotateZ').value = 90

		elif side == 'RGT':
			stick_ctrl.attr('rotateZ').value = -90



	# Make stick control follow lower
	fkIkCtrlGrp_parCons = core.parentConstraint( lower_bJnt , stickZro_grp , mo = False)
	fkIkCtrlGrp_parCons.name = part + side + 'Stick'+ '_parCons'

	# Attr scale name
	if region == 'arm':
		stickScalNam = 'hand'
	else:
		stickScalNam = region

	attScaleName = stickScalNam +'Scale'
	stick_ctrl.addAttribute( longName = attScaleName , defaultValue = 1 , keyable = True )

	# * * * * * * ** 
	# Test to get rid of rotation value
	# upper_bJnt.freeze()	

	# shift this connection to another at end line
	'''
	stick_ctrl.attr( attScaleName ) >> lower_bJnt.attr( 'sx' )
	stick_ctrl.attr( attScaleName ) >> lower_bJnt.attr( 'sy' )
	stick_ctrl.attr( attScaleName ) >> lower_bJnt.attr( 'sz' )
	'''

	# Lock and hide
	stick_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )



	#... freeze bind joint (Why freeze scale seqment is turn on again)
	upper_bJnt.freeze()
	middle_bJnt.freeze()
	lower_bJnt.freeze()

	#... Disable Segment scale conpensate
	upper_bJnt.attr('segmentScaleCompensate').value = 0
	middle_bJnt.attr('segmentScaleCompensate').value = 0
	lower_bJnt.attr('segmentScaleCompensate').value = 0






	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Create Fk 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# = = = = = =   = = = = = = = = #

	# Create fk rig grp
	fkCtrl_grp = core.Null( part + 'FkCtrl' + side + '_grp' )
	fkCtrl_grp.snap( priorJnt )
	fkCtrl_grp.parent( fkIkRig_grp )


	# Create Fk joint grp
	fkJnt_grp = core.Null( part + 'FkJnt' + side + '_grp' )
	fkJnt_grp.snap( priorJnt )
	fkJnt_grp.parent( fkIkJnt_grp )


	# create FK joint
	upper_fkJnt = rigTools.jointAt( upper_bJnt )
	middle_fkJnt = rigTools.jointAt( middle_bJnt )
	lower_fkJnt	 = rigTools.jointAt( lower_bJnt )

	upper_fkJnt.name = nameSpace + rawName[0] + side + '_fkJnt' 
	middle_fkJnt.name = nameSpace + rawName[1] + side + '_fkJnt'
	lower_fkJnt.name = nameSpace + rawName[2] + side + '_fkJnt'

	# Parent
	middle_fkJnt.parent( upper_fkJnt )
	lower_fkJnt.parent( middle_fkJnt )
	upper_fkJnt.parent( fkJnt_grp )


	# add color and adjust radius
	upper_fkJnt.setJointColor('softGray')
	middle_fkJnt.setJointColor('softGray')
	lower_fkJnt.setJointColor('softGray')

	upper_fkJnt.attr( 'radius' ).value = 2
	middle_fkJnt.attr( 'radius' ).value = 2
	lower_fkJnt.attr( 'radius' ).value = 2



	# Set rotation order
	upper_fkJnt.rotateOrder = rotOrder
	middle_fkJnt.rotateOrder = rotOrder
	lower_fkJnt.rotateOrder = rotOrder





	# Create upper
	part = nameSpace + rawName[0]
	type = 'Fk'
	upper_ctrl = core.Dag( part + type + side + '_ctrl' )
	upper_ctrl.nmCreateController(ctrlShape)
	upperZro_grp = rigTools.zeroGroup( upper_ctrl )
	upperZro_grp.name = part + type + side + 'Zro_grp'
	upper_ctrl.editCtrlShape( axis = charScale * 0.9 )

	if side == 'RGT':
		upper_ctrl.flipCtrlShape(axis = 'Y')

	upperGmbl_ctrl = core.createGimbal( upper_ctrl )
	upper_ctrl.color = colorSide

	# adjust rotate order
	upper_ctrl.rotateOrder = rotOrder
	upperGmbl_ctrl.rotateOrder = rotOrder


	# Parenting and positioning
	upperZro_grp.matchPosition( upper_fkJnt )
	upperZro_grp.matchRotation( upper_fkJnt )

	# Parent Constraint 
	upperFkJnt_parCons = core.parentConstraint( upperGmbl_ctrl , upper_fkJnt )
	upperFkJnt_parCons.name = part + type + side + '_parCons'
	# Scale Constraint 
	upperFkJnt_scaleCons = core.scaleConstraint( upperGmbl_ctrl , upper_fkJnt )
	upperFkJnt_scaleCons.name = part + type + side + '_scaleCons'



	# Create middle
	part = nameSpace + rawName[1]
	middle_ctrl = core.Dag( part + type + side + '_ctrl' )
	middle_ctrl.nmCreateController(ctrlShape)
	middleZro_grp = rigTools.zeroGroup( middle_ctrl )
	middleZro_grp.name = part + type + side + 'Zro_grp'
	middle_ctrl.editCtrlShape( axis = charScale * 0.8 )

	if side == 'RGT':
		middle_ctrl.flipCtrlShape(axis = 'Y')

	middleGmbl_ctrl = core.createGimbal( middle_ctrl )

	middle_ctrl.color = colorSide
	middle_ctrl.rotateOrder = rotOrder
	middleGmbl_ctrl.rotateOrder = rotOrder

	# Parenting and positioning
	middleZro_grp.matchPosition( middle_fkJnt )
	middleZro_grp.matchRotation( middle_fkJnt )

	# Constraint
	middleFkJnt_parCons = core.parentConstraint( middleGmbl_ctrl , middle_fkJnt )
	middleFkJnt_parCons.name = part + type + side + '_parCons'
	# Scale Constraint 
	middleFkJnt_scaleCons = core.scaleConstraint( middleGmbl_ctrl , middle_fkJnt )
	middleFkJnt_scaleCons.name = part + type + side + '_scaleCons'



	# Create lower
	part = nameSpace + rawName[2]
	lower_ctrl = core.Dag( part + type + side + '_ctrl' )
	lower_ctrl.nmCreateController(ctrlShape)
	lowerZro_grp = rigTools.zeroGroup( lower_ctrl )
	lowerZro_grp.name = part + type + side + 'Zro_grp'
	lower_ctrl.editCtrlShape( axis = charScale * 0.7 )

	if side == 'RGT':
		lower_ctrl.flipCtrlShape(axis = 'Y')

	lowerGmbl_ctrl = core.createGimbal( lower_ctrl )
	lower_ctrl.color = colorSide
	lower_ctrl.rotateOrder = rotOrder
	lowerGmbl_ctrl.rotateOrder = rotOrder


	if linkRotOrder:
		upper_ctrl.addRotEnum()
		upperGmbl_ctrl.addRotEnum()
		middle_ctrl.addRotEnum()
		middleGmbl_ctrl.addRotEnum()
		lower_ctrl.addRotEnum()
		lowerGmbl_ctrl.addRotEnum()

	# Parenting and positioning
	lowerZro_grp.matchPosition( lower_fkJnt )
	lowerZro_grp.matchRotation( lower_fkJnt )

	# Constraint
	lowerFkJnt_parCons = core.parentConstraint( lowerGmbl_ctrl , lower_fkJnt , mo = True)
	lowerFkJnt_parCons.name = part + type + side + 'Jnt_parCons'
	# Scale Constraint 
	lowerFkJnt_scaleCons = core.scaleConstraint( lowerGmbl_ctrl , lower_fkJnt ,mo = True)
	lowerFkJnt_scaleCons.name = part + type + side + 'Jnt_scaleCons'

	# Parent upper ,lower and lower
	lowerZro_grp.parent( middleGmbl_ctrl )
	middleZro_grp.parent( upperGmbl_ctrl )
	# Parent UpperArm to All fk ctrl 
	upperZro_grp.parent( fkCtrl_grp )


	# Add local world to upper arm
	# = = = = = = = = = = = = = #
	#  Local / World setup 
	# = = = = = = = = = = = = = #
	# [0] controller itself
	# [1] local group space
	# [2] world group space
	# [3] zero group of controller
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( upper_ctrl , fkCtrl_grp , parentTo , upperZro_grp.name )

	# Set name
	Loc_grp.name = part  + type + side+ 'Local_grp'
	World_grp.name = part  + type + side+ 'World_grp'
	WorldGrp_orientCons.name = part  + type + side+ 'WorldGrp_orientCons'
	ZroGrp_orientCons.name = part  + type + side+ 'ZroGrp_orientCons'
	reverseNode_rev.name = part  + type + side+ 'ZroGrpOrientCons_rev'



	print ('\n # = = = = = = = = End of %s %s %s Rig = = = = = = = = = = # ' %(type,part,side))




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  ik 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	# = = = = = = create IK rig grp = = = = = = = = #
	# old 
	# part = nameSpace + region
	part = nameSpace + rawName[2]
	ctrlType = 'Ik'

	# Create ik rig grp
	ikCtrl_grp = core.Null( part + ctrlType + 'Ctrl' + side + '_grp' )
	ikCtrl_grp.snap( priorJnt )
	ikCtrl_grp.parent( fkIkRig_grp )

	# Create ik joint grp
	ikJnt_grp = core.Null( part + ctrlType + 'Jnt' + side + '_grp' )
	ikJnt_grp.snap( priorJnt )
	ikJnt_grp.parent( fkIkJnt_grp )

	# create ik joint
	# upper_IkJnt = rigTools.jointAt( upper_bJnt , orient = False)
	upper_IkJnt = rigTools.jointAt( upper_bJnt )
	middle_IkJnt = rigTools.jointAt( middle_bJnt )
	lower_IkJnt	 = rigTools.jointAt( lower_bJnt )

	# add color and adjust radius
	upper_IkJnt.setJointColor('softGray')
	middle_IkJnt.setJointColor('softGray')
	lower_IkJnt.setJointColor('softGray')

	upper_IkJnt.attr( 'radius' ).value = 2
	middle_IkJnt.attr( 'radius' ).value = 2
	lower_IkJnt.attr( 'radius' ).value = 2

	upper_IkJnt.name = nameSpace + rawName[0] + side + '_ikJnt' 
	middle_IkJnt.name = nameSpace + rawName[1] + side + '_ikJnt'
	lower_IkJnt.name = nameSpace + rawName[2] + side + '_ikJnt'

	# Parent
	middle_IkJnt.parent( upper_IkJnt )
	lower_IkJnt.parent( middle_IkJnt )
	upper_IkJnt.parent( ikJnt_grp )

	# Set rotation order
	upper_IkJnt.rotateOrder = rotOrder
	middle_IkJnt.rotateOrder = rotOrder
	lower_IkJnt.rotateOrder = rotOrder

	# assign this to old name to the old procress
	uprIK = upper_IkJnt.name
	midIK = middle_IkJnt.name
	lwrIK = lower_IkJnt.name

	# qury name
	ikJntLst = (uprIK,midIK,lwrIK)
	part = nameSpace + rawName[2]

	# Create IK lower 
	ikhName = mc.ikHandle( name = part + ctrlType + side + '_ikh', startJoint = ikJntLst[0], endEffector = ikJntLst[2], solver = 'ikRPsolver' )
	mc.rename( ikhName[1] , lwrIK + '_eff')
	ikhNam = ikhName[0]
	# hide Ik lowerle
	mc.setAttr( ikhNam + ".visibility" ,0)



	# ===== Create ik controller
	name = nameSpace  + rawName[2] # arm , ankle
									 #[ik]
	lowerIk_ctrl = core.Dag( name + ctrlType + side + '_ctrl' )




	#
	#	 Insert condition for IK controller shape
	# 

	if not ikPosi:
		lowerIk_ctrl.nmCreateController('cube_ctrlShape')
		lowerIk_ctrl.editCtrlShape( axis = charScale * 3 )
	elif ikPosi == 'foot':
		lowerIk_ctrl.nmCreateController('squarePlain_ctrlShape')
	elif ikPosi == 'ankle':
		ankleIk_ctrl.nmCreateController('cube_ctrlShape')
	else:
		lowerIk_ctrl.nmCreateController('squarePlain_ctrlShape')



	#... No need anymore
	# lowerIk_ctrl.editCtrlShape( axis = charScale * 5 )
	# print('This is error for sure')
	logger.debug('589')
	lowerIk_ctrl.setColor( colorSide )
	
	logger.debug('591')
	# Create Attr
	lowerIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'autoStretch' 	, k = True , minValue = 0 , maxValue = 1 ,dv = 0 )
	lowerIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True  ,dv = 0 )
	lowerIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'lowStretch' 	, k = True  ,dv = 0 )
	lowerIk_ctrl.hideArnoldNode()

	logger.debug('598')
	ikGmbl_ctrl = core.createGimbal( lowerIk_ctrl )
	logger.debug('601')
	# Create zero grp
	ikZro_grp = rigTools.zeroGroup( lowerIk_ctrl )
	logger.debug('604')
	ikZro_grp.name = ( name +'Ik'+ side + 'Zro_grp' )


	logger.debug('606')

	# Actually ik should be act to world orientation but this is requirement from animator
	if region == 'arm':# if hand make it along hand orient
		misc.snapParentConst( ikJntLst[2]  , ikZro_grp.name )
	elif region == 'leg':# if leg or another make it orient along world
		misc.snapPointConst( ikJntLst[2]  , ikZro_grp.name )
	else:
		misc.snapPointConst( ikJntLst[2]  , ikZro_grp.name )


	


	# Make ankle or wrist rotate freely
	# Make ikJnt rotation following  lower ik controll     
	# lowerIkRotation = core.orientConstraint( lowerIk_ctrl , lower_IkJnt  , mo = True )
	lowerIkRotation = core.orientConstraint( ikGmbl_ctrl , lower_IkJnt  , mo = True )
	lowerIkRotation.name = name + ctrlType + side + '_orientCons'

	# Parent ik lowerle under ik ctrl
	mc.parent( ikhNam ,  ikGmbl_ctrl.name )

	



	logger.info('\n# ------------------ Prepare Feature SoftIk Start ------------------------------------------------------------------- #')
	
	#... Add zero grp to ikhNam

	ikhZro_grp = mc.group(em = True , name = name + 'Ikh' + side + 'Zro_grp' )
	misc.snapParentConst( lower_bJnt.name  , ikhZro_grp )
	mc.parent( ikhZro_grp ,  ikGmbl_ctrl.name )
	logger.info('parent {0} to {1}'.format(ikhNam,ikhZro_grp))
	mc.parent( ikhNam ,  ikhZro_grp)

	#... Reset ikh orientation
	# mc.rotate(ikhNam, r=True, os=True, fo=True, value=(0, 0, 0))
	mc.rotate( 0, 0, 0, ikhNam, os=True, fo=True )

	logger.info('\n# ------------------ Prepare Feature SoftIk End ------------------------------------------------------------------- #')









	povZro_grp = mc.group(em = True , name = nameSpace + rawName[3] + side + 'Zro_grp' )	
	# Create POV Controller
	# name = nameSpace + tmpPov
	pov_ctrl = core.Dag(  nameSpace + rawName[3] + side  + '_ctrl' )


	if povShape == 'sphereAxis':
		# Change Shape from sphere to pyramid la
		pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')

	elif povShape == 'pyramid':
		pov_ctrl.nmCreateController('pyramid_ctrlShape')
		pov_ctrl.rotateShape( rotate = ( 90 , 0 , 0) )
		# Add pole vector line 
		pc.targetPov( ctrl = pov_ctrl.name , jnt = middle_bJnt.name )



	pov_ctrl.editCtrlShape( axis = charScale * 1.4 )
	pov_ctrl.setColor( colorSide )


	mc.parent( pov_ctrl.name , povZro_grp  )

	# Set oriantation of pov to world
	# misc.snapParentConst( tmpPov , povZro_grp )

	misc.snapPointConst( nameSpace + tmpJnt[3] , povZro_grp )

	mc.poleVectorConstraint ( pov_ctrl.name , ikhName[0] , w = 1 ,name = nameSpace + rawName[0]+'Pov' + side + '_povCons')
	mc.parent( povZro_grp , ikGmbl_ctrl.name )	




	# ========== # create local / world for Pole Vector
	partName = nameSpace + rawName[0]+'Pov'
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.parentLocalWorldCtrl( pov_ctrl , ikGmbl_ctrl , parentTo , povZro_grp , partName ,value = 1)
	Loc_grp.name = partName + side + 'Local_grp'
	World_grp.name = partName + side + 'World_grp'
	WorldGrp_orientCons.name = partName + side + 'WorldGrp_parCons'
	ZroGrp_orientCons.name = partName + side + 'ZroGrp_parCons'
	reverseNode_rev.name = partName + side + 'ZroGrpParCons_rev'


	rootName = nameSpace + rawName[0] + 'IkRoot' + side 

	ikRoot_ctrl = core.Dag(rootName + '_ctrl')
	ikRoot_ctrl.nmCreateController('cube_ctrlShape')
	# ikRoot_ctrl.setColor(colorSide)
	ikRoot_ctrl.setColor('yellow')
	ikRoot_ctrl.editCtrlShape( axis = charScale * 5.5 )

	ikRootGmbl_ctrl = core.createGimbal( ikRoot_ctrl )

	ikRootZro_grp = rigTools.zeroGroup( ikRoot_ctrl )
	ikRootZro_grp.name = rootName + 'Zro_grp'
	ikRootZro_grp.snap(upper_bJnt)


	# ========== # constraint to bind joint
	part = nameSpace + rootName
	rootIk_parCons = core.parentConstraint( ikRootGmbl_ctrl , upper_IkJnt.name   )
	rootIk_parCons.name = part + side + 'Jnt_parCons'



	#------------------------------ Create ik Stretchy -----------------------------#
	stretchNode = create.iKStretch(	ikJnt = (    upper_IkJnt.name , middle_IkJnt.name , lower_IkJnt.name )  , 
								ikCtrl = ( ikRoot_ctrl.name , lowerIk_ctrl.name ) , 
								side = side , scaleCtrl = 'placement_ctrl'	, 
								region = region ,noTouchGrp = noTouchGrp , nameSpace = nameSpace ,
								lowNam = rawName[2], 
								alongAxis = alongAxis,
								povPosi = povPosi
								)
	pmaNode = stretchNode[0]
	psStreEndName = stretchNode[1]



	



	# Create attr FK/Ik switch attr
	stick_ctrl.addAttribute( attributeType = 'float' , longName = 'FK_IK' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )
	if keepFkIkBoth == True:
		stick_ctrl.addAttribute( attributeType = 'bool' , longName = 'fkVis' , minValue = 0 , maxValue = 1 , defaultValue = 1 , keyable = True )
		stick_ctrl.addAttribute( attributeType = 'bool' , longName = 'ikVis' , minValue = 0 , maxValue = 1 , defaultValue = 1 , keyable = True )




	# Exclude POV joint
	logger.info(hastag)
	logger.info(rawName)
	#namJnt = rawName[:-1] # WARNING Solid method it will error when run with list more than three 
	rawName = [	'{0}{1}'.format( nameSpace ,rawName[0] ), '{0}{1}'.format(nameSpace,rawName[1]), '{0}{1}'.format(nameSpace,rawName[2])	]

	placementCtrl = stick_ctrl.name
	logger.info(hastag)














	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create buffer joint 
	# Result : ik and fk joint >>> buffer joint >>> twist joint >>> bind joint
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	part = nameSpace + region


	# Create joint grp
	# buffJnt_grp = core.Null( part + 'BuffJnt' + side + '_grp' )


	# buffJnt_grp.snap( priorJnt )


	# create FK joint
	upper_buffJnt = rigTools.jointAt( upper_bJnt )
	middle_buffJnt = rigTools.jointAt( middle_bJnt )
	lower_buffJnt = rigTools.jointAt( lower_bJnt )


	upper_buffJnt.name = rawName[0] + side + '_buffJnt' 
	middle_buffJnt.name = rawName[1] + side + '_buffJnt'
	lower_buffJnt.name = rawName[2] + side + '_buffJnt'


	# Create buffer joint grp

	ctrlType = 'Buff'
	buffJnt_grp = core.Null( nameSpace + region + ctrlType + 'Jnt' + side + '_grp' )

	# Parent
	middle_buffJnt.parent( upper_buffJnt )
	lower_buffJnt.parent( middle_buffJnt )
	upper_buffJnt.parent( buffJnt_grp )
	buffJnt_grp.parent( fkIkJnt_grp )

	# add color and adjust radius
	upper_buffJnt.setJointColor('softGray')
	middle_buffJnt.setJointColor('softGray')
	lower_buffJnt.setJointColor('softGray')

	upper_buffJnt.attr( 'radius' ).value = 1.25
	middle_buffJnt.attr( 'radius' ).value = 1.25
	lower_buffJnt.attr( 'radius' ).value = 1.25


	# Set rotation order
	upper_buffJnt.rotateOrder = rotOrder
	middle_buffJnt.rotateOrder = rotOrder
	lower_buffJnt.rotateOrder = rotOrder







	# Parent to main grp
	# buffJnt_grp.parent( jnt_grp )






	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Pair constraint each of bind joint to FK and IK
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	for each in rawName:

		logger.info( '______')
		logger.info( each)
		logger.info( '\n\n\n\n\n')
		logger.info( each + side +'_fkJnt')
		logger.info( each + side +'_ikJnt')
		logger.info( each + side +'_bJnt')

		psCon = mc.parentConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_buffJnt'  , name = each + 'Switch' + side + '_parCons' )
		
		revNode = mc.createNode('reverse' , name = each + 'Switch' + side + '_rev')

		# Connection fk/ik Stick controller switch to placement
		# IK = W1
		# Just tempolary for switch fk/ik
		
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , revNode + '.inputX'  )
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) ,  psCon[0] + '.' + each + side + '_ikJnt' + 'W1' )


		# FK = W0
		mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.' + each + side +'_fkJnt' + 'W0'  )




	# Parent to main grp
	fkIkJnt_grp.parent( jnt_grp )
	fkIkJnt_grp.attr('visibility').value = 0
	fkIkRig_grp.parent( parentTo )
	stickZro_grp.parent( parentTo )
	ikZro_grp.parent( ikhGrp )
	ikRootZro_grp.parent( ikCtrl_grp )


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Switch visibility each FK/IK
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	if keepFkIkBoth == True:	# Change the stick attribute
		stick_ctrl.attr('ikVis') >> ikZro_grp.attr('visibility')
		stick_ctrl.attr('ikVis') >> ikRootZro_grp.attr('visibility')
		stick_ctrl.attr('fkVis') >> fkCtrl_grp.attr('visibility')

	elif keepFkIkBoth == False:
		stickVis_rev = core.Reverse()
		stickVis_rev.name = part + 'StickVis' + side + '_rev'

		# Fk switch
		stick_ctrl.attr('FK_IK') >> stickVis_rev.attr('inputX')
		stickVis_rev.attr('outputX') >> fkCtrl_grp.attr('visibility')

		# Set value FK/IK switch
		stick_ctrl.attr('FK_IK') >> ikZro_grp.attr('visibility')
		stick_ctrl.attr('FK_IK') >> ikRootZro_grp.attr('visibility')








	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Lock and hide attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	lowerIk_ctrl.lockHideAttrLst( 'sx' , 'sy' , 'sz' , 'v' )
	ikRoot_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	ikRootGmbl_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	ikRoot_ctrl.setColor(colorSide)
	pov_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	ikGmbl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'v')


	'''
	part = nameSpace + region
	offset_null = core.Null( part + 'Offset' + side + '_null')
	offset_null.maSnap( lower_bJnt, position = True , rotation = True , scale = True )
	offset_parCons = core.parentConstraint( lower_bJnt , offset_null , mo = True)
	offset_parCons.name = part + 'Offset' + side + '_parCons'

	offset_null.parent( nullGrp )
	'''




	print (''' \n # = = = = = = Create Knee Elbow Lock Rig function''')

	print ('Create %s' %ikRootGmbl_ctrl.name)
	rawNameUPR , distanceUPRName , povUPR_Ctrl , lowerUPR_loc , upperUPR_loc = midLockModule.createDistance( nameSpace , part = 'up' , startP = ikRootGmbl_ctrl.name , endP = pov_ctrl.name )

	print ('Create %s' %pov_ctrl.name)
	rawNameLWR , distanceLWRName , povLWR_Ctrl , lowerLWR_loc , upperLWR_loc = midLockModule.createDistance( nameSpace , part = 'dn' ,startP = pov_ctrl.name , endP = ikGmbl_ctrl.name )
	blendName,invertNodeName  = midLockModule.createBlendColor(         nameSpace ,
										uprDistance = distanceUPRName		, 
										lwrDistance = distanceLWRName 		,
										side 		=  side   				,
										uprNam 		= rawNameUPR	           )
	# cancle arg 'type' but arfraid of error then keep
	attrName = midLockModule.doAddAttr( povUPR_Ctrl , region )
	midLockModule.connectIkJnt(	stretchNode = pmaNode , upperIKJnt = middle_IkJnt.name , lowerIKJnt = lower_IkJnt.name , blendName = blendName , namLock = attrName	, povName = povUPR_Ctrl, alongAxis = alongAxis )




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# 				Adding message to attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	print ('''# = = = = = = Create message''')
	stick_ctrl.addAttribute( dataType = 'string' , longName = 'region')
	stick_ctrl.setAttribute('region'  , region , type = 'string')
	stick_ctrl.lockHideAttrLst('region')
	stick_ctrl.addAttribute( dataType = 'string' , longName = 'location')
	# for location is for snape snap
	# Attention !!! use same variable as region
	stick_ctrl.setAttribute('location'  , region , type = 'string')
	# lock later with arm or leg rig
	# stick_ctrl.lockHideAttrLst('location')

	# add scale grp for make hand or foot scalable
	stick_ctrl.addAttribute( dataType = 'string' , longName = 'scale_Attr')
	stick_ctrl.setAttribute('scale_Attr'  , attScaleName , type = 'string')
	stick_ctrl.lockHideAttrLst('scale_Attr')


	message_Dict = mnd.MESSAGE_dict


	for keys in message_Dict:
		#print keys
		if keys != 'listString': # list string already create at early
			for each in message_Dict[keys]:
				stick_ctrl.addAttribute( attributeType = 'message' , longName = each)


	stick_ctrl.attr('message') >> stick_ctrl.attr('stick')
	upper_bJnt.attr('message') >> stick_ctrl.attr('upJnt')
	middle_bJnt.attr('message') >> stick_ctrl.attr('midJnt')
	lower_bJnt.attr('message') >> stick_ctrl.attr('lowJnt')
	upper_ctrl.attr('message') >> stick_ctrl.attr('upFkCtrl')
	middle_ctrl.attr('message') >> stick_ctrl.attr('midFkCtrl')
	lower_ctrl.attr('message') >> stick_ctrl.attr('lowFkCtrl')

	# move to each arm and leg Rig
	# offset_null.attr('message') >> stick_ctrl.attr('offset')
	pov_ctrl.attr('message') >> stick_ctrl.attr('pov')
	lowerIk_ctrl.attr('message') >> stick_ctrl.attr('ikCtrl')

	#... Add IkRootCtrl for make it can snap
	ikRoot_ctrl.attr('message') >> stick_ctrl.attr('ikRootCtrl')



	if region == 'leg':
		stick_ctrl.attr('FK_IK').value = 1



	print (''' \n
	# = = = = = = Create Shoulder, Thigh twist Rig function
	''')


	print (''' \n
	# = = = = = = Create ribbon Rig function
	''')


	# sys.exit('runmanual')






	


	
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create ribbon rig
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
  
	if ribbon == True:
		if ribbonRes == 'high':
			numJoints = 5
		else:
			numJoints = 3


		hingesUprBtm = ribbonRig.ribbonRigExt(
			nameSpace = nameSpace		,
			width = 10								,
			numJoints = numJoints							,
			side = side								,
			jointTop = upper_bJnt.name			,
			jointBtm = middle_bJnt.name			,
			part = ribbonName[0]							,
			charScale = charScale					,
			noTouch_grp = noTouchGrp				,
			showInfo = showInfo  					,
			ctrl_grp = fkIkRig_grp.name 		,
			alongAxis = alongAxis )



		hingesLwrTop = ribbonRig.ribbonRigExt(
				nameSpace = nameSpace		,
				width = 10								,
				numJoints = numJoints							,
				side = side								,
				jointTop = middle_bJnt.name			,
				jointBtm = lower_bJnt.name				,
				part = ribbonName[1]						,
				charScale = charScale					,
				noTouch_grp = noTouchGrp				,
				showInfo = showInfo  					,
				ctrl_grp = fkIkRig_grp.name 		,
				alongAxis = alongAxis)

		logger.info('This is something that ribbonRig return >>>> \n\n\n\n')
		logger.info(hingesUprBtm)
		logger.info('++++++++++++++++++++++++++++++++++++++++++++++++ \n\n\n\n')
		

		# sys.exit('Try to run manual 1059')
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Create elbow mover 
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #		
		ribbonRig.makeHigesMover( 						part = region, 		
														nameSpace = nameSpace		,
														side = side 				, 
														btmName = hingesUprBtm		, 
														topName = hingesLwrTop 		 , 
														charScale = charScale		,
														moverPosition = middle_buffJnt.name	,
														ctrl_grp = 'ctrl_grp',
														alongAxis = alongAxis		
																									)
		



	misc.makeHeader(	'End of %s %s Rig'%(part,side)	)
	#print '\n\n\n\n\n\n #### End of %s %s Rig ####' %(part,side)

	logger.info(hastag)

	# cancle if for use it constancely
	#if creTwistJnt:
	print ('Create Twist Rig function ...')

	# twist rig for arm and leg 
	# auto is still not good 
	# so put manual for user drive value insted		
	
	
	# sys.exit('BREAK')
	follow_grp = tr.twistRigAuto(	 
									nameSpace = nameSpace ,
									parent_jnt = upper_buffJnt.name , 
									child_jnt = middle_buffJnt.name , 
									fk_shoulderCtrl = upper_ctrl.name ,
									ik_shoulderCtrl = ikRoot_ctrl.name ,	
									side = side , 
									region = region ,
									priorJnt = priorJnt ,
									stick_ctrl = stick_ctrl.name ,
									charScale = charScale,
									showInfo = showInfo,
									alongAxis = alongAxis )


	mc.parent( follow_grp[0] , noTouchGrp )





	# Collect name for pov in case of request of ik leg place at foot





	# forget to parent upperArmTwist to upper_buffJnt
	# * * * * * * * *
	stick_ctrl.attr( attScaleName ) >> lower_buffJnt.attr( 'sx' )
	stick_ctrl.attr( attScaleName ) >> lower_buffJnt.attr( 'sy' )
	stick_ctrl.attr( attScaleName ) >> lower_buffJnt.attr( 'sz' )



	# # # # # # # # # # # # # # # #
	# Parent buffer joint >>> bind joint
	# # # # # # # # # # # # # # # # # # # #

	# misc.parentMatrix( follow_grp[1] , upper_bJnt.name , mo = True, t = True, r = True, s = True)
	# misc.parentMatrix( middle_buffJnt.name , middle_bJnt.name , mo = True, t = True, r = True, s = True)
	# misc.parentMatrix( lower_buffJnt.name , lower_bJnt.name , mo = True, t = True, r = True, s = True)



	# # # # # # # # # # # # # # # #
	# START Parent and Scale Cons buffer joint >>> bind joint
	# # # # # # # # # # # # # # # # # # # #
	region = region.capitalize()

	upperTwist_parCons = core.parentConstraint( follow_grp[1] , upper_bJnt.name, mo = True   )
	upperTwist_parCons.name = nameSpace + 'upper' + region +'Twist'+ side + '_parCons'
	
	#... for debug
	# mc.select(follow_grp[1] ,r=1)
	# mc.error('WHAT')

	#... Add mo for make bind joint not have rotate value
	upperTwist_scalCons = core.scaleConstraint( follow_grp[1] , upper_bJnt.name, mo = True   )
	upperTwist_scalCons.name = nameSpace + 'upper' + region +'Twist'+ side 
	upperTwist_scalCons.suffix

	midTwist_parCons = core.parentConstraint( middle_buffJnt.name , middle_bJnt.name, mo = True   )
	midTwist_parCons.name = nameSpace + 'mid' + region +'Twist'+ side + '_parCons'
	midTwist_scalCons = core.scaleConstraint( middle_buffJnt.name , middle_bJnt.name, mo = True   )
	midTwist_scalCons.name = nameSpace + 'mid' + region +'Twist'+ side 
	midTwist_scalCons.suffix

	lwrTwist_parCons = core.parentConstraint( lower_buffJnt.name , lower_bJnt.name, mo = True   )
	lwrTwist_parCons.name = nameSpace + 'lwr' + region +'Twist'+ side + '_parCons'
	lwrTwist_scalCons = core.scaleConstraint( lower_buffJnt.name , lower_bJnt.name, mo = True   )
	lwrTwist_scalCons.name = nameSpace + 'lwr' + region +'Twist'+ side 
	lwrTwist_scalCons.suffix



	
	# # # # # # # # # # # # # # # #
	# END Parent and Scale Cons buffer joint >>> bind joint
	# # # # # # # # # # # # # # # # # # # #

	print('#### End of %s %s Rig ####' %( __name__ , side ))


	#... Create metaNode ...#

	# fkIkTwistRig_meta = core.MetaGeneric( nameSpace + region + 'fkIkTwistRig' + side + '_meta')

	fkIkTwistRig_meta = core.MetaGeneric( nameSpace + region.lower() + 'fkIkTwistRig'.capitalize() + side + '_meta')

	
	mc.connectAttr(priorJnt + '.message', fkIkTwistRig_meta.name + '.Rig_Prior')
	fkIkTwistRig_meta.addAttribute( dataType = 'string' , longName = 'ikh_Name')
	fkIkTwistRig_meta.addAttribute( dataType = 'string' , longName = 'ikh_Zro_Name')
	fkIkTwistRig_meta.addAttribute( dataType = 'string' , longName = 'stick_ctrl_name')
	fkIkTwistRig_meta.addAttribute( dataType = 'string' , longName = 'ikh_ctrl_name')

	fkIkTwistRig_meta.setAttribute('Base_Name' 		,	__name__, type = 'string')
	fkIkTwistRig_meta.setAttribute('Side' 			,	side, type = 'string')
	fkIkTwistRig_meta.setAttribute('ikh_Name' 		,	ikhNam, type = 'string')
	fkIkTwistRig_meta.setAttribute('ikh_Zro_Name' 	,	ikhZro_grp, type = 'string')
	fkIkTwistRig_meta.setAttribute('stick_ctrl_name',	stick_ctrl.name, type = 'string')
	fkIkTwistRig_meta.setAttribute('ikh_ctrl_name'	,	lowerIk_ctrl, type = 'string')

	# ------------------ Meta Node Start ------------------------------------------------------------------- #
	#... Connect to root_meta 

	if mc.objExists(root_meta):
		mc.connectAttr('{0}.message'.format(root_meta), '{0}.Rig_Prior'.format(fkIkTwistRig_meta.name), f=True)
		mc.addAttr(root_meta, longName = f'{nameSpace}{region}_{side}', dataType='string', keyable=True)
		mc.connectAttr( '{0}.{1}'.format(fkIkTwistRig_meta.name, 'Base_Name'), '{0}.{1}{2}_{3}'.format(root_meta, nameSpace, region, side), f=True)

	
	# if mc.objExists(root_meta):
	# 	mc.connectAttr('{0}.message'.format(root_meta), '{0}.Rig_Prior'.format(fkIkTwistRig_meta.name), f=True)
	# 	mc.addAttr(root_meta, longName='{0}_{1}'.format(region,side), dataType='string', keyable=True)
	# 	mc.connectAttr( '{0}.{1}'.format(fkIkTwistRig_meta.name, 'Base_Name'), '{0}.{1}_{2}'.format(root_meta, region, side), f=True)

	#... change connect from root_meta to stick_ctrl instead
	if mc.objExists(stick_ctrl):
		# mc.connectAttr('{0}.message'.format(stick_ctrl), '{0}.Rig_Prior'.format(fkIkTwistRig_meta.name), f=True)
		metaName = mnd.MESSAGE_dict['meta'][0]
		fkIkTwistRig_meta.attr('message') >> stick_ctrl.attr(metaName)


	#... Lock All Attr
	fkIkTwistRig_meta.lockAllAttr()
	# ------------------ Meta Node End ------------------------------------------------------------------- #


	#------------------------------ Create SoftIk -----------------------------#
	'''
	if softIk == True:

		softIkfunc.softIK(	region = region, side = side, ctrlName = lowerIk_ctrl.name,
					upAxis = 2, primaryAxis = 2, ikhName = ikhNam, 
					inputMax = 40, outputMax = 4  )
	'''

	#... Add ikhZro_grp for SoftIK
	ikhAll_name = ikhNam, povZro_grp, Loc_grp.name, World_grp.name, ikhZro_grp
	softIk_name = [lowerIk_ctrl.name]



	return stick_ctrl.name , lower_bJnt.name , middle_bJnt.name , upper_bJnt.name , ikhAll_name ,psStreEndName, softIk_name, fkIkTwistRig_meta