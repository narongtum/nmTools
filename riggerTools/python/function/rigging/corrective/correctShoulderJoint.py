#... move to rig tools already
#... using only Y alone
#... D:\narongtum\research_and_developement\22.10.Oct.21.Fri.10_Helper Joint

# create joint that aim to the desinate point to make fake muscle
# 1. create delt muscle joint at shoulder position start_jnt and end_jnt
# 2. name of the upperArm and lowerArm 
# 3. remember the this function is will made bind join extract from all bind joint chain



"""
#... corrective joint for shoulder

# direct run
from function.rigging.corrective import correctShoulderJoint as chd
reload(chd)

chd.correctShoulderJoint(	tmpJnt = 	('L_deltMidAimStart_jnt' , 
										                   'L_deltMidAimEnd_jnt') 	, 
							side = 'LFT',
							priorJnt = 'clavLFT_tmpJnt',
							belowJnt = 'upperArmLFT_tmpJnt',
							part = 'deltMid',
							showInfo = True
							
							)

"""




import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.util import misc as misc
reload(misc)








def correctShoulderJoint(	tmpJnt = 	('L_deltMidAimStart_jnt' , 
										'L_deltMidAimEnd_jnt') 	, 
							side = 'LFT',
							priorJnt = 'clavLFT_bJnt',
							belowJnt = 'upperArmLFT_tmpJnt',
							part = 'deltMid',
							showInfo = True
							
							):

	
	
	types = 'Aim'
	# create joint start and end
	start_jnt = rigTools.jointAt(tmpJnt[0])
	start_jnt.name = part + types + 'Start' + side + '_bJnt' 
	start_jnt.setJointColor('white')

	end_jnt = rigTools.jointAt(tmpJnt[1])
	end_jnt.name = part + types + 'End' + side + '_jnt' 
	end_jnt.setJointColor('white')

	end_jnt.parent(start_jnt)



	# create locator at each position
	types = ''
	start_loc = core.Locator( part + types + '_Start' + side + '_loc' )
	end_loc = core.Locator( part + types + '_End' + side + '_loc' )
	up_loc = core.Locator( part + types + '_Up' + side + '_loc' )
	up_loc.setColor('white')

	# Snap position
	start_loc.maSnap(start_jnt)
	end_loc.maSnap(end_jnt)
	up_loc.maSnap(start_jnt)
	# up_loc.maSnap(start_jnt, pos = True,rot = False,scl = False)



	# Find distance between shoulder to elbow
	lenght = end_jnt.attr('translateY').value 


	# Change value by side
	if side == 'LFT':
		i = 1
		aimVec = (0,1,0)
		upVec = (0,0,1)

	elif side == 'RGT':
		i = -1
		aimVec = (0,-1,0)
		upVec = (0,0,-1)

	# move up locator to forwatd
	mc.move(0,  0, i*lenght ,  up_loc.name , relative=True, objectSpace=True, worldSpaceDistance=True )

	# make zeroGroup
	upZro_grp = rigTools.zeroGroup(up_loc)
	upZro_grp.name = part + types + 'Up' + side + 'Zro_grp'

	# joint_aimCons = core.aimConstraint( end_loc , start_jnt , aimVector = aimVec , mo = False , upVector = upVec , worldUpType = "object"  , worldUpObject = up_loc.name )
	joint_aimCons = core.aimConstraint( end_loc , start_jnt , aimVector = aimVec , mo = False , upVector = upVec , worldUpType = "object"  , worldUpObject = up_loc.name )

	joint_aimCons.name = part + types + 'Start' + side
	joint_aimCons.suffix



	jointStart_poiCons = core.pointConstraint( start_loc , start_jnt , mo = False )
	jointStart_poiCons.name = part + types + 'Start' + side
	jointStart_poiCons.suffix


	jointEnd_poiCons = core.pointConstraint( end_loc , end_jnt , mo = False )
	jointEnd_poiCons.name = part + types + 'End' + side
	jointEnd_poiCons.suffix

	types = 'distance'
	lengte_dis = core.DistanceBetween()
	lengte_dis.name = part + types + side 
	lengte_dis.suffix



	start_loc.attr( 'center' ) >> lengte_dis.attr( 'point1' )
	end_loc.attr( 'center' ) >> lengte_dis.attr( 'point2' )




	reserveVal_mdl = core.MultiplyDivide( part + 'Reserv' + side )
	reserveVal_mdl.suffix

	lengte_dis.attr( 'distance' ) >> reserveVal_mdl.attr('input1X')

	distance = lengte_dis.attr( 'distance' ).value

	reserveVal_mdl.attr('input2X').value = distance
	reserveVal_mdl.attr('operation').value = 2
	reserveVal_mdl.attr( 'outputX' ) >> start_jnt.attr('scaleY')



	# parentConst end loc to the child of this mucsle joint



	endLoc_psCons = core.parentConstraint( priorJnt , end_loc.name , mo = True )
	endLoc_psCons.name = part + 'End' + side
	endLoc_psCons.suffix


	# make grp 
	types = 'All'
	all_grp = core.Null( part + 'Ctrl' + side + '_grp' )
	#all_grp.maSnap(start_jnt)

	start_jnt.setOutlineColor('white')
	end_jnt.setOutlineColor('white')
	start_jnt.parent(all_grp)
	start_loc.parent(all_grp)
	end_loc.parent(all_grp)
	# up_loc.parent(all_grp)
	upZro_grp.parent(all_grp)

	#... this will cause error for sure 	 
	# not elbow use upperArm siwa
	endLoc_psCons = core.parentConstraint( belowJnt , all_grp , mo = True )
	endLoc_psCons.name = part + 'End' + side
	endLoc_psCons.suffix




	if showInfo == False:
		start_loc.lockHideAttrLst( 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')
		end_loc.lockHideAttrLst( 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')
		up_loc.lockHideAttrLst( 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')
		all_grp.attr('visibility').value = 0
	# delete template joint
	mc.delete(tmpJnt)

	mc.select(deselect = True)
	misc.makeHeader('End of function') 
	return all_grp
	