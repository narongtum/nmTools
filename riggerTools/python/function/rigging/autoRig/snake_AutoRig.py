
#... Fk first and then Ik and then Deformer
#... IK spine Rig for tentacle make deformer before Ik spine
#... make stretchy by using arcLength
#... increade detail joint to 24
#... make sin wave for tail
#... TODO collect ikh name to stick

import maya.cmds as mc
import maya.api.OpenMaya as om
import pymel.core as pm
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

from function.rigging.de_boor import hh_de_boor_to_curve as hh
reload(hh)

from function.rigging.constraint import pinLocatorToSurface as pls
reload(pls)

from function.rigging.de_boor import hh_de_boor_to_mesh as hm
reload(hm)

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

import logging
from function.pipeline import logger 
reload(logger)

class TentacleRig(logger.MayaLogger):
	LOGGER_NAME = "TentacleRig"

TentacleRig.set_level(logging.DEBUG)


SIDE = ''
BASE_NAME = 'spineBCK'
SCALE = 20
COUNT_DETAIL = 24
COUNT_MAIN = 6
stickShape = 'stickCircle_Y_long_ctrlShape'
mesh = 'snake_ply'
smoothCrv = False
smoothweight = False
sineDef = False
squashDef = False
priorJnt = 'hip_bJnt'
parentTo = 'hip_gmbCtrl'
place_ctrl ='placement_ctrl'
enableTwist = True			
worldUpType = 4
forwardAxis = 'y+'
worldUpAxis = 'z+'
worldUpVector = (0, 0, 1)
worldUpVectorEnd = (0, 0, 1)
upObject ='upFRTObj_crv'
upObjectEnd ='upBCKObj_crv'
		
#... Create Null grp
if mc.objExists(priorJnt):
	pass
else:
	core.Joint('root')





if SIDE == '':
	COMP_BASE_NAME = BASE_NAME
else:
	COMP_BASE_NAME = f'{SIDE}_{BASE_NAME}'



#... Create Null grp
nurbAll_grp = core.Null(f'{COMP_BASE_NAME}AllNurbe_grp')
nurbAll_grp.lockAllAttr(attrs=['t', 'r', 's'])


