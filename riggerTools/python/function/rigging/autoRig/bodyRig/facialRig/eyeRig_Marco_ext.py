#... [EYE RIG Marco Fashion]

#... eye lid rig
# by Marco Giordano
# https://www.youtube.com/watch?v=-rtys3vFmso

#... Source file
# D:\narongtum\research_and_developement\23.09.Sep.09.Sat.17_Cartoon eyeLid rigging _Macro Giordano
# D:\narongtum\research_and_developement\23.09.Sep.09.Sat.17_Cartoon eyeLid rigging _Macro Giordano\2023_09_11_EyeLid Marco

#... Sample scene
# D:\narongtum\research_and_developement\24.03.Mar.18.Mon.17_Facial Rig(Use this)\myFile\round_4\04_05_eye\04_05_eye_01_start.0001.ma

'''
# direct run

'''

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc
from maya import OpenMaya

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

#...  logging system 
import logging
from function.pipeline import logger 
reload(logger)

from function.rigging.util import misc
reload(misc)

#... create controller link to the joint
from function.rigging.controllerBox import adjustController as adjust
reload(adjust)




'''
### direct run







from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.bodyRig.facialRig import eyeRig_Marco_ext
reload(eyeRig_Marco_ext)

from function.rigging.autoRig.base import core
reload(core)


eye_up_dict = eyeRig_Marco_ext.createControlEye(		group_name = 'L_eye_up_locGrp', 
									CENTER = 'L_center', SIDE = 'L',
									PART = 'up',
									crv_hi = 'L_upLidHigh_CRV',
									crv_low = 'L_upLidLow_CRV',
									crtlShape = 'plainSphereB_ctrlShape',
									ctrlSize = 0.01,
									upVec = 'L_eyeVec_LOC',
									proxy_jointCurve = ('L_eye01_jnt', 'L_eye02_jnt', 'L_eye03_jnt', 
														'L_eye07_corner_jnt', 'L_eye08_corner_jnt')
										)
										
										
eye_down_dict = eyeRig_Marco_ext.createControlEye(		group_name = 'L_eye_down_locGrp', 
									CENTER = 'L_center', SIDE = 'L',
									PART = 'down',
									crv_hi = 'L_downLidHigh_CRV',
									crv_low = 'L_downLidLow_CRV',
									crtlShape = 'plainSphereB_ctrlShape',
									ctrlSize = 0.01,
									upVec = 'L_eyeVec_LOC',
									proxy_jointCurve = ('L_eye04_jnt','L_eye05_jnt','L_eye06_jnt'
														)	,
									corner_joint = (eye_up_dict['joint'][-2], eye_up_dict['joint'][-1])
									)

#... eye_up_dict['joint'][-2] = 'L_eye07_corner_pxyJnt'
#... eye_up_dict['joint'][-1] = 'L_eye08_corner_pxyJnt'
									
#eye_up_dict['joint'][-2]
#... Make share transition

#... L SIDE									
eyeRig_Marco_ext.makeInbetweener(eye_up_dict = eye_up_dict, eye_down_dict = eye_down_dict)



#... Make smart blink left side

smartBlink_grp = eyeRig_Marco_ext.makeSmartBlink(
					SIDE = 'L'							,
					CURVE = 'CRV'						,
					up_low_crv = 'L_upLidLow_CRV'		,
					down_low_crv = 'L_downLidLow_CRV'	,
					up_hi_crv = 'L_upLidHigh_CRV'		,
					down_hi_crv = 'L_downLidHigh_CRV'
															)








'''




#... [Must have]
#... 1. eye center locator
#... 2. eye up vector locator
#... 3. create group name 'group1' that contain locator at every upper VTX naming 'up_locatorxx'
#... 4. curve hi and curve low
#... 5. joint for broad each minor joint



# # # # # # 
# Part 1 # make this to function and return dict that up or down
# # # # # # 



# group_name = 'group1'
# CENTER = 'L_center'
# SIDE = 'L'
# crv_hi = 'L_{}LidHigh_CRV'.format(PART)
# crv_low = 'L_{}LidLow_CRV'.format(PART)
# crtlShape = 'plainSphereB_ctrlShape'
# ctrlSize = 0.01

class EyeRigMarco(logger.MayaLogger):
	LOGGER_NAME = "eyeRig_Marco"




