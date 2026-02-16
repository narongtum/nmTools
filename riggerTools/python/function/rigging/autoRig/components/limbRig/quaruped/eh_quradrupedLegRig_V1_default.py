import maya.cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload

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

from function.rigging.tools import proc as pc
reload(pc)

import maya.mel as mel

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


from function.pipeline import logger 
reload(logger)


class QuardrupedLogger(logger.MayaLogger):
	LOGGER_NAME = "quardruped"

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)
color_part_dict = mnd.COLOR_part_dict

'''
nameSpace = '' 		
parentTo = 'ctrl_grp' 			
side = 'LFT'					
tmpJnt = (	'upLegBackLFT_tmpJnt'  , 'midLegBackLFT_tmpJnt' ,  'ankleBackLFT_tmpJnt' , 
			'legPovBackLFT_tmpJnt' ,'ballRollBackLFT_tmpJnt' ,'toeRollBackLFT_tmpJnt' ,
			'heelRollBackLFT_tmpJnt' , 'footOutBackLFT_tmpJnt' , 'footInBackLFT_tmpJnt' , 'lowLegBackLFT_tmpJnt')
priorJnt = 'hip_bJnt'				
ikhGrp = 'ikh_grp' 					
noTouchGrp = 'noTouch_grp' 			
nullGrp = 'snapNull_grp'			
showInfo = False  					
ribbon = True						
ribbonRes = 'low'					
ribbonName = ('upLeg', 'lwrLeg')	
charScale = 1
'''

