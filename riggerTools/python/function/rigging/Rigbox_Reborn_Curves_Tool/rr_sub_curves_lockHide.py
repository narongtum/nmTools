"""
RigBox Reborn - Sub: Lock and Hide Tool

Author: Jennifer Conley
Date Modified: 11/23/12

Description:
    A custom GUI to easily lock and hide unused transform channels of a control icon.
    
    Able to use preset options for FK and IK controls.

How to run:
    import rr_sub_curves_lockHide
    rr_sub_curves_lockHide.window_creation()
"""


import pymel.core as pm


window_name = 'lock_and_hide_window'
window_bgc = (.2,.2,.2)
element_bgc = (.45,.45,.45)
width = 300
cbw = 20


# Gui Creation
def window_creation():
    if (pm.window(window_name, q=True, ex=True)):
	pm.deleteUI(window_name)
    if (pm.windowPref(window_name, ex=True)):
	pm.windowPref(window_name, r=True)
	    
    window_object = pm.window(window_name, bgc=window_bgc, w=width, t='RigBox Reborn - Lock / Hide')
    gui_creation()
    window_object.show()
    
	
def gui_creation():
    global controlType_radioGrp
    global translate_checkBoxes, rotate_checkBoxes, scale_checkBoxes, visibility_checkBox
    
    main_col = pm.columnLayout(w=width, co=('both', 50))
    pm.rowColumnLayout(nc=5, cw=[(1,89),(2,cbw),(3,cbw),(4,cbw+4),(5,cbw+2)])
    pm.text(l='', w=cbw)
    pm.text(l='X', w=cbw)
    pm.text(l='Y', w=cbw)
    pm.text(l='Z', w=cbw)
    pm.text(l='All', w=cbw)
    pm.setParent(main_col)
    
    pm.rowColumnLayout(nc=2, cw=[(1,90),(2,80)])
    pm.text(l='Translation:')
    translate_checkBoxes = pm.checkBoxGrp('translate_checkBoxes', ncb=4, cw4=(cbw, cbw, cbw, cbw), cc4=pm.Callback(set_checkBoxGrp, 'translate_checkBoxes'))
    pm.text(l='Rotation:')
    rotate_checkBoxes = pm.checkBoxGrp('rotate_checkBoxes', ncb=4, cw4=(cbw, cbw, cbw, cbw), cc4=pm.Callback(set_checkBoxGrp, 'rotate_checkBoxes'))
    pm.text(l='Scale: ')
    scale_checkBoxes = pm.checkBoxGrp('scale_checkBoxes', ncb=4, cw4=(cbw, cbw, cbw, cbw), cc4=pm.Callback(set_checkBoxGrp, 'scale_checkBoxes'))
    pm.text(l='Visibility:')
    visibility_checkBox = pm.checkBoxGrp('visibility_checkBox', cw=(1,cbw))
    pm.setParent(main_col)
    
    pm.separator(w=175, h=5)
    
    pm.rowColumnLayout(nc=2, cw=[(1,75),(2,100)])
    pm.button(l='Lock / Hide', bgc=element_bgc, c=pm.Callback(set_channels, 1))
    pm.button(l='Show', bgc=element_bgc, c=pm.Callback(set_channels, 0))
    pm.setParent(main_col)
    
    pm.separator(w=175, h=5)
    pm.text(l='Selection Type', w=175)
    controlType_radioGrp = pm.radioButtonGrp(la4=['Ik', 'Fk', 'All', 'None'], nrb=4, cw4=(40,40,40,40), sl=4, cc=set_controlType)
    pm.setParent(main_col)
 



# Work Fuctions
def get_checkBoxState(checkBox_list, checkBox_group):
    checkBox_list.append(pm.checkBoxGrp(checkBox_group, q=True, v1=True))
    checkBox_list.append(pm.checkBoxGrp(checkBox_group, q=True, v2=True))
    checkBox_list.append(pm.checkBoxGrp(checkBox_group, q=True, v3=True))			

	
def get_visibility():
    state = pm.checkBoxGrp(visibility_checkBox, q=True, v1=True)
    
    return state


def set_ikControls():
    translate_checkBoxes.setValue4(False)
    rotate_checkBoxes.setValue4(True)
    scale_checkBoxes.setValue4(True)
    visibility_checkBox.setValue1(True)
    
    
def set_fkControls():
    translate_checkBoxes.setValue4(True)
    rotate_checkBoxes.setValue4(False)
    scale_checkBoxes.setValue4(True)
    visibility_checkBox.setValue1(True)
    
    
def set_allControls():
    translate_checkBoxes.setValue4(True)
    rotate_checkBoxes.setValue4(True)
    scale_checkBoxes.setValue4(True)
    visibility_checkBox.setValue1(True)
    
     
def set_noControls():
    translate_checkBoxes.setValue4(False)
    rotate_checkBoxes.setValue4(False)
    scale_checkBoxes.setValue4(False)
    visibility_checkBox.setValue1(False)
    
      
def set_controlType(*args):
    ctrl_type = controlType_radioGrp.getSelect()
    
    if ctrl_type == 1:
	set_ikControls()
	
    elif ctrl_type ==2:
	set_fkControls()

    elif ctrl_type ==3:
	set_allControls()

    elif ctrl_type == 4:
	set_noControls()
	
    set_checkBoxGrp('translate_checkBoxes')
    set_checkBoxGrp('rotate_checkBoxes')
    set_checkBoxGrp('scale_checkBoxes')
    

def set_checkBoxGrp(checkBox_group):
    
	box_state = pm.checkBoxGrp(checkBox_group, q=True, v4=True)

	if box_state == True:
	    pm.checkBoxGrp(checkBox_group, e=True, v1=True)
	    pm.checkBoxGrp(checkBox_group, e=True, v2=True)
	    pm.checkBoxGrp(checkBox_group, e=True, v3=True)

	else:
	    pm.checkBoxGrp(checkBox_group, e=True, v1=False)
	    pm.checkBoxGrp(checkBox_group, e=True, v2=False)
	    pm.checkBoxGrp(checkBox_group, e=True, v3=False)
  
  
def set_visibility(control_node, checkBox_state, lock):
    if checkBox_state:
	if lock:
	    pm.setAttr(control_node+'.v', l=True, k=False)
	else:
	    pm.setAttr(control_node+'.v', l=False, k=True)
			

def set_checkBox(control_node, attribute, checkBox_state, lock):
    if checkBox_state:
	if lock:
	    pm.setAttr(control_node + attribute, l=True, k=False)
	else:
	    pm.setAttr(control_node + attribute, l=False, k=True)
  
   
def set_channels(lock):
    selection = pm.ls(sl=True)
    
    checkBoxGrp_list = ['translate_checkBoxes', 'rotate_checkBoxes', 'scale_checkBoxes']
    checkBox_list = []
    attribute = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz']
    
    
    vis_checkBox = get_visibility()
    
    for checkBox_group in checkBoxGrp_list:
	get_checkBoxState(checkBox_list, checkBox_group)
    
    
    for control_node in selection:
	set_visibility(control_node, vis_checkBox, lock)

	for i, checkBox in enumerate(checkBox_list):
	    set_checkBox(control_node, attribute[i], checkBox, lock)


			

	