ik_detail_joints = core.generate_named_pattern(f'{COMP_BASE_NAME}##_ikJnt', COUNT_DETAIL)
spine_crv = f'{COMP_BASE_NAME}_ikSpine_crv'
ik_nrb = f'{COMP_BASE_NAME}_ik_nrb'
ik_nrb_shape = mc.listRelatives(ik_nrb, shapes=True)[0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Make FK controller
core.makeHeader('Make FK controller')


ik_joints = core.generate_named_pattern(f'{COMP_BASE_NAME}##_masterIk_ikJnt', COUNT_DETAIL)
bJnts_list = []

for num in range(0, COUNT_MAIN):
	print(num)
	print(ik_joints[num])
	ik_jnt = core.Dag(ik_joints[num])
	fk_jnt = core.Joint(ik_joints[num].replace('masterIk_ikJnt', 'masterFk_fkJnt'))
	fk_jnt.maSnap(ik_jnt)
	fk_jnt.attr('radius').value = 2
	fk_jnt.setJointColor('gray')
	bJnts_list.append(fk_jnt.name)

#... parent to hirachey
for num in range(0, COUNT_MAIN):
	print(num)
	if num !=0:
		mc.parent(bJnts_list[num], bJnts_list[num-1])



fk_rig = createFkRig.fkRig_omni_newCurl( nameSpace = '', parentCtrlTo = '',
					jntLst = bJnts_list,
					charScale = 1*SCALE, priorJnt = '',side = SIDE,
					ctrlShape = 'ring_ctrlShape', localWorld = False ,
					color = 'yellow', curlCtrl = True, curlPosiAtFirst = False, rotateOrder = 'zxy',
					parentToPriorJnt = False, parentMatrix = False,
					curlCtrlShape = stickShape)


TentacleRig.debug(f'{fk_rig[5]}')

# mc.error('BREAK')





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ..................  create IK spine controller




joints = core.generate_named_pattern(f'{COMP_BASE_NAME}##_masterIk_ikJnt', COUNT_MAIN)




main_ik_ctrl = adjust.creControllerFunc( 		selected = joints, scale = 5*SCALE, ctrlShape = 'cube_ctrlShape', color = 'yellow',
							constraint = True, matrixConst = False, mo = False, translate=True,
							rotate = True, scaleConstraint = True, rotateOrder = 'xzy', parentUnder = False)



master_ik_zroGrp = core.generate_named_pattern(f'{COMP_BASE_NAME}##_masterIkZro_grp', COUNT_MAIN)
master_fk_gmbl = core.generate_named_pattern(f'{COMP_BASE_NAME}##_masterFk_gmbCtrl', COUNT_MAIN)
for index, each in enumerate (master_fk_gmbl):
	mc.parent(master_ik_zroGrp[index], each)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. create Ik handle
ik_detail_jnt = core.generate_named_pattern(f'{COMP_BASE_NAME}##_ikJnt', COUNT_DETAIL)


ikHandle = core.DoIkSpline( 	startJoint = ik_detail_jnt[0] , 
						endEffector = ik_detail_jnt[-1] ,  
						solverType = 'ikSplineSolver' ,
						createCurve = False,
						curveName = spine_crv, 
						parentCurve = False)


ikHandle.name = f'{COMP_BASE_NAME}_ikh'
ikHandle.eff = f'{COMP_BASE_NAME}_eff'







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. skinweight joint to curve
TentacleRig.info('\n#.................................... skinweight joint to curve')



skin_name = f'{COMP_BASE_NAME}_ikCrv_skc'
skin_cluster = mc.skinCluster(joints, spine_crv, toSelectedBones=True, name = skin_name)[0]

if smoothCrv:
	#... smooth weight ( not work too soft)
	jnts = hh.list_joints_from_skincluster(skin_name)
	hh.split_curve_cvs_with_de_boor_v4(jnts, spine_crv, degree=3, falloff_mode='linear', falloff_width=0.01)




TentacleRig.info('#.................................... skinweight joint to ik_nrb curve for make match blendshape')

# PATTERN = '{COMP_BASE_NAME}{index}_ikJnt'
# count = 9
# joints = [PATTERN.format(SIDE=SIDE,BASE_NAME=BASE_NAME, index=str(i).zfill(2)) for i in range(1, COUNT_DETAIL + 1)]

joints = core.generate_named_pattern(f'{COMP_BASE_NAME}##_ikJnt', COUNT_DETAIL)






skin_name = f'{COMP_BASE_NAME}_ikNrb_skc'
skin_cluster = mc.skinCluster(joints, ik_nrb, toSelectedBones=True, name = skin_name)[0]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Blendshape ik nurbe to combin nurvbe
combineFkIk_nrb = mc.duplicate(ik_nrb,n = ik_nrb.replace('ik','combineFkIk'))[0]
mc.blendShape(ik_nrb, combineFkIk_nrb, frontOfChain = True, name = f'{COMP_BASE_NAME}_bsh', w=[(0, 1)] )












# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Create Detail Joint
core.makeHeader('Create Detail Joint')
ik_detail_jnt = core.generate_named_pattern(f'{COMP_BASE_NAME}##_ikJnt', COUNT_DETAIL)
locs = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_loc', COUNT_DETAIL)

for num in range(0,COUNT_DETAIL):
	print(locs[num])
	locator = core.Locator(locs[num])
	ik_jnt = core.Dag(ik_detail_jnt[num])
	locator.maSnap(ik_jnt)



tenTail_resultDef_nrb_grp = pls.pin_locator_surface(	
						nurbs = combineFkIk_nrb,
						region = f'{BASE_NAME}_combineFkik',
						side = SIDE,
						source_loc = locs,
						locator_scale = 1*SCALE,
						creJnt = True , suffixJnt = 'pxyJnt',
						creCtrl = True , ctrlShape = 'circle_Y_along_ctrlShape',
						snapAtEnd = False,
						priorJnt = '',
						scale = 20	)



#... parent joint under pin

detail_gmbl_ctrl = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_gmbCtrl', COUNT_DETAIL)
detail_jnt = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_pxyJnt', COUNT_DETAIL)

for num in range(0,COUNT_DETAIL):
	mc.parent(detail_jnt[num], detail_gmbl_ctrl[num])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Create bind joint from detail joint


bind_jnt_list = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_bJnt', COUNT_DETAIL)
for index, each in enumerate(bind_jnt_list):
	pxy_jnt = core.Dag(detail_jnt[index])
	bind_jnt = rigTools.jointAt( pxy_jnt )
	bind_jnt.attr('radius').value = 0.5
	bind_jnt.name = each

#... parent to hirechy
for i in range(1, len(bind_jnt_list)):
	mc.parent(bind_jnt_list[i], bind_jnt_list[i-1])

#... Skin bind joint to mesh
skin_cluster = mc.skinCluster(bind_jnt_list, mesh, toSelectedBones=True, name = f'{COMP_BASE_NAME}{mesh}_skc')[0]

jntPxy_list = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_pxyJnt', COUNT_DETAIL)

if mc.objExists(priorJnt):
	mc.parent(bind_jnt_list[0], priorJnt)

	for index, each in enumerate(bind_jnt_list):
		# ... pair constraint to pxyJnt
		# mtc.parentConMatrixGPT(locs[index], each, mo = True, translate = True, rotate = True, scale = True)
		print(f'parent {jntPxy_list[index]} and {each}')
		mtc.parentConMatrixGPT(jntPxy_list[index], each, mo = True, translate = True, rotate = True, scale = True)

#... parent to grp
detail_grp = core.Null(f'{COMP_BASE_NAME}_detailJnt_grp')
detail_grp.lockAllAttr(attrs=['t', 'r', 's'])
detail_loc = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_loc', COUNT_DETAIL)

for each in detail_loc:
	mc.parent(each, detail_grp)
	
	

	
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Splite weight to mesh

if smoothweight == True:
	spine_crv = core.Dag(spine_crv)
	jnts = hh.list_joints_from_skincluster(skin_cluster)
	hm.split_with_curve_to_mesh_V2(mesh, jnts, spine_crv.name, d=3, tol=0.1)

elif smoothweight == 'reverse':
	spine_crv = core.Dag(spine_crv)
	jnts = hh.list_joints_from_skincluster(skin_cluster)
	jnts = jnts[::-1]  # or jnts.reverse()
	hm.split_with_curve_to_mesh_V2(mesh, jnts, spine_crv.name, d=3, tol=0.1)
else:
	TentacleRig.info('Do nothing pass.')
	# print('Do nothing pass.')



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Make stretchy version 2

# stick_ctrl = core.Dag(f'{COMP_BASE_NAME}01_masterFkCurl_ctrl')
stick_ctrl = core.Dag(fk_rig[5])

stick_ctrlShape = core.Dag(stick_ctrl.shape)
stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'stretchy', minValue = 0, maxValue = 1, defaultValue = 1, keyable = True )

