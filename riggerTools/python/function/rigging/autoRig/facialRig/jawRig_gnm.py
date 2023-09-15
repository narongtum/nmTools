#...source >>> I:\Resource\Tutorial\Rigging The Jaw with Python in Maya\MyFile


import maya.cmds as mc
import sys

from function.rigging.autoRig.base import core
reload(core)


#... change joint to controller

# object constants
GROUP = 'GRP'
JOINT = 'JNT'
GUIDE = 'GUIDE'
JAW = 'jaw'
PROXY_JOINT = 'pxyJnt'
#... side constants
LEFT = 'L'
RIGHT = 'R'
CENTER = 'C'
jaw_attr = 'jaw_attributes'
CONTROLLER = 'ctrl'
ctrlShape = 'sphereB_ctrlShape'
charScale = 0.125

def addOffset(dst, suffix='OFF'):
	'''
	create zero group  
	'''

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
	'''
	create locator template guide  
	'''	
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
	'''
	return name template
	'''
	grp = '{}_lipMinor_{}_{}_{}'.format(CENTER, JAW, GUIDE, GROUP)
	guides = []
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
	'''
	create template group
	'''
	main_grp = mc.createNode('transform', name='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
	lip_grp = mc.createNode('transform', name='{}_{}Lip_{}'.format(CENTER, JAW, GROUP), parent=main_grp)
	base_grp = mc.createNode('transform', name='{}_{}Base_{}'.format(CENTER, JAW, GROUP), parent=main_grp)

	lip_minor_grp = mc.createNode('transform', name='{}_{}Rig_minor_{}'.format(CENTER, JAW, GROUP), parent=lip_grp)
	lip_broad_grp = mc.createNode('transform', name='{}_{}Rig_broad_{}'.format(CENTER, JAW, GROUP), parent=lip_grp)

	mc.select(cl=True)

#... change here
def createMinorJoints():
	'''
	04 create Main Structre minor joint
	create joint along locator
	'''

	minor_joints = []
	for guide in lip_guides():
		mat = mc.xform(guide, q=True, m=True, ws=True)
		# jnt = mc.joint(name = guide.replace(GUIDE, JOINT))
		jnt = mc.createNode('transform', name = guide.replace(GUIDE, JOINT))
		mc.setAttr('{}.displayHandle'.format(jnt), 1)

		# mc.setAttr('{}.radius'.format(jnt), 0.25)
		mc.xform(jnt, m=mat, ws=True)

		#... parent
		mc.parent(jnt, '{}_{}Rig_minor_{}'.format(CENTER, JAW, GROUP))

		minor_joints.append(jnt)
		
	return minor_joints


def createBroadJoints():
	upper_joint = mc.joint(name='{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT))
	mc.setAttr('{}.overrideEnabled'.format(upper_joint), 1)
	mc.setAttr('{}.overrideColor'.format(upper_joint), 18)
	mc.setAttr('{}.radius'.format(upper_joint), 4)
	mc.select(cl=True)
	lower_joint = mc.joint(name='{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT))
	mc.setAttr('{}.overrideEnabled'.format(lower_joint), 1)
	mc.setAttr('{}.overrideColor'.format(lower_joint), 18)
	mc.setAttr('{}.radius'.format(lower_joint), 4)
	mc.select(cl=True)
	left_joint = mc.joint(name='{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT))
	mc.setAttr('{}.overrideEnabled'.format(left_joint), 1)
	mc.setAttr('{}.overrideColor'.format(left_joint), 18)
	mc.setAttr('{}.radius'.format(left_joint), 4)
	mc.select(cl=True)
	right_joint = mc.joint(name='{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT))
	mc.setAttr('{}.overrideEnabled'.format(right_joint), 1)
	mc.setAttr('{}.overrideColor'.format(right_joint), 18)
	mc.setAttr('{}.radius'.format(right_joint), 4)
	mc.select(cl=True)

	#... parent joints under broad group
	mc.parent([upper_joint, lower_joint, left_joint,right_joint],'{}_{}Rig_broad_{}'.format(CENTER, JAW, GROUP))

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
	jaw_jnt = mc.joint(name='{}_{}_{}'.format(CENTER, JAW, PROXY_JOINT))
	jaw_inverse_jnt = mc.joint(name='{}_inverse_{}_{}'.format(CENTER, JAW, PROXY_JOINT))

	#... make it bigger
	mc.setAttr('{}.radius'.format(jaw_jnt), 2)
	mc.setAttr('{}.radius'.format(jaw_inverse_jnt), 2)
	
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

	C_upper = '{}_{}_broadUpper_{}'.format(CENTER, JAW, CONTROLLER)
	C_lower = '{}_{}_broadLower_{}'.format(CENTER, JAW, CONTROLLER)
	L_corner = '{}_{}_broadCorner_{}'.format(LEFT, JAW, CONTROLLER)
	R_corner = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, CONTROLLER)

	
	lip_joints = mc.listRelatives('{}_{}Lip_{}'.format(CENTER, JAW, GROUP), allDescendents=True)
	lookup = {	'C_upper':{}, 'C_lower':{},
				'L_upper':{}, 'L_lower':{},
				'R_upper':{}, 'R_lower':{},
				'L_corner':{}, 'R_corner':{}	}

	for joint in lip_joints:

		# if mc.objectType(joint) != 'joint':
		if mc.objectType(joint) != 'transform':
			continue

		if joint.startswith('C') and upper_token in joint: #... ask if any in 'common'
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



#.... 06 Create Seal And Jaw Attribute
def createSeal(part):
	'''
	crete constraint for seal 
	connect constraint to broad joint by distrubute weight 
	'''
	seal_name = '{}_seal_{}'.format(CENTER, GROUP)
	seal_parent = seal_name if mc.objExists(seal_name) else mc.createNode('transform', name = seal_name, parent='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
	part_grp = mc.createNode('transform', name=seal_name.replace('seal','seal_{}'.format(part)), parent=seal_parent)

	l_corner = '{}_{}_broadCorner_{}'.format(LEFT, JAW, CONTROLLER)
	r_corner = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, CONTROLLER)

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

#... END of part 1/3









def createJawAttrs():
	# node = mc.createNode('transform', name='jaw_attributes', parent='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
	jaw_attributes = core.Dag(jaw_attr)
	jaw_attributes.nmCreateController('gear_ctrlShape')
	node = jaw_attributes.name
	mc.addAttr(node, ln=sorted(getLipParts()['C_upper'].keys())[0], min=0, max=1, dv=0)
	
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

	createOffsetFollow(jaw_attr)
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



def createOffsetFollow(jaw_attr=''):
	
	jaw_joint = '{}_{}_{}'.format(CENTER, JAW, PROXY_JOINT)
	jaw_auto = '{}_{}_{}_AUTO'.format(CENTER, JAW, PROXY_JOINT)

	#.. add follow attrbutes
	mc.addAttr(jaw_attr, ln='follow_ty', min=-10, max=10, dv=0)
	mc.addAttr(jaw_attr, ln='follow_tz', min=-10, max=10, dv=0)

	unit = mc.createNode('unitConversion', name = '{}_{}_follow_UNIT'.format(CENTER, JAW))

	remap_y = mc.createNode('remapValue', name='{}_{}_followY_REMAP'.format(CENTER, JAW))
	mc.setAttr('{}.inputMax'.format(remap_y), 1)

	remap_z = mc.createNode('remapValue', name='{}_{}_followZ_REMAP'.format(CENTER, JAW))
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
	jaw_attr = 'jaw_attributes'
	mc.addAttr(jaw_attr, at='double', ln='L_seal', min=0, max=10, dv=0 )
	mc.addAttr(jaw_attr, at='double', ln='R_seal', min=0, max=10, dv=0 )

	mc.addAttr(jaw_attr, at='double', ln='L_seal_delay', min=0, max=10, dv=4 )
	mc.addAttr(jaw_attr, at='double', ln='R_seal_delay', min=0, max=10, dv=4 )

#... END of part 2/3












def connectSeal(part):

	seal_token = 'seal_{}'.format(part)

	jaw_attrs = 'jaw_attributes'

	lip_jnts = lipPart(part)

	value = len(lip_jnts)
	seal_driver = mc.createNode('lightInfo', name='C_{}_DRV'.format(seal_token))

	triggers = {'L': [], 'R':[]}

	for side in 'LR':
		#... get falloff
		delay_sub_name = '{}_{}_delay_SUB'.format(side, seal_token) 							
		delay_sub = mc.createNode('plusMinusAverage', name= delay_sub_name) 					

		mc.setAttr('{}.operation'.format(delay_sub), 2)											
		mc.setAttr('{}.input1D[0]'.format(delay_sub), 10)										
		mc.connectAttr('{}.{}_seal_delay'.format(jaw_attrs, side), '{}.input1D[1]'.format(delay_sub))	#.... link value from jaw_attrs grp

		lerp = 1 / float(value-1)	

		delay_div_name = '{}_{}_delay_DIV'.format(side, seal_token)						
		delay_div = mc.createNode('multDoubleLinear', name = delay_div_name)			
		mc.setAttr('{}.input2'.format(delay_div), lerp)	
		mc.connectAttr('{}.output1D'.format(delay_sub), '{}.input1'.format(delay_div))	

		mult_triggers = []	
		sub_triggers = []	
		triggers[side].append(mult_triggers)	
		triggers[side].append(sub_triggers)		

		for index in range(value):
			index_name = 'jaw_{:02d}'.format(index)

			#... create MULT node
			delay_mult_name = '{}_{}_{}_delay_MULT'.format(index_name, side, seal_token)		
			delay_mult = mc.createNode('multDoubleLinear', name=delay_mult_name)				
			mc.setAttr('{}.input1'.format(delay_mult), index)									
			mc.connectAttr('{}.output'.format(delay_div), '{}.input2'.format(delay_mult))		

			mult_triggers.append(delay_mult)													

			#... create SUB node
			delay_sub_name = '{}_{}_{}_delay_SUB'.format(index_name, side, seal_token)			
			delay_sub = mc.createNode('plusMinusAverage', name=delay_sub_name)					
			mc.connectAttr('{}.output'.format(delay_mult), '{}.input1D[0]'.format(delay_sub))			
			mc.connectAttr('{}.{}_seal_delay'.format(jaw_attrs, side), '{}.input1D[1]'.format(delay_sub))		

			sub_triggers.append(delay_sub)														

			# 09_[12:55]
			
	num_spans = value #... not sure num_spans is


	#... store psCons name
	const_targets = [] 
	for jnt in lip_jnts: 
		attrs=mc.listAttr('{}_parentConstraint1'.format(jnt), ud=True) 
		for attr in attrs: 
			if 'SEAL' in attr: 
				const_targets.append('{}_parentConstraint1.{}'.format(jnt, attr)) 


	#... beyond this is very complex
	#... connect seal trigger to driver node
	for left_index, const_target in enumerate(const_targets):	
		right_index = num_spans - left_index -1					
		index_name = '{}_{}'.format(seal_token, left_index)


		#... store value to dict [0] is MULT, [1] is SUB
		l_mult_trigger, l_sub_trigger = triggers['L'][0][left_index], triggers['L'][1][left_index]		
		r_mult_trigger, r_sub_trigger = triggers['R'][0][right_index], triggers['R'][1][right_index]	


		#... LFET
		l_remap_name = 'L_{}_{}_REMAP'.format(seal_token, index_name)						
		l_remap = mc.createNode('remapValue', name = l_remap_name)							
		mc.setAttr('{}.outputMax'.format(l_remap), 1)										
		mc.setAttr('{}.value[0].value_Interp'.format(l_remap), 2)							

		mc.connectAttr('{}.output'.format(l_mult_trigger), '{}.inputMin'.format(l_remap))			
		mc.connectAttr('{}.output1D'.format(l_sub_trigger), '{}.inputMax'.format(l_remap))			

		#... connect left seal attribure to input of remap
		mc.connectAttr('{}.L_seal'.format(jaw_attrs), '{}.inputValue'.format(l_remap))		

		#... RIGHT
		# substract 1 minus result from left remap

		r_sub_name = 'R_{}_offset_{}_SUB'.format(seal_token, index_name)	
		r_sub = mc.createNode('plusMinusAverage', name=r_sub_name)			
		mc.setAttr('{}.input1D[0]'.format(r_sub), 1)						
		mc.setAttr('{}.operation'.format(r_sub), 2)							

		mc.connectAttr('{}.outValue'.format(l_remap), '{}.input1D[1]'.format(r_sub))	#...change [0] to [1]

		r_remap_name = 'R_{}_{}_REMAP'.format(seal_token, index_name)				
		r_remap = mc.createNode('remapValue', name = r_remap_name)					
		mc.setAttr('{}.outputMax'.format(r_remap), 1) 								
		mc.setAttr('{}.value[0].value_Interp'.format(r_remap), 2)					

		mc.connectAttr('{}.output'.format(r_mult_trigger), '{}.inputMin'.format(r_remap))	
		mc.connectAttr('{}.output1D'.format(r_sub_trigger), '{}.inputMax'.format(r_remap))	

		#... connect left seal attribure to input of remap
		mc.connectAttr('{}.R_seal'.format(jaw_attrs), '{}.inputValue'.format(r_remap)) 
		
		mc.connectAttr('{}.output1D'.format(r_sub), '{}.outputMax'.format(r_remap))# if remove this line the R_zip will work
		# mc.connectAttr('{}.output1D'.format(r_sub), '{}.inputMin'.format(r_remap))
		print('{}.output1D'.format(r_sub), '{}.outputMax'.format(r_remap))



		#... final addition for both side
		plus_name = '{}_SUM'.format(index_name)
		plus = mc.createNode('plusMinusAverage', name=plus_name)

		mc.connectAttr('{}.outValue'.format(l_remap), '{}.input1D[0]'.format(plus))
		mc.connectAttr('{}.outValue'.format(r_remap), '{}.input1D[1]'.format(plus))

		clamp_name = '{}_CLAMP'.format(index_name)
		clamp = mc.createNode('remapValue', name=clamp_name)
		mc.connectAttr('{}.output1D'.format(plus), '{}.inputValue'.format(clamp))

		mc.addAttr(seal_driver, at='double', ln=index_name, min=0, max=1, dv=0)
		mc.connectAttr('{}.outValue'.format(clamp), '{}.{}'.format(seal_driver, index_name))

		mc.connectAttr('{}.{}'.format(seal_driver, index_name), const_target)
		print('End of function')
		# 09_[30:00]




def createJawPin():
	pin_driver = mc.createNode('lightInfo', name='{}_pin_DRV'.format(CENTER))
	jaw_attr = 'jaw_attributes'

	for side in 'LR':
		

		mc.addAttr(jaw_attr, at='bool', ln='{}_auto_corner_pin'.format(side))
		mc.addAttr(jaw_attr, at='double', ln='{}_corner_pin'.format(side), min=-10, max=10, dv=0)
		mc.addAttr(jaw_attr, at='double', ln='{}_input_ty'.format(side), min=-10, max=10, dv=0)

		#... create clamp and connect the input_ty
		clamp = mc.createNode('clamp', name='{}_corner_pin_auto_CLAMP'.format(side))
		mc.setAttr('{}.minR'.format(clamp), -10)
		mc.setAttr('{}.maxR'.format(clamp), 10)

		mc.connectAttr('{}.{}_input_ty'.format(jaw_attr, side), '{}.inputR'.format(clamp))

		#... create the condition for the two sernario
		cnd = mc.createNode('condition', name='{}_corner_pin_auto_CND'.format(side))
		mc.setAttr('{}.operation'.format(cnd), 0)
		mc.setAttr('{}.secondTerm'.format(cnd), 1)

		mc.connectAttr('{}.{}_auto_corner_pin'.format(jaw_attr, side), '{}.firstTerm'.format(cnd))
		mc.connectAttr('{}.outputR'.format(clamp), '{}.colorIfTrueR'.format(cnd))
		mc.connectAttr('{}.{}_corner_pin'.format(jaw_attr, side), '{}.colorIfFalseR'.format(cnd))

		#... create addtion
		plus = mc.createNode('plusMinusAverage', name='{}_corner_pin_auto_PLUS'.format(side))
		mc.setAttr('{}.input1D[1]'.format(plus), 10)
		mc.connectAttr('{}.outColorR'.format(cnd), '{}.input1D[0]'.format(plus))

		#... create division
		div = mc.createNode('multDoubleLinear', name='{}_corner_pin_DIV'.format(side))
		mc.setAttr('{}.input2'.format(div), 0.05)
		mc.connectAttr('{}.output1D'.format(plus), '{}.input1'.format(div))

		#... add final attributes to the driver node
		mc.addAttr(pin_driver, at='double', ln='{}_pin'.format(side), min=0, max=1, dv=0)
		mc.connectAttr('{}.output'.format(div), '{}.{}_pin'.format(pin_driver, side))
		# [10_18:00]

		#... connect driver to broad joint constraint targets
		const_pin_up = '{}_jaw_broadCorner_JNT_OFF_parentConstraint1.C_jaw_broadUpper_JNT_OFFW0'.format(side)
		const_pin_down = '{}_jaw_broadCorner_JNT_OFF_parentConstraint1.C_jaw_broadLower_JNT_OFFW1'.format(side)

		mc.connectAttr('{}.{}_pin'.format(pin_driver, side), const_pin_up)

		rev = mc.createNode('reverse', name='{}_corner_pin_REV'.format(side))
		mc.connectAttr('{}.{}_pin'.format(pin_driver, side), '{}.inputX'.format(rev))
		mc.connectAttr('{}.outputX'.format(rev), const_pin_down)
#... END of part 3/3



