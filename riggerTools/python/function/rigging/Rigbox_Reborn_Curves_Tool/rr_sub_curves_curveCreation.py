"""
RigBox Reborn - Sub: Curve Creation

Author: Jennifer Conley
Date Modified: 11/23/12

Description:
    A custom GUI to easily create commonly used control icons for rig construction.
	- Includes 2D, 3D, and text based curves.
	
    Provides features for:
	- Priming controls based on a selected transform node, or a heirarchy of nodes.
	- Naming control icons
	- Naming priming groups
	- Constraining selected transform node
	    ~ Parent or orient constraint options

    The curve must be selected first, then the transform node. This selection order was
    choosen because it replicates actual parenting inside of Maya.
    

How to run:
    import rr_sub_curves_curveCreation
    rr_sub_curves_curveCreation.window_creation()
"""


import pymel.core as pm
from functools import partial


window_name = 'Curve_Tool'
window_bgc = (.2,.2,.2)
element_bgc = (.45,.45,.45)
title_color = (0.860652, 0.759494, 1)
frame_color = (0.655297, 0.405063, 1 )
width = 290


# Gui Creation
def window_creation():
    if (pm.window(window_name, q=True, ex=True)):
	    pm.deleteUI(window_name)
	    
    if (pm.windowPref(window_name, ex=True)):
	    pm.windowPref(window_name, r=True)
	    
    global window_object    
    window_object = pm.window(window_name, bgc=window_bgc, t='RigBox Reborn - Curve Creation', w=width)
    gui_creation()
    window_object.show()
            
                  
def gui_creation():
    global main, naming_form, grouping_form, grouping_options_frame
    main = pm.columnLayout()
    
    naming_form = pm.formLayout()
    naming_title = title_creation('Control Naming', naming_form)
    rename_col = rename_gui()
    ctrl_options_col = control_options_gui()
    
    pm.formLayout(naming_form, e=True,
	attachForm=[(ctrl_options_col, 'right', 5), (ctrl_options_col, 'left', 5), (rename_col, 'right', 5), (rename_col, 'left', 5), (naming_title, 'right', 5), (naming_title, 'left', 5), (naming_title, 'top', 5)],
	attachControl=[(ctrl_options_col, 'top', 5, rename_col), (rename_col, 'top', 5, naming_title)])
    pm.setParent(main)
    
    
    pm.columnLayout(co=('left', 5))
    grouping_options_frame = pm.frameLayout(l='Grouping', en=False, w=width, cl=True, cll=True, bgc=frame_color, cc=pm.Callback(window_resize, -200))
    pm.setParent(main)
    
    grouping_form = pm.formLayout(p=grouping_options_frame)
    grouping_title = title_creation('Group Naming', grouping_form)
    group_naming_col = group_naming_gui()
    grouping_instructions_title = title_creation('Grouping Options', grouping_form)
    grouping_instructions_col = group_instructions_gui()
    grouping_options_col = grouping_options_gui()
    pm.setParent(main)
    
    pm.formLayout(grouping_form, e=True,
	attachForm=[(grouping_options_col, 'left', 0), (grouping_options_col, 'right', 0),(grouping_instructions_col, 'left', 0), (grouping_instructions_col, 'right', 0),(grouping_instructions_title, 'left', 0), (grouping_instructions_title, 'right', 0),(group_naming_col, 'left', 0), (group_naming_col, 'right', 0),(grouping_title, 'left', 0), (grouping_title, 'right', 0), (grouping_title, 'top', 5), ],
	attachControl=[(grouping_options_col, 'top', 5, grouping_instructions_col), (grouping_instructions_col, 'top', 5, grouping_instructions_title), (grouping_instructions_title, 'top', 5, group_naming_col), (group_naming_col, 'top', 5, grouping_title)])
    
    pm.setParent(main)
    control_buttons_gui()
    
       
def rename_gui():
    main_col = pm.columnLayout()
    pm.rowColumnLayout(nc=3, cw=[(1,width/3),(2,width/3),(3,width/3)])
    
    pm.text(l='Prefix', w=width/3)
    pm.text(l='Name', w=width/3)
    pm.text(l='Suffix', w=width/3)
    
    global ctrl_prefix_field, ctrl_name_field, ctrl_suffix_field
    
    ctrl_prefix_field = pm.textField(w=width/3)
    ctrl_name_field = pm.textField(w=width/3)
    ctrl_suffix_field = pm.textField(w=width/3)
    pm.setParent(naming_form)
    
    return main_col
    
     
def control_options_gui():
    global snap_optionMenu, group_optionMenu
    
    main_col = pm.columnLayout()
    pm.rowColumnLayout(nc=3, cw=[(1,width/2),(2,width/2)])
    
    snap_optionMenu = pm.optionMenu(w=width/2, bgc=element_bgc)
    pm.menuItem(l='Default')
    pm.menuItem(l='Snap')
    
    group_optionMenu = pm.optionMenu(w=width/2, bgc=element_bgc, cc=unlock_grouping_frame)
    pm.menuItem(l='Default')
    pm.menuItem(l='Group')
    pm.setParent(naming_form)
    
    return main_col
        
    
