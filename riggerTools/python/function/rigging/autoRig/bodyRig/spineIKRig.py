# -*- coding: utf-8 -*-
"""
This module is create spine IK hybride with FK  
source : nomanTools/21.03.Mar.29.Mon_ikSpinePart2
Issue: bind joint rotation not zero out
"""


'''

from function.rigging.autoRig.bodyRig import spineIKRig
reload(spineIKRig)

'''
from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )


from function.pipeline import logger 
reload(logger)

class spineHybridLog(logger.MayaLogger):
	LOGGER_NAME = "SpineRig"

def spineHybridIK(
				nameSpace = '' 		,
				parentTo = 'ctrl_grp' 						,		
				tmpJnt = (		'spine01_tmpJnt' 			,
								'spine02_tmpJnt' 			,
								'spine03_tmpJnt' 			,
								'spine04_tmpJnt'			),
				priorCtrl = 'cog_gmbCtrl'					,
				priorJnt = 'hip_bJnt'						,				
				charScale = 1.0								,							
				linkRotOrder = True							,
				rotateOrder = 'yzx'								):




	core.makeHeader('Create spineHybridIK Rig')

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

	# freeze
	spine1_bJnt.freeze()
	spine2_bJnt.freeze()
	spine3_bJnt.freeze()
	spine4_bJnt.freeze()


	# joint label
	spine1_bJnt.setLable('CEN','spine')
	spine2_bJnt.setLable('CEN','spine')
	spine3_bJnt.setLable('CEN','spine')
	spine4_bJnt.setLable('CEN','spine')




	# set segmentScaleCompensate for make it scaleable in ikSpine fashion
	# spine1_bJnt.attr('segmentScaleCompensate').value = 1
	# spine2_bJnt.attr('segmentScaleCompensate').value = 1
	# spine3_bJnt.attr('segmentScaleCompensate').value = 1
	# spine4_bJnt.attr('segmentScaleCompensate').value = 1





	# Template objects
	rootJnt = core.Dag( nameSpace + priorJnt )








	start_jnt = spine1_bJnt.name
	end_jnt = spine4_bJnt.name

	partName = 'spineIK'




	if nameSpace:
		partName = nameSpace + partName.capitalize()




	rotateOrder = rotateOrder


	# create spine ik
	oSpine_ik = core.DoIk(startJoint = start_jnt , endEffector = end_jnt ,solverType = 'ikSplineSolver'  , parentCurve = False)
	oSpine_ik.name = partName + '_ikh'
	oSpine_ik.crv = partName + '_crv'




	# create joint top 
	upr_pxyJnt = core.Joint(partName + 'Upr' +'_pxyJnt')
	upr_pxyJnt.setLable('CEN','none')
	upr_pxyJnt.setJointColor('white')
	upr_pxyJnt.attr('radius').value = 3
	# Set Sacle seqment compensate
	upr_pxyJnt.attr('segmentScaleCompensate').value = 0
	# rotateOrder = 'yzx'
	upr_pxyJnt.attr('rotateOrder').value = 1 



	# create joint  bottom
	lwr_pxyJnt = core.Joint(partName + 'Lwr' +'_pxyJnt')
	lwr_pxyJnt.setLable('CEN','none')
	lwr_pxyJnt.setJointColor('white')
	lwr_pxyJnt.attr('radius').value = 3
	# set rotate order
	lwr_pxyJnt.attr('rotateOrder').value = 1 
	lwr_pxyJnt.attr('segmentScaleCompensate').value = 0



	# snap position
	upr_pxyJnt.snapPoint(spine4_bJnt)
	lwr_pxyJnt.snapPoint(spine1_bJnt)




	# skin it with spine IK curve
	core.SkinCluster( upr_pxyJnt.name , lwr_pxyJnt.name , oSpine_ik.crv , maximumInfluences = 2 , name = partName + '_skc')



	# create controller for both






	# Upr
	spineUpr_ctrl = core.Dag( partName + 'Upr' + '_ctrl' )
	spineUpr_ctrl.nmCreateController('cube_ctrlShape')
	spineUpr_ctrl.editCtrlShape( axis = charScale * 4.0 )
	# Create ctrl group
	spineUprZro_grp = rigTools.zeroGroup( spineUpr_ctrl )
	spineUprZro_grp.name = partName + 'Upr' + 'Zro_grp'
	spineUpr_ctrl.color = 'softBlue'
	spineUpr_ctrl.rotateOrder = rotateOrder
	spineUprGmbl_ctrl = core.createGimbal( spineUpr_ctrl )
	spineUprZro_grp.matchPosition( upr_pxyJnt )
	# Constraint
	spineUpr_parCons = core.parentConstraint( spineUprGmbl_ctrl , upr_pxyJnt )
	spineUpr_parCons.name = partName + 'Jnt_parCons'



	# Lower
	spineLwr_ctrl = core.Dag( partName + 'Lwr' + '_ctrl' )
	spineLwr_ctrl.nmCreateController('cube_ctrlShape')
	spineLwr_ctrl.editCtrlShape( axis = charScale * 3.5 )
	# Create ctrl group
	spineLwrZro_grp = rigTools.zeroGroup( spineLwr_ctrl )
	spineLwrZro_grp.name = partName + 'Lwr' + 'Zro_grp'
	spineLwr_ctrl.color = 'softBlue'
	spineLwr_ctrl.rotateOrder = rotateOrder
	spineLwrGmbl_ctrl = core.createGimbal( spineLwr_ctrl )
	spineLwrZro_grp.matchPosition( lwr_pxyJnt )
	# Constraint
	spineLwr_parCons = core.parentConstraint( spineLwrGmbl_ctrl , lwr_pxyJnt )
	spineLwr_parCons.name = partName + 'Jnt_parCons'






	# enable twist control
	ik_handle = core.Dag(oSpine_ik.name)
	ik_handle.attr('dTwistControlEnable').value = 1
	ik_handle.attr('dForwardAxis').value = 2
	ik_handle.attr('dWorldUpAxis').value = 4



	# create locator for direct up object
	upUpr_loc = core.Locator( partName + 'Upr' + '_loc' )
	upUpr_loc.snapPoint(spineUpr_ctrl)

	# find suit translate relating to mesh
	# upUpr_loc.moveObj([0,0,-2])
	upUpr_loc.moveObj([0, 0, 12.5*charScale])

	upUpr_loc.parent(spineUprGmbl_ctrl)
	upUpr_loc.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz','v')




	# create locator for direct up object
	upLwr_loc = core.Locator( partName + 'Lwr' + '_loc' )
	upLwr_loc.snapPoint(spineLwr_ctrl)

	# upLwr_loc.moveObj([0,0,-2])
	upLwr_loc.moveObj([0, 0, 12.5*charScale])
	
	upLwr_loc.parent(spineLwrGmbl_ctrl)
	upLwr_loc.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz','v')


	# set to world up type
	ik_handle.attr('dWorldUpType').value = 2


	# manual way
	# lower is start
	mc.connectAttr(upLwr_loc.name + '.worldMatrix[0]' , oSpine_ik.name + '.dWorldUpMatrix')
	# upper is end
	mc.connectAttr(upUpr_loc.name + '.worldMatrix[0]' , oSpine_ik.name + '.dWorldUpMatrixEnd')





	# make it object
	# ikh_crv = core.Dag(oSpine_ik.name)
	# link attr
	# upUpr_loc.attr('worldMatrix[0]') >> ikh_crv.attr('dWorldUpMatrixEnd')
	# upLwr_loc.attr('worldMatrix[0]') >> ikh_crv.attr('dWorldUpMatrix')




	# Create joint at each spine
	spine1_fkJnt = rigTools.jointAt( spine1 )
	spine2_fkJnt = rigTools.jointAt( spine2 )
	spine3_fkJnt = rigTools.jointAt( spine3 )
	spine4_fkJnt = rigTools.jointAt( spine4 )



	# Naming 
	spine1_fkJnt.name = nameSpace + 'spine' + '01' + '_fkJnt'
	spine2_fkJnt.name = nameSpace + 'spine' + '02' + '_fkJnt'
	spine3_fkJnt.name = nameSpace + 'spine' + '03' + '_fkJnt'
	spine4_fkJnt.name = nameSpace + 'spine' + '04' + '_fkJnt'



	spine1_fkJnt.rotateOrder = rotateOrder
	spine2_fkJnt.rotateOrder = rotateOrder
	spine3_fkJnt.rotateOrder = rotateOrder
	spine4_fkJnt.rotateOrder = rotateOrder




	# Parent each 
	spine4_fkJnt.parent( spine3_fkJnt )
	spine3_fkJnt.parent( spine2_fkJnt )
	spine2_fkJnt.parent( spine1_fkJnt )



	spine1_fkJnt.setJointColor('gray')
	spine1_fkJnt.attr('radius').value = 0.5
	spine2_fkJnt.attr('radius').value = 0.5
	spine3_fkJnt.attr('radius').value = 0.5
	spine4_fkJnt.attr('radius').value = 0.5




	# psCon from fk joint to ik Ctrl

	spineFkLwr_parCons = core.parentConstraint( spine1_fkJnt , spineLwrZro_grp )
	spineFkLwr_parCons.name = partName + 'FkLwr_parCons'

	spineFkUpr_parCons = core.parentConstraint( spine4_fkJnt , spineUprZro_grp )
	spineFkUpr_parCons.name = partName + 'FkUpr_parCons'



	# create FK joint to ctrl ik 

	# fk spine 02
	spineFk02_ctrl = core.Dag( partName + '02' + 'Fk' + '_ctrl' )
	spineFk02_ctrl.nmCreateController('circle_ctrlShape')
	spineFk02_ctrl.editCtrlShape( axis = charScale * 1.6 )
	# Create ctrl group
	spineFk02Zro_grp = rigTools.zeroGroup( spineFk02_ctrl )
	spineFk02Zro_grp.name = partName + '02' + 'Fk' + 'Zro_grp'
	spineFk02_ctrl.color = 'softBlue'
	spineFk02_ctrl.rotateOrder = rotateOrder
	spineFk02Gmbl_ctrl = core.createGimbal( spineFk02_ctrl )
	spineFk02Zro_grp.matchPosition( spine2_fkJnt )
	# Constraint
	spineUpr_parCons = core.parentConstraint( spineFk02Gmbl_ctrl , spine2_fkJnt ,mo = True)
	spineUpr_parCons.name = partName + 'Jnt_parCons'






	# fk spine 03
	spineFk03_ctrl = core.Dag( partName + '03' + 'Fk' + '_ctrl' )
	spineFk03_ctrl.nmCreateController('circle_ctrlShape')
	spineFk03_ctrl.editCtrlShape( axis = charScale * 1.65 )
	# Create ctrl group
	spineFk03Zro_grp = rigTools.zeroGroup( spineFk03_ctrl )
	spineFk03Zro_grp.name = partName + '03' + 'Fk' + 'Zro_grp'
	spineFk03_ctrl.color = 'softBlue'
	spineFk03_ctrl.rotateOrder = rotateOrder
	spineFk03Gmbl_ctrl = core.createGimbal( spineFk03_ctrl )
	spineFk03Zro_grp.matchPosition( spine3_fkJnt )
	# Constraint
	spineUpr_parCons = core.parentConstraint( spineFk03_ctrl , spine2_fkJnt ,mo=True)
	spineUpr_parCons.name = partName + 'Jnt_parCons'



	# parent fk spine02 to fk spine03
	spineFk03Zro_grp.parent(spineFk02Gmbl_ctrl)


	# get the name curveInfo
	curveInfo = core.CurveInfo( partName + 'CurveInfo')
	spine_crv = core.Dag(partName + '_crv')




	"""
	DISABLE FOR EVER
	"""

	"""




	# connect it
	mc.connectAttr(spine_crv.shape + '.worldSpace[0]' , curveInfo.name + '.inputCurve')
	# find default arc length 
	default_length = curveInfo.attr('arcLength').value 



	# make scale master_ctrl compensate first
	scaleCompensate = core.MultiplyDivide(partName + 'ScaleCompensate')


	# plugins length to the scaleCompensate
	curveInfo.attr('arcLength') >> scaleCompensate.attr('input1X')



	# set to operation to divide
	scaleCompensate.attr('operation').value  = 2

	# feed the scale of placement_ctrl
	placement_ctrl = core.Dag('placement_ctrl')
	placement_ctrl.attr('scaleX') >> scaleCompensate.attr('input2X')




	#create MDV
	stretch_mdv = core.MultiplyDivineWithVal(partName + 'Stretch' , 2)
	# connect crv length to mdv
	scaleCompensate.attr('outputX') >> stretch_mdv.attr('input1X')
	# insert default length of this curve
	stretch_mdv.attr('input2X').value = default_length







	# destibute this value to the joint
	stretch_mdv.attr('outputX') >> spine1_bJnt.attr('scaleY')
	stretch_mdv.attr('outputX') >> spine2_bJnt.attr('scaleY')
	stretch_mdv.attr('outputX') >> spine3_bJnt.attr('scaleY')
	stretch_mdv.attr('outputX') >> spine4_bJnt.attr('scaleY')


	"""





	# freeze
	spine1_bJnt.freeze()
	spine2_bJnt.freeze()
	spine3_bJnt.freeze()
	spine4_bJnt.freeze()





	# alternate way to make spine stretchables with translate y driven



	# multiplier
	divider = 3 


	# try to make for loop
	for num in range(1,4):

		spineHybridLog.info('#\n# Spine %02d\n#' %num)

		
		
		

		# create plus minus set op to divide
		spStretch_mdv = core.MultiplyDivineWithVal(partName + 'SpStretch%02d' %num, 2)
		# using "4" because number of spine joint
		spStretch_mdv.attr('input2X').value = divider
		# link ik upr ctrl
		spineUpr_ctrl.attr('translateY') >> spStretch_mdv.attr('input1X')
		# create add double linear
		spStretchDef_add = core.AddDoubleLinear(partName + 'SpStretchDef%02d' %num )
		# set last name
		spStretchDef_add.suffix

		# get the default value of translateY for each joint
		# spine3_bJnt.name
		# yeahyeah='spine'+'%d' %'2'+'_bJnt'



		defaultVal = mc.getAttr('spine%02d_bJnt' %num + '.translateY')
		# defaultVal = spine3_bJnt.attr('translateY').value
		# assign value
		spStretchDef_add.attr('input2').value = defaultVal

		# link attribute
		spStretch_mdv.attr('outputX') >> spStretchDef_add.attr('input1')
		mc.connectAttr(spStretchDef_add.name + '.output' , 'spine%02d_bJnt.translateY' %num)
		# spStretchDef_add.attr('output') >> spine3_bJnt.attr('translateY')






	# regroup

	spine1_bJnt.parent(priorJnt)

	spineIK_grp = core.Null(partName + 'Rig_grp')

	# parent local grp
	spineFk02Zro_grp.parent(spineIK_grp)
	spine1_fkJnt.parent(spineIK_grp)
	spineUprZro_grp.parent(spineIK_grp)
	spineLwrZro_grp.parent(spineIK_grp)




	mc.setAttr(spine_crv.name + '.' + 'inheritsTransform' , 0)
	spine_crv.parent(spineIK_grp)

	# Constraint to hip joint
	# hip_parCons = core.parentConstraint( priorJnt , spineIK_grp  ,mo=True)
	# hip_parCons.name = partName + '_parCons'
	# hip_scalCons = core.scaleConstraint( priorJnt, spineIK_grp   )
	# hip_scalCons.name = partName + '_scalCons'


	# Change the parent constraint want to make hip rotate freely from spine
	hip_parCons = core.parentConstraint( priorCtrl , spineIK_grp  ,mo=True)
	hip_parCons.name = partName + '_parCons'







	spineIK_grp.parent(parentTo)

	ik_handle.parent('ikh_grp')


	spineJnt_grp = core.Null(partName + 'Jnt_grp')
	upr_pxyJnt.parent(spineJnt_grp)
	lwr_pxyJnt.parent(spineJnt_grp)
	spineJnt_grp.parent('jnt_grp')

	# hide visibility
	spine1_fkJnt.attr('v').value = 0
	spine_crv.attr('v').value = 0
	spineJnt_grp.attr('v').value = 0
	ik_handle.attr('v').value = 0

	# the problem now bJnt got the eff in entire bJnt chain 





	# add link rotate order
	if linkRotOrder:
		
		spineLwr_ctrl.addRotEnum()
		spineLwrGmbl_ctrl.addRotEnum()
		spineUpr_ctrl.addRotEnum()
		spineUprGmbl_ctrl.addRotEnum()	

		spineFk02_ctrl.addRotEnum()
		spineFk02Gmbl_ctrl.addRotEnum()
		spineFk03_ctrl.addRotEnum()
		spineFk03Gmbl_ctrl.addRotEnum()







	# test dry return
	spineHybridLog.info('return: '+spine4_bJnt.name)
	return spine4_bJnt.name