def _unparent_if_not_world(obj_name):
	parent = mc.listRelatives(obj_name, parent=True)
	if parent == None:
		print('object has been unparented from its previous parent and is now a child of world')
	else:
		mc.parent(obj_name, world=True)
	


#... Make eye rig with skin around Eye socket
def createControlEye(	group_name = 'upLoc_grp', 
						CENTER = 'L_center_LOC', 
						SIDE = 'L',
						PART = 'up',
						crv_hi = 'L_upLidHigh_CRV',
						crv_low = 'L_upLidLow_CRV',
						crtlShape = 'plainSphereB_ctrlShape',
						ctrlSize = 0.01 ,
						upVec = 'L_eyeUpVec_LOC',
						color = 'yellow'	,
						proxy_jointCurve = ('L_eye01_jnt', 'L_eye02_jnt', 'L_eye03_jnt', 'L_eye07_jnt', 'L_eye08_jnt'), #... [between ,mid, between, corner, corner]
						corner_joint = ('L_eye07_corner_pxyJnt', 'L_eye08_corner_pxyJnt') ,#... use for down only
						orient_joint = 'xyz'
						):

	#... unparent obj to world outliner

	_unparent_if_not_world(crv_low)
	_unparent_if_not_world(crv_hi)
	_unparent_if_not_world(CENTER)
	_unparent_if_not_world(upVec)

	part_dict = {}

	#... find name and list member
	objectsInGroup = mc.listRelatives(group_name, children=True)

	#... Select all objects in the list.
	mc.select(objectsInGroup)
	loc = mc.ls(sl=True, fl=True)[0]

	#... ask part is upper or lower
	PART = PART

	#... select locator again
	vtx = mc.ls(sl=True, fl=True)

	mc.select(cl=True)
	# grp = mc.group(empty=True, name = '{}_{}EyeLid_Jnt_GRP'.format(SIDE,PART))
	eyeLid_aimJnt_grp = core.Null('{0}_{1}EyeLid_AimJnt_GRP'.format(SIDE,PART))
	eyeLid_aimJnt_grp.maSnap( CENTER , position = True , rotation = True , scale = True )


	num = 1
	tipJnt = []
	for each in vtx:
		mc.select(cl=True)
		# jnt = mc.joint(name = '{}_{}EyeLidTip{:02d}_{}'.format(SIDE, PART, num, 'JNT'))
		tip_jnt = core.Joint('{}_{}EyeLidTip{:02d}_{}'.format(SIDE, PART, num, 'JNT'),radius = 0.1, overrideEnabled = True, overrideColor = 3)
		jnt = tip_jnt.name
		pos = mc.xform(each, q=True, ws=True, t=True)
		mc.xform(jnt, ws=True, t=pos)
		posC = mc.xform(CENTER, q=True, ws=True, t=True)
		mc.select(cl=True)
		jntC = mc.joint(name = '{}_{}EyeLidAim{:02d}_{}'.format(SIDE, PART, num, 'JNT'))
		mc.xform(jntC, ws=True, t=posC)
		mc.parent(jnt, jntC)
		mc.joint(jntC, e=True, oj = orient_joint , secondaryAxisOrient='yup', ch=True, zso=True)
		tipJnt.append(jnt)
		num = num + 1

		mc.parent(jntC, eyeLid_aimJnt_grp)
	part_dict['top_grp'] = []
	part_dict['top_grp'].append(eyeLid_aimJnt_grp.name)
	mc.select(cl=True)






	#...#...#...#...#...#...#...#...#...#...#...#...
	#... Ppart 1/2: Make Eye Aim 
	#...#...#...#...#...#...#...#...#...#...#...#...


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

		mc.aimConstraint(loc.name, par, mo=True, weight=1, aimVector=(1,0,0), upVector=(0,1,0), worldUpType='object', worldUpObject = upVec, name = f'{SIDE}_{PART}EyeLidAim{num:02d}_aimCon' )
		aimLoc.append(loc.name)
		num = num + 1

		mc.parent(loc.name, grp)

	part_dict['top_grp'].append(grp)
	mc.select(cl=True)


	part_dict['locator_still'] = []
	part_dict['locator_still'] = grp


	#... END OF PART 1





	def getUParam( pnt = [], crv = None):

		point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
		curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
		paramUtill=OpenMaya.MScriptUtil()
		paramPtr=paramUtill.asDoublePtr()
		isOnCurve = curveFn.isPointOnCurve(point)
		if isOnCurve == True:
			
			curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
		else :
			point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
			curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
		
		param = paramUtill.getDouble(paramPtr)
		print (param)  
		return param


	def getDagPath(objectName):
		# check for objectName type
		objectName = objectName if isinstance(objectName, list) else [objectName]
		
		oNodeList=[]
		for o in objectName:
			selectionList = OpenMaya.MSelectionList()
			selectionList.add(o)
			oNode = OpenMaya.MDagPath()
			selectionList.getDagPath(0, oNode)
			oNodeList.append(oNode)
		# if the input was a single object (not a list), then return a single result
		# otherwise return a list
		return oNodeList[0] if len(oNodeList) == 1 else oNodeList 



	#...#...#...#...#...#...#...#...#...#...#...#...
	#... start of part 1/2: Wire deformer 
	#...#...#...#...#...#...#...#...#...#...#...#...

	#... select aim locator
	#... fill curve shape name
	sel = aimLoc

	pos = []

	for each in sel:	
		pos = mc.xform(each, q=True, ws=True, t=True)
		type(pos)
		type(crv_hi)
		uVal = getUParam(pos, crv_hi)
		name = each.replace('LOC', 'PCI')
		print(name)
		pci=mc.createNode('pointOnCurveInfo', name = name)
		mc.connectAttr(crv_hi + '.worldSpace', pci + '.inputCurve')
		mc.setAttr(pci+'.parameter', uVal)
		mc.connectAttr( pci + '.position', each + '.t')




			
	#... making low resolution curve
	#... make wire deformer
	wire_name = mc.wire(crv_hi, wire = crv_low , envelope=1, crossingEffect=0, localInfluence=0, name=crv_low + '_WR', groupWithBase = False)
	 

	mc.rename(crv_low + 'BaseWire', crv_low + '_baseWire')
	base_wire_node = crv_low + '_baseWire'

	# mc.error()
	# mc.select(base_wire_node, r=True)
	




	#...#...#...#...#...#...#...#...#...#...#...#...
	#... Duplicate curve joint
	#...#...#...#...#...#...#...#...#...#...#...#...



	eyeLidZro_grp = core.Null('{0}_{1}EyeLid_broadWireZro_{2}'.format(SIDE, PART,  'grp'))
	eyeLidZro_grp.maSnap( CENTER , position = True , rotation = True , scale = True )

	joint_curve=[]

	if PART == 'up':
		for each in proxy_jointCurve:
			rawName = misc.makeProperSeparater(each)
			tmp_jnt = core.Dag( each )
			# each_joint = rigTools.jointAt( joint )
			each_joint = core.Joint(rawName + '_pxyJnt',radius = 0.1, overrideEnabled = True, overrideColor = 3)
			each_joint.snap(tmp_jnt)
			# each_joint.name = rawName + '_pxyJnt'
			joint_curve.append(each_joint.name)
			each_joint.parent(eyeLidZro_grp)

		# mc.error('Mile Stone Stop.')


	elif PART == 'down':
		for each in proxy_jointCurve:
			# if each.split('_')[-3] == 'corner':
			if 'corner' in each:
				continue
			else:
				rawName = misc.makeProperSeparater(each)
				tmp_jnt = core.Dag( each )
				# each_joint = rigTools.jointAt( joint )
				each_joint = core.Joint(rawName + '_pxyJnt',radius = 0.1, overrideEnabled = True, overrideColor = 3)
				each_joint.snap(tmp_jnt)
				# each_joint.name = rawName + '_pxyJnt'
				joint_curve.append(each_joint.name)
				each_joint.parent(eyeLidZro_grp)


	part_dict['top_grp'].append(eyeLidZro_grp.name)










	#...#...#...#...#...#...#...#...#...#...#...#...
	#... skin joint curve to low curve 
	#...#...#...#...#...#...#...#...#...#...#...#...

	#... Up and Down There must be both corner joint
	if PART == 'up':
		if corner_joint:
			mc.warning(f'Up is no need for corner joint. {corner_joint}')


	if PART == 'up':
		eyeCurve_skc = core.SkinCluster( joint_curve, crv_low, dropoffRate = 7 , maximumInfluences = 2 )
		eyeCurve_skc.name =  crv_low + '_skc'

	elif PART == 'down':
		joint_curve_down = list(joint_curve)+list(corner_joint) #... add corner joint
		eyeCurve_skc = core.SkinCluster( joint_curve_down, crv_low, dropoffRate = 7 , maximumInfluences = 2 )
		eyeCurve_skc.name =  crv_low + '_skc'

	
	part_dict['ctrl_grp'] = []



	if PART == 'up':
		print(joint_curve)
		ctrl_name = adjust.creControllerFunc( joint_curve, scale = ctrlSize, ctrlShape = crtlShape, color = color )
		part_dict['ctrl_grp'].append(ctrl_name)
		print(part_dict)

		
			


	elif PART == 'down':
		
		print('This is joint_curve >>> {0}'.format(joint_curve))
		filtered_joint_curve = [joint for joint in joint_curve if 'corner' not in joint]
		print('This is filtered_proxy_jointCurve >>> {0}'.format(filtered_joint_curve))
		print(filtered_joint_curve)
		
		ctrl_name = adjust.creControllerFunc( filtered_joint_curve, scale = ctrlSize, ctrlShape = crtlShape, color = color )
		part_dict['ctrl_grp'].append(ctrl_name)
		print(ctrl_name)


		


	

	#... Make group
	part_dict['curve_grp'] = []
	part_dict['curve_grp'] = crv_hi, crv_low ,base_wire_node

	#... Make this curve back to still grp
	# mc.parent(crv_hi, eyeLid_aimJnt_grp.name)


	part_dict['locator'] = []
	part_dict['locator'] = CENTER, upVec


	part_dict['joint_curve'] = []
	part_dict['joint_curve'] = joint_curve

	part_dict['joint_tip'] = []
	part_dict['joint_tip'] = tipJnt

	misc.makeHeader('{0} is complete'.format(__name__))
	EyeRigMarco.info('\n...EyeRig DONE Really')
	return part_dict

	#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...
	#... End of part 2 (make this to function and run two time for up and down)
	#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...



