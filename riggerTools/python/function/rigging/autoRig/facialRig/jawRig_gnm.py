#... explain seal mouth 08_16:47

import maya.cmds as mc
import sys

# object constants
GROUP = 'GRP'
JOINT = 'JNT'
GUIDE = 'GUIDE'
JAW = 'jaw'

#... side constants
LEFT = 'L'
RIGHT = 'R'
CENTER = 'C'

#... zero group
def addOffset(dst, suffix='OFF'):

	print('got name: {0}'.format(dst))

	grp_offset = mc.createNode('transform', name='{}_{}'.format(dst, suffix))
	dst_mat = mc.xform(dst, q=True, m=True, ws=True)
	mc.xform(grp_offset, m=dst_mat, ws=True)

	dst_parent = mc.listRelatives(dst, parent=True)
	if dst_parent:
		mc.parent(grp_offset, dst_parent)

	mc.parent(dst, grp_offset)
	return grp_offset


def createGuides(number=5):
	jaw_guide_grp = mc.createNode('transform', name='{}_{}_{}_{}'.format(CENTER, JAW, GUIDE, GROUP))
	locs_grp = mc.createNode('transform', name='{}_{}_lip_{}_{}'.format(CENTER, JAW, GUIDE, GROUP), parent=jaw_guide_grp)

	lip_locs_grp = mc.createNode('transform', name='{}_lipMinor_{}_{}_{}'.format(CENTER, JAW, GUIDE, GROUP), parent=locs_grp)

	# ... create locators
	for part in ['Upper', 'Lower']:
		part_mult = 1 if part == 'Upper' else -1
		mid_data = (0, part_mult, 0)

		mid_loc = mc.spaceLocator(name='{}_{}{}_lip_{}'.format(CENTER, JAW, part, GUIDE))[0]
		mc.parent(mid_loc, lip_locs_grp)

		# Print the locator name for debugging
		print("mid_loc:", mid_loc)

		for side in 'LR':
			for x in range(number):
				multplier = x + 1 if side == 'L' else -(x + 1)
				loc_data = (multplier, part_mult, 0)
				loc = mc.spaceLocator(name='{}_{}{}_lip_{:02d}_{}'.format(side, JAW, part, x + 1, GUIDE))[0]
				mc.parent(loc, lip_locs_grp)

				# ... set data
				mc.setAttr('{}.t'.format(loc), *loc_data)

		# ... set center data
		mc.setAttr('{}.t'.format(mid_loc), *mid_data)


	#... create corners
	left_corner_loc = mc.spaceLocator(name = '{}_{}Corner_lip_{}'.format(LEFT, JAW, GUIDE))[0]
	right_corner_loc = mc.spaceLocator(name = '{}_{}Corner_lip_{}'.format(RIGHT, JAW, GUIDE))[0]

	mc.parent(left_corner_loc, lip_locs_grp)
	mc.parent(right_corner_loc, lip_locs_grp)

	mc.setAttr('{}.t'.format(left_corner_loc), *(number+1, 0, 0))
	mc.setAttr('{}.t'.format(right_corner_loc), *(-(number+1), 0, 0))

	mc.select(cl=True)

	#... create jaw base
	jaw_base_guide_grp = mc.createNode('transform', name='{}_{}_base_{}_{}'.format(CENTER, JAW, GUIDE, GROUP),
		parent = jaw_guide_grp)
	jaw_guide = mc.spaceLocator(name = '{}_{}_{}'.format(CENTER , JAW, GUIDE))[0]
	jaw_inverse_guide = mc.spaceLocator(name = '{}_{}_inverse_{}'.format(CENTER , JAW, GUIDE))[0]

	mc.setAttr('{}.t'.format(jaw_guide), *(0, -1, -number))
	mc.setAttr('{}.t'.format(jaw_inverse_guide), *(0, 1, -number))

	mc.parent(jaw_guide, jaw_base_guide_grp)
	mc.parent(jaw_inverse_guide, jaw_base_guide_grp)

	mc.select(cl=True)


def lip_guides():
	grp = '{}_lipMinor_{}_{}_{}'.format(CENTER, JAW, GUIDE, GROUP)
	guides = list()
	#guides = [loc for loc in mc.listRelatives(grp) if mc.objExists(grp)]
	if mc.objExists(grp):
		for loc in mc.listRelatives(grp):
			guides.append(loc)
	return guides