def quradrupedLegRig(		nameSpace = '' 	,	
							parentTo = 'ctrl_grp' 	,		
							side = 'LFT'		,			
							tmpJnt = (	'upLegBackLFT_tmpJnt'  , 'midLegBackLFT_tmpJnt' ,  'ankleBackLFT_tmpJnt' , 
										'legPovBackLFT_tmpJnt' ,'ballRollBackLFT_tmpJnt' ,'toeRollBackLFT_tmpJnt' ,
										'heelRollBackLFT_tmpJnt' , 'footOutBackLFT_tmpJnt' , 'footInBackLFT_tmpJnt' , 'lowLegBackLFT_tmpJnt'), # [9] because of it can't change the main code joint order so i put the fifth leg joint here
							priorJnt = 'hip_bJnt',				
							ikhGrp = 'ikh_grp' 		,			
							noTouchGrp = 'noTouch_grp' 	,		
							nullGrp = 'snapNull_grp',			
							showInfo = False  ,					
							ribbon = True	,					
							ribbonRes = 'low'	,				
							ribbonName = ('upLeg', 'lwrLeg'),	
							charScale = 1,
							region = 'backLeg',
							alongAxis = 'y',
							povShape = 'sphereAxis' ):

	core.makeHeader(	'Start of %s%s Rig' %('quradrupedLegRig',side)	)


	print ('''
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# 				Quradruped Leg Rig Function \n 
	# please remember it calling stretcy rig and knee lock function so it need to be update if these function is modify
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	''')


	if side == 'LFT':
		colorSide = color_part_dict['left'] #... blue
	else:
		colorSide = color_part_dict['right'] #... red





	upperLeg = core.Dag( tmpJnt[ 0 ] )
	midLeg = core.Dag( tmpJnt[ 1 ] )
	lowerLeg = core.Dag( tmpJnt[ 9 ] )
	ankle = core.Dag( tmpJnt[ 2 ] )
	povLeg = core.Dag( tmpJnt[ 3 ] )
	ball = core.Dag(tmpJnt[ 4 ])
	toe = core.Dag( tmpJnt[5] )
	heel = core.Dag( tmpJnt[6] )
	footIn = core.Dag( tmpJnt[7] )
	footOut = core.Dag( tmpJnt[8] )


	# Create bind joint
	upperLeg_bJnt = rigTools.jointAt( upperLeg )
	midLeg_bJnt = rigTools.jointAt( midLeg )
	lowerLeg_bJnt = rigTools.jointAt( lowerLeg )
	ankle_bJnt = rigTools.jointAt( ankle )
	ball_bJnt = rigTools.jointAt( ball )
	toe_bJnt = rigTools.jointAt( toe )


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Check type is for animal or human
	# Result : return string
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	if 'Front' in tmpJnt[0]:
		print ('This is animal.')
		legType = 'frontLeg'
		position = 'Front'

	elif 'Back' in tmpJnt[0]:
		legType = 'backLeg'
		position = 'Back'
		
	else :
		print ('This is human Leg like.')
		legType = 'leg'



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Store raw name
	# Result : raw name without side
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	rawName = []
	for each in tmpJnt:
		tmp = each.split('_')[0][:-3]
		rawName.append(tmp)

	print ('\nThis is raw name : '  )
	print (rawName)



	upperLeg_bJnt.name =   rawName[0] + side + '_bJnt'
	midLeg_bJnt.name =   rawName[1] + side + '_bJnt'
	lowerLeg_bJnt.name =   rawName[9] + side + '_bJnt'
	ankle_bJnt.name =   rawName[2] + side + '_bJnt'
	ball_bJnt.name =   rawName[4] + side + '_bJnt'
	toe_bJnt.name =   rawName[5] + side + '_bJnt'


	# Adjust rotate order
	upperLeg_bJnt.rotateOrder = 'yzx'
	midLeg_bJnt.rotateOrder = 'yzx'
	lowerLeg_bJnt.rotateOrder = 'yzx'
	ankle_bJnt.rotateOrder = 'yzx'

	# Parent
	midLeg_bJnt.parent( upperLeg_bJnt )
	lowerLeg_bJnt.parent( midLeg_bJnt )
	ankle_bJnt.parent( lowerLeg_bJnt )
	toe_bJnt.parent(ball_bJnt)
	ball_bJnt.parent(ankle_bJnt)
	ankle_bJnt.attr('segmentScaleCompensate').value = 0
	# Parent it to prior joint
	upperLeg_bJnt.parent( priorJnt )



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create main rig grp
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	part = nameSpace + legType
	legRig_grp = core.Null( part + 'Rig' + side + '_grp' )
	legRigGrp_parCons = core.parentConstraint( priorJnt , legRig_grp )
	legRigGrp_parCons.name = part + 'Rig' + side + '_parCons'
	# Create joint grp
	jnt_grp = core.Null( part + 'Jnt' + side + '_grp' )



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Stick Controller 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	stick_ctrl = core.Dag( part + 'Stick' + side + '_ctrl' )
	stick_ctrl.nmCreateController('stick_ctrlShape')
	stick_ctrl.editCtrlShape( axis = charScale * 3.6 )
	stick_ctrl.color = 'yellow'
	stick_ctrl.hideArnoldNode()

	if side == 'LFT':
		stick_ctrl.attr('rotateX').value -= 90

	else:
		stick_ctrl.attr('rotateX').value -= 90

	stickZro_grp = rigTools.zeroGroup( stick_ctrl )
	stickZro_grp.name = part + 'Stick'+ side + 'Zro_grp'
	stickZro_grp.matchPosition( ankle_bJnt )
	print('Set rotation to %s controller...' %stick_ctrl.name)
	ctrlGrp_parCons = core.parentConstraint( ankle_bJnt , stickZro_grp , mo = True)
	ctrlGrp_parCons.name = part + side + 'Stick'+ '_parCons'

	stick_ctrl.addAttribute( longName = 'legScale' , defaultValue = 1 , keyable = True )
	# Loch and hide
	stick_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Create FK
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create fk rig grp

	part = nameSpace + legType
	fkCtrl_grp = core.Null( part + 'FkCtrl' + side + '_grp' )
	fkCtrl_grp.snap( priorJnt )
	fkCtrl_grp.parent( legRig_grp )

	# Create Fk joint grp
	fkJnt_grp = core.Null( part + 'FkJnt' + side + '_grp' )
	fkJnt_grp.snap( priorJnt )
	fkJnt_grp.parent( jnt_grp )

	# create FK joint
	upperLeg_fkJnt = rigTools.jointAt( upperLeg )
	lowerLeg_fkJnt = rigTools.jointAt( lowerLeg )
	ankle_fkJnt	 = rigTools.jointAt( ankle )
	ball_fkJnt = rigTools.jointAt( ball )
	midLeg_fkJnt = rigTools.jointAt( midLeg )


	# Use variable instead
	upperLeg_fkJnt.name 	= rawName[0] + side + '_fkJnt' 
	midLeg_fkJnt.name 		= rawName[1] + side + '_fkJnt'
	lowerLeg_fkJnt.name 	= rawName[9] + side + '_fkJnt'
	ankle_fkJnt.name 		= rawName[2] + side + '_fkJnt'
	ball_fkJnt.name 		= rawName[4] + side + '_fkJnt'


	# Parent
	midLeg_fkJnt.parent( upperLeg_fkJnt )
	lowerLeg_fkJnt.parent( midLeg_fkJnt )
	ankle_fkJnt.parent( lowerLeg_fkJnt )
	ball_fkJnt.parent( ankle_fkJnt )
	upperLeg_fkJnt.parent( fkJnt_grp )

	# Set rotation order
	upperLeg_fkJnt.rotateOrder = 'xyz'
	lowerLeg_fkJnt.rotateOrder = 'yzx'
	ankle_fkJnt.rotateOrder = 'xzy'
	ball_fkJnt.rotateOrder = 'yzx'

	# Create Fk upperLeg
	part = nameSpace +'upper' + legType.capitalize()
	type = 'Fk'
	ctrlShape = 'lowerLeg%s_FK_ctrlShape' %side

	upperFkLeg_ctrl = core.Dag( part + type + side + '_ctrl' )
	upperFkLeg_ctrl.nmCreateController( ctrlShape )
	upperLegFkZro_grp = rigTools.zeroGroup( upperFkLeg_ctrl )
	upperLegFkZro_grp.name = part + type + side + 'Zro_grp'
	upperFkLeg_ctrl.editCtrlShape( axis = charScale * 0.9 )
	upperLegFkGmbl_ctrl = core.createGimbal( upperFkLeg_ctrl )
	upperFkLeg_ctrl.color = colorSide
	upperFkLeg_ctrl.rotateOrder = 'xyz'
	upperLegFkGmbl_ctrl.rotateOrder = 'xyz'
	# Parenting and positioning
	upperLegFkZro_grp.matchPosition( upperLeg_fkJnt )
	upperLegFkZro_grp.matchRotation( upperLeg_fkJnt )
	# Constraint
	upperLegFkJnt_parCons = core.parentConstraint( upperLegFkGmbl_ctrl , upperLeg_fkJnt )
	upperLegFkJnt_parCons.name = part + type + side + '_parCons'



	# Create Middle Leg
	part = nameSpace +'mid' + legType.capitalize()
	middleLegFk_ctrl = core.Dag( part + type + side + '_ctrl' )
	middleLegFk_ctrl.nmCreateController( ctrlShape )
	middleLegFkZro_grp = rigTools.zeroGroup( middleLegFk_ctrl )
	middleLegFkZro_grp.name = part + type + side + 'Zro_grp'
	middleLegFk_ctrl.editCtrlShape( axis = charScale * 0.8 )
	middleLegFkGmbl_ctrl = core.createGimbal( middleLegFk_ctrl )
	middleLegFk_ctrl.color = colorSide
	middleLegFk_ctrl.rotateOrder = 'yzx'
	middleLegFkGmbl_ctrl.rotateOrder = 'yzx'
	# Parenting and positioning
	middleLegFkZro_grp.matchPosition( midLeg_fkJnt )
	middleLegFkZro_grp.matchRotation( midLeg_fkJnt )
	# Constraint
	middleLegFkJnt_parCons = core.parentConstraint( middleLegFkGmbl_ctrl , midLeg_fkJnt )
	middleLegFkJnt_parCons.name = part + type + side + '_parCons'



	# Create lowerLeg
	part = nameSpace +'lower' + legType.capitalize()
	lowerLegFk_ctrl = core.Dag( part + type + side + '_ctrl' )
	lowerLegFk_ctrl.nmCreateController( ctrlShape )
	lowerLegFkZro_grp = rigTools.zeroGroup( lowerLegFk_ctrl )
	lowerLegFkZro_grp.name = part + type + side + 'Zro_grp'
	lowerLegFk_ctrl.editCtrlShape( axis = charScale * 0.8 )
	lowerLegFkGmbl_ctrl = core.createGimbal( lowerLegFk_ctrl )
	lowerLegFk_ctrl.color = colorSide
	lowerLegFk_ctrl.rotateOrder = 'yzx'
	lowerLegFkGmbl_ctrl.rotateOrder = 'yzx'
	# Parenting and positioning
	lowerLegFkZro_grp.matchPosition( lowerLeg_fkJnt )
	lowerLegFkZro_grp.matchRotation( lowerLeg_fkJnt )
	# Constraint
	lowerLegFkJnt_parCons = core.parentConstraint( lowerLegFkGmbl_ctrl , lowerLeg_fkJnt )
	lowerLegFkJnt_parCons.name = part + type + side + '_parCons'



	# Create ankle
	part = nameSpace +'ankle' + legType.capitalize()
	ankleFk_ctrl = core.Dag( part + type + side + '_ctrl' )
	ankleFk_ctrl.nmCreateController( ctrlShape )
	ankleFkZro_grp = rigTools.zeroGroup( ankleFk_ctrl )
	ankleFkZro_grp.name = part + type + side + 'Zro_grp'
	ankleFk_ctrl.editCtrlShape( axis = charScale * 0.7 )
	ankleFkGmbl_ctrl = core.createGimbal( ankleFk_ctrl )
	ankleFk_ctrl.color = colorSide
	ankleFk_ctrl.rotateOrder = 'xzy'
	ankleFkGmbl_ctrl.rotateOrder = 'xzy'
	# Parenting and positioning
	ankleFkZro_grp.matchPosition( ankle_fkJnt )
	ankleFkZro_grp.matchRotation( ankle_fkJnt )
	# Constraint
	legFkJnt_parCons = core.parentConstraint( ankleFkGmbl_ctrl , ankle_fkJnt )
	legFkJnt_parCons.name = part + type + side + '_parCons'


	# Create ball
	part = nameSpace +'ball' + legType.capitalize()
	ballFk_ctrl = core.Dag( part + type + side + '_ctrl' )
	ballFk_ctrl.nmCreateController( ctrlShape )
	ballFkZro_grp = rigTools.zeroGroup( ballFk_ctrl )
	ballFkZro_grp.name = part + type + side + 'Zro_grp'
	ballFk_ctrl.editCtrlShape( axis = charScale * 0.7 )
	ballGmbl_ctrl = core.createGimbal( ballFk_ctrl )
	ballFk_ctrl.color = colorSide
	ballFk_ctrl.rotateOrder = 'xzy'
	ballGmbl_ctrl.rotateOrder = 'xzy'
	# Parenting and positioning
	ballFkZro_grp.matchPosition( ball_fkJnt )
	ballFkZro_grp.matchRotation( ball_fkJnt )
	# Constraint
	ballFkJnt_parCons = core.parentConstraint( ballGmbl_ctrl , ball_fkJnt )
	ballFkJnt_parCons.name = part + type + side + '_parCons'


	# Parent upper ,lower and ankle
	ballFkZro_grp.parent( ankleFkGmbl_ctrl )
	ankleFkZro_grp.parent( lowerLegFkGmbl_ctrl )
	lowerLegFkZro_grp.parent( middleLegFkGmbl_ctrl )
	middleLegFkZro_grp.parent( upperLegFkGmbl_ctrl )

	# Parent upperLeg to All fk ctrl 
	upperLegFkZro_grp.parent( fkCtrl_grp )
	print ('\n#### End of %s %s %s Rig ####' %(type,part,side))



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  IK Controller
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	# = = = = = = create IK rig grp = = = = = = = = #

	ctrlType = 'Ik'

	# Create ik rig grp
	part = nameSpace + legType
	armIkCtrl_grp = core.Null( part + ctrlType + 'Ctrl' + side + '_grp' )
	armIkCtrl_grp.snap( priorJnt )
	armIkCtrl_grp.parent( legRig_grp )


	# Create ik joint grp
	armIkJnt_grp = core.Null( part + ctrlType + 'Jnt' + side + '_grp' )
	armIkJnt_grp.snap( priorJnt )
	armIkJnt_grp.parent( jnt_grp )


	# create ik joint
	upperLeg_ikJnt = rigTools.jointAt( upperLeg )
	midLeg_ikJnt = rigTools.jointAt( midLeg )
	lowerLeg_ikJnt = rigTools.jointAt( lowerLeg )
	ankle_ikJnt	 = rigTools.jointAt( ankle )
	ball_ikJnt	 = rigTools.jointAt( ball )
	toe_ikJnt	 = rigTools.jointAt( toe )

	upperLeg_ikJnt.name = rawName[0] + side + '_ikJnt' 
	midLeg_ikJnt.name = rawName[1] + side + '_ikJnt' 
	lowerLeg_ikJnt.name = rawName[9] + side + '_ikJnt'
	ankle_ikJnt.name = rawName[2] + side + '_ikJnt'
	ball_ikJnt.name = rawName[4] + side + '_ikJnt'
	toe_ikJnt.name = rawName[5] + side + '_ikJnt'



	# Parent
	midLeg_ikJnt.parent( upperLeg_ikJnt )
	lowerLeg_ikJnt.parent( midLeg_ikJnt )
	ankle_ikJnt.parent( lowerLeg_ikJnt )
	ball_ikJnt.parent( ankle_ikJnt )
	toe_ikJnt.parent( ball_ikJnt )
	upperLeg_ikJnt.parent( armIkJnt_grp )


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Transfer preferredAngle from guide to IK joint
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	guide_map_ik = [
		(tmpJnt[0], upperLeg_ikJnt),
		(tmpJnt[1], midLeg_ikJnt),
		(tmpJnt[9], lowerLeg_ikJnt),
		(tmpJnt[2], ankle_ikJnt)
	]
	
	pref_attrs = ['guide_preferredAngleX', 'guide_preferredAngleY', 'guide_preferredAngleZ']

	for guide_jnt, ik_jnt in guide_map_ik:
		for attr in pref_attrs:
			if mc.attributeQuery(attr, node=guide_jnt, exists=True):
				val = mc.getAttr(guide_jnt + '.' + attr)
				if val != 0:
					target_attr = attr.replace('guide_', '')
					ik_jnt.attr(target_attr).value = val
					QuardrupedLogger.info('Set %s.%s to %s from guide.' %(ik_jnt.name, target_attr, val))

	
	uprIK = upperLeg_ikJnt.name
	midIK = midLeg_ikJnt.name
	lwrIK = lowerLeg_ikJnt.name
	ankleIK = ankle_ikJnt.name
	ikJntLst = ( uprIK,midIK,lwrIK,ankleIK )

	

	# Create IK angle 
	# [0] is upper leg , [2] is lower leg

	
	QuardrupedLogger.info('ENABLE IK SPRING SOLVER.')
	
	
	try:
		# lowerIk_ikh = core.IkRp(	startJoint = ikJntLst[0], endEffector = ikJntLst[2]	)
		lowerIk_ikh = core.IkSpring(	startJoint = ikJntLst[0], endEffector = ikJntLst[2]	) # try to change for better result
	except:
		mc.error("Please enable Maya IkSpring solver by typing 'ikSpringSolver' before use this module.")

	lowerIk_ikh.name = rawName[9] + side + '_ikSpring_handle'
	lowerIk_ikh.eff = rawName[9] + side + '_eff'
	lowerIk_ikh.attr('v').value = 0
	mc.error('break 3')
	
	# mc.error('break 446')
	# 
	# 		Create ik handle controller 
	# 


	name = nameSpace + rawName[9] 
	# name = nameSpace + rawName[9] + legType.capitalize()

	# this ctrl don't show shape on viewport
	lowerLegIK_ctrl = core.Dag( name +'Ik'+ side + '_ctrl' )
	lowerLegIK_ctrl.nmCreateController('cube_ctrlShape')
	# lowerLegIK_ctrl.nmCreateController('squarePlain_ctrlShape')
	lowerLegIK_ctrl.editCtrlShape( axis = charScale * 1 )
	lowerLegIK_ctrl.setColor(colorSide)

	# Reshape ik handle
	# heel_tmp = core.Dag( 'heelRollLFT_tmpJnt'  )
	# toesTip_tmp = core.Dag( 'toesTipLFT_tmpJnt'  )
	# adjust foot ik controller
	fSA = heel.getWorldSpace()
	fSB = toe.getWorldSpace()
	QuardrupedLogger.info(0.5+fSA[2]+fSB[2])
	# make it too small
	# lowerLegIK_ctrl.scaleShape( scale = (	1.5 , 1.5, 	fSA[2]/26 + fSB[2]/26	)		 )
	lowerLegIK_ctrl.setColor( colorSide )

	

	# Fix to point prosition cause of this is ik legle it should be world orientation
	lowerLegIK_ctrl.snapPoint ( lowerLeg_ikJnt )


	# Create zero grp
	lowerLegIkZro_grp = rigTools.zeroGroup( lowerLegIK_ctrl )
	lowerLegIkZro_grp.name = ( name +'Ik'+ side + 'Zro_grp' )

	# Make ankle ik controll ikJnt ankle rotation  
	legIkRotation = core.orientConstraint( lowerLegIK_ctrl , ankle_ikJnt.name  , mo = True )
	legIkRotation.name = name + ctrlType + side + '_orientCons'


	# Create pov and parent
	tmpPov = rawName[3]
	# rawPov = misc.splitName( tmpPov )
	print(tmpPov)

	# change index to one
	# create grp
	povZro_grp = core.Null( nameSpace + 'knee' + legType.capitalize() + side + 'Zro_grp' )



	#... Create POV Controller
	name = nameSpace + tmpPov + legType.capitalize() + side
	pov_ctrl = core.Dag( name + '_ctrl' )

	# pov_ctrl.nmCreateController(povShape)
	if povShape == 'sphereAxis':
		# Change Shape from sphere to pyramid la
		pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')

	elif povShape == 'pyramid':
		pov_ctrl.nmCreateController('pyramid_ctrlShape')
		pov_ctrl.rotateShape( rotate = ( 90 , 0 , 0) )
		#... Add pole vector line 
		pc.targetPov( ctrl = pov_ctrl.name , jnt = lowerLeg_bJnt.name )



	pov_ctrl.editCtrlShape( axis = charScale * 0.8 )
	pov_ctrl.setColor('yellow')




	

	mc.parent( pov_ctrl.name , povZro_grp  )
	# Snap with orient and prosition
	povZro_grp.snap(povLeg)


	# misc.snapPointConst( tmpPov , povZro_grp )



	
	print ('''\n
	# ========== # create root IK Controller
	''')

	# rootName = upperLeg_bJnt.name.split('_')[0][:-3]
	rawNam = upperLeg_bJnt.name.split('_')
	rootName = rawName[0]
	# [0] = 'upperLegLFT'
	# [0][:-3]	= 'upperLeg'



	rootName =  rootName + 'Ik' + side
	ikRoot = core.Dag(rootName + '_ctrl')
	ikRoot.nmCreateController('cube_ctrlShape')

	ikRoot.editCtrlShape( axis = charScale * 5.5 )
	ikRoot.setColor(colorSide)
	IkRootZro_grp = rigTools.zeroGroup( ikRoot )
	IkRootZro_grp.name = rootName + 'Zro_grp'
	IkRootZro_grp.snap(upperLeg_bJnt)

	ikRootGmbl_ctrl = core.createGimbal( ikRoot )
	# ========== # constraint to bind joint
	rootIk_parCons = core.parentConstraint( ikRootGmbl_ctrl , upperLeg_ikJnt.name   )
	rootIk_parCons.name = part + side + 'Jnt_parCons'

	
	'''
	# # #  Shift to here because i want to add attr to leg stretchy
	'''
	footBehav = [ 'footOut','footIn','heelRoll','toeRoll','ballRoll','ankle' ,'rollBackAnkle']
	# Create ankle controller
	ctrlName = nameSpace + footBehav[5] + legType + 'IK' + side  
	ankleIk_ctrl = core.Dag(ctrlName +  '_ctrl')
	ankleIk_ctrl.nmCreateController( 'cube_ctrlShape' )
	ankleIk_ctrl.rotateShape( rotate = (90,90,0) )
	ankleIk_ctrl.editCtrlShape( axis = charScale * 10 )
	ankleIk_ctrl.setColor( colorSide )
	# Create zero group
	ankleIkZro_grp = rigTools.zeroGroup( ankleIk_ctrl )
	ankleIkZro_grp.name = ctrlName + 'Zro_grp'
	# Snap position
	ankleIkZro_grp.snapPoint( ankle_ikJnt )
	
	

	#  Pov ankle
	mc.poleVectorConstraint ( pov_ctrl.name , lowerIk_ikh.name , name = nameSpace + 'knee' + legType.capitalize() + side + '_povCons' , w = 1  )
	mc.parent( povZro_grp , lowerLegIK_ctrl.name )	

	

	# ========== # create local / world for Pole Vector
	# change lowerLegIK_ctrl to ankleIk_ctrl
	partName = nameSpace +'knee'
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.parentLocalWorldCtrl( pov_ctrl , ankleIk_ctrl , parentTo , povZro_grp , partName )
	Loc_grp.name = part + 'Local_grp'
	World_grp.name = part + 'World_grp'
	WorldGrp_orientCons.name = part + side + 'WorldGrp_parCons'
	ZroGrp_orientCons.name = part + side + 'ZroGrp_parCons'
	reverseNode_rev.name = part + side + 'ZroGrParCons_rev'



	#... Create attribute for rollBackAnkle
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'toe_Aim' , k = True , minValue = 0 , maxValue = 1  ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'autoStretch' 	, k = True , minValue = 0 , maxValue = 1 ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True  ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'lowStretch' 	, k = True  ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'Upper_IK' 	, k = True, minValue = 0 , maxValue = 1 ,dv = 0 )
	ankleIk_ctrl.hideArnoldNode()



	

	# Create ik stretchy
	# update more arg
	stretchNode = create.iKStretch(	ikJnt = (    upperLeg_ikJnt.name , midLeg_ikJnt.name ,lowerLeg_ikJnt.name )  , 
								ikCtrl = ( ikRoot.name , ankleIk_ctrl.name ) , 
								region = legType	,  
								side = side , 
								scaleCtrl = 'placement_ctrl'	, 
								noTouchGrp = 	noTouchGrp ,
								lowNam = rawName[2]  )

	pmaNode = stretchNode[0]
	psStreEndName = stretchNode[1]

	# Create attr FK/Ik switch attr
	stick_ctrl.addAttribute( attributeType = 'float' , longName = 'FK_IK' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )



	# Pair constraint between ik >> bJnt << fk
	placementCtrl = stick_ctrl.name
	# need only upper , lower , anlke , ball .Then i add that name to this list manually 
	# [0] is upper
	# [9] is middle
	# [1] is lower
	# [2] is ankle
	# [4] is ball
	QuardrupedLogger.info('this is rawName %s' %rawName)





	rawName = ['upLeg%s' %(position), 'lowLeg%s' %(position), 'midLeg%s' %(position), 'ankle%s' %(position) , 'ballRoll%s' %(position)]


	for each in rawName:	
		QuardrupedLogger.info('\n')
		QuardrupedLogger.info(each + side +'_fkJnt')
		QuardrupedLogger.info(each + side +'_ikJnt')
		QuardrupedLogger.info(each + side +'_bJnt')

		
		psCon = mc.parentConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_bJnt'  ,name = each +'Switch'+'_parentCons' , mo = True)
		revNode = mc.createNode( 'reverse' , name = each + 'Switch' + side + '_rev' )
		
		
		# IK = W1
		# Just tempolary for switch fk/ik
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , revNode + '.inputX'  )
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , psCon[0] + '.' + each + side + '_ikJnt' + 'W1' )
		## Add scale constraint

		# FK = W0
		mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.' + each + side +'_fkJnt' + 'W0'  )
		## Add scale constraint




	# Parent to main grp
	jnt_grp.parent('jnt_grp')
	jnt_grp.attr('visibility').value = showInfo
	legRig_grp.parent( parentTo )
	stickZro_grp.parent( parentTo )
	IkRootZro_grp.parent( armIkCtrl_grp )

	# Switch visibility each FK/IK
	stickVis_rev = core.Reverse()
	stickVis_rev.name = part + 'StickVis' + side + '_rev'

	# Fk switch
	stick_ctrl.attr('FK_IK') >> stickVis_rev.attr('inputX')
	stickVis_rev.attr('outputX') >> fkCtrl_grp.attr('visibility')

	# Set value FK/IK switch
	stick_ctrl.attr('FK_IK').value = 1
	stick_ctrl.attr('FK_IK') >> lowerLegIkZro_grp.attr('visibility')
	stick_ctrl.attr('FK_IK') >> IkRootZro_grp.attr('visibility')

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Lock and hide attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	ikRoot.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	pov_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )

	# mc.setAttr(lowerLegIK_ctrl.shape + '.visibility' , 0)
	# lowerLegIK_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'v')
	mc.connectAttr('{0}.Upper_IK'.format(ankleIk_ctrl.name), '{0}.visibility'.format(lowerLegIK_ctrl.shape), f=True)

	print ('\n#### End of %s %s Rig ####' %( part,side ))






	print ('\n#### Starting of foot Behavior of %s Rig ####\n' %side)
	# create  ball roll controller
	ctrlName = nameSpace + footBehav[4] + 'Ik' + legType + side
	ballRoll_ctrl = core.Dag(ctrlName  + '_ctrl')
	ballRoll_ctrl.nmCreateController( 'ballRoll%s_IK_ctrlShape' %side )
	ballRoll_ctrl.editCtrlShape( axis = charScale * 1.25 )
	ballRoll_ctrl.setColor('yellow')
	# Create zero group
	ballRollZro_grp = rigTools.zeroGroup( ballRoll_ctrl )
	ballRollZro_grp.name = ctrlName + 'Zro_grp'
	# Snap position
	ballRollZro_grp.snap( ball_bJnt )
		

	# Create footOut controller
	ctrlName = nameSpace + footBehav[0] + 'IK' + legType + side 
	footOut_ctrl = core.Dag(ctrlName+ '_ctrl')
	footOut_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footOut_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footOut_ctrl.setColor('yellow')
	# Create zero group
	footOutZro_grp = rigTools.zeroGroup( footOut_ctrl )
	footOutZro_grp.name = ctrlName + 'Zro_grp'
	# Snap position
	footOutZro_grp.snap( footOut ) 	


	# Create footIn controller
	ctrlName = nameSpace + footBehav[1]+ 'IK'  + legType + side 
	footIn_ctrl = core.Dag(ctrlName + '_ctrl' )
	footIn_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footIn_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footIn_ctrl.setColor('yellow')
	# Create zero group
	footInZro_grp = rigTools.zeroGroup( footIn_ctrl )
	footInZro_grp.name = ctrlName + 'Zro_grp'
	# Snap position
	footInZro_grp.snap( footIn ) 


	# Create footHeel controller
	ctrlName = nameSpace + footBehav[2] + legType + 'IK' + side 
	footHeel_ctrl = core.Dag(ctrlName + '_ctrl')
	footHeel_ctrl.nmCreateController( 'sphere_ctrlShape'  )
	footHeel_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footHeel_ctrl.setColor('yellow')
	# Create zero group
	footHeelZro_grp = rigTools.zeroGroup( footHeel_ctrl )
	footHeelZro_grp.name =ctrlName  +  'Zro_grp'
	# Snap position
	footHeelZro_grp.snap( heel )


	# Create toeRoll controller
	ctrlName = nameSpace + footBehav[3] + legType + 'IK' + side  
	footToe_ctrl = core.Dag(ctrlName +  '_ctrl')
	footToe_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footToe_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footToe_ctrl.setColor('yellow')
	# Create zero group
	footToeZro_grp = rigTools.zeroGroup( footToe_ctrl )
	footToeZro_grp.name = ctrlName + 'Zro_grp'
	# Snap position
	footToeZro_grp.snap( toe_bJnt )


	# create IK handle
	# Create lowLeg >>> ankle IK handle
	ankleIk_ikh = core.IkRp( startJoint = lowerLeg_ikJnt , endEffector = ankle_ikJnt  )
	ankleIk_ikh.name = nameSpace + footBehav[5] + legType + side  + '_ikh'
	ankleIk_ikh.eff = nameSpace + footBehav[5] + legType + side + '_eff'
	ankleIk_ikh.attr('v').value = showInfo

	# Create ankle >>> ball  IK handle
	ballIk_ikh = core.IkRp( startJoint = ankle_ikJnt , endEffector = ball_ikJnt  )
	ballIk_ikh.name = nameSpace + footBehav[4] + legType + side  + '_ikh'
	ballIk_ikh.eff = nameSpace + footBehav[4] + legType + side + '_eff'
	ballIk_ikh.attr('v').value = showInfo

	# Create ball >>> toeRoll   IK handle
	toeIk_ikh = core.IkRp( startJoint = ball_ikJnt , endEffector = toe_ikJnt  )
	toeIk_ikh.name = nameSpace + footBehav[3] + legType + side  + '_ikh'
	toeIk_ikh.eff = nameSpace + footBehav[3] + legType + side + '_eff'
	toeIk_ikh.attr('v').value = showInfo



	# Create ankle controller

	ctrlName = nameSpace + footBehav[6] + legType + 'IK'  
	rollBackAnkleIk_ctrl = core.Dag( ctrlName + side +  '_ctrl')
	rollBackAnkleIkZro_grp = core.Null( ctrlName + 'Aim' + side + 'Zro_grp' )
	rollBackAnkleIkOffset_grp = core.Null( ctrlName + 'Aim' + side + 'Offset_grp' )
	rollBackAnkleIk_ctrl.nmCreateController( 'orientAxisC_ctrlShape' )
	rollBackAnkleIk_ctrl.rotateShape( rotate = ( 0 , 0 , 90) )
	rollBackAnkleIk_ctrl.editCtrlShape( axis = charScale * 0.75 )
	rollBackAnkleIk_ctrl.hideArnoldNode()
	rollBackAnkleIk_ctrl.setColor( colorSide )
	rollBackAnkleIkOffset_grp.parent( rollBackAnkleIkZro_grp )
	rollBackAnkleIk_ctrl.parent( rollBackAnkleIkOffset_grp )
	# Snap position to ankle joint na
	rollBackAnkleIkZro_grp.snap( ankle_ikJnt )

	# Parenting
	ankleIkZro_grp.parent( lowerLegIK_ctrl )
	footInZro_grp.parent( footOut_ctrl )
	footHeelZro_grp.parent( footIn_ctrl )
	footToeZro_grp.parent( footHeel_ctrl )
	footOutZro_grp.parent( ankleIk_ctrl )
	# lowerLegIkZro_grp.parent( footToe_ctrl )
	ballRollZro_grp.parent( footToe_ctrl )
	# ankleIkZro_grp.parent( ballRoll_ctrl )
	rollBackAnkleIkZro_grp.parent( ballRoll_ctrl )


	# Parenting ikh 
	# shift this parent after adjust aimCon
	# ankleIk_ikh.parent( rollBackAnkleIk_ctrl	 )
	# lowerIk_ikh.parent(	rollBackAnkleIk_ctrl	)
	ballIk_ikh.parent( ballRoll_ctrl )
	toeIk_ikh.parent( footToe_ctrl )

	# Create static grp for pair switch aimLeg
	ctrlName = nameSpace + footBehav[6] + legType + 'IK'  
	rollBackAnkleIkStill_grp = core.Null( ctrlName + side + 'Still_grp' )
	rollBackAnkleIkStill_grp.maSnap( upperLeg_bJnt)
	rollBackAnkleIkStill_grp.parent( ankleIk_ctrl )


	# make rollBack Aim upLegBack
	# aimVec = ( 0,1,0 )
	# upVec = ( 0,0,1 )

	# create up obj to prevent joint filp
	up_obj = core.Locator(ctrlName + side + '_loc')
	up_obj.maSnap(rollBackAnkleIkOffset_grp)

	# set initial position of loc here
	mc.move( 0, 0,  charScale*30, up_obj.name, relative=True, objectSpace=True, worldSpaceDistance = True )
	upperLeg_aimCons = core.aimConstraint( upperLeg_ikJnt , rollBackAnkleIkStill_grp  , rollBackAnkleIkOffset_grp , mo = True ,  aimVector = ( 0,-1,0 ) , upVector = ( 0,0,1 ), worldUpType='object', worldUpObject = up_obj.name )

	# upperLeg_aimCons = core.aimConstraint( upperLeg_ikJnt , rollBackAnkleIkStill_grp  , rollBackAnkleIkOffset_grp , mo = True ,  aimVector = ( 0,-1,0 ) , upVector = ( 0,0,1 ), worldUpObject = pov_ctrl.name )
	# upperLeg_aimCons = core.aimConstraint( upperLeg_ikJnt , rollBackAnkleIkStill_grp  , rollBackAnkleIkOffset_grp , mo = True )
	# upperLeg_aimCons = core.aimConstraint( upperLeg_ikJnt , rollBackAnkleIkStill_grp  , rollBackAnkleIkOffset_grp , mo = True ,  aimVector = ( 0,-1,0 ) , upVector = ( 0,0,1 ), worldUpObject = pov_ctrl.name )
	# upperLeg_aimCons = core.aimConstraint( upperLeg_ikJnt , rollBackAnkleIkStill_grp  , rollBackAnkleIkOffset_grp , mo = True ,  aimVector = aimVec , upVector = upVec, worldUpObject = pov_ctrl.name )

	# cancle world up type setup use from abrove arg instead
	upperLeg_aimCons.attr('worldUpType').value = 1

	upperLeg_aimCons.attr( upperLeg_ikJnt.name + 'W0').value = 1
	upperLeg_aimCons.name = ctrlName + side + '_aimCons' 
	toeAnim_rev = core.Reverse()
	toeAnim_rev.name = ctrlName + side + '_rev' 
	# Switch Controller
	ankleIk_ctrl.attr( 'toe_Aim' ) >> toeAnim_rev.attr( 'inputY' )
	ankleIk_ctrl.attr( 'toe_Aim' ) >> upperLeg_aimCons.attr( rollBackAnkleIkStill_grp.name + 'W1') 
	toeAnim_rev.attr( 'outputY' ) >> upperLeg_aimCons.attr( upperLeg_ikJnt.name + 'W0')

	# Parent after adjust orientation
	ankleIk_ikh.parent( rollBackAnkleIk_ctrl )
	lowerIk_ikh.parent( rollBackAnkleIk_ctrl )

	# Parenting
	lowerLegIkZro_grp.parent( parentTo )


	# parent up obj to the ik_ctrl
	up_obj.parent(ankleIk_ctrl)
	up_obj.attr('v').value = 0
	QuardrupedLogger.info('Foot rig complete.')


	print (''' \n
	# = = = = = = Create elbow knee Lock Rig function
	''')

	QuardrupedLogger.info('Create %s' %ikRootGmbl_ctrl.name)
	rawNameUPR , distanceUPRName , povUPR_Ctrl , lowerUPR_loc , upperUPR_loc = midLockModule.createDistance( nameSpace , part = 'up' , startP = ikRootGmbl_ctrl.name , endP = pov_ctrl.name )
	QuardrupedLogger.info('Create %s' %pov_ctrl.name)
	rawNameLWR , distanceLWRName , povLWR_Ctrl , lowerLWR_loc , upperLWR_loc = midLockModule.createDistance( nameSpace , part = 'dn' ,startP = pov_ctrl.name , endP = lowerLegIK_ctrl.name )
	

	#rawNameUPR , distanceUPRName , povUPR_Ctrl , lowerUPR_loc , upperUPR_loc = midLockModule.createDistance( nameSpace , startP = ikRootGmbl_ctrl.name , endP = pov_ctrl.name )
	#rawNameLWR , distanceLWRName , povLWR_Ctrl , lowerLWR_loc , upperLWR_loc = midLockModule.createDistance( nameSpace , startP = pov_ctrl.name , endP = lowerLegIK_ctrl.name ) 
	blendName,invertNodeName  = midLockModule.createBlendColor(		nameSpace 	,
										uprDistance = distanceUPRName			, 
										lwrDistance = distanceLWRName 			,
										side 		=  side   					,
										uprNam 		= rawNameUPR	)
	attrName = midLockModule.doAddAttr( povUPR_Ctrl , region )
	midLockModule.connectIkJnt(	stretchNode = pmaNode , upperIKJnt = midLeg_ikJnt.name , lowerIKJnt = lowerLeg_ikJnt.name , blendName = blendName , namLock = attrName	, povName = povUPR_Ctrl,alongAxis = alongAxis )




	print (''' \n
	# = = = = = = Create Ribbon Rig function
	''')

	if ribbon == True:

		if ribbonRes == 'high':
			numJoints = 5
		else:
			numJoints = 3


		hingesUprBtm = ribbonRig.ribbonRig(
			nameSpace = nameSpace 				,
			width = 10								,
			numJoints = numJoints					,
			side = side								,
			jointTop = upperLeg_bJnt			,
			jointBtm = midLeg_bJnt			,
			part = ribbonName[0]							,
			charScale = charScale					,
			noTouch_grp = noTouchGrp				,
			showInfo = showInfo 						,	
			ctrl_grp = legRig_grp.name )



		hingesLwrTop = ribbonRig.ribbonRig(
				nameSpace = nameSpace 				,
				width = 10								,
				numJoints = numJoints					,
				side = side								,
				jointTop = midLeg_bJnt			,
				jointBtm = lowerLeg_bJnt				,
				part = ribbonName[1]							,
				charScale = charScale					,
				noTouch_grp = noTouchGrp				,
				showInfo = showInfo  						,
				ctrl_grp = legRig_grp.name )



		ribbonRig.makeHigesMover( 						part = legType, 		
														nameSpace = nameSpace 				,
														side = side 						, 
														btmName = hingesUprBtm				, 
														topName = hingesLwrTop  			, 
														charScale = charScale				,
														moverPosition = midLeg_bJnt.name 			,
														ctrl_grp = 'ctrl_grp'

															)




	print ('\n\n\n\n\n\n #### End of %s %s Rig ####' %( part , side ))