'''
eye_up_dict = createControlEye(		group_name = 'group1', 
									CENTER = 'L_center', SIDE = 'L',
									PART = 'up',
									crv_hi = 'L_upLidHigh_CRV',
									crv_low = 'L_upLidLow_CRV',
									crtlShape = 'plainSphereB_ctrlShape',
									ctrlSize = 0.01,
									proxy_jointCurve = ('L_eye01_jnt', 'L_eye02_jnt', 'L_eye03_jnt', 'L_eye07_jnt', 'L_eye08_jnt')
										)


eye_down_dict = createControlEye(		group_name = 'group2', 
									CENTER = 'L_center', SIDE = 'L',
									PART = 'down',
									crv_hi = 'L_downLidHigh_CRV',
									crv_low = 'L_downLidLow_CRV',
									crtlShape = 'plainSphereB_ctrlShape',
									ctrlSize = 0.01,
									proxy_jointCurve = ('L_eye04_jnt','L_eye05_jnt','L_eye06_jnt', 'L_eye07_jnt', 'L_eye08_jnt')	
									)




'''



#...#...#...#...#...#...
#... Start of part 2.5
#...#...#...#...#...#...

'''
# Make inbetween controller move following both corner and middle 
'''

def makeInbetweener(eye_up_dict, eye_down_dict):

	# # # # # # # #
	#... up part
	# # # # # # # #

	L_up_between_zro = eye_up_dict['ctrl_grp'][0][6] #... L_eye03Zro_grp
	up_middle_ctrl = eye_up_dict['ctrl_grp'][0][4] #... L_eye02_ctrl
	R_up_between_zro = eye_up_dict['ctrl_grp'][0][0] #... L_eye01Zro_grp
	L_corner_ctrl = eye_up_dict['ctrl_grp'][0][-2] #... L_eye08_ctrl
	R_corner_ctrl = eye_up_dict['ctrl_grp'][0][-5] #... L_eye07_ctrl

	#... make middle ctrl bigger
	up_middle_obj = core.Dag(up_middle_ctrl)
	up_middle_obj.scaleCurve(scale = 1.75)
	# mc.error('STOP')


	#... [pattern constraint] corner_ctrl and middle_ctrl ---> inbetween_zro
	constr_object = core.pointConstraint( L_corner_ctrl, up_middle_ctrl, L_up_between_zro, maintainOffset=True) 
	constr_object.name = L_up_between_zro + '_poiCon'
	constr_object = core.pointConstraint( R_corner_ctrl, up_middle_ctrl, R_up_between_zro, maintainOffset=True) 
	constr_object.name = R_up_between_zro + '_poiCon'




	# # # # # # # #
	#... down part
	# # # # # # # #

	down_middle_ctrl = eye_down_dict['ctrl_grp'][0][4] #...L_eye05_ctrl
	R_down_between_zro = eye_down_dict['ctrl_grp'][0][0] #... L_eye04Zro_grp
	L_down_between_zro = eye_down_dict['ctrl_grp'][0][6] #.... L_eye06Zro_grp

	#... make middle ctrl bigger
	down_middle_obj = core.Dag(down_middle_ctrl)
	down_middle_obj.scaleCurve(scale = 1.75)


	constr_object = core.pointConstraint( L_corner_ctrl, down_middle_ctrl, L_down_between_zro, maintainOffset=True) 
	constr_object.name = L_down_between_zro + '_poiCon'
	constr_object = core.pointConstraint( R_corner_ctrl, down_middle_ctrl, R_down_between_zro, maintainOffset=True) 
	constr_object.name = R_down_between_zro + '_poiCon'

	# EyeRigMarco.info('\n...EyeRig make Inbetweener DONE')
	misc.makeHeader('{0} is complete'.format(__name__))




