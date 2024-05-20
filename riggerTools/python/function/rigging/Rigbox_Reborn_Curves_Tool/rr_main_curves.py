"""
RigBox Reborn - Main: Curves Tool

Author: Jennifer Conley
Date Modified: 11/23/12

Description:
	This is a main tool comprised of smaller, sub-scripts.
	The Curves Tool script contains commonly used features such as:
		- Control icon creation
	- Colorizing options
	- Preset and custom attribut creation
	- Control clean up options

How to run:
	import rr_main_curves
	rr_main_curves.window_creation()
"""


import pymel.core as pm

# import rr_sub_curves_addAttributes
# import rr_sub_curves_colorOptions
# import rr_sub_curves_curveCreation
# import rr_sub_curves_lockHide


from function.rigging.Rigbox_Reborn_Curves_Tool import rr_sub_curves_addAttributes
from function.rigging.Rigbox_Reborn_Curves_Tool import rr_sub_curves_colorOptions
from function.rigging.Rigbox_Reborn_Curves_Tool import rr_sub_curves_curveCreation
from function.rigging.Rigbox_Reborn_Curves_Tool import rr_sub_curves_lockHide


window_name = 'rr_control_window'
window_bgc = (.2,.2,.2)
frame_backgroundColor = (0.655297, 0.405063, 1)
width = 325
height = 600



# GUI Creation Functions
def window_creation():
	global window_object
	
	if (pm.window(window_name, q=True, ex=True)):
		pm.deleteUI(window_name) 
	if (pm.windowPref(window_name, ex=True)):
		pm.windowPref(window_name, r=True)
 
	window_object = pm.window(window_name, bgc=window_bgc, w=width, h=height, t='RigBox Reborn - Curve Tool')
	gui_creation()
	window_object.show()
	
	
def gui_creation():
	main = pm.columnLayout()
	main_scroll = pm.scrollLayout(h=height, w=width)
	
	create_frameLayout('Creation')
	rr_sub_curves_curveCreation.gui_creation()
	pm.setParent(main_scroll)
	
	create_frameLayout('Coloring')
	rr_sub_curves_colorOptions.gui_creation()
	pm.setParent(main_scroll)

	create_frameLayout('Attributes')
	rr_sub_curves_addAttributes.gui_creation()
	pm.setParent(main_scroll)

	create_frameLayout('Lock and Hide')
	rr_sub_curves_lockHide.gui_creation()
	pm.setParent(main_scroll)


def create_frameLayout(frame_name):
	pm.frameLayout(l=frame_name, w=width-25, cll=True, cl=True, bgc=frame_backgroundColor)



