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

from function.rigging.autoRig.bodyRig import fkIkTwsitGenRig
reload( fkIkTwsitGenRig )

from function.rigging.util import misc as misc
reload(misc)

# Arm rig with twist upper arm function

# armRig original has been deleted please use below function
# new arm rig function that passing arg to fkikRig
def armRigTws(	
			nameSpace = '' 		,
			charScale = ''						,
			parentTo = 'ctrl_grp' 				,
			side = 'LFT'						,
			region = 'arm'						,
			tmpJnt = (	'upperArmLFT_tmpJnt'	,
						'lowerArmLFT_tmpJnt'	,
						'handLFT_tmpJnt'		,
						'armLFT_pov_tmpJnt')	,
			priorJnt = 'clavLFT_bJnt'			,
			ikhGrp = 'ikh_grp'					,
			noTouchGrp = 'noTouch_grp' 			,
			nullGrp = 'snapNull_grp'			,
			jnt_grp =  'jnt_grp'				,
			showInfo = False 					,
			ribbon = False 						,
			ribbonRes = 'high'					,
			ribbonName = ('upLeg', 'lwrLeg'),
			propCtrl = False 					,
			keepFkIkBoth = True	,# keep fk/ik ctrl visibility both or not
			povShape = 'pyramid', # choice pyramid or sphereAxis
			linkRotOrder = False,
			creTwistJnt = False ):

	misc.makeHeader(	'Start of %s%s Rig' %(region,side)	)
	print creTwistJnt


	



	# passing arg to fkIkGenRig
	stickNam, hand_bJnt , middle_bJnt , upper_bJnt , ikhAll_name , psStreEndName   = fkIkTwsitGenRig.fkIkTwsitGenRig(
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
				showInfo = showInfo,
				linkRotOrder = linkRotOrder 	,
				creTwistJnt = creTwistJnt			)

	

	

	print ''' \n
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# Create Null Snap group for matcher
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	'''
	part = nameSpace + region
	offset_null = core.Null( part + 'Offset' + side + '_null')
	offset_null.maSnap( hand_bJnt , position = True , rotation = True , scale = True )
	offset_parCons = core.parentConstraint( hand_bJnt , offset_null , mo = True)
	offset_parCons.name = part + 'Offset' + side + '_parCons'
	offset_null.parent( nullGrp )

	stick_ctrl = core.Dag( stickNam )
	offset_null.attr('message') >> stick_ctrl.attr('offset')
	
	stick_ctrl.lockHideAttrLst('location')
	print 'Lock Message attr'

	return stickNam, hand_bJnt

