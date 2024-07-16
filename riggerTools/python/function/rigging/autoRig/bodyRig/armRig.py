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

from function.rigging.autoRig.bodyRig import midLockModule
reload( midLockModule )

from function.rigging.autoRig.bodyRig import createIKStretch as create
reload( create )

from function.rigging.tools import proc as pc
reload(pc)

from function.rigging.autoRig.bodyRig import fkIkGenRig
reload( fkIkGenRig )

# from function.rigging.autoRig.bodyRig import fkIkTwistGenRig
# reload( fkIkTwistGenRig )

from function.rigging.autoRig.bodyRig import fkIkTwistGenRig as fitr
reload( fitr )

from function.rigging.autoRig.bodyRig import createSoftIk as softIkfunc
reload( softIkfunc )

#... diagram
# [armRigExt] >>> [fkIkTwistGenRig] >>> [iKStretch]
import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


# armRig original has been deleted please use below function
# new arm rig function that passing arg to fkikRig
def armRigExt(	
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
			linkRotOrder = False			,
			ctrlShape = 'fk_ctrlShape'		,
			creTwistJnt = True 				,
			softIk = True					,
			softIkPrimaryAxis = 2					,
			softIkUpAxis = 2				,
			alongAxis = 'y',			
			stickShape = 'stick_ctrlShape',
			):

	core.makeHeader(	'Start of %s%s Rig' %(region,side)	)



	


	if creTwistJnt == True:
		# using non twisting upper joint
		# passing arg to fkIkGenRig
		stickNam, hand_bJnt , middle_bJnt , upper_bJnt , ikhAll_name , psStreEndName, softIk_name, priorMeta   = fitr.fkIkTwistGenRig(
					nameSpace = nameSpace 	,				
					charScale = charScale	,			
					parentTo = parentTo 	,			
					side = side				,
					region = region			,							
					tmpJnt = tmpJnt			,
					priorJnt = priorJnt		,	
					ikhGrp = ikhGrp				,			
					noTouchGrp = noTouchGrp 	,			
					nullGrp = nullGrp			,			
					jnt_grp =  jnt_grp			,			
					povShape = povShape			,
					keepFkIkBoth = keepFkIkBoth		,
					ribbon = ribbon					,
					ribbonRes = ribbonRes			,
					ribbonName = ribbonName			,
					showInfo = showInfo				,
					linkRotOrder = linkRotOrder 	,
					ctrlShape = ctrlShape			,
					creTwistJnt = creTwistJnt		,
					alongAxis = alongAxis,	
					stickShape = stickShape				)

		

		

		print (''' \n
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# Create Null Snap group for matcher
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		''')
		part = nameSpace + region
		offset_null = core.Null( part + 'Offset' + side + '_null')
		offset_null.maSnap( hand_bJnt , position = True , rotation = True , scale = True )
		offset_parCons = core.parentConstraint( hand_bJnt , offset_null , mo = True)
		offset_parCons.name = part + 'Offset' + side + '_parCons'
		offset_null.parent( nullGrp )

		stick_ctrl = core.Dag( stickNam )
		offset_null.attr('message') >> stick_ctrl.attr('offset')
		
		stick_ctrl.lockHideAttrLst('location')
		print ('Lock Message attr')



		if softIk == True:

			softIkfunc.softIK(	priorMeta = priorMeta ,region = region, side = side, ctrlName = softIk_name[0],
						upAxis = softIkUpAxis, primaryAxis = softIkPrimaryAxis, ikhName = ikhAll_name[0], 
						inputMax = 40, outputMax = 4  )

			print ('#### End of %s%s Rig ####' %( 'bipedLegRig' , side ))
			print ('\n\n\n\n\n')




		print('#### End of %s%s Rig ####' %( region , side ))
		print ('\n\n\n\n\n')

		return stickNam, hand_bJnt, priorMeta








	elif creTwistJnt == False:

		# using normally twisting 
		# passing arg to fkIkGenRig
		stickNam, hand_bJnt , middle_bJnt , upper_bJnt , ikhAll_name , psStreEndName   = fkIkGenRig.fkIkGenRig(
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
					jnt_grp =  jnt_grp			,	
					showInfo = showInfo				,
					ribbon = ribbon			,
					ribbonRes = ribbonRes			,
					ribbonName = ribbonName			,			
					propCtrl = propCtrl				,
					keepFkIkBoth = keepFkIkBoth		,
					povShape = povShape				,
					ikPosi = None 					,
					ctrlShape = ctrlShape			,
					linkRotOrder = linkRotOrder 	,
					stickShape = stickShape		)

		

		

		print (''' \n
				# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
				# Create Null Snap group for matcher
				# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
				''')
		part = nameSpace + region
		offset_null = core.Null( part + 'Offset' + side + '_null')
		offset_null.maSnap( hand_bJnt , position = True , rotation = True , scale = True )
		offset_parCons = core.parentConstraint( hand_bJnt , offset_null , mo = True)
		offset_parCons.name = part + 'Offset' + side + '_parCons'
		offset_null.parent( nullGrp )

		stick_ctrl = core.Dag( stickNam )
		offset_null.attr('message') >> stick_ctrl.attr('offset')
		
		stick_ctrl.lockHideAttrLst('location')
		print ('Lock Message attr')

		print('#### End of %s%s Rig ####' %( region , side ))
		print ('\n\n\n\n\n')
		
		return stickNam, hand_bJnt


