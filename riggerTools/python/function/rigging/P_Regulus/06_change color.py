
#... change color
import re

names_list = mc.ls('*_ctrl')

# create a joined regex pattern
pattern = re.compile(r'.*(LFT|RGT).*_ctrl')

# filter the list
filtered_names = [name for name in names_list if pattern.match(name)]

print(filtered_names)


import fnmatch
# Lists to hold the names that contain 'LFT' and 'RGT', respectively
left_names = [name for name in filtered_names if fnmatch.fnmatch(name, '*LFT*_ctrl')]
right_names = [name for name in filtered_names if fnmatch.fnmatch(name, '*RGT*_ctrl')]


from function.rigging.autoRig.base import core
reload(core)


for each in right_names:
	ctrl_obj = core.Dag(each)
	ctrl_obj.color = 'red'


for each in left_names:
	ctrl_obj = core.Dag(each)
	ctrl_obj.color = 'blue'


#... change to RGT to RED
# mc.select(right_names,add=True)

# mc.select(left_names,add=True)