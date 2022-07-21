##############################################################################################
'''
mz_ctrlCreator v1.0.0
by Mingquan Zhou
2012.1.27
m.charles.zhou@gmail.com

Description:
	This scirpt uses to create controllers.

Instruction:
	1. put the mz_icons folder to ...maya\20**\prefs\icons\
	2. put the mz_ctrlCreator.py to ...maya\20**\scripts\
	3. type following commands in command line (Python mode):
			import  mz_ctrlCreator
			reload(mz_ctrlCreator)

Reference:
	kk_controllers v1.7 by Karim Kashefy
'''
##############################################################################################

import maya.cmds as cmds

#############################################
'''global variable, the name of the window'''
#############################################

#global varibles
mz_ccWin = 'mz_ctrlCreatorWin'
mz_ctrlColor = 'ctrlColor'
mz_groupsNum = 'groupsNum'

iconPath = r'D:\True_Axion\Tools\riggerTools\image\mz_icons'

# image = iconPath + '\\bullet_interactivePlayback.png'
#create the window
def mz_ctrlCreator():
	#if the window is exsit, delete it
	if cmds.window(mz_ccWin, exists = 1):
		cmds.deleteUI(mz_ccWin, window = 1)
	
	#run the function to create the window
	mz_ccUI()

	#initial the window position and size
	cmds.windowPref(mz_ccWin, remove = True)
	cmds.window(mz_ccWin, edit = True,  topLeftCorner = (200, 200))
	#show the window
	cmds.showWindow(mz_ccWin)
	
	
#############################################
'''making the GUI of the window'''
#############################################
#ctrlCreator GUI
def mz_ccUI():
	#initial the window
	ccWin = cmds.window(mz_ccWin, title = 'mz_ctrlCreator v1.0.0', resizeToFitChildren = 1,  sizeable = 0)
	
	#the main layout -- column
	mainLayout = cmds.columnLayout( adjustableColumn = 1, width = 300)
	
	#layout of the "group" set
	cmds.frameLayout(label = 'Groups')
	cmds.columnLayout(columnAttach = ('left', 0))
	cmds.intFieldGrp(mz_groupsNum, numberOfFields = 1, label = 'number of group: ', value1 = 0 )
	cmds.setParent(mainLayout)

	#layout of the "controllers" set
	cmds.frameLayout(label = 'Controllers')
	cmds.scrollLayout(childResizable = 1)
	cmds.gridLayout(numberOfColumns = 7, cellWidthHeight = (40, 40), width = 100)
	
	#icons of the "controllers" 
	cmds.symbolButton(image = iconPath + '\\ccButton01.PNG', command = mz_ccButtonSnap01)
	cmds.symbolButton(image = iconPath + '\\ccButton02.PNG', command = mz_ccButtonSnap02)
	cmds.symbolButton(image = iconPath + '\\ccButton03.PNG', command = mz_ccButtonSnap03)
	cmds.symbolButton(image = iconPath + '\\ccButton04.PNG', command = mz_ccButtonSnap04)
	cmds.symbolButton(image = iconPath + '\\ccButton05.PNG', command = mz_ccButtonSnap05)
	cmds.symbolButton(image = iconPath + '\\ccButton06.PNG', command = mz_ccButtonSnap06)
	cmds.symbolButton(image = iconPath + '\\ccButton07.PNG', command = mz_ccButtonSnap07)
	cmds.symbolButton(image = iconPath + '\\ccButton08.PNG', command = mz_ccButtonSnap08)
	cmds.symbolButton(image = iconPath + '\\ccButton09.PNG', command = mz_ccButtonSnap09)
	cmds.symbolButton(image = iconPath + '\\ccButton10.PNG', command = mz_ccButtonSnap10)
	cmds.symbolButton(image = iconPath + '\\ccButton11.PNG', command = mz_ccButtonSnap11)
	cmds.symbolButton(image = iconPath + '\\ccButton12.PNG', command = mz_ccButtonSnap12)
	cmds.symbolButton(image = iconPath + '\\ccButton13.PNG', command = mz_ccButtonSnap13)
	cmds.symbolButton(image = iconPath + '\\ccButton14.PNG', command = mz_ccButtonSnap14)
	cmds.symbolButton(image = iconPath + '\\ccButton15.PNG', command = mz_ccButtonSnap15)
	cmds.symbolButton(image = iconPath + '\\ccButton16.PNG', command = mz_ccButtonSnap16)
	cmds.symbolButton(image = iconPath + '\\ccButton17.PNG', command = mz_ccButtonSnap17)
	cmds.symbolButton(image = iconPath + '\\ccButton18.PNG', command = mz_ccButtonSnap18)
	cmds.symbolButton(image = iconPath + '\\ccButton19.PNG', command = mz_ccButtonSnap19)
	cmds.symbolButton(image = iconPath + '\\ccButton20.PNG', command = mz_ccButtonSnap20)
	cmds.symbolButton(image = iconPath + '\\ccButton21.PNG', command = mz_ccButtonSnap21)
	cmds.symbolButton(image = iconPath + '\\ccButton22.PNG', command = mz_ccButtonSnap22)
	cmds.symbolButton(image = iconPath + '\\ccButton23.PNG', command = mz_ccButtonSnap23)
	cmds.symbolButton(image = iconPath + '\\ccButton24.PNG', command = mz_ccButtonSnap24)
	cmds.symbolButton(image = iconPath + '\\ccButton25.PNG', command = mz_ccButtonSnap25)
	cmds.symbolButton(image = iconPath + '\\ccButton26.PNG', command = mz_ccButtonSnap26)
	cmds.symbolButton(image = iconPath + '\\ccButton27.PNG', command = mz_ccButtonSnap27)
	cmds.symbolButton(image = iconPath + '\\ccButton28.PNG', command = mz_ccButtonSnap28)
	cmds.symbolButton(image = iconPath + '\\ccButton29.PNG', command = mz_ccButtonSnap29)
	cmds.symbolButton(image = iconPath + '\\ccButton30.PNG', command = mz_ccButtonSnap30)
	cmds.symbolButton(image = iconPath + '\\ccButton31.PNG', command = mz_ccButtonSnap31)
	cmds.symbolButton(image = iconPath + '\\ccButton32.PNG', command = mz_ccButtonSnap32)
	cmds.symbolButton(image = iconPath + '\\ccButton33.PNG', command = mz_ccButtonSnap33)
	cmds.symbolButton(image = iconPath + '\\ccButton34.PNG', command = mz_ccButtonSnap34)
	cmds.symbolButton(image = iconPath + '\\ccButton35.PNG', command = mz_ccButtonSnap35)
	cmds.symbolButton(image = iconPath + '\\ccButton36.PNG', command = mz_ccButtonSnap36)
	cmds.symbolButton(image = iconPath + '\\ccButton37.PNG', command = mz_ccButtonSnap37)
	cmds.symbolButton(image = iconPath + '\\ccButton38.PNG', command = mz_ccButtonSnap38)
	cmds.symbolButton(image = iconPath + '\\ccButton39.PNG', command = mz_ccButtonSnap39)
	cmds.symbolButton(image = iconPath + '\\ccButton40.PNG', command = mz_ccButtonSnap40)
	cmds.symbolButton(image = iconPath + '\\ccButton41.PNG', command = mz_ccButtonSnap41)
	cmds.symbolButton(image = iconPath + '\\ccButton42.PNG', command = mz_ccButtonSnap42)
	cmds.symbolButton(image = iconPath + '\\ccButton43.PNG', command = mz_ccButtonSnap43)
	cmds.symbolButton(image = iconPath + '\\ccButton44.PNG', command = mz_ccButtonSnap44)
	cmds.symbolButton(image = iconPath + '\\ccButton45.PNG', command = mz_ccButtonSnap45)
	cmds.setParent(mainLayout)
	
	#layout of the "Mirror" set 
	cmds.frameLayout(label = 'Mirror')
	cmds.columnLayout(columnWidth = 100, columnAttach = ('left', 65))
	cmds.rowLayout(numberOfColumns = 3, columnWidth3 = (60, 60, 60),  columnAlign = (50, 'left'))
	cmds.button(label = '   X   ', command = mz_mirrorX)
	cmds.button(label = '   Y   ', command = mz_mirrorY)
	cmds.button(label = '   Z   ', command = mz_mirrorZ)
	cmds.setParent(mainLayout)

	#layout of the "Color" set     
	cmds.frameLayout(label = 'Color')
	cmds.columnLayout(columnAttach = ('left', 5))
	cmds.colorIndexSliderGrp(mz_ctrlColor, minValue = 1, maxValue = 31, value = 16, columnWidth = (1,60), columnWidth2 = (1, 220),\
							  dragCommand = mz_hideManipulator, changeCommand = mz_showManipulator)    
	cmds.setParent(mainLayout)

	#button of Combine Shapes and Freeze Transformations
	cmds.button(label = 'Combine Shapes', command = mz_combineShapes)
	cmds.button(label = 'Make Groups', command = mz_makeGroups)
	cmds.button(label = 'Center Pivot', command = mz_centerPivot)  
	cmds.button(label = 'Freeze Transformations', command = mz_freezeTrans)
	

#############################################
'''set the color to the contollers'''
#############################################

#hide the manipulators when changing the color of the ctrl
def mz_hideManipulator():
	#activate the window
	selPanel = cmds.getPanel(withFocus = 1)
	#hide the manipulators
	cmds. modelEditor(selPanel, edit = 1,  selectionHiliteDisplay = 0, manipulators = 0)
	#set the color
	mz_setColor()

#show the manipulators when the color has set
def mz_showManipulator():
	#activate the window
	selPanel = cmds.getPanel(withFocus = 1)
	#show the manipulators
	cmds. modelEditor(selPanel, edit = 1,  selectionHiliteDisplay = 1, manipulators = 1)

#set the color of the ctrl
def mz_setColor():
	selColor = cmds.colorIndexSliderGrp(mz_ctrlColor, query = 1, value = 1)
	selCtrl = cmds.ls(selection = 1)
	for ctrl in selCtrl:
		#turn on the overrideEnabled attribute
		cmds.setAttr(ctrl + ".overrideEnabled", 1)
		#set the overrideColor attribute
		cmds.setAttr(ctrl + ".overrideColor", (selColor - 1))


#############################################
'''Groups'''
#############################################
#mz_groups
def mz_groups():
	groupValue = cmds.intFieldGrp(mz_groupsNum, query = 1, value1 = 1)
	return groupValue

def mz_makeGroups(self):    
	selObj = cmds.ls(selection = 1)
	#if no object is selected
	if len(selObj) == 0:
		#if number of group is 0
		if mz_groups() == 0 :
			cmds.warning('Please input a number at "number of group:" ')
		else:
			#create a empty group
			cmds.group(empty = 1)
			for i in xrange(mz_groups()-1):
				cmds.group()
	else:
		#when the number of group is not 0
		if mz_groups() > 0:
			for j in xrange(len(selObj)):
				cmds.select(selObj[j])
				#get the transformations info
				objRot = cmds.xform(selObj[j], query = 1, worldSpace = 1, rotation = 1)
				objTrans = cmds.xform(selObj[j], query = 1, worldSpace = 1, translation = 1)
				objScale = cmds.xform(selObj[j], query = 1, relative = 1, scale = 1)
				#set the ctrl back to the center of the scene
				cmds.xform(selObj[j], worldSpace = 1, translation = (0,0,0), rotation = (0,0,0), scale = (1,1,1))
				#group the ctrl
				for k in xrange(mz_groups()):
					cmds.group()
					cmds.xform(pivots = (0, 0, 0))
				#get the name of the last group
				selGroup = cmds.ls(selection = 1)
				#set the last group back to the original position of the ctrl
				cmds.xform(selGroup, worldSpace = 1, translation = objTrans, rotation = objRot, scale = objScale)
				

#############################################
'''Mirror'''
#############################################

#unlock the attributes of translate, rotate and scale
def mz_unlockAttrs():
	selObj = cmds.ls(selection = 1)
	for i in xrange(len(selObj)):
		cmds.setAttr(selObj[i] + ".tx", keyable = 1, lock = 0)
		cmds.setAttr(selObj[i] + ".ty", keyable = 1, lock = 0)
		cmds.setAttr(selObj[i] + ".tz", keyable = 1, lock = 0)
		
		cmds.setAttr(selObj[i] + ".rx", keyable = 1, lock = 0)
		cmds.setAttr(selObj[i] + ".ry", keyable = 1, lock = 0)
		cmds.setAttr(selObj[i] + ".rz", keyable = 1, lock = 0)
		
		cmds.setAttr(selObj[i] + ".sx", keyable = 1, lock = 0)
		cmds.setAttr(selObj[i] + ".sy", keyable = 1, lock = 0)
		cmds.setAttr(selObj[i] + ".sz", keyable = 1, lock = 0)

#mirror X axis
def mz_mirrorX(self):
	mz_unlockAttrs()
	mirrorGrpX = cmds.group()
	cmds.xform(objectSpace = 1,  pivots = (0, 0, 0), scale = (-1, 1, 1))
	cmds.ungroup(mirrorGrpX)
	cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)

#mirror Y axis
def mz_mirrorY(self):
	mz_unlockAttrs()
	mirrorGrpY = cmds.group()
	cmds.xform(objectSpace = 1,  pivots = (0, 0, 0), scale = (1, -1, 1))
	cmds.ungroup(mirrorGrpY)
	cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
	
#mirror Z axis
def mz_mirrorZ(self):
	mz_unlockAttrs()
	mirrorGrpZ = cmds.group()
	cmds.xform(objectSpace = 1,  pivots = (0, 0, 0), scale = (1, 1, -1))
	cmds.ungroup(mirrorGrpZ)
	cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)


#############################################
'''Combine Shapes'''
#############################################

def mz_combineShapes(self):
	#store the names of transform nodes
	selObj = cmds.ls(selection = 1)
	#freeze transformations
	cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
	#delete history
	cmds.delete(constructionHistory = 1)
	#store the names of shape nodes
	objShape = cmds.listRelatives(selObj, shapes = 1)
	
	for i in xrange(len(objShape)-1):
		#parent the shape nodes to the last transform node
		cmds.parent(objShape[i],selObj[-1],add = 1, shape = 1)
		#delete the unused transform nodes
		cmds.delete(selObj[i])
		cmds.select(selObj[-1], replace = 1)


#############################################
'''enter Pivot'''
#############################################

def mz_centerPivot(self):
	cmds.xform(centerPivots = 1)


#############################################
'''Freeze Transformations'''
#############################################

def mz_freezeTrans(self):
	mz_unlockAttrs()
	cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
	

#########################################################
'''create the controllers
make the controller can snap to the selected object(s)'''
#########################################################

