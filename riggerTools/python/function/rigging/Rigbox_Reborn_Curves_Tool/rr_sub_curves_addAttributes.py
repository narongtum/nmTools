"""
RigBox Reborn - Sub: Add Attributes Tool

Author: Jennifer Conley
Date Modified: 11/23/12

Description:
    A custom GUI to easily add common attributes to objects.
    
    Allows for additonal, custom attributes, to be added to objects
    without having to navigate to other windows.
    
How to run:
    import rr_sub_curves_addAttributes
    rr_sub_curves_addAttributes.window_creation()
"""


import pymel.core as pm


windowName = 'rr_addAttrs_tool'
window_bgc = (.2,.2,.2)
element_bgc = (.45,.45,.45)
title_color = (0.860652, 0.759494, 1)
width = 300


# Attribute Lists
finger_dropAttrs = ['Finger_Drops', 'Thumb_Drop', 'Pinky_Drop']
finger_spreadAttrs = ['Spreads', 'Thumb_Spread', 'Index_Spread', 'Middle_Spread', 'Ring_Spread', 'Pinky_Spread']
thumb_curlAttrs = ['Thumb_Curl', 'Thumb_Root', 'Thumb_Mid', 'Thumb_End']
index_curlAttrs = ['Index_Curl', 'Index_Root', 'Index_Mid', 'Index_End']
mid_curlAttrs = ['Mid_Curl', 'Mid_Root', 'Mid_Mid', 'Mid_End']
ring_curlAttrs = ['Ring_Curl', 'Ring_Root', 'Ring_Mid', 'Ring_End']
pinky_curlAttrs = ['Pinky_Curl', 'Pinky_Root', 'Pinky_Mid', 'Pinky_End']

toe_spreadAttrs = ['Spreads', 'Big_Spread', 'Index_Spread', 'Middle_Spread', 'Fourth_Spread', 'Pinky_Spread']
big_curlAttrs = ['Big_Curl', 'Big_Root', 'Big_Mid', 'Big_End']
fourth_curlAttrs = ['Fourth_Curl', 'Fourth_Root', 'Fourth_Mid', 'Fourth_End']

foot_raiseAttrs = ['Raises', 'Heel_Raise', 'Ball_Raise', 'Toe_Raise']



# Gui Functions
def window_creation():
    if (pm.window(windowName, q=True, ex=True)):
	    pm.deleteUI(windowName)   
    if (pm.windowPref(windowName, ex=True)):
	    pm.windowPref(windowName, r=True)

    window_object = pm.window(windowName, bgc=window_bgc, t='RigBox Reborn - Add Attribute', w=width)
    gui_creation()
    window_object.show()
               
	       
def gui_creation():
    main = pm.columnLayout(w=width)
    main_form = pm.formLayout(nd=100, w=width)
    
    preset_options_column = pm.columnLayout(w=width)
    title_creation('Preset Options')
    preset_options()
    pm.setParent(main_form)
    
    custom_options_column = pm.columnLayout(w=width)
    title_creation('Custom Options')
    custom_options()
    pm.setParent(main_form)
    
    pm.formLayout(main_form, e=True,
	attachForm=[(custom_options_column, 'left', 5), (custom_options_column, 'right', 5), (custom_options_column, 'bottom', 5), (preset_options_column, 'left', 5), (preset_options_column, 'right', 5), (preset_options_column, 'top', 5)],
	attachControl=[(custom_options_column, 'top', 2, preset_options_column)])

    
def title_creation(title):
    pm.columnLayout(w=width)
    pm.separator(w=width-15, h=5)
    pm.text(l=title, w=width-15, bgc=title_color)
    pm.separator(w=width-15, h=5)
    
    
