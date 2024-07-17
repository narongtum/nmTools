#... using this module
# D:\sysTools\nmTools_github\riggerTools\python\function\rigging\autoRig\bodyRig\headRigExt

# Neck rig module
import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)
import sys
import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)



def _eyeCtrl( nameSpace = ''  , eyeJntNam = '' , side = ''  , headJnt = '' , charScale = '' , parentTo = '', eyeCenCtrl = '', eyeTarget = '' ):
	# = = = = = = = = = = = = = #
	# Right Eye
	# = = = = = = = = = = = = = #

	# Ask first if eyeLft.exists :

	# Left Eye skin joint
	# nameSpace = charName + elem
	part = nameSpace + 'eye' + side
	core.makeHeader('Start of %s Rig' %part)
	eyeSide_bJnt = rigTools.jointAt( eyeJntNam )


	eyeTarget = core.Dag( eyeTarget )
	# Naming is decundance
	# eyeSide_bJnt.name = nameSpace + part + '_bJnt'
	eyeSide_bJnt.name = part + '_bJnt'
	eyeSide_bJnt.parent( headJnt )


	# Set Sacle seqment compensate
	#eyeSide_bJnt.attr('segmentScaleCompensate').value = 0
	eyeSide_ctrl = core.Dag(   part + '_ctrl' )
	eyeSide_ctrl.nmCreateController('sphere_ctrlShape')
	eyeSide_ctrl.editCtrlShape( axis = charScale * 1.01 )
	# Create aim group
	eyeAimSide_grp = rigTools.zeroGroup( eyeSide_ctrl )
	eyeAimSide_grp.name =  part + 'Aim_grp'
	eyeSideZro_grp = rigTools.zeroGroup( eyeAimSide_grp )
	eyeSideZro_grp.name =  part + 'Zro_grp'
	eyeSideGmbl_ctrl = core.createGimbal( eyeSide_ctrl )
	eyeSide_ctrl.color = 'softBlue'
	eyeSide_ctrl.rotateOrder = 'zxy'
	eyeSideGmbl_ctrl.rotateOrder = 'zxy'
	eyeSideZro_grp.matchPosition( eyeSide_bJnt )
	eyeSideZro_grp.matchRotation( eyeSide_bJnt )

	# Add freeze transform to get rid orientation
	eyeSide_bJnt.freeze()


	# = = = = = = = = = = = = = #
	#... Additional joint for facial Start
	# = = = = = = = = = = = = = #
	#... extended for make facial joint
	eye_loc = core.Locator(name = 'eye' + '{0}_bLoc'.format(side), lock = True, scale = charScale)
	eye_loc.snap( eyeSide_bJnt )




	# = = = = = = = = = = = = = #
	#  Eye target
	# = = = = = = = = = = = = = #


	#  Eye skin joint
	part = nameSpace + 'eyeTarget' + side
	eyeTargetSide_ctrl = core.Dag( part  + '_ctrl' )
	eyeTargetSide_ctrl.nmCreateController('legRGT_pov_ctrlShape')
	eyeTargetSide_ctrl.editCtrlShape( axis = charScale * 0.8 )
	eyeTargetSide_ctrl.color = 'softBlue'
	eyeTargetSide_ctrl.rotateOrder = 'zxy'
	eyeTargetSideZro_grp = rigTools.zeroGroup( eyeTargetSide_ctrl )
	eyeTargetSideZro_grp.name =   part  + 'Zro_grp'

	# Prosition controller
	# mc.delete( core.pointConstraint( eyeSide_bJnt , eyeTargetSideZro_grp ))
	# For make sure this position is translate just z for aim reason
	# mc.delete( core.pointConstraint( eyeCenCtrl , eyeTargetSideZro_grp  , skip = ( 'x' , 'y' ) ) )
	eyeTargetSideZro_grp.maSnap( eyeTarget )

	# Move zro grp under eyeCenter grp
	eyeTargetSideZro_grp.parent( eyeCenCtrl )
	# Aim Constraint
	# Z Aim , Y up , world up is Y , upObject is head01
	eyeCtrlAimGrpSide_aimCons = core.aimConstraint( eyeTargetSide_ctrl , eyeAimSide_grp , aimVector = (0,0,1) , upVector = (0,1,0) , worldUpType = "objectrotation" , worldUpVector = (0,1,0) , worldUpObject = headJnt )
	eyeCtrlAimGrpSide_aimCons.name =  part  + '_aimCons'


	# Shif to here to avoid joint having rotation value
	# Making joint parent to controller
	eyeSide_parCons = core.parentConstraint( eyeSideGmbl_ctrl , eyeSide_bJnt , mo = True)
	eyeSide_parCons.name =  part + 'Jnt_parCons'

	# = = = = = = = = = = = = = #
	#... Additional joint for facial End
	# = = = = = = = = = = = = = #
	#... comment this line for assign root grp to bLoc instead
	# eyeSideZro_grp.parent( parentTo )
	eye_loc.parent( eyeSideZro_grp )
	eyeAimSide_grp.parent( eye_loc )
	eyeSideZro_grp.parent( parentTo )




	# Lock and hide attr
	for attr in ('rx','ry','rz','sx','sy','sz','v') :
		eyeTargetSide_ctrl.attr( attr ).lockHide()

	return eyeSideZro_grp