def jaw_guides():
	grp = '{}_{}_base_{}_{}'.format(CENTER, JAW, GUIDE, GROUP)
	return [loc for loc in mc.listRelatives(grp) if mc.objExists(grp)]

def build():#... collection of function
	createGuides()
	createHierarchy()
	createMinorJoints()
	createBroadJoints()
	createJawBase()
	constraintBroadJoints()


def createHierarchy():
	# create template group
	main_grp = mc.createNode('transform', name='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
	lip_grp = mc.createNode('transform', name='{}_{}Lip_{}'.format(CENTER, JAW, GROUP), parent=main_grp)
	base_grp = mc.createNode('transform', name='{}_{}Base_{}'.format(CENTER, JAW, GROUP), parent=main_grp)

	lip_minor_grp = mc.createNode('transform', name='{}_{}Lig_minor_{}'.format(CENTER, JAW, GROUP), parent=lip_grp)
	lip_broad_grp = mc.createNode('transform', name='{}_{}Lig_broad_{}'.format(CENTER, JAW, GROUP), parent=lip_grp)

	mc.select(cl=True)

# 04 Main Structre
#... create minor joint
def createMinorJoints():
	#... create joint along locator
	minor_joints = list()
	for guide in lip_guides():
		mat = mc.xform(guide, q=True, m=True, ws=True)
		jnt = mc.joint(name = guide.replace(GUIDE, JOINT))
		mc.setAttr('{}.radius'.format(jnt), 0.5)
		mc.xform(jnt, m=mat, ws=True)

		#... parent
		mc.parent(jnt, '{}_{}Lig_minor_{}'.format(CENTER, JAW, GROUP))

		minor_joints.append(jnt)
		
	return minor_joints


def createBroadJoints():
	upper_joint = mc.joint(name='{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT))
	mc.select(cl=True)
	lower_joint = mc.joint(name='{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT))
	mc.select(cl=True)
	left_joint = mc.joint(name='{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT))
	mc.select(cl=True)
	right_joint = mc.joint(name='{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT))
	mc.select(cl=True)

	#... parent joints under broad group
	mc.parent([upper_joint, lower_joint, left_joint,right_joint],'{}_{}Lig_broad_{}'.format(CENTER, JAW, GROUP))

	#... retrieve guide position
	upper_pos = mc.xform('{}_{}Upper_lip_{}'.format(CENTER, JAW,  GUIDE), q=True, m=True, ws=True)
	lower_pos = mc.xform('{}_{}Lower_lip_{}'.format(CENTER, JAW, GUIDE), q=True, m=True, ws=True)
	left_pos = mc.xform('{}_{}Corner_lip_{}'.format(LEFT, JAW, GUIDE), q=True, m=True, ws=True)
	right_pos = mc.xform('{}_{}Corner_lip_{}'.format(RIGHT, JAW, GUIDE), q=True, m=True, ws=True)

	#... set guide position
	mc.xform(upper_joint, m = upper_pos )
	mc.xform(lower_joint, m = lower_pos )
	mc.xform(left_joint, m = left_pos )
	mc.xform(right_joint, m = right_pos )

	mc.select(cl=True)


def createJawBase():
	jaw_jnt = mc.joint(name='{}_{}_{}'.format(CENTER, JAW, JOINT))
	jaw_inverse_jnt = mc.joint(name='{}_inverse_{}_{}'.format(CENTER, JAW, JOINT))

	jaw_mat = mc.xform(jaw_guides()[0], q=True, m=True, ws=True)
	jaw_inverse_mat = mc.xform(jaw_guides()[1], q=True, m=True, ws=True)

	print(jaw_mat)

	mc.xform(jaw_jnt ,m=jaw_mat, ws=True)
	mc.xform(jaw_inverse_jnt, m=jaw_inverse_mat, ws=True)

	mc.parent(jaw_jnt, '{}_{}Base_{}'.format(CENTER, JAW, GROUP))
	mc.parent(jaw_inverse_jnt, '{}_{}Base_{}'.format(CENTER, JAW, GROUP))
	mc.select(cl=True)
	#chapter4, 29:30
	print(jaw_jnt)
	addOffset(jaw_jnt, suffix='OFF')
	print(jaw_inverse_jnt)
	addOffset(jaw_inverse_jnt, suffix='OFF')
	mc.select(cl=True)

	addOffset(jaw_jnt, suffix='AUTO')
	addOffset(jaw_inverse_jnt, suffix='AUTO')

	print('error mai')





#... 05 Main Connections And Acces Methods (Start)

def constraintBroadJoints():
	jaw_jnt = '{}_{}_{}'.format(CENTER, JAW, JOINT)
	inverse_jaw_jnt = '{}_inverse_{}_{}'.format(CENTER, JAW, JOINT) 

	broad_upper = '{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT)
	broad_lower = '{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT)
	broad_left = '{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT)
	broad_right = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT)

	# add offsets to broad joints
	upper_off = addOffset(broad_upper)
	lower_off = addOffset(broad_lower)
	left_off = addOffset(broad_left)	
	right_off = addOffset(broad_right)	

	#... Create constraints to upper and lower to jaw joint
	print('\nthis is lower_off: {}'.format(lower_off))
	mc.parentConstraint(jaw_jnt, lower_off, mo=True) 
	mc.parentConstraint(inverse_jaw_jnt, upper_off, mo=True) 

	#... Create constraints to corners
	print('\nthis is left_off: {}'.format(left_off))
	mc.parentConstraint(upper_off, lower_off, left_off, mo=True) 
	mc.parentConstraint(upper_off, lower_off, right_off, mo=True)
	# sys.exit()
	mc.select(cl=True)
	# 7:35

def getLipParts():
	upper_token = '{0}Upper'.format(JAW)
	lower_token = '{0}Lower'.format(JAW)
	corner_token = '{0}Corner'.format(JAW)

	C_upper = '{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT)
	C_lower = '{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT)
	L_corner = '{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT)
	R_corner = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT)

	
	lip_joints = mc.listRelatives('{}_{}Lip_{}'.format(CENTER, JAW, GROUP), allDescendents=True)
	lookup = {	'C_upper':{}, 'C_lower':{},
				'L_upper':{}, 'L_lower':{},
				'R_upper':{}, 'R_lower':{},
				'L_corner':{}, 'R_corner':{}	}

	for joint in lip_joints:

		if mc.objectType(joint) != 'joint':
			continue

		if joint.startswith('C') and upper_token in joint:
			lookup['C_upper'][joint] = [C_upper]

		if joint.startswith('C') and lower_token in joint:
			lookup['C_lower'][joint] = [C_lower]

		if joint.startswith('L') and upper_token in joint:
			lookup['L_upper'][joint] = [C_upper, L_corner]

		if joint.startswith('L') and lower_token in joint:
			lookup['L_lower'][joint] = [C_lower, L_corner]	

		if joint.startswith('R') and upper_token in joint:
			lookup['R_upper'][joint] = [C_upper, R_corner]	

		if joint.startswith('R') and lower_token in joint:
			lookup['R_lower'][joint] = [C_lower, R_corner]	

		if joint.startswith('L') and corner_token in joint:
			lookup['L_corner'][joint] = [L_corner]

		if joint.startswith('R') and corner_token in joint:
			lookup['R_corner'][joint] = [R_corner]
			
	print(lookup)
	return lookup

def lipPart(part):
	lip_parts = [reversed(	sorted(getLipParts()['L_{}'.format(part)].keys())	), 
							sorted(getLipParts()['C_{}'.format(part)].keys())	,
							sorted(getLipParts()['R_{}'.format(part)].keys())		]
	#... make into list
	return [joint for joint in lip_parts for joint in joint]
	#... End of chaper 04


# def lipPart(part):
#     lookup = getLipParts()
#     print(lookup)  # Add this line to see the dictionary
#     lip_parts = [reversed(sorted(lookup['{}_{}'.format(side, part)].keys())) for side in [CENTER, LEFT, RIGHT]]
#     return [joint for joint_list in lip_parts for joint in joint_list]




#.... 06 Create Seal And Jaw Attribute
def createSeal(part):
	seal_name = '{}_seal_{}'.format(CENTER, GROUP)
	seal_parent = seal_name if mc.objExists(seal_name) else mc.createNode('transform', name = seal_name, parent='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
	part_grp = mc.createNode('transform', name=seal_name.replace('seal','seal_{}'.format(part)), parent=seal_parent)

	l_corner = '{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT)
	r_corner = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT)

	value = len(lipPart(part))

	for index, joint in enumerate(lipPart(part)):
		node = mc.createNode('transform', name = joint.replace('JNT', '{}_SEAL'.format(part)), parent=part_grp)
		print('This is node: {}\n'.format(node))
		mat = mc.xform(joint, q=True, m=True, ws=True)
		mc.xform(node, m=mat, ws=True)

		print (l_corner)
		print (r_corner)
		print (node)
		
		constraint = mc.parentConstraint(l_corner, r_corner, node, mo=True)[0]
		print (constraint)
		
		# exit(1)
		mc.setAttr('{}.interpType'.format(constraint), 2)
		l_corner_value = 0
		r_corner_value = float(index) / float(value-1)
		l_corner_value = 1 - r_corner_value

		l_corner_attr = '{}.{}W0'.format(constraint, l_corner)
		r_corner_attr = '{}.{}W1'.format(constraint, r_corner)

		mc.setAttr(l_corner_attr, l_corner_value)
		mc.setAttr(r_corner_attr, r_corner_value)

	mc.select(cl=True)


def createJawAttrs():
	node = mc.createNode('transform', name='jaw_attributes', parent='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
	mc.addAttr(node, ln=sorted(getLipParts()['C_upper'].keys())[0], min=0, max=1, dv=0)
	print('yeah')
	# exit(1)
	mc.setAttr('{}.{}'.format(node, sorted(getLipParts()['C_upper'].keys())[0]), lock=1)

	for upper in sorted(getLipParts()['L_upper'].keys()):
		mc.addAttr(node, ln=upper, min=0, max=1, dv=0)

	mc.addAttr(node, ln=sorted(getLipParts()['L_corner'].keys())[0], min=0, max=1, dv=1)
	mc.setAttr('{}.{}'.format(node, sorted(getLipParts()['L_corner'].keys())[0]), lock=1)

	for lower in sorted(getLipParts()['L_lower'].keys())[::-1]:
		mc.addAttr(node, ln=lower, min=0, max=1, dv=0)

	mc.addAttr(node, ln=sorted(getLipParts()['C_lower'].keys())[0], min=0, max=1, dv=0)
	mc.setAttr('{}.{}'.format(node, sorted(getLipParts()['C_lower'].keys())[0]), lock=1)

	createOffsetFollow()
	addSealAttr()


# 07 Minor Connections And Initial Values



#... Make weight attibure
def createConstraints():
	for value in getLipParts().values():
		for lip_jnt, broad_jnt in value.items():

			seal_token = 'upper_SEAL' if 'Upper' in lip_jnt else 'lower_SEAL'
			lip_seal = lip_jnt.replace(JOINT, seal_token)

			if mc.objExists(lip_seal):
				# print('This is broad_jnt: {}\nThis is lip_seal:{}'.format(broad_jnt, lip_seal))
				const = mc.parentConstraint(broad_jnt, lip_seal, lip_jnt, mo=True)[0]
				mc.setAttr('{}.interpType'.format(const), 2)
				# print('This is const: {}'.format(const))

				if len(broad_jnt) ==1:
					# print('This is seal_attr: {}'.format(seal_attr))
					seal_attr = '{}_parentConstraint1.{}W1'.format(lip_jnt, lip_seal)
					rev = mc.createNode('reverse', name=lip_jnt.replace(JOINT, 'REV'))
					mc.connectAttr(seal_attr, '{}.inputX'.format(rev))
					print('This is lip_jnt: {}\nThis is broad_jnt:{}'.format(lip_jnt, broad_jnt))
					mc.connectAttr('{}.outputX'.format(rev), '{}_parentConstraint1.{}W0'.format(lip_jnt, broad_jnt[0]))
					mc.setAttr(seal_attr, 0)

				if len(broad_jnt) == 2:
					seal_attr = '{}_parentConstraint1.{}W2'.format(lip_jnt, lip_seal)
					mc.setAttr(seal_attr, 0)

					seal_rev = mc.createNode('reverse', name=lip_jnt.replace('JNT', 'seal_REV'))
					jaw_attr_rev = mc.createNode('reverse', name=lip_jnt.replace('JNT', 'jaw_attr_REV'))
					seal_mult = mc.createNode('multiplyDivide', name=lip_jnt.replace('JNT', 'seal_MULT'))

					mc.connectAttr(seal_attr, '{}.inputX'.format(seal_rev))
					mc.connectAttr('{}.outputX'.format(seal_rev), '{}.input2X'.format(seal_mult))
					mc.connectAttr('{}.outputX'.format(seal_rev), '{}.input2Y'.format(seal_mult))

					mc.connectAttr(	'jaw_attributes.{}'.format(lip_jnt.replace(lip_jnt[0], 'L')),
									'{}.input1Y'.format(seal_mult))

					mc.connectAttr(	'jaw_attributes.{}'.format(lip_jnt.replace(lip_jnt[0], 'L')),
									'{}.inputX'.format(jaw_attr_rev))

					mc.connectAttr(	'{}.outputX'.format(jaw_attr_rev),
									'{}.input1X'.format(seal_mult))

					mc.connectAttr(	'{}.outputX'.format(seal_mult),
									'{}_parentConstraint1.{}W0'.format(lip_jnt, broad_jnt[0]))

					mc.connectAttr(	'{}.outputY'.format(seal_mult),
									'{}_parentConstraint1.{}W1'.format(lip_jnt, broad_jnt[1]))
			else:
				# print('This is broad_jnt: {}'.format(broad_jnt))
				const = mc.parentConstraint(broad_jnt, lip_jnt, mo=True)[0]
				mc.setAttr('{}.interpType'.format(const), 2)

				#... 07 Minor Connections And Initial Values(20:40)




def createIntialValues(part, degree=1.3):
	jaw_attr = [part for part in lipPart(part) if not part.startswith('C') and not part.startswith('R') ]
	value = len(jaw_attr)


	for index, attr_name in enumerate(jaw_attr[::-1]):
		attr = 'jaw_attributes.{}'.format(attr_name)

		linear_value = float(index) / float(value-1)

		

		div_value = linear_value / degree
		final_value = div_value * linear_value

		mc.setAttr(attr, final_value)

#... END of 07 Minor Connections And Initial Values



#... START of 08 Connect Seal Part 1
def createOffsetFollow():
	jaw_attr = 'jaw_attributes'
	jaw_joint = '{}_{}_{}'.format(CENTER, JAW, JOINT)
	jaw_auto = '{}_{}_{}_AUTO'.format(CENTER, JAW, JOINT)

	#.. add follow attrbutes
	mc.addAttr(jaw_attr, ln='follow_ty', min=-10, max=10, dv=0)
	mc.addAttr(jaw_attr, ln='follow_tz', min=-10, max=10, dv=0)

	unit = mc.createNode('unitConversion', name = '{}_{}_follow_UNIT'.format(CENTER, JAW))

	remap_y = mc.createNode('remapValue', name='{}_{}_followY_REMAP'.format(CENTER, JAW))
	mc.setAttr('{}.inputMax'.format(remap_y), 1)

	remap_z = mc.createNode('remapValue', name='{}_{}_followY_REMAP'.format(CENTER, JAW))
	mc.setAttr('{}.inputMax'.format(remap_z), 1)

	mult_y = mc.createNode('multDoubleLinear', name='{}_{}_follow_MULT'.format(CENTER, JAW))
	mc.setAttr('{}.input2'.format(mult_y), -1)

	mc.connectAttr('{}.rx'.format(jaw_joint), '{}.input'.format(unit))
	mc.connectAttr('{}.output'.format(unit), '{}.inputValue'.format(remap_y))
	mc.connectAttr('{}.output'.format(unit), '{}.inputValue'.format(remap_z))

	mc.connectAttr('{}.follow_ty'.format(jaw_attr), '{}.input1'.format(mult_y))
	mc.connectAttr('{}.follow_tz'.format(jaw_attr), '{}.outputMax'.format(remap_z))
	mc.connectAttr('{}.output'.format(mult_y), '{}.outputMax'.format(remap_y))

	mc.connectAttr('{}.outValue'.format(remap_y), '{}.ty'.format(jaw_auto))
	mc.connectAttr('{}.outValue'.format(remap_z), '{}.tz'.format(jaw_auto))

#... create seal feature
def addSealAttr():
	mc.addAttr(jaw_attr, at='double', ln='L_seal', min=0, max=10, dv=0 )
	mc.addAttr(jaw_attr, at='double', ln='R_seal', min=0, max=10, dv=0 )

	mc.addAttr(jaw_attr, at='double', ln='L_seal_delay', min=0, max=10, dv=4 )
	mc.addAttr(jaw_attr, at='double', ln='R_seal_delay', min=0, max=10, dv=4 )

# Call the function to create guides with default values
#createGuides()
#lip_guides()
#jaw_guides()

#... create template
createGuides(number=9)

createHierarchy()
createMinorJoints()
createBroadJoints()
createJawBase()
constraintBroadJoints()
createSeal('lower')
createSeal('upper')
createJawAttrs()
createConstraints()
createIntialValues('upper')
createIntialValues('lower')

#... set intial value for make smooth shape
#... get all the Left part