def preset_options():
    main = pm.columnLayout(w=width)
    
    pm.rowColumnLayout(nc=2, w=width)
    pm.button(w=141, bgc=element_bgc, l='Ik Foot', c=add_ikFootAttrs)
    pm.button(w=141, bgc=element_bgc, l='Foot Switch', c=add_footSwitchAttrs)
    pm.button(w=141, bgc=element_bgc, l='Ik Hand', c=add_ikHandAttrs)
    pm.button(w=141, bgc=element_bgc, l='Hand Switch', c=add_handSwitchAttrs)
    pm.setParent(main)
    
    pm.rowColumnLayout(nc=3, w=width)
    pm.button(w=94, bgc=element_bgc, l='Cog', c=add_cogAttrs)
    pm.button(w=94, bgc=element_bgc, l='Head', c=add_headAttrs)
    pm.button(w=94, bgc=element_bgc, l='Eye', c=add_eyeAttrs)
    pm.setParent(main)
    
    
def custom_options():
    global attributeType_radioGrp, attribute_nameField, attribute_minField, attribute_maxField
    main = pm.columnLayout()
    attributeType_radioGrp = pm.radioButtonGrp(cc=field_display, sl=1, nrb=4, cw4=(75,75,75,75), la4=('Float', 'Integer', 'Boolean', 'Sep'))
    
    pm.separator(w=width-15, h=10)
    pm.rowColumnLayout(nc=4, w=width)
    attribute_nameField = pm.textField(w=71, ann = 'Attribute Name', tx='Name')
    attribute_minField = pm.floatField(w=71, ann='Attribute Min', v=-360, pre=1)
    attribute_maxField = pm.floatField(w=71, ann='Attribute Max', v=360, pre=1)
    pm.button(l='Create', bgc=element_bgc, w=71, c=create_attr)
    pm.setParent(main)
  
  
  
  
# Gui Work Functions    
def field_display(*args):
    attr_value = attributeType_radioGrp.getSelect()
    
    if attr_value == 1:
	attribute_minField.setEnable(True)
	attribute_maxField.setEnable(True)
	
    elif attr_value == 2:
	attribute_minField.setEnable(True)
	attribute_maxField.setEnable(True)
	
    elif attr_value == 3:
	attribute_minField.setEnable(False)
	attribute_maxField.setEnable(False)
	
    else:
	attribute_minField.setEnable(False)
	attribute_maxField.setEnable(False)

    print 'Attribut Creation GUI has been updated.'
        



# Work Functions
def add_cogAttrs(*args):
    selection = pm.ls(sl=True)
	
    for individual_object in selection:
	create_separatorAttr(individual_object, 'Adv_Back')
	pm.addAttr(individual_object, ln='Back_Ctrls', at='enum', en='Fk_Ctrls:Ik_Ctrls:Both:None', k=True)
	
	create_separatorAttr(individual_object, 'Other')
	pm.addAttr(individual_object, ln='Res', at='enum', en='Low:Proxy:High', k=True)
	create_boolAttr(individual_object, 'Auto_Hips')


def add_eyeAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Control_Visibility')
	create_boolAttr(individual_object, 'Indiv_Ctrls')