'''
makeInbetweener(eye_up_dict = eye_up_dict, eye_down_dict = eye_down_dict)
'''




# # # # # # # #
#		Next step make blink
# # # # # # # #



from function.rigging.autoRig.base import core
reload(core)



def makeSmartBlink(
					SIDE = 'L'							,
					CURVE = 'CRV'						,
					up_low_crv = 'L_upLidLow_CRV'		,
					down_low_crv = 'L_downLidLow_CRV'	,
					up_hi_crv = 'L_upLidHigh_CRV'		,
					down_hi_crv = 'L_downLidHigh_CRV'	,
					up_attrAt = 'L_eye02_ctrl'				,
					down_attrAt = 'L_eye05_ctrl'				,
					color = 'red'
															):
	#... duplicate for make smart blink
	blendShape_upBlink_crv = core.duplicate(up_low_crv)
	blendShape_upBlink_crv.name = '{0}_lidBlink_master_CRV'.format(SIDE)


	blendShape_upBlink_crv.color = color


	#... create attr at broad ctrl for control blendshape
	middle_ctrl = core.Dag(up_attrAt)
	shapeName = core.shapeName(up_attrAt)
	middle_ctrlShape = core.Dag(shapeName)

	middle_ctrlShape.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink_heigh', keyable = True, defaultValue = 0   )
	middle_ctrlShape.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink', keyable = True, defaultValue = 0   )

	shapeName = core.shapeName(down_attrAt)
	middle_down_ctrlShape = core.Dag(shapeName)
	# middle_down_ctrlShape.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink_heigh', keyable = True, defaultValue = 0   )
	middle_down_ctrlShape.addAttribute( at = 'float'  , min = 0  , max = 1, longName = 'smart_Blink', keyable = True, defaultValue = 0   )


	smartBlink_bsh = mc.blendShape(up_low_crv, down_low_crv, blendShape_upBlink_crv.name, origin = 'world', name =  '{0}_targetSmartBlink_BSH'.format(SIDE))[0]
	mc.setAttr('{}.{}'.format(smartBlink_bsh,up_low_crv), 0)
	mc.setAttr('{}.{}'.format(smartBlink_bsh,down_low_crv), 0)
	#smartBlink_bsh = 	'L_targetSmartBlink_BSH'


	# #... duplicate up and down (this is original version)
	upBlink_crv = core.duplicate(up_hi_crv)
	upBlink_crv.name = '{}_{}LidBlink_{}'.format(SIDE, 'Up', CURVE)
	downBlink_crv = core.duplicate(down_hi_crv)
	downBlink_crv.name = '{}_{}LidBlink_{}'.format(SIDE, 'Down', CURVE)

	#... updarent to the world
	_unparent_if_not_world(upBlink_crv.name)
	_unparent_if_not_world(downBlink_crv.name)

	#... duplicate up and down
	# upBlink_crv = core.duplicate(up_low_crv)
	# upBlink_crv.name = '{}_{}LidBlink_follow_{}'.format(SIDE, 'Up', CURVE)
	# downBlink_crv = core.duplicate(down_low_crv)
	# downBlink_crv.name = '{}_{}LidBlink_follow_{}'.format(SIDE, 'Down', CURVE)


	#... make it follow smart blink curve
	#... [child][parent]
	up_wire = mc.wire(upBlink_crv.name, wire = blendShape_upBlink_crv.name , envelope=1, crossingEffect=0, localInfluence=0, name='{}_{}LidBlink_{}'.format(SIDE, 'Up', 'WR'), groupWithBase = False)[0]
	#mc.setAttr('L_UpLidBlink_WR.scale[0]', 0)
	new_upBlink_Name = blendShape_upBlink_crv.name + '_Up_BaseWire'
	mc.rename(blendShape_upBlink_crv.name + 'BaseWire', new_upBlink_Name)

	

	#... if down must fix value of BSH dow to 1 
	mc.setAttr('{}.{}'.format(smartBlink_bsh,down_low_crv), 1)
	mc.setAttr('{}.{}'.format(smartBlink_bsh,up_low_crv), 1)

	down_wire = mc.wire(downBlink_crv.name, wire = blendShape_upBlink_crv.name , envelope=1, crossingEffect=0, localInfluence=0, name='{}_{}LidBlink_{}'.format(SIDE, 'Down', 'WR'), groupWithBase = False)[0]
	mc.setAttr('{}.scale[0]'.format(down_wire), 0)
	new_downBlink_Name = blendShape_upBlink_crv.name + '_Down_BaseWire'
	mc.rename(blendShape_upBlink_crv.name + 'BaseWire', new_downBlink_Name)
	base_wire_Down_Blink_node = blendShape_upBlink_crv.name + '_BaseWire'




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
	mc.connectAttr('{}.smart_Blink'.format(middle_ctrlShape), '{}.{}'.format(upLidBlink_bsh, upBlink_crv.name), f=True)
	mc.connectAttr('{}.smart_Blink'.format(middle_down_ctrlShape), '{}.{}'.format(downLidBlink_bsh, downBlink_crv.name),f=True)

	#... link smart blink heigh
	rev_value = core.ReverseNam('{}_smartBlink_{}'.format(SIDE,'REV'))
	mc.connectAttr('{}.smart_Blink_heigh'.format(middle_ctrlShape), '{}.{}'.format(smartBlink_bsh, down_low_crv), f=True)
	mc.connectAttr('{}.smart_Blink_heigh'.format(middle_ctrlShape), '{}.inputX'.format(rev_value.name), f=True)
	mc.connectAttr('{}.outputX'.format(rev_value.name), '{}.{}'.format(smartBlink_bsh, up_low_crv), f=True)

	#... set intial value
	middle_ctrl.attr('smart_Blink_heigh').value = 0.8

	EyeRigMarco.info('{0} is DONE'.format(__name__))

	misc.makeHeader('{0} is complete'.format(__name__))

	return upBlink_crv.name, downBlink_crv.name, blendShape_upBlink_crv.name, new_upBlink_Name, new_downBlink_Name




