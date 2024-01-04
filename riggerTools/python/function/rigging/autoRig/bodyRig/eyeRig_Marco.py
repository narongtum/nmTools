#... [EYE RIG Marco Fashion]

import maya.cmds as mc
from maya import OpenMaya

from function.rigging.autoRig.base import core
reload(core)

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


def createControlEye(	group_name = 'group1', CENTER = 'L_center', SIDE = 'L',
						PART = 'up',
						crv_hi = 'L_upLidHigh_CRV',
						crv_low = 'L_upLidLow_CRV',
						crtlShape = 'plainSphereB_ctrlShape',
						ctrlSize = 0.01 ,
						color = 'yellow'	):



	objectsInGroup = mc.listRelatives(group_name, children=True)
	# Select all objects in the list.
	mc.select(objectsInGroup)
	loc = mc.ls(sl=True, fl=True)[0]

	#... ask part is upper or lower
	PART = loc.split('_')[0]




	#... The last 2 order is corner joint

	if PART == 'up':
		jointCurve = ['L_eye01_jnt', 'L_eye02_jnt', 'L_eye03_jnt', 'L_eye07_jnt', 'L_eye08_jnt']
	elif PART == 'down':
		jointCurve = ['L_eye04_jnt','L_eye05_jnt','L_eye06_jnt', 'L_eye07_jnt', 'L_eye08_jnt']

	upVec = 'L_eyeVec_LOC'


	#... select locator again
	vtx = mc.ls(sl=True, fl=True)




	mc.select(cl=True)
	grp = mc.group(empty=True, name = '{}_{}EyeLid_Jnt_GRP'.format(SIDE,PART))
	num = 1
	tipJnt = []
	for each in vtx:
		mc.select(cl=True)
		jnt = mc.joint(name = '{}_{}EyeLidTip{:02d}_{}'.format(SIDE, PART, num, 'JNT'))
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
		mc.aimConstraint(loc.name, par, mo=True, weight=1, aimVector=(1,0,0), upVector=(0,1,0), worldUpType='object', worldUpObject = upVec )
		aimLoc.append(loc.name)
		num = num + 1

		mc.parent(loc.name, grp)
	mc.select(cl=True)

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


	#...#...#...#...#...#...
	#... start of part 2
	#...#...#...#...#...#...

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
	mc.wire(crv_hi, wire = crv_low , envelope=1, crossingEffect=0, localInfluence=0, name=crv_low + '_WR', groupWithBase = False)


	#... skin joint to low curve
	eyeCurve_skc = core.SkinCluster( jointCurve, crv_low, dropoffRate = 7 , maximumInfluences = 2 )
	eyeCurve_skc.name =  crv_low + '_skc'


	#... create controller link to the joint
	from function.rigging.controllerBox import adjustController as adjust
	from function.framework.reloadWrapper import reloadWrapper as reload
	reload(adjust)



	# if part_dict:
	# 	up_dict = None
	# 	down_dict = None


	#... there are run two time first is up second is down
	try: #... ask if part_dict is exists before
		part_dict = {}
	except NameError:
		part_dict = {'up':[],'down':[]}

	if PART == 'up':
		part_dict[PART] = []
		# part_dict = {PART:[]}
		ctrl_name = adjust.creControllerFunc( jointCurve, scale = ctrlSize, ctrlShape = crtlShape, color = color )
		part_dict[PART].append(ctrl_name)


	elif PART == 'down':
		part_dict[PART] = []
		for each in jointCurve:
			if mc.objExists('{}.isCorner'.format(each)):
				continue
			else:
				ctrl_name = adjust.creControllerFunc( [each], scale = ctrlSize, ctrlShape = crtlShape, color = color )
				part_dict[PART].append(ctrl_name)

	print('DONE')

	return part_dict

	#...#...#...#...#...#...
	#... End of part 2 (make this to function and run two time for up and down)
	#...#...#...#...#...#...



eye_up_dict = createControlEye(		group_name = 'group1', 
									CENTER = 'L_center', SIDE = 'L',
									PART = 'up',
									crv_hi = 'L_upLidHigh_CRV',
									crv_low = 'L_upLidLow_CRV',
									crtlShape = 'plainSphereB_ctrlShape',
									ctrlSize = 0.01	)


eye_down_dict = createControlEye(		group_name = 'group2', 
									CENTER = 'L_center', SIDE = 'L',
									PART = 'down',
									crv_hi = 'L_downLidHigh_CRV',
									crv_low = 'L_downLidLow_CRV',
									crtlShape = 'plainSphereB_ctrlShape',
									ctrlSize = 0.01	)








#...#...#...#...#...#...
#... Start of part 2.5
#...#...#...#...#...#...

'''
# Make inbetween controller move following both corner and middle 
'''

import pprint
if len(part_dict['up']) >1:
	mc.error('length must be not more than one.')
	
pprint.pprint(part_dict['up'][0])
pprint.pprint(part_dict['down'])

# # # # # # # #
#... up part
# # # # # # # #
L_up_between_zro = part_dict['up'][0][6] # L_eye03Zro_grp
up_middle_ctrl = part_dict['up'][0][5] # L_eye02_gmbCtrl
R_up_between_zro = part_dict['up'][0][0] # L_eye01Zro_grp
L_corner_ctrl = part_dict['up'][0][-2] # L_eye08_ctrl
R_corner_ctrl = part_dict['up'][0][-5] # L_eye07_ctrl

#... [pattern constraint] corner_ctrl and middle_ctrl ---> inbetween_zro
constr_object = core.pointConstraint( L_corner_ctrl, up_middle_ctrl, L_up_between_zro, maintainOffset=True) 
constr_object.name = L_up_between_zro + '_poiCon'
constr_object = core.pointConstraint( R_corner_ctrl, up_middle_ctrl, R_up_between_zro, maintainOffset=True) 
constr_object.name = R_up_between_zro + '_poiCon'



# # # # # # # #
#... down part
# # # # # # # #


down_middle_ctrl = part_dict['down'][1][1]
R_down_between_zro = part_dict['down'][0][0]
L_down_between_zro = part_dict['down'][2][0]

constr_object = core.pointConstraint( L_corner_ctrl, down_middle_ctrl, L_down_between_zro, maintainOffset=True) 
constr_object.name = L_down_between_zro + '_poiCon'
constr_object = core.pointConstraint( R_corner_ctrl, down_middle_ctrl, R_down_between_zro, maintainOffset=True) 
constr_object.name = R_down_between_zro + '_poiCon'











# # # # # # # #
#		Next step
# # # # # # # #