def add_headAttrs(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	create_separatorAttr(individual_object, 'Control_Visibility')
	create_boolAttr(individual_object, 'Face_Ctrls')
	create_boolAttr(individual_object, 'Eye_Ctrls')


def add_ikFootAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Foot_SDKs')

	create_floatAttr(individual_object, 'Foot_Roll', -10, 10)
	create_floatAttr(individual_object, 'Bank', -360, 360)
	
	create_curlAttrs(individual_object, foot_raiseAttrs)
	
	create_separatorAttr(individual_object, 'Grinds')
	create_floatAttr(individual_object, 'Heel_Grind', -360, 360)
	create_floatAttr(individual_object, 'Toe_Grind', -360, 360)

	create_separatorAttr(individual_object, 'Knee_Pv')
	create_floatAttr(individual_object, 'Knee', -360, 360)
	create_floatAttr(individual_object, 'Offset', -360, 360)

	create_separatorAttr(individual_object, 'Space_Switching')
	create_floatAttr(individual_object, 'Cog', -360, 360)
	create_floatAttr(individual_object, 'Locator', -360, 360)


def add_ikHandAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Space_Switching')
	create_floatAttr(individual_object, 'Head', 0, 10)
	create_floatAttr(individual_object, 'Back', 0, 10)
	create_floatAttr(individual_object, 'Hips', 0, 10)
	create_floatAttr(individual_object, 'Locator', 0, 10)


def add_footSwitchAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Foot_SDKs')
	create_floatAttr(individual_object, 'Ik_Fk_Switch', 0 , 10)
	create_boolAttr(individual_object, 'Indiv_Ctrls')
	create_floatAttr(individual_object, 'All_Curl', -10 , 10)
	create_floatAttr(individual_object, 'All_Spread', -10 , 10)

	create_curlAttrs(individual_object, big_curlAttrs)
	create_curlAttrs(individual_object, index_curlAttrs)
	create_curlAttrs(individual_object, mid_curlAttrs)
	create_curlAttrs(individual_object, fourth_curlAttrs)
	create_curlAttrs(individual_object, pinky_curlAttrs)
	
	create_spreadAttrs(individual_object, toe_spreadAttrs)


def add_handSwitchAttrs(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	create_separatorAttr(individual_object, 'Hand_SDKs')
	create_floatAttr(individual_object, 'Ik_Fk_Switch', 0 , 10)
	create_boolAttr(individual_object, 'Indiv_Ctrls')
	create_floatAttr(individual_object, 'All_Curl', -10 , 10)
	create_floatAttr(individual_object, 'All_Spread', -10 , 10)
	
	
	create_dropAttrs(individual_object, finger_dropAttrs)
	
	create_curlAttrs(individual_object, thumb_curlAttrs)
	create_curlAttrs(individual_object, index_curlAttrs)
	create_curlAttrs(individual_object, mid_curlAttrs)
	create_curlAttrs(individual_object, ring_curlAttrs)
	create_curlAttrs(individual_object, pinky_curlAttrs)
	
	create_spreadAttrs(individual_object, finger_spreadAttrs)
	
	
def create_dropAttrs(individual_object, attr_list):
    create_separatorAttr(individual_object, attr_list[0])
    create_floatAttr(individual_object, attr_list[1], -360 , 360)
    create_floatAttr(individual_object, attr_list[2], -360 , 360)
	
	
def create_curlAttrs(individual_object, attr_list):
    create_separatorAttr(individual_object, attr_list[0])
    create_floatAttr(individual_object, attr_list[1], -360 , 360)
    create_floatAttr(individual_object, attr_list[2], -360 , 360)
    create_floatAttr(individual_object, attr_list[3], -360 , 360)
	
	
def create_spreadAttrs(individual_object, attr_list):
    create_separatorAttr(individual_object, attr_list[0])
    create_floatAttr(individual_object, attr_list[1], -360 , 360)
    create_floatAttr(individual_object, attr_list[2], -360 , 360)
    create_floatAttr(individual_object, attr_list[3], -360 , 360)
    create_floatAttr(individual_object, attr_list[4], -360 , 360)
    create_floatAttr(individual_object, attr_list[5], -360 , 360)
    
    
    
def create_attr(*args):
    attr_value = attributeType_radioGrp.getSelect()
    name = attribute_nameField.getText()
    min_value = attribute_minField.getValue()
    max_value = attribute_maxField.getValue()

    selection = pm.ls(sl=True)

    for individual_object in selection:
	if attr_value == 1:
	    create_floatAttr(individual_object, name, min_value, max_value)
	    
	elif attr_value == 2:
	    create_intAttr(individual_object, name, min_value, max_value)

	elif attr_value == 3:
	    create_boolAttr(individual_object, name)
	    
	else:
	    create_separatorAttr(individual_object, attr_name)
	
    print "Custom attribute '" + name + "' has been added to selected objects."
 
     
def create_boolAttr(control, attr_name):
    pm.addAttr(control, ln=attr_name, at='bool', dv=1, k=True)


def create_separatorAttr(control, attr_name):
    pm.addAttr(control, ln=attr_name, at='enum', en='----------------')
    pm.setAttr(control + '.' + attr_name, cb=True)


def create_floatAttr(control, attr_name, min_value, max_value):
    pm.addAttr(control, ln=attr_name, at='double', min=min_value, max=max_value, k=True)

def create_intAttr(control, attr_name, min_value, max_value):
    pm.addAttr(control, ln=attr_name, at='long', min=min_value, max=max_value, k=True)