def group_naming_gui():
    sub_width = width-5
    
    main_col = pm.columnLayout(w=sub_width)
    pm.rowColumnLayout(nc=3, cw=[(1,sub_width/3),(2,sub_width/3),(3,sub_width/3)])
    
    pm.text(l='Prefix', w=sub_width/3)
    pm.text(l='Name', w=sub_width/3)
    pm.text(l='Suffix', w=sub_width/3)
    
    global grp1_prefix_field, grp1_name_field, grp1_suffix_field
    global grp2_prefix_field, grp2_name_field, grp2_suffix_field
    
    grp1_prefix_field = pm.textField(w=sub_width/3)
    grp1_name_field = pm.textField(w=sub_width/3)
    grp1_suffix_field = pm.textField(w=sub_width/3)
    
    grp2_prefix_field = pm.textField(w=sub_width/3)
    grp2_name_field = pm.textField(w=sub_width/3)
    grp2_suffix_field = pm.textField(w=sub_width/3)
    pm.setParent(grouping_form)
    
    return main_col


def group_instructions_gui():
    sub_width = width-5
    
    main_col = pm.columnLayout(w=sub_width)
    pm.text(l='Select a curve, then a joint.', w=sub_width)
    pm.text(l="Click 'Apply' once tool options have been set.", w=sub_width)
    pm.separator(w=sub_width, h=5)
    pm.setParent(grouping_form)
    
    return main_col
    
   
def grouping_options_gui():
    global duplicate_optionMenu, hierarchy_optionMenu, constraint_optionMenu
    sub_width = width-5
    
    main_col = pm.columnLayout(w=sub_width)
    grouping_form = pm.formLayout(w=sub_width)
    menu_col = pm.rowColumnLayout(nc=3, cw=[(1,sub_width/3),(2,sub_width/3), (3,sub_width/3)])
    
    duplicate_optionMenu = pm.optionMenu(bgc=element_bgc, w=sub_width/3)
    pm.menuItem(l='Single')
    pm.menuItem(l='Chain')
    
    hierarchy_optionMenu = pm.optionMenu(bgc=element_bgc, w=sub_width/3)
    pm.menuItem(l='Default')
    pm.menuItem(l='Hierarchy')
    
    constraint_optionMenu = pm.optionMenu(bgc=element_bgc, w=sub_width/3)
    pm.menuItem(l='Default')
    pm.menuItem(l='Orient')
    pm.menuItem(l='Parent')
    pm.setParent(grouping_form)
    
    apply_button_col = pm.columnLayout(w=sub_width)
    pm.separator(w=sub_width)
    pm.button(l='Apply', w=sub_width, bgc=(.451,.451,.451), c=apply_button)
    pm.separator(w=sub_width)
    
    pm.formLayout(grouping_form, e=True,
	attachForm=[(apply_button_col, 'bottom',5), (apply_button_col, 'right',0), (apply_button_col, 'left',0), (menu_col, 'top',5), (menu_col, 'right',0), (menu_col, 'left',0)],
	attachControl=[(apply_button_col, 'top',5, menu_col) ])
    
    return main_col

    
def control_buttons_gui():
    create_shapeButtons_gui()
    pm.setParent(main)
    
    global char_form
    
    char_form = pm.formLayout()
    
    text_title_col = title_creation('Text Shapes', char_form)
    letter_col = letter_controls_gui()
    text_col = text_controls_gui()
    
    pm.formLayout(char_form, e=True,
	attachForm=[(letter_col, 'bottom', 5),(text_col, 'bottom', 5),(text_col, 'right', 5), (letter_col, 'left', 5),(text_title_col, 'left', 5), (text_title_col, 'right', 5),(text_title_col, 'top', 5)],
	attachControl=[(text_col, 'left', 0, letter_col),(text_col, 'top', 5, text_title_col),(letter_col, 'top', 5, text_title_col),],
	attachPosition=[(text_col, 'left', 0, 49)])
    
    
def create_shapeButtons_gui():
    global twoD_form
    main_col = pm.columnLayout(p=main)
    twoD_form = pm.formLayout(nd=100)
    
    twoD_shapes_title = title_creation('2D Shapes', twoD_form)
    twoD_controls_col = twoD_controls_gui()
    
    twoD_arrows_title = half_title_creation('2D Arrows', twoD_form)
    twoD_arrows_col = twoD_arrows_gui()
    threeD_title = half_title_creation('3D Shapes', twoD_form)
    threeD_controls_col = threeD_controls_gui()
    
    
    pm.formLayout(twoD_form, e=True,
	attachForm=[(threeD_controls_col, 'right', 5),(twoD_arrows_col, 'left', 5),(threeD_title, 'right', 5),  (twoD_arrows_title, 'left', 5), (twoD_controls_col, 'right', 5), (twoD_controls_col, 'left', 5), (twoD_shapes_title, 'right', 5), (twoD_shapes_title, 'left', 5), (twoD_shapes_title, 'top', 5)],
	attachControl=[(threeD_controls_col, 'left', 0, twoD_arrows_col),(threeD_controls_col, 'top', 5, threeD_title),(twoD_arrows_col, 'top', 5, twoD_arrows_title),(threeD_title, 'left', 0, twoD_arrows_title),(threeD_title, 'top', 5, twoD_controls_col),(twoD_arrows_title, 'top', 5, twoD_controls_col),(twoD_controls_col, 'top', 5, twoD_shapes_title), ],
	attachPosition=[(threeD_title, 'left', 0, 49), (threeD_controls_col, 'left', 0, 49)])

    
