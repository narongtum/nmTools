"""
Rigbox Reborn - Sub: Color Options

Author: Jennifer Conley
Date Modified: 11/23/12

Description:
    A script to quickly color control icons for a rig. Able to be run on a selection.
    
    Also has options for templating an object.

    
How to run:
    import rr_sub_curves_colorOptions
    rr_sub_curves_colorOptions.window_creation()
"""


import pymel.core as pm


window_name = 'rr_colors_win'
window_bgc = (.2,.2,.2)
element_bgc = (.45,.45,.45)
width = 300



# Gui Creation
def window_creation():
    if (pm.window(window_name, q=True, ex=True)):
	    pm.deleteUI(window_name)
	    
    if (pm.windowPref(window_name, ex=True)):
	    pm.windowPref(window_name, r=True)
	    
    window_object = pm.window(window_name, bgc=window_bgc, w=width, t='RigBox Reborn - Color Options')
    gui_creation()
    window_object.show()
            
                  
def gui_creation():
    main = pm.columnLayout(w=width)
    main_form = pm.formLayout(nd=100, w=width)
    
    color_options_title = pm.columnLayout(w=width)
    create_grouping_title = pm.columnLayout()
    #pm.separator(w=width-15, h=5)
    #pm.text(l='Color Options', w=width-15, bgc=(.66, 1, .66))
    pm.separator(w=width-15, h=5)
    pm.text(w=width, l='Select the curves for coloring.')
    pm.text(w=width, l='Then select the color.')
    pm.separator(w=width-15, h=5)
    pm.setParent(main_form)
    
    color_options = pm.columnLayout()
    pm.rowColumnLayout(nc=2)
    pm.button(l='', w=90, bgc=(1,0,0), c=pm.Callback(rr_colorCurves_buttons, 13))
    pm.button(l='', w=90, bgc=(0,0,1), c=pm.Callback(rr_colorCurves_buttons, 6))
    pm.setParent(color_options)
    
    pm.button(l='', w=180, bgc=(0,1,1), c=pm.Callback(rr_colorCurves_buttons, 18))
    
    pm.rowColumnLayout(nc=2)
    pm.button(l='', w=90, bgc=(.6,0,1), c=pm.Callback(rr_colorCurves_buttons, 30))
    pm.button(l='', w=90, bgc=(1,1,0), c=pm.Callback(rr_colorCurves_buttons, 17))
    pm.setParent(main_form)
    
    divider = pm.columnLayout()
    pm.separator(h=70, hr=False)
    pm.setParent(main_form)
    
    template_options = pm.columnLayout(w=width)
    pm.button(l='Template Attr', bgc=element_bgc, w=95, c=rr_template_attr)
    pm.button(l='Template', bgc=element_bgc, w=95, c=rr_template_object)
    pm.button(l='Untemplate', bgc=element_bgc, w=95, c=rr_untemplate)
    pm.setParent(main_form)
    
    pm.formLayout(main_form, e=True,
	attachForm=[(divider, 'bottom', 5), (color_options, 'bottom', 5), (color_options, 'left', 5), (template_options, 'bottom', 5), (color_options_title, 'right', 5), (color_options_title, 'left', 5), (color_options_title, 'top', 5)],
	attachControl=[(divider, 'top', 2, color_options_title), (divider, 'right', 0, template_options), (divider, 'left', 0, color_options),(color_options, 'top', 2, color_options_title), (template_options, 'left', 5, color_options), (template_options, 'top', 2, color_options_title)],
	attachPosition=[(color_options_title, 'right', 2, 60 )])




# Work Functions    
def rr_colorCurves_buttons(color):
    selection = pm.ls(sl=True)

    for each in selection:
	pm.setAttr(each + '.overrideEnabled', True)
	pm.setAttr(each + '.overrideColor', color)
	
    print "Selection's color has been changed."
 
    
def rr_template_object(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	pm.setAttr(individual_object + '.template', k=True)
	pm.setAttr(individual_object + '.template', 1)
    
    print "Selection has been templated."

    
def rr_untemplate(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
    	pm.setAttr(individual_object + '.template', 0)
	
    print "Selection has been untemplated."
  
    
def rr_template_attr(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	pm.setAttr(individual_object + '.template', k=True)
    
    print "Selection has had the template attribute set to 'keyable'."




    
    
    
    
    
    
    
    