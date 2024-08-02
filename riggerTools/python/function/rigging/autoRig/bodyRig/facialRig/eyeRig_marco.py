#... source >>> D:\narongtum\research_and_developement\23.09.Sep.09.Sat.17_Cartoon eyeLid rigging _Macro Giordano\2023_09_11_EyeLid Marco
from function.rigging.autoRig.base import core
reload(core)

import maya.cmds as mc

from maya import OpenMaya
import uuid
#... start of part 1
#... todo: create root and tip joint at the eye ball for each in vertex at eyeSocket
#... todo: create series of locator of each vtx




def eyeRig_marco(	loc_grp = 'L_eye_up_locGrp', part_dict = {},
					CENTER = 'L_center', SIDE = 'L', crtlShape = 'plainSphereB_ctrlShape', 
					ctrlSize = 0.01):
	

	objectsInGroup = mc.listRelatives(loc_grp, children=True)

	# Select all objects in the list.
	mc.select(objectsInGroup)




	# loc = mc.ls(sl=True, fl=True)[0]


	#... ask part is up or down
	PART = loc_grp.split('_')[2]
	#PART = 'up'
	
	
	crv_hi = 'L_{}LidHigh_CRV'.format(PART)
	crv_low = 'L_{}LidLow_CRV'.format(PART)
	
	

	#... ask if part_dict is exists before
	if PART == 'up':
		part_dict = {'up':[],'down':[]}


	#... the last 2 order is corner joint
	if PART == 'up':
		#... this is an order ['R_between', 'mid', 'L_between', 'R_corner', 'L_corner']
		jointCurve = ['L_eye01_jnt', 'L_eye02_jnt', 'L_eye03_jnt', 'L_eye07_jnt', 'L_eye08_jnt']
	elif PART == 'down':
		jointCurve = ['L_eye04_jnt','L_eye05_jnt','L_eye06_jnt', 'L_eye07_jnt', 'L_eye08_jnt']

	upVec = 'L_eyeVec_LOC'



	vtx = mc.ls(sl=True, fl=True)



	#...	[ START OF PART 1 ]
	mc.select(cl=True)
	grp = mc.group(empty=True, name = '{}_{}EyeLid_Jnt_GRP'.format(SIDE,PART))
	num = 1
	tipJnt = []
	for each in vtx:
		mc.select(cl=True)
		tip_jnt = core.Joint('{}_{}EyeLidTip{:02d}_{}'.format(SIDE, PART, num, 'JNT'),radius = 0.1, overrideEnabled = True, overrideColor = 3)
		jnt = tip_jnt.name
		# jnt = mc.joint(name = '{}_{}EyeLidTip{:02d}_{}'.format(SIDE, PART, num, 'JNT'))
		pos = mc.xform(each, q=True, ws=True, t=True)
		mc.xform(jnt, ws=True, t=pos)
		posC = mc.xform(CENTER, q=True, ws=True, t=True)
		mc.select(cl=True)
		jntC = mc.joint(name = '{}_{}EyeLid{:02d}_{}'.format(SIDE, PART, num, 'JNT'))
		mc.xform(jntC, ws=True, t=posC)
		mc.parent(jnt, jntC)
		mc.joint(jntC, e=True, oj = 'xyz' , secondaryAxisOrient='yup', ch=True, zso=True)
		tipJnt.append(jnt)
		num = num + 1

		mc.parent(jntC, grp)


	mc.select(cl=True)






	#... select tip joint first
	#sel = mc.ls(sl=True)


	sel = tipJnt
	grp = mc.group(empty=True, name = '{}_{}EyeLid_AimLoc_GRP'.format(SIDE,PART))

	aimLoc = []
	num = 1
	for each in sel:
		# loc = mc.spaceLocator(name = '{}_{}EyeLidAim{:02d}_{}'.format(SIDE, PART, num, 'LOC'))[0]
		loc = core.Locator(name = '{}_{}EyeLidAim{:02d}_{}'.format(SIDE, PART, num, 'LOC'), lock = True, scale = 0.1)
		pos = mc.xform(each, q=True, ws=True, t=True)
		mc.xform(loc.name, ws=True, t=pos)
		par = mc.listRelatives(each, p=True)[0]
		mc.aimConstraint(loc.name, par, mo=True, weight=1, aimVector=(1,0,0), upVector=(0,1,0), worldUpType='object', worldUpObject = upVec, name = '{}_{}EyeLidAim{:02d}_{}'.format(SIDE, PART, num, 'aimCon')  )
		aimLoc.append(loc.name)
		num = num + 1

		mc.parent(loc.name, grp)
	mc.select(cl=True)

	#...	[ END OF PART 1 ]

	def getUParam(pnt=[], crv=None):
		point = OpenMaya.MPoint(pnt[0], pnt[1], pnt[2])
		curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
		paramUtil = OpenMaya.MScriptUtil()
		paramPtr = paramUtil.asDoublePtr()
		isOnCurve = curveFn.isPointOnCurve(point)
		if isOnCurve:
			curveFn.getParamAtPoint(point, paramPtr, 0.001, OpenMaya.MSpace.kObject)
		else:
			point = curveFn.closestPoint(point, paramPtr, 0.001, OpenMaya.MSpace.kObject)
			curveFn.getParamAtPoint(point, paramPtr, 0.001, OpenMaya.MSpace.kObject)

		param = paramUtil.getDouble(paramPtr)
		print(param)
		return param

	def getDagPath(objectName):
		# Ensure objectName is a string or list of strings
		if not isinstance(objectName, (str, list)):
			raise TypeError("objectName must be a string or list of strings")

		# If it's a single string, convert to list for processing
		objectName = objectName if isinstance(objectName, list) else [objectName]

		oNodeList = []
		for o in objectName:
			selectionList = OpenMaya.MSelectionList()
			selectionList.add(o)
			oNode = OpenMaya.MDagPath()
			selectionList.getDagPath(0, oNode)
			oNodeList.append(oNode)
		# Return a single result if input was a single object
		return oNodeList[0] if len(oNodeList) == 1 else oNodeList

	def cleanup_nodes(nodes):
		"""Deletes the specified nodes if they exist."""
		for node in nodes:
			if mc.objExists(node):
				mc.delete(node)









	#...[ START OF PART 2 ]_make locator stick to curve
	#... select aim locator
	#... fill curve shape name
	sel = aimLoc
	print(sel)
	# mc.error('Stop')

	pos = []

	for each in sel:	
		pos = mc.xform(each, q=True, ws=True, t=True)
		print(f'This is pos: {pos}')
		print(f'This is crv_hi: {crv_hi}')
		print(f'This is arg 1 data type: {type(pos)}')
		print(f'This is arg 2 data type: {type(crv_hi)}')
		uVal = getUParam(pos, crv_hi)
		print(f'\nthis is uVal{uVal}.')
		name = each.replace('LOC', 'PCI')
		print(name)
		pci=mc.createNode('pointOnCurveInfo', name = name)
		mc.connectAttr(crv_hi + '.worldSpace', pci + '.inputCurve')
		mc.setAttr(pci+'.parameter', uVal)
		mc.connectAttr( pci + '.position', each + '.t')





			
			
	#... making low resolution curve
	#... make wire deformer
	mc.wire(crv_hi, wire = crv_low , envelope=1, crossingEffect=0, localInfluence=0, name=crv_low + '_WR', groupWithBase = False)


	#... skin joint to low curve
	eyeCurve_skc = core.SkinCluster( jointCurve, crv_low, dropoffRate = 7 , maximumInfluences = 2 )
	eyeCurve_skc.name =  crv_low + '_skc'


	#... create controller link to the joint
	from function.rigging.controllerBox import adjustController as adjust
	from function.framework.reloadWrapper import reloadWrapper as reload
	reload(adjust)





	if PART == 'up':

		ctrl_name = adjust.creControllerFunc( jointCurve, scale = ctrlSize, ctrlShape = crtlShape, color = 'yellow' )
		part_dict[PART].append(ctrl_name)

	elif PART == 'down':

		for each in jointCurve:
			if mc.objExists('{}.isCorner'.format(each)): #... if found joint that at the corner do not repeat
				continue
			else:
				ctrl_name = adjust.creControllerFunc( [each], scale = ctrlSize, ctrlShape = crtlShape, color = 'yellow' )
				part_dict[PART].append(ctrl_name)






	from function.rigging.util import misc
	reload(misc)


	#... constraint from middle and corner to in between
	if PART == 'up':
		
		#... find raw name from L to R
		#... L is L of object

		L_between_zro = part_dict['up'][0][6]
		R_between_zro = part_dict['up'][0][0]

		middle_ctrl = part_dict['up'][0][4]
		
		R_corner_ctrl = part_dict['up'][0][-4]
		L_corner_ctrl = part_dict['up'][0][-1]
		
		#... make middle ctrl bigger
		middle_ctrl_obj = core.Dag(middle_ctrl)
		middle_ctrl_obj.editCtrlShape(axis =   1.75 )
		middle_ctrl_obj.color = 'yellow'


		#... constraint between
		
		constr_object = core.pointConstraint( L_corner_ctrl, middle_ctrl, L_between_zro, maintainOffset=True) 
		constr_object.name = L_between_zro + '_poiCon'

		constr_object = core.pointConstraint( middle_ctrl, R_corner_ctrl, R_between_zro, maintainOffset=True) 
		constr_object.name = R_between_zro + '_poiCon'

		core.makeHeader(f'eye part {PART} rig almose done.')

		return part_dict

	#... their is cuase an error if I ever ran 'down' before
	if PART == 'down':
		print('down is exists')
		R_corner_ctrl = part_dict['up'][0][-4]	
		L_corner_ctrl = part_dict['up'][0][-1]
		


		#... find raw name from L to R
		middle_ctrl = part_dict['down'][1][1]

		#... between
		R_between_zro = part_dict['down'][0][0]
		L_between_zro = part_dict['down'][2][0]
		
		
		#... make middle ctrl bigger
		middle_ctrl_obj = core.Dag(middle_ctrl)
		middle_ctrl_obj.editCtrlShape(axis =   1.75 )
		middle_ctrl_obj.color = 'yellow'


		constr_object = core.pointConstraint( R_corner_ctrl, middle_ctrl, R_between_zro, maintainOffset=True) 
		constr_object.name = L_between_zro + '_poiCon'
		constr_object = core.pointConstraint( middle_ctrl, L_corner_ctrl, L_between_zro, maintainOffset=True) 
		constr_object.name = R_between_zro + '_poiCon'

		core.makeHeader(f'eye part {PART} rig almose done.')





