# -*- coding: utf-8 -*-
"""
Date: 23.01.Jan.31.Tue.08_

#... change from 1 to 0 for use simulation method to 'Off' instead 'Static' (static make join alway jiggle whan translate controller)

This function is Mod from 

MadeBy = "UKDP"
Contact = "ukdp.scripts@gmail.com"
ScriptName = "Dynamics FK Chains" # DFKC
Version = "1.0"

"""


'''
Create dynamic joint chains
from an existing joint chain
and add FK controls offsets.
'''


"""
try not make function try to test it test
make sure it no bug
"""



"""
from function.rigging.autoRig.addRig import creatingDynamicIkSpineRig as dySpine
reload(dySpine)

"""





'''
using TabNine
'''

'''
destination :
rigging.autoRig.addRig
'''
from function.framework.reloadWrapper import reloadWrapper as reload

from maya import cmds as mc
import pymel.core as pm
import maya.mel as mel

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc as misc
reload(misc)

from function.pipeline import logger 
reload(logger)


class DynLogger(logger.MayaLogger):
	LOGGER_NAME = "dynLogger"



def createDynamicTail(

		# arg
		side = 'LFT',
		baseName = 'breast',
		firstJnt = 'breast01LFT_bJnt' ,
		lastJnt = 'breast02LFT_bJnt'  ,		
		selectedHairSystem = ''			, #... if the HairSystem is already exists name here?
		stick = ''						, #... can blank if no HairSystem
		charScale = 1					,
		nameSpace = ''					,
		curlCtrl = False				,
		nbrOfCtrl = None				,
		parentTo = 'ctrl_grp'  			,
		priorJnt = 'hip_bJnt'			,
		ctrlShape ='cube_ctrlShape'		,
		meta = False):

	# # # # # # # # # # # # # # # #
	# in case using exists hair system
	# # # # # # # # # # # # # # # # 

	if selectedHairSystem:
		if not stick:
			mc.error('Please assign stick name.')
			

		else:
			selectedHairSystemShape = misc.shapeName(selectedHairSystem)
			#selectedHairSystem = selectedHairSystem + 'Shape'
			stick_ctrl = core.Dag( stick )


	if mc.objExists(firstJnt) and mc.objExists(lastJnt):
		pass
	else:
		raise RuntimeError('No joint attached found.')

	# make spIkJnt Chain
	spIkJnt = mc.duplicate (firstJnt, rr = 1)
	mc.select (spIkJnt, hi = 1)

	lastName = misc.findLastName(firstJnt)
	misc.searchReplace( searchText = lastName, replaceText='spIkJnt' )
	spIkJnt = misc.searchReplace( searchText='spIkJnt1', replaceText='spIkJnt' )
	pm.select( clear=True )





	# define joint chain
	mc.select (cl = 1)
	mc.select (firstJnt, hi = 1)
	jntChain = mc.ls (sl = 1)
	lastJntIndx = jntChain.index(lastJnt)
	#del jntChain [(lastJntIndx + 1):]



	# create curve prepare for ik skine rig
	jntsPositions = []
	for jnt in jntChain:
		jntPos = mc.xform (jnt, q = 1, ws = 1, t = 1)
		jntsPositions.append (jntPos)
	rawCrv = mc.curve (d = 3, ep = jntsPositions)
	baseCrv = mc.rename (rawCrv, baseName + side + "Dyn_baseCurve")


	if not nbrOfCtrl:
		# create fk control
		nbrOfCtrl = len(jntChain) # number of control
		DynLogger.info('Using specific joint number: %s ' %nbrOfCtrl)

	if nbrOfCtrl == 0:
		mc.error ("You have to create at least two FK control.")
	# elif nbrOfCtrl == 2:
	# 	mc.error ("The number of FK controls can't be superior to the number of joints in the chain.")
	elif nbrOfCtrl > len(jntChain):
		mc.error ("The number of FK controls can't be superior to the number of joints in the chain.")







	mc.select (baseCrv, r = 1)

	if selectedHairSystem != "":
		mc.select (selectedHairSystem, tgl = 1)
	# activate hsir system
	# !!! beware  if hair sys exists unname curve and follicle occur
	mel.eval ('makeCurvesDynamic 2 { "0", "0", "1", "1", "0"};')
	## After executing this command,
	## it created hairSystemShape itself
	## is selected by default.
	#... beware listHistory it will qury the old hairSystem by not intended
	dynItemsRaw = mc.listHistory()
	print(dynItemsRaw)


	# function organizeDynItems
	# Rename/organize newly created (dynamics) elements



	dynItems = []
	# if hair system never exists
	if selectedHairSystem == "":

	# dynItemsRaw = [hairSystemShape#, time#, nucleus#, follicleShape#, [baseCrv]rebuiltCurveShape#, rebuildCurve#, [baseCrv]Shape#', [baseCrv]]
	# Index =       [        0       ,   1   ,   2    ,        3      ,              4             ,        5     ,         6       ,      7   ]

		rawHairSyst = mc.pickWalk (dynItemsRaw[0], d = "up")
		hairSyst = mc.rename (rawHairSyst, baseName + side + "Dyn_hairSystem")
		rawNucleus = mc.pickWalk (dynItemsRaw[2], d = "up")
		nucleus = mc.rename (rawNucleus, baseName + side + "Dyn_nucleus")
		rawDynCrv = mc.listConnections (dynItemsRaw[3] + ".outCurve")
		dynCrv = mc.rename (rawDynCrv, baseName + side + "Dyn_dynamicCurve")
		rawHairSystCrvsGrp = mc.pickWalk (dynCrv, d = "up")
		hairSystCrvsGrp = mc.rename (rawHairSystCrvsGrp, baseName + side + "Dyn_hairSystem_OutputCurves")
		rawFollicle = mc.pickWalk (dynItemsRaw[3], d = "up")
		follicle = mc.rename (rawFollicle, baseName + side + "Dyn_follicle")
		rawHairSystFolliclesGrp = mc.pickWalk (follicle, d = "up")
		hairSystFolliclesGrp = mc.rename (rawHairSystFolliclesGrp, baseName + side + "Dyn_hairSystem_Follicles")
		dynItems.append (hairSyst)
		dynItems.append (nucleus)
		dynItems.append (hairSystFolliclesGrp)
		dynItems.append (follicle)
		dynItems.append (hairSystCrvsGrp)
		dynItems.append (dynCrv)

	# if hair system has exists
	else :
		'''
		newIdx = 0
		# fixed here
		# using index [1] in case using exists dynamic system
		
		folliclesInScene = mc.ls (type = "follicle")
		DynLogger.info('this is folliclesInScene = %s' %folliclesInScene[newIdx])
		if folliclesInScene[newIdx] != 'follicleShape1':
			mc.error('wrong name terminate.')
			newIdx = -1
		rawFollicle = mc.pickWalk (folliclesInScene[newIdx], d = "up")
		rawDynCrv = mc.listConnections (folliclesInScene[newIdx] + ".outCurve")
		hairSyst = mc.listConnections (folliclesInScene[newIdx] + ".outHair")
		'''

		DynLogger.info('Use fix variable instead if having some error let find here.')
		# use fix variable instead because of found unstable which idx use for sure
		new_folliclesInScene = 'follicleShape1'



		rawFollicle = mc.pickWalk (new_folliclesInScene, d = "up")
		rawDynCrv = mc.listConnections (new_folliclesInScene + ".outCurve")
		hairSyst = mc.listConnections (new_folliclesInScene + ".outHair")

		follicle = mc.rename (rawFollicle, baseName + side + "Dyn_follicle")
		dynCrv = mc.rename (rawDynCrv, baseName + side + "Dyn_dynamicCurve")
		hairSystShape = mc.pickWalk (hairSyst, d = "down")
		nucleus = mc.listConnections(hairSystShape) [1]
		rawHairSystFolliclesGrp = mc.pickWalk (follicle, d = "up")
		hairSystFolliclesGrp = mc.rename (rawHairSystFolliclesGrp, baseName + side + "Dyn_hairSystem_Follicles")
		rawHairSystCrvsGrp = mc.pickWalk (dynCrv, d = "up")
		hairSystCrvsGrp = mc.rename (rawHairSystCrvsGrp, baseName + side + "Dyn_hairSystem_OutputCurves")
		dynItems.append (hairSyst)
		dynItems.append (nucleus)
		dynItems.append (hairSystFolliclesGrp)
		dynItems.append (follicle)
		dynItems.append (hairSystCrvsGrp)
		dynItems.append (dynCrv)

	dynItemsList = dynItems




	# Set default parameters add later
	mc.setAttr (dynItemsList[3] + "Shape.pointLock", 1) # Follicle - Point Lock : Base
	if selectedHairSystem == "":
		hairSystRaw = dynItemsList[0]
		hairSyst = mc.pickWalk (hairSystRaw, d = "down") [0]
		mc.setAttr (hairSyst + ".startCurveAttract", 0.35)
		mc.setAttr (hairSyst + ".damp", 2)
		mc.setAttr (hairSyst + ".attractionScale[0].attractionScale_FloatValue", 0.6)
		mc.setAttr (hairSyst + ".attractionScale[1].attractionScale_FloatValue", 0.16)





	# Create the Ik spline


	'''
	Create the IK spline using the dynamic curve.

	Called by function(s): Rig.buildRig
	Call function(s): -
	Return: dynIkSpline (name of the ik handle)
	'''
	dynCrv = dynItemsList[-1]
	dynIkSplineRaw = mc.ikHandle (sol = "ikSplineSolver", ccv = 0, pcv = 0, sj = spIkJnt[0], ee = spIkJnt[-1], c = dynCrv)
	dynIkSpline = mc.rename (dynIkSplineRaw[0], baseName + side +"Dyn_ikh")
	mc.rename (dynIkSplineRaw[1], baseName + side +"Dyn_eff")
	mc.setAttr (dynIkSpline + ".visibility", 0)
	# return dynIkSpline







	# create Temp joint for fk joint chain
	origCrv = baseCrv
	x = 0
	fkJntChain = []
	radius = mc.joint (firstJnt, q = 1, rad = 1) [0]
	crv = mc.duplicate (origCrv, rr = 1)
	mc.rebuildCurve (crv, rpo = 1, rt = 0, end = 1, kr = 0, kcp = 0, kep = 1, kt = 1, s = 20, d = 3, tol = 0)

	# no need to check , check this condition as abrove
	# if nbrOfCtrl >= 2:
	DynLogger.info('This number of ctrl is more than two.')
	

	# for make output following arg that user want
	nbrOfCtrl = nbrOfCtrl - 1


	# change condition (edit#v 2)
	# for x in range (x, nbrOfCtrl + 1, x + 1):
	for x in range (x, nbrOfCtrl + 1, x + 1):
	# for x in range (nbrOfCtrl):
		incr = (1.0/nbrOfCtrl) * x
		ptOnCrvPos = mc.pointOnCurve (crv, pr = incr)
		rawFkJnt = mc.joint (rad = radius*0.75)
		fkJnt = mc.rename (rawFkJnt, baseName + "0%d_temp" % (x + 1) + side)
		fkJntChain.append (fkJnt)
		mc.xform (ws = 1, t = ptOnCrvPos)
	mc.delete (crv)
	# Orient FK joint chain
	# mc.joint (fkJntChain[0], e = 1, oj = "yzx", secondaryAxisOrient = "yup", ch = 1, zso = 1)
	# fix the orientation
	mc.joint (fkJntChain[0], e = 1, oj = "yxz", secondaryAxisOrient = "xdown", ch = 1, zso = 1)
	mc.setAttr (fkJntChain[-1] + ".jointOrientX", 0)
	mc.setAttr (fkJntChain[-1] + ".jointOrientY", 0)
	mc.setAttr (fkJntChain[-1] + ".jointOrientZ", 0)
	# return fkJntChain
	DynLogger.info('%s is joint chain.' %fkJntChain)



	'''
	elif nbrOfCtrl == 2: # just start and end
		for x in range (x, nbrOfCtrl):
			print x
			# position just start and end
			incr = (1.0) * x
			ptOnCrvPos = mc.pointOnCurve (crv, pr = incr)
			rawFkJnt = mc.joint (rad = radius*0.75)
			fkJnt = mc.rename (rawFkJnt, baseName + "0%d_temp" % (x + 1) + side)
			fkJntChain.append (fkJnt)
			mc.xform (ws = 1, t = ptOnCrvPos)
		mc.delete (crv)
		# Orient FK joint chain
		mc.joint (fkJntChain[0], e = 1, oj = "yzx", secondaryAxisOrient = "yup", ch = 1, zso = 1)
		mc.setAttr (fkJntChain[-1] + ".jointOrientX", 0)
		mc.setAttr (fkJntChain[-1] + ".jointOrientY", 0)
		mc.setAttr (fkJntChain[-1] + ".jointOrientZ", 0)
		# return fkJntChain
		DynLogger.info('%s is joint chain.' %fkJntChain)
	'''



	# MAKE TEMP JOINT TO IK JOINT
	# make controllre and parenting my method

	from function.rigging.autoRig.addRig import createFkRig
	reload(createFkRig)

	# dup fk joint chain to ik joint
	ikSpGen_jnt_grp = createFkRig.newCreateFkRig(	nameSpace = ''  ,  name = baseName + 'Ik' , parentTo = ''  ,
						tmpJnt = 	fkJntChain	,
						charScale = charScale	, priorJnt = '' 			,
						side = side ,ctrlShape = ctrlShape  , localWorld = False , 
						color = 'white' , curlCtrl = curlCtrl ,suffix = '_ikJnt'	)
										
	pm.delete( fkJntChain )					




	# skin ik joint to curve

	# exclude the last one
	# mc.select (ikSpGen_jnt_grp[2][:-1], baseCrv, r = 1)

	# add all joint (edit#v 2)
	mc.select (ikSpGen_jnt_grp[2], baseCrv, r = 1)

	# mc.select (ikSpGen_jnt_grp[2], baseCrv, r = 1)
	# mc.select (fkJntChain[:-1], baseCrv, r = 1)
	mc.skinCluster (n = baseName + side +"Dyn_Fk_skinCluster", tsb = 1, bm = 0, sm = 0, nw = 1, wd = 0, mi = 5, omi = 1, dr = 4, rui = 1)



	# make spFk_jnt_grp Chain
	spFk_jnt_grp = mc.duplicate (firstJnt, rr = 1)
	mc.select (spFk_jnt_grp, hi = 1)


	misc.searchReplace( searchText = lastName, replaceText='spFkJnt' )
	spFk_jnt_grp = misc.searchReplace( searchText='spFkJnt1', replaceText='spFkJnt' )
	pm.select( clear=True )




	# duplicate th curve
	# mc.dynCrv
	spFk_crv = mc.duplicate (baseCrv, rr = 1)[0]

	spFk_crv = mc.rename(spFk_crv, baseName + 'FK' + '_spFkJnt' + '_crv')
	# for attatch Dyn node (outdate)
	# firstFkCtrl = ctrlList[0]


	mc.select ( baseCrv , spFk_crv, r = 1)


	from function.rigging.skin import skinUtil
	reload(skinUtil)

	mc.select ( baseCrv, spFk_crv , r = 1)
	skinUtil.copyWeight()


	# mc.select ( spFk_crv,  spFk_jnt_grp[2][:-1] , r = 1)
	# mc.skinCluster (name = baseName + side +"FK_skinCluster", tsb = 1, bm = 0, sm = 0, nw = 1, wd = 0, mi = 5, omi = 1, dr = 4, rui = 1)




	dynFkSplineRaw = mc.ikHandle (sol = "ikSplineSolver", ccv = 0, pcv = 0, sj = spFk_jnt_grp[0], ee = spFk_jnt_grp[-1], c = spFk_crv)
	dynFkSpline = mc.rename (dynFkSplineRaw[0], baseName + side +"Manual_ikh")
	mc.rename (dynFkSplineRaw[1], baseName + side +"Manual_eff")
	mc.setAttr (dynFkSpline + ".visibility", 0)




	if selectedHairSystem == "":


		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
		# if HairSystem Non Exist Then Create stick controller
		# = = = = = = = = = = = = = = = = = = = = = = = = = = = #


		stickName = baseName + 'Stick'
		stick_ctrl = core.Dag( nameSpace + stickName + side + '_ctrl' )
		stick_ctrl.nmCreateController('stick_ctrlShape')
		stick_ctrl.editCtrlShape( axis = charScale * 1 )

		stick_ctrl.color = 'yellow'
		stick_ctrl.hideArnoldNode()

		stickZro_grp = rigTools.zeroGroup( stick_ctrl )
		stickZro_grp.name = nameSpace + stickName + side + 'Zro_grp'
		stickZro_grp.snapPoint( ikSpGen_jnt_grp[2][0] )

		print('Set rotation to %s controller...' %stick_ctrl.name)
		stickZro_grp.attr('rotateX').value += 90
		# Make stick control follow bJnt
		fkIkCtrlGrp_parCons = core.pointConstraint( firstJnt , stickZro_grp , mo = True)
		fkIkCtrlGrp_parCons.name = baseName + side + 'Stick'+ '_parCons'
		# Lock and hide
		stick_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )


		# stick_ctrl.attr('dynamic') >> 
		# ctrlShape.attr( 'gimbal' ) >> gmblCtrlShape.attr( 'v' ) 


		# attScaleName = stickScalNam +'Scale'
		# stick_ctrl.addAttribute( at = 'enum', keyable = True , en = 'Off:On', ln = 'dynamic')  

		stick_ctrl.addAttribute( longName = 'dynamic', defaultValue = 1 , min = 0  , max = 1  , keyable = True )



		# forget to connect
		stick_ctrl.addAttribute( longName = 'startFrame', defaultValue = 1 ,at = 'long'  , min = 0  , keyable = True )



		hairSystRaw = dynItemsList[0]
		hairSyst = mc.pickWalk (hairSystRaw, d = "down") [0]
		startCrvAttract = 	True
		motionDrag = 		True
		drag = 				True
		attrDamp = 			True
		damp = 				True
		mass = 				True
		noStretch = 		True
		default = startCrvAttract + motionDrag + drag + attrDamp + damp + mass + noStretch

		



		if default == 0:
			mc.warning ("As there's no dynamics parameters selected, all will be be added by default.")
		if (startCrvAttract == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "StartCurveAttract", at = "float", min = 0, max = 1, dv = 0.35, keyable = 1, hnv = 1, hxv = 1)
			mc.connectAttr (stick_ctrl.name + ".StartCurveAttract", hairSyst + ".startCurveAttract", f = 1)
		if (motionDrag == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "MotionDrag", at = "float", min = 0, max = 1, dv = 0, keyable = 1, hnv = 1, hxv = 1)
			mc.connectAttr (stick_ctrl.name + ".MotionDrag", hairSyst + ".motionDrag", f = 1)
		if (drag == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "Drag", at = "float", min = 0, max = 1, dv = 0.05, keyable = 1, hnv = 1, hxv = 1)
			mc.connectAttr (stick_ctrl.name + ".Drag", hairSyst + ".drag", f = 1)
		if (attrDamp == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "AttractionDamp", at = "float", min = 0, max = 1, dv = 0, keyable = 1, hnv = 1, hxv = 1)
			mc.connectAttr (stick_ctrl.name + ".AttractionDamp", hairSyst + ".attractionDamp", f = 1)
		if (damp == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "Damp", at = "float", min = 0, max = 10, dv = 2, keyable = 1, hnv = 1, hxv = 1)
			mc.connectAttr (stick_ctrl.name + ".Damp", hairSyst + ".damp", f = 1)
		if (mass == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "Mass", at = "float", min = 0, max = 10, dv = 1, keyable = 1, hnv = 1, hxv = 1)
			mc.connectAttr (stick_ctrl.name + ".Mass", hairSyst + ".mass", f = 1)
		if (noStretch == 1) or (default == 0) :
			mc.select (stick_ctrl.name, r = 1)
			mc.addAttr (ln = "NoStretch", at = "bool", keyable = 1)
			mc.connectAttr (stick_ctrl.name + ".NoStretch", hairSyst + ".noStretch", f = 1)
	else:
		mc.warning ("No attributes will be created since the hairSystem is already connected to another control.")


	#... Making pair psCon between ik << bJnt >> ik
	# list name
	# fkChain = spFk_jnt_grp[2]
	fkChain = spFk_jnt_grp

	# Fkjnt
	ikChain = spIkJnt
	# bjnt
	bJntChain = jntChain

	# placementCtrl = 'skirtFrontStick_ctrl'

	num = 0
	for i in range(len(bJntChain)):
		# psCon = mc.parentConstraint( each + side +'_fkJnt', each + side +'_ikJnt' , each + side +'_buffJnt'  , name = each + 'Switch' + side + '_parCons' )
		print ('# # # pair constraint # # #')
		DynLogger.info(baseName + '%02d%s_psCon' %(( num +1),side))
		print (fkChain[i])
		print (ikChain[i])
		print (bJntChain[i])
		

		# psCon = mc.parentConstraint( fkChain[i] , ikChain[i] , bJntChain[i] , name = baseName + '%02d%s_psCon' %(( num +1),side) )
		psCon = mc.parentConstraint( fkChain[i] , ikChain[i] , bJntChain[i] , name = baseName + '%02d%s_psCon' %(( num +1),side) )

		#... CASE Create New One
		#... If new one create switch connection between dynamic and IK
		if selectedHairSystem == "":
			revNode = mc.createNode( 'reverse' , name = baseName + '%02d%s' %(( num +1),side) + '_rev')
			mc.connectAttr( '%s.%s' %( stick_ctrl.name, 'dynamic' ) , revNode + '.inputX'  )
			mc.connectAttr( '%s.%s' %( stick_ctrl.name, 'dynamic' ) ,  psCon[0] + '.w1' )
			mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.w0' )
			num = num+1

			print ('\n')



		#... CASE Already Exists
		#... If  dynamic system already exists create connection only
		if selectedHairSystem:
			if meta:
				revNode = meta.attr('reverseNode').value
				DynLogger.info('YESH')
				mc.connectAttr( '%s.%s' %( stick_ctrl.name, 'dynamic' ) ,  psCon[0] + '.w1' )
				mc.connectAttr( revNode + '.outputX'  , psCon[0] + '.w0' )
				num = num+1




	if selectedHairSystem == "":
		# connect value to turn off dynamic

		# create condition node for pipe value
		enable_cnd = core.Condition(baseName + side)
		enable_cnd.suffix

		#... set inital value
		#... change from 1 to 0 for use simulation method to 'Off' instead 'Static' (static make join alway jiggle whan translate controller)
		# enable_cnd.attr('colorIfTrueR').value = 1
		enable_cnd.attr('colorIfTrueR').value = 0
		enable_cnd.attr('colorIfFalseR').value = 3	

		# ctrl >> condition
		mc.connectAttr (stick_ctrl.name + ".dynamic", enable_cnd.name + '.firstTerm', f = 1)

		# condition >> dynamic node
		mc.connectAttr ( enable_cnd.name + '.outColorR',  dynItemsList[0] + 'Shape' + '.simulationMethod' ,f=1)
		mc.connectAttr ( enable_cnd.name + '.outColorG',  dynItemsList[1] + '.enable' ,f=1)



	# clearSceneAndScript

	'''
	Group the objects, delete unused nodes,
	clear the script UI, etc.

	Called by function(s): Rig.buildRig
	Call function(s): -
	Return: -
	'''
	 # Use: dynItemsList, dynIkSpline, baseName

	all_dyn_grp = mc.group (n = baseName + side + "Dyn_grp", em = 1)
	mc.parent (dynItemsList[0], all_dyn_grp)
	mc.parent (dynItemsList[1], all_dyn_grp)
	mc.parent (dynItemsList[2], all_dyn_grp)
	mc.parent (dynItemsList[4], all_dyn_grp)
	mc.parent (dynIkSpline, all_dyn_grp)
	mc.parent (dynFkSpline, all_dyn_grp)
	mc.setAttr (all_dyn_grp + ".visibility", 0)

	mc.setAttr ( str(ikSpGen_jnt_grp[2][0]) + ".visibility", 0)
	mc.setAttr ( fkChain[0] + ".visibility", 0)
	mc.setAttr ( spIkJnt[0]+ ".visibility", 0)

	all_jnt_grp = mc.group (n = baseName + side + "Jnt_grp", em = 1)
	mc.parent ( spIkJnt[0], all_jnt_grp )
	mc.parent ( ikSpGen_jnt_grp[2][0], all_jnt_grp )
	mc.parent ( spFk_jnt_grp[0], all_jnt_grp )



	pm.select( clear=True )

	# return
	print ('\n')
	# print "------------ return all of this string --------------------"
	misc.makeHeader('Dynamics FK Chains Ending')
	# print firstJnt ,spIkJnt[0] ,ikSpGen_jnt_grp[1] ,ikSpGen_jnt_grp[2][0] ,spFk_jnt_grp[0] ,ikSpGen_jnt_grp[3] ,allGrp, dynItems[0]
	# will correct this later


	# parenting group
	if priorJnt:
		mc.parent(firstJnt, priorJnt)

		DynLogger.info(all_dyn_grp)


		# Constraint rig_grp to prior controller grp
		rigGrp_parCons = core.parentConstraint( priorJnt , ikSpGen_jnt_grp[1] , mo = True)
		rigGrp_parCons.name = nameSpace + baseName + side +'RigGrp_parCons'

	if parentTo:
		mc.parent(ikSpGen_jnt_grp[1], parentTo)


	# no need prior ctrl, use above instead
	# if priorCtrl:
		# pass
		# priorCtrl_parCons = core.parentConstraint( priorCtrl , spineRig_grp , mo = True)
		# priorCtrl_parCons.name = nameSpace + baseName + side + '_parCons'

	# set default value to zero
	stick_ctrl.attr('dynamic').value = 0

	#... Create network node for store data
	dynIkSpline_meta = core.MetaGeneric(baseName + side)

	mc.connectAttr(priorJnt + '.message', dynIkSpline_meta.name + '.Rig_Prior')

	dynIkSpline_meta.setAttribute('Base_Name', all_dyn_grp , type = 'string')
	dynIkSpline_meta.addAttribute( dataType = 'string' , longName = 'Input')
	dynIkSpline_meta.setAttribute('Input', [firstJnt,lastJnt] , type = 'string')

	dynIkSpline_meta.addAttribute( dataType = 'string' , longName = 'hairSystem')
	dynIkSpline_meta.setAttribute('hairSystem', dynItems[0] , type = 'string')

	dynIkSpline_meta.addAttribute( dataType = 'string' , longName = 'reverseNode')
	dynIkSpline_meta.setAttribute('reverseNode', revNode , type = 'string')

	dynIkSpline_meta.addAttribute( dataType = 'string' , longName = 'stickCtrl')
	dynIkSpline_meta.setAttribute('stickCtrl', stick_ctrl.name , type = 'string')

	if side:
		dynIkSpline_meta.setAttribute('Side', side , type = 'string')


	if selectedHairSystem == "":
		# return = [firstJnt#, ik joint#, nucleus#, follicleShape#, [baseCrv]rebuiltCurveShape#, rebuildCurve#, [baseCrv]Shape#', [baseCrv]]
		# Index =  [        0       ,   1   ,   2    ,        3      ,              4             ,        5     ,         6       ,      7   ]
		# print  all_jnt_grp ,ikSpGen_jnt_grp[1] ,all_dyn_grp, dynItems[0] ,stickZro_grp.name

		return firstJnt, spIkJnt[0], ikSpGen_jnt_grp[1], ikSpGen_jnt_grp[2][0], spFk_jnt_grp[0], ikSpGen_jnt_grp[3], all_dyn_grp, dynItems[0], stickZro_grp.name, all_jnt_grp, revNode, dynIkSpline_meta
	else:
		# print  all_jnt_grp ,ikSpGen_jnt_grp[1] ,all_dyn_grp, dynItems[0] 
		return firstJnt ,spIkJnt[0] ,ikSpGen_jnt_grp[1] ,ikSpGen_jnt_grp[2][0] ,spFk_jnt_grp[0] ,ikSpGen_jnt_grp[3] ,all_dyn_grp, dynItems[0],all_jnt_grp

"""
# u must manage to store the grp by use this as a sample

jnt_grp = mc.group(em=True, name = 'skirtDynJnt_grp')
rig_grp = mc.group(em=True, name = 'skirtDynRig_grp')
#rig_grp = mc.group(em=True, name = 'skirtDynRig_grp')
dyn_grp = mc.group(em=True, name = 'skirtDyn_grp')
mc.parent( rig_grp ,'hip_gmbCtrl' )





# new condition
bJnt_grp = skirtFront_grp[0]
jnt_grp = skirtFront_grp[9]
dyn_grp = skirtFront_grp[6]
rig_grp  = skirtFront_grp[2] 
stick_grp  = skirtFront_grp[8] 


# parent
mc.parent( bJnt_grp ,'hip_bJnt')	
mc.parent( rig_grp ,'hip_gmbCtrl' )
mc.parent( jnt_grp ,'jnt_grp' )
mc.parent( dyn_grp ,'noTouch_grp' )
mc.parent( stick_grp ,'ctrl_grp' )



"""
