import maya.cmds as mc
from function.rigging.util import misc as misc
from function.rigging.util import generic_maya_dict as mnd

#... Determine namespace and reference string

def resetAllController( reference = False ):

	refStr = '*:*' if reference else '*'

	#... Select controllers
	sel = mc.ls(f'{refStr}_ctrl', f'{refStr}_gmbCtrl')

	#... Reset transformation attributes
	for name in sel:
		attr_list = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
		for attr in attr_list:
			attr_name = f"{name}.{attr}"
			if mc.getAttr(attr_name, lock=True):
				continue

			#... if attr is SCALE reset to '1' if not SCALE reset to '0'
			default_value = 1 if attr in ['sx', 'sy', 'sz'] else 0

			#... long version
			'''
			if attr in ['sx', 'sy', 'sz']:
				default_value = 1
			else:
				default_value = 0
			'''

			try:
				if mc.getAttr(attr_name) != default_value:
					mc.setAttr(attr_name, default_value)
			except:
				print(f"{attr_name} cannot be reset, skipped.")
				continue


	#... Handle specific finger and foot controllers
	handle_behavior_dict = mnd.handle_behavior_dict
	print(name)
	mc.select(name)

	nameSpace = misc.findNameSpace()

	for category, data in handle_behavior_dict.items(): #... loop throught finger or foot
		for side in data['side']:
			print(data['stick_name'])
			stick_with_side = data['stick_name'][0].replace('LFT', side)
			for behavior in data['behavior_name']:
				combined_name = f"{nameSpace}{stick_with_side}.{behavior}"
				if mc.objExists(combined_name):
					mc.setAttr(combined_name, 0)
					print(f"Reset {category}: {combined_name} ...\n")
				else:
					print(f'{combined_name} is not found. Please check.')

	# Clean up
	mc.select(cl=True)
	print("### RESET CTRL VALUE COMPLETE ###")