#mz_ccButton01
def mz_ccButton01(self):
	cmds.curve( degree = 3,\
				knot = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\
				point = [(1.9590290622280626, 1.199559335247117e-016, -1.9590290622280595),\
						 (-3.1607926519573314e-016, 1.6964330807777285e-016, -2.7704854688859699),\
						 (-1.9590290622280606, 1.1995593352471178e-016, -1.9590290622280606),\
						 (-2.7704854688859699, 4.9158386540469646e-032, -8.0281737680930749e-016),\
						 (-1.9590290622280613, -1.1995593352471173e-016, 1.9590290622280602),\
						 (-8.3480134089762987e-016, -1.6964330807777287e-016, 2.7704854688859704),\
						 (1.9590290622280595, -1.199559335247118e-016, 1.9590290622280611),\
						 (2.7704854688859699, -9.1115751697619806e-032, 1.4880331498201463e-015),\
						 (1.9590290622280626, 1.199559335247117e-016, -1.9590290622280595),\
						 (-3.1607926519573314e-016, 1.6964330807777285e-016, -2.7704854688859699),\
						 (-1.9590290622280606, 1.1995593352471178e-016, -1.9590290622280606)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
			  
#mz_ccButtonSnap01
def mz_ccButtonSnap01(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton01(self)
		cmds.select(clear = 1)
	
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton01(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
		
		
#mz_ccButton02
def mz_ccButton02(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],\
				point = [(-0.5, 0.5, -0.5),\
						 (-0.5, 0.5, 0.5),\
						 (0.5, 0.5, 0.5),\
						 (0.5, 0.5, -0.5),\
						 (-0.5, 0.5, -0.5),\
						 (-0.5, -0.5, -0.5),\
						 (-0.5, -0.5, 0.5),\
						 (0.5, -0.5, 0.5),\
						 (0.5, 0.5, 0.5),\
						 (-0.5, 0.5, 0.5),\
						 (-0.5, -0.5, 0.5),\
						 (-0.5, -0.5, -0.5),\
						 (0.5, -0.5, -0.5),\
						 (0.5, 0.5, -0.5),\
						 (0.5, 0.5, 0.5),\
						 (0.5, -0.5, 0.5),\
						 (0.5, -0.5, -0.5)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap02
def mz_ccButtonSnap02(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton02(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton02(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
		
		
#mz_ccButton03
def mz_ccButton03(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7],\
				point = [(-2, 0, 0),\
						 (1, 0, 1),\
						 (1, 0, -1),\
						 (-2, 0, 0),\
						 (1, 1, 0),\
						 (1, 0, 0),\
						 (1, -1, 0),\
						 (-2, 0, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap03
def mz_ccButtonSnap03(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton03(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton03(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton04
def mz_ccButton04(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\
				point = [(-4, 0, 0),\
						 (-2, 0, -2),\
						 (-2, 0, -1),\
						 (2, 0, -1),\
						 (2, 0, -2),\
						 (4, 0, 0),\
						 (2, 0, 2),\
						 (2, 0, 1),\
						 (-2, 0, 1),\
						 (-2, 0, 2),\
						 (-4, 0, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap04
def mz_ccButtonSnap04(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton04(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton04(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)       
		 
		
#mz_ccButton05
def mz_ccButton05(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,\
						23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43],\
				point = [(-2.1213199999999999, 0, 2.1213199999999999),\
						 (-2.4275890000000002, 0, 1.760219),\
						 (-2.6713830000000001, 0, 1.3581639999999999),\
						 (-2.8528880000000001, 0, 0.91765300000000005),\
						 (-2.9599489999999999, 0, 0.47963099999999997),\
						 (-2.9999920000000002, 0, 0.0065315299999999998),\
						 (-2.9641760000000001, 0, -0.453565),\
						 (-2.8391410000000001, 0, -0.95904599999999995),\
						 (-2.6717170000000001, 0, -1.357504),\
						 (-2.4336000000000002, 0, -1.751819),\
						 (-2.1309930000000001, 0, -2.1116009999999998),\
						 (-1.7928569999999999, 0, -2.4038110000000001),\
						 (-1.387964, 0, -2.6561140000000001),\
						 (-0.942438, 0, -2.844735),\
						 (-0.46542499999999998, 0, -2.9622820000000001),\
						 (0.0084003199999999993, 0, -2.9999880000000001),\
						 (0.45493899999999998, 0, -2.963959),\
						 (0.94169899999999995, 0, -2.8449810000000002),\
						 (1.3494409999999999, 0, -2.6757759999999999),\
						 (1.7573289999999999, 0, -2.429662),\
						 (2.1288819999999999, 0, -2.1137299999999999),\
						 (2.411311, 0, -1.782662),\
						 (2.6613889999999998, 0, -1.377759),\
						 (2.8479290000000002, 0, -0.93281199999999997),\
						 (2.9608530000000002, 0, -0.47417700000000002),\
						 (2.9999989999999999, 0, 0.00169319),\
						 (2.964737, 0, 0.449986),\
						 (2.8521960000000002, 0, 0.91978700000000002),\
						 (2.6751839999999998, 0, 1.3506199999999999),\
						 (2.4316279999999999, 0, 1.7545809999999999),\
						 (2.124565, 0, 2.1180699999999999),\
						 (1.7739180000000001, 0, 2.417691),\
						 (1.3726860000000001, 0, 2.6639930000000001),\
						 (0.92380099999999998, 0, 2.8508870000000002),\
						 (0.40900599999999998, 0, 2.9708540000000001),\
						 (0, 0, 3),\
						 (0.62022299999999997, 0.59294500000000006, 3),\
						 (-1, 0, 3),\
						 (0.62022299999999997, -0.59294500000000006, 3),\
						 (0, 0, 3),\
						 (0.62022299999999997, 0, 2.4070550000000002),\
						 (-1, 0, 3),\
						 (0.62022299999999997, 0, 3.5929449999999998),\
						 (0, 0, 3)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap05
def mz_ccButtonSnap05(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton05(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton05(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)        
		
		
#mz_ccButton06
def mz_ccButton06(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,\
						23, 24, 25, 26, 27, 28, 29, 30, 31],\
				point = [(-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),\
						 (-2.9915446383506463, 2.5597753382632042, 0.23863999999999944),\
						 (-2.6540560067191499, 2.2222867066317078, 0.23863999999999949),\
						 (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),\
						 (-2.6540560067191499, 2.2222867066317078, 0.23863999999999949),\
						 (-2.6540560067191499, 2.2222867066317078, -0.23864000000000049),\
						 (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),\
						 (-2.6540560067191499, 2.2222867066317078, -0.23864000000000049),\
						 (-2.9915446383506463, 2.5597753382632042, -0.23864000000000055),\
						 (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),\
						 (-2.9915446383506463, 2.5597753382632042, 0.23863999999999944),\
						 (-2.9915446383506463, 2.5597753382632042, -0.23864000000000055),\
						 (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),\
						 (-2.6069153189377863, 2.6069153189377867, -5.7885148206655284e-016),\
						 (-1.9614611780028937, 3.1216480434482845, -6.931451065224713e-016),\
						 (-1.2176513122320769, 3.4798485398075156, -7.7268159422050689e-016),\
						 (-0.41278348301258339, 3.663554174453, -8.1347243928786562e-016),\
						 (0.41278348301258405, 3.6635541744529996, -8.1347243928786552e-016),\
						 (1.2176513122320776, 3.4798485398075156, -7.7268159422050689e-016),\
						 (1.9614611780028941, 3.1216480434482841, -6.931451065224712e-016),\
						 (2.6069153189377867, 2.6069153189377863, -5.7885148206655274e-016),\
						 (3.9723250783801674, 1.2415055594954054, -2.7566961147038725e-016),\
						 (2.6540560067191499, 2.2222867066317069, 0.23863999999999949),\
						 (2.9915446383506463, 2.5597753382632034, 0.23863999999999944),\
						 (3.9723250783801674, 1.2415055594954054, -2.7566961147038725e-016),\
						 (2.9915446383506463, 2.5597753382632034, 0.23863999999999944),\
						 (2.9915446383506463, 2.5597753382632034, -0.23864000000000055),\
						 (3.9723250783801674, 1.2415055594954054, -2.7566961147038725e-016),\
						 (2.6540560067191499, 2.2222867066317069, -0.23864000000000049),\
						 (2.9915446383506463, 2.5597753382632034, -0.23864000000000055),\
						 (2.6540560067191499, 2.2222867066317069, -0.23864000000000049),\
						 (2.6540560067191499, 2.2222867066317069, 0.23863999999999949)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap06
def mz_ccButtonSnap06(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton06(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton06(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)       
		 
		
#mz_ccButton07
def mz_ccButton07(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],\
				point = [(-2.187163, -0.5, -0.5),\
						 (-2.187163, -0.5, 0.5),\
						 (-2.187163, 0.5, 0.5),\
						 (-2.187163, 0.5, -0.5),\
						 (-2.187163, -0.5, -0.5),\
						 (-3.812837, 0, 0),\
						 (-2.187163, -0.5, 0.5),\
						 (-2.187163, 0.5, 0.5),\
						 (-3.812837, 0, 0),\
						 (-2.187163, 0.5, -0.5),\
						 (-3.812837, 0, 0),\
						 (0, 0, 0),\
						 (3.812837, 0, 0),\
						 (2.187163, 0.5, 0.5),\
						 (2.187163, 0.5, -0.5),\
						 (3.812837, 0, 0),\
						 (2.187163, 0.5, -0.5),\
						 (2.187163, -0.5, -0.5),\
						 (3.812837, 0, 0),\
						 (2.187163, -0.5, -0.5),\
						 (2.187163, -0.5, 0.5),\
						 (3.812837, 0, 0),\
						 (2.187163, -0.5, 0.5),\
						 (2.187163, 0.5, 0.5)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap07
def mz_ccButtonSnap07(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton07(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton07(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)        
		
		
#mz_ccButton08
def mz_ccButton08(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,\
						24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,\
						46, 47, 48, 49, 50, 51, 52, 53, 54, 55],\
				point = [(0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008),\
						 (0.932697, 1.2471760000000001, -0.35686000000000001),\
						 (0.92075200000000001, 1.1728350000000001, -0.68600300000000003),\
						 (0.89147600000000005, 1.068829, -0.97843500000000005),\
						 (0.84007600000000004, 0.94667800000000002, -1.2319290000000001),\
						 (0.76359100000000002, 0.81499100000000002, -1.4457660000000001),\
						 (0.66171500000000005, 0.68111100000000002, -1.621424),\
						 (0.53715500000000005, 0.551427, -1.765671),\
						 (0.38761699999999999, 0.43313299999999999, -1.880322),\
						 (0.20958599999999999, 0.33878000000000003, -1.961541),\
						 (0, 0.29736299999999999, -1.9937469999999999),\
						 (-0.20958599999999999, 0.33878000000000003, -1.961541),\
						 (-0.38761699999999999, 0.43313299999999999, -1.880322),\
						 (-0.53715500000000005, 0.551427, -1.765671),\
						 (-0.66171500000000005, 0.68111100000000002, -1.621424),\
						 (-0.76359100000000002, 0.81499100000000002, -1.4457660000000001),\
						 (-0.84007600000000004, 0.94667800000000002, -1.2319290000000001),\
						 (-0.89147600000000005, 1.068829, -0.97843500000000005),\
						 (-0.92075200000000001, 1.1728350000000001, -0.68600300000000003),\
						 (-0.932697, 1.2471760000000001, -0.35686000000000001),\
						 (-0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008),\
						 (-0.91757200000000005, 1.4706170000000001, 0),\
						 (-0.85697100000000004, 1.6571290000000001, 0),\
						 (-0.75891600000000004, 1.826965, 0),\
						 (-0.62769200000000003, 1.972704, 0),\
						 (-0.46903600000000001, 2.087974, 0),\
						 (-0.28988000000000003, 2.1677390000000001, 0),\
						 (-0.098055100000000006, 2.2085129999999999, 0),\
						 (0.098055100000000006, 2.2085129999999999, 0),\
						 (0.28988000000000003, 2.1677390000000001, 0),\
						 (0.46903600000000001, 2.087974, 0),\
						 (0.62769200000000003, 1.972704, 0),\
						 (0.75891600000000004, 1.826965, 0),\
						 (0.85697100000000004, 1.6571290000000001, 0),\
						 (0.91757200000000005, 1.4706170000000001, 0),\
						 (0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008),\
						 (0.932697, 1.2471760000000001, 0.35686000000000001),\
						 (0.92075200000000001, 1.1728339999999999, 0.68600300000000003),\
						 (0.89147600000000005, 1.0688299999999999, 0.97843500000000005),\
						 (0.84007600000000004, 0.94667800000000002, 1.23193),\
						 (0.76359100000000002, 0.81499200000000005, 1.445765),\
						 (0.66171500000000005, 0.68110999999999999, 1.621426),\
						 (0.53715500000000005, 0.55142999999999998, 1.7656689999999999),\
						 (0.38761699999999999, 0.43312699999999998, 1.8803259999999999),\
						 (0.20958599999999999, 0.33878799999999998, 1.9615359999999999),\
						 (0, 0.29731800000000003, 1.9937750000000001),\
						 (-0.20958599999999999, 0.33878799999999998, 1.9615359999999999),\
						 (-0.38761699999999999, 0.43312699999999998, 1.8803259999999999),\
						 (-0.53715500000000005, 0.55142999999999998, 1.7656689999999999),\
						 (-0.66171500000000005, 0.68110999999999999, 1.621426),\
						 (-0.76359100000000002, 0.81499200000000005, 1.445765),\
						 (-0.84007600000000004, 0.94667800000000002, 1.23193),\
						 (-0.89147600000000005, 1.0688299999999999, 0.97843500000000005),\
						 (-0.92075200000000001, 1.1728339999999999, 0.68600300000000003),\
						 (-0.932697, 1.2471760000000001, 0.35686000000000001),\
						 (-0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap08
def mz_ccButtonSnap08(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton08(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton08(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
							  
					  
#mz_ccButton09
def mz_ccButton09(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7],\
				point = [(-2, 0, 0),\
						 (2, 0, 0),\
						 (0, 0, 0),\
						 (0, 0, 2),\
						 (0, 0, -2),\
						 (0, 0, 0),\
						 (0, 2, 0),\
						 (0, -2, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap09
def mz_ccButtonSnap09(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton09(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton09(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
							  
					  
#mz_ccButton10
def mz_ccButton10(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
						39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
				point = [(0, 1, 0),\
						 (0, 0.92388000000000003, 0.382683),\
						 (0, 0.70710700000000004, 0.70710700000000004),\
						 (0, 0.382683, 0.92388000000000003),\
						 (0, 0, 1),\
						 (0, -0.382683, 0.92388000000000003),\
						 (0, -0.70710700000000004, 0.70710700000000004),\
						 (0, -0.92388000000000003, 0.382683),\
						 (0, -1, 0),\
						 (0, -0.92388000000000003, -0.382683),\
						 (0, -0.70710700000000004, -0.70710700000000004),\
						 (0, -0.382683, -0.92388000000000003),\
						 (0, 0, -1),\
						 (0, 0.382683, -0.92388000000000003),\
						 (0, 0.70710700000000004, -0.70710700000000004),\
						 (0, 0.92388000000000003, -0.382683),\
						 (0, 1, 0),\
						 (0.382683, 0.92388000000000003, 0),\
						 (0.70710700000000004, 0.70710700000000004, 0),\
						 (0.92388000000000003, 0.382683, 0),\
						 (1, 0, 0),\
						 (0.92388000000000003, -0.382683, 0),\
						 (0.70710700000000004, -0.70710700000000004, 0),\
						 (0.382683, -0.92388000000000003, 0),\
						 (0, -1, 0),\
						 (-0.382683, -0.92388000000000003, 0),\
						 (-0.70710700000000004, -0.70710700000000004, 0),\
						 (-0.92388000000000003, -0.382683, 0),\
						 (-1, 0, 0),\
						 (-0.92388000000000003, 0.382683, 0),\
						 (-0.70710700000000004, 0.70710700000000004, 0),\
						 (-0.382683, 0.92388000000000003, 0),\
						 (0, 1, 0),\
						 (0, 0.92388000000000003, -0.382683),\
						 (0, 0.70710700000000004, -0.70710700000000004),\
						 (0, 0.382683, -0.92388000000000003),\
						 (0, 0, -1),\
						 (-0.382683, 0, -0.92388000000000003),\
						 (-0.70710700000000004, 0, -0.70710700000000004),\
						 (-0.92388000000000003, 0, -0.382683),\
						 (-1, 0, 0),\
						 (-0.92388000000000003, 0, 0.382683),\
						 (-0.70710700000000004, 0, 0.70710700000000004),\
						 (-0.382683, 0, 0.92388000000000003),\
						 (0, 0, 1),\
						 (0.382683, 0, 0.92388000000000003),\
						 (0.70710700000000004, 0, 0.70710700000000004),\
						 (0.92388000000000003, 0, 0.382683),\
						 (1, 0, 0),\
						 (0.92388000000000003, 0, -0.382683),\
						 (0.70710700000000004, 0, -0.70710700000000004),\
						 (0.382683, 0, -0.92388000000000003),\
						 (0, 0, -1)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap10
def mz_ccButtonSnap10(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton10(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton10(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton11
def mz_ccButton11(self):
	#handCtrl
	handCtrl = cmds.curve( degree = 3,\
				knot = [24.684238740000001, 24.684238740000001, 24.684238740000001, 25, 26, 27, 28, 29, 30,\
						30.758475789999999, 31.626223939999999, 32.49397209, 33.361720239999997,\
						34.229468389999994	, 35.097216539999991, 35.964964689999988, 36.832712839999985,\
						37.700460989999982, 38.568209139999979, 39.435957289999976, 40.303705439999973,\
						41.17145358999997, 42.039201739999967, 42.906949889999964, 43.774698039999961,\
						44.642446189999959, 45.510194339999956, 46.377942489999953, 47.24569063999995,\
						48.113438789999947, 48.113438789999947, 48.113438789999947],\
				point = [(2.6512482552363492, -0.44091928826262577, 0.004029063622544393),\
						 (2.5887665424827091, -0.7560259313703569, 0.0040290636225444069),\
						 (2.1966825988479726, -1.7212327432979919, 0.0040290636225444945),\
						 (2.3737604079451313, -2.6324056420962623, 0.0040290636225444546),\
						 (1.9460056415041418, -3.8652504539923829, 0.00402906362254455),\
						 (-0.14594419514494811, -3.7388528673677346, 0.0040290636225450141),\
						 (-0.85609714412593019, -3.606417864398384, 0.0040290636225451719),\
						 (-1.253541668575024, -3.4277114913474862, 0.0040290636225452604),\
						 (-1.4500691830144992, -3.3374779789567017, 0.0040290636225453038),\
						 (-1.569721131888149, -3.2504927080601878, 0.0040290636225453307),\
						 (-1.3150935495419322, -2.1179798396582554, 0.0040290636225452743),\
						 (-1.0379510683787732, -1.9564432523874531, 0.0040290636225452127),\
						 (-1.0071574593606432, -1.5179868012238558, 0.0040290636225452058),\
						 (-1.0379510683787732, -0.20261744773304147, 0.0040290636225452127),\
						 (0.039825247255744149, 0.2127623481061619, 0.0040290636225449733),\
						 (0.88232801689266405, 0.15183220447463555, 0.0040290636225447859),\
						 (2.0722034424522673, -0.61799724357224484, 0.0040290636225445223),\
						 (2.3801395326335562, -0.87184045214064554, 0.0040290636225444538),\
						 (1.9490290063797471, -1.5872167671970603, 0.0040290636225445492),\
						 (0.87125269074523259, -0.9179937627894561, 0.0040290636225447886),\
						 (0.22458690136452156, -0.59492058824785088, 0.0040290636225449325),\
						 (-0.45287249703432231, -0.75645717551865355, 0.0040290636225450826),\
						 (-0.69922136917935418, -1.5410634565482497, 0.0040290636225451372),\
						 (-0.69922136917935418, -2.441053014199861, 0.0040290636225451372),\
						 (-0.021761970780513097, -2.7641261887414661, 0.0040290636225449872),\
						 (1.3639504350352962, -2.6256662567950571, 0.0040290636225446793),\
						 (0.87125269074523259, -2.1179798396582554, 0.0040290636225447886),\
						 (1.1483951719083945, -1.6564467331702533, 0.004029063622544727),\
						 (1.9490290063797471, -1.7487533544678628, 0.0040290636225445492),\
						 (2.2261714875429148, -2.1410564949826609, 0.0040290636225444876)]\
			  )
	#pinkyCtrl          
	pinkyCtrl = cmds.curve( degree = 3,\
				knot = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5],\
				point = [(2.6686783300760872, -0.44376961119187402, -0.0040290636225455744),\
						 (2.8868844886683429, 0.17943229893994614, -0.004029063622545623),\
						 (3.0970229059233798, 1.0186345623460398, -0.0040290636225456698),\
						 (3.8207924638323281, 2.1221125363782902, -0.0040290636225458303),\
						 (3.0310682323511955, 2.5347982892879148, -0.004029063622545655),\
						 (2.8570893286503694, 1.8618297053336619, -0.004029063622545616),\
						 (2.2740086422670838, 0.50071478431675587, -0.0040290636225454868),\
						 (1.8241121380753016, -0.15722036747739596, -0.004029063622545387)]\
			  )
	#ringCtrl            
	ringCtrl = cmds.curve( degree = 3,\
				knot = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5],\
				point = [(1.8241121380753391, -0.12705728919153217, -0.004029063622545387),\
						 (2.0053311427043523, 0.80215313924268239, -0.0040290636225454269),\
						 (2.3677691519623711, 2.6605739961110886, -0.0040290636225455076),\
						 (2.6657919111013118, 3.170532068468026, -0.0040290636225455735),\
						 (1.8349362092305008, 3.4104656457412719, -0.0040290636225453896),\
						 (1.693213037572106, 2.7551763780070249, -0.0040290636225453575),\
						 (1.277761133145221, 1.0448288145414268, -0.0040290636225452656),\
						 (0.8957443607257809, 0.18965503280862778, -0.0040290636225451806)]\
			  )
	#midCtrl          
	midCtrl = cmds.curve( degree = 3,\
				knot = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 7, 7],\
				point = [(0.91921978950307892, 0.14441041538018454, -0.0040290636225451858),\
						 (0.83650360029821058, 0.21391881672695945, -0.0040290636225451676),\
						 (0.64090814360273385, 0.44342485427773681, -0.0040290636225451242),\
						 (0.93151401567485392, 3.0656128457933733, -0.0040290636225451884),\
						 (0.81656066957314077, 3.8303054242713417, -0.0040290636225451633),\
						 (0.020549676764098114, 3.8652504539923829, -0.0040290636225449863),\
						 (0.046853000099142686, 1.5129499989141095, -0.0040290636225449924),\
						 (0.10422605556742869, 0.28488477206835799, -0.0040290636225450054),\
						 (-0.066304307904681892, 0.23145263865714016, -0.0040290636225449672),\
						 (-0.15156948964073394, 0.20473657195151418, -0.0040290636225449481)]\
			  )
	#indexCtrl
	indexCtrl = cmds.curve( degree = 3,\
				knot = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5],\
				point = [(-0.15516888382709695, 0.18965503280875284, -0.0040290636225449473),\
						 (-0.31643212007974281, 1.1315897582231742, -0.0040290636225449117),\
						 (-0.46517891124324751, 3.0154592090519827, -0.0040290636225448788),\
						 (-0.79740573523251368, 3.3647159049917263, -0.004029063622544805),\
						 (-1.3115491151032015, 2.8971881915631119, -0.0040290636225446905),\
						 (-1.2000611822048697, 1.2961637467644551, -0.0040290636225447157),\
						 (-0.99875751221016573, -0.11012363120669307, -0.0040290636225447599),\
						 (-1.0866249164986959, -1.8312712123360144, -0.0040290636225447408)]\
			  )
	#thumbCtrl              
	thumbCtrl = cmds.curve( degree = 3,\
				knot = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8],\
				point = [(-1.0866249164987971, -1.5447219686213658, -0.0040290636225447408),\
						 (-1.1710837568386716, -1.694693789669077, -0.0040290636225447218),\
						 (-1.3400014375184068, -1.9946374317644997, -0.0040290636225446845),\
						 (-2.1996158515650679, -1.3587848043361648, -0.0040290636225444936),\
						 (-2.3535741557902279, -0.73760280519015853, -0.004029063622544459),\
						 (-3.4570697182739765, -0.41959250462784897, -0.0040290636225442144),\
						 (-3.8207924638323281, -1.1967818094507947, -0.0040290636225441337),\
						 (-2.2577875025447538, -1.8898704327243536, -0.0040290636225444806),\
						 (-2.0833058667026219, -3.0457668473828678, -0.0040290636225445197),\
						 (-1.5998303696144487, -3.3018651901144835, -0.0040290636225446264),\
						 (-1.3580926210703592, -3.4299143614802916, -0.0040290636225446801)]\
			  )
	#put the fingers ctrl underneath the hand ctrl          
	cmds.parent(pinkyCtrl, handCtrl)
	cmds.parent(ringCtrl, handCtrl)
	cmds.parent(midCtrl, handCtrl)
	cmds.parent(indexCtrl, handCtrl)
	cmds.parent(thumbCtrl, handCtrl)
	cmds.select(handCtrl, replace = 1)
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap11
def mz_ccButtonSnap11(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton11(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton11(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton12
def mz_ccButton12(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],\
				point = [(0.54489100000000001, 0, -1.0972170000000001),\
						 (-0.54489100000000001, 0, -1.0972170000000001),\
						 (-0.57190399999999997, 0, -1.448294),\
						 (-0.51227900000000004, 0, -1.7534350000000001),\
						 (-0.39327099999999998, 0, -1.92306),\
						 (-0.26683899999999999, 0, -2.0357470000000002),\
						 (-0.133965, 0, -2.097731),\
						 (0, 0, -2.1201279999999998),\
						 (0.133965, 0, -2.097731),\
						 (0.26683899999999999, 0, -2.0357470000000002),\
						 (0.39327099999999998, 0, -1.92306),\
						 (0.51227900000000004, 0, -1.7534350000000001),\
						 (0.57190399999999997, 0, -1.448294),\
						 (0.54489100000000001, 0, -1.0972170000000001),\
						 (0.54505400000000004, 0, -0.74610399999999999),\
						 (0.59780699999999998, 0, -0.41958600000000001),\
						 (0.67365600000000003, 0, -0.12723699999999999),\
						 (0.74920699999999996, 0, 0.167214),\
						 (0.82460199999999995, 0, 0.55612799999999996),\
						 (0.84614400000000001, 0, 0.82138999999999995),\
						 (0.81947400000000004, 0, 1.166447),\
						 (0.73763100000000004, 0, 1.452029),\
						 (0.636486, 0, 1.6792670000000001),\
						 (0.51900800000000002, 0, 1.858641),\
						 (0.39550400000000002, 0, 1.9981),\
						 (0.266596, 0, 2.09545),\
						 (0.134293, 0, 2.163449),\
						 (-1.6742199999999999e-006, 0, 2.182925),\
						 (-0.13416, 0, 2.1634199999999999),\
						 (-0.26677899999999999, 0, 2.095529),\
						 (-0.39547199999999999, 0, 1.99807),\
						 (-0.51899300000000004, 0, 1.8586320000000001),\
						 (-0.63649599999999995, 0, 1.679268),\
						 (-0.73763199999999995, 0, 1.452024),\
						 (-0.81947400000000004, 0, 1.166445),\
						 (-0.84614400000000001, 0, 0.82138699999999998),\
						 (-0.82460199999999995, 0, 0.55612799999999996),\
						 (-0.74920600000000004, 0, 0.167213),\
						 (-0.67365600000000003, 0, -0.12723699999999999),\
						 (-0.59780800000000001, 0, -0.41958699999999999),\
						 (-0.54505400000000004, 0, -0.74610399999999999),\
						 (-0.54489100000000001, 0, -1.0972170000000001)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap12
def mz_ccButtonSnap12(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton12(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton12(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton13
def mz_ccButton13(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],\
				point = [(-4.5, 0, 0),\
						 (-2.5, 0, -2),\
						 (-2.5, 0, -1.5),\
						 (-1.5, 0, -1.5),\
						 (-1.5, 0, -2.5),\
						 (-2, 0, -2.5),\
						 (0, 0, -4.5),\
						 (2, 0, -2.5),\
						 (1.5, 0, -2.5),\
						 (1.5, 0, -1.5),\
						 (2.5, 0, -1.5),\
						 (2.5, 0, -2),\
						 (4.5, 0, 0),\
						 (2.5, 0, 2),\
						 (2.5, 0, 1.5),\
						 (1.5, 0, 1.5),\
						 (1.5, 0, 2.5),\
						 (2, 0, 2.5),\
						 (0, 0, 4.5),\
						 (-2, 0, 2.5),\
						 (-1.5, 0, 2.5),\
						 (-1.5, 0, 1.5),\
						 (-2.5, 0, 1.5),\
						 (-2.5, 0, 2),\
						 (-4.5, 0, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap13
def mz_ccButtonSnap13(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton13(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton13(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
		

#mz_ccButton14
def mz_ccButton14(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,\
						41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,\
						61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,\
						81, 82, 83, 84, 85, 86, 87, 88, 89, 90],\
				point = [(-2.5135064000000003, 0, 3.64816e-010),\
						 (-2.4814316000000005, 0, -0.39286599999999999),\
						 (-2.3879808000000002, 0, -0.77580280000000013),\
						 (-2.2371327999999999, 0, -1.1399820000000001),\
						 (-2.0324352000000001, 0, -1.4768392000000001),\
						 (-1.7773171999999999, 0, -1.7773171999999999),\
						 (-1.4768392000000001, 0, -2.0324352000000001),\
						 (-1.1399820000000001, 0, -2.2371327999999999),\
						 (-0.77580280000000013, 0, -2.3879808000000002),\
						 (-0.39286599999999999, 0, -2.4814319999999999),\
						 (0, 0, -2.5135056000000002),\
						 (0, 0.39286480000000001, -2.4814319999999999),\
						 (0, 0.77580320000000003, -2.3879808000000002),\
						 (0, 1.1399816, -2.2371327999999999),\
						 (0, 1.4768392000000001, -2.0324352000000001),\
						 (0, 1.7773171999999999, -1.7773171999999999),\
						 (0, 2.0324356000000003, -1.4768392000000001),\
						 (0, 2.2371327999999999, -1.1399820000000001),\
						 (0, 2.3879808000000002, -0.77580280000000013),\
						 (0, 2.4814316000000005, -0.39286599999999999),\
						 (0, 2.5135064000000003, 0),\
						 (0, 2.4814316000000005, 0.39286599999999999),\
						 (0, 2.3879808000000002, 0.77580280000000013),\
						 (0, 2.2371327999999999, 1.1399820000000001),\
						 (0, 2.0324356000000003, 1.4768392000000001),\
						 (0, 1.7773171999999999, 1.7773171999999999),\
						 (0, 1.4768392000000001, 2.0324352000000001),\
						 (0, 1.1399816, 2.2371327999999999),\
						 (0, 0.77580320000000003, 2.3879808000000002),\
						 (0, 0.39286480000000001, 2.4814319999999999),\
						 (0, 0, 2.5135064000000003),\
						 (-0.39286599999999999, 0, 2.4814316000000005),\
						 (-0.77580280000000013, 0, 2.3879808000000002),\
						 (-1.1399820000000001, 0, 2.2371327999999999),\
						 (-1.4768392000000001, 0, 2.0324352000000001),\
						 (-1.7773171999999999, 0, 1.7773171999999999),\
						 (-2.0324352000000001, 0, 1.4768392000000001),\
						 (-2.2371327999999999, 0, 1.1399820000000001),\
						 (-2.3879808000000002, 0, 0.77580280000000013),\
						 (-2.4814316000000005, 0, 0.39286599999999999),\
						 (-2.5135064000000003, 0, 3.64816e-010),\
						 (-2.4814319999999999, 0.39286480000000001, 0),\
						 (-2.3879808000000002, 0.77580320000000003, 0),\
						 (-2.2371327999999999, 1.1399816, 0),\
						 (-2.0324352000000001, 1.4768392000000001, 0),\
						 (-1.7773171999999999, 1.7773171999999999, 0),\
						 (-1.4768392000000001, 2.0324356000000003, 0),\
						 (-1.1399820000000001, 2.2371327999999999, 0),\
						 (-0.77580280000000013, 2.3879808000000002, 0),\
						 (-0.39286599999999999, 2.4814316000000005, 0),\
						 (0, 2.5135064000000003, 0),\
						 (0.39286599999999999, 2.4814316000000005, 0),\
						 (0.77580280000000013, 2.3879808000000002, 0),\
						 (1.1399820000000001, 2.2371327999999999, 0),\
						 (1.4768392000000001, 2.0324356000000003, 0),\
						 (1.7773171999999999, 1.7773171999999999, 0),\
						 (2.0324352000000001, 1.4768392000000001, 0),\
						 (2.2371327999999999, 1.1399816, 0),\
						 (2.3879808000000002, 0.77580320000000003, 0),\
						 (2.4814319999999999, 0.39286480000000001, 0),\
						 (2.5135064000000003, 0, 3.6481800000000002e-010),\
						 (2.4814316000000005, 0, 0.39286599999999999),\
						 (2.3879808000000002, 0, 0.77580280000000013),\
						 (2.2371327999999999, 0, 1.1399820000000001),\
						 (2.0324352000000001, 0, 1.4768392000000001),\
						 (1.7773171999999999, 0, 1.7773171999999999),\
						 (1.4768392000000001, 0, 2.0324352000000001),\
						 (1.1399820000000001, 0, 2.2371327999999999),\
						 (0.77580280000000013, 0, 2.3879808000000002),\
						 (0.39286599999999999, 0, 2.4814316000000005),\
						 (0, 0, 2.5135064000000003),\
						 (0.39286599999999999, 0, 2.4814316000000005),\
						 (0.77580280000000013, 0, 2.3879808000000002),\
						 (1.1399820000000001, 0, 2.2371327999999999),\
						 (1.4768392000000001, 0, 2.0324352000000001),\
						 (1.7773171999999999, 0, 1.7773171999999999),\
						 (2.0324352000000001, 0, 1.4768392000000001),\
						 (2.2371327999999999, 0, 1.1399820000000001),\
						 (2.3879808000000002, 0, 0.77580280000000013),\
						 (2.4814316000000005, 0, 0.39286599999999999),\
						 (2.5135064000000003, 0, 3.6481800000000002e-010),\
						 (2.4814316000000005, 0, -0.39286599999999999),\
						 (2.3879808000000002, 0, -0.77580280000000013),\
						 (2.2371327999999999, 0, -1.1399820000000001),\
						 (2.0324352000000001, 0, -1.4768392000000001),\
						 (1.7773171999999999, 0, -1.7773171999999999),\
						 (1.4768392000000001, 0, -2.0324352000000001),\
						 (1.1399820000000001, 0, -2.2371327999999999),\
						 (0.77580280000000013, 0, -2.3879808000000002),\
						 (0.39286599999999999, 0, -2.4814319999999999),\
						 (0, 0, -2.5135056000000002)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap14
def mz_ccButtonSnap14(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton14(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton14(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton15
def mz_ccButton15(self):
	cmds.curve( degree = 1,\
				knot = [0, 2.3135629999999998, 4.6271259999999996, 6.9406889999999999, 8.5778230000000004,\
						10.214957999999999, 11.849695000000001, 13.484432, 15.119168999999999, 16.744737000000001,\
						18.379473999999998, 20.014211, 21.648949000000002, 23.283685999999999, 24.920819999999999,\
						26.557953999999999, 28.871517000000001, 31.185079999999999, 33.498643000000001, 35.812206000000003,\
						38.125770000000003, 40.439332999999998, 42.076467000000001, 43.713600999999997, 45.348337999999998,\
						46.983074999999999, 48.617812000000001, 50.252549999999999, 51.878118000000001, 53.512855000000002,\
						55.147592000000003, 56.782328999999997, 58.419463, 60.056598000000001, 62.370161000000003,\
						64.683723999999998, 66.997287, 69.310850000000002, 71.624413000000004, 73.937976000000006,\
						75.575109999999995, 77.212243999999998, 78.846981999999997, 80.481718999999998, 82.116455999999999,\
						83.742024000000001, 85.376761000000002, 87.011498000000003, 88.646235000000004, 90.280972000000006,\
						91.918107000000006, 93.555240999999995, 95.868803999999997, 98.182366999999999, 100.49593,\
						102.809493, 105.12305600000001, 107.43661899999999, 109.07375399999999, 110.710888, 112.345625,\
						113.980362, 115.615099, 117.240667, 118.875404, 120.510142, 122.144879, 123.779616,\
						125.41674999999999, 127.053884, 129.367447, 131.68100999999999, 133.994574],\
				point = [(0, 2.4341246999999999, 2.6128529999999999),\
						 (0.49114020000000003, 1.9503278999999996, 2.5325198999999996),\
						 (0.98228040000000005, 1.4899844999999996, 2.3634132000000001),\
						 (1.4734209, 1.0692317999999996, 2.1114609000000004),\
						 (0.98228040000000005, 1.0692317999999996, 2.1114609000000004),\
						 (0.49114020000000003, 1.0692317999999996, 2.1114609000000004),\
						 (0.49114020000000003, 0.70281809999999978, 1.7854947000000001),\
						 (0.49114020000000003, 0.40358759999999982, 1.3969409999999998),\
						 (0.49114020000000003, 0.1820294999999999, 0.95941979999999993),\
						 (0.48826769999999997, 0.045909599999999953, 0.49114020000000003),\
						 (0.95941979999999993, 0.18202949999999996, 0.49114020000000008),\
						 (1.3969409999999998, 0.40358759999999988, 0.49114020000000003),\
						 (1.7854946999999999, 0.7028181, 0.49114020000000003),\
						 (2.1114609, 1.0692317999999998, 0.49114020000000014),\
						 (2.1114609, 1.0692318000000001, 0.98228040000000016),\
						 (2.1114609, 1.0692318000000001, 1.4734209),\
						 (2.3634132000000001, 1.4899844999999998, 0.98228040000000005),\
						 (2.5325198999999996, 1.9503279, 0.49114020000000025),\
						 (2.6128529999999999, 2.4341246999999999, 2.4238995509170921e-016),\
						 (2.5325198999999996, 1.9503279, -0.49114019999999975),\
						 (2.3634132000000001, 1.4899845, -0.98228039999999994),\
						 (2.1114609, 1.0692318000000001, -1.4734208999999998),\
						 (2.1114609, 1.0692318000000001, -0.98228039999999983),\
						 (2.1114609, 1.0692318000000001, -0.49114019999999986),\
						 (1.7854946999999999, 0.7028181, -0.49114019999999997),\
						 (1.3969409999999998, 0.40358760000000005, -0.49114019999999997),\
						 (0.95941979999999993, 0.18202950000000004, -0.49114019999999992),\
						 (0.48826769999999997, 0.045909600000000043, -0.49114020000000003),\
						 (0.49114020000000003, 0.18202950000000009, -0.95941979999999993),\
						 (0.49114020000000003, 0.40358760000000016, -1.3969409999999998),\
						 (0.49114020000000003, 0.70281810000000011, -1.7854946999999997),\
						 (0.49114020000000003, 1.0692318000000003, -2.1114608999999995),\
						 (0.98228040000000005, 1.0692318000000003, -2.1114608999999995),\
						 (1.4734209, 1.0692318000000003, -2.1114608999999995),\
						 (0.98228040000000005, 1.4899845000000003, -2.3634131999999997),\
						 (0.49114020000000003, 1.9503279000000002, -2.5325198999999996),\
						 (0, 2.4341246999999999, -2.6128529999999999),\
						 (-0.49114020000000003, 1.9503279000000002, -2.5325198999999996),\
						 (-0.98228040000000005, 1.4899845000000003, -2.3634131999999997),\
						 (-1.4734209, 1.0692318000000003, -2.1114608999999995),\
						 (-0.98228040000000005, 1.0692318000000003, -2.1114608999999995),\
						 (-0.49114020000000003, 1.0692318000000003, -2.1114608999999995),\
						 (-0.49114020000000003, 0.70281810000000011, -1.7854946999999997),\
						 (-0.49114020000000003, 0.40358760000000016, -1.3969409999999998),\
						 (-0.49114020000000003, 0.18202950000000009, -0.95941979999999993),\
						 (-0.48826769999999997, 0.045909600000000043, -0.49114020000000003),\
						 (-0.95941979999999993, 0.18202950000000004, -0.49114019999999992),\
						 (-1.3969409999999998, 0.40358760000000005, -0.49114019999999997),\
						 (-1.7854946999999999, 0.7028181, -0.49114019999999997),\
						 (-2.1114609, 1.0692318000000001, -0.49114019999999986),\
						 (-2.1114609, 1.0692318000000001, -0.98228039999999983),\
						 (-2.1114609, 1.0692318000000001, -1.4734208999999998),\
						 (-2.3634132000000001, 1.4899845, -0.98228039999999994),\
						 (-2.5325198999999996, 1.9503279, -0.49114019999999975),\
						 (-2.6128529999999999, 2.4341246999999999, 2.4238995509170921e-016),\
						 (-2.5325198999999996, 1.9503279, 0.49114020000000025),\
						 (-2.3634132000000001, 1.4899844999999998, 0.98228040000000005),\
						 (-2.1114609, 1.0692318000000001, 1.4734209),\
						 (-2.1114609, 1.0692318000000001, 0.98228040000000016),\
						 (-2.1114609, 1.0692317999999998, 0.49114020000000014),\
						 (-1.7854946999999999, 0.7028181, 0.49114020000000003),\
						 (-1.3969409999999998, 0.40358759999999988, 0.49114020000000003),\
						 (-0.95941979999999993, 0.18202949999999996, 0.49114020000000008),\
						 (-0.49114020000000003, 0.045909599999999953, 0.48826769999999997),\
						 (-0.49114020000000003, 0.1820294999999999, 0.95941979999999993),\
						 (-0.49114020000000003, 0.40358759999999982, 1.3969409999999998),\
						 (-0.49114020000000003, 0.70281809999999978, 1.7854947000000001),\
						 (-0.49114020000000003, 1.0692317999999996, 2.1114609000000004),\
						 (-0.98228040000000005, 1.0692317999999996, 2.1114609000000004),\
						 (-1.4734209, 1.0692317999999996, 2.1114609000000004),\
						 (-0.98228040000000005, 1.4899844999999996, 2.3634132000000001),\
						 (-0.49114020000000003, 1.9503278999999996, 2.5325198999999996),\
						 (0, 2.4341246999999999, 2.6128529999999999)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap15
def mz_ccButtonSnap15(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton15(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton15(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton16
def mz_ccButton16(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],\
				point = [(0, 2.4341247000000004, 2.6128529999999994),\
						 (0.49114020000000003, 1.9503279000000007, 2.5325198999999992),\
						 (0.98228040000000005, 1.4899845000000005, 2.3634131999999997),\
						 (1.4734209, 1.0692318000000005, 2.1114608999999995),\
						 (0.98228040000000005, 1.0692318000000005, 2.1114608999999995),\
						 (0.49114020000000003, 1.0692318000000005, 2.1114608999999995),\
						 (0.49114020000000003, 0.70281810000000045, 1.7854946999999997),\
						 (0.49114020000000003, 0.40358760000000032, 1.3969409999999998),\
						 (0.49114020000000003, 0.18202950000000021, 0.95941979999999993),\
						 (0.48826769999999997, 0.045909600000000113, 0.49114020000000003),\
						 (0.48826769999999997, 0, 0),\
						 (0.48826769999999997, 0.045909599999999891, -0.49114020000000003),\
						 (0.49114020000000003, 0.18202949999999976, -0.95941979999999993),\
						 (0.49114020000000003, 0.40358759999999966, -1.3969409999999998),\
						 (0.49114020000000003, 0.70281809999999956, -1.7854947000000001),\
						 (0.49114020000000003, 1.0692317999999996, -2.1114609000000004),\
						 (0.98228040000000005, 1.0692317999999996, -2.1114609000000004),\
						 (1.4734209, 1.0692317999999996, -2.1114609000000004),\
						 (0.98228040000000005, 1.4899844999999996, -2.3634132000000005),\
						 (0.49114020000000003, 1.9503278999999993, -2.5325199),\
						 (0, 2.4341246999999995, -2.6128530000000003),\
						 (-0.49114020000000003, 1.9503278999999993, -2.5325199),\
						 (-0.98228040000000005, 1.4899844999999996, -2.3634132000000005),\
						 (-1.4734209, 1.0692317999999996, -2.1114609000000004),\
						 (-0.98228040000000005, 1.0692317999999996, -2.1114609000000004),\
						 (-0.49114020000000003, 1.0692317999999996, -2.1114609000000004),\
						 (-0.49114020000000003, 0.70281809999999956, -1.7854947000000001),\
						 (-0.49114020000000003, 0.40358759999999966, -1.3969409999999998),\
						 (-0.49114020000000003, 0.18202949999999976, -0.95941979999999993),\
						 (-0.48826769999999997, 0.045909599999999891, -0.49114020000000003),\
						 (-0.48826769999999997, 0, 0),\
						 (-0.49114020000000003, 0.045909600000000113, 0.48826769999999997),\
						 (-0.49114020000000003, 0.18202950000000021, 0.95941979999999993),\
						 (-0.49114020000000003, 0.40358760000000032, 1.3969409999999998),\
						 (-0.49114020000000003, 0.70281810000000045, 1.7854946999999997),\
						 (-0.49114020000000003, 1.0692318000000005, 2.1114608999999995),\
						 (-0.98228040000000005, 1.0692318000000005, 2.1114608999999995),\
						 (-1.4734209, 1.0692318000000005, 2.1114608999999995),\
						 (-0.98228040000000005, 1.4899845000000005, 2.3634131999999997),\
						 (-0.49114020000000003, 1.9503279000000007, 2.5325198999999992),\
						 (0, 2.4341247000000004, 2.6128529999999994)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap16
def mz_ccButtonSnap16(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton16(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton16(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton17
def mz_ccButton17(self):
	cmds.curve( degree = 1,\
				knot = [0, 4.7999999999999998, 9.5999999999999996, 12.800000000000001, 17.600000000000001,\
						22.399999999999999, 25.600000000000001, 30.399999999999999, 35.200000000000003,\
						38.399999999999999, 43.200000000000003, 48, 51.200000000000003],\
				point = [(-0.64000000000000012, -2.5600000000000005, 0),\
						 (-0.64000000000000012, -0.64000000000000012, 0),\
						 (-2.5600000000000005, -0.64000000000000012, 0),\
						 (-2.5600000000000005, 0.64000000000000012, 0),\
						 (-0.64000000000000012, 0.64000000000000012, 0),\
						 (-0.64000000000000012, 2.5600000000000005, 0),\
						 (0.64000000000000012, 2.5600000000000005, 0),\
						 (0.64000000000000012, 0.64000000000000012, 0),\
						 (2.5600000000000005, 0.64000000000000012, 0),\
						 (2.5600000000000005, -0.64000000000000012, 0),\
						 (0.64000000000000012, -0.64000000000000012, 0),\
						 (0.64000000000000012, -2.5600000000000005, 0),\
						 (-0.64000000000000012, -2.5600000000000005, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap17
def mz_ccButtonSnap17(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton17(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton17(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton18
def mz_ccButton18(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],\
				point = [(-2, 0, -2),\
						 (-2, 0, -3),\
						 (2, 0, -3),\
						 (2, 0, -2),\
						 (3, 0, -2),\
						 (3, 0, 2),\
						 (2, 0, 2),\
						 (2, 0, 3),\
						 (-2, 0, 3),\
						 (-2, 0, 2),\
						 (-3, 0, 2),\
						 (-3, 0, -2),\
						 (-2, 0, -2)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap18
def mz_ccButtonSnap18(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton18(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton18(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton19
def mz_ccButton19(self):
	cmds.curve( degree = 1,\
				knot = [0, 9.9992300000000007, 13.898834000000001, 17.798387999999999,\
						21.697965, 25.597534, 35.596760000000003, 45.595986000000003,\
						49.495555000000003, 53.395130999999999, 57.294685999999999,\
						61.194290000000002, 71.193520000000007, 81.192749000000006,\
						85.092258000000001, 88.991923, 92.891391999999996, 96.791135999999995,\
						106.79113599999999, 116.79113599999999, 120.690881, 124.59035, 128.490015,\
						132.38952399999999, 142.38875300000001, 162.38875300000001, 166.38875300000001,\
						175.33302499999999, 184.277297, 188.277297, 192.277297, 201.22156899999999,\
						210.165841, 215.82269500000001, 221.47954899999999, 227.136403,\
						232.79325800000001, 236.79325800000001],\
				point = [(7.8826092109875007e-016, 5.5999999999999917, 5.854783632927615e-017),\
						 (1.9998460000000011, 5.5999999999999917, -4.4471999999414518e-006),\
						 (1.8457720000000009, 5.5999999999999917, 0.76454620000000018),\
						 (1.4141046000000008, 5.5999999999999917, 1.4141032),\
						 (0.76454380000000088, 5.5999999999999917, 1.8457728),\
						 (7.8826092109875007e-016, 5.5999999999999917, 1.9998452000000002),\
						 (7.8826092109875007e-016, 5.5999999999999917, 5.854783632927615e-017),\
						 (7.8826092109875007e-016, 5.5999999999999917, 1.9998452000000002),\
						 (-0.76454379999999933, 5.5999999999999917, 1.8457728),\
						 (-1.414104599999999, 5.5999999999999917, 1.4141032),\
						 (-1.8457719999999991, 5.5999999999999917, 0.76454620000000018),\
						 (-1.9998459999999993, 5.5999999999999917, -4.4471999999414518e-006),\
						 (7.8826092109875007e-016, 5.5999999999999917, 5.854783632927615e-017),\
						 (-1.9998459999999993, 5.5999999999999917, -4.4471999999414518e-006),\
						 (-1.8457719999999991, 5.5999999999999917, -0.76453559999999987),\
						 (-1.414104599999999, 5.5999999999999917, -1.4141192),\
						 (-0.76454379999999933, 5.5999999999999917, -1.8457498000000001),\
						 (7.8826092109875007e-016, 5.5999999999999917, -2),\
						 (7.8826092109875007e-016, 5.5999999999999917, 5.854783632927615e-017),\
						 (7.8826092109875007e-016, 5.5999999999999917, -2),\
						 (0.76454380000000088, 5.5999999999999917, -1.8457498000000001),\
						 (1.4141046000000008, 5.5999999999999917, -1.4141192),\
						 (1.8457720000000009, 5.5999999999999917, -0.76453559999999987),\
						 (1.9998460000000011, 5.5999999999999917, -4.4471999999414518e-006),\
						 (7.8826092109875007e-016, 5.5999999999999917, 5.854783632927615e-017),\
						 (2.9840220143980878e-016, 1.5999999999999917, 5.854783632927615e-017),\
						 (2.9840220143980878e-016, 1.5999999999999917, 0.80000000000000016),\
						 (1.0245871357623221e-016, -8.8817841970012523e-015, 5.854783632927615e-017),\
						 (2.9840220143980878e-016, 1.5999999999999917, -0.79999999999999993),\
						 (2.9840220143980878e-016, 1.5999999999999917, 5.854783632927615e-017),\
						 (-0.79999999999999971, 1.5999999999999917, 5.854783632927615e-017),\
						 (1.0245871357623221e-016, -8.8817841970012523e-015, 5.854783632927615e-017),\
						 (0.80000000000000038, 1.5999999999999917, 5.854783632927615e-017),\
						 (2.9840220143980878e-016, 1.5999999999999917, 0.80000000000000016),\
						 (-0.79999999999999971, 1.5999999999999917, 5.854783632927615e-017),\
						 (2.9840220143980878e-016, 1.5999999999999917, -0.79999999999999993),\
						 (0.80000000000000038, 1.5999999999999917, 5.854783632927615e-017),\
						 (2.9840220143980878e-016, 1.5999999999999917, 5.854783632927615e-017)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap19
def mz_ccButtonSnap19(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton19(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton19(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton20
def mz_ccButton20(self):
	cmds.curve( degree = 1,\
				knot = [0, 9.9992300000000007, 13.898834000000001, 17.798387999999999, 21.697965,\
						25.597534, 35.596760000000003, 45.595986000000003, 49.495555000000003,\
						53.395130999999999, 57.294685999999999, 61.194290000000002, 71.193520000000007,\
						81.192749000000006, 85.092258000000001, 88.991923, 92.891391999999996,\
						96.791135999999995, 106.79113599999999, 116.79113599999999, 120.690881,\
						124.59035, 128.490015, 132.38952399999999, 142.38875300000001, 162.38875300000001,\
						166.38875300000001, 175.33302499999999, 184.277297, 188.277297, 192.277297,\
						201.22156899999999, 210.165841, 215.82269500000001, 221.47954899999999, 227.136403,\
						232.79325800000001, 236.79325800000001],\
				point = [(0, 0, 0),\
						(-1.9998460000000002, 0, -4.4471999999999995e-006),\
						(-1.845772, 0, 0.76454620000000006),\
						(-1.4141045999999999, 0, 1.4141032),\
						(-0.76454380000000011, 0, 1.8457728),\
						(0, 0, 1.9998452000000002),\
						(0, 0, 0),\
						(0, 0, 1.9998452000000002),\
						(0.76454380000000011, 0, 1.8457728),\
						(1.4141045999999999, 0, 1.4141032),\
						(1.845772, 0, 0.76454620000000006),\
						(1.9998460000000002, 0, -4.4471999999999995e-006),\
						(0, 0, 0),\
						(1.9998460000000002, 0, -4.4471999999999995e-006),\
						(1.845772, 0, -0.76453559999999998),\
						(1.4141045999999999, 0, -1.4141192),\
						(0.76454380000000011, 0, -1.8457498000000001),\
						(0, 0, -2),\
						(0, 0, 0),\
						(0, 0, -2),\
						(-0.76454380000000011, 0, -1.8457498000000001),\
						(-1.4141045999999999, 0, -1.4141192),\
						(-1.845772, 0, -0.76453559999999998),\
						(-1.9998460000000002, 0, -4.4471999999999995e-006),\
						(0, 0, 0),\
						(0, 4, 0),\
						(0, 5.6000000000000005, 0.80000000000000004),\
						(0, 5.6000000000000005, 0),\
						(0, 5.6000000000000005, -0.80000000000000004),\
						(0, 4, 0),\
						(0.80000000000000004, 5.6000000000000005, 0),\
						(0, 5.6000000000000005, 0),\
						(-0.80000000000000004, 5.6000000000000005, 0),\
						(0, 5.6000000000000005, 0.80000000000000004),\
						(0.80000000000000004, 5.6000000000000005, 0),\
						(0, 5.6000000000000005, -0.80000000000000004),\
						(-0.80000000000000004, 5.6000000000000005, 0),\
						(0, 4, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap20
def mz_ccButtonSnap20(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton20(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton20(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton21
def mz_ccButton21(self):
	cmds.curve( degree = 1,\
				knot = [0, 4, 12.944272, 21.888544, 25.888544, 45.888544000000003,\
				46.932133999999998, 47.975695999999999, 49.019289000000001, 50.062885999999999,\
				51.106444000000003, 52.150039, 53.193634000000003, 54.237194000000002,\
				55.280788999999999, 56.324384000000002, 57.367942999999997, 58.411538,\
				59.455132999999996, 60.498693000000003, 61.542287999999999, 62.585881999999998,\
				63.629441999999997, 64.673036999999994, 65.716632000000004, 66.760191000000006,\
				67.803787, 68.847380000000001, 69.890941999999995, 70.934532000000004],\
				point = [(-1.6485242005752952e-016, 1.5999999999999943, 0),\
						(0.79999999999999993, 1.5999999999999943, 0),\
						(-3.6079590792110599e-016, -5.3290705182007514e-015, 0),\
						(-0.80000000000000016, 1.5999999999999943, 0),\
						(-1.6485242005752952e-016, 1.5999999999999943, 0),\
						(3.2500629960141186e-016, 5.5999999999999952, 0),\
						(-0.20683759999999971, 5.6279535999999952, 0),\
						(-0.3996623999999997, 5.7078255999999952, 0),\
						(-0.56568959999999968, 5.834309999999995, 0),\
						(-0.69217499999999965, 6.0003377999999952, 0),\
						(-0.77204559999999967, 6.1931621999999953, 0),\
						(-0.80000599999999955, 6.4000000461259949, 0),\
						(-0.77204559999999967, 6.6068375999999951, 0),\
						(-0.69217499999999965, 6.7996623999999954, 0),\
						(-0.56568959999999946, 6.9656895999999948, 0),\
						(-0.39966239999999947, 7.0921749999999948, 0),\
						(-0.20683759999999954, 7.1720455999999952, 0),\
						(5.2095052225306782e-016, 7.2000059999999948, 0),\
						(0.20683760000000054, 7.1720455999999952, 0),\
						(0.39966240000000058, 7.0921749999999948, 0),\
						(0.56568960000000057, 6.9656895999999948, 0),\
						(0.69217500000000054, 6.7996623999999946, 0),\
						(0.77204560000000055, 6.6068375999999951, 0),\
						(0.80000600000000044, 6.4000000461259949, 0),\
						(0.77204560000000055, 6.1931621999999953, 0),\
						(0.69217500000000054, 6.0003377999999952, 0),\
						(0.56568960000000035, 5.834309999999995, 0),\
						(0.39966240000000036, 5.7078255999999952, 0),\
						(0.20683760000000037, 5.6279535999999952, 0),\
						(3.2500629960141186e-016, 5.5999999999999952, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap21
def mz_ccButtonSnap21(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton21(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton21(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton22
def mz_ccButton22(self):
	cmds.curve( degree = 1,\
				knot = [0, 4, 12.944272, 21.888544, 25.888544, 45.888544000000003,\
						46.932133999999998, 47.975695999999999, 49.019289000000001,\
						50.062885999999999, 51.106444000000003, 52.150039, 53.193634000000003,\
						54.237194000000002, 55.280788999999999, 56.324384000000002,\
						57.367942999999997, 58.411538, 59.455132999999996, 60.498693000000003,\
						61.542287999999999, 62.585881999999998, 63.629441999999997,\
						64.673036999999994, 65.716632000000004, 66.760191000000006, 67.803787,\
						68.847380000000001, 69.890941999999995, 70.934532000000004],\
				point = [(0, 4.8000000000000007, 0),\
						 (-0.80000000000000004, 6.4000000000000004, 0),\
						 (0, 6.4000000000000004, 0),\
						 (0.80000000000000004, 6.4000000000000004, 0),\
						 (0, 4.8000000000000007, 0),\
						 (0, 0.80000000000000004, 0),\
						 (0.20683760000000004, 0.77204640000000002, 0),\
						 (0.39966240000000003, 0.69217440000000008, 0),\
						 (0.56568960000000001, 0.56569000000000003, 0),\
						 (0.6921750000000001, 0.39966220000000002, 0),\
						 (0.77204560000000011, 0.20683780000000002, 0),\
						 (0.80000599999999999, -4.6125999999999999e-008, 0),\
						 (0.77204560000000011, -0.20683760000000004, 0),\
						 (0.6921750000000001, -0.39966240000000003, 0),\
						 (0.56568960000000001, -0.56568960000000001, 0),\
						 (0.39966240000000003, -0.6921750000000001, 0),\
						 (0.20683760000000004, -0.77204560000000011, 0),\
						 (0, -0.80000599999999999, 0),\
						 (-0.20683760000000004, -0.77204560000000011, 0),\
						 (-0.39966240000000003, -0.6921750000000001, 0),\
						 (-0.56568960000000001, -0.56568960000000001, 0),\
						 (-0.6921750000000001, -0.39966240000000003, 0),\
						 (-0.77204560000000011, -0.20683760000000004, 0),\
						 (-0.80000599999999999, -4.6125999999999999e-008, 0),\
						 (-0.77204560000000011, 0.20683780000000002, 0),\
						 (-0.6921750000000001, 0.39966220000000002, 0),\
						 (-0.56568960000000001, 0.56569000000000003, 0),\
						 (-0.39966240000000003, 0.69217440000000008, 0),\
						 (-0.20683760000000004, 0.77204640000000002, 0),\
						 (0, 0.80000000000000004, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap22
def mz_ccButtonSnap22(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton22(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton22(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton23
def mz_ccButton23(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],\
				point = [(0, 0, -2),\
						 (0.76454380000000011, 0, -1.8457498000000001),\
						 (1.4141045999999999, 0, -1.4141192),\
						 (1.845772, 0, -0.76453559999999998),\
						 (1.9998460000000002, 0, -4.4471999999999995e-006),\
						 (1.845772, 0, 0.76454620000000006),\
						 (1.4141045999999999, 0, 1.4141032),\
						 (0.76454380000000011, 0, 1.8457728),\
						 (0, 0, 1.9998452000000002),\
						 (0, 0, 0),\
						 (0, 0, -2),\
						 (-0.76454380000000011, 0, -1.8457498000000001),\
						 (-1.4141045999999999, 0, -1.4141192),\
						 (-1.845772, 0, -0.76453559999999998),\
						 (-1.9998460000000002, 0, -4.4471999999999995e-006),\
						 (0, 0, 0),\
						 (1.9998460000000002, 0, -4.4471999999999995e-006),\
						 (1.845772, 0, 0.76454620000000006),\
						 (1.4141045999999999, 0, 1.4141032),\
						 (0.76454380000000011, 0, 1.8457728),\
						 (0, 0, 1.9998452000000002),\
						 (-0.76454380000000011, 0, 1.8457728),\
						 (-1.4141045999999999, 0, 1.4141032),\
						 (-1.845772, 0, 0.76454620000000006),\
						 (-1.9998460000000002, 0, -4.4471999999999995e-006)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap23
def mz_ccButtonSnap23(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton23(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton23(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton24
def mz_ccButton24(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],\
				point = [(4.4964032497318838e-016, 1.6000000000000012, -2.2557010682735437e-015),\
						 (-0.3119235293234579, 1.5688757999304204, -2.2506959151650479e-015),\
						 (-0.61179992425629959, 1.4775355211816883, -2.2360072780566864e-015),\
						 (-0.88816423422255186, 1.3295695200849658, -2.2122125302821148e-015),\
						 (-1.130589804340127, 1.1308261083641808, -2.1802521520958941e-015),\
						 (-1.3293898447288988, 0.88844923528803887, -2.1412749781607401e-015),\
						 (-1.4772553023026735, 0.61203519477418755, -2.0968242102368441e-015),\
						 (-1.5682658227913404, 0.31205878131852949, -2.0485843237521635e-015),\
						 (-1.5991784838738627, 0.00011039946844738636, -1.9984191979138542e-015),\
						 (-1.5682630253857908, -0.31183819334539664, -1.9482540381499844e-015),\
						 (-1.4772753935903149, -0.61182275836088429, -1.9000128407945046e-015),\
						 (-1.3295355374380915, -0.88830478098581056, -1.8555511405133494e-015),\
						 (-1.1308474670756683, -1.1307718807569309, -1.8165594570190147e-015),\
						 (-0.88839144588362751, -1.3294735186432725, -1.7846057965777277e-015),\
						 (-0.61191601590586864, -1.477226285107555, -1.760845339547368e-015),\
						 (-0.31194415892591898, -1.5682561640787946, -1.7462066185302709e-015),\
						 (2.2815083156046968e-015, -1.5992086836047279, -1.7412290737588495e-015),\
						 (0.31194415892592231, -1.5682561640787931, -1.7462066185302711e-015),\
						 (0.61191601590587175, -1.4772262851075539, -1.7608453395473682e-015),\
						 (0.8883914458836305, -1.3294735186432698, -1.7846057965777281e-015),\
						 (1.1308474670756701, -1.1307718807569294, -1.8165594570190151e-015),\
						 (1.3295355374380942, -0.88830478098580823, -1.8555511405133494e-015),\
						 (1.4772753935903185, -0.61182275836088262, -1.9000128407945046e-015),\
						 (1.568263025385791, -0.31183819334539253, -1.9482540381499848e-015),\
						 (1.5991784838738625, 0.00011039946845280424, -1.998419197913855e-015),\
						 (1.5682658227913402, 0.3120587813185336, -2.0485843237521639e-015),\
						 (1.4772553023026744, 0.61203519477419133, -2.0968242102368445e-015),\
						 (1.3293898447288983, 0.88844923528804043, -2.1412749781607401e-015),\
						 (1.1305898043401246, 1.1308261083641831, -2.1802521520958948e-015),\
						 (0.88816423422255164, 1.3295695200849658, -2.2122125302821148e-015),\
						 (0.61179992425629914, 1.4775355211816885, -2.2360072780566864e-015),\
						 (0.31192352932345913, 1.5688757999304204, -2.2506959151650479e-015),\
						 (4.4964032497318838e-016, 1.6000000000000012, -2.2557010682735437e-015),\
						 (3.6082248300317588e-016, 4.4000000000000004, -2.9753977059954196e-015),\
						 (-1.1999999999999997, 2.8000000000000003, -2.6201263381153696e-015),\
						 (3.6082248300317588e-016, 4.4000000000000004, -2.9753977059954196e-015),\
						 (1.2000000000000006, 2.8000000000000003, -2.6201263381153696e-015)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap24
def mz_ccButtonSnap24(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton24(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton24(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton25
def mz_ccButton25(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 35.58035297, 36],\
				point = [(8.8817841970012528e-017, 1.6000000000000012, -2.5729962394826207e-016),\
						 (-0.31192352932345824, 1.5688757999304204, -2.5229447083976599e-016),\
						 (-0.61179992425629992, 1.4775355211816883, -2.3760583373140462e-016),\
						 (-0.8881642342225522, 1.3295695200849658, -2.1381108595683288e-016),\
						 (-1.1305898043401275, 1.1308261083641808, -1.8185070777061248e-016),\
						 (-1.3293898447288992, 0.88844923528803887, -1.4287353383545829e-016),\
						 (-1.477255302302674, 0.61203519477418755, -9.842276591156229e-017),\
						 (-1.5682658227913409, 0.31205878131852949, -5.0182879426881578e-017),\
						 (-1.5991784838738632, 0.00011039946844738636, -1.7753588572245247e-020),\
						 (-1.5682630253857912, -0.31183819334539664, 5.0147406175297471e-017),\
						 (-1.4772753935903153, -0.61182275836088429, 9.8388603530777391e-017),\
						 (-1.3295355374380919, -0.88830478098581056, 1.4285030381193257e-016),\
						 (-1.1308474670756687, -1.1307718807569309, 1.818419873062669e-016),\
						 (-0.88839144588362784, -1.3294735186432725, 2.1379564774755401e-016),\
						 (-0.61191601590586897, -1.477226285107555, 2.3755610477791369e-016),\
						 (-0.31194415892591937, -1.5682561640787946, 2.521948257950109e-016),\
						 (1.9206858326015209e-015, -1.5992086836047279, 2.5717237056643222e-016),\
						 (0.31194415892592192, -1.5682561640787931, 2.521948257950107e-016),\
						 (0.61191601590587141, -1.4772262851075539, 2.3755610477791354e-016),\
						 (0.88839144588363017, -1.3294735186432698, 2.1379564774755361e-016),\
						 (1.1308474670756696, -1.1307718807569294, 1.8184198730626671e-016),\
						 (1.3295355374380937, -0.88830478098580823, 1.428503038119322e-016),\
						 (1.477275393590318, -0.61182275836088262, 9.838860353077712e-017),\
						 (1.5682630253857905, -0.31183819334539253, 5.0147406175296768e-017),\
						 (1.5991784838738621, 0.00011039946845280424, -1.7753588573116074e-020),\
						 (1.5682658227913397, 0.3120587813185336, -5.0182879426882207e-017),\
						 (1.477255302302674, 0.61203519477419133, -9.8422765911562845e-017),\
						 (1.3293898447288979, 0.88844923528804043, -1.4287353383545851e-016),\
						 (1.1305898043401241, 1.1308261083641831, -1.8185070777061297e-016),\
						 (0.88816423422255131, 1.3295695200849658, -2.1381108595683293e-016),\
						 (0.61179992425629881, 1.4775355211816885, -2.3760583373140467e-016),\
						 (0.31192352932345879, 1.5688757999304204, -2.5229447083976604e-016),\
						 (8.8817841970012528e-017, 1.6000000000000012, -2.5729962394826207e-016),\
						 (0, 3.2000000000000002, -7.1054273576010023e-016),\
						 (0, 4, -8.8817841970012523e-016),\
						 (0, 3.2000000000000002, -7.1054273576010023e-016),\
						 (1.2000000000000002, 3.2000000000000002, -7.1054273576010023e-016),\
						 (-1.2000000000000002, 3.2000000000000002, -7.1054273576010023e-016)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap25
def mz_ccButtonSnap25(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton25(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton25(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton26
def mz_ccButton26(self):
	cmds.curve( degree = 1,\
				knot = [0, 4, 8, 12, 16, 24.485281000000001, 32.970562999999999, 36.970562999999999,\
						45.455843999999999, 53.941125, 57.941125, 66.426406999999998, 74.911687999999998],\
				point = [(-0.80000000000000049, 3.2000000000000002, 0.80000000000000004),\
						 (0.7999999999999996, 3.2000000000000002, 0.80000000000000004),\
						 (0.7999999999999996, 3.2000000000000002, -0.80000000000000004),\
						 (-0.80000000000000049, 3.2000000000000002, -0.80000000000000004),\
						 (-0.80000000000000049, 3.2000000000000002, 0.80000000000000004),\
						 (0, 0, 0),\
						 (0.7999999999999996, 3.2000000000000002, 0.80000000000000004),\
						 (0.7999999999999996, 3.2000000000000002, -0.80000000000000004),\
						 (0, 0, 0),\
						 (-0.80000000000000049, 3.2000000000000002, -0.80000000000000004),\
						 (-0.80000000000000049, 3.2000000000000002, 0.80000000000000004),\
						 (0, 0, 0),\
						 (0.7999999999999996, 3.2000000000000002, 0.80000000000000004)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap26
def mz_ccButtonSnap26(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton26(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton26(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton27
def mz_ccButton27(self):
	cmds.curve( degree = 1,\
				knot = [0, 2, 4.0871430000000002, 6.1743430000000004, 8.2614889999999992, 10.348646,\
						12.435838, 14.522990999999999, 16.610143000000001, 18.697337999999998,\
						20.784490000000002, 22.871642000000001, 24.958836000000002, 27.045988999999999,\
						29.133140999999998, 31.220334999999999, 33.307487999999999, 35.394638999999998,\
						37.481833999999999, 39.568986000000002, 41.686399999999999, 48.748496000000003,\
						55.810591000000002, 58.009692000000001, 59.575055999999996, 61.140450999999999,\
						62.705815999999999, 64.271180999999999, 65.836574999999996, 67.401939999999996,\
						68.967304999999996, 70.532698999999994, 72.098063999999994, 73.663428999999994,\
						75.228823000000006, 76.794188000000005, 78.359554000000003, 79.924946000000006,\
						81.490313999999998, 83.055674999999994, 84.621072999999996, 86.186430999999999],\
				point = [(0, 0, -2.4000000000000004),\
						 (0, 0, -3.2000000000000002),\
						 (0.82733600000000007, 0, -3.0881896000000002),\
						 (1.5986624000000003, 0, -2.7686900000000003),\
						 (2.2627592000000001, 0, -2.2627604000000003),\
						 (2.7686924000000004, 0, -1.5986616),\
						 (3.0881860000000003, 0, -0.82733640000000008),\
						 (3.2000248, 0, 2.0621280000000001e-007),\
						 (3.0881860000000003, 0, 0.82733600000000007),\
						 (2.7686924000000004, 0, 1.5986624000000003),\
						 (2.2627592000000001, 0, 2.2627592000000001),\
						 (1.5986624000000003, 0, 2.7686924000000004),\
						 (0.82733600000000007, 0, 3.0881860000000003),\
						 (0, 0, 3.2000248),\
						 (-0.82733600000000007, 0, 3.0881860000000003),\
						 (-1.5986624000000003, 0, 2.7686924000000004),\
						 (-2.2627592000000001, 0, 2.2627592000000001),\
						 (-2.7686924000000004, 0, 1.5986624000000003),\
						 (-3.0881860000000003, 0, 0.82733600000000007),\
						 (-3.2000248, 0, 2.0621280000000001e-007),\
						 (-4.0469904000000003, 0, 0),\
						 (-2.7836844000000003, 0, -2.5266120000000001),\
						 (-1.5203784000000002, 0, 0),\
						 (-2.4000184000000004, 0, 1.5477240000000003e-007),\
						 (-2.3161396000000001, 0, 0.62050240000000001),\
						 (-2.0765191999999999, 0, 1.1989964000000002),\
						 (-1.6970696000000001, 0, 1.6970692000000001),\
						 (-1.1989964000000002, 0, 2.0765191999999999),\
						 (-0.62050240000000001, 0, 2.3161396000000001),\
						 (0, 0, 2.4000184000000004),\
						 (0.62050240000000001, 0, 2.3161396000000001),\
						 (1.1989964000000002, 0, 2.0765191999999999),\
						 (1.6970696000000001, 0, 1.6970692000000001),\
						 (2.0765191999999999, 0, 1.1989964000000002),\
						 (2.3161396000000001, 0, 0.62050240000000001),\
						 (2.4000184000000004, 0, 1.5477240000000003e-007),\
						 (2.3161396000000001, 0, -0.62050280000000013),\
						 (2.0765191999999999, 0, -1.198996),\
						 (1.6970696000000001, 0, -1.6970704000000003),\
						 (1.1989964000000002, 0, -2.0765176000000003),\
						 (0.62050240000000001, 0, -2.3161420000000001),\
						 (0, 0, -2.4000000000000004)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap27
def mz_ccButtonSnap27(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton27(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton27(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton28
def mz_ccButton28(self):
	cmds.curve( degree = 1,\
				knot = [0, 1.411065, 6.7736340000000004, 12.136203, 13.547268000000001, 18.909838000000001,\
						24.272407000000001, 25.683471000000001, 31.046040999999999, 36.408610000000003,\
						37.819674999999997, 43.182243999999997, 48.544812999999998, 49.955877999999998,\
						55.318447999999997, 60.681016999999997, 62.092081999999998, 67.454650999999998,\
						95.205282999999994, 122.955915, 128.31848400000001, 129.72954899999999, 135.092118,\
						140.45468700000001, 141.86575199999999, 143.27681699999999, 144.687883, 150.05045200000001,\
						155.41302099999999, 156.82408599999999, 162.186655, 167.54922400000001, 168.96028999999999,\
						174.32285899999999, 179.685428, 181.09649300000001, 186.45906199999999, 208.56543400000001,\
						214.20969400000001, 219.85395500000001, 225.49821499999999, 231.14247499999999,\
						236.78673499999999, 242.43099599999999, 248.075256, 253.719516, 275.82588800000002,\
						281.18845700000003, 282.59952199999998, 287.96209099999999, 293.32465999999999, 294.735726,\
						300.09829500000001, 305.46086400000002, 306.87192900000002, 308.28299399999997,\
						309.69405999999998, 315.05662899999999, 320.41919799999999, 321.830263, 323.24132800000001,\
						328.60389700000002, 333.96646600000003],\
				point = [(0.1058298, 3.3865561500000001, 0.18330270000000001),\
						 (-0.10582994999999999, 3.3865561500000001, 0.18330270000000001),\
						 (0, 4.1625947999999999, 0),\
						 (0.1058298, 3.3865561500000001, 0.18330270000000001),\
						 (0.21165975000000001, 3.3865561500000001, 0),\
						 (0, 4.1625947999999999, 0),\
						 (0.21165975000000001, 3.3865561500000001, 0),\
						 (0.10582994999999999, 3.3865561500000001, -0.18330270000000001),\
						 (0, 4.1625947999999999, 0),\
						 (0.10582994999999999, 3.3865561500000001, -0.18330270000000001),\
						 (-0.1058298, 3.3865561500000001, -0.18330284999999999),\
						 (0, 4.1625947999999999, 0),\
						 (-0.1058298, 3.3865561500000001, -0.18330284999999999),\
						 (-0.21165975000000001, 3.3865561500000001, -3.3622199999999999e-008),\
						 (0, 4.1625947999999999, 0),\
						 (-0.21165975000000001, 3.3865561500000001, -3.3622199999999999e-008),\
						 (-0.10582994999999999, 3.3865561500000001, 0.18330270000000001),\
						 (0, 4.1625947999999999, 0),\
						 (0, 0, 0),\
						 (0, 0, 4.1625947999999999),\
						 (-0.18330270000000001, 0.10582994999999999, 3.3865561500000001),\
						 (0, 0.21165975000000001, 3.3865561500000001),\
						 (0, 0, 4.1625947999999999),\
						 (0.18330270000000001, 0.1058298, 3.3865561500000001),\
						 (0, 0.21165975000000001, 3.3865561500000001),\
						 (0.18330270000000001, 0.1058298, 3.3865561500000001),\
						 (0.18330270000000001, -0.10582994999999999, 3.3865561500000001),\
						 (0, 0, 4.1625947999999999),\
						 (0.18330270000000001, -0.10582994999999999, 3.3865561500000001),\
						 (-3.3622199999999999e-008, -0.21165975000000001, 3.3865561500000001),\
						 (0, 0, 4.1625947999999999),\
						 (-3.3622199999999999e-008, -0.21165975000000001, 3.3865561500000001),\
						 (-0.18330284999999999, -0.1058298, 3.3865561500000001),\
						 (0, 0, 4.1625947999999999),\
						 (-0.18330284999999999, -0.1058298, 3.3865561500000001),\
						 (-0.18330270000000001, 0.10582994999999999, 3.3865561500000001),\
						 (0, 0, 4.1625947999999999),\
						 (0, 0, 0.84663900000000003),\
						 (0, 0.84663900000000003, 0.84663900000000003),\
						 (0, 0.84663900000000003, 0),\
						 (0.84663900000000003, 0.84663900000000003, 0),\
						 (0.84663900000000003, 0, 0),\
						 (0, 0, 0),\
						 (0, 0, 0.84663900000000003),\
						 (0.84663900000000003, 0, 0.84663900000000003),\
						 (0.84663900000000003, 0, 0),\
						 (4.1625947999999999, 0, 0),\
						 (3.3865561500000001, 0.21165975000000001, 0),\
						 (3.3865561500000001, 0.1058298, -0.18330270000000001),\
						 (4.1625947999999999, 0, 0),\
						 (3.3865561500000001, 0.1058298, -0.18330270000000001),\
						 (3.3865561500000001, -0.10582994999999999, -0.18330270000000001),\
						 (4.1625947999999999, 0, 0),\
						 (3.3865561500000001, -0.21165975000000001, 3.3622199999999999e-008),\
						 (3.3865561500000001, -0.10582994999999999, -0.18330270000000001),\
						 (3.3865561500000001, -0.21165975000000001, 3.3622199999999999e-008),\
						 (3.3865561500000001, -0.1058298, 0.18330284999999999),\
						 (4.1625947999999999, 0, 0),\
						 (3.3865561500000001, -0.1058298, 0.18330284999999999),\
						 (3.3865561500000001, 0.10582994999999999, 0.18330270000000001),\
						 (3.3865561500000001, 0.21165975000000001, 0),\
						 (4.1625947999999999, 0, 0),\
						 (3.3865561500000001, 0.10582994999999999, 0.18330270000000001)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap28
def mz_ccButtonSnap28(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton28(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton28(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton29
def mz_ccButton29(self):
	cmds.curve( degree = 1,\
				knot = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],\
				point = [(-2.0857863095420344, -9.3632573363181929e-025, 5.0971193932269898e-009),\
						 (2.0857863095420339, -5.1957367987512135e-016, 2.8284273758870384),\
						 (1.5905961601981407, -4.0800222655138452e-016, 2.2210606728157671),\
						 (1.2229632672818962, -2.8086649577231904e-016, 1.5289659895836587),\
						 (0.99353414115743455, -1.4321487083376504e-016, 0.779625444841058),\
						 (0.91421332817924306, -7.8384805911619546e-025, 4.2670694477831006e-009),\
						 (0.99353414115743632, 1.4321486858069046e-016, -0.77962543257589201),\
						 (1.2229632672818953, 2.8086649447759225e-016, -1.5289659825354958),\
						 (1.590596160198142, 4.0800222361869959e-016, -2.221060656850975),\
						 (2.0857863095420335, 5.1957367987512135e-016, -2.8284273758870384),\
						 (-2.0857863095420344, -9.3632573363181929e-025, 5.0971193932269898e-009)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap29
def mz_ccButtonSnap29(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton29(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton29(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton30
def mz_ccButton30(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],\
				point = [(-2.0857863095420344, -9.3632573363181929e-025, 5.0971193932269898e-009),\
						 (2.0857863095420335, 2.8284273758870384, -1.0846335936285916e-016),\
						 (1.590596160198142, 2.221060656850975, -8.5172312446305679e-017),\
						 (1.2229632672818953, 1.5289659825354958, -5.863215305831422e-017),\
						 (0.99353414115743632, 0.77962543257589201, -2.989675258513013e-017),\
						 (0.91421332817924306, -7.8384805911619546e-025, 4.2670694477831006e-009),\
						 (-2.0857863095420344, -9.3632573363181929e-025, 5.0971193932269898e-009),\
						 (2.0857863095420339, -5.1957367987512135e-016, 2.8284273758870384),\
						 (1.5905961601981407, -4.0800222655138452e-016, 2.2210606728157671),\
						 (1.2229632672818962, -2.8086649577231904e-016, 1.5289659895836587),\
						 (0.99353414115743455, -1.4321487083376504e-016, 0.779625444841058),\
						 (0.91421332817924306, -7.8384805911619546e-025, 4.2670694477831006e-009),\
						 (0.99353414115743632, 1.4321486858069046e-016, -0.77962543257589201),\
						 (1.2229632672818953, 2.8086649447759225e-016, -1.5289659825354958),\
						 (1.590596160198142, 4.0800222361869959e-016, -2.221060656850975),\
						 (2.0857863095420335, 5.1957367987512135e-016, -2.8284273758870384),\
						 (-2.0857863095420344, -9.3632573363181929e-025, 5.0971193932269898e-009)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap30
def mz_ccButtonSnap30(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton30(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton30(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton31
def mz_ccButton31(self):
	cmds.curve( degree = 3,\
				knot = [-0.0625, -0.03125, 0, 0.03125, 0.0625, 0.09375, 0.125, 0.15625, 0.1875,\
						0.21875, 0.25, 0.28125, 0.3125, 0.34374999999999994, 0.375, 0.40625,\
						0.4375, 0.46875, 0.5, 0.53125, 0.5625, 0.59375, 0.625, 0.65625,\
						0.68749999999999989, 0.71875000000000011, 0.75, 0.78125, 0.8125,\
						0.84375, 0.875, 0.90625000000000011, 0.9375, 0.96875, 1, 1.03125, 1.0625],\
				point = [(0.58861386459314402, -0.53470441984959005, -2.9592563244160668),\
						 (-9.1493801345217877e-016, 0.53470441984959038, -3.0203722237754098),\
						 (-0.58861386459314979, -0.53470441984959005, -2.9592563244160668),\
						 (-1.1538590132298956, 0.53470441984959038, -2.7856622316112523),\
						 (-1.6762970257645677, -0.53470441984959005, -2.5087230486515049),\
						 (-2.1357258630710247, 0.53470441984959038, -2.13572609126081),\
						 (-2.5087227360730369, -0.53470441984959016, -1.6762972987936653),\
						 (-2.7856620788060509, 0.53470441984959027, -1.1538592622322161),\
						 (-2.9592558529950805, -0.53470441984959027, -0.5886141264006699),\
						 (-3.0203724810660262, 0.53470441984959027, -2.5494660060499269e-007),\
						 (-2.9592558529950779, -0.53470441984959027, 0.5886136059885243),\
						 (-2.785662078806054, 0.53470441984959027, 1.1538587565872813),\
						 (-2.5087227360730338, -0.53470441984959027, 1.6762967680753449),\
						 (-2.1357258630710261, 0.53470441984959005, 2.1357256059439962),\
						 (-1.6762970257645669, -0.53470441984959038, 2.5087224786436075),\
						 (-1.1538590132298974, 0.53470441984959005, 2.7856618215437541),\
						 (-0.58861386459314713, -0.53470441984959038, 2.9592555956343283),\
						 (-1.7695683200978657e-015, 0.53470441984959005, 3.0203722237754098),\
						 (0.58861386459314513, -0.53470441984959038, 2.9592555956343274),\
						 (1.1538590132298963, 0.53470441984959005, 2.7856618215437545),\
						 (1.6762970257645613, -0.53470441984959038, 2.5087224786436062),\
						 (2.1357258630710252, 0.53470441984959005, 2.1357256059439966),\
						 (2.5087227360730293, -0.53470441984959027, 1.676296768075344),\
						 (2.7856620788060495, 0.53470441984959027, 1.1538587565872847),\
						 (2.9592558529950725, -0.53470441984959027, 0.58861360598852408),\
						 (3.0203724810660262, 0.53470441984959027, -2.5494659819101423e-007),\
						 (2.9592558529950725, -0.53470441984959027, -0.58861412640066746),\
						 (2.7856620788060522, 0.53470441984959027, -1.1538592622322161),\
						 (2.508722736073032, -0.53470441984959016, -1.6762972987936595),\
						 (2.1357258630710279, 0.53470441984959038, -2.1357260912608118),\
						 (1.6762970257645611, -0.53470441984959005, -2.5087230486515066),\
						 (1.1538590132298925, 0.53470441984959038, -2.7856622316112523),\
						 (0.58861386459314402, -0.53470441984959005, -2.9592563244160668),\
						 (-9.1493801345217877e-016, 0.53470441984959038, -3.0203722237754098),\
						 (-0.58861386459314979, -0.53470441984959005, -2.9592563244160668)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap31
def mz_ccButtonSnap31(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton31(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton31(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton32
def mz_ccButton32(self):
	cmds.curve( degree = 1,\
				knot = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,\
						26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,\
						51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76],\
				point = [(3.6915440258113947, -9.3629908994031406e-017, 1.5290924543994273),\
						 (2.8282092152668978, -1.731777004387582e-016, 2.8282064765013288),\
						 (1.4141046076334489, -8.6588850219379102e-017, 1.4141032382506644),\
						 (1.8457720129056974, -4.6814954497015703e-017, 0.76454622719971366),\
						 (3.6915440258113947, -9.3629908994031406e-017, 1.5290924543994273),\
						 (3.9996918294590156, 5.4462398553035891e-022, -8.8943846656142078e-006),\
						 (1.9998459147295078, 2.7231199276517946e-022, -4.4471923328071039e-006),\
						 (1.8457720129056974, -4.6814954497015703e-017, 0.76454622719971366),\
						 (1.4141046076334489, -8.6588850219379102e-017, 1.4141032382506644),\
						 (0.76454380079422812, -1.130209927361695e-016, 1.8457728843101386),\
						 (1.5290876015884562, -2.26041985472339e-016, 3.6915457686202773),\
						 (2.8282092152668978, -1.731777004387582e-016, 2.8282064765013288),\
						 (1.4141046076334489, -8.6588850219379102e-017, 1.4141032382506644),\
						 (0.76454380079422812, -1.130209927361695e-016, 1.8457728843101386),\
						 (8.3266726846886741e-017, -1.2245520061760724e-016, 1.9998451913297028),\
						 (1.6653345369377348e-016, -2.4491040123521448e-016, 3.9996903826594057),\
						 (1.5290876015884562, -2.26041985472339e-016, 3.6915457686202773),\
						 (0.76454380079422812, -1.130209927361695e-016, 1.8457728843101386),\
						 (8.3266726846886741e-017, -1.2245520061760724e-016, 1.9998451913297028),\
						 (-0.76454380079422712, -1.130209927361695e-016, 1.8457728843101384),\
						 (-1.5290876015884542, -2.26041985472339e-016, 3.6915457686202768),\
						 (1.6653345369377348e-016, -2.4491040123521448e-016, 3.9996903826594057),\
						 (8.3266726846886741e-017, -1.2245520061760724e-016, 1.9998451913297028),\
						 (-0.76454380079422712, -1.130209927361695e-016, 1.8457728843101384),\
						 (-1.4141046076334489, -8.6588850219379053e-017, 1.414103238250664),\
						 (-2.8282092152668978, -1.7317770043875811e-016, 2.8282064765013279),\
						 (-1.5290876015884542, -2.26041985472339e-016, 3.6915457686202768),\
						 (-0.76454380079422712, -1.130209927361695e-016, 1.8457728843101384),\
						 (-1.4141046076334489, -8.6588850219379053e-017, 1.414103238250664),\
						 (-1.8457720129056985, -4.6814954497015678e-017, 0.76454622719971232),\
						 (-3.691544025811397, -9.3629908994031357e-017, 1.5290924543994246),\
						 (-2.8282092152668978, -1.7317770043875811e-016, 2.8282064765013279),\
						 (-1.4141046076334489, -8.6588850219379053e-017, 1.414103238250664),\
						 (-1.8457720129056985, -4.6814954497015678e-017, 0.76454622719971232),\
						 (-1.9998459147295065, 2.7231199284837963e-022, -4.4471923335287489e-006),\
						 (-3.9996918294590129, 5.4462398569675926e-022, -8.8943846670574978e-006),\
						 (-3.691544025811397, -9.3629908994031357e-017, 1.5290924543994246),\
						 (-1.8457720129056985, -4.6814954497015678e-017, 0.76454622719971232),\
						 (-1.9998459147295065, 2.7231199284837963e-022, -4.4471923335287489e-006),\
						 (-1.8457720129056985, 4.6814304039116263e-017, -0.76453560441606883),\
						 (-3.691544025811397, 9.3628608078232526e-017, -1.5290712088321377),\
						 (-3.9996918294590129, 5.4462398569675926e-022, -8.8943846670574978e-006),\
						 (-1.9998459147295065, 2.7231199284837963e-022, -4.4471923335287489e-006),\
						 (-1.8457720129056985, 4.6814304039116263e-017, -0.76453560441606883),\
						 (-1.414104607633448, 8.658982224938694e-017, -1.4141191127053805),\
						 (-2.8282092152668961, 1.7317964449877388e-016, -2.828238225410761),\
						 (-3.691544025811397, 9.3628608078232526e-017, -1.5290712088321377),\
						 (-1.8457720129056985, 4.6814304039116263e-017, -0.76453560441606883),\
						 (-1.414104607633448, 8.658982224938694e-017, -1.4141191127053805),\
						 (-0.76454380079422712, 1.1301958153051444e-016, -1.8457498375728087),\
						 (-1.5290876015884542, 2.2603916306102888e-016, -3.6914996751456175),\
						 (-2.8282092152668961, 1.7317964449877388e-016, -2.828238225410761),\
						 (-1.414104607633448, 8.658982224938694e-017, -1.4141191127053805),\
						 (-0.76454380079422712, 1.1301958153051444e-016, -1.8457498375728087),\
						 (-2.7755575615628914e-017, 1.2246467991473535e-016, -2.0000000000000009),\
						 (-5.5511151231257827e-017, 2.4492935982947069e-016, -4.0000000000000018),\
						 (-1.5290876015884542, 2.2603916306102888e-016, -3.6914996751456175),\
						 (-0.76454380079422712, 1.1301958153051444e-016, -1.8457498375728087),\
						 (-2.7755575615628914e-017, 1.2246467991473535e-016, -2.0000000000000009),\
						 (0.76454380079422657, 1.1301958153051444e-016, -1.845749837572809),\
						 (1.5290876015884531, 2.2603916306102888e-016, -3.6914996751456179),\
						 (-5.5511151231257827e-017, 2.4492935982947069e-016, -4.0000000000000018),\
						 (-2.7755575615628914e-017, 1.2246467991473535e-016, -2.0000000000000009),\
						 (0.76454380079422657, 1.1301958153051444e-016, -1.845749837572809),\
						 (1.4141046076334503, 8.6589822249386927e-017, -1.4141191127053805),\
						 (2.8282092152669005, 1.7317964449877385e-016, -2.828238225410761),\
						 (1.5290876015884531, 2.2603916306102888e-016, -3.6914996751456179),\
						 (0.76454380079422657, 1.1301958153051444e-016, -1.845749837572809),\
						 (1.4141046076334503, 8.6589822249386927e-017, -1.4141191127053805),\
						 (1.8457720129056994, 4.681430403911622e-017, -0.76453560441606694),\
						 (3.6915440258113987, 9.3628608078232439e-017, -1.5290712088321339),\
						 (2.8282092152669005, 1.7317964449877385e-016, -2.828238225410761),\
						 (1.4141046076334503, 8.6589822249386927e-017, -1.4141191127053805),\
						 (1.8457720129056994, 4.681430403911622e-017, -0.76453560441606694),\
						 (1.9998459147295078, 2.7231199276517946e-022, -4.4471923328071039e-006),\
						 (3.9996918294590156, 5.4462398553035891e-022, -8.8943846656142078e-006),\
						 (3.6915440258113987, 9.3628608078232439e-017, -1.5290712088321339)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap32
def mz_ccButtonSnap32(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton32(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton32(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton33
def mz_ccButton33(self):
	#lowerLip ctrl
	lowerLipCtrl = cmds.curve( degree = 3,\
								knot = [-0.0625, -0.03125, 0, 0.03125, 0.0625, 0.09375, 0.125, 0.15625, 0.1875,\
										0.21875, 0.25, 0.28125, 0.3125, 0.34374999999999994, 0.375, 0.40625, 0.4375,\
										0.46875, 0.5, 0.53125, 0.5625, 0.59375, 0.625, 0.65625, 0.68749999999999989,\
										0.71875000000000011, 0.75, 0.78125, 0.8125, 0.84375, 0.875, 0.90625000000000011,\
										0.9375, 0.96875, 1, 1.03125, 1.0625],\
								point = [(4.1586760871755955e-017, -0.078481848612419428, -2.8181393974009046),\
										 (2.4659259073008035e-017, -1.0005286979807415e-016, -3.2165052773850884),\
										 (6.7338187338943015e-018, 0.078481848612419761, -2.8181393974009046),\
										 (5.274868544319447e-018, 0.078669530972728385, -2.6528234054767039),\
										 (7.6646014695000367e-018, 0.05772441132037285, -2.3890904927148315),\
										 (1.447077356135111e-017, 0.013357489510922083, -2.0338804679988209),\
										 (2.7383988389083284e-017, -0.061691101893637815, -1.5963602429837824),\
										 (2.5782714976181116e-017, -0.073689023285074914, -1.0988354664339401),\
										 (-9.4505999428234055e-019, 0.025898793026568126, -0.56054491287582853),\
										 (-1.6666521407561656e-017, 0.075059339513305665, 2.2624062088525939e-009),\
										 (-1.0556314489868419e-017, 0.025898793026567724, 0.56054490738330853),\
										 (6.9417850756346022e-018, -0.073689023285074567, 1.0988354750044338),\
										 (1.2364436873077406e-020, -0.061691101893638217, 1.5963602276765536),\
										 (-2.0402690763278213e-017, 0.013357489510922261, 2.0338804959280576),\
										 (-3.329937486170919e-017, 0.057724346612149625, 2.3890904399916097),\
										 (-4.0211175212285627e-017, 0.07866960287365185, 2.6528235050668769),\
										 (-4.1586759123473419e-017, 0.078481848612419414, 2.8181391934752158),\
										 (-2.4659263274727054e-017, 1.3897837754684109e-017, 3.2165057674880586),\
										 (-6.7338169856118417e-018, -0.07848184861241958, 2.8181391934752149),\
										 (1.1418074841646101e-017, -0.15384786843065307, 2.6528235050668774),\
										 (2.9146366319394119e-017, -0.22350627010194174, 2.3890904399916084),\
										 (4.5793455117135146e-017, -0.28476344840947027, 2.0338804959280585),\
										 (1.3932105297393567e-016, -0.68908165967862578, 1.5963602276765527),\
										 (1.8606117604324313e-016, -0.88037104570162672, 1.0988354750044369),\
										 (1.6159730075135922e-016, -0.7494121644243088, 0.56054490738330831),\
										 (1.4363641154837683e-016, -0.64688088961345658, 2.2624085077167814e-009),\
										 (1.7120855524694535e-016, -0.7494121644243088, -0.5605449128758262),\
										 (2.0490210594378969e-016, -0.88037104570162716, -1.0988354664339401),\
										 (1.6669267692614601e-016, -0.68908165967862611, -1.5963602429837771),\
										 (8.0666919441764454e-017, -0.28476344840947065, -2.0338804679988227),\
										 (7.0110357018715263e-017, -0.22350627010194168, -2.3890904927148333),\
										 (5.6904102633038839e-017, -0.15384786843065257, -2.6528234054767035),\
										 (4.1586760871755955e-017, -0.078481848612419428, -2.8181393974009046),\
										 (2.4659259073008035e-017, -1.0005286979807415e-016, -3.2165052773850884),\
										 (6.7338187338943015e-018, 0.078481848612419761, -2.8181393974009046)]\
							  )
	#upperLip ctrl
	upperLipCtrl = cmds.curve( degree = 3,\
								knot = [-0.0625, -0.03125, 0, 0.03125, 0.0625, 0.09375, 0.125, 0.15625, 0.1875,\
										0.21875, 0.25, 0.28125, 0.3125, 0.34374999999999994, 0.375, 0.40625,\
										0.4375, 0.46875, 0.5, 0.53125, 0.5625, 0.59375, 0.625, 0.65625, 0.68749999999999989,\
										0.71875000000000011, 0.75, 0.78125, 0.8125, 0.84375, 0.875, 0.90625000000000011,\
										0.9375, 0.96875, 1, 1.03125, 1.0625],\
								point = [(-3.6617721706843892e-016, 0.25147225754440167, 2.8181393974009046),\
										 (-4.0582602516255544e-016, 0.16472814103675762, 3.2165052773850884),\
										 (-3.4890127183460769e-016, 0.077984024529113016, 2.8181393974009046),\
										 (-3.3005252118965219e-016, 0.077776583690028794, 2.6528234054767039),\
										 (-3.0232086169148782e-016, 0.10092672517513855, 2.3890904927148315),\
										 (-2.4319849081849315e-016, 0.038023542109642455, 2.0338804679988209),\
										 (-1.7098663516530611e-016, -0.024678234301747273, 1.5963602429837824),\
										 (-1.1095738552658047e-016, -0.033690795710892042, 1.0988354664339401),\
										 (-9.7567813980243131e-017, 0.1361028224513276, 0.56054491287582853),\
										 (-4.52868984429307e-017, 0.16243603015231334, -2.2624062088525939e-009),\
										 (3.0114837517874043e-017, 0.13610282245132804, -0.56054490738330853),\
										 (1.3933875297403864e-016, -0.033690795710892445, -1.0988354750044338),\
										 (1.9263723137912469e-016, -0.024678234301746829, -1.5963602276765536),\
										 (2.2008508927383802e-016, 0.038023542109642254, -2.0338804959280576),\
										 (2.4187353898577517e-016, 0.10092679669559526, -2.3890904399916097),\
										 (2.7421580957293305e-016, 0.077776504219651987, -2.6528235050668769),\
										 (2.9302320384994394e-016, 0.077984024529113405, -2.8181391934752158),\
										 (3.3267209098805653e-016, 0.16472814103675748, -3.2165057674880586),\
										 (2.757472586161126e-016, 0.25147225754440178, -2.8181391934752149),\
										 (2.5810943193998175e-016, 0.28968617093646548, -2.6528235050668774),\
										 (2.2277985593801145e-016, 0.35539252979687991, -2.3890904399916084),\
										 (1.6372278682316895e-016, 0.47947039268704139, -2.0338804959280585),\
										 (1.2940207055320073e-016, 0.68392495569292955, -1.6699128084708303),\
										 (5.3741701938408123e-017, 0.91898225418857893, -1.2297813767771351),\
										 (-2.7733304333212219e-017, 0.9082137141500678, -0.63926424120404912),\
										 (-9.7795039163941054e-017, 0.69014201996729707, -2.2624085077167814e-009),\
										 (-1.7469663187024553e-016, 0.9082137141500678, 0.63926424669656678),\
										 (-2.286269324556911e-016, 0.91898225418857926, 1.2297813682066387),\
										 (-2.5223698251897717e-016, 0.68392495569292988, 1.6699128237780543),\
										 (-2.9956079326916254e-016, 0.47947039268704172, 2.0338804679988227),\
										 (-3.2141455186125321e-016, 0.35539252979687985, 2.3890904927148333),\
										 (-3.4615889090894929e-016, 0.28968617093646493, 2.6528234054767035),\
										 (-3.6617721706843892e-016, 0.25147225754440167, 2.8181393974009046),\
										 (-4.0582602516255544e-016, 0.16472814103675762, 3.2165052773850884),\
										 (-3.4890127183460769e-016, 0.077984024529113016, 2.8181393974009046)]\
							  )
	#put the upperLip ctrl underneath lowerLip ctrl
	cmds.parent(upperLipCtrl, lowerLipCtrl)
	cmds.select(lowerLipCtrl, replace = 1)
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap33
def mz_ccButtonSnap33(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton33(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton33(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
						

#mz_ccButton34
def mz_ccButton34(self):
	cmds.curve( degree = 3,\
				knot = [-0.125, -0.0625, 0, 0.0625, 0.125, 0.1875, 0.25, 0.3125, 0.375, 0.4375, 0.5, 0.5625,\
						0.625, 0.68749999999999989, 0.75, 0.8125, 0.875, 0.9375, 1, 1.0625, 1.125],\
				point = [(7.2720718463205509e-017, 1.2994958327503943, -2.3650985432555687),\
						 (-1.5721101582347884e-016, 0.88118819320136388, -2.5674507283722168),\
						 (-3.6236175452980667e-016, 0.84584253694393374, -2.3650985432555687),\
						 (-5.1421002400042411e-016, 1.1584377880816721, -1.8152788804015749),\
						 (-5.8517905827366483e-016, 1.5947679589781483, -0.97967928042848573),\
						 (-5.7000890360322904e-016, 1.7830574937529287, -2.1031004997970949e-005),\
						 (-4.6519984000624716e-016, 1.594699247456006, 0.97973005050597606),\
						 (-2.9190745804910439e-016, 1.1584821264601102, 1.8151975329789358),\
						 (-7.2711193086758609e-017, 0.84562862371461867, 2.36525410445826),\
						 (1.5718847945313973e-016, 0.88143348037097879, 2.567082681514063),\
						 (3.6237127990625401e-016, 1.299420120431658, 2.3652541044582605),\
						 (5.1420504290738654e-016, 1.8866525537871803, 1.8151975329789365),\
						 (5.8518216704430905e-016, 2.3728279811565729, 0.9797300505059765),\
						 (5.7000632804793454e-016, 2.5674936881655688, -2.1031004997003702e-005),\
						 (4.6520294877689237e-016, 2.3728300554666775, -0.97967928042848207),\
						 (2.919024769560677e-016, 1.8866476273006925, -1.8152788804015758),\
						 (7.2720718463205509e-017, 1.2994958327503943, -2.3650985432555687),\
						 (-1.5721101582347884e-016, 0.88118819320136388, -2.5674507283722168),\
						 (-3.6236175452980667e-016, 0.84584253694393374, -2.3650985432555687)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap34
def mz_ccButtonSnap34(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton34(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton34(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton35
def mz_ccButton35(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7],\
				point = [(0, 0, 0),\
						 (5.3290705182007522e-016, 2.4000000000000004, -2.4000000000000004),\
						 (5.3290705182007522e-016, 2.4000000000000004, -1.6000000000000001),\
						 (1.0658141036401504e-015, 4.8000000000000007, -1.6000000000000001),\
						 (1.0658141036401504e-015, 4.8000000000000007, 1.6000000000000001),\
						 (5.3290705182007522e-016, 2.4000000000000004, 1.6000000000000001),\
						 (5.3290705182007522e-016, 2.4000000000000004, 2.4000000000000004),\
						 (0, 0, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap35
def mz_ccButtonSnap35(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton35(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton35(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton36
def mz_ccButton36(self):
	#eyes ctrl
	eyesCtrl = cmds.curve( degree = 3,\
							knot = [-0.125, -0.0625, 0, 0.0625, 0.125, 0.1875, 0.25, 0.3125, 0.375, 0.4375,\
									0.5, 0.5625, 0.625, 0.68749999999999989, 0.75, 0.8125, 0.875, 0.9375, 1, 1.0625, 1.125],\
							point = [(5.4667766244599386e-016, -1.4704200208281852, -3.5957931707434332),\
									 (2.3901680489201403e-016, -8.4984610036314788e-016, -3.9034406501274796),\
									 (-1.0632000275130833e-016, 1.4704200208281888, -3.5957931707434332),\
									 (-3.208896543184324e-016, 2.2062370182034488, -2.7598712196396766),\
									 (-3.023093244110717e-016, 1.772223014694893, -1.4894618560943953),\
									 (-2.9435037134086058e-016, 1.3256450402002948, -3.1974627171973714e-005),\
									 (-4.847409168528897e-016, 1.7723148725901197, 1.4895390447165942),\
									 (-6.5886200110549474e-016, 2.206206278008942, 2.7597475425490887),\
									 (-5.4669711720006189e-016, 1.4704424162615588, 3.5960296792440474),\
									 (-2.3898254157271632e-016, 3.0205530167176254e-016, 3.902881087658999),\
									 (1.0631049356755134e-016, -1.4704424162615617, 3.5960296792440483),\
									 (3.2089040166174368e-016, -2.2062062780089424, 2.75974754254909),\
									 (3.0232499452117143e-016, -1.772314872590121, 1.4895390447165948),\
									 (2.9435428710334364e-016, -1.3256450402002999, -3.1974627170503149e-005),\
									 (4.8471579386287967e-016, -1.7722230146948952, -1.4894618560943897),\
									 (6.5887639983749675e-016, -2.2062370182034554, -2.759871219639678),\
									 (5.4667766244599386e-016, -1.4704200208281852, -3.5957931707434332),\
									 (2.3901680489201403e-016, -8.4984610036314788e-016, -3.9034406501274796),\
									 (-1.0632000275130833e-016, 1.4704200208281888, -3.5957931707434332)]\
						  )
	#left eyes ctrl
	leftEyeCtrl = cmds.curve( degree = 3,\
							knot = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\
							point = [(3.1077074990292601e-016, -1.0970562748477151, -3.0970562748477133),\
									 (9.5000252523552743e-017, 1.7700438850961058e-016, -3.5514718625761432),\
									 (-1.764201043552486e-016, 1.097056274847714, -3.0970562748477137),\
									 (-3.4449595677802209e-016, 1.551471862576143, -2.0000000000000004),\
									 (-3.1077074990292582e-016, 1.0970562748477142, -0.90294372515228649),\
									 (-9.5000252523552904e-017, 4.6748875090267269e-016, -0.44852813742385678),\
									 (1.7642010435524845e-016, -1.0970562748477133, -0.90294372515228605),\
									 (3.4449595677802209e-016, -1.551471862576143, -1.9999999999999991),\
									 (3.1077074990292601e-016, -1.0970562748477151, -3.0970562748477133),\
									 (9.5000252523552743e-017, 1.7700438850961058e-016, -3.5514718625761432),\
									 (-1.764201043552486e-016, 1.097056274847714, -3.0970562748477137)]\
						  )
	#cmds.move(0, 0, -2, leftEyeCtrl + ".scalePivot")
	#cmds.move(0, 0, -2, leftEyeCtrl + ".rotatePivot")
	#right eyes ctrl
	rightEyeCtrl = cmds.curve( degree = 3,\
							knot = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\
							point = [(3.1077074990292601e-016, -1.0970562748477151, 0.90294372515228671),\
									 (9.5000252523552743e-017, 1.7700438850961058e-016, 0.448528137423857),\
									 (-1.764201043552486e-016, 1.097056274847714, 0.90294372515228605),\
									 (-3.4449595677802209e-016, 1.551471862576143, 1.9999999999999996),\
									 (-3.1077074990292582e-016, 1.0970562748477142, 3.0970562748477137),\
									 (-9.5000252523552904e-017, 4.6748875090267269e-016, 3.5514718625761432),\
									 (1.7642010435524845e-016, -1.0970562748477133, 3.0970562748477137),\
									 (3.4449595677802209e-016, -1.551471862576143, 2.0000000000000009),\
									 (3.1077074990292601e-016, -1.0970562748477151, 0.90294372515228671),\
									 (9.5000252523552743e-017, 1.7700438850961058e-016, 0.448528137423857),\
									 (-1.764201043552486e-016, 1.097056274847714, 0.90294372515228605)]\
						  )
	#cmds.move(0, 0, 2, rightEyeCtrl + ".scalePivot")
	#cmds.move(0, 0, 2, rightEyeCtrl + ".rotatePivot")
	#parent right and left eye ctrl underneath eyes ctrl
	cmds.parent(leftEyeCtrl, eyesCtrl)
	cmds.parent(rightEyeCtrl, eyesCtrl)
	cmds.select(eyesCtrl, replace = 1)
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap36
def mz_ccButtonSnap36(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton36(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton36(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton37
def mz_ccButton37(self):
	cmds.curve( degree = 3,\
				knot = [0, 0, 0, 0.027777777777777773, 0.055555555555555546, 0.083333333333333329,\
						0.11111111111111109, 0.1388888888888889, 0.16666666666666666, 0.19444444444444445,\
						0.22222222222222218, 0.25, 0.27777777777777779, 0.30555555555555558, 0.33333333333333331,\
						0.3611111111111111, 0.3888888888888889, 0.41666666666666669, 0.44444444444444436,\
						0.47222222222222221, 0.5, 0.52777777777777779, 0.55555555555555558, 0.58333333333333337,\
						0.61111111111111116, 0.63888888888888884, 0.66666666666666663, 0.69444444444444431,\
						0.72222222222222221, 0.75, 0.77777777777777779, 0.80555555555555558, 0.83333333333333337,\
						0.86111111111111116, 0.88888888888888873, 0.91666666666666663, 0.94444444444444442,\
						0.97222222222222221, 1, 1, 1],\
				point = [(0.0042846424073841654, 1.4825828442512174, 0.74605669343488845),\
						 (0.0012911261408082883, 1.3491715268382307, 0.55296872080904858),\
						 (-0.0046677955435500823, 0.86959671911984615, 0.14858976609841387),\
						 (-0.0079202892712114947, -0.068461680847409542, 0.73413486617074197),\
						 (0.014323974644007222, 0.58326776407758185, 1.4294234410884512),\
						 (0.0085540696525040292, 1.203456465550653, 1.8426839450516994),\
						 (0.0083458463828882442, 1.9971123311263987, 2.0283752743153745),\
						 (0.010059473757073107, 2.7808262337339986, 1.765116944627894),\
						 (0.0017479009466927315, 3.3718697747756137, 1.2512203126283767),\
						 (-0.00076168073682232943, 3.7419181639092196, 0.52388870442378965),\
						 (-0.0048102399236967259, 3.8280190286673745, -0.26138162324696157),\
						 (0.00044457650946134325, 3.6419327289799215, -1.043477835594792),\
						 (0.011211978181936467, 3.239424103483465, -1.726166230491192),\
						 (0.01418759736783717, 2.6190910959078253, -2.2377385433159542),\
						 (0.013950537270604777, 1.8801372029671275, -2.5274432680126591),\
						 (0.0040841798262233964, 1.0758043103800494, -2.5365799327539627),\
						 (0.0045309070055883725, 0.31900664615383073, -2.2847184623679686),\
						 (-0.0025137725283751796, -0.28002657510994255, -1.7641165897078293),\
						 (-0.0085528173658597981, -0.92807202387929832, -1.2967433701083211),\
						 (-0.017211602851218095, -1.7324940441574719, -1.2003545533007844),\
						 (-0.020394479919590557, -2.4963995493056932, -1.1165901285964821),\
						 (-0.016003599841645958, -3.2162216280070068, -0.63760186121760398),\
						 (0.0074951406030358747, -3.2017214617129044, 0.29113957587819839),\
						 (0.0077601308028441025, -2.5292402290620024, 0.70032451843193588),\
						 (0.017268074736741967, -1.7850498840042652, 1.1438452818858833),\
						 (0.01360936682221758, -0.93790595603698479, 0.4276310380014684),\
						 (0.0012324234927648236, -2.3256871710507458, 0.1889086833584144),\
						 (-0.0021125743257816671, -1.8962611182768918, -0.62735442386658524),\
						 (-0.0012020234920010369, -0.99891149730062123, -0.59024828985780209),\
						 (-0.0023514724333760363, -0.27543282322095919, -0.77287270962000409),\
						 (-0.0088357272621925557, 0.32203987603711298, -1.3830927148509866),\
						 (-0.0077135376497158414, 1.0292241783286571, -1.6800920777007198),\
						 (0.0045672361477779267, 1.877963076200506, -1.5926436710514111),\
						 (0.015680954018943743, 2.4812548656072329, -1.0513317948666503),\
						 (0.017782594746068095, 2.6458261733627975, -0.24634014578839966),\
						 (0.015635545703409207, 2.5395588613523454, 0.55666298153115101),\
						 (0.011276695221016602, 1.9275055312690017, 1.1270116767543406),\
						 (0.003793853928484471, 1.3698453084484996, 1.169698579412189),\
						 (1.0630802479859386e-017, 1.1157645443069566, 1.1636414223939007)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap37
def mz_ccButtonSnap37(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton37(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton37(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton38
def mz_ccButton38(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
						21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,\
						41, 42, 43, 44, 45, 46, 47, 48],\
				point = [(-3.1365431247355415, -3.819023300387824e-017, 0.623693836140637),\
						 (-4, 0, 0.80000000000000004),\
						 (-4, 0, 1.6000000000000001),\
						 (-5.6000000000000005, 0, 0),\
						 (-4, 0, -1.6000000000000001),\
						 (-4, 0, -0.80000000000000004),\
						 (-3.1365342751582044, 3.8192692435327155e-017, -0.62373400170430104),\
						 (-2.9532115201439462, 7.4904857374240085e-017, -1.223289154495677),\
						 (-2.6588921488091724, 1.0880178124855442e-016, -1.7768679316241476),\
						 (-2.2625592428733143, 1.3854423128474127e-016, -2.2625990021155689),\
						 (-1.776794143541462, 1.6281013397300349e-016, -2.6588912670389244),\
						 (-1.2232143185648301, 1.808320895540634e-016, -2.9532121372458668),\
						 (-0.62370040326238529, 1.9206572749663177e-016, -3.1366713672930926),\
						 (-0.80000000000000004, 0, -4),\
						 (-1.6000000000000001, 0, -4),\
						 (0, 0, -5.6000000000000005),\
						 (1.6000000000000001, 0, -4),\
						 (0.80000000000000004, 0, -4),\
						 (0.62370040326238407, 1.9206572749663185e-016, -3.1366713672930926),\
						 (1.2232143185648312, 1.808320895540634e-016, -2.9532121372458664),\
						 (1.7767941435414629, 1.6281013397300349e-016, -2.6588912670389258),\
						 (2.2625592428733148, 1.3854423128474151e-016, -2.2625990021155715),\
						 (2.6588921488091737, 1.0880178124855452e-016, -1.7768679316241494),\
						 (2.9532115201439439, 7.4904857374240603e-017, -1.223289154495683),\
						 (3.136534275158203, 3.8192692435327482e-017, -0.62373400170430693),\
						 (4, 0, -0.80000000000000004),\
						 (4, 0, -1.6000000000000001),\
						 (5.6000000000000005, 0, 0),\
						 (4, 0, 1.6000000000000001),\
						 (4, 0, 0.80000000000000004),\
						 (3.136543124735546, -3.8190233003877864e-017, 0.62369383614062934),\
						 (2.9532336400027384, -7.490263320801017e-017, 1.2232528311046151),\
						 (2.6589082661209607, -1.0879935973282562e-016, 1.7768283852711821),\
						 (2.2625737811483626, -1.3854177878362525e-016, 2.2625589497328309),\
						 (1.776844236468518, -1.6281034758848543e-016, 2.6588947556444888),\
						 (1.2232715976872581, -1.8083291678879909e-016, 2.9532256470143374),\
						 (0.62371425969669825, -1.9205771067676957e-016, 3.1365404426890713),\
						 (0.80000000000000004, 0, 4),\
						 (1.6000000000000001, 0, 4),\
						 (0, 0, 5.6000000000000005),\
						 (-1.6000000000000001, 0, 4),\
						 (-0.80000000000000004, 0, 4),\
						 (-0.62371425969669225, -1.9205771067676969e-016, 3.1365404426890731),\
						 (-1.2232715976872506, -1.8083291678879911e-016, 2.9532256470143396),\
						 (-1.7768442364685115, -1.628103475884856e-016, 2.6588947556444924),\
						 (-2.2625737811483595, -1.3854177878362547e-016, 2.2625589497328336),\
						 (-2.6589082661209544, -1.0879935973282614e-016, 1.7768283852711904),\
						 (-2.9532336400027375, -7.4902633208010762e-017, 1.223252831104622),\
						 (-3.1365431247355415, -3.819023300387824e-017, 0.623693836140637)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap38
def mz_ccButtonSnap38(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton38(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton38(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton39
def mz_ccButton39(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],\
				point = [(5.8520521406535408e-007, 0, -1.0398099422454834),\
						 (1.2360682487487793, 0, -3.8042259216308594),\
						 (3.2360701560974121, 0, -2.351142406463623),\
						 (0.69169783592224121, 0, -0.53726297616958618),\
						 (3.9999988079071045, 0, 2.2737367544323206e-013),\
						 (3.2360680103302002, 0, 2.3511412143707275),\
						 (0.42749345302581787, 0, 0.27587676048278809),\
						 (1.2360677719116211, 0, 3.8042242527008057),\
						 (-1.2360682487487793, 0, 3.8042266368865967),\
						 (-0.42749285697937012, 0, 0.27587652206420898),\
						 (-3.236067533493042, 0, 2.3511402606964111),\
						 (-4.0000009536743164, 0, 0),\
						 (-0.6916964054107666, 0, -0.53726291656494141),\
						 (-3.2360677719116211, 0, -2.3511404991149902),\
						 (-1.2360686063766479, 0, -3.8042278289794922),\
						 (5.8520521406535408e-007, 0, -1.0398099422454834)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap39
def mz_ccButtonSnap39(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton39(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton39(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton40
def mz_ccButton40(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,\
						16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],\
				point = [(0, 0, 0),\
						 (6.8580220752251786e-016, 5.6000000000000005, 0),\
						 (0.20683760000000073, 5.6279536000000006, 0),\
						 (0.39966240000000075, 5.7078255999999996, 0),\
						 (0.56568960000000068, 5.8343100000000003, 0),\
						 (0.69217500000000076, 6.0003378000000005, 0),\
						 (0.77204560000000089, 6.1931621999999997, 0),\
						 (0.80000600000000066, 6.4000000461260003, 0),\
						 (0, 6.4000000000000004, 0),\
						 (6.8580220752251786e-016, 5.6000000000000005, 0),\
						 (-0.20683759999999932, 5.6279536000000006, 0),\
						 (-0.39966239999999931, 5.7078256000000005, 0),\
						 (-0.56568959999999924, 5.8343100000000003, 0),\
						 (-0.69217499999999932, 6.0003378000000005, 0),\
						 (-0.77204559999999933, 6.1931622000000006, 0),\
						 (-0.80000599999999933, 6.4000000461260003, 0),\
						 (-0.77204559999999933, 6.6068376000000004, 0),\
						 (-0.69217499999999921, 6.7996623999999999, 0),\
						 (-0.56568959999999913, 6.965689600000001, 0),\
						 (-0.39966239999999914, 7.092175000000001, 0),\
						 (-0.20683759999999915, 7.1720456000000006, 0),\
						 (8.8174643017417381e-016, 7.200006000000001, 0),\
						 (0.20683760000000093, 7.1720456000000006, 0),\
						 (0.39966240000000092, 7.092175000000001, 0),\
						 (0.5656896000000009, 6.965689600000001, 0),\
						 (0.69217500000000098, 6.7996623999999999, 0),\
						 (0.77204560000000089, 6.6068376000000004, 0),\
						 (0.80000600000000066, 6.4000000461260003, 0),\
						 (-0.80000599999999933, 6.4000000461260003, 0),\
						 (0, 6.4000000000000004, 0),\
						 (8.8174643017417381e-016, 7.200006000000001, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap40
def mz_ccButtonSnap40(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton40(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton40(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton41
def mz_ccButton41(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6, 7, 8],\
				point = [(2, 0, 0),\
						 (-2, 0, 0),\
						 (-2, 0, 3),\
						 (2, 0, 3),\
						 (2, 0, 0),\
						 (2, 3, 0),\
						 (-2, 3, 0),\
						 (-2, 0, 0),\
						 (2, 0, 0)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap41
def mz_ccButtonSnap41(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton41(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton41(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton42
def mz_ccButton42(self):
	cmds.curve( degree = 1,\
				knot = [0, 1.565366, 3.1307580000000002, 4.6961259999999996, 6.2614869999999998,\
						7.8268849999999999, 9.3922439999999998, 15.392244, 16.957602000000001, 18.523,\
						20.088360999999999, 21.653728999999998, 23.219121000000001, 24.784486999999999,\
						30.784486999999999, 32.349851999999998, 33.915246000000003, 35.480611000000003,\
						37.045976000000003, 38.611370000000001, 40.176735000000001, 41.742100000000001,\
						43.307493999999998, 44.872858999999998, 46.438223999999998, 48.003618000000003,\
						49.568983000000003, 55.568983000000003, 57.134349, 58.699741000000003, 60.265109000000002,\
						61.830469999999998, 63.395868, 64.961225999999996,70.961225999999996, 72.526584,\
						74.091982000000002, 75.657342999999997, 77.222712000000001, 78.788104000000004,\
						80.353470000000002, 86.353470000000002, 87.918834000000004, 89.484228999999999,\
						91.049593999999999, 92.614958999999999, 94.180352999999997, 95.745717999999997,\
						101.745718, 107.745718, 109.311083, 110.87647699999999, 112.44184199999999,\
						114.00720699999999, 115.57260100000001, 117.13796600000001],\
				point = [(1.4896573996191746, 0, 9.6065034716741649e-008),\
						 (1.4375950174761141, 0, -0.38513729207426778),\
						 (1.2888660319151257, 0, -0.74419982093211945),\
						 (1.0533470440513093, 0, -1.053347540599969),\
						 (0.74420006920644932, 0, -1.2888650388178065),\
						 (0.38513704379993791, 0, -1.4375965071220931),\
						 (0, 0, -1.4896459790000023),\
						 (0, 4.4213115194744992, -1.4896459790000023),\
						 (0.38513704379993791, 4.4213115194744992, -1.4375965071220931),\
						 (0.74420006920644932, 4.4213115194744992, -1.2888650388178065),\
						 (1.0533470440513093, 4.4213115194744992, -1.053347540599969),\
						 (1.2888660319151257, 4.4213115194744992, -0.74419982093211945),\
						 (1.4375950174761141, 4.4213115194744992, -0.38513729207426778),\
						 (1.4896573996191746, 4.4213115194744992, 9.6065034716741649e-008),\
						 (1.4896573996191746, 0, 9.6065034716741649e-008),\
						 (1.4375950174761141, 0, 0.38513704379993791),\
						 (1.2888660319151257, 0, 0.74420006920644932),\
						 (1.0533470440513093, 0, 1.0533467957769795),\
						 (0.74420006920644932, 0, 1.2888660319151257),\
						 (0.38513704379993791, 0, 1.4375950174761141),\
						 (0, 0, 1.4896573996191746),\
						 (-0.38513704379993791, 0, 1.4375950174761141),\
						 (-0.74420006920644932, 0, 1.2888660319151257),\
						 (-1.0533470440513093, 0, 1.0533467957769795),\
						 (-1.2888660319151257, 0, 0.74420006920644932),\
						 (-1.4375950174761141, 0, 0.38513704379993791),\
						 (-1.4896573996191746, 0, 9.6065034716741649e-008),\
						 (-1.4896573996191746, 4.4213115194744992, 9.6065034716741649e-008),\
						 (-1.4375950174761141, 4.4213115194744992, -0.38513729207426778),\
						 (-1.2888660319151257, 4.4213115194744992, -0.74419982093211945),\
						 (-1.0533470440513093, 4.4213115194744992, -1.053347540599969),\
						 (-0.74420006920644932, 4.4213115194744992, -1.2888650388178065),\
						 (-0.38513704379993791, 4.4213115194744992, -1.4375965071220931),\
						 (0, 4.4213115194744992, -1.4896459790000023),\
						 (0, 0, -1.4896459790000023),\
						 (-0.38513704379993791, 0, -1.4375965071220931),\
						 (-0.74420006920644932, 0, -1.2888650388178065),\
						 (-1.0533470440513093, 0, -1.053347540599969),\
						 (-1.2888660319151257, 0, -0.74419982093211945),\
						 (-1.4375950174761141, 0, -0.38513729207426778),\
						 (-1.4896573996191746, 0, 9.6065034716741649e-008),\
						 (-1.4896573996191746, 4.4213115194744992, 9.6065034716741649e-008),\
						 (-1.4375950174761141, 4.4213115194744992, 0.38513704379993791),\
						 (-1.2888660319151257, 4.4213115194744992, 0.74420006920644932),\
						 (-1.0533470440513093, 4.4213115194744992, 1.0533467957769795),\
						 (-0.74420006920644932, 4.4213115194744992, 1.2888660319151257),\
						 (-0.38513704379993791, 4.4213115194744992, 1.4375950174761141),\
						 (0, 4.4213115194744992, 1.4896573996191746),\
						 (0, 0, 1.4896573996191746),\
						 (0, 4.4213115194744992, 1.4896573996191746),\
						 (0.38513704379993791, 4.4213115194744992, 1.4375950174761141),\
						 (0.74420006920644932, 4.4213115194744992, 1.2888660319151257),\
						 (1.0533470440513093, 4.4213115194744992, 1.0533467957769795),\
						 (1.2888660319151257, 4.4213115194744992, 0.74420006920644932),\
						 (1.4375950174761141, 4.4213115194744992, 0.38513704379993791),\
						 (1.4896573996191746, 4.4213115194744992, 9.6065034716741649e-008)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap42
def mz_ccButtonSnap42(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton42(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton42(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton43
def mz_ccButton43(self):
	cmds.curve( degree = 1,\
				knot = [0, 1, 2, 3, 4, 5, 6],\
				point = [(0, 0, 0),\
						 (-2.7610131682735411e-031, 5.5999999999999996, -1.2434497875801752e-015),\
						 (-0.69999999999999996, 5.5999999999999996, -1.0880185641326533e-015),\
						 (-0.69999999999999996, 7, -1.3988810110276972e-015),\
						 (0.69999999999999996, 7, -1.7097434579227411e-015),\
						 (0.69999999999999996, 5.5999999999999996, -1.3988810110276972e-015),\
						 (-2.7610131682735411e-031, 5.5999999999999996, -1.2434497875801752e-015)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap43
def mz_ccButtonSnap43(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton43(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton43(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton44
def mz_ccButton44(self):
	cmds.curve( degree = 3,\
				knot = [0, 0, 0, 0.50358628617148704, 1.4337586472378248, 2.4062686187308571,\
						3.2255926458086837, 4.3739460616280263, 5.1168801677211926, 5.8776710459855988,\
						6.9714677697371412, 7.9607070521530687, 8.9970790790600361, 10.514734166445262,\
						11.613972698532207, 13.032031958456606, 13.74211278192406, 14.839993390661135,\
						15.997404382189339, 17.561529023861784, 18.581944755283953, 19.947484800413672,\
						20.27973503321914, 20.607464644050278, 21.366292187742889, 22.185616214820719,\
						23.038832910413674, 23.902476266169479, 24.66130380986209, 25.46778209578223,\
						26.819045897881551, 28.12996434120608, 29.440882784530604, 30.756345152895225,\
						31.499279258988391, 32.647632674807731, 34, 34, 34],\
				point = [(-1, 0, -1.2246467991473532e-016),\
						 (-0.97725595851908231, 0.046683937024927957, -1.1967933815480726e-016),\
						 (-0.91891806126076725, 0.1952067070806858, -1.1253500624016901e-016),\
						 (-0.82712268213054196, 0.4902257926484429, -1.0129331451733421e-016),\
						 (-0.6776246779018229, 0.82265818907219379, -8.2985089281572358e-017),\
						 (-0.4368353550477182, 1.1224074276941929, -5.3496901931358562e-017),\
						 (-0.14267028666323212, 1.3145708945724375, -1.7472070989556253e-017),\
						 (0.16835256422958267, 1.424059132948474, 2.0617242891200764e-017),\
						 (0.46674872608731999, 1.4821551192807847, 5.7160233340894105e-017),\
						 (0.76999553557257672, 1.4996183421073668, 9.4297256799670797e-017),\
						 (1.0727184473466227, 1.4855067588023139, 1.31370121292936e-016),\
						 (1.3891567185990361, 1.4419239978156093, 1.70122632894635e-016),\
						 (1.6899190217840458, 1.3680458740853401, 2.0695539208460582e-016),\
						 (2.0157243632819988, 1.2814656063023122, 2.4685503894566367e-016),\
						 (2.2867458701253351, 1.2222122027139579, 2.8004560103124206e-016),\
						 (2.5869714380088009, 1.1940540983449761, 3.1681262910431035e-016),\
						 (2.8969514191892567, 1.2104663001282678, 3.5477422827955054e-016),\
						 (3.3660525873808878, 1.3313830632913592, 4.1222255268976705e-016),\
						 (3.8833958398476889, 1.5459478244513665, 4.7557882850916199e-016),\
						 (4.3795563420471844, 1.717355673920143, 5.363409655973575e-016),\
						 (4.6120795613907131, 1.7192344502809114, 5.6481684722700645e-016),\
						 (4.6590444909250195, 1.6126769583044658, 5.7056839228964345e-016),\
						 (4.6538106968966924, 1.5130432076767182, 5.6992743737922475e-016),\
						 (4.5680663130688703, 1.3476313590690672, 5.5942677885926432e-016),\
						 (4.3647064617885363, 1.1379388928841814, 5.3452237976471013e-016),\
						 (4.1022680274455432, 0.95043394381899793, 5.0238294090557106e-016),\
						 (3.8321517300165646, 0.7954796590540234, 4.6930323500117783e-016),\
						 (3.570899765099818, 0.66217225324061735, 4.3730909674055282e-016),\
						 (3.2656633108897593, 0.53697217664350427, 3.9992841207740915e-016),\
						 (2.9143427435438283, 0.45890644503861633, 3.5690405124992649e-016),\
						 (2.5246061915109204, 0.45147080878723589, 3.0917508915414387e-016),\
						 (2.1494064218058782, 0.47651344922911787, 2.6322636945313342e-016),\
						 (1.8358389676552627, 0.46848763042196429, 2.2482543154889987e-016),\
						 (1.5425429777208777, 0.40439026090146746, 1.8890703202130997e-016),\
						 (1.2573116330950223, 0.27788172376529213, 1.5397626670005503e-016),\
						 (1.0755938101270506, 0.11090083097847503, 1.3172225167547986e-016),\
						 (1, 0, 1.2246467991473532e-016)]\
			  )
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap44
def mz_ccButtonSnap44(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton44(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton44(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
				
		
#mz_ccButton45
def mz_ccButton45(self):
	#paw ctrl
	pawCtrl = cmds.curve( degree = 2,\
							knot = [0, 0, 0.03125, 0.0625, 0.09375, 0.125, 0.15625, 0.1875, 0.21875, 0.25, 0.28125,\
									0.3125, 0.34375, 0.375, 0.40625, 0.4375, 0.46875, 0.5, 0.53125, 0.5625, 0.59375,\
									0.625, 0.65625, 0.6875, 0.71875, 0.75, 0.78125, 0.8125, 0.84375000000000011,\
									0.875, 0.90625, 0.9375, 0.96875, 1, 1],\
							point = [(1.2760358807837899, -0.97838365661065585, 0),\
									 (0.90814202020255952, -0.69662064413776004, 0),\
									 (0.38216986052950103, -0.50348432875199789, -8.4709398363252871e-019),\
									 (-0.099495232080049498, -0.41642425866385091, -1.9052679222664819e-018),\
									 (-0.8179434195163503, -0.49339324922786321, -1.4830322280713755e-018),\
									 (-1.3119400593594779, -0.86109674853764884, 6.7274539123863291e-018),\
									 (-1.2779459679340806, -1.4713367597030014, -2.8882694283436788e-018),\
									 (-0.60334366183634358, -1.7036354285180624, -1.3373038982381737e-017),\
									 (-0.011917466409856942, -1.6990757065576552, -5.7173642517224206e-019),\
									 (0.5702844021096648, -1.4300397328167522, 2.933244909221897e-017),\
									 (1.2048356243487746, -1.7235495734005259, 7.1167824023927416e-018),\
									 (1.1089403113033698, -2.2491812442752837, -1.1097876902128557e-016),\
									 (0.38227812453539201, -2.2384939323474802, -1.6423150377622724e-016),\
									 (-0.19423914124238653, -2.1661528138748154, -1.92998001638554e-016),\
									 (-0.82373418287847866, -2.1942533359210592, -1.8536383724453082e-016),\
									 (-1.4353205624286198, -2.3094990856093935, -1.3071211359465302e-016),\
									 (-2.1478113629899105, -2.2756563786258233, -1.1845652744173071e-016),\
									 (-2.6497715163869153, -1.939371278349626, -1.2258325700549487e-016),\
									 (-2.7630913685427787, -1.3032204397322737, -1.868357371089103e-016),\
									 (-2.5054176871230989, -0.70619044669475461, -2.5830054477709535e-016),\
									 (-2.1032101903288907, -0.24862198960147786, -3.251080455544342e-016),\
									 (-1.5843686162324753, 0.12719899303009496, -3.8141342345219598e-016),\
									 (-1.0029689934902117, 0.38248169198978577, -4.2036792860554472e-016),\
									 (-0.42131578809042419, 0.52595804679784708, -4.4312605036974659e-016),\
									 (0.19849613061491012, 0.57116823817710305, -4.4842321471339974e-016),\
									 (0.81673662601764507, 0.44968606313010318, -4.3676569896025518e-016),\
									 (1.3858269320371137, 0.20758555690405656, -3.9816466614863837e-016),\
									 (1.9145110538903138, -0.1296906841666976, -3.3332295691815949e-016),\
									 (2.3439396207874093, -0.55888240118746091, -2.7860249287649361e-016),\
									 (2.64766910436926, -1.131178705669494, -2.4181129437627538e-016),\
									 (2.6176160844681737, -1.7788271973226091, -1.5947174925992623e-016),\
									 (2.2478234742110157, -2.1839312462172291, -4.8766755489312473e-017),\
									 (1.6342254918008643, -2.2134716564190371, 0),\
									 (1.3410994874315185, -2.0800197971551282, 0)]\
						  )
	#finger ctrl1
	fingerCtrl1 = cmds.curve( degree = 1,\
								knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],\
								point = [(-3.6946897904112177, 0.64218970589797353, 0),\
										 (-3.6266386065840659, 0.31799776951128589, -7.4808172158191868e-017),\
										 (-3.7687187258109178, 0.10434412909920532, -4.0450046324938557e-017),\
										 (-3.8193249476843567, -0.14718552537798812, -9.9288192708233226e-022),\
										 (-3.7687223072905844, -0.39872426540960704, 4.0449521629669752e-017),\
										 (-3.6266433687565778, -0.61236796261865112, 7.4806048473922076e-017),\
										 (-3.4129986699037471, -0.75444927863914901, 9.7654466712764472e-017),\
										 (-3.1614634005240712, -0.80505309461244723, 1.0579218097543764e-016),\
										 (-2.9099281311443979, -0.75444927863914835, 9.7654466712764361e-017),\
										 (-2.6962834322915685, -0.61236796261864868, 7.4806048473921842e-017),\
										 (-2.5542044937575641, -0.39872426540960437, 4.0449521629669382e-017),\
										 (-2.5036018533637825, -0.14718552537798768, -9.9288192736921871e-022),\
										 (-2.5542080752372387, 0.10434412909920843, -4.0450046324938643e-017),\
										 (-2.6962881944640777, 0.317997769511285, -7.4808172158191954e-017),\
										 (-2.909938261257893, 0.46005741661433097, -9.7653105769338831e-017),\
										 (-3.1614634005240738, 0.51076389001845435, -1.0580732860597924e-016),\
										 (-3.4129885397902733, 0.46005741661433097, -9.7653105769338794e-017),\
										 (-3.6946897904112177, 0.64218970589797353, 0)]\
							  )

	#finger ctrl2
	fingerCtrl2 = cmds.curve( degree = 1,\
								knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],\
								point = [(-1.2696684120546053, 2.3094990856093935, 7.5738152707983916e-021),\
										 (-1.355103987599422, 1.9894488744397196, -7.4800598342921068e-017),\
										 (-1.578256781857672, 1.8628097463805529, -4.0442472509667758e-017),\
										 (-1.7368401785606933, 1.661118241691208, 6.580933343716059e-021),\
										 (-1.8050909656161429, 1.4137840648821234, 4.0457095444940552e-017),\
										 (-1.7746054270660094, 1.1590279342956187, 7.4813622289192876e-017),\
										 (-1.6479748196654769, 0.93587810351054879, 9.7662040528035272e-017),\
										 (-1.4462772184349491, 0.7772943225276987, 1.0579975479070844e-016),\
										 (-1.1989456093872457, 0.70904614966689339, 9.7662040528035161e-017),\
										 (-0.94418751275990209, 0.73953335867077241, 7.4813622289192641e-017),\
										 (-0.72104025570078079, 0.86616414402366182, 4.0457095444940182e-017),\
										 (-0.56245595911385748, 1.0678653731412511, 6.5809333434291729e-021),\
										 (-0.49421246543532582, 1.3151930552641216, -4.0442472509667844e-017),\
										 (-0.52469457450496215, 1.5699585932937237, -7.4800598342921155e-017),\
										 (-0.65133974361129943, 1.7930915032780432, -9.7645531954068031e-017),\
										 (-0.85298201522037476, 1.9517623463094167, -1.0579975479070844e-016),\
										 (-1.1003508700761979, 2.0199143218881388, -9.7645531954067994e-017),\
										 (-1.2696684120546053, 2.3094990856093935, 7.5738152707983916e-021)]\
							  )
	#finger ctrl3
	fingerCtrl3 = cmds.curve( degree = 1,\
								knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],\
								point = [(1.2696684120546067, 2.3094990856093927, 4.5247657638222111e-016),\
										 (1.3551039875994233, 1.9894488744397187, 3.6933453777881835e-016),\
										 (1.5782567818576738, 1.8628097463805529, 4.2109245993543549e-016),\
										 (1.7368401785606951, 1.6611182416912076, 4.6773898814187173e-016),\
										 (1.8050909656161447, 1.4137840648821229, 5.0199246649480479e-016),\
										 (1.7746054270660108, 1.1590279342956182, 5.1894934160886466e-016),\
										 (1.6479748196654787, 0.93587810351054834, 5.1563383018721509e-016),\
										 (1.4462772184349508, 0.77729432252769826, 4.9296735819803953e-016),\
										 (1.198945609387247, 0.70904614966689294, 4.5402545768351787e-016),\
										 (0.94418751275990298, 0.73953335867077197, 4.0501310978418361e-016),\
										 (0.72104025570078212, 0.86616414402366138, 3.5325693120973891e-016),\
										 (0.56245595911385882, 1.0678653731412506, 3.0660938053947725e-016),\
										 (0.49421246543532715, 1.3151930552641211, 2.7235780185989287e-016),\
										 (0.52469457450496348, 1.5699585932937232, 2.5539947235000181e-016),\
										 (0.65133974361130076, 1.7930915032780423, 2.5871912578252132e-016),\
										 (0.85298201522037609, 1.9517623463094158, 2.8136784861662301e-016),\
										 (1.1003508700761993, 2.0199143218881388, 3.2032501712400782e-016),\
										 (1.2696684120546067, 2.3094990856093927, 4.5247657638222111e-016)]\
							  )
	#finger ctrl4
	fingerCtrl4 = cmds.curve( degree = 1,\
								knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],\
								point = [(3.6946897904112177, 0.64218970589797353, 4.5246900256695025e-016),\
										 (3.6266386065840659, 0.31799776951128589, 3.6932696396354754e-016),\
										 (3.7687187258109178, 0.10434412909920532, 4.2108488612016468e-016),\
										 (3.8193249476843567, -0.14718552537798812, 4.6773141432660087e-016),\
										 (3.7687223072905844, -0.39872426540960704, 5.0198489267953393e-016),\
										 (3.6266433687565778, -0.61236796261865112, 5.189417677935938e-016),\
										 (3.4129986699037471, -0.75444927863914901, 5.1562625637194423e-016),\
										 (3.1614634005240712, -0.80505309461244723, 4.9295978438276867e-016),\
										 (2.9099281311443979, -0.75444927863914835, 4.5401788386824701e-016),\
										 (2.6962834322915685, -0.61236796261864868, 4.050055359689128e-016),\
										 (2.5542044937575641, -0.39872426540960437, 3.532493573944681e-016),\
										 (2.5036018533637825, -0.14718552537798768, 3.0660180672420644e-016),\
										 (2.5542080752372387, 0.10434412909920843, 2.7235022804462206e-016),\
										 (2.6962881944640777, 0.317997769511285, 2.55391898534731e-016),\
										 (2.909938261257893, 0.46005741661433097, 2.5871155196725051e-016),\
										 (3.1614634005240738, 0.51076389001845435, 2.813602748013522e-016),\
										 (3.4129885397902733, 0.46005741661433097, 3.2031744330873701e-016),\
										 (3.6946897904112177, 0.64218970589797353, 4.5246900256695025e-016)]\
							  )
	#parent the fingers underneath the paw ctrl
	cmds.parent(fingerCtrl1, pawCtrl)
	cmds.parent(fingerCtrl2, pawCtrl)
	cmds.parent(fingerCtrl3, pawCtrl)
	cmds.parent(fingerCtrl4, pawCtrl)
	cmds.select(pawCtrl, replace = 1)
	#make group(s)
	for i in xrange(mz_groups()):
		cmds.group()
		cmds.xform(pivots = (0, 0, 0))
		   
#mz_ccButtonSnap45
def mz_ccButtonSnap45(self):
	#the selected object(s)
	selObj = cmds.ls(selection = 1)
	
	#if no object is selected, create the ctrl at the center of the scene
	if len(selObj) == 0:
		mz_ccButton45(self)
		cmds.select(clear = 1)    
	#else, put the ctrl at the centre of the object(s)       
	else:
		mz_ccButton45(self)
		selCtrl = cmds.ls(selection = 1)
		pConst = cmds.parentConstraint(selObj, selCtrl[0])
		cmds.delete(pConst)
		cmds.select(clear = 1)
		
		
#run the script        
mz_ctrlCreator()