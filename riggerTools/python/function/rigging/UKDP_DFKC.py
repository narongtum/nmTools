# -*- coding: utf-8 -*-
'''
Create dynamic joint chains
from an existing joint chain
and add FK controls offsets.
'''
MadeBy = "UKDP"
Contact = "ukdp.scripts@gmail.com"
ScriptName = "Dynamics FK Chains" # DFKC
Version = "1.0"
''''''

from maya import cmds
from maya import mel



class RigFunctions:
	'''
	Functions and options to build the rig.
	The three first def are used to update UI
	depending on user's actions.
	'''
	
	def hairSystInScene (self, *args):
		'''
		List the existing hairSystems in the scene
		and add them to the optionMenu in the UI.
		
		Called by function(s): Main.UI
		Call function(s): -
		Return: -
		'''
		existingItems = cmds.optionMenu ("opMenuHairSys", q = 1, ils = 1)
		for item in existingItems:
			if item == "menuItemNewHairSyst":
				pass
			else:
				cmds.deleteUI (item)
		allHairSyst = cmds.ls (typ = "hairSystem")
		for hairSyst in allHairSyst:
			cmds.menuItem (p = "opMenuHairSys", l = str(hairSyst))
	
	
	def setFirstJnt (self):
		'''
		Set the selected object as the "first joint"
		for the rig to be created.
		
		Called by function(s): Main.UI
		Call function(s): -
		Return: -
		'''
		rawSelection = cmds.ls (sl = 1)
		if len(rawSelection) == 0:
			cmds.textFieldButtonGrp ("btnFirstJnt", e = 1, tx = "")
			cmds.error ("Please select the first joint of the chain.")
		else:
			firstJnt = cmds.ls (sl = 1, typ = "joint")
			if len(firstJnt) == 0:
				cmds.error ("You have to select the first joint of the chain.")
			else:
				cmds.textFieldButtonGrp ("btnFirstJnt", e = 1, tx = firstJnt[0])
	
	
	def setLastJnt (self):
		'''
		Set the selected object as the "last joint"
		for the rig to be created.
		
		Called by function(s): Main.UI
		Call function(s): -
		Return: -
		'''
		rawSelection = cmds.ls (sl = 1)
		if len(rawSelection) == 0:
			cmds.textFieldButtonGrp ("btnLastJnt", e = 1, tx = "")
			cmds.error ("Please select the last joint of the chain.")
		else:
			lastJnt = cmds.ls (sl = 1, typ = "joint")
			if len(lastJnt) == 0:
				cmds.error ("You have to select the last joint of the chain.")
			else:
				cmds.textFieldButtonGrp ("btnLastJnt", e = 1, tx = lastJnt[0])
	
	
	def defineJntChain (self, firstJnt, lastJnt):
		'''
		List the joints between the first selected joint
		and the last selected joint as the "joint chain"
		we will use to build the rig.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: jntChain (joints names in the joint chain)
		'''
		cmds.select (cl = 1)
		cmds.select (firstJnt, hi = 1)
		jntChain = cmds.ls (sl = 1)
		lastJntIndx = jntChain.index(lastJnt)
		del jntChain [(lastJntIndx + 1):]
		return jntChain
	
	
	def createCrv (self, jntChain, prefix):
		'''
		Create a cubic curve with one point
		for each joint in the joint chain.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: jntsPositions (joints positions)
				baseCrv (name of the curve)
		'''
		jntsPositions = []
		for jnt in jntChain:
			jntPos = cmds.xform (jnt, q = 1, ws = 1, t = 1)
			jntsPositions.append (jntPos)
		rawCrv = cmds.curve (d = 3, ep = jntsPositions)
		baseCrv = cmds.rename (rawCrv, prefix + "DYN_baseCurve")
		return jntsPositions, baseCrv
	
	
	def createFkJntChain (self, firstJnt, nbrOfCtrl, origCrv, prefix):
		'''
		It duplicates the base curve et rebuild it
		with the corresponding number of points,
		each position of this points will be the position
		of a FK joint. Number of points is defined by the user.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: fkJntChain (list of the joints in the fk chain)
		'''
		x = 0
		fkJntChain = []
		radius = cmds.joint (firstJnt, q = 1, rad = 1) [0]
		crv = cmds.duplicate (origCrv, rr = 1)
		cmds.rebuildCurve (crv, rpo = 1, rt = 0, end = 1, kr = 0, kcp = 0, kep = 1, kt = 1, s = 20, d = 3, tol = 0)
		for x in range (x, nbrOfCtrl + 1, x + 1):
			incr = (1.0/nbrOfCtrl) * x
			ptOnCrvPos = cmds.pointOnCurve (crv, pr = incr)
			rawFkJnt = cmds.joint (rad = radius*0.75)
			fkJnt = cmds.rename (rawFkJnt, prefix + "FK_JNT%d" % (x + 1))
			fkJntChain.append (fkJnt)
			cmds.xform (ws = 1, t = ptOnCrvPos)
		cmds.delete (crv)
		# Orient FK joint chain
		cmds.joint (fkJntChain[0], e = 1, oj = "xyz", secondaryAxisOrient = "zup", ch = 1, zso = 1)
		cmds.setAttr (fkJntChain[-1] + ".jointOrientX", 0)
		cmds.setAttr (fkJntChain[-1] + ".jointOrientY", 0)
		cmds.setAttr (fkJntChain[-1] + ".jointOrientZ", 0)
		return fkJntChain
	
	
	def organizeDynItems (self, dynItemsRaw, selectedHairSystem, prefix):
		'''
		Rename the newly created dynamics elements
		and sort them in a "clean" list.
		If an already-created hairSystem is selected,
		rename only the newly created elements.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: dynItems (list of the main dynamics items)
		'''
		dynItems = []
		if selectedHairSystem == "":
			# dynItemsRaw = [hairSystemShape#, time#, nucleus#, follicleShape#, [baseCrv]rebuiltCurveShape#, rebuildCurve#, [baseCrv]Shape#', [baseCrv]]
			# Index =       [        0       ,   1   ,   2    ,        3      ,              4             ,        5     ,         6       ,      7   ]
			rawHairSyst = cmds.pickWalk (dynItemsRaw[0], d = "up")
			hairSyst = cmds.rename (rawHairSyst, prefix + "DYN_hairSystem")
			rawNucleus = cmds.pickWalk (dynItemsRaw[2], d = "up")
			nucleus = cmds.rename (rawNucleus, prefix + "DYN_nucleus")
			rawDynCrv = cmds.listConnections (dynItemsRaw[3] + ".outCurve")
			dynCrv = cmds.rename (rawDynCrv, prefix + "DYN_dynamicCurve")
			rawHairSystCrvsGrp = cmds.pickWalk (dynCrv, d = "up")
			hairSystCrvsGrp = cmds.rename (rawHairSystCrvsGrp, prefix + "DYN_hairSystem_OutputCurves")
			rawFollicle = cmds.pickWalk (dynItemsRaw[3], d = "up")
			follicle = cmds.rename (rawFollicle, prefix + "DYN_follicle")
			rawHairSystFolliclesGrp = cmds.pickWalk (follicle, d = "up")
			hairSystFolliclesGrp = cmds.rename (rawHairSystFolliclesGrp, prefix + "DYN_hairSystem_Follicles")
			dynItems.append (hairSyst)
			dynItems.append (nucleus)
			dynItems.append (hairSystFolliclesGrp)
			dynItems.append (follicle)
			dynItems.append (hairSystCrvsGrp)
			dynItems.append (dynCrv)
		else :
			folliclesInScene = cmds.ls (type = "follicle")
			rawFollicle = cmds.pickWalk (folliclesInScene[-1], d = "up")
			rawDynCrv = cmds.listConnections (folliclesInScene[-1] + ".outCurve")
			hairSyst = cmds.listConnections (folliclesInScene[-1] + ".outHair")
			follicle = cmds.rename (rawFollicle, prefix + "DYN_follicle")
			dynCrv = cmds.rename (rawDynCrv, prefix + "DYN_dynamicCurve")
			hairSystShape = cmds.pickWalk (hairSyst, d = "down")
			nucleus = cmds.listConnections(hairSystShape) [1]
			rawHairSystFolliclesGrp = cmds.pickWalk (follicle, d = "up")
			hairSystFolliclesGrp = cmds.rename (rawHairSystFolliclesGrp, prefix + "DYN_hairSystem_Follicles")
			rawHairSystCrvsGrp = cmds.pickWalk (dynCrv, d = "up")
			hairSystCrvsGrp = cmds.rename (rawHairSystCrvsGrp, prefix + "DYN_hairSystem_OutputCurves")
			dynItems.append (hairSyst)
			dynItems.append (nucleus)
			dynItems.append (hairSystFolliclesGrp)
			dynItems.append (follicle)
			dynItems.append (hairSystCrvsGrp)
			dynItems.append (dynCrv)
		return dynItems # [hairSystem, nucleus, hairSystem_folliclesGrp, follicle, hairSystem_curvesGrp, dynamicCurve]
	
	
	def setDynParameters (self, dynItemsList, selectedHairSystem):
		'''
		If there is no hairSystem selected by user,
		modify the attributes values of the hairSystem.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: -
		'''
		cmds.setAttr (dynItemsList[3] + "Shape.pointLock", 1) # Follicle - Point Lock : Base
		if selectedHairSystem == "":
			hairSystRaw = dynItemsList[0]
			hairSyst = cmds.pickWalk (hairSystRaw, d = "down") [0]
			cmds.setAttr (hairSyst + ".startCurveAttract", 0.35)
			cmds.setAttr (hairSyst + ".damp", 2)
			cmds.setAttr (hairSyst + ".attractionScale[0].attractionScale_FloatValue", 0.6)
			cmds.setAttr (hairSyst + ".attractionScale[1].attractionScale_FloatValue", 0.16)
	
	
	def createIkSystem (self, dynItemsList, jntChain, prefix):
		'''
		Create the IK spline using the dynamic curve.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: dynIkSpline (name of the ik handle)
		'''
		dynCrv = dynItemsList[-1]
		dynIkSplineRaw = cmds.ikHandle (sol = "ikSplineSolver", ccv = 0, pcv = 0, sj = jntChain[0], ee = jntChain[-1], c = dynCrv)
		dynIkSpline = cmds.rename (dynIkSplineRaw[0], prefix + "DYN_ikHandle")
		cmds.setAttr (dynIkSpline + ".visibility", 0)
		return dynIkSpline
	
	
	def createControls (self, nbrOfCtrl, prefix):
		'''
		Create the FK controls corresponding
		to the number of joints in the FK joint chain.
		Shapes are defined by user.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: ctrlAndOrigList (list containing all the orig then
								the control name for each FK control)
		'''
		selectedShape = cmds.radioButtonGrp ("radBtnGrpCtrlShape", q = 1, sl = 1)
		ctrlAndOrigList = []
		x = 1
		for ctrl in range (nbrOfCtrl):
			if selectedShape == 1:
				ctrl = cmds.circle (ch = 1, o = 1, nr = (1, 0, 0), r = 2.5)
				ctrlName = cmds.rename (ctrl[0], prefix + "FK_CTRL_%d" % x)
				ctrlOrig = cmds.group (ctrlName, n = prefix + "FK_CTRL_ORIG_%d" % x)
				ctrlAndOrigList.append (ctrlOrig)
				ctrlAndOrigList.append (ctrlName)
			elif selectedShape == 2:
				ctrl = cmds.curve (d = 1, p = [(0, 2.5, -2.5), (0, -2.5, -2.5), (0, -2.5, 2.5), (0, 2.5, 2.5), (0, 2.5, -2.5)], k = (0, 1, 2, 3, 4))
				ctrlName = cmds.rename (ctrl, prefix + "FK_CTRL_%d" % x)
				ctrlOrig = cmds.group (ctrlName, n = prefix + "FK_CTRL_ORIG_%d" % x)
				ctrlAndOrigList.append (ctrlOrig)
				ctrlAndOrigList.append (ctrlName)
			elif selectedShape == 3:
				ctrl = cmds.curve (d = 1, p = [(0, 3, 0), (0, 0, -3), (0, -3, 0), (0, 0, 3), (0, 3, 0)], k = (0, 1, 2, 3, 4))
				ctrlName = cmds.rename (ctrl, prefix + "FK_CTRL_%d" % x)
				ctrlOrig = cmds.group (ctrlName, n = prefix + "FK_CTRL_ORIG_%d" % x)
				ctrlAndOrigList.append (ctrlOrig)
				ctrlAndOrigList.append (ctrlName)
			x = x + 1
		return ctrlAndOrigList
	
	
	def placeFkControls (self, allCtrlsList, fkJntChain, baseCrv, prefix):
		'''
		Place the FK controls in the scene at 
		the position of each FK joint.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: ctrlList[0] (the first control of the FK controls chain)
		'''
		ctrlList = allCtrlsList[1::2]
		origList = allCtrlsList[::2]
		for orig, ctrl, jnt in zip(origList, ctrlList, fkJntChain): # zip() = loop over multiple lists
			tmpConstraint = cmds.parentConstraint (jnt, orig, mo = 0, w = 1)
			cmds.delete (tmpConstraint)
			cmds.parentConstraint (ctrl, jnt, mo = 0, w = 1)
		# Parent the 'orig' to the previous control to create the FK hierarchy
		tmpCtrlList = ctrlList[:-1]
		tmpOrigList = origList[1:]
		for ctrl, orig in zip(tmpCtrlList, tmpOrigList):
			cmds.parent (orig, ctrl)
		cmds.select (fkJntChain[:-1], baseCrv, r = 1)
		cmds.skinCluster (n = prefix + "DYN_Fk_skinCluster", tsb = 1, bm = 0, sm = 0, nw = 1, wd = 0, mi = 5, omi = 1, dr = 4, rui = 1)
		return ctrlList[0] # First FK control of the chain
	
	
	def dynamicsAttributes (self, firstFkCtrl, dynItemsList, selectedHairSystem):
		'''
		If there's no selected hairSystem,
		create attributes to control the
		dynamics parameters, on the
		first FK control of the chain.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: -
		'''
		if selectedHairSystem == "":
			hairSystRaw = dynItemsList[0]
			hairSyst = cmds.pickWalk (hairSystRaw, d = "down") [0]
			startCrvAttract = cmds.checkBoxGrp ("cbGrpDynAttrRow1", q = 1, v1 = 1)
			motionDrag = cmds.checkBoxGrp ("cbGrpDynAttrRow1", q = 1, v2 = 1)
			drag = cmds.checkBoxGrp ("cbGrpDynAttrRow1", q = 1, v3 = 1)
			attrDamp = cmds.checkBoxGrp ("cbGrpDynAttrRow2", q = 1, v1 = 1)
			damp = cmds.checkBoxGrp ("cbGrpDynAttrRow2", q = 1, v2 = 1)
			mass = cmds.checkBoxGrp ("cbGrpDynAttrRow2", q = 1, v3 = 1)
			noStretch = cmds.checkBoxGrp ("cbGrpDynAttrRow2", q = 1, v4 = 1)
			default = startCrvAttract + motionDrag + drag + attrDamp + damp + mass + noStretch
			if default == 0:
				cmds.warning ("As there's no dynamics parameters selected, all will be be added by default.")
			if (startCrvAttract == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "StartCurveAttract", at = "float", min = 0, max = 1, dv = 0.35, keyable = 1, hnv = 1, hxv = 1)
				cmds.connectAttr (firstFkCtrl + ".StartCurveAttract", hairSyst + ".startCurveAttract", f = 1)
			if (motionDrag == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "MotionDrag", at = "float", min = 0, max = 1, dv = 0, keyable = 1, hnv = 1, hxv = 1)
				cmds.connectAttr (firstFkCtrl + ".MotionDrag", hairSyst + ".motionDrag", f = 1)
			if (drag == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "Drag", at = "float", min = 0, max = 1, dv = 0.05, keyable = 1, hnv = 1, hxv = 1)
				cmds.connectAttr (firstFkCtrl + ".Drag", hairSyst + ".drag", f = 1)
			if (attrDamp == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "AttractionDamp", at = "float", min = 0, max = 1, dv = 0, keyable = 1, hnv = 1, hxv = 1)
				cmds.connectAttr (firstFkCtrl + ".AttractionDamp", hairSyst + ".attractionDamp", f = 1)
			if (damp == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "Damp", at = "float", min = 0, max = 10, dv = 2, keyable = 1, hnv = 1, hxv = 1)
				cmds.connectAttr (firstFkCtrl + ".Damp", hairSyst + ".damp", f = 1)
			if (mass == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "Mass", at = "float", min = 0, max = 10, dv = 1, keyable = 1, hnv = 1, hxv = 1)
				cmds.connectAttr (firstFkCtrl + ".Mass", hairSyst + ".mass", f = 1)
			if (noStretch == 1) or (default == 0) :
				cmds.select (firstFkCtrl, r = 1)
				cmds.addAttr (ln = "NoStretch", at = "bool", keyable = 1)
				cmds.connectAttr (firstFkCtrl + ".NoStretch", hairSyst + ".noStretch", f = 1)
		else:
			cmds.warning ("No attributes will be created since the hairSystem is already connected to another control.")
	
	
	def clearSceneAndScript (self, dynItemsList, dynIkSpline, prefix):
		'''
		Group the objects, delete unused nodes,
		clear the script UI, etc.
		
		Called by function(s): Rig.buildRig
		Call function(s): -
		Return: -
		'''
		allGrp = cmds.group (n = prefix + "DYN_ALL_GRP", em = 1)
		cmds.parent (dynItemsList[0], allGrp)
		cmds.parent (dynItemsList[1], allGrp)
		cmds.parent (dynItemsList[2], allGrp)
		cmds.parent (dynItemsList[4], allGrp)
		cmds.parent (dynIkSpline, allGrp)
		cmds.setAttr (allGrp + ".visibility", 0)



