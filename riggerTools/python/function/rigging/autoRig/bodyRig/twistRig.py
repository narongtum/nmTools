# -*- coding: utf-8 -*-
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

import maya.cmds as mc

from function.rigging.util import misc
reload( misc )

import sys

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


"""
Example:
Create single joint at the same position of shoulder or thight that ignore Rotation y (twist)


 [+] << shoulder joint
  +
 [+] << twist joint (acually is the same prosition)
  +
  +
  +
  +
 [+] << elbow joint

# direct run


from function.rigging.autoRig.bodyRig import twistRig as tr
reload( tr )

tr.twistRig( 	side = 'LFT' , 
				region = 'arm' ,
				parent_jnt = 'upperArmLFT_bind_jnt' , 
				child_jnt = 'lowerArmLFT_bind_jnt' ,
				showInfo = False,
				haveRibbon = False )
"""


def twistRigAuto(			nameSpace = '',
							parent_jnt = 'upperLegLFT_bJnt' , 
							child_jnt = 'lowerLegLFT_bJnt' , 
							fk_shoulderCtrl = 'upperArmFkLFT_ctrl' ,
							ik_shoulderCtrl = 'upperArmIkRootLFT_ctrl' ,
							side = 'LFT' , 
							region = 'leg' ,
							priorJnt = 'handStickLFT_ctrl', 
							stick_ctrl = '',
							charScale = 1.0 ,
							showInfo = True,
							alongAxis = 'y' ):



	"""
	Create single joint at the same position of shoulder or thight that ignore Rotation y (twist)
	Result :
	got twsit joint  and auto rotate
	
	it pretty ok i think
	
	Args:
		side (str): LFT or RGT side parameter.
		region (str): arm or leg part parameter.
		priorJnt(str): name of joint that parent of the parent joint
		parent_jnt(str): name of joint that parent of the second joint
		child_jnt(str): name of joint that child of the second joint
		charScale(int): character scale

	Returns:
		follow_grp(str)



	"""




	# cancle this method get name from arg instead for make it more elestic

	'''
	if region == 'arm':
		# priorJnt = 'clav%s_bJnt' %side
		stick_ctrl = 'handStick%s_ctrl' %side

	elif region == 'leg':
		# priorJnt = 'hip_bJnt'
		stick_ctrl = 'ankleStick%s_ctrl' %side
	'''


	core.makeHeader(	'Start of %s%s Rig' %('twistRigAuto',side)	)

	# return follow_grp name


	region = region.capitalize() 
	shoulder_jnt = core.Dag(parent_jnt)
	elbow_jnt = core.Dag(child_jnt)


		



	# Find distance between shoulder to elbow
	if alongAxis == 'y':
		lenght = elbow_jnt.attr('translateY').value 
	if alongAxis == 'x':
		lenght = elbow_jnt.attr('translateX').value 

	# Divide half
	lenght = lenght/2


	# Change value by side
	#... Add more condition
	if side == 'LFT' and alongAxis == 'y':
		i = 1
		aimVec = (0,1,0)
		upVec = (0,0,-1)

	elif side == 'RGT' and alongAxis == 'y':
		i = -1
		aimVec = (0,-1,0)
		upVec = (0,0,1)

	elif side == 'LFT' and alongAxis == 'x':
		i = 1
		aimVec = (1,0,0)
		upVec = (0,-1,0)

	elif side == 'RGT' and alongAxis == 'x':
		i = -1
		aimVec = (-1,0,0)
		upVec = (0,1,0)


	upperTwist01_jnt = core.Joint()
	upperTwist01_jnt.name = nameSpace + 'upper%sTwist01%s_twJnt' %(region,side) 
	twistShapeJnt = core.Locator('tmpName')
	# Swap shape node of locator to joint 
	mc.parent( twistShapeJnt.shape , upperTwist01_jnt.name , s = True , r = True )
	mc.rename( twistShapeJnt.name + 'Shape' , upperTwist01_jnt.name + 'Shape')
	mc.delete( twistShapeJnt.name)
	upperTwist01_jnt.setOutlineColor('white')
	upperTwist01_jnt.setJointColor('white')


	upperTwist02_jnt = core.Joint()
	upperTwist02_jnt.name = nameSpace +'upper%sTwist02%s_twJnt' %(region,side) 
	twistShapeJnt = core.Locator('tmpName')
	# Swap shape node of locator to joint 
	mc.parent( twistShapeJnt.shape , upperTwist02_jnt.name , s = True , r = True )
	mc.rename( twistShapeJnt.name + 'Shape' , upperTwist02_jnt.name + 'Shape')
	mc.delete( twistShapeJnt.name)
	upperTwist02_jnt.setOutlineColor('white')
	upperTwist02_jnt.setJointColor('white')



	upperTwist01_jnt.maSnap( parent_jnt )

	# make it forward a bit
	if alongAxis == 'y':
		mc.move(0, i*0.0125, 0 ,  upperTwist01_jnt.name , relative=True, objectSpace=True, worldSpaceDistance=True )
	elif alongAxis == 'x':
		mc.move(i*0.0125, 0, 0 ,  upperTwist01_jnt.name , relative=True, objectSpace=True, worldSpaceDistance=True )

	upperTwist01_jnt.freeze()

	upperTwist02_jnt.maSnap( upperTwist01_jnt )
	upperTwist02_jnt.parent(upperTwist01_jnt)



	upperTwist01_jnt.parent(shoulder_jnt)

	upperTwist02_jnt.freeze()
	if alongAxis == 'y':
		upperTwist02_jnt.attr('translateY').value = lenght
	elif alongAxis == 'x':
		upperTwist02_jnt.attr('translateX').value = lenght

	upperTwist01_jnt.attr('radius').value = charScale*4

	upperTwist01_jnt.attr('localScaleX').value = charScale*0.1
	upperTwist01_jnt.attr('localScaleY').value = charScale*0.1
	upperTwist01_jnt.attr('localScaleZ').value = charScale*0.1

	upperTwist02_jnt.attr('localScaleX').value = charScale*0.1
	upperTwist02_jnt.attr('localScaleY').value = charScale*0.1
	upperTwist02_jnt.attr('localScaleZ').value = charScale*0.1



	# Create locator for guide upVector
	upVectorGuide_loc = core.Locator( nameSpace + 'upper%sAimUp%s_loc' %(region,side) )
	upVectorGuide_loc.maSnap(upperTwist01_jnt)
	#upVectorGuide_loc.freeze()
	#upVectorGuide_loc.attr('translateY').value = 0.5


	if alongAxis == 'y':
		MOVE_POSITION = ( 0, 0, lenght*-1*1.25 )
	elif alongAxis == 'x':
		MOVE_POSITION = ( 0, lenght*-1*1.25, 0 )
	



	if alongAxis == 'y':
		MOVE_UPVEC = ( 0, 0, lenght*-1*2.5 )
	elif alongAxis == 'x' and side == 'LFT':
		MOVE_UPVEC = ( 0, lenght*-1*2.5, 0 )
	elif alongAxis == 'x' and side == 'RGT':
		MOVE_UPVEC = ( 0, lenght*-1*2.5, 0 )

	#... if to short it will flip
	upVectorGuide_loc.moveObj( position = MOVE_UPVEC )
	upVectorGuide_loc.setColor('white')





	#upVectorGuide_grp = rigTools.zeroGroupNam( upVectorGuide_loc )

	twist_aimCons = core.aimConstraint( child_jnt , upperTwist01_jnt , aimVector = aimVec , mo = False , upVector = upVec , worldUpType = "object"  , worldUpObject = upVectorGuide_loc.name )
	twist_aimCons.name = nameSpace + 'upper%s%s' %(region,side) 
	twist_aimCons.suffix


	# create following joint 
	upperFollow01_jnt = rigTools.jointAt( upperTwist01_jnt )
	upperFollow01_jnt.name = nameSpace + 'upper%sFollow01%s_twJnt' %(region,side) 
	upperFollow01_jnt.moveObj( position = MOVE_POSITION )
	upperFollow01_jnt.setJointColor('white')

	upperFollow01_jnt.freeze()



	upperFollow02_jnt = rigTools.jointAt( upperTwist02_jnt )
	upperFollow02_jnt.name = nameSpace + 'upper%sFollow02%s_twJnt' %(region,side) 
	upperFollow02_jnt.moveObj( position = MOVE_POSITION )
	upperFollow01_jnt.setJointColor('white')
	upperFollow02_jnt.parent(upperFollow01_jnt)


	upVectorGuide_loc.parent(upperFollow01_jnt)

	upVectorGuide_loc.attr('localScaleX').value = charScale*0.1
	upVectorGuide_loc.attr('localScaleY').value = charScale*0.1
	upVectorGuide_loc.attr('localScaleZ').value = charScale*0.1

	# fix error here
	twistAim_ikh = core.DoIk( startJoint = upperFollow01_jnt , endEffector = upperFollow02_jnt , solverType = 'ikRPsolver' )
	twistAim_ikh.name = nameSpace + 'upper%sFollow%s_ikh' %(region,side) 



	twistAim_ikh.parent(child_jnt)
	twistAim_ikh.maSnap(child_jnt)


	# reset value for enable twist effect proper
	twistAim_ikh.attr('poleVectorX').value = 0
	twistAim_ikh.attr('poleVectorY').value = 0
	twistAim_ikh.attr('poleVectorZ').value = 0





	# Manipulate Enable and attr value function
	fk_shoulder_ctrl = core.Dag(fk_shoulderCtrl)
	ik_shoulder_ctrl = core.Dag(ik_shoulderCtrl)



	# Enable / Disable twist option 
	# start
	fk_shoulder_ctrl.addAttribute(  attributeType = 'bool',longName = '%sTwist' %region , min = 0 , max = 1, defaultValue = 1 , keyable = True )
	fk_shoulder_ctrl.attr( '%sTwist' %region ) >> twist_aimCons.attr( '%sW0'%elbow_jnt.name )


	# bypass twist value to fk
	fk_shoulder_ctrl.addAttribute( longName = '%sFkTwist' %region , defaultValue = 0 , keyable = True )
	fk_invertVal_mdl = core.MDLWithMul('%sFkInVal%s' %(region,side) )
	fk_invertVal_mdl.attr( 'multiply' ).value = i*0.5
	fk_shoulder_ctrl.attr( '%sFkTwist' %region ) >> fk_invertVal_mdl.attr( 'input1' )

	# bypass twist value to ik
	ik_shoulder_ctrl.addAttribute( longName = '%sIkTwist' %region , defaultValue = 0 , keyable = True )
	ik_invertVal_mdl = core.MDLWithMul('%sInVal%sIk' %(region,side) )
	ik_invertVal_mdl.attr( 'multiply' ).value = i*0.5
	ik_shoulder_ctrl.attr( '%sIkTwist' %region) >> ik_invertVal_mdl.attr( 'input1' )

	limbSwitch_ctrl = core.Dag( stick_ctrl )

	# create condition for plug that two line together
	shoulder_con = core.Condition('%sTwist%s_con' %(region,side) )
	limbSwitch_ctrl.attr( 'FK_IK' ) >> shoulder_con.attr( 'firstTerm' )
	fk_invertVal_mdl.attr( 'output' ) >> shoulder_con.attr( 'colorIfTrueR' )
	ik_invertVal_mdl.attr( 'output' ) >> shoulder_con.attr( 'colorIfFalseR' )
	
	# make upVec translatable via attr
	shoulder_con.attr( 'outColorR' ) >> upVectorGuide_loc.attr( 'tx' )
	# end










	# Parent constraint the follow upper jnt (humerus) for follow as the rest of the body joint
	# create null grp
	follow_grp = core.Null( nameSpace + 'upper%sFollow%s_grp' %(region,side)  )
	upperFollow01_jnt.parent(follow_grp)



	followGrp_parCons = core.parentConstraint( priorJnt , follow_grp , mo = True	 )
	followGrp_parCons.name = nameSpace + 'upper%sFollow%s_psCons' %(region,side) 
	followGrp_scalCons = core.scaleConstraint( priorJnt , follow_grp , mo = True	 )
	followGrp_scalCons.name = nameSpace + 'upper%sFollow%s_scalCons' %(region,side) 

	if showInfo == False:
		upperFollow01_jnt.attr('visibility').value = 0
	
	misc.makeHeader(	nameSpace + 'twistRigAuto %s%s Complete' %(region,side)	)

	#... for debug
	# sys.exit(upVectorGuide_loc.name)

	return follow_grp.name , upperTwist01_jnt.name 
