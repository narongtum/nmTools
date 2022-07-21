#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Spine rig module
# 03_hipRig


import maya.cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)

# direct run
'''from function.rigging.autoRig import spineFkRig
reload(spineFkRig)'''



# D:\True_Axion\Tools\riggerTools\python\axionTools\rigging\autoRig\base\version

def spineRig( 		nameSpace = '' ,
					parentTo = 'ctrl_grp' 						,
					tmpJnt = (		'spine01_tmpJnt' 			,
									'spine02_tmpJnt' 			,
									'spine03_tmpJnt' 			,
									'spine04_tmpJnt'			),
					priorCtrl = 'cog_gmbCtrl'			,
					priorJnt = ''						,
					charScale = ''						,
					ctrShape = ''						,
					linkRotOrder = False							):


	core.makeHeader('Start of spine FK Rig')

	
	
	# nameSpace = charName + elem
	# priorCtrl = '%s%s' %(nameSpace,priorCtrl)
	# parentTo = '%s%s' %(nameSpace,parentTo)
	# charScale = mc.getAttr( 'template_ctrl.scaleX' )
	partName = 'spine'
	
	if nameSpace:
		partName = partName.capitalize()

	spine1 = core.Dag( tmpJnt[ 0 ] )
	spine2 = core.Dag( tmpJnt[ 1 ] )
	spine3 = core.Dag( tmpJnt[ 2 ] )
	spine4 = core.Dag( tmpJnt[ 3 ] )

	# Create joint at each spine
	spine1_bJnt = rigTools.jointAt( spine1 )
	spine2_bJnt = rigTools.jointAt( spine2 )
	spine3_bJnt = rigTools.jointAt( spine3 )
	spine4_bJnt = rigTools.jointAt( spine4 )

	# Parent each 
	spine4_bJnt.parent( spine3_bJnt )
	spine3_bJnt.parent( spine2_bJnt )
	spine2_bJnt.parent( spine1_bJnt )

	

	# Naming 
	spine1_bJnt.name = nameSpace + 'spine' + '01' + '_bJnt'
	spine2_bJnt.name = nameSpace + 'spine' + '02' + '_bJnt'
	spine3_bJnt.name = nameSpace + 'spine' + '03' + '_bJnt'
	spine4_bJnt.name = nameSpace + 'spine' + '04' + '_bJnt'


	# joint label
	spine1_bJnt.setLable('CEN','spine')
	spine2_bJnt.setLable('CEN','spine')
	spine3_bJnt.setLable('CEN','spine')
	spine4_bJnt.setLable('CEN','spine')

	# Template objects
	# rootJnt = priorJnt
	rootJnt = core.Dag( nameSpace + 'hip_bJnt' )

	# Parent to Prior joint
	spine1_bJnt.parent( rootJnt )

	# Create Controller group
	part = nameSpace + 'spineRip'
	spineRig_grp = core.Null()
	spineRig_grp.rename( part + '_' + 'grp')
	# Prosition
	spineRig_grp.matchPosition (spine1_bJnt)
	spineRig_grp.matchRotation (spine1_bJnt)

	# Create spine1
	part = nameSpace + 'spine01'
	spine1_ctrl = core.Dag( part + '_ctrl' )


	if ctrShape:
		spineShape = ctrShape
	else:
		spineShape = 'chest_ctrlShape'

	spine1_ctrl.nmCreateController( spineShape )

	spine1Zro_grp = rigTools.zeroGroup( spine1_ctrl )
	spine1Zro_grp.name = part + 'Zro_grp'
	spine1_ctrl.editCtrlShape( axis = charScale * 0.6 )
	spine1Gmbl_ctrl = core.createGimbal( spine1_ctrl )
	spine1_ctrl.color = 'yellow'
	spine1_ctrl.rotateOrder = 'xzy'
	spine1Gmbl_ctrl.rotateOrder = 'xzy'

	# Parenting and positioning
	spine1Zro_grp.matchPosition( spine1_bJnt )
	spine1Zro_grp.matchRotation( spine1_bJnt )
	spine1_ctrl.matchRotation( spine1_bJnt )

	# Constraint joint parent of controller
	spine1Jnt_parCons = core.parentConstraint( spine1Gmbl_ctrl , spine1_bJnt )
	spine1Jnt_parCons.name = part + 'Jnt_parCons'

	spine1Jnt_scaleCons = core.scaleConstraint( spine1Gmbl_ctrl , spine1_bJnt )
	spine1Jnt_scaleCons.name = part + 'Jnt_scaleCons'




	# Create spine2
	part = nameSpace +'spine02'
	spine2_ctrl = core.Dag( part + '_ctrl' )
	spine2_ctrl.nmCreateController( spineShape )
	spine2Zro_grp = rigTools.zeroGroup( spine2_ctrl )
	spine2Zro_grp.name = part + 'Zro_grp'
	spine2_ctrl.editCtrlShape( axis = charScale * 0.6 )
	spine2Gmbl_ctrl = core.createGimbal( spine2_ctrl )
	spine2_ctrl.color = 'yellow'
	spine2_ctrl.rotateOrder = 'xzy'
	spine2Gmbl_ctrl.rotateOrder = 'xzy'
	# Parenting and positioning
	spine2Zro_grp.matchPosition( spine2_bJnt )
	spine2Zro_grp.matchRotation( spine2_bJnt )
	spine2_ctrl.matchRotation( spine2_bJnt )

	# Constraint joint parent of controller
	spine2Jnt_parCons = core.parentConstraint( spine2Gmbl_ctrl , spine2_bJnt )
	spine2Jnt_parCons.name = part + 'Jnt_parCons'

	spine2Jnt_scaleCons = core.scaleConstraint( spine2Gmbl_ctrl , spine2_bJnt )
	spine2Jnt_scaleCons.name = part + 'Jnt_scaleCons'	

	# Create spine3
	part = nameSpace +'spine03'
	spine3_ctrl = core.Dag( part + '_ctrl' )
	spine3_ctrl.nmCreateController( spineShape )
	spine3Zro_grp = rigTools.zeroGroup( spine3_ctrl )
	spine3Zro_grp.name = part + 'Zro_grp'
	spine3_ctrl.editCtrlShape( axis = charScale * 0.6 )
	spine3Gmbl_ctrl = core.createGimbal( spine3_ctrl )
	spine3_ctrl.color = 'yellow'
	spine3_ctrl.rotateOrder = 'xzy'
	spine3Gmbl_ctrl.rotateOrder = 'xzy'

	# Parenting and positioning
	spine3Zro_grp.matchPosition( spine3_bJnt )
	spine3Zro_grp.matchRotation( spine3_bJnt )
	spine3_ctrl.matchRotation( spine3_bJnt )
	# Constraint joint parent of controller
	spine3Jnt_parCons = core.parentConstraint( spine3Gmbl_ctrl , spine3_bJnt )
	spine3Jnt_parCons.name = part + 'Jnt_parCons'

	spine3Jnt_scaleCons = core.scaleConstraint( spine3Gmbl_ctrl , spine3_bJnt )
	spine3Jnt_scaleCons.name = part + 'Jnt_scaleCons'

	# Create spine4
	part = nameSpace +'spine04'
	spine4_ctrl = core.Dag( part + '_ctrl' )
	spine4_ctrl.nmCreateController( spineShape )
	spine4Zro_grp = rigTools.zeroGroup( spine4_ctrl )
	spine4Zro_grp.name = part + 'Zro_grp'
	spine4_ctrl.editCtrlShape( axis = charScale * 0.75 )
	spine4Gmbl_ctrl = core.createGimbal( spine4_ctrl )
	spine4_ctrl.color = 'yellow'
	spine4_ctrl.rotateOrder = 'xzy'
	spine4Gmbl_ctrl.rotateOrder = 'xzy'

	# Parenting and positioning
	spine4Zro_grp.matchPosition( spine4_bJnt )
	spine4Zro_grp.matchRotation( spine4_bJnt )
	spine4_ctrl.matchRotation( spine4_bJnt )
	# Constraint joint parent of controller
	spine4Jnt_parCons = core.parentConstraint( spine4Gmbl_ctrl , spine4_bJnt )
	spine4Jnt_parCons.name = part + 'Jnt_parCons'

	spine4Jnt_scaleCons = core.scaleConstraint( spine4Gmbl_ctrl , spine4_bJnt )
	spine4Jnt_scaleCons.name = part + 'Jnt_scaleCons'

	# Parenting Group
	spine1Zro_grp.parent( spineRig_grp )
	spine2Zro_grp.parent( spine1Gmbl_ctrl )
	spine3Zro_grp.parent( spine2Gmbl_ctrl )
	spine4Zro_grp.parent( spine3Gmbl_ctrl )


	if linkRotOrder:
		# link rotate order
		spine1_ctrl.addRotEnum()
		spine1Gmbl_ctrl.addRotEnum()
		spine2_ctrl.addRotEnum()
		spine2Gmbl_ctrl.addRotEnum()		
		spine3_ctrl.addRotEnum()
		spine3Gmbl_ctrl.addRotEnum()
		spine4_ctrl.addRotEnum()
		spine4Gmbl_ctrl.addRotEnum()

	# Define object
	rootGrp = core.Dag( parentTo )
	spineRig_grp.parent(rootGrp)


	# Parent Ctrl spine Grp to Hip Ctrl grp
	priorCtrl_parCons = core.parentConstraint( priorCtrl , spineRig_grp , mo = True)
	priorCtrl_parCons.name = nameSpace + 'spineRig' + '_parCons'
	print ('\n#### End of %s Rig ####' %(part))
	
	return spine4_bJnt.name