curveInfo = core.CurveInfo(f'{COMP_BASE_NAME}')
spine_crv = core.Dag(spine_crv)
spine_crv.attr('worldSpace[0]') >> curveInfo.attr('inputCurve')

#... get length
crv_length = curveInfo.attr('arcLength').value
length_ratio_mdv = core.MultiplyDivineWithVal(f'{COMP_BASE_NAME}_length_ratio_mdv',2)
curveInfo.attr('arcLength') >> length_ratio_mdv.attr('input1X')
length_ratio_mdv.attr('input2X').value = crv_length
length_ratio_mdv.attr('input1Y').value = 1
#mc.setAttr(f'{length_ratio_mdv.name}.input2X', lock = True)
length_ratio_mdv.setLocked('input2X')
length_ratio_mdv.setLocked('input1Y')
length_ratio_mdv.setLocked('input2Y')

length_store = core.MultiDoubleLinear(f'{COMP_BASE_NAME}_length_store')
length_store.attr('input2').value = 1
envelope_bta = core.BlendTwoAttr(f'{COMP_BASE_NAME}_length_store')
length_ratio_mdv.attr('outputY') >> envelope_bta.attr('input[0]')
length_ratio_mdv.attr('outputX') >> envelope_bta.attr('input[1]')
envelope_bta.attr('output') >> length_store.attr('input1')

minorIK_jnt_list = core.generate_named_pattern(f'{COMP_BASE_NAME}##_ikJnt', COUNT_DETAIL)




for index,each in enumerate(minorIK_jnt_list):
	minorIK_jnt = core.Dag(each)
	baseName = core.check_name_style(each)[0]
	y_val = mc.getAttr(f'{each}.translateY')
	print(y_val)
	multiStartVal_adl = core.MDLWithMul(f'{baseName}_stretch', dv=y_val)
	length_store.attr('output') >> multiStartVal_adl.attr('input1')
	multiStartVal_adl.attr('output') >> minorIK_jnt.attr('translateY')