#... arrange grp
def arrange_eye_grp(eye_up_dict, eye_down_dict, smartBlink, center_loc, SIDE):


	move_grp = core.Null(f'{SIDE}_eyeMover_grp')
	move_grp.snap(center_loc)


	# zro_grp = []
	# for index, value in enumerate(eye_dict['ctrl_grp'][0]):
	# 	if index % 3 == 0:
	# 		print(value)
	# 		zro_grp.append(value)
			
		
	zro_up_grp = [value for index, value in enumerate(eye_up_dict['ctrl_grp'][0]) if index % 3 == 0]
	zro_down_grp = [value for index, value in enumerate(eye_down_dict['ctrl_grp'][0]) if index % 3 == 0]

	eye_all_zro_grp = core.Null(f'{SIDE}_eyeZro_grp')
	eye_all_zro_grp.snap(move_grp)

	for each in zro_up_grp:
		mc.parent(each, eye_all_zro_grp)

	for each in zro_down_grp:
		mc.parent(each, eye_all_zro_grp)	
	
	
	eye_aim_grp = core.Null(f'{SIDE}_eyeAim_grp')
	eye_aim_grp.snap(move_grp)
	eye_aim_grp.parent(move_grp)

	print(['top_grp'][0])
	mc.parent(eye_up_dict['top_grp'][0], eye_aim_grp)
	mc.parent(eye_down_dict['top_grp'][0], eye_aim_grp)
	
	eye_all_zro_grp.parent(move_grp)

	print('END of part 1')


	curve_still_grp = core.Null(f'{SIDE}_eyeWireStill_grp')


	for idx, each in enumerate(eye_up_dict['curve_grp']):
		mc.parent(eye_up_dict['curve_grp'][idx], curve_still_grp.name)
		mc.parent(eye_down_dict['curve_grp'][idx], curve_still_grp.name)


	for each in smartBlink:
		mc.parent(each, curve_still_grp.name)

	mc.parent(eye_up_dict['top_grp'][2], curve_still_grp)
	mc.parent(eye_down_dict['top_grp'][2], curve_still_grp)


	loc_still_grp = core.Null(f'{SIDE}_eyeLocStill_grp')

	mc.parent(eye_up_dict['top_grp'][1], loc_still_grp)
	mc.parent(eye_down_dict['top_grp'][1], loc_still_grp)

	mc.select(deselect=True)
	misc.makeHeader('{0} is complete'.format(__name__))
	return eye_all_zro_grp, curve_still_grp, loc_still_grp