class Rig:
	'''
	Build the final rig
	'''
	
	def __init__ (self):
		self.pre = RigFunctions()
	
	
	def buildRig(self, *args):
		# Query UI infos
		firstJnt = cmds.textFieldButtonGrp ("btnFirstJnt", q = 1, tx = 1)
		lastJnt = cmds.textFieldButtonGrp ("btnLastJnt", q = 1, tx = 1)
		if (firstJnt == "") or (lastJnt == ""):
			cmds.error ("Please define the first and last joint of your joint chain.")
		if cmds.objExists (firstJnt) == 0:
			cmds.error ("The object you defined as the first joint does not exists. Please select the first joint of the chain.")
		if cmds.objExists (lastJnt) == 0:
			cmds.error ("The object you defined as the last joint does not exists. Please select the last joint of the chain.")
		if cmds.objectType (firstJnt, isType = "joint") == 0:
			cmds.error ("the object you defined as the 'first joint' in not a joint. Please select the first joint of the chain.")
		if cmds.objectType (lastJnt, isType = "joint") == 0:
			cmds.error ("the object you defined as the 'last joint' in not a joint. Please select the last joint of the chain.")
		
		prefix = cmds.textFieldGrp ("txtFGrpName", q = 1, tx = 1)
		if prefix != "":
			prefix = prefix + "_"
		
		selectedHairSystem = cmds.optionMenu ("opMenuHairSys", q = 1, v = 1)
		
		# Define joint chain
		jntChain = self.pre.defineJntChain (firstJnt, lastJnt)
		
		# Create the curve
		jntsPositions, baseCrv = self.pre.createCrv (jntChain, prefix)
		
		# Check number of FK controls
		nbrOfCtrl = cmds.intFieldGrp ("intFGrpFkCtrl", q = 1, v1 = 1)
		if nbrOfCtrl == 0:
			cmds.error ("You have to create at least one FK control.")
		elif nbrOfCtrl > len(jntChain):
			cmds.error ("The number of FK controls can't be superior to the number of joints in the chain.")
		else:
			# Create the FK joint chain
			fkJntChain = self.pre.createFkJntChain (firstJnt, nbrOfCtrl, baseCrv, prefix)
		
		# Create the dynamics system
		cmds.select (baseCrv, r = 1)
		if selectedHairSystem != "":
			cmds.select (selectedHairSystem, tgl = 1)
		mel.eval ('makeCurvesDynamic 2 { "0", "0", "1", "1", "0"};')
		## After executing this command,
		## the newly created hairSystemShape
		## is selected by default.
		dynItemsRaw = cmds.listHistory ()
		# Rename/organize newly created (dynamics) elements
		dynItemsList = self.pre.organizeDynItems (dynItemsRaw, selectedHairSystem, prefix)
		# Set dynamics parameters
		self.pre.setDynParameters (dynItemsList, selectedHairSystem)
		
		# Create the Ik spline
		dynIkSpline = self.pre.createIkSystem (dynItemsList, jntChain, prefix)
		
		# Create the controls
		ctrlOrigList = self.pre.createControls(nbrOfCtrl, prefix)
		
		# Place the FK controls
		firstFkCtrl = self.pre.placeFkControls (ctrlOrigList, fkJntChain, baseCrv, prefix)
		
		# Add dynamics attributes
		if cmds.checkBox ("cbDynParam", q = 1, v = 1) == 1:
			self.pre.dynamicsAttributes(firstFkCtrl, dynItemsList, selectedHairSystem)
		
		# Ending & clear scene
		self.pre.clearSceneAndScript (dynItemsList, dynIkSpline, prefix)
		cmds.select (cl = 1)
		cmds.inViewMessage(amg = "<hl>The dynamic joint chain has been successfully set-up.</hl> -UKDP", pos = "midCenterTop", fade = True)
		print "The dynamic joint chain has been successfully set-up."