stick_ctrl.attr('stretchy') >> envelope_bta.attr('attributesBlender')





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Make Squash Tentacle(optional)
if squashDef:
	squash_nrb = mc.duplicate(ik_nrb, n = ik_nrb.replace('ik', 'squash'))[0]
	squash_loc_list = core.generate_named_pattern(f'{COMP_BASE_NAME}Squash##_loc', COUNT_DETAIL)


	mc.parent(squash_nrb, nurbAll_grp)


	for num in range(0,COUNT_DETAIL):
		locator = core.Locator(squash_loc_list[num])
		ik_jnt = core.Dag(ik_detail_jnt[num])
		locator.maSnap(ik_jnt)

	squash_nrb_grp = pls.pin_locator_surface(	# need pxy nrb to drive locator
							nurbs = squash_nrb,
							region = f'{BASE_NAME}Squash',
							side = SIDE,
							source_loc = squash_loc_list,
							locator_scale = 1*SCALE,
							creJnt = False , suffixJnt = 'pxyJnt',
							creCtrl = False , ctrlShape = 'circle_Y_along_ctrlShape',
							snapAtEnd = False,
							priorJnt = '',
							scale = 20	)

	mc.setAttr(f"{COMP_BASE_NAME}_squash_nrb.tx", lock=False )
	mc.setAttr(f"{COMP_BASE_NAME}_squash_nrb.ty", lock=False )
	mc.setAttr(f"{COMP_BASE_NAME}_squash_nrb.tz", lock=False )
	mc.setAttr(f"{COMP_BASE_NAME}_squash_nrb.rx", lock=False )
	mc.setAttr(f"{COMP_BASE_NAME}_squash_nrb.ry", lock=False )
	mc.setAttr(f"{COMP_BASE_NAME}_squash_nrb.rz", lock=False )



	#... Depen on size and orientation of Nurbe
	mc.setAttr(f"{squash_nrb}.rotateX", 90 )
	mc.setAttr(f"{squash_nrb}.rotateZ", 180 )
	mc.setAttr(f"{squash_nrb}.rotateY", 0 )

	mc.setAttr(f"{squash_nrb}.translateX", 0 )
	mc.setAttr(f"{squash_nrb}.translateY", 0 )
	mc.setAttr(f"{squash_nrb}.translateZ", 0 )

	squash_meta = core.MetaBlank(f'{COMP_BASE_NAME}_squash_xVal')
	squash_deformer, squash_handle = mc.nonLinear(squash_nrb, type='squash', name = f'{COMP_BASE_NAME}_squash_deformer' )
	jntPxy_list = core.generate_named_pattern(f'{COMP_BASE_NAME}_detail##_pxyJnt', COUNT_DETAIL)



	for index, each in enumerate (squash_loc_list):
		mc.setAttr(f'{each}Shape.parameterV', 1)

		baseName = core.check_name_style(squash_loc_list[index])[0]
		multi01 = core.MDLWithMul(f'{baseName}_multiply', dv = 0.1)
		plus01 = core.AddDoubleLinear(f'{baseName}_plus01', input2 = 1)

		multi01.attr('output') >> plus01.attr('input1')
		squash_meta.addAttribute( attributeType = 'float' , longName = f'squash_{index+1:02}', minValue = -100, maxValue = 100, defaultValue = 0, keyable = True )
		squash_loc = core.Dag(each)
		squash_loc.attr('translateX') >> multi01.attr('input1')
		plus01.attr('output') >> squash_meta.attr(f'squash_{index+1:02}')

		if not mc.objExists(place_ctrl):
			pxy_jnt = core.Dag(jntPxy_list[index])
			squash_meta.attr(f'squash_{index+1:02}') >> pxy_jnt.attr('scaleY')
			squash_meta.attr(f'squash_{index+1:02}') >> pxy_jnt.attr('scaleZ')

	#... Connect scale value to placement_ctrl

	if not mc.objExists(place_ctrl):
		# print('Error, please specify placement controller.')
		TentacleRig.info('Error, please specify placement controller.')
		# return False
	else:
		placeObj_ctrl = core.Dag(place_ctrl)

		minusOne_pma = core.PlusMinusAverage(f'{COMP_BASE_NAME}_minusOne')
		minusOne_pma.attr('operation').value = 2
		placeObj_ctrl.attr('scaleX') >> minusOne_pma.attr('input3D[0].input3Dx')
		placeObj_ctrl.attr('scaleY') >> minusOne_pma.attr('input3D[0].input3Dy')
		placeObj_ctrl.attr('scaleZ') >> minusOne_pma.attr('input3D[0].input3Dz')

		minusOne_pma.attr('input3D[1].input3Dx').value = 1
		minusOne_pma.attr('input3D[1].input3Dy').value = 1
		minusOne_pma.attr('input3D[1].input3Dz').value = 1

		for index, each in enumerate (squash_loc_list):

			storeValue = core.PlusMinusAverage(f'{COMP_BASE_NAME}_storeValue{index+1:02}')
			storeValue.attr('input3D[1].input3Dx').value = 1

			minusOne_pma.attr('output3Dx') >> storeValue.attr('input3D[0].input3Dx')
			minusOne_pma.attr('output3Dy') >> storeValue.attr('input3D[0].input3Dy')
			minusOne_pma.attr('output3Dz') >> storeValue.attr('input3D[0].input3Dz')

			squash_meta.attr(f'squash_{index+1:02}') >> storeValue.attr('input3D[1].input3Dy')
			squash_meta.attr(f'squash_{index+1:02}') >> storeValue.attr('input3D[1].input3Dz')

			# pxy_jnt = core.Dag(jntPxy_list[index])
			# storeValue.attr('output3Dx') >> pxy_jnt.attr('scaleX')
			# storeValue.attr('output3Dy') >> pxy_jnt.attr('scaleY') 
			# storeValue.attr('output3Dz') >> pxy_jnt.attr('scaleZ')

			detailObj_loc = core.Dag(detail_loc[index])
			storeValue.attr('output3Dx') >> detailObj_loc.attr('scaleX')
			storeValue.attr('output3Dy') >> detailObj_loc.attr('scaleY') 
			storeValue.attr('output3Dz') >> detailObj_loc.attr('scaleZ')

	offset_X = squash_loc.attr('translateX').value
	offset_X_forHandle = offset_X * -2

	#... move handle for rim side
	mc.setAttr(f'{squash_handle}.translateX', offset_X_forHandle)
	mc.setAttr(f'{squash_nrb}.translateX', offset_X*-1)

	TentacleRig.debug(f'This is storeValue: {storeValue.name}')
	# mc.error('BREAK')



	squashLoc_list = core.generate_named_pattern(f'{COMP_BASE_NAME}Squash##_loc', COUNT_DETAIL)

	#... Cleanup grp
	squash_grp = core.Null(f'{COMP_BASE_NAME}_squashLoc_grp')
	squash_grp.lockAllAttr(attrs=['t', 'r', 's'])

	for each in squashLoc_list:
		mc.parent(each, squash_grp.name)

	mc.parent(squash_handle, squash_grp.name)

	#... Link attr to deformer
	stick_ctrlShape.addAttribute( at = 'enum', keyable = True , en = "_Squash:", longName = 'Squash'  )

	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'factor',minValue = 0 , maxValue = 1, defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'expan', minValue = -1, maxValue = 2, defaultValue = 1, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'expan_pos', minValue = 0.02, maxValue = 0.90, defaultValue = 0.8, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'start_smooth', defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'end_smooth', defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'low_bound', minValue = -10, maxValue = 0, defaultValue = -1, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'high_bound', minValue = 0, maxValue = 10, defaultValue = 1, keyable = True )
	squash_deformer = core.Dag(squash_deformer)
	inv_value_mdl = core.MDLWithMul(f'{COMP_BASE_NAME}_squash_invValue',dv=-1)

	stick_ctrlShape.attr('factor')>> inv_value_mdl.attr('input1')
	inv_value_mdl.attr('output')>> squash_deformer.attr('factor')
	# stick_ctrlShape.attr('factor')>> squash_deformer.attr('factor')

	stick_ctrlShape.attr('expan_pos')>> squash_deformer.attr('maxExpandPos')
	stick_ctrlShape.attr('start_smooth')>> squash_deformer.attr('startSmoothness')
	stick_ctrlShape.attr('end_smooth')>> squash_deformer.attr('endSmoothness')

	stick_ctrlShape.attr('expan')>> squash_deformer.attr('expand')
	stick_ctrlShape.attr('low_bound')>> squash_deformer.attr('lowBound')
	stick_ctrlShape.attr('high_bound')>> squash_deformer.attr('highBound')


	mc.setAttr(f'{squash_nrb}.visibility', 0)
	squash_grp.attr('visibility').value = 0








# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. create sine wave deformer
if sineDef:
	sine_def_nrb = mc.duplicate(ik_nrb,n = ik_nrb.replace('ik','sine'))[0]
	sine_deformer, sine_handle = mc.nonLinear(sine_def_nrb, type='sine', name = f'{COMP_BASE_NAME}_sineDef' )
	sine_zro_grp = core.Null(f'{COMP_BASE_NAME}_sineDefZroGrp')
	mc.parent(sine_handle, sine_zro_grp.name)
	sine_zro_grp.attr('visibility').value = 0
	sine_zro_grp.lockAllAttr(attrs=['t', 'r', 's'])

	#... BlendShape change 2 to 3
	mc.blendShape(f'{COMP_BASE_NAME}_bsh', e=True, t=(f'{COMP_BASE_NAME}_combineFkIk_nrb', 2, sine_def_nrb, 1.0))
	mc.setAttr(f'{COMP_BASE_NAME}_bsh.{sine_def_nrb}',1)

	#... Connect value for stick
	stick_ctrlShape = core.Dag(stick_ctrl.shape)
	stick_ctrlShape.addAttribute( at = 'enum', keyable = True , en = "_SINE:", longName = 'SINE'  )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'envelope',minValue = 0 , maxValue = 1, defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'amplitude', defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'wavelength', defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'offset', defaultValue = 0, keyable = True )
	stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'orientation', defaultValue = 0, keyable = True )

	sine_deformer = core.Dag(sine_deformer)
	#... set starter volumne
	stick_ctrlShape.attr('envelope').value = 0
	stick_ctrlShape.attr('amplitude').value = 0.3
	stick_ctrlShape.attr('wavelength').value = 1.5


	#... store value for upcomming connection
	offset_store_val = core.PlusMinusAverage(f'{COMP_BASE_NAME}_offsetStoreVal_pma')
	amp_store_val = core.PlusMinusAverage(f'{COMP_BASE_NAME}_ampStoreVal_pma')
	length_store_val = core.PlusMinusAverage(f'{COMP_BASE_NAME}_lengthStoreVal_pma')

	stick_ctrlShape.attr('offset') >> offset_store_val.attr('input1D[0]')
	stick_ctrlShape.attr('amplitude') >> amp_store_val.attr('input1D[0]')
	stick_ctrlShape.attr('wavelength') >> length_store_val.attr('input1D[0]')

	offset_store_val.attr('output1D') >> sine_deformer.attr('offset')
	sine_handle = core.Dag(sine_handle)
	stick_ctrlShape.attr('orientation') >> sine_handle.attr('rotateY')

	stick_ctrlShape.attr('envelope') >> sine_deformer.attr('envelope')
	amp_store_val.attr('output1D') >> sine_deformer.attr('amplitude')
	length_store_val.attr('output1D') >> sine_deformer.attr('wavelength')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Cleanup
