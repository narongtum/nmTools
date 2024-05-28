# log
# use the same  rotateOrder of both bJnt and ctrl

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

from function.rigging.tools import proc as pc
reload(pc)

from function.rigging.util import mayaNodeDict as mnd
reload(mnd)

# from function.rigging.autoRig.bodyRig import fkIkGenRig
# reload( fkIkGenRig )

from function.rigging.autoRig.bodyRig import fkIkTwsitGenRig
reload( fkIkTwsitGenRig )

from function.rigging.util import misc as misc
reload(misc)




# bipedLegRig original has been deleted please use below function

# this function just passing throught keyword arg to fkIk function
def bipedLegRigTws(
					nameSpace = '' 	,	
					parentTo = 'ctrl_grp' ,			
					side = 'LFT'	,				
					region = 'leg',
					tmpJnt = (	'upperLegLFT_tmpJnt'  , 'lowerLegLFT_tmpJnt' ,  'ankleLFT_tmpJnt' , 
								'legLFT_pov_tmpJnt' ,'ballLFT_tmpJnt' ,'toesTipLFT_tmpJnt' ,
								'heelRollLFT_tmpJnt' , 'footOutLFT_tmpJnt' , 'footInLFT_tmpJnt'),
					priorJnt = 'hip_bJnt'	,			
					ikhGrp = 'ikh_grp' 	,				
					noTouchGrp = 'noTouch_grp' 	,		
					nullGrp = 'snapNull_grp'	,		
					showInfo = False  ,					
					ribbon = False	,				
					ribbonRes = 'high'	,				
					ribbonName = ('upLeg', 'lwrLeg'),	
					charScale = 1	,					
					ikPosi = 'foot', # get only 2 variable 'foot' or 'ankle'
					keepFkIkBoth = True	,# keep fk/ik ctrl visibility both or not
					povShape = 'pyramid' ,# choice pyramid or sphereAxis
					productionType = 'game' ,
					jnt_grp = 'jnt_grp' ,	
					footAttr = False	,
					linkRotOrder = False ,
					creTwistJnt = False):
	

	misc.makeHeader(	'Start of %s%s Rig' %(region,side)	)





	# Passing arg to fkIkGenRig
	stickNam, lower_bJnt ,middle_bJnt , upper_bJnt , ikhAll_name , stretchEndName_psCon = fkIkTwsitGenRig.fkIkTwsitGenRig(
				nameSpace = nameSpace 	,				
				charScale = charScale	,			
				parentTo = parentTo 	,			
				side = side	,
				region = region		,							
				tmpJnt = tmpJnt,
				priorJnt = priorJnt	,	
				ikhGrp = ikhGrp		,			
				noTouchGrp = noTouchGrp ,			
				nullGrp = nullGrp,			
				jnt_grp =  jnt_grp	,			
				povShape = povShape,
				keepFkIkBoth = keepFkIkBoth,
				ribbon = ribbon,
				ribbonRes = ribbonRes,
				ribbonName = ribbonName,
				showInfo = showInfo 	,
				ikPosi = ikPosi	,
				linkRotOrder = linkRotOrder,
				creTwistJnt = creTwistJnt,
				)






	# Then create fool roll behavior

	if side == 'LFT':
	    colorSide = 'red'
	else:
	    colorSide = 'blue'

	ball = core.Dag(tmpJnt[ 4 ])
	toe = core.Dag( tmpJnt[5] )
	heel = core.Dag( tmpJnt[6] )

	footIn = core.Dag( tmpJnt[7] )
	footOut = core.Dag( tmpJnt[8] )



	# Create bind joint
	upperLeg_bJnt = core.Dag(upper_bJnt)
	lowerLeg_bJnt = core.Dag(middle_bJnt)
	ankle_bJnt = core.Dag( lower_bJnt )

	#upperLeg_bJnt = rigTools.jointAt( upperLeg )
	#lowerLeg_bJnt = rigTools.jointAt( lowerLeg )
	#ankle_bJnt = rigTools.jointAt( ankle )

	ball_bJnt = rigTools.jointAt( ball )
	toe_bJnt = rigTools.jointAt( toe )


	legRotOrder = ( 'xyz' , 'yzx' )


	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Check type is for animal or humal
	# (no need anymore but keep it )
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	if region ==  'frontLeg' :
		print 'This maybe animal limb'
		legType = 'frontLeg'

	elif region ==  'backLeg':
		print 'This maybe animal limb'
		legType = 'backLeg'
	else:
		print 'This maybe human limb.'
		legType = 'leg'	




	












	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Store raw name
	# Result : raw name without side
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	rawName = []
	for each in tmpJnt:
		tmp = each.split('_')[0][:-3]
		rawName.append(tmp)

	print '\nThis is raw name : '  
	print rawName


	ball_bJnt.name =   rawName[4] + side + '_bJnt'
	toe_bJnt.name =   rawName[5] + side + '_bJnt'


	# Adjust rotate order
	# Change it to list

	ball_bJnt.rotateOrder = legRotOrder[1]




	# Parent
	toe_bJnt.parent(ball_bJnt)
	ball_bJnt.parent(ankle_bJnt)


	# add lable
	toe_bJnt.setLable( side ,'toe')
	ball_bJnt.setLable( side ,'none')


	ankle_bJnt.attr('segmentScaleCompensate').value = 0
	ball_fkJnt = rigTools.jointAt( ball )

	# add toe fk joint for Space Switch
	toe_fkJnt = rigTools.jointAt( toe )

	ankle_fkJnt = rawName[2]  + side + '_fkJnt'
	ball_fkJnt.name = rawName[4]  + side + '_fkJnt'
	toe_fkJnt.name = rawName[5]  + side + '_fkJnt'


	# Parent
	ball_fkJnt.parent( ankle_fkJnt )
	toe_fkJnt.parent( ball_fkJnt )

	#upperLeg_fkJnt.parent( armFkJnt_grp )

	# Set rotation order
	ball_fkJnt.rotateOrder = legRotOrder[1]




	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  Fk Controller
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	kind = 'Fk'
	print rawName
	ankleFkGmbl_ctrl = core.Dag( rawName[2] + kind + side + '_gmbCtrl' )



	ctrlShape = 'lowerLeg%s_FK_ctrlShape' %side

	# Create ball
	part = nameSpace +'ball' + legType.capitalize() 
	ballFk_Ctrl = core.Dag( part + kind + side + '_ctrl' )
	ballFk_Ctrl.nmCreateController( ctrlShape )
	ballZro_grp = rigTools.zeroGroup( ballFk_Ctrl )
	ballZro_grp.name = part + kind + side + 'Zro_grp'
	ballFk_Ctrl.editCtrlShape( axis = charScale * 0.7 )
	ballGmbl_ctrl = core.createGimbal( ballFk_Ctrl )
	ballFk_Ctrl.color = colorSide
	ballFk_Ctrl.rotateOrder = legRotOrder[1]
	ballGmbl_ctrl.rotateOrder = legRotOrder[1]
	# Parenting and positioning
	ballZro_grp.matchPosition( ball_fkJnt )
	ballZro_grp.matchRotation( ball_fkJnt )
	# Constraint
	ballFkJnt_parCons = core.parentConstraint( ballGmbl_ctrl , ball_fkJnt )
	ballFkJnt_parCons.name = part + kind + side + '_parCons'


	ballZro_grp.parent( ankleFkGmbl_ctrl )

	print '\n#### End of %s %s %s Rig ####' %(kind,part,side)






	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	#  IK Controller
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #


	# create IK rig grp 
	ctrlType = 'Ik'

	# Create ik rig grp
	part = nameSpace + legType

	# create ik joint
	ball_ikJnt	 = rigTools.jointAt( ball )
	toe_ikJnt	 = rigTools.jointAt( toe )

	ankle_ikJnt = rawName[2] + side + '_ikJnt'
	ball_ikJnt.name = rawName[4] + side + '_ikJnt'
	toe_ikJnt.name = rawName[5] + side + '_ikJnt'





	# Parent
	ball_ikJnt.parent( ankle_ikJnt )
	toe_ikJnt.parent( ball_ikJnt )

	uprIK = rawName[0] + side + '_ikJnt' 
	midIK = rawName[1] + side + '_ikJnt'
	lwrIK = rawName[2] + side + '_ikJnt'

	name = nameSpace  + rawName[2]


	# Instance name of 'zro_grp' , 'ctrl' , 'gmblCtrl'
	# Attention solid variable weak point

	ankleIk_ctrl = core.Dag( name + ctrlType + side + '_ctrl' )
	ikZro_grp = core.Dag( name + ctrlType + side + 'Zro_grp' )
	ankleIkGmbl_ctrl = core.Dag( name + ctrlType + side + '_gmbCtrl' )



	ankleIk_ctrl.editCtrlShape( axis = charScale * 1.1 )
	ankleIk_ctrl.setColor(colorSide)



	# # # # # # # # # # 
	# List of solid variable
	# # # # # # # # # # 

	# ikZro_grp = rawName[2] + ctrlType + side + 'Zro_grp'
	# ikZro_grp = core.Dag( rawName[2] + ctrlType + side + 'Zro_grp' )



	# Change the name of ik ctrl following place ankle or foot
	if ikPosi == 'foot':
		ankleIk_ctrl.name = nameSpace + ikPosi + ctrlType + side + '_ctrl'	# footIKLFT_ctrl
		ikZro_grp.name = nameSpace + ikPosi + ctrlType + side + 'Zro_grp'
		ankleIkGmbl_ctrl.name  = nameSpace + ikPosi + ctrlType + side + '_gmbCtrl' 

	if ikPosi == 'animalFoot':
		# in case for quaruped naming
		ankleIk_ctrl.name = nameSpace + region + ctrlType + side + '_ctrl'	
		ikZro_grp.name = nameSpace + region  + ctrlType + side + 'Zro_grp'
		ankleIkGmbl_ctrl.name  = nameSpace + region + ctrlType + side + '_gmbCtrl' 

	print ankleIk_ctrl.name

	# get ikh gimbal name
	# ankleIkGmbl_ctrl = rawName[2] + ctrlType + side + '_gmbCtrl'
	ankle_ikh = ikhAll_name[0]

	# Adjust controller
	fSA = heel.getWorldSpace()
	fSB = toe.getWorldSpace()
	ftScl = ((fSA[2] + fSB[2])*0.8)
	print 'foot scale is ================================='
	print ftScl
	ankleIk_ctrl.scaleShape( scale = (	ftScl/3 , 1.5 , ftScl	)		 )
	ankleIk_ctrl.setColor( colorSide )





	# relocate child inside of ik handle grp
	for each in ikhAll_name:
	    mc.parent( each , world = True )



	# Attention 1
	# Change ik position following animator comment

	# Attention 2
	# Delete and re constraint for solve ik stretchy problem

	# Attention 3
	# arm Rig must be same code 

	try:
		if ikPosi== 'foot' or ikPosi == 'animalFoot':

			# Delete old parent 
			mc.delete( stretchEndName_psCon )

			# snap zro of ik grp
			ikZro_grp.maSnap ( ball_ikJnt , pos = True )

			# And reparent locator again
			print '.a .b .c .d .e .f .g'
			print stretchEndName_psCon
			endLoc = stretchEndName_psCon.replace('_parCons' , '_loc')
			# endLoc = 'ankle'+ 'EndDist' + side + '_loc'
			mc.parentConstraint( ankleIk_ctrl.name , endLoc , mo = 1, w = 1 , name = stretchEndName_psCon )
			# mc.parentConstraint( ankleIk_ctrl.name , endLoc , mo = 1, w = 1 , name = part + 'EndDist' + side + '_parCons')

		elif ikPosi == 'ankle':
			ikZro_grp.maSnap ( ankle_ikJnt , pos = True)
	except :
		mc.error( 'Please Check attribute %s in rig_grp.' %stretchEndName_psCon )
		return None
		



	for each in ikhAll_name:
	    mc.parent( each ,ankleIkGmbl_ctrl )

	mc.select(deselect = True)
	    

	# make ankle or wrist rotate freely
	# already do it (maybe)
	#legIkRotation = core.orientConstraint( ankleIkGmbl_ctrl , ankle_ikJnt  , mo = True )
	#legIkRotation.name = name + ctrlType + side + '_orientCons'



	print '\n#### Starting of %s %s Rig ####\n' %('foot Behavior',side)
	footBehav = ['footOut','footIn','heelRoll','toeRoll','ballRoll','ankle']	




	# Create ball roll controller
	# nameSpace = nameSpace + legType

	ctrlName = nameSpace + footBehav[4] + legType+ 'Ik'  + side
	ballRoll_ctrl = core.Dag(ctrlName  + '_ctrl')
	ballRoll_ctrl.nmCreateController( 'ballRoll%s_IK_ctrlShape' %side )
	ballRoll_ctrl.editCtrlShape( axis = charScale * 1.25 )
	ballRoll_ctrl.setColor('yellow')
	# Create zero group
	ballRollZro_grp = rigTools.zeroGroup( ballRoll_ctrl )
	ballRollZro_grp.name = ctrlName + 'Zro_grp'
	ballRoll_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )





	# Create footOut controller
	ctrlName = nameSpace + footBehav[0] + legType+ 'IK'  + side 
	footOut_ctrl = core.Dag(ctrlName+ '_ctrl')
	footOut_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footOut_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footOut_ctrl.setColor('yellow')
	# Create zero group
	footOutZro_grp = rigTools.zeroGroup( footOut_ctrl )
	footOutZro_grp.name = ctrlName + 'Zro_grp'
	footOut_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )


	# Create footIn controller
	ctrlName = nameSpace + footBehav[1]+ legType+ 'IK'  + side 
	footIn_ctrl = core.Dag(ctrlName + '_ctrl' )
	footIn_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footIn_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footIn_ctrl.setColor('yellow')
	# Create zero group
	footInZro_grp = rigTools.zeroGroup( footIn_ctrl )
	footInZro_grp.name = ctrlName + 'Zro_grp'
	footIn_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )


	# Create footHeel controller
	ctrlName = nameSpace + footBehav[2]+ legType  + 'IK' + side 
	footHeel_ctrl = core.Dag(ctrlName + '_ctrl')
	footHeel_ctrl.nmCreateController( 'sphere_ctrlShape'  )
	footHeel_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footHeel_ctrl.setColor('yellow')
	# Create zero group
	footHeelZro_grp = rigTools.zeroGroup( footHeel_ctrl )
	footHeelZro_grp.name =ctrlName  +  'Zro_grp'
	footHeel_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )



	# Create toeRoll controller
	ctrlName = nameSpace + footBehav[3]+ legType  + 'IK' + side  
	footToe_ctrl = core.Dag(ctrlName +  '_ctrl')
	footToe_ctrl.nmCreateController( 'sphere_ctrlShape' )
	footToe_ctrl.editCtrlShape( axis = charScale * 1.25 )
	footToe_ctrl.setColor('yellow')
	# Create zero group
	footToeZro_grp = rigTools.zeroGroup( footToe_ctrl )
	footToeZro_grp.name = ctrlName + 'Zro_grp'
	footToe_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )

	

	priorJnt = ankle_bJnt.name
	jntLst = ( ball_bJnt.name  ,  toe_bJnt.name)
	#priorIkJnt = misc.splitName(priorJnt)[0]
	priorIkJnt = rawName[2] + side 




	# Create IK handle for ankle roll
	# ankle to ball 
	# Beware ik misProsition from wrong rotate place location of lower joint
	ballIk_ikh = core.IkRp(  startJoint = ankle_ikJnt , endEffector = ball_ikJnt  )
	ballIk_ikh.name = nameSpace + footBehav[4]+ legType  + side  + '_ikh'
	ballIk_ikh.eff = nameSpace + footBehav[4]+ legType  + side + '_eff'
	ballIk_ikh.attr('v').value = 0


	# Create IK handle for toe roll
	# ball to toeTip 
	toesTip_ikh = core.IkRp(   startJoint = ball_ikJnt.name , endEffector = toe_ikJnt.name   )
	toesTip_ikh.name = nameSpace + footBehav[3]+ legType  + side + '_ikh'
	toesTip_ikh.eff = nameSpace + footBehav[3]+ legType  + side + '_eff'
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
	#ankle_ikh.parent( ballRoll_ctrl )
	mc.parent(ankle_ikh , ballRoll_ctrl.name)

	# variable for create pair of ball joint
	# contraint ball joint
	placementCtrl = stickNam


	print '\nReset the location attribute to ikPosi.'
	stick_ctrl = core.Dag( stickNam )
	stick_ctrl.setAttribute('location'  , ikPosi , type = 'string')
	stick_ctrl.lockHideAttrLst('location')	

	# Adding ball joint for support FK IK Space switch
	stick_ctrl.addAttribute( attributeType = 'message' , longName = 'ballJnt')
	# Connect Message
	ball_bJnt.attr('message') >> stick_ctrl.attr('ballJnt')	

	# Adding ball ctrl for support FK IK Space switch
	stick_ctrl.addAttribute( attributeType = 'message' , longName = 'ballFkCtrl')
	# Connect Message
	ballFk_Ctrl.attr('message') >> stick_ctrl.attr('ballFkCtrl')

	# add toe fk joint to message
	stick_ctrl.addAttribute( attributeType = 'message' , longName = 'toeFkJnt')
	toe_fkJnt.attr('message') >> stick_ctrl.attr('toeFkJnt')	







	psCon = mc.parentConstraint( ball_fkJnt.name , ball_ikJnt.name , ball_bJnt.name  ,name = rawName[4] +'Switch'+ side +'_parCons' )
	revNode = mc.createNode( 'reverse' , name = rawName[4] + 'Switch' + side + '_rev' )


	# Connection fk/ik Stick controller switch to placement
	# connect attr to ik
	mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , revNode + '.inputX'  )
	mc.connectAttr( '%s.%s' %( placementCtrl, 'FK_IK' ) , psCon[0] + '.' + rawName[4] + side + '_ikJnt' + 'W1' )

	# connect attr to fk
	mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.' + rawName[4] + side +'_fkJnt' + 'W0'  )


	if productionType == 'game':
		toe_bJnt.deleteName()



	print ''' \n
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create Null Snap group for matcher
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	'''
	part = nameSpace + region
	offset_null = core.Null( part + 'Offset' + side + '_null')

	if ikPosi == 'ankle':
		offset_null.maSnap( ankle_bJnt , position = True , rotation = True , scale = True )
		offset_parCons = core.parentConstraint( ankle_bJnt , offset_null , mo = True)
	elif ikPosi == 'foot' or ikPosi == 'animalFoot':# for animal case
		offset_null.maSnap( ankle_bJnt , position = True , rotation = False , scale = True )
		offset_parCons = core.parentConstraint( ankle_bJnt , offset_null , mo = True)
	


	try:
		offset_parCons.name = part + 'Offset' + side + '_parCons'
		offset_null.parent( nullGrp )

		stick_ctrl = core.Dag( stickNam )
		offset_null.attr('message') >> stick_ctrl.attr('offset')
	except Exception as e:
		raise e












	if footAttr:
		print '# Create foot roll attr'
		ankleIk_ctrl.addAttribute( longName = 'footBar', niceName = '_' , at ='enum' , en = 'Foot'  , keyable = True)
		ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'heelRoll' 	, k = True  ,dv = 0 )
		ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'ballRoll' 	, k = True  ,dv = 0 )
		ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'toeRoll' 	, k = True  ,dv = 0 )
		ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'heelTwist' 	, k = True  ,dv = 0 )
		ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'toeTwist' 	, k = True  ,dv = 0 )
		ankleIk_ctrl.addAttribute(  attributeType = 'float' ,ln = 'footRock' 	, k = True  ,dv = 0 )

		print '# Connect foot attr'
		ankleIk_ctrl.attr( 'heelRoll' ) >> footHeel_ctrl.attr( 'rx' )
		ankleIk_ctrl.attr( 'heelTwist' ) >> footHeel_ctrl.attr( 'rz' )
		ankleIk_ctrl.attr( 'ballRoll' ) >> ballRoll_ctrl.attr( 'rx' )
		ankleIk_ctrl.attr( 'toeRoll' ) >> footToe_ctrl.attr( 'rx' )
		ankleIk_ctrl.attr( 'toeTwist' ) >> footToe_ctrl.attr( 'rz' )

		print '# Connect'
		# footBehav = ['footOut','footIn','heelRoll','toeRoll','ballRoll','ankle']	

		pos_cnd = core.Condition('{0}{1}PosVal{2}_cnd'.format(rawName[3],footBehav[0],side))
		# pos_cnd = core.Condition(rawName[3] + footBehav[0]+'PosVal{0}_cnd'.format(side))
		neg_cnd = core.Condition('{0}{1}NegVal{2}_cnd'.format(rawName[3],footBehav[0],side))
		# neg_cnd = core.Condition(rawName[3] + footBehav[1]+'NegVal{0}_cnd'.format(side))
		minus_mdl = core.MultiDoubleLinear(rawName[3] + footBehav[1] + 'MinusVal')

		#... set if false to zero
		pos_cnd.attr('colorIfFalseR').value = 0
		neg_cnd.attr('colorIfFalseR').value = 0


		# footout case
		ankleIk_ctrl.attr( 'footRock' ) >> pos_cnd.attr( 'colorIfTrueR' )
		ankleIk_ctrl.attr( 'footRock' ) >> pos_cnd.attr( 'firstTerm' )
		# 3 == 'Equal and grater'
		pos_cnd.attr('operation').value = 3
		pos_cnd.attr( 'outColorR' ) >> footOut_ctrl.attr( 'rotateX' )



		# footin case
		ankleIk_ctrl.attr( 'footRock' ) >> neg_cnd.attr( 'colorIfTrueR' )
		ankleIk_ctrl.attr( 'footRock' ) >> neg_cnd.attr( 'firstTerm' )
		neg_cnd.attr('operation').value = 5
		minus_mdl.attr('input2').value = -1
		neg_cnd.attr( 'outColorR' ) >> minus_mdl.attr( 'input1' )
		minus_mdl.attr( 'output' ) >> footIn_ctrl.attr( 'rotateX' )


		# lock and hide vis
		footOutZro_grp.attr('visibility').value = 0
		footOutZro_grp.lockHideAttrLst( 'v' )

	else:
		print 'Skip add attribute.'




	print '\n\n\n\n\n\n # # # # End of %s %s Rig # # # #' %( region , side )