# backup from SVN
# this function is human leg but it can run fourth time for quradrupedLeg 
# this is redundance 
# u should use biped legRig instead

def plantigradeLegRig(

	nameSpace = '' 		,
	parentTo = 'ctrl_grp' 			,
	side = 'LFT'					,
	tmpJnt = (	'upperLegLFT_tmpJnt'  , 'lowerLegLFT_tmpJnt' ,  'ankleLFT_tmpJnt' , 
				'legLFT_pov_tmpJnt' ,'ballLFT_tmpJnt' ,'toesTipLFT_tmpJnt' ,
				'heelRollFrontLFT_tmpJnt' , 'footOutFrontLFT_tmpJnt' , 'footInFrontLFT_tmpJnt'),
	priorJnt = 'hip_bJnt'				,
	ikhGrp = 'ikh_grp' 					,
	noTouchGrp = 'noTouch_grp' 			,
	nullGrp = 'snapNull_grp'			,
	showInfo = False  					,
	ribbon = False						,
	ribbonRes = 'high'					,
	ribbonName = ('upLeg', 'lwrLeg')	,
	charScale = ''						,
	ikPosi = 'foot', # get only 2 variable 'foot' or 'ankle'
	keepFkIkBoth = True	,# keep fk/ik ctrl visibility both or not
	povShape = 'pyramid' # choice pyramid or sphereAxis
	):


	print ('''\n
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# 				biped Leg Rig Function
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	''')
	# temp variable find charscale
	# nameSpace = charName + elem
	# priorJnt = '%s%s' %(nameSpace,priorJnt)

	part = 'ankle'
	if side == 'LFT':
		colorSide = 'red'
	else:
		colorSide = 'blue'

	upperLeg = core.Dag( tmpJnt[ 0 ] )
	lowerLeg = core.Dag( tmpJnt[ 1 ] )
	ankle = core.Dag( tmpJnt[ 2 ] )
	povLeg = core.Dag( tmpJnt[ 3 ] )

	ball = core.Dag(tmpJnt[ 4 ])
	toe = core.Dag( tmpJnt[5] )
	heel = core.Dag( tmpJnt[6] )

	footIn = core.Dag( tmpJnt[7] )
	footOut = core.Dag( tmpJnt[8] )



	# Create bind joint
	upperLeg_bJnt = rigTools.jointAt( upperLeg )
	lowerLeg_bJnt = rigTools.jointAt( lowerLeg )
	ankle_bJnt = rigTools.jointAt( ankle )

	ball_bJnt = rigTools.jointAt( ball )
	toe_bJnt = rigTools.jointAt( toe )





	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Check type is for animal or humal
	# Result : return string
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	if 'Front' in tmpJnt[0] :
		print ('This is animal.')
		legType = 'frontLeg'
	elif 'Back' in tmpJnt[0]:
		legType = 'backLeg'
	else :
		print ('This is human like.')
		legType = 'leg'




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create attr for save position of leg ik
	# Result : add string attr for ctrl_grp
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #


	ikLoc = legType +'ik' + side +'location'
	mc.addAttr('rig_grp' , longName = ikLoc, dt = 'string')
	mc.setAttr('rig_grp' + '.' + ikLoc , ikPosi , type = 'string' ,lock = True)
	ikPosiName = mc.getAttr( 'rig_grp' + '.' + ikLoc )




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Store raw name
	# Result : raw name without side
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	rawName = []
	for each in tmpJnt:
		tmp = each.split('_')[0][:-3]
		rawName.append(tmp)


	QuardrupedLogger.info('\nThis is raw name : ')
	QuardrupedLogger.info(rawName)



	upperLeg_bJnt.name =   rawName[0] + side + '_bJnt'
	lowerLeg_bJnt.name =   rawName[1] + side + '_bJnt'
	ankle_bJnt.name =   rawName[2] + side + '_bJnt'
	ball_bJnt.name =   rawName[4] + side + '_bJnt'
	toe_bJnt.name =   rawName[5] + side + '_bJnt'


	# Adjust rotate order
	upperLeg_bJnt.rotateOrder = 'yzx'
	lowerLeg_bJnt.rotateOrder = 'yzx'
	ankle_bJnt.rotateOrder = 'yzx'


	# Parent
	lowerLeg_bJnt.parent( upperLeg_bJnt )
	ankle_bJnt.parent( lowerLeg_bJnt )
	toe_bJnt.parent(ball_bJnt)
	ball_bJnt.parent(ankle_bJnt)


	# add lable
	upperLeg_bJnt.setLable( side ,'none')
	lowerLeg_bJnt.setLable( side ,'knee')
	ankle_bJnt.setLable( side ,'foot')
	toe_bJnt.setLable( side ,'toe')
	ball_bJnt.setLable( side ,'none')


	ankle_bJnt.attr('segmentScaleCompensate').value = 0
	# Parent it to prior joint
	upperLeg_bJnt.parent( priorJnt )



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create main rig grp
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	part = nameSpace + legType
	legRig_grp = core.Null( part + 'Rig' + side + '_grp' )
	legRigGrp_parCons = core.parentConstraint( priorJnt , legRig_grp )
	legRigGrp_parCons.name = part + 'Rig' + side + '_parCons'

	# Create joint grp
	jnt_grp = core.Null( part + 'Jnt' + side + '_grp' )



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Stick Controller 
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	stick_ctrl = core.Dag( part + 'Stick' + side + '_ctrl' )
	stick_ctrl.nmCreateController('stick_ctrlShape')
	stick_ctrl.editCtrlShape( axis = charScale * 3.6 )
	stick_ctrl.color = 'yellow'
	stick_ctrl.hideArnoldNode()

	if side == 'LFT':
		stick_ctrl.attr('rotateX').value -= 90

	else:
		stick_ctrl.attr('rotateX').value -= 90


	stickZro_grp = rigTools.zeroGroup( stick_ctrl )
	stickZro_grp.name = part + 'Stick'+ side + 'Zro_grp'
	stickZro_grp.matchPosition( ankle_bJnt )
	QuardrupedLogger.info('Set rotation to %s controller...' %stick_ctrl.name)


	type = 'Fk'
	ctrlGrp_parCons = core.parentConstraint( ankle_bJnt , stickZro_grp , mo = True)
	ctrlGrp_parCons.name = part + side + 'Stick'+ '_parCons'
	stick_ctrl.addAttribute( longName = 'legScale' , defaultValue = 1 , keyable = True )



	# Loch and hide
	stick_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )





	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Create FK
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create fk rig grp

	part = nameSpace + legType
	armFkCtrl_grp = core.Null( part + 'FkCtrl' + side + '_grp' )
	armFkCtrl_grp.snap( priorJnt )
	armFkCtrl_grp.parent( legRig_grp )

	# Create Fk joint grp
	armFkJnt_grp = core.Null( part + 'FkJnt' + side + '_grp' )
	armFkJnt_grp.snap( priorJnt )
	armFkJnt_grp.parent( jnt_grp )

	# create FK joint
	upperLeg_fkJnt = rigTools.jointAt( upperLeg )
	lowerLeg_fkJnt = rigTools.jointAt( lowerLeg )
	ankle_fkJnt	 = rigTools.jointAt( ankle )
	ball_fkJnt = rigTools.jointAt( ball )

	# Use variable instead
	upperLeg_fkJnt.name =  rawName[0] + side + '_fkJnt' 
	lowerLeg_fkJnt.name = rawName[1] + side + '_fkJnt'
	ankle_fkJnt.name = rawName[2] + side + '_fkJnt'
	ball_fkJnt.name = rawName[4] + side + '_fkJnt'

	# Parent
	lowerLeg_fkJnt.parent( upperLeg_fkJnt )
	ankle_fkJnt.parent( lowerLeg_fkJnt )
	ball_fkJnt.parent( ankle_fkJnt )
	upperLeg_fkJnt.parent( armFkJnt_grp )

	# Set rotation order
	upperLeg_fkJnt.rotateOrder = 'xyz'
	lowerLeg_fkJnt.rotateOrder = 'yzx'
	ankle_fkJnt.rotateOrder = 'xzy'
	ball_fkJnt.rotateOrder = 'yzx'

	# Create upperLeg
	part = nameSpace + rawName[0] #+ legType.capitalize() 
	type = 'Fk'
	ctrlShape = 'lowerLeg%s_FK_ctrlShape' %side

	upperLeg_ctrl = core.Dag( part + type + side + '_ctrl' )
	upperLeg_ctrl.nmCreateController( ctrlShape )
	upperLegZro_grp = rigTools.zeroGroup( upperLeg_ctrl )
	upperLegZro_grp.name = part + type + side + 'Zro_grp'
	upperLeg_ctrl.editCtrlShape( axis = charScale * 0.9 )
	upperLegGmbl_ctrl = core.createGimbal( upperLeg_ctrl )
	upperLeg_ctrl.color = colorSide
	upperLeg_ctrl.rotateOrder = 'xyz'
	upperLegGmbl_ctrl.rotateOrder = 'xyz'
	# Parenting and positioning
	upperLegZro_grp.matchPosition( upperLeg_fkJnt )
	upperLegZro_grp.matchRotation( upperLeg_fkJnt )
	# Constraint
	upperLegFkJnt_parCons = core.parentConstraint( upperLegGmbl_ctrl , upperLeg_fkJnt )
	upperLegFkJnt_parCons.name = part + type + side + '_parCons'



	# Create lowerLeg
	part = nameSpace + rawName[1] #+ legType.capitalize()  
	lowerLeg_ctrl = core.Dag( part + type + side + '_ctrl' )
	lowerLeg_ctrl.nmCreateController( ctrlShape )
	lowerLegZro_grp = rigTools.zeroGroup( lowerLeg_ctrl )
	lowerLegZro_grp.name = part + type + side + 'Zro_grp'
	lowerLeg_ctrl.editCtrlShape( axis = charScale * 0.8 )
	lowerLegGmbl_ctrl = core.createGimbal( lowerLeg_ctrl )
	lowerLeg_ctrl.color = colorSide
	lowerLeg_ctrl.rotateOrder = 'yzx'
	lowerLegGmbl_ctrl.rotateOrder = 'yzx'
	# Parenting and positioning
	lowerLegZro_grp.matchPosition( lowerLeg_fkJnt )
	lowerLegZro_grp.matchRotation( lowerLeg_fkJnt )
	# Constraint
	lowerLegFkJnt_parCons = core.parentConstraint( lowerLegGmbl_ctrl , lowerLeg_fkJnt )
	lowerLegFkJnt_parCons.name = part + type + side + '_parCons'



	# Create ankle
	part = nameSpace + rawName[2] 
	ankleFk_ctrl = core.Dag( part + type + side + '_ctrl' )
	ankleFk_ctrl.nmCreateController( ctrlShape )
	ankleFkZro_grp = rigTools.zeroGroup( ankleFk_ctrl )
	ankleFkZro_grp.name = part + type + side + 'Zro_grp'
	ankleFk_ctrl.editCtrlShape( axis = charScale * 0.7 )
	ankleFkGmbl_ctrl = core.createGimbal( ankleFk_ctrl )
	ankleFk_ctrl.color = colorSide
	ankleFk_ctrl.rotateOrder = 'xzy'
	ankleFkGmbl_ctrl.rotateOrder = 'xzy'
	# Parenting and positioning
	ankleFkZro_grp.matchPosition( ankle_fkJnt )
	ankleFkZro_grp.matchRotation( ankle_fkJnt )

	# # Fix prosition of ankle 
	# ankleFkZro_grp.attr('translateY').value = 0
	

	# Constraint
	legFkJnt_parCons = core.parentConstraint( ankleFkGmbl_ctrl , ankle_fkJnt )
	legFkJnt_parCons.name = part + type + side + '_parCons'



	# Create ball
	part = nameSpace +rawName[4] 
	ball_ctrl = core.Dag( part + type + side + '_ctrl' )
	ball_ctrl.nmCreateController( ctrlShape )
	ballZro_grp = rigTools.zeroGroup( ball_ctrl )
	ballZro_grp.name = part + type + side + 'Zro_grp'
	ball_ctrl.editCtrlShape( axis = charScale * 0.7 )
	ballGmbl_ctrl = core.createGimbal( ball_ctrl )
	ball_ctrl.color = colorSide
	ball_ctrl.rotateOrder = 'xzy'
	ballGmbl_ctrl.rotateOrder = 'xzy'
	# Parenting and positioning
	ballZro_grp.matchPosition( ball_fkJnt )
	ballZro_grp.matchRotation( ball_fkJnt )
	# Constraint
	ballFkJnt_parCons = core.parentConstraint( ballGmbl_ctrl , ball_fkJnt )
	ballFkJnt_parCons.name = part + type + side + '_parCons'

	# Parent upper ,lower and ankle
	ballZro_grp.parent( ankleFkGmbl_ctrl )
	ankleFkZro_grp.parent( lowerLegGmbl_ctrl )
	lowerLegZro_grp.parent( upperLegGmbl_ctrl )

	# Parent upperLeg to All fk ctrl 
	upperLegZro_grp.parent( armFkCtrl_grp )

	print ('\n#### End of %s %s %s Rig ####' %(type,part,side))




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  IK Controller
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	# = = = = = = create IK rig grp = = = = = = = = #

	ctrlType = 'Ik'

	# Create ik rig grp
	part = nameSpace + legType 
	armIkCtrl_grp = core.Null( part + ctrlType + 'Ctrl' + side + '_grp' )
	armIkCtrl_grp.snap( priorJnt )
	armIkCtrl_grp.parent( legRig_grp )



	# Create ik joint grp
	armIkJnt_grp = core.Null( part + ctrlType + 'Jnt' + side + '_grp' )
	armIkJnt_grp.snap( priorJnt )
	armIkJnt_grp.parent( jnt_grp )



	# create ik joint
	upperLeg_ikJnt = rigTools.jointAt( upperLeg )
	lowerLeg_ikJnt = rigTools.jointAt( lowerLeg )
	ankle_ikJnt	 = rigTools.jointAt( ankle )
	ball_ikJnt	 = rigTools.jointAt( ball )
	toe_ikJnt	 = rigTools.jointAt( toe )
	upperLeg_ikJnt.name = rawName[0] + side + '_ikJnt' 
	lowerLeg_ikJnt.name = rawName[1] + side + '_ikJnt'
	ankle_ikJnt.name = rawName[2] + side + '_ikJnt'
	ball_ikJnt.name = rawName[4] + side + '_ikJnt'
	toe_ikJnt.name = rawName[5] + side + '_ikJnt'



	# Parent
	lowerLeg_ikJnt.parent( upperLeg_ikJnt )
	ankle_ikJnt.parent( lowerLeg_ikJnt )
	ball_ikJnt.parent( ankle_ikJnt )
	toe_ikJnt.parent( ball_ikJnt )
	upperLeg_ikJnt.parent( armIkJnt_grp )



	uprIK = upperLeg_ikJnt.name
	midIK = lowerLeg_ikJnt.name
	lwrIK = ankle_ikJnt.name
	ikJntLst = ( uprIK,midIK,lwrIK )



	# Create IK legle 
	ankle_ikh = core.IkRp(	startJoint = ikJntLst[0], endEffector = ikJntLst[2]	)
	ankle_ikh.name =  rawName[2] + side + '_ikh'
	ankle_ikh.eff =  rawName[2] + side + '_eff'
	ankle_ikh.attr('v').value = 0


	# 
	# 		Create ik handle controller
	# 

	name = nameSpace +legType+ 'ankle' 
	ankleIk_ctrl = core.Dag( name +'Ik'+ side + '_ctrl' )


	# 	Choice ik handle controller

	if ikPosi == 'foot':
		ankleIk_ctrl.nmCreateController('squarePlain_ctrlShape')
	elif ikPosi == 'ankle':
		ankleIk_ctrl.nmCreateController('cube_ctrlShape')
	else:
		ankleIk_ctrl.nmCreateController('squarePlain_ctrlShape')
	



	ankleIk_ctrl.editCtrlShape( axis = charScale * 4 )
	ankleIk_ctrl.setColor(colorSide)


	# Reshape ik handle
	# heel_tmp = core.Dag( 'heelRollLFT_tmpJnt'  )
	# toesTip_tmp = core.Dag( 'toesTipLFT_tmpJnt'  )
	# adjust foot ik controller
	fSA = heel.getWorldSpace()
	fSB = toe.getWorldSpace()
	ftScl = ((fSA[2] + fSB[2])*0.8)
	QuardrupedLogger.info('foot scale is =================================')
	QuardrupedLogger.info(ftScl)
	ankleIk_ctrl.scaleShape( scale = (	ftScl/3 , 1.5 , ftScl	)		 )
	ankleIk_ctrl.setColor( colorSide )



	# Create Attr
	ankleIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'autoStretch' 	, k = True , minValue = 0 , maxValue = 1 ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True  ,dv = 0 )
	# ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True , minValue = -500 ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'lowStretch' 	, k = True  ,dv = 0 )
	ankleIk_ctrl.hideArnoldNode()

	

	# attention
	# Change ik position following animator commet

	try:
		if ikPosiName == 'foot':
			ankleIk_ctrl.snapPoint (ball_ikJnt)
		elif ikPosiName == 'ankle':
			ankleIk_ctrl.snapPoint (ankle_ikJnt)
	except :
		mc.warning('Please Check attribute name in rig_grp.')




	

	# Create zero grp
	ikZro_grp = rigTools.zeroGroup( ankleIk_ctrl )
	ikZro_grp.name = ( name +'Ik'+ side + 'Zro_grp' )

	ankleIkGmbl_ctrl = core.createGimbal( ankleIk_ctrl )

	# Make ankle ik controll ikJnt ankle rotation  
	legIkRotation = core.orientConstraint( ankleIkGmbl_ctrl , ankle_ikJnt.name  , mo = True )
	legIkRotation.name = name + ctrlType + side + '_orientCons'

	# Parent ik legle under ik ctrl
	mc.parent( ankle_ikh.name ,  ankleIkGmbl_ctrl.name )



	# Create pov and parent
	tmpPov = tmpJnt[3]
	rawPov = misc.splitName( tmpPov )
	QuardrupedLogger.info(rawPov[1])
	# change index to one
	povZro_grp = mc.group(em = True , name = nameSpace + 'knee' +legType + side + 'Zro_grp' )	
	# Create POV Controller
	name = nameSpace + rawPov[1] 
	pov_ctrl = core.Dag( nameSpace + 'knee'+legType+ side + '_ctrl' )


	if povShape == 'sphereAxis':
		# Change Shape from sphere to pyramid la
		pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')

	elif povShape == 'pyramid':
		pov_ctrl.nmCreateController('pyramid_ctrlShape')
		pov_ctrl.rotateShape( rotate = ( 90 , 0 , 0) )
		#... Add pole vector line 
		pc.targetPov( ctrl = pov_ctrl.name , jnt = lowerLeg_bJnt.name )


	pov_ctrl.editCtrlShape( axis = charScale * 1.2 )
	pov_ctrl.setColor( colorSide )

	mc.parent( pov_ctrl.name , povZro_grp  )
	# Snap with orient and prosition
	misc.snapParentConst( tmpPov , povZro_grp )
	# misc.snapPointConst( tmpPov , povZro_grp )

	#  move here
	mc.poleVectorConstraint ( pov_ctrl.name , ankle_ikh.name , name = nameSpace + 'knee'  + side + '_povCons' , w = 1  )
	mc.parent( povZro_grp , ankleIkGmbl_ctrl.name )	



	# ========== # create local / world for Pole Vector
	partName = nameSpace + 'knee'
	Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.parentLocalWorldCtrl( pov_ctrl , ankleIkGmbl_ctrl , parentTo , povZro_grp , partName )
	Loc_grp.name = partName + side + 'Local_grp'
	World_grp.name = partName + side + 'World_grp'
	WorldGrp_orientCons.name = partName + side + 'WorldGrp_parCons'
	ZroGrp_orientCons.name = partName + side + 'ZroGrp_parCons'
	reverseNode_rev.name = partName + side + 'ZroGrParCons_rev'

	QuardrupedLogger.info('''\n# ========== # create root IK Controller # ========== #	''')


	# rootName = upperLeg_bJnt.name.split('_')[0][:-3]
	rawNam = upperLeg_bJnt.name.split('_')
	rootName = rawName[0]
	# [0] = 'upperLegLFT'
	# [0][:-3]	= 'upperLeg'





	part = nameSpace 
	rootName =  rootName + legType + 'Ik' + side
	ikRoot = core.Dag(rootName + '_ctrl')
	ikRoot.nmCreateController('cube_ctrlShape')
	
	ikRoot.editCtrlShape( axis = charScale * 5.5 )
	ikRoot.setColor(colorSide)
	ikRootZro_grp = rigTools.zeroGroup( ikRoot )
	ikRootZro_grp.name = rootName + 'Zro_grp'
	ikRootZro_grp.snap(upperLeg_bJnt)
	ikRootGmbl_ctrl = core.createGimbal( ikRoot )
	# ========== # constraint to bind joint
	rootIk_parCons = core.parentConstraint( ikRootGmbl_ctrl , upperLeg_ikJnt.name   )
	rootIk_parCons.name = part + side + 'Jnt_parCons'



	# Create ik stretchy
	stretchNode = create.iKStretch(	ikJnt = (    upperLeg_ikJnt.name , lowerLeg_ikJnt.name , ankle_ikJnt.name )  , 
									ikCtrl = ( ikRoot.name , ankleIk_ctrl.name ) , 
									region = legType	,  
									side = side , 
									scaleCtrl = 'placement_ctrl'	, 
									noTouchGrp = 	noTouchGrp ,
									lowNam = rawName[2] )
		
	pmaNode = stretchNode[0]
	psStreEndName = stretchNode[1]

	# Create attr FK/Ik switch attr
	stick_ctrl.addAttribute( attributeType = 'float' , longName = 'FK_IK' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )
	if keepFkIkBoth == True:
		stick_ctrl.addAttribute( attributeType = 'bool' , longName = 'fkVis' , minValue = 0 , maxValue = 1 , defaultValue = 1 , keyable = True )
		stick_ctrl.addAttribute( attributeType = 'bool' , longName = 'ikVis' , minValue = 0 , maxValue = 1 , defaultValue = 1 , keyable = True )




	# constraint pair each of bind joint to FK and IK
	# Exclude POV joint
	
	# namJnt = rawName[:-1]
	# print 'namJnt is %s' %namJnt


	placementCtrl = stick_ctrl.name
	# need only upper , lower , anlke , ball .Then i add that name to this list manually 
	# [0] is upper
	# [1] is lower
	# [2] is anlke
	# [4] is ball
	rawName = ['{0}{1}'.format( nameSpace ,rawName[0] ), '{0}{1}'.format(nameSpace,rawName[1]), '{0}{1}'.format(nameSpace,rawName[2]), '{0}{1}'.format(nameSpace,rawName[4])]
	print ('\n\n')
	print ('this is rawName %s' %rawName)
	print ('\n\n')

	for each in rawName:		
		
		# if each == '{0}{1}'.format( nameSpace,legType ) or each == '{0}{1}'.format( nameSpace,rawName[3] ):
		# if each == '{0}{1}'.format(nameSpace,rawName[5]):

			# continue

		print ('\n\n\n\n\n')
		print (each + side +'_fkJnt')
		print (each + side +'_ikJnt')
		print (each + side +'_bJnt')

		psCon = mc.parentConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_bJnt'  ,name = each +'Switch'+'_parentCons' )
		## Add scale constraint
		#scCon = mc.scaleConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_bJnt'  ,name = each +'Switch'+'_scaleCons' )

		
		revNode = mc.createNode( 'reverse' , name = each + 'Switch' + side + '_rev' )
		
		
		# Connection fk/ik Stick controller switch to placement
		# IK = W1
		# Just tempolary for switch fk/ik
		
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , revNode + '.inputX'  )
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , psCon[0] + '.' + each + side + '_ikJnt' + 'W1' )
		## Add scale constraint
		#mc.connectAttr( revNode + '.outputX' ,  scCon[0]+'.'+ each + side +'_ikJnt' + 'W1' )

		# FK = W0
		mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.' + each + side +'_fkJnt' + 'W0'  )
		## Add scale constraint
		#mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) ,  scCon[0]+'.'+ each + side +'_fkJnt' + 'W0' )



	# Parent to main grp
	jnt_grp.parent('jnt_grp')
	jnt_grp.attr('visibility').value = 0
	legRig_grp.parent( parentTo )
	stickZro_grp.parent( parentTo )
	ikZro_grp.parent( ikhGrp )
	ikRootZro_grp.parent( armIkCtrl_grp )


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Switch visibility each FK/IK
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	if keepFkIkBoth == True:	# Change the stick attribute
		stick_ctrl.attr('ikVis') >> ikZro_grp.attr('visibility')
		stick_ctrl.attr('ikVis') >> ikRootZro_grp.attr('visibility')
		stick_ctrl.attr('fkVis') >> armFkCtrl_grp.attr('visibility')

	elif keepFkIkBoth == False:
		stickVis_rev = core.Reverse()
		stickVis_rev.name = part + 'StickVis' + side + '_rev'

		# Fk switch
		stick_ctrl.attr('FK_IK') >> stickVis_rev.attr('inputX')
		stickVis_rev.attr('outputX') >> armFkCtrl_grp.attr('visibility')

		# Set value FK/IK switch
		stick_ctrl.attr('FK_IK') >> ikZro_grp.attr('visibility')
		stick_ctrl.attr('FK_IK') >> ikRootZro_grp.attr('visibility')

	# Set leg to IK
	stick_ctrl.attr('FK_IK').value = 1


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Lock and hide attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	ankleIk_ctrl.lockHideAttrLst( 'sx' , 'sy' , 'sz' , 'v' )
	ikRoot.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	pov_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )

	ankleIkGmbl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'v')
	#return stick_ctrl.name
	print ('\n#### End of %s %s Rig ####\n' %(part,side))



	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# foot Roll rig
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	print ('\n#### Starting of %s %s Rig ####\n' %('foot Behavior',side))
	footBehav = ['footOut','footIn','heelRoll','toeRoll','ballRoll','ankle']



	# Create ball roll controller
	ctrlName = nameSpace + footBehav[4] +legType+ 'Ik'  + side
	ballRoll_ctrl = core.Dag(ctrlName  + '_ctrl')
	ballRoll_ctrl.nmCreateController( 'ballRoll%s_IK_ctrlShape' %side )
	ballRoll_ctrl.editCtrlShape( axis = charScale * 1.25 )
	ballRoll_ctrl.setColor('yellow')
	# Create zero group
	ballRollZro_grp = rigTools.zeroGroup( ballRoll_ctrl )
	ballRollZro_grp.name = ctrlName + 'Zro_grp'



	# Create footOut controller
	ctrlName = nameSpace + footBehav[0] +legType+ 'IK'  + side 
	footOut_ctrl = core.Dag(ctrlName+ '_ctrl')
	footOut_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footOut_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footOut_ctrl.setColor('yellow')
	# Create zero group
	footOutZro_grp = rigTools.zeroGroup( footOut_ctrl )
	footOutZro_grp.name = ctrlName + 'Zro_grp'



	# Create footIn controller
	ctrlName = nameSpace + footBehav[1]+legType+ 'IK'  + side 
	footIn_ctrl = core.Dag(ctrlName + '_ctrl' )
	footIn_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footIn_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footIn_ctrl.setColor('yellow')
	# Create zero group
	footInZro_grp = rigTools.zeroGroup( footIn_ctrl )
	footInZro_grp.name = ctrlName + 'Zro_grp'



	# Create footHeel controller
	ctrlName = nameSpace + footBehav[2]  +legType+ 'IK' + side 
	footHeel_ctrl = core.Dag(ctrlName + '_ctrl')
	footHeel_ctrl.nmCreateController( 'sphere_ctrlShape'  )
	footHeel_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footHeel_ctrl.setColor('yellow')
	# Create zero group
	footHeelZro_grp = rigTools.zeroGroup( footHeel_ctrl )
	footHeelZro_grp.name =ctrlName  +  'Zro_grp'



	# Create toeRoll controller
	ctrlName = nameSpace + footBehav[3]  +legType+ 'IK' + side  
	footToe_ctrl = core.Dag(ctrlName +  '_ctrl')
	footToe_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footToe_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footToe_ctrl.setColor('yellow')
	# Create zero group
	footToeZro_grp = rigTools.zeroGroup( footToe_ctrl )
	footToeZro_grp.name = ctrlName + 'Zro_grp'


	priorJnt = ankle_bJnt.name
	jntLst = ( ball_bJnt.name  ,  toe_bJnt.name)
	priorIkJnt = misc.splitName(priorJnt)[0]

	# Create IK handle for ankle roll
	# ankle to ball 
	# Beware ik misProsition from wrong rotate place location of lower joint
	ballIk_ikh = core.IkRp(  startJoint = ankle_ikJnt.name , endEffector = ball_ikJnt.name  )
	ballIk_ikh.name = nameSpace + footBehav[4]  + side  + '_ikh'
	ballIk_ikh.eff = nameSpace + footBehav[4]  + side + '_eff'
	ballIk_ikh.attr('v').value = 0

	# Create IK handle for toe roll
	# ball to toeTip 
	toesTip_ikh = core.IkRp(   startJoint = ball_ikJnt.name , endEffector = toe_ikJnt.name   )
	toesTip_ikh.name = nameSpace + footBehav[3]  + side + '_ikh'
	toesTip_ikh.eff = nameSpace + footBehav[3]  + side + '_eff'
	toesTip_ikh.attr('v').value = 0

	# Snap each grp to joint prosition
	footOutZro_grp.snap( footOut ) 
	footInZro_grp.snap( footIn ) 
	footHeelZro_grp.snap( heel ) 
	ballRollZro_grp.snap( ball_bJnt )
	footToeZro_grp.snap( toe_bJnt )


	# Footin ---> footOut
	footInZro_grp.parent( footOut_ctrl )
	# Heel roll ---> footIn
	footHeelZro_grp.parent( footIn_ctrl )
	# Toe ---> Heel
	footToeZro_grp.parent( footHeel_ctrl )
	# Ball  ---> Toe
	ballRollZro_grp.parent( footToe_ctrl )



	# Parent ikh to FootRoll group
	ballIk_ikh.parent( ballRoll_ctrl )
	toesTip_ikh.parent( footToe_ctrl )
	footOutZro_grp.parent( ankleIkGmbl_ctrl )
	ankle_ikh.parent( ballRoll_ctrl )





	print (''' \n
	# Create Null Snap group for matcher #
	''')

	offset_null = core.Null( legType + 'Offset' + side + '_null')
	offset_null.maSnap( ankle_bJnt, position = True , rotation = False , scale = True )
	offset_parCons = core.parentConstraint( ankle_bJnt , offset_null , mo = True)
	offset_parCons.name = legType + 'Offset' + side + '_parCons'
	offset_null.parent( nullGrp )


	print (''' \n
	# = = = = = = Create elbow knee Lock Rig function
	''')
	rawNameUPR , distanceUPRName , povUPR_Ctrl , lowerUPR_loc , upperUPR_loc = midLockModule.createDistance( nameSpace , startP = ikRootGmbl_ctrl.name , endP = pov_ctrl.name ,part ='up' )
	rawNameLWR , distanceLWRName , povLWR_Ctrl , lowerLWR_loc , upperLWR_loc = midLockModule.createDistance( nameSpace , startP = pov_ctrl.name , endP = ankleIkGmbl_ctrl.name , part ='dn' )
	blendName,invertNodeName  = midLockModule.createBlendColor(         nameSpace ,
										uprDistance = distanceUPRName		, 
										lwrDistance = distanceLWRName 		,
										side 		=  side   				,
										uprNam 		= rawNameUPR	           )

	attrName = midLockModule.doAddAttr( povUPR_Ctrl , rawNameUPR  )
	midLockModule.connectIkJnt(	stretchNode = pmaNode , upperIKJnt = lowerLeg_ikJnt.name , lowerIKJnt = ankle_ikJnt.name , blendName = blendName , namLock = attrName	, povName = povUPR_Ctrl )

	# Delete toe bind joint
	mc.delete(toe_bJnt.name)

	mc.select(deselect = True)


	# # Add pole vector line 
	# pc.targetPov( ctrl = pov_ctrl.name , jnt = lowerLeg_bJnt.name )



	if ribbon == True:

		if ribbonRes == 'high':
			numJoints = 5
		else:
			numJoints = 3


		HingesUprBtm = ribbonRig.ribbonRig(
			nameSpace = nameSpace 				,
			width = 10								,
			numJoints = numJoints					,
			side = side								,
			jointTop = upperLeg_bJnt.name			,
			jointBtm = lowerLeg_bJnt.name			,
			part = ribbonName[0]							,
			charScale = charScale					,
			noTouch_grp = noTouchGrp				,
			showInfo = showInfo 						,	
			ctrl_grp = legRig_grp.name )

	

		HingesLwrTop = ribbonRig.ribbonRig(
				nameSpace = nameSpace 				,
				width = 10								,
				numJoints = numJoints					,
				side = side								,
				jointTop = lowerLeg_bJnt.name			,
				jointBtm = ankle_bJnt.name				,
				part = ribbonName[1]							,
				charScale = charScale					,
				noTouch_grp = noTouchGrp				,
				showInfo = showInfo  						,
				ctrl_grp = legRig_grp.name )



		ribbonRig.makeHigesMover( 						part = legType, 		
														nameSpace = nameSpace 				,
														side = side 						, 
														btmName = HingesUprBtm				, 
														topName = HingesLwrTop  			, 
														charScale = charScale				,
														moverPosition = lowerLeg_bJnt.name 		,
														ctrl_grp = 'ctrl_grp'

															)




	print ('\n\n\n\n\n\n #### End of %s %s Rig  add preferred angle####' %( part , side ))












def add_guide_preferred_angle_attrs():
	"""
	Adds 'guide_preferredAngle' X, Y, Z attributes to the selected joints.
	Used to input values that the AutoRig will read and utilize.
	"""
	# 1. Find the selected joints
	selection = mc.ls(sl=True, type='joint')
	
	if not selection:
		mc.warning("Please select at least one joint.")
		return

	# 2. Attribute names to create (avoiding Maya's existing 'preferredAngle' name)
	attrs = ['guide_preferredAngleX', 'guide_preferredAngleY', 'guide_preferredAngleZ']

	for jnt in selection:
		for attr in attrs:
			# Check if the attribute already exists to prevent errors.
			if not mc.attributeQuery(attr, node=jnt, exists=True):
				# Create the attribute as a float (double) and make it Keyable (visible in the Channel Box).
				mc.addAttr(jnt, longName=attr, attributeType='double', defaultValue=0, keyable=True)
				print(f"Created {attr} on {jnt}")
			else:
				print(f"Skipped {attr} on {jnt} (Already exists)")

	print("\nDone! Attributes added. Please check Channel Box.")