#...[ END OF PART 2 ]


part_dict = eyeRig_marco(loc_grp = 'L_eye_up_locGrp')
eyeRig_marco(loc_grp = 'L_eye_down_locGrp', part_dict = part_dict)

#...[ START OF PART 3 ] create smart blink whit blendshape the curve run once alter finish part 1 and 2
#... create blendshape between upLid_low, downLid_low, new_dup_crv
#... create attr to broad ctrl

#... duplicate lid low
#... if part






from function.rigging.autoRig.base import core
reload(core)


def make_eyeMarco_blink(	PART = 'up',
							SIDE = 'L',
							CURVE = 'CRV',
							up_low_crv = 'L_upLidLow_CRV',
							down_low_crv = 'L_downLidLow_CRV',

							up_hi_crv = 'L_upLidHigh_CRV',
							down_hi_crv = 'L_downLidHigh_CRV',
							mid_up_ctrl = 'L_eye02_ctrl',
							mid_down_ctrl = 'L_eye05_ctrl'):




	if PART == "up":
		blendShape_upBlink_crv = core.duplicate(up_low_crv)
		blendShape_upBlink_crv.name = 'L_lidBlink_master_CRV'


	blendShape_upBlink_crv.color = 'red'


	#... create attr at broad ctrl for control blendshape
	shapeName = core.shapeName(mid_up_ctrl)
	#mc.error('stop')
	middle_ctrl = core.Dag(shapeName)

	# middle_ctrlShape =middle_ctrl.shape
	middle_ctrl.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink_heigh', keyable = True, defaultValue = 0   )
	middle_ctrl.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink', keyable = True, defaultValue = 0   )

	shapeName = core.shapeName(mid_down_ctrl)
	middle_down_ctrl = core.Dag(shapeName)
	# middle_down_ctrl.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink_heigh', keyable = True, defaultValue = 0   )
	# middle_down_ctrlShape = middle_ctrl.shape

	middle_down_ctrl.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink', keyable = True, defaultValue = 0   )


	smartBlink_bsh = mc.blendShape(up_low_crv, down_low_crv, blendShape_upBlink_crv.name, origin = 'world', name =  'L_targetSmartBlink_BSH')[0]
	mc.setAttr('{}.{}'.format(smartBlink_bsh,up_low_crv), 0)
	mc.setAttr('{}.{}'.format(smartBlink_bsh,down_low_crv), 0)
	#smartBlink_bsh = 	'L_targetSmartBlink_BSH'


	# #... duplicate up and down (this is original version)
	upBlink_crv = core.duplicate(up_hi_crv)
	upBlink_crv.name = '{}_{}LidBlink_{}'.format(SIDE, 'Up', CURVE)
	downBlink_crv = core.duplicate(down_hi_crv)
	downBlink_crv.name = '{}_{}LidBlink_{}'.format(SIDE, 'Down', CURVE)

	#... duplicate up and down
	# upBlink_crv = core.duplicate(up_low_crv)
	# upBlink_crv.name = '{}_{}LidBlink_follow_{}'.format(SIDE, 'Up', CURVE)
	# downBlink_crv = core.duplicate(down_low_crv)
	# downBlink_crv.name = '{}_{}LidBlink_follow_{}'.format(SIDE, 'Down', CURVE)


	#... make it follow smart blink curve
	#... [child][parent]
	up_wire = mc.wire(upBlink_crv.name, wire = blendShape_upBlink_crv.name , envelope=1, crossingEffect=0, localInfluence=0, name='{}_{}LidBlink_{}'.format(SIDE, 'Up', 'WR'), groupWithBase = False)[0]
	#mc.setAttr('L_UpLidBlink_WR.scale[0]', 0)

	#... if down must fix value of BSH dow to 1 
	mc.setAttr('{}.{}'.format(smartBlink_bsh,down_low_crv), 1)
	mc.setAttr('{}.{}'.format(smartBlink_bsh,up_low_crv), 1)

	down_wire = mc.wire(downBlink_crv.name, wire = blendShape_upBlink_crv.name , envelope=1, crossingEffect=0, localInfluence=0, name='{}_{}LidBlink_{}'.format(SIDE, 'Down', 'WR'), groupWithBase = False)[0]
	mc.setAttr('{}.scale[0]'.format(down_wire), 0)
	#mc.setAttr('{}.{}'.format(smartBlink_bsh,down_low_crv), 0)

	#... if you want to make controller foller curve use another method below


	#... now blendshape between 
	upLidBlink_bsh = mc.blendShape(upBlink_crv.name, up_hi_crv, origin = 'local', before=True, name =  '{}_{}LidBlink_{}'.format(SIDE, 'Up', 'BSH'))[0]
	mc.setAttr('{}.{}'.format(upLidBlink_bsh, upBlink_crv.name), 1)

	downLidBlink_bsh = mc.blendShape(downBlink_crv.name, down_hi_crv, origin = 'local', before=True, name =  '{}_{}LidBlink_{}'.format(SIDE, 'Down', 'BSH'))[0]
	mc.setAttr('{}.{}'.format(downLidBlink_bsh, downBlink_crv.name), 1)

	#upLidBlink_bsh = 'blendShape1'
	#downLidBlink_bsh = 'blendShape2'

	#... link connnection
	mc.connectAttr('{}.smart_Blink'.format(middle_ctrl), '{}.{}'.format(upLidBlink_bsh, upBlink_crv.name), f=True)
	mc.connectAttr('{}.smart_Blink'.format(middle_down_ctrl), '{}.{}'.format(downLidBlink_bsh, downBlink_crv.name),f=True)

	#... link smart blink heigh
	rev_value = core.ReverseNam('{}_smartBlink_{}'.format(SIDE,'REV'))
	mc.connectAttr('{}.smart_Blink_heigh'.format(middle_ctrl), '{}.{}'.format(smartBlink_bsh, down_low_crv), f=True)
	mc.connectAttr('{}.smart_Blink_heigh'.format(middle_ctrl), '{}.inputX'.format(rev_value.name), f=True)
	mc.connectAttr('{}.outputX'.format(rev_value.name), '{}.{}'.format(smartBlink_bsh, up_low_crv), f=True)

	#... set intial value
	middle_ctrl.attr('smart_Blink_heigh').value = 0.8

	core.makeHeader(f'Make eyeMarco blink {PART}done.')


make_eyeMarco_blink()