class Main:
	'''
	Creates the script UI
	'''
	
	def __init__ (self):
		# Variables
		self.winWidth = 300
		# Classes
		self.pre = RigFunctions()
		self.rig = Rig()
	
	
	def updateUI (self, checkBoxBool):
		'''
		Update the script UI depending on
		user interactions with the base UI.
		
		Called by function(s): UI (self)
		Call function(s): -
		Return: -
		'''
		if checkBoxBool == 1:
			cmds.columnLayout ("dynParamLayout", parent = "dynParamLayoutVoid")
			cmds.separator (h = 15, st = "in", w = self.winWidth)
			cmds.text (h = 20, w = self.winWidth, al = "left", l = "Dynamics parameters:")
			cmds.checkBoxGrp ("cbGrpDynAttrRow1", ncb = 3, va3 = [1, 1, 1], l1 = "Start Curve Attract", l2 = "Motion Drag", l3 = "Drag", cw3 = [(self.winWidth/3)+25, (self.winWidth/3)-12, (self.winWidth/3)-14])
			cmds.checkBoxGrp ("cbGrpDynAttrRow2", ncb = 4, va4 = [1, 1, 1, 1], l1 = "Attraction Damp", l2 = "Damp", l3 = "Mass", l4 = "No Stretch", cw4 = [(self.winWidth/4)+30, (self.winWidth/4)-15, (self.winWidth/4)-15, (self.winWidth/4)-5])
			cmds.setParent ("..")
		else:
			cmds.deleteUI ("dynParamLayout", layout = 1)
	
	
	def UI (self):
		'''
		Create the base UI of the script
		
		Called by function(s): -
		Call function(s): RigFunctions.setFirstJnt
						  RigFunctions.setLastJnt
						  RigFunctions.hairSystInScene
		Return: -
		'''
		if cmds.window ("UKDP_DFKC_MAIN_WIN", exists = 1):
			cmds.deleteUI ("UKDP_DFKC_MAIN_WIN", window = 1)
		
		cmds.window ("UKDP_DFKC_MAIN_WIN", title = (MadeBy + " - " + ScriptName), s = 0, mxb = 0)
		
		cmds.columnLayout ("mainLayout", w = (self.winWidth + 10), co = ("both", 5))
		
		cmds.text (l = "Create a dynamic joint chain with FK controls offsets.", w = self.winWidth, h = 20)
		cmds.textFieldGrp ("txtFGrpName", cw = [(1, 100), (2, 150)], w = self.winWidth, l = "Name:", pht = "Object name", ann = '''The name of the object corresponding to the joint chain, for example: tail, leaf, hairLock...
You can leave it blank.''')
		
		cmds.separator (h = 15, st = "in", w = self.winWidth)
		cmds.text (h = 35, w = self.winWidth, al = "left", ww = 1, l = "Select the first joint of the joint chain you want to be dynamic, then click 'Set'. Do the same for the last joint.")
		cmds.textFieldButtonGrp ("btnFirstJnt", cw = [(1, 55), (2, 195), (3, 50)], l = "First joint: ", bl = "Set", bc = self.pre.setFirstJnt)
		cmds.textFieldButtonGrp ("btnLastJnt", cw = [(1, 55), (2, 195), (3, 50)], l = "Last joint: ", bl = "Set", bc = self.pre.setLastJnt)
		
		cmds.separator (h = 15, st = "in", w = self.winWidth)
		cmds.intFieldGrp ("intFGrpFkCtrl", cw = [(1, 112), (2, 180)], w = self.winWidth, v1 = 3, l = "Number of FK controls:", ann = "Can't be superior to the number of joints in the chain.")
		cmds.text (h = 5, l = "") # Spacing
		cmds.text (h = 20, l = "Controllers' shapes:")
		cmds.radioButtonGrp ("radBtnGrpCtrlShape", numberOfRadioButtons = 3, labelArray3 = ["Circle", "Square", "Diamond"], sl = 2)
		
		cmds.separator (h = 15, st = "in", w = self.winWidth)
		cmds.text (h = 20, l = "Assign to an existing hairSystem:")
		cmds.rowLayout (w = self.winWidth, nc = 2)
		cmds.optionMenu ("opMenuHairSys", w = (self.winWidth/1.5))
		cmds.menuItem ("menuItemNewHairSyst", l = "")
		cmds.button ("btnRefresh", l = "Refresh", c = self.pre.hairSystInScene)
		cmds.setParent ("..")
		cmds.checkBox ("cbDynParam", h = 25, v = 1, w = self.winWidth, l = "Add dynamics parameters to the first FK controller", ann = "If checked, add controls attributes to the first FK controller to ease access to the dynamics parameters.", cc = self.updateUI)
		
		cmds.columnLayout ("dynParamLayoutVoid") # Updating layout
		cmds.columnLayout ("dynParamLayout")
		cmds.separator (h = 15, st = "in", w = self.winWidth)
		cmds.text (h = 20, w = self.winWidth, al = "left", l = "Dynamics parameters:")
		cmds.checkBoxGrp ("cbGrpDynAttrRow1", ncb = 3, va3 = [1, 1, 1], l1 = "Start Curve Attract", l2 = "Motion Drag", l3 = "Drag", cw3 = [(self.winWidth/3)+25, (self.winWidth/3)-12, (self.winWidth/3)-14])
		cmds.checkBoxGrp ("cbGrpDynAttrRow2", ncb = 4, va4 = [1, 1, 1, 1], l1 = "Attraction Damp", l2 = "Damp", l3 = "Mass", l4 = "No Stretch", cw4 = [(self.winWidth/4)+30, (self.winWidth/4)-15, (self.winWidth/4)-15, (self.winWidth/4)-5])
		cmds.setParent ("..")
		cmds.setParent ("..") # Updating layout -end
		
		cmds.separator (h = 15, st = "in", w = self.winWidth)
		cmds.button ("btnBuildRig", w = self.winWidth, h = 60, l = "BUILD RIG", c = self.rig.buildRig)
		
		cmds.separator (h = 15, st = "in", w = self.winWidth)
		# Script infos
		cmds.text (en = 0, w = self.winWidth, h = 20, l = MadeBy + " (" + Contact + ") - " + ScriptName + " " + Version)
		
		cmds.setParent ("..")
		cmds.showWindow ("UKDP_DFKC_MAIN_WIN")



# Launch script
dynFkChains = Main ()
dynFkChains.UI ()