# Use any number of FK Chain rig
# this is outdate
# move to add rig folder
def spineFkChainRig(	nameSpace = ''  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'ear01LFT_tmpJnt','ear02LFT_tmpJnt'  ,'ear03LFT_tmpJnt')	,
					charScale = ''	, priorJnt = 'head01_bJnt' 			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = False	):

	

	part = name + side
	# Create main group
	rigGrp = core.Null()
	rigGrp.name = '%sFkRig%s_grp' % ( name , side )

	# Creatre empyt for append name
	ctrls = []
	jnts = []
	gmbls = []
	zGrps = []
	bJnts = []
	ofGrps = []

	# For loop in tmpJnt 
	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		# print  num 
		ctrl = core.Dag(     '%s%s%02dFk%s_ctrl'  %(nameSpace , name,( num +1),side)     )
		ctrl.nmCreateController( ctrlShape )
		logger.info(charScale)
		ctrl.editCtrlShape( axis = charScale * 6.4 )
		ctrl.color = color
		
		gimbal = core.createGimbal( ctrl )
		tmp = core.Dag( tmpJnt[  num  ] )
		bJnt = rigTools.jointAt( tmp )
		bJnt.name =  '%s%s%02dFk%s_bJnt'  %(nameSpace,	name,( num +1),side	)
		zroGrp,offsetGrp =  rigTools.zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%s%02dFk%sZro_grp'  %(nameSpace,	name,( num +1),side	)
		offsetGrp.name = '%s%s%02dFk%sOffset_grp'  %(nameSpace,	name,( num +1),side	)

		
		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		bJnts.append( bJnt )
		ofGrps.append( offsetGrp )
		
		if not  num  == 0:
			zroGrp.parent( gmbls[ num -1] )
			bJnt.parent( bJnts[ num -1] )
		else:
			rigGrp.maSnap(bJnts[0])
			zroGrp.parent( rigGrp )


	if priorJnt :
		rigGrp.parent( parentTo )
		bJnts[0].parent( priorJnt )

	# shift to here because joint will move if constraint and parent it later
	for  i  in range( 0 , ( len( tmpJnt )  ) ):
		# parent joint to controller
		parCons = core.parentConstraint( gmbls[i] , bJnts[i] , mo = True)
		parCons.name = '%s%s%02dFk%s_psCons'  %(nameSpace,	name,(i +1),side	)



	# create local / world follwer arg #
	if localWorld:
		Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( ctrls[0] , rigGrp.name , parentTo , zGrps[0] )
		Loc_grp.name = part + 'Local_grp'
		World_grp.name = part + 'World_grp'
		WorldGrp_orientCons.name = part + 'WorldGrp_orientCons'
		ZroGrp_orientCons.name = part + 'ZroGrp_orientCons'
		reverseNode_rev.name = part + 'ZroGrpOrientCons_rev'

	# Make curl controller 
	if curlCtrl:
		curl_ctrl = core.Dag('%s%s%s%s_ctrl'  %(nameSpace, name,'Curl',side))
		curl_ctrl.nmCreateController( ctrlShape )
		curl_ctrl.editCtrlShape( axis = charScale * 7.4 )
		curl_ctrl.color = 'white'
		zroGrpCurl = rigTools.zeroGroupNam(curl_ctrl)
		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )
		curl_parCons = core.parentConstraint( bJnts[0],zroGrpCurl ,mo = False)
		# zroGrpCurl.maSnap(bJnts[0])
		curl_parCons.name = '%s%s%sFk%s_psCons'  %(nameSpace,	name,'Curl',side	)

		for eachObj in ofGrps:
			logger.info(type( eachObj ))
			curl_ctrl.attr('rotate') >> eachObj.attr( 'rotate' )

		zroGrpCurl.parent( rigGrp )
		if priorJnt :
			mc.parentConstraint( priorJnt , rigGrp , name = '%sFkRig%s_psCons' % ( name,side )  ,mo = True )
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sFkRig%s_scaleCons' % ( name,side ) ,mo = True)


	# If having priorJnt but disable curl then just pa
	if priorJnt :
		if curlCtrl == False:
			mc.parentConstraint( priorJnt , rigGrp , name = '%sFkRig%s_psCons' % ( name,side )   ,mo = True)
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sFkRig%s_scaleCons' % ( name,side )   ,mo = True)

	print ('#### End of Spine FK Rig ####')
	print('\n\n\n\n\n')
	return bJnt.name