def twoD_controls_gui():
    main_col = pm.columnLayout(w=width)

    pm.rowColumnLayout(w=width, nc=2, cw=[(width/2),(width/2)])
    pm.button(l='Circle', bgc=element_bgc, w=width/2, c=partial(create_shape_control, 'create_circle'))
    pm.button(l='Square', bgc=element_bgc, w=width/2, c=partial(create_shape_control, 'create_square'))
    pm.button(l='Move All', bgc=element_bgc, w=width/2, c=partial(create_shape_control, 'create_move_all'))	
    pm.button(l='Sun', bgc=element_bgc, w=width/2, c=partial(create_shape_control, 'create_sun'))
    pm.setParent(main_col)
    
    pm.rowColumnLayout(w=width, nc=5, cw=[(1,width/5),(2,width/5),(3,width/5),(4,width/5),(5,width/5)])
    pm.button(l='Pick', bgc=element_bgc, w=width/5, c=partial(create_shape_control, 'create_pick'))
    pm.button(l='Frame', bgc=element_bgc, w=width/5, c=partial(create_shape_control, 'create_frame'))
    pm.button(l='Triangle', bgc=element_bgc, w=width/5, c=partial(create_shape_control, 'create_triangle'))
    pm.button(l='Plus', bgc=element_bgc, w=width/5, c=partial(create_shape_control, 'create_plus'))
    pm.button(l='Swirl', bgc=element_bgc, w=width/5, c=partial(create_shape_control, 'create_swirl'))
    pm.setParent(twoD_form)
    
    return main_col