#... create bind joint 

from function.rigging.util import misc
reload(misc)

def cre_eye_bJnt(
	eye_up_dict, 
	eye_down_dict,
	SIDE = 'L',
	region = 'eyeCen',
	center_loc = 'L_center_loc',
	):

	#... create joint at center

	center_name = f'{SIDE}_{region}_bJnt'

	center_jnt = core.Joint(center_name, radius = 1, overrideEnabled = True, overrideColor = 1)
	center_jnt.snap(center_loc)

	for idx, each in enumerate(eye_up_dict['joint_tip']):
		print(each)
		newName = each.replace('_JNT','_bJnt')
		bind_jnt = core.Joint(newName, radius = 1, overrideEnabled = True, overrideColor = 1)
		bind_jnt.snap(each)
		bind_jnt.parent(center_jnt)


	for idx, each in enumerate(eye_down_dict['joint_tip'][1:-1]):
		print(each)
		newName = each.replace('_JNT','_bJnt')
		bind_jnt = core.Joint(newName, radius = 1, overrideEnabled = True, overrideColor = 1)
		# bind_jnt = core.Joint(f'{SIDE}_{PART}EyeLidTip{idx:02d}_bJnt', radius = 1, overrideEnabled = True, overrideColor = 1)
		bind_jnt.snap(each)
		bind_jnt.parent(center_jnt)

















'''
makeBlink(
					SIDE = 'L'							,
					CURVE = 'CRV'						,
					up_low_crv = 'L_upLidLow_CRV'		,
					down_low_crv = 'L_downLidLow_CRV'	,
					up_hi_crv = 'L_upLidHigh_CRV'		,
					down_hi_crv = 'L_downLidHigh_CRV'
															)


'''




'''




#... try to make controller follow eyelid still not work
from function.rigging.autoRig.base import core
reload(core)




sel = ['locator1','locator2', 'locator3' , 'locator4' , 'locator5']
sel = ['locator11','locator12', 'locator13']
crv_hi = 'L_DownLidBlink_follow_collective_CRV'
pos = []

for each in sel:	
	pos = mc.xform(each, q=True, ws=True, t=True)
	type(pos)
	type(crv_hi)
	uVal = core.getUParam(pos, crv_hi)
	name = each.replace('LOC', 'PCI')
	print(name)
	pci=mc.createNode('pointOnCurveInfo', name = name)
	mc.connectAttr(crv_hi + '.worldSpace', pci + '.inputCurve')
	mc.setAttr(pci+'.parameter', uVal)
	mc.connectAttr( pci + '.position', each + '.t')


'''