# add 'headTop_tmpJnt',	'headBottom_tmpJnt' for suit facial JH rig

def headRig(	nameSpace = '' ,
				parentTo = 'ctrl_grp'  ,
				tmpJnt = ( 		'head01_tmpJnt', 'eyeLFT_tmpJnt', 'eyeRGT_tmpJnt' 	,    # head
				'jaw01Lwr_tmpJnt', 'jaw02Lwr_tmpJnt', 'jaw03Lwr_tmpJnt' 				,    # jaw
				'jaw01Upr_tmpJnt', 'jaw02Upr_tmpJnt'									,	
				'eye_tmpJnt', 'eyeTargetLFT_tmpJnt', 'eyeTargetRGT_tmpJnt'				,
				'headTop_tmpJnt', 'headBottom_tmpJnt'	    )							,
				faceCtrl = False	,
				priorJnt = ''		,
				charScale = ''		,
				ctrlShape = 'cubeExpand_ctrlShape',
				linkRotOrder = False
			):


	core.makeHeader('Start of Head Rig')
	# Get name object
	head1 = core.Dag( tmpJnt[ 0 ] )

	if faceCtrl == True:
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Eye name setup 
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

		try:
			eyeLFT = core.Dag(tmpJnt[ 1 ])
			eyeRGT = core.Dag(tmpJnt[ 2 ])


		except:
			mc.error('\nEye joint not found.')
			pass

		# = = = = = = = = Jaw name setup = = = = = = = = = = = = = = = = = = = #
		try:
			jaw1Lwr = core.Dag( tmpJnt[ 3 ] )
			jaw2Lwr = core.Dag( tmpJnt[ 4 ] )
			jaw1Upr = core.Dag( tmpJnt[ 6 ] )
			jaw2Upr = core.Dag( tmpJnt[ 7 ] )

		except:
			mc.error('\nJaw joint not found.')
			pass
		# = = = = = = = = eye name setup = = = = = = = = = = = = = = = = = = = #

		try:
			eyeCen = core.Dag( tmpJnt[8] )
			eyeTargetLFT = core.Dag( tmpJnt[9] )
			eyeTargetRGT = core.Dag( tmpJnt[10] )
			eyeLFT = core.Dag( tmpJnt[1] )
			eyeRGT = core.Dag( tmpJnt[2] )
		except:
			mc.error('\nEye joint not found.')
			pass


		try:
			headTop = core.Dag( tmpJnt[11] )
			headButtom = core.Dag( tmpJnt[12] )
		except:
			mc.error('\n\theadTop, headButtom joint not found.')

	if not headTop:
		mc.error('\n\tYou maybe want to turn on facial Rig First.')



	# Create bind joint at
	head01_bJnt = rigTools.jointAt( head1 )
	# Set Name 
	head01_bJnt.name = nameSpace + 'head' + '01' + '_bJnt'

	# parent
	head01_bJnt.parent( priorJnt )

	# set joint lable
	head01_bJnt.setLable('CEN','head')

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# New element head top Start
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	headTop_jnt = rigTools.jointAt( headTop )
	headButtom_jnt = rigTools.jointAt( headButtom )

	headTop_jnt.name = nameSpace + 'headTop' + '_bJnt'
	headButtom_jnt.name = nameSpace + 'headBottom' + '_bJnt'

	headTop_jnt.parent( head01_bJnt )
	headButtom_jnt.parent( head01_bJnt )


	# Create Head Rig Group
	headRig_grp = core.Null()
	headRig_grp.name = nameSpace + 'headRig_grp'
	# Parenting and positioning
	headRig_grp.matchPosition( head1 )
	headRig_grp.matchRotation( head1 )
	headRotOrder = 'xzy'

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# New element head top End
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Head setup 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	part = nameSpace + 'head01'
	head_ctrl = core.Dag( part + '_ctrl' )
	head_ctrl.nmCreateController( ctrlShape ) # circleSphere_ctrlShape , cubeExpand_ctrlShape
	headZro_grp = rigTools.zeroGroup( head_ctrl )
	headZro_grp.name =   part + 'Zro_grp'
	head_ctrl.editCtrlShape( axis = charScale * 7.0 )
	headGmbl_ctrl = core.createGimbal( head_ctrl )
	head_ctrl.color = 'yellow'
	head_ctrl.rotateOrder = headRotOrder
	headGmbl_ctrl.rotateOrder = headRotOrder
	headZro_grp.snap( head1 )
	head_ctrl.moveShape(  move = ( 0 , charScale * 4.2 , 0 )  )
	headGmbl_ctrl.moveShape(  move = ( 0 , charScale * 4.2 , 0 )  )

	if linkRotOrder:
		# link rotate order
		head_ctrl.addRotEnum()
		headGmbl_ctrl.addRotEnum()

	# = = = = = = = = = = = = = #
	# Head Local / World setup
	# = = = = = = = = = = = = = #
	partName = nameSpace + 'head'
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( head_ctrl , headRig_grp , parentTo , headZro_grp.name , partName )
	Loc_grp.name = part + 'Local_grp'
	World_grp.name = part + 'World_grp'
	WorldGrp_orientCons.name = part + 'WorldGrp_orientCons'
	ZroGrp_orientCons.name = part + 'ZroGrp_orientCons'
	reverseNode_rev.name = part + 'ZroGrpOrientCons_rev'

	# Constraint joint parent to controller
	head01Lwr_parCons = core.parentConstraint( headGmbl_ctrl , head01_bJnt )
	head01Lwr_parCons.name = part + 'Jnt_parCons'
	# Scale Constraint 
	head01Lwr_sacleCons = core.scaleConstraint( headGmbl_ctrl , head01_bJnt )
	head01Lwr_sacleCons.name = part + 'Jnt_scaleCons'


	# = = = = = = = = = = = = = #
	#	Additional joint for facial Start
	# = = = = = = = = = = = = = #
	head_loc = core.Locator(name = 'head_bLoc', lock = True, scale = charScale)
	head_loc.maSnap( head01_bJnt )


	# = = = = = = = = = = = = = #
	# Group Head to HeadRig
	# = = = = = = = = = = = = = #
	headZro_grp.parent( headRig_grp )
	headRig_grp.parent( parentTo )





	if faceCtrl == True:
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Check Jaw 
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

		# add check if Jaw exists later
		jaw1Lwr_bJnt = rigTools.jointAt( jaw1Lwr )
		jaw2Lwr_bJnt = rigTools.jointAt( jaw2Lwr )
		jaw1Upr_bJnt = rigTools.jointAt( jaw1Upr )
		jaw1Lwr_bJnt.name = nameSpace + 'jaw' + '01' +'Lwr' + '_bJnt'
		jaw2Lwr_bJnt.name = nameSpace + 'jaw' + '02' +'Lwr' + '_bJnt'
		jaw1Upr_bJnt.name = nameSpace + 'jaw' + '01' +'Upr' + '_bJnt'

		#...Parent each (change hirachy)
		# jaw1Lwr_bJnt.parent( head01_bJnt )
		jaw2Lwr_bJnt.parent( jaw1Lwr_bJnt )
		jaw1Upr_bJnt.parent( headButtom_jnt )
		jaw1Lwr_bJnt.parent( headButtom_jnt )


		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Create special locator
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

		#... Create spcial locator
		jaw1Upr_loc = core.Locator(name = 'jaw1Upr_bLoc', lock = True, scale = charScale)
		jaw1Upr_loc.snap( jaw1Upr_bJnt )
		jaw1Lwr_loc = core.Locator(name = 'jaw1Lwr_bLoc', lock = True, scale = charScale)
		jaw1Lwr_loc.snap( jaw1Lwr_bJnt )


		#... Create spcial locator
		# headTop_ctrl = core.Locator(name = 'headTop_ctrl', lock = True, scale = charScale)
		headTop_ctrl = core.Dag( part + 'Top_ctrl' )
		headTop_ctrl.nmCreateController( 'circle_ctrlShape' )
		headTop_ctrl.rotateOrder = 'xzy'
		headTop_ctrl.editCtrlShape( axis = charScale * 1.25 )
		headTop_ctrl.color = 'white'
		headTop_ctrl.snap( headTop_jnt )




		# headBottom_ctrl = core.Locator(name = 'headBottom_ctrl', lock = True, scale = charScale)
		headBottom_ctrl = core.Dag( part + 'Bottom_ctrl' )
		headBottom_ctrl.nmCreateController( 'circle_ctrlShape' )
		headBottom_ctrl.rotateOrder = 'xzy'
		headBottom_ctrl.editCtrlShape( axis = charScale * 1.25 )
		headBottom_ctrl.color = 'white'

		headBottom_ctrl.snap( headButtom_jnt )


		

		
		headTopZro_grp = rigTools.zeroGroup( headTop_ctrl )
		headTopZro_grp.name = nameSpace + 'head'+'TopZro' + '_grp'
		headBottomZro_grp = rigTools.zeroGroup( headBottom_ctrl )
		headBottomZro_grp.name = nameSpace + 'head'+'BottomZro' + '_grp'

		headTopZro_grp.parent(headGmbl_ctrl)
		headBottomZro_grp.parent(headGmbl_ctrl)

		


		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Upper Jaw setup
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

		part = nameSpace + 'jaw01Upr'
		jaw01Upr = core.Dag( part + '_ctrl' )
		jaw01Upr.nmCreateController('squareExpand_ctrlShape')
		#jaw01Upr.rotateShape(  rotate = ( -70 , 0 , 0  )  )
		jaw01Upr.editCtrlShape( axis = charScale * 3.5)
		jaw01Upr.moveShape(  move = (  0  ,0 , charScale * 1.12  )  )
		jaw01UprZro_grp = rigTools.zeroGroup( jaw01Upr )
		jaw01UprZro_grp.name = part + 'Zro_grp'
		jaw01GmblUpr_ctrl = core.createGimbal( jaw01Upr )
		jaw01Upr.color = 'red'
		jaw01Upr.rotateOrder = headRotOrder
		jaw01GmblUpr_ctrl.rotateOrder = headRotOrder
		jaw01UprZro_grp.snap( jaw1Upr_bJnt )
		jaw1Lwr_bJnt.attr('segmentScaleCompensate').value = 0

		#... Paren
		# jaw01UprZro_grp.parent( headGmbl_ctrl )
		jaw01UprZro_grp.parent( headBottom_ctrl )
		jaw1Upr_loc.parent( jaw01UprZro_grp )
		jaw01Upr.parent( jaw1Upr_loc )

		#... Constraint joint parent to controller
		jaw01Lwr_parCons = core.parentConstraint( jaw01GmblUpr_ctrl , jaw1Upr_bJnt )
		jaw01Lwr_parCons.name = part + 'Jnt_parCons'





		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Lower Jaw setup
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		part = nameSpace + 'jaw01Lwr'
		jaw01Lwr = core.Dag( part + '_ctrl' )
		jaw01Lwr.nmCreateController('squareExpand_ctrlShape')
		#jaw01Lwr.rotateShape(  rotate = ( -70 , 0 , 0  )  )
		jaw01Lwr.editCtrlShape( axis = charScale * 2.8)
		jaw01Lwr.scaleShape(  scale = (  1, 1 , 1 )  )
		jaw01Lwr.moveShape(  move = ( 0 , charScale * -1.8 ,charScale * 2.8 )  )
		jaw01LwrZro_grp = rigTools.zeroGroup( jaw01Lwr )
		jaw01LwrZro_grp.name = part + 'Zro_grp'
		jaw01GmblLwr_ctrl = core.createGimbal( jaw01Lwr )
		jaw01Lwr.color = 'red'
		jaw01Lwr.rotateOrder = headRotOrder
		jaw01GmblLwr_ctrl.rotateOrder = headRotOrder
		jaw01LwrZro_grp.snap( jaw1Lwr_bJnt )
		jaw1Lwr_bJnt.attr('segmentScaleCompensate').value = 0
		# Constraint joint parent of controller
		jaw01Lwr_parCons = core.parentConstraint( jaw01GmblLwr_ctrl , jaw1Lwr_bJnt )
		jaw01Lwr_parCons.name = part + 'Jnt_parCons'

		#... Replace parent
		jaw1Lwr_loc.parent( jaw01LwrZro_grp )
		jaw01Lwr.parent(jaw1Lwr_loc)
		# jaw01LwrZro_grp.parent( headGmbl_ctrl )
		jaw01LwrZro_grp.parent( headBottom_ctrl )


		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# (UPDATE)Lower Gum setup
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

		part = nameSpace + 'jaw02Lwr'
		jaw02Lwr = core.Dag( part + '_ctrl' )
		jaw02Lwr.nmCreateController('squareExpand_ctrlShape')
		jaw02Lwr.editCtrlShape( axis = charScale * 2.8)
		jaw02Lwr.scaleShape(  scale = (  1, 1 , 1 )  )
		jaw02Lwr.moveShape(  move = (  0  ,0 , charScale * 1.12  )  )
		jaw02LwrZro_grp = rigTools.zeroGroup( jaw02Lwr )
		jaw02LwrZro_grp.name = part + 'Zro_grp'
		jaw02GmblLwr_ctrl = core.createGimbal( jaw02Lwr )
		jaw02Lwr.color = 'red'
		jaw02Lwr.rotateOrder = headRotOrder
		jaw02GmblLwr_ctrl.rotateOrder = headRotOrder
		jaw02LwrZro_grp.snap( jaw2Lwr_bJnt )
		jaw2Lwr_bJnt.attr('segmentScaleCompensate').value = 0





		#... Constraint joint parent of controller
		jaw02Lwr_parCons = core.parentConstraint( jaw02GmblLwr_ctrl , jaw2Lwr_bJnt )
		jaw02Lwr_parCons.name = part + 'Jnt_parCons'
		jaw02LwrZro_grp.parent( jaw01GmblLwr_ctrl )


		





		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Eye center rig
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

		# add check if Jaw exists later
		part = nameSpace + 'eyeCenter'
		eyeCenter_ctrl = core.Dag( part + '_ctrl' )
		eyeCenter_ctrl.nmCreateController('capsule_ctrlShape')
		eyeCenterOffset_grp = rigTools.zeroGroup( eyeCenter_ctrl )
		eyeCenterOffset_grp.name = part + 'Offset_grp'
		eyeCenterZro_grp = rigTools.zeroGroup( eyeCenterOffset_grp )
		eyeCenterZro_grp.name = part + 'Zro_grp'
		eyeCenterZro_grp.snap( eyeCen )
		eyeCenterZro_grp.parent( headGmbl_ctrl )
		eyeCenter_ctrl.editCtrlShape( axis = charScale * 0.8 )
		eyeCenter_ctrl.color = 'yellow'
		eyeCenter_ctrl.rotateOrder = headRotOrder
			


		# = = = = = = = = = = = = = #
		#  Local / World setup      #
		# = = = = = = = = = = = = = #
		Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.parentLocalWorldCtrl( eyeCenter_ctrl , headGmbl_ctrl , parentTo , eyeCenterZro_grp.name )
		# rename group after exec the function
		Loc_grp.name = part + 'Local_grp'
		World_grp.name = part + 'World_grp'
		WorldGrp_orientCons.name = part + 'WorldGrp_orientCons'
		ZroGrp_orientCons.name = part + 'ZroGrp_orientCons'
		reverseNode_rev.name = part + 'ZroGrpOrientCons_rev'
		# return eyeLFT.name
		# return eyeRGT.name



		_eyeCtrl( nameSpace =  nameSpace, eyeJntNam = eyeLFT.name , side = 'LFT' , headJnt = headTop_jnt.name , charScale = charScale , parentTo = headTop_ctrl.name , eyeCenCtrl = eyeCenter_ctrl.name , eyeTarget = eyeTargetLFT.name  )
		_eyeCtrl( nameSpace =  nameSpace, eyeJntNam = eyeRGT.name , side = 'RGT' , headJnt = headTop_jnt.name , charScale = charScale , parentTo = headTop_ctrl.name , eyeCenCtrl = eyeCenter_ctrl.name , eyeTarget = eyeTargetRGT.name  )





	# shift to here because of having an unexpect head grp prosition
	# Constraint rig_grp to prior controller grp
	headRigGrp_parCons = core.parentConstraint( priorJnt , headRig_grp , mo = True)
	headRigGrp_parCons.name = nameSpace + 'headRigGrp_parCons'




	# = = = = = = = = = = = = = = = = = = #
	#  Spcial locator for facial rig      #
	# = = = = = = = = = = = = = = = = = = #

	headTopCtrl_parCons = core.parentConstraint( headTop_ctrl , headTop_jnt )
	headTopCtrl_parCons.name = part + '_Top' + 'Jnt_parCons'

	headBottomCtrl_parCons = core.parentConstraint( headBottom_ctrl , headButtom_jnt )
	headBottomCtrl_parCons.name = part + '_Bottom' + 'Jnt_parCons'	



	headTop_parCons = core.parentConstraint( head01_bJnt , headTopZro_grp, mo = True )
	headTop_parCons.name = part + '_headTop' + 'Jnt_parCons'

	# print('\nStop righe there...')
	# sys.exit(0)

	headBottom_parCons = core.parentConstraint( head01_bJnt , headBottomZro_grp, mo = True  )
	headBottom_parCons.name = part + '_headBottom' + 'Jnt_parCons'


	head_loc.maSnap( head01_bJnt )
	head_loc.parent( headRig_grp )
	head_ctrl.parent( head_loc )




	print('\n\n\n\n\n')
	logger.info('#### End of %s ####' %(__name__))

	
	return head01_bJnt.name






'''
headRig(	parentTo = 'ctrl_grp'  , 
				tmpJnt = ( 		'head01_tmpJnt' , 'eyeLFT_tmpJnt' , 'eyeRGT_tmpJnt' ,		# head
				'jaw01Lwr_tmpJnt' , 'jaw02Lwr_tmpJnt' , 'jaw03Lwr_tmpJnt' 			,		# jaw
				'jaw01Upr_tmpJnt' , 'jaw02Upr_tmpJnt','eye_tmpJnt' , 
				'eyeTargetLFT_tmpJnt' , 'eyeTargetRGT_tmpJnt'		 		# eye			
																			),
				faceCtrl = True	,
				priorJnt = neckJnt				
			)
'''