def twoD_arrows_gui():
    main_col = pm.columnLayout(w=width/2)
    
    pm.rowColumnLayout(nc=2, w=width/2, cw=[(1,width/4),(2,width/4)])	
    pm.button(l='Single', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_single_arrow'))
    pm.button(l='Curved', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_curved_single_arrow'))
    pm.setParent(main_col)
    
    pm.rowColumnLayout(nc=2)
    pm.button(l='Double', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_double_arrow'))
    pm.button(l='Curved', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_curved_double_arrow'))
    pm.button(l='Triple', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_triple_arrow'))
    pm.button(l='Quad', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_quad_arrow'))
    pm.setParent(twoD_form)
    
    return main_col


def threeD_controls_gui():
    main_col = pm.columnLayout(w=width/2)
    
    pm.rowColumnLayout(w=width/2, nc=2, cw=[(1,width/4),(2,width/4)])
    pm.button(l='Cube', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_cube'))
    pm.button(l='Diamond', bgc=element_bgc, w=width/4, c=partial(create_shape_control, 'create_diamond'))
    pm.setParent(main_col)
    
    pm.rowColumnLayout(w=width/2, nc=3, cw=[(1,width/6),(2,width/6),(3,width/6)])
    pm.button(l='Ring', bgc=element_bgc, w=width/6, c=partial(create_shape_control, 'create_ring'))
    pm.button(l='Cone', bgc=element_bgc, w=width/6, c=partial(create_shape_control, 'create_cone'))
    pm.button(l='Orb', bgc=element_bgc, w=width/6, c=partial(create_shape_control, 'create_orb'))

    pm.button(l='Lever', bgc=element_bgc, w=width/6, c=partial(create_shape_control, 'create_lever'))
    pm.button(l='Jack', bgc=element_bgc, w=width/6, c=partial(create_shape_control, 'create_jack'))
    pm.button(l='Point', bgc=element_bgc, w=width/6, c=partial(create_shape_control, 'create_pointer'))
    pm.setParent(twoD_form)
    
    return main_col


def letter_controls_gui():
    main_col = pm.columnLayout(w=width/2 )

    control_icon_list1 = ['E', 'K', 'L']
    pm.rowColumnLayout(w=width/2, nc=2, cw=[(1,width/4),(2,width/4)])
    create_letter_button(control_icon_list1, width/4)
    pm.button(l='R', w=width/4, bgc=element_bgc, c=pm.Callback(create_text_control, 'R'))
    pm.setParent(main_col)
    
    control_icon_list2 = ['C', 'H', 'S']
    pm.rowColumnLayout(w=width/2, nc=4, cw=[(1,width/8),(2,width/8),(3,width/8),(4,width/8)])
    pm.button(l='B', w=width/8, bgc=element_bgc, c=pm.Callback(create_text_control, 'B'))
    create_letter_button(control_icon_list2, width/8)
    pm.setParent(char_form)
    
    return main_col


def text_controls_gui():
    main_col = pm.columnLayout(w=width/2,)

    control_icon_list1 = ['Lf', 'Rt', 'Blends', 'Ik / Fk']
    pm.rowColumnLayout(w=width/2, nc=2, cw=[(1,width/4),(2,width/4)])
    create_text_button(control_icon_list1, width/4)
    pm.setParent(main_col)
    
    pm.rowColumnLayout(w=width/2, nc=2, cw=[(1,width/4),(2,width/4)])
    control_icon_list2 = ['COG', 'GUI']
    create_text_button(control_icon_list2, width/4)
    pm.setParent(char_form)

    return main_col

  
  
    
# Gui Work Functions    
def create_letter_button(text_list, size):
    for individual_item in text_list:
	pm.button(l=individual_item, w=size, bgc=element_bgc, c=pm.Callback(create_letter_control, individual_item))
	
	
def create_text_button(text_list, size):
    for individual_item in text_list:
	pm.button(l=individual_item, w=size, bgc=element_bgc, c=pm.Callback( create_text_control, individual_item))
    
     
def title_creation(title, parent_layout):
    main = pm.columnLayout()
    
    pm.separator(w=width, h=5)
    pm.text(l=title, w=width, bgc=title_color)
    pm.separator(w=width, h=5)
    pm.setParent(parent_layout)
    
    return main


def half_title_creation(title, parent_layout):
    main = pm.columnLayout(w=(width/2))
    
    pm.separator(w=(width/2), h=5)
    pm.text(l=title, w=(width/2), bgc=title_color)
    pm.separator(w=(width/2), h=5)
    pm.setParent(parent_layout)
    
    return main
    
    
def window_resize(difference):
    if (pm.window(window_name, q=True, ex=True)):
	current_height = window_object.getHeight()
	height = current_height + difference
	window_object.setHeight(height)

    
def unlock_grouping_frame(*args):
    if group_optionMenu.getSelect() == 2:
	pm.frameLayout(grouping_options_frame, e=True, en=True, cl=False)
	#pm.frameLayout(grouping_options, en=True)
    else:
	if (pm.frameLayout(grouping_options_frame, q=True, cl=True)):
	    pm.frameLayout(grouping_options_frame, e=True, en=False)
	else:
	     window_resize(-200)
	     pm.frameLayout(grouping_options_frame, e=True, en=False, cl=True)
	
	
    
        
# Control Creation Functions
def run_function(function_name):
    exec(function_name + '()')
    

def create_shape_control(function_name, *args):
    if (duplicate_optionMenu.getSelect()) == 2:
	snap_objects = select_hierarchy()
	parent_control = ''
	
	for i, indiv_object in enumerate(snap_objects):
	    run_function(function_name)
	    create_multiple_controls(control, indiv_object, parent_control, i)
	    parent_control = control
	    
	pm.select(parent_control)
		
    else:
	snap_object = pm.ls(sl=True)
	run_function(function_name)
	create_control(snap_object, control)
	    
	pm.select(control)
	

def create_letter_control(var):
    if (duplicate_optionMenu.getSelect()) == 2:
	snap_objects = select_hierarchy()
	parent_control = ''
	
	for i, indiv_object in enumerate(snap_objects):
	    create_char(var)
	    create_multiple_controls(control, indiv_object, parent_control, i)
	    parent_control = control
	    
	pm.select(parent_control)
		
    else:
	snap_object = pm.ls(sl=True)
	create_char(var)
	create_control(snap_object, control)
	    
	pm.select(control)

	
def create_text_control(var):
    if (duplicate_optionMenu.getSelect()) == 2:
	snap_objects = select_hierarchy()
	parent_control = ''
	
	for i, indiv_object in enumerate(snap_objects):
	    create_text(var)
	    create_multiple_controls(control, indiv_object, parent_control, i)
	    parent_control = control
	    
	pm.select(parent_control)
		
    else:
	snap_object = pm.ls(sl=True)
	create_text(var)
	create_control(snap_object, control)
	    
	pm.select(control)
	



#Control Shape Functions	
def create_circle():
    global control
    control = pm.circle( nr=[0,1,0])[0]
    
    
def create_square():
    global control
    control = pm.curve(d=1, p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1), (-1,0,-1)], k=[0,1,2,3,4])


def create_move_all():
    global control
    control = pm.circle(nr=[0,1,0])[0]
    
    arrow_list = []
    arrow_list.append(pm.curve(d=1, p=[(1.75625, 0, 0.115973),(1.75625, 0, -0.170979),(2.114939, 0, -0.170979),(2.114939, 0, -0.314454),(2.473628, 0, -0.0275029),(2.114939, 0, 0.259448),(2.114939, 0, 0.115973),(1.75625, 0, 0.115973)], k=[0,1,2,3,4,5,6,7]))
    arrow_list.append(pm.curve(d=1, p=[(0.143476, 0, -1.783753),(0.143476, 0, -2.142442),(0.286951, 0, -2.142442),(0, 0, -2.501131),(-0.286951, 0, -2.142442),(-0.143476, 0, -2.142442),(-0.143476, 0, -1.783753),(0.143476, 0, -1.783753)], k=[0,1,2,3,4,5,6,7]))
    arrow_list.append(pm.curve(d=1, p=[(-1.75625, 0, -0.170979),(-2.114939, 0, -0.170979),(-2.114939, 0, -0.314454),(-2.473628, 0, -0.0275029),(-2.114939, 0, 0.259448),(-2.114939, 0, 0.115973),(-1.75625, 0, 0.115973),(-1.75625, 0, -0.170979)], k=[0,1,2,3,4,5,6,7]))
    arrow_list.append(pm.curve(d=1, p=[(-0.143476, 0, 1.728747),(-0.143476, 0, 2.087436),(-0.286951, 0, 2.087436),(0, 0, 2.446125),(0.286951, 0, 2.087436),(0.143476, 0, 2.087436),(0.143476, 0, 1.728747),(-0.143476, 0, 1.728747)], k=[0,1,2,3,4,5,6,7]))

    pm.select(arrow_list)
    pm.pickWalk(d='Down')
    pm.select(control, tgl=True)
    pm.parent(r=True, s=True)
    pm.delete(arrow_list)
    pm.xform(control, cp=True)


def create_sun():
    global control
    control = pm.circle(s=16, nr=[0,1,0])[0]
    pm.select((control + '.cv[1]'), (control + '.cv[3]'), (control + '.cv[5]'), (control + '.cv[7]'), (control + '.cv[9]'), (control + '.cv[11]'), (control + '.cv[13]'), (control + '.cv[15]'), (control + '.cv[17]'), (control + '.cv[19]'), r=True)
    pm.scale(0.3, 0.3, 0.3, p=[0, 0, 0], r=True)
    pm.makeIdentity(control, apply=True, t=1, r=1, s=1, n=0)
    pm.xform(control, cp=True)
    
 
def create_pick():
    global control
    control = pm.circle(nr=[0,1,0])[0]
    
    pm.move(control + '.cv[5]', (0, 0, -1.108194) ,r=True)
    pm.move(control + '.cv[1]', (0, 0, 1.108194) ,r=True)
    pm.move(control + '.cv[6]', (-0.783612, 0, -0.783612) ,r=True)
    pm.move(control + '.cv[0]', (-0.783612, 0, 0.783612) ,r=True)
    pm.move(control + '.cv[7]', (-1.108194, 0, 0) ,r=True)
	

def create_frame():
    global control
    control = pm.curve(d=1, p=[(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1),(-1,0,-1),(-2,0,-2),(2,0,-2),(1,0,-1),(1,0,1),(2,0,2),(2,0,-2),(2,0,2),(-2,0,2),(-1,0,1),(-2,0,2),(-2,0,-2)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


def create_triangle():
    global control
    control = pm.curve(d=1, p=[(-1,0,1),(1,0,1),(0,0,-1),(-1,0,1)], k=[0,1,2,3,])
    
    
def create_plus():
    global control
    control = pm.curve(d=1, p=[(-1,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,1),(1,0,1),(1,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,-1),(-1,0,-1),(-1,0,-3)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12])
    pm.scale(control, .33, .33, .33)
    pm.makeIdentity(control, apply=True, t=True, r=True, s=True)
    
    
def create_swirl():
    global control
    control = pm.curve(d=3, p=[(0, 0, 0.0360697),(-0.746816, 0, 1),(-2, 0, -0.517827),(0, 0, -2),(2, 0, 0),(0.536575, 0, 2.809361),(-3.191884, 0, 1.292017),(-2.772303, 0, -2.117866),(-0.771699, 0, -3),(1.229059, 0, -3),(3, 0, -1.863394),(3.950518, 0, 0.314344),(3, 0, 3.347373),(0, 0, 4.152682)], k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,11,11])

		
def create_single_arrow():
    global control
    control = pm.curve(d=1, p=[(0, 1.003235, 0),(0.668823, 0, 0),(0.334412, 0, 0),(0.334412, -0.167206, 0),(0.334412, -0.501617, 0),(0.334412, -1.003235, 0),(-0.334412, -1.003235, 0),(-0.334412, -0.501617, 0),(-0.334412, -0.167206, 0),(-0.334412, 0, 0),(-0.668823, 0, 0),(0, 1.003235, 0)], k=[0,1,2,3,4,5,6,7,8,9,10,11])

      
def create_curved_single_arrow():
    global control
    control = pm.curve(d=1, p=[(-0.251045, 0, 1.015808),(-0.761834, 0, 0.979696),(-0.486547, 0, 0.930468),(-0.570736, 0, 0.886448),(-0.72786, 0, 0.774834),(-0.909301, 0, 0.550655),(-1.023899, 0, 0.285854),(-1.063053, 0, 9.80765e-009),(-0.961797, 0, 8.87346e-009),(-0.926399, 0, 0.258619),(-0.822676, 0, 0.498232),(-0.658578, 0, 0.701014),(-0.516355, 0, 0.802034),(-0.440202, 0, 0.841857),(-0.498915, 0, 0.567734),(-0.251045, 0, 1.015808),], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    pm.xform(cp=True)


def create_double_arrow():
    global control
    control = pm.curve(d=1, p=[(0, 1, 0),(1, 1, 0),(2, 1, 0),(3, 1, 0),(3, 2, 0),(4, 1, 0),(5, 0, 0),(4, -1, 0),(3, -2, 0),(3, -1, 0),(2, -1, 0),(1, -1, 0),(0, -1, 0),(-1, -1, 0),(-2, -1, 0),(-3, -1, 0),(-3, -2, 0),(-4, -1, 0),(-5, 0, 0),(-4, 1, 0),(-3, 2, 0),(-3, 1, 0),(-2, 1, 0),(-1, 1, 0),(0, 1, 0),], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    pm.xform(cp=True)
    pm.scale(.2,.2,.2)
    pm.makeIdentity(apply=True, t=True, r=True, s=True)

	 
def create_curved_double_arrow():
    global control
    control = pm.curve(d=1, p=[(-0.251045, 0, -1.015808), (-0.761834, 0, -0.979696), (-0.486547, 0, -0.930468), (-0.570736, 0, -0.886448), (-0.72786, 0, -0.774834), (-0.909301, 0, -0.550655), (-1.023899, 0, -0.285854), (-1.063053, 0, 9.80765e-009), (-1.023899, 0, 0.285854), (-0.909301, 0, 0.550655), (-0.72786, 0, 0.774834), (-0.570736, 0, 0.886448), (-0.486547, 0, 0.930468), (-0.761834, 0, 0.979696), (-0.251045, 0, 1.015808), (-0.498915, 0, 0.567734), (-0.440202, 0, 0.841857), (-0.516355, 0, 0.802034), (-0.658578, 0, 0.701014), (-0.822676, 0, 0.498232), (-0.926399, 0, 0.258619), (-0.961797, 0, 8.87346e-009), (-0.926399, 0, -0.258619), (-0.822676, 0, -0.498232), (-0.658578, 0, -0.701014), (-0.516355, 0, -0.802034), (-0.440202, 0, -0.841857), (-0.498915, 0, -0.567734), (-0.251045, 0, -1.015808)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
    pm.makeIdentity(apply=True, t=True, r=True, s=True)
    pm.xform(cp=True)

    
def create_triple_arrow():
    global control
    control = pm.curve(d=1, p=[(-1, 1, 0),(-3, 1, 0),(-3, 2, 0),(-5, 0, 0),(-3, -2, 0),(-3, -1, 0),(-1, -1, 0),(1, -1, 0),(3, -1, 0),(3, -2, 0),(5, 0, 0),(3, 2, 0),(3, 1, 0),(1, 1, 0),(1, 3, 0),(2, 3, 0),(0, 5, 0),(-2, 3, 0),(-1, 3, 0),(-1, 1, 0),], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])    	
    pm.xform(cp=True)
    pm.xform(t=[0,-1.5,0])
    pm.scale(.2,.2,.2)
    pm.makeIdentity(apply=True, t=True, r=True, s=True)


def create_quad_arrow():
    global control
    control = pm.curve(d=1, p=[(1, 0, 1),(3, 0, 1),(3, 0, 2),(5, 0, 0),(3, 0, -2),(3, 0, -1),(1, 0, -1),(1, 0, -3),(2, 0, -3),(0, 0, -5),(-2, 0, -3),(-1, 0, -3),(-1, 0, -1),(-3, 0, -1),(-3, 0, -2),(-5, 0, 0),(-3, 0, 2),(-3, 0, 1),(-1, 0, 1),(-1, 0, 3),(-2, 0, 3),(0, 0, 5),( 2, 0, 3),(1, 0, 3),(1, 0, 1),], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    pm.xform(cp=True)
    pm.scale(.2,.2,.2)
    pm.makeIdentity(apply=True, t=True, r=True, s=True)

    
def create_cube():
    global control
    control = pm.curve(d=1, p=[(1, 1, 1),(1, 1, -1),(-1, 1, -1),(-1, 1, 1),(1, 1, 1),(1, -1, 1),(1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, -1),(-1, -1, -1),(-1, -1, 1),(-1, 1, 1),(-1, -1, 1),(1, -1, 1)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

	
def create_diamond():
    global control
    control = pm.curve(d=1, p=[(0, 1, 0),(-1, 0.00278996, 6.18172e-08),(0, 0, 1),(0, 1, 0),(1, 0.00278996, 0),(0, 0, 1),(1, 0.00278996, 0),(0, 0, -1),(0, 1, 0),(0, 0, -1),(-1, 0.00278996, 6.18172e-08),(0, -1, 0),(0, 0 ,-1),(1, 0.00278996, 0),(0, -1, 0),(0, 0, 1)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


def create_ring():
    global control
    control = pm.curve(d=1, p=[(-0.707107, 0.0916408, 0.707107),(0, 0.0916408, 1), (0, -0.0916408, 1), (-0.707107, -0.0916408, 0.707107), (-0.707107, 0.0916408, 0.707107),(-1, 0.0916408, 0), (-1, -0.0916408, 0), (-0.707107, -0.0916408, 0.707107), (-1, -0.0916408, 0), (-0.707107, -0.0916408, -0.707107), (-0.707107, 0.0916408, -0.707107), (-1, 0.0916408, 0), (-0.707107, 0.0916408, -0.707107), (0, 0.0916408, -1), (0, -0.0916408, -1), (-0.707107, -0.0916408, -0.707107),(-0.707107, 0.0916408, -0.707107), (-0.707107, -0.0916408, -0.707107), (0, -0.0916408, -1), (0.707107, -0.0916408, -0.707107), (0.707107, 0.0916408, -0.707107), (0, 0.0916408, -1), (0.707107, 0.0916408, -0.707107), (1, 0.0916408, 0), (1, -0.0916408, 0), (0.707107, -0.0916408, -0.707107), (1, -0.0916408, 0), (0.707107, -0.0916408, 0.707107), (0.707107, 0.0916408, 0.707107), (1, 0.0916408, 0), (0.707107, 0.0916408, 0.707107),(0, 0.0916408, 1), (0, -0.0916408, 1), (0.707107, -0.0916408, 0.707107)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])
   

def create_cone():
    global control
    control = pm.curve(d=1, p=[(-0.5, -1, 0.866025),(0, 1, 0),(0.5, -1, 0.866025),(-0.5, -1, 0.866025),(-1, -1, -1.5885e-07),(0, 1, 0),(-1, -1, -1.5885e-07),(-0.5, -1, -0.866026),(0, 1, 0),(0.5, -1, -0.866025),(-0.5, -1, -0.866026),(0.5, -1, -0.866025),(0, 1, 0),(1, -1, 0), (0.5, -1, -0.866025),(1, -1, 0),(0.5, -1, 0.866025)  ], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])


def create_orb():
    global control
    control = pm.circle(nr=[0,1,0])[0]
    
    circle_list = []
    circle_list.append(pm.duplicate(rr=True))
    pm.xform(ro=[90,0,0])
    
    circle_list.append(pm.duplicate(rr=True))
    pm.xform(ro=[90,90,0])
    
    circle_list.append(pm.duplicate(rr=True))
    pm.xform(ro=[90,45,0])
    
    circle_list.append(pm.duplicate(rr=True))
    pm.xform(ro=[90,-45,0])

    pm.select(circle_list)
    pm.makeIdentity(apply=True, t=True, r=True, s=True)
    pm.pickWalk(d='down')
    pm.select(control, tgl=True)
    pm.parent(r=True, s=True)
    pm.delete(circle_list)
    pm.xform(control, cp=True)
    
    return control

	
def create_lever():
    line = pm.curve(d=1, p=[(0, -1, 0),(0, -2, 0 ),(0, -3, 0 ),(0, -4, 0),(0, -5, 0)], k=[0,1,2,3,4])
    create_orb()
    
    pm.select(line, r=True)
    pm.pickWalk(d='down')
    pm.select(control, tgl=True)
    pm.parent(r=True, s=True)
    
    pm.delete(line)
    pm.xform(control, rp=[0,-5,0], sp=[0,-5,0])
    pm.xform(control, t=[0,5,0])
    pm.scale(.2,.2,.2)
    pm.makeIdentity(control, apply=True, t=True, r=True, s=True)

    
def create_jack():
    cross = pm.curve(d=1, p=[(0, 0, 0.75),(0, 0, 0),(0, 0, -0.75),(0, 0, 0),(0.75, 0, 0),(0, 0, 0),(-0.75, 0, 0),(0, 0, 0),(0, 0.75, 0),(0, 0, 0),(0, -0.75, 0)], k=[0,1,2,3,4,5,6,7,8,9,10])
    create_diamond()
    pm.scale(.3,.3,.3)
    pm.xform(t=[0,0,1])
    
    diamond_list=[]
    
    diamond_list.append(pm.duplicate(rr=True))
    pm.xform(t=[1,0,0])
    diamond_list.append(pm.duplicate(rr=True))
    pm.xform(t=[-1,0,0])
    diamond_list.append(pm.duplicate(rr=True))
    pm.xform(t=[0,-1,0])
    diamond_list.append(pm.duplicate(rr=True))
    pm.xform(t=[0,1,0])
    diamond_list.append(pm.duplicate(rr=True))
    pm.xform(t=[0,0,-1])
    
    pm.makeIdentity(control, apply=True, t=True, r=True, s=True)
    pm.select(diamond_list, r=True)
    pm.select(cross, tgl=True)
    
    pm.makeIdentity(apply=True, t=True, r=True, s=True)
    pm.pickWalk(d='down')
    pm.select(control, tgl=True)
    pm.parent(s=True, r=True)
    pm.xform(control, cp=True)
    
    pm.delete(diamond_list)
    pm.delete(cross)


def create_pointer():
    global control
    control = pm.curve(d=1, p=[(0, 1.003235, 0),(0.668823, 0, 0),(0.334412, 0, 0),(0.334412, -0.167206, 0),(0.334412, -0.501617, 0),(0.334412, -1.003235, 0),(-0.334412, -1.003235, 0),(-0.334412, -0.501617, 0),(-0.334412, -0.167206, 0),(-0.334412, 0, 0),(-0.668823, 0, 0),(0, 1.003235, 0),(0, 0, -0.668823),(0, 0, -0.334412),(0, -0.167206, -0.334412),(0, -0.501617, -0.334412),(0, -1.003235, -0.334412),(0, -1.003235, 0.334412),(0, -0.501617, 0.334412),(0, -0.167206, 0.334412),(0, 0, 0.334412),(0, 0, 0.668823),(0, 1.003235, 0)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])


def create_char(var):
    global control
    pm.textCurves(ch=0, f='Times New Roman', t=var)
    pm.ungroup()
    pm.ungroup()
    control = pm.ls(sl=True)[0]
    pm.xform(cp=True)
    
    
def create_text(var):
    global control
    
    pm.textCurves(ch=0, f='Times New Roman', t=var)
    pm.ungroup()
    pm.ungroup()
    
    curves = pm.ls(sl=True)
    pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    shapes = curves[1:]
    pm.select(shapes, r=True)
    pm.pickWalk(d='Down')
    pm.select(curves[0], tgl=True)
    pm.parent(r=True, s=True)
    pm.pickWalk(d='up')
    control = pm.ls(sl=True)[0]
    pm.delete(shapes)
    
    pm.xform(cp=True)
    pm.xform(ws=True, t=[0,0,0])


    

# Work Functions
def rename_control(control, i):
    prefix = ctrl_prefix_field.getText()
    name = ctrl_name_field.getText()
    suffix = ctrl_suffix_field.getText()
    
    if name != '':
	pm.rename(control, name + str(i))
    
    if prefix != '':
	pm.rename(control, prefix + '_'+ control)
	
    if suffix != '':
	pm.rename(control, control + '_' + suffix)


def select_hierarchy():
    pm.select(hi=True)
    snap_objects = pm.ls(sl=True)
    snap_objects.pop(-1)
    
    return snap_objects
    
    
def create_control(snap_object, control):
    snap_to_object(control, snap_object)
    rename_control(control, 0)
    create_grouping(control, snap_object)
    freeze_control(control)
    create_constraint(snap_object, control)

    
def create_multiple_controls(control, indiv_object, parent_control, i):
    snap_to_object(control, indiv_object)
    rename_control(control, i)
    
    null_group = create_grouping(control, indiv_object)
    
    check_hierarchy(null_group, parent_control)
    freeze_control(control)
    create_constraint(indiv_object, control)


def freeze_control(control):
    pm.makeIdentity(control, apply=True, t=True, r=True, s=True)
	

def zero_control(control):
    pm.xform(control, t=(0,0,0), ro=(0,0,0))
    
    
def snap_to_object(control, snap_object):    
    if (snap_optionMenu.getSelect()) == 2:
	constraint = pm.parentConstraint(snap_object, control)
	pm.delete(constraint)
	pm.makeIdentity(control, apply=True, t=True, r=True, s=True)
    
	
def move_to_object(control, snap_object):
    if (snap_optionMenu.getSelect()) == 2:
	constraint = pm.pointConstraint(snap_object, control, mo=False)
	pm.delete(constraint)
	pm.makeIdentity(control, apply=True, t=True, r=True, s=True)


def create_grouping(control, snap_object):
    if (group_optionMenu.getSelect()) == 2:
	pivot = pm.xform(snap_object, q=True, ws=True, rp=True)
	
	pm.select(control, snap_object, r=True)
	pm.parent()
	grp2 = pm.group()
	pm.xform(ws=True, rp=pivot)
	grp1 = pm.group()
	pm.xform(ws=True, rp=pivot)
	pm.parent(w=True)
	
	rename_groups(grp1, grp2, control)
	
	return grp1
    
    
def rename_groups(grp1, grp2, control):
    grp1_prefix = grp1_prefix_field.getText()
    grp1_name = grp1_name_field.getText()
    grp1_suffix = grp1_suffix_field.getText()
    
    if grp1_name == '':
	pm.rename(grp1, control)
    else:
	pm.rename(grp1, grp1_name)
    
    if grp1_prefix != '':
	pm.rename(grp1, grp1_prefix + '_' + grp1)
	
    if grp1_suffix != '':
	pm.rename(grp1, grp1 + '_' + grp1_suffix)
	
	
    grp2_prefix = grp2_prefix_field.getText()
    grp2_name = grp2_name_field.getText()
    grp2_suffix = grp2_suffix_field.getText()
    
    if grp2_name == '':
	pm.rename(grp2, control)
    else:
	pm.rename(grp2, grp2_name)
    
    if grp2_prefix != '':
	pm.rename(grp2, grp2_prefix + '_' + grp2)
	
    if grp2_suffix != '':
	pm.rename(grp2, grp2 + '_' + grp2_suffix)
	
    
def create_constraint(constrained_object, control):
    if group_optionMenu.getSelect() == 2:
	if constraint_optionMenu.getSelect() == 2:
	    pm.orientConstraint(control, constrained_object)
	elif constraint_optionMenu.getSelect() == 3:
	    pm.parentConstraint(control, constrained_object, mo=True)
    
    
def check_hierarchy(null_group, parent_control):
    if hierarchy_optionMenu.getSelect() == 2:
	if parent_control != '':
	    pm.parent(null_group, parent_control)
    

def apply_button(*args):
    selection = pm.ls(sl=True)
    
    if duplicate_optionMenu.getSelect() == 1:
	applyButton_singleObject(selection)
	
	
    elif duplicate_optionMenu.getSelect() == 2:
	applyButton_objectChain(selection)

	
    
def applyButton_singleObject(selection):
    null_grp = create_grouping(selection[0], selection[1])
    freeze_control(selection[0])
    create_constraint(selection[1], selection[0])

    return null_grp

    
def applyButton_objectChain(selection):
    pm.select(selection[1], hi=True)
    object_chain = pm.ls(sl=True)
    object_chain.pop(-1)
    parent_control=''
    
    curve_list = []
    nullGrp_list = []
    
    
    for each in object_chain:
	if each == object_chain[0]:
	    control=selection[0]
	    curve_list.append(control)
	    
	    applyButton_singleObject(selection)
	    pm.select(control, r=True)
	    parent_control = control
	else:
	    curve_list.append(control)
	    
	    null_grp = create_grouping(control, each)
	    nullGrp_list.append(null_grp)
	    pm.select(control, r=True)
	    
	    zero_control(control)
	    create_constraint(each, control)
	    parent_control = control
 
	pm.duplicate(control)
	control = pm.ls(sl=True)[0]

    
    pm.delete(control)
    create_hierarchy(nullGrp_list, curve_list)
    
    

def create_hierarchy(nullGrp_list, curve_list):
    if hierarchy_optionMenu.getSelect() == 2:
	curve_list.pop(-1)
	curve_list.reverse()
	nullGrp_list.reverse()
	
	for i, each in enumerate(nullGrp_list):
	    pm.parent(nullGrp_list[i], curve_list[i])
	    pm.select(cl=True)
    
    
    
    
    
    
    
    