stick_ctrlShape.deleteAttribute('Detail')


#stick_ctrlShape=core.Dag('C_tenTail01_masterFkCurl_ctrlShape')

stick_ctrlShape.addAttribute( at = 'enum', keyable = True , en = "_MAIN:", longName = 'MAIN_CTRL'  )
stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'ten_FKIK', minValue = 0, maxValue = 1, defaultValue = 0, keyable = True )
stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'ten_IK', minValue = 0, maxValue = 1, defaultValue = 0, keyable = True )
stick_ctrlShape.addAttribute( attributeType = 'float' , longName = 'ten_Detail', minValue = 0, maxValue = 1, defaultValue = 0, keyable = True )
masterFk_zrpGrp = core.Dag(f'{COMP_BASE_NAME}01_masterFkZro_grp')


masterFk_zrpGrp.disconnectAttr('visibility')
stick_ctrlShape.attr('ten_FKIK') >> masterFk_zrpGrp.attr('visibility')
stick_ctrlShape.attr('ten_Detail') >> detail_grp.attr('visibility')
stick_ctrlShape.attr('ten_FKIK').value = 1

if sineDef:
	mc.setAttr(f'{sine_def_nrb}.visibility',0)
	mc.parent(sine_def_nrb, nurbAll_grp.name)



mc.setAttr(f'{ik_nrb}.visibility',0)

# mc.parent(twist_def_nrb, nurbAll_grp.name)

mc.parent(ik_nrb, nurbAll_grp.name)
mc.parent(combineFkIk_nrb, nurbAll_grp.name)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Create meta node
if sineDef:
	chain_meta = core.Dag(fk_rig[-1])
	chain_meta.addAttribute( dataType = 'string' , longName = 'storeValue')
	chain_meta.attr('storeValue').value = f'{offset_store_val.name}, {amp_store_val.name}, {length_store_val.name}'
	chain_meta.setLocked('storeValue')
	chain_meta.addAttribute( dataType = 'string' , longName = 'stickName')
	chain_meta.attr('stickName').value = stick_ctrl.name
	chain_meta.setLocked('stickName')
	#stick_ctrl.attr('message') >> chain_meta.attr('Rig_Prior')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ..................Hide Ik ctrl vis

# master_ik_ctrl = [PATTERN.format(SIDE=SIDE, BASE_NAME=BASE_NAME, index=str(i).zfill(2)) for i in range(1, COUNT_MAIN + 1)]
master_ik_ctrl = core.generate_named_pattern(f'{COMP_BASE_NAME}##_masterIk_ctrl', COUNT_DETAIL)

for each in master_ik_ctrl:
	master_ik_ctrlShape = core.Dag(core.shapeName(each))

	stick_ctrlShape.attr('ten_IK') >> master_ik_ctrlShape.attr('visibility')




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. make scalable
if sineDef == False or squashDef == False:
	if mc.objExists(place_ctrl):
		placeObj_ctrl = core.Dag(place_ctrl)
		for index, each in enumerate (detail_loc):
			detail_loc = core.Dag(each)

			minusOne_pma = core.PlusMinusAverage(f'{COMP_BASE_NAME}_minusOne')
			placeObj_ctrl.attr('scaleX') >> detail_loc.attr('scaleX')
			placeObj_ctrl.attr('scaleY') >> detail_loc.attr('scaleY')
			placeObj_ctrl.attr('scaleZ') >> detail_loc.attr('scaleZ')



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Parent Importent grp

if not mc.objExists('tentacleStill_grp'):
	tenStillStore_grp = core.Null('tentacleStill_grp')
else:
	tenStillStore_grp = core.Dag('tentacleStill_grp')



mc.parent(nurbAll_grp.name, tenStillStore_grp.name)
# mc.parent(twist_grp_obj.name, tenStillStore_grp.name)
mc.parent(detail_grp.name, tenStillStore_grp.name)


if not mc.objExists('tentacleIkh_grp'):
	tenIkhStore_grp = core.Null('tentacleIkh_grp')
else:
	tenIkhStore_grp = core.Dag('tentacleIkh_grp')

# mc.parent(ikHandle.name(), tenIkhStore_grp)
mc.parent(ikHandle.name, tenIkhStore_grp)

if sineDef:
	mc.parent(sine_zro_grp.name, tenStillStore_grp.name)
	
if squashDef:
	mc.parent(squash_grp.name, tenStillStore_grp.name)

if not mc.objExists('tentacleFkJnt_grp'):
	tenFkJnt_grp = core.Null('tentacleFkJnt_grp')
else:
	tenFkJnt_grp = core.Dag('tentacleFkJnt_grp')

	
mc.parent(f'{COMP_BASE_NAME}01_masterFk_fkJnt', tenFkJnt_grp.name)

if mc.objExists(parentTo):
	print(f'{COMP_BASE_NAME}01_masterFkRig_grp')
	
	master_fk_zroGrp = core.Dag(f'{COMP_BASE_NAME}01_masterFkRig_grp')
	mc.parent(master_fk_zroGrp, parentTo)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Assign ikh to stick
stick_ctrl.addAttribute( attributeType = 'message' , longName = 'ikh_msg')
# stick_ctrl.attr('message') >> stick_ctrl.attr('ikHandle')
ikHandle.attr('message') >> stick_ctrl.attr('ikh_msg')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Set IK twist 
if enableTwist:
    ikHandle.attr('dWorldUpType').value = 2
	ikHandle.enableTwistControl(
								forwardAxis=forwardAxis,
								worldUpAxis=worldUpAxis,
								worldUpVector=worldUpVector,
								worldUpVectorEnd=worldUpVectorEnd,
								worldUpType=worldUpType,
								upObject=upObject,
								upObjectEnd=upObjectEnd
							)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # .................. Done
core.makeHeader('DONE')