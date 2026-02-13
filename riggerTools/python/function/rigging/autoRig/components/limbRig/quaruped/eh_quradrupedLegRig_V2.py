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


# from function.rigging.autoRig.components.limbRig.quaruped import eh_quradrupedLegRig_V2


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

	
	QuardrupedLogger.info('ENABLE DOUBLE IK SOLVER (Proxy Chain).')

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Double IK Implementation
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	# 1. Identify Joints
	hip_jnt = upperLeg_ikJnt
	knee_jnt = midLeg_ikJnt
	hock_jnt = lowerLeg_ikJnt
	ankle_jnt = ankle_ikJnt

	# 2. Determine Primary Axis (based on Knee -> Hock)
	# We assume the translation is mostly on one axis
	# This logic helps to place the proxy ankle correctly along the bone axis
	tx = abs(mc.getAttr(hock_jnt.name + '.tx'))
	ty = abs(mc.getAttr(hock_jnt.name + '.ty'))
	tz = abs(mc.getAttr(hock_jnt.name + '.tz'))
	
	primary_axis = 'tx'
	if ty > tx and ty > tz: primary_axis = 'ty'
	elif tz > tx and tz > ty: primary_axis = 'tz'
	
	# 3. Calculate Scale/Lengths (local translation sum)
	len_knee_hock = mc.getAttr(hock_jnt.name + '.' + primary_axis) 
	len_hock_ankle = mc.getAttr(ankle_jnt.name + '.' + primary_axis)
	len_proxy_low = len_knee_hock + len_hock_ankle

	# 4. Create Proxy Chain
	# Hip Proxy
	pxyHip_jnt = rigTools.jointAt(hip_jnt)
	pxyHip_jnt.name = rawName[0] + side + '_pxyJnt'
	
	# Knee Proxy
	pxyKnee_jnt = rigTools.jointAt(knee_jnt)
	pxyKnee_jnt.name = rawName[1] + side + '_pxyJnt'
	pxyKnee_jnt.parent(pxyHip_jnt)

	# Ankle Proxy (Extended)
	# Create at Knee to inherit orientation, then move
	pxyAnkle_jnt = rigTools.jointAt(knee_jnt) 
	pxyAnkle_jnt.name = rawName[2] + side + '_pxyJnt' 
	pxyAnkle_jnt.parent(pxyKnee_jnt)
	
	# Extend Proxy Ankle to full length
	pxyAnkle_jnt.attr(primary_axis).value = len_proxy_low
	
	# Verify Proxy Hierarchy parenting
	pxyHip_jnt.parent(armIkJnt_grp)
	pxyHip_jnt.attr('visibility').value = 0 # Hide Proxy Chain by default

	# 5. Create IK Handles
	# Main IK: Hip -> Hock
	main_ikh = core.IkRp(startJoint=hip_jnt, endEffector=hock_jnt)
	main_ikh.name = rawName[0] + side + '_main_ikh'
	main_ikh.eff = rawName[0] + side + '_main_eff'
	main_ikh.attr('v').value = 0
	
	# Proxy IK: ProxyHip -> ProxyAnkle
	proxy_ikh = core.IkRp(startJoint=pxyHip_jnt, endEffector=pxyAnkle_jnt)
	proxy_ikh.name = rawName[0] + side + '_proxy_ikh'
	proxy_ikh.eff = rawName[0] + side + '_proxy_eff'
	proxy_ikh.attr('v').value = 0

	# 6. Controls Setup
	
	# Create Main Ankle IK Control
	ctrlName = nameSpace + rawName[2] + legType + 'IK' + side 
	ankleIk_ctrl = core.Dag(ctrlName + '_ctrl')
	ankleIk_ctrl.nmCreateController('cube_ctrlShape')
	ankleIk_ctrl.rotateShape(rotate=(90, 90, 0))
	ankleIk_ctrl.editCtrlShape(axis=charScale * 10)
	ankleIk_ctrl.setColor(colorSide)
	
	ankleIkZro_grp = rigTools.zeroGroup(ankleIk_ctrl)
	ankleIkZro_grp.name = ctrlName + 'Zro_grp'
	# Snap to Real Ankle
	ankleIkZro_grp.snapPoint(ankle_jnt) # Snap to ankle

	# Create Hock IK Control (secondary)
	ctrlName = nameSpace + rawName[9] + legType + 'IK' + side
	hockIk_ctrl = core.Dag(ctrlName + '_ctrl')
	hockIk_ctrl.nmCreateController('orientAxisC_ctrlShape') 
	hockIk_ctrl.editCtrlShape(axis=charScale * 2.0)
	hockIk_ctrl.setColor('yellow')

	hockIk_pos = core.Null(ctrlName + '_pos')
	# Snap pos to Proxy Ankle (end of proxy chain)
	hockIk_pos.snap(pxyAnkle_jnt)
	
	# Setup Hierarchy: Ankle -> Hock_Pos -> Hock_Ctrl
	hockIk_pos.parent(ankleIk_ctrl)
	hockIk_ctrl.parent(hockIk_pos)
	
	# 7. Constraints & Logic
	# Hock Pos aims at Proxy Knee
	# Aim Vector -X? (Assuming bone points X)
	# Ref script used aimVector (0,1,0) up (0,0,1).
	# If current joint setup is 'yzx', X is length.
	# We aim BACK at knee. If X is forward, -X is back.
	aim_vec = (-1, 0, 0) if primary_axis == 'tx' else (0, -1, 0)
	up_vec = (0, 0, 1) # Standard Z up?
	
	hock_aimConst = core.aimConstraint(pxyKnee_jnt, hockIk_pos, mo=False, 
									   aimVector=aim_vec,
									   upVector=up_vec, 
									   worldUpType="objectrotation", 
									   worldUpObject=ankleIk_ctrl.name)

	# Hock Joint constraint
	# Hock Joint Aims at Hock Ctrl (aligns lower leg bone)
	forward_vec = (1, 0, 0) if primary_axis == 'tx' else (0, 1, 0)
	core.aimConstraint(hockIk_ctrl, hock_jnt, mo=True,
					   aimVector=forward_vec,
					   upVector=up_vec,
					   worldUpType="objectrotation",
					   worldUpObject=ankleIk_ctrl.name)
	
	# IK Handles Parenting
	# Main IK follows Hock Ctrl
	core.parentConstraint(hockIk_ctrl, main_ikh, mo=True)
	
	# Proxy IK follows Ankle Ctrl
	core.parentConstraint(ankleIk_ctrl, proxy_ikh, mo=True)

	# 8. Pole Vector Controller
	tmpPov = rawName[3]
	povZro_grp = core.Null(nameSpace + 'knee' + legType.capitalize() + side + 'Zro_grp')
	name = nameSpace + tmpPov + legType.capitalize() + side
	pov_ctrl = core.Dag(name + '_ctrl')
	
	if povShape == 'sphereAxis':
		pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')
	elif povShape == 'pyramid':
		pov_ctrl.nmCreateController('pyramid_ctrlShape')
		pov_ctrl.rotateShape(rotate=(90, 0, 0))
		pc.targetPov(ctrl=pov_ctrl.name, jnt=lowerLeg_bJnt.name) # Use Bind Joint for visual line

	pov_ctrl.editCtrlShape(axis=charScale * 0.8)
	pov_ctrl.setColor('yellow')
	
	mc.parent(pov_ctrl.name, povZro_grp)
	povZro_grp.snap(povLeg) # Snap to guide POV
	
	# Constraint IK PVs
	mc.poleVectorConstraint(pov_ctrl.name, main_ikh.name, w=1)
	mc.poleVectorConstraint(pov_ctrl.name, proxy_ikh.name, w=1)
	
	# Parent PV Control to Ankle Controller (Standard for this type of rig)
	mc.parent(povZro_grp, ankleIk_ctrl.name)

	# 9. Cleanup / Integration
	# Alias for compatibility with footer code if needed
	lowerLegIK_ctrl = hockIk_ctrl 
	
	# Create IK Root (Hip) Control
	rootName = rawName[0] + 'Ik' + side
	ikRoot = core.Dag(rootName + '_ctrl')
	ikRoot.nmCreateController('cube_ctrlShape')
	ikRoot.editCtrlShape(axis=charScale * 5.5)
	ikRoot.setColor(colorSide)
	IkRootZro_grp = rigTools.zeroGroup(ikRoot)
	IkRootZro_grp.name = rootName + 'Zro_grp'
	IkRootZro_grp.snap(upperLeg_bJnt)
	ikRootGmbl_ctrl = core.createGimbal(ikRoot)
	rootIk_parCons = core.parentConstraint(ikRootGmbl_ctrl, upperLeg_ikJnt.name)

	# Define lowerLegIkZro_grp alias for hock pos (for visibility switch compatibility)
	lowerLegIkZro_grp = hockIk_pos 
	
	
	# Attributes on Ankle Ctrl
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'toe_Aim' , k = True , minValue = 0 , maxValue = 1  ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'autoStretch' 	, k = True , minValue = 0 , maxValue = 1 ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'upStretch' 	, k = True  ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'lowStretch' 	, k = True  ,dv = 0 )
	ankleIk_ctrl.addAttribute(  attributeType = 'long' ,ln = 'Upper_IK' 	, k = True, minValue = 0 , maxValue = 1 ,dv = 0 )
	ankleIk_ctrl.hideArnoldNode()

	# Create ik stretchy
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
	
	
	# Pair constraint between ik >> bJnt << fk needs rawName list of all 5 joints?
	# Original code had loop over: upLeg, lowLeg, midLeg, ankle, ballRoll.
	# Note: rawName in V2 code around line 671 was:
	# rawName = ['upLeg%s' %(position), 'lowLeg%s' %(position), 'midLeg%s' %(position), 'ankle%s' %(position) , 'ballRoll%s' %(position)]
	# I should ensure this list logic is preserved or executed.
	# The original code re-defined `rawName` variable at line 671.
	# I am replacing up to line 729. 
	# Line 671 is INSIDE my replacement block.
	# So I MUST include it.
	
	QuardrupedLogger.info('DOUBLE IK SETUP COMPLETE.')

	# Re-define rawName for Switch Constraint Loop (Legacy Logic)
	# Need 'position' variable. Defined earlier?
	# Yes, line 130/134.
	rawName = ['upLeg%s' %(position), 'lowLeg%s' %(position), 'midLeg%s' %(position), 'ankle%s' %(position) , 'ballRoll%s' %(position)]

	for each in rawName:	
		QuardrupedLogger.info('\n')
		QuardrupedLogger.info(each + side +'_fkJnt')
		QuardrupedLogger.info(each + side +'_ikJnt')
		QuardrupedLogger.info(each + side +'_bJnt')

		psCon = mc.parentConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_bJnt'  ,name = each +'Switch'+'_parentCons' , mo = True)
		revNode = mc.createNode( 'reverse' , name = each + 'Switch' + side + '_rev' )
		
		# IK = W1
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , revNode + '.inputX'  )
		mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , psCon[0] + '.' + each + side + '_ikJnt' + 'W1' )

		# FK = W0
		mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.' + each + side +'_fkJnt' + 'W0'  )


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
	# Visibility for IK controls
	# lowerLegIkZro_grp is hockIk_pos alias
	stick_ctrl.attr('FK_IK') >> lowerLegIkZro_grp.attr('visibility')
	stick_ctrl.attr('FK_IK') >> IkRootZro_grp.attr('visibility')
	stick_ctrl.attr('FK_IK') >> ankleIkZro_grp.attr('visibility') # Added ankle visibility switch

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Lock and hide attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	ikRoot.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
	pov_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )

	# Connect visibility of Hock Control Shape to Upper_IK attr on Ankle
	mc.connectAttr('{0}.Upper_IK'.format(ankleIk_ctrl.name), '{0}.visibility'.format(hockIk_ctrl.shape), f=True)

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