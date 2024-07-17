#... Core function from nick miller

#...Formula
#
#y = {                                              
#                     -(x-da)/
#        dsoft(1 - e^  dsoft  ) + da   (da <= x)
#                                                   }
#
# da = length_AB - dsoft
# length_AB = sum of bone lengths
# dsoft = user set soft distance (how far the effector should fall behind)
# x = distance between root and ik

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

import math
#... find magnitude
def mag( v ):
	return( math.sqrt( pow( v[0], 2) + pow( v[1], 2) + pow( v[2], 2)))

from function.pipeline import logger 
reload(logger)

class SoftIkLogger(logger.MayaLogger):
	LOGGER_NAME = "SoftIk"

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload( misc )

MAYA_VERSION = mc.about(v=True)
# upAxis = 2
# primaryAxis = 2 
# ikhName= 'ankleIkRGT_ikh'# ikhNam
# side = 'RGT' #side
# region = 'leg' #region
# ctrlName = 'footIkRGT_ctrl' # lowerIk_ctrl.name
# inputMax = 40
# outputMax = 4





def softIK(		nameSpace,priorMeta, region, side, ctrlName,
				upAxis = 2, primaryAxis = 2, ikhName= 'ankleIkRGT_ikh', 
				inputMax = 40, outputMax = 4, debug = False  ):

	SoftIkLogger.debug('ikhName is:{0}'.format(ikhName))
	SoftIkLogger.debug('ctrlName is:{0}'.format(ctrlName))

	name = '{0}softIk{1}_{2}'.format(nameSpace, side, region)


	#primary axis options
	if( primaryAxis == 1):
		primaryAxis = 'X'
	if( primaryAxis == 2):
		primaryAxis = 'Y'
	if( primaryAxis == 3):
		primaryAxis = 'Z'



	#... finds name for joints
	startJoint = mc.listConnections( ikhName + ".startJoint" )
	endEffector = mc.listConnections( ikhName + ".endEffector" )
	endJoint = mc.listConnections( endEffector, d = False, s = True )

	#selects joint chain effected by IKH
	mc.select( startJoint, hi = True )
	mc.select( endJoint, hi = True, d = True )
	mc.select( endEffector, d = True )

	if MAYA_VERSION != '2022':
		mc.select( endJoint, toggle = True ) #... only maya 2022 is not select end joint
	else:
		SoftIkLogger.debug('# # # # found maya 2022 change order HERE')
		mc.select( endJoint[0], toggle = True ) #... only maya 2022 is not select end joint

	#lists the joints
	joints = []
	joints = mc.ls( sl = True )



	n = len(joints)
	#------------------ Filter something not joint -------------------------------------------------------------------#
	for each in range(n):
	    print(each)
	    
	    if mc.nodeType(joints[each]) != 'joint':
	        del_lana = each

	#... remove unwanted         
	joints.pop(del_lana)        
	n = len(joints)        


	SoftIkLogger.debug('number is:{0}'.format(n))
	SoftIkLogger.debug('name is:{0}'.format(joints))

	if len(joints) < 3:
		mc.warning('EndEffector not found.')

	#... gives position value for joints
	firstPos = mc.xform( joints[0], q = True, piv = True, ws = True )
	lastPos = mc.xform( joints[n - 1], q = True, piv = True, ws = True )
	fPoints  = firstPos[0:3]
	lPoints = lastPos[0:3]

	#up axis options
	if( upAxis == 1):
		upAxis = 'X'
		gPoint = ( 0, lPoints[1], lPoints[2] )
	if( upAxis == 2):
		upAxis = 'Y'
		gPoint = (lPoints[0], 0, lPoints[2])
	if( upAxis == 3):
		upAxis = 'Z'
		gPoint = ( lPoints[0], lPoints[1], 0)




	

	#-----------------------------------------------------------------------------------------------------------------------------#
	#find the length_AB = sum of bone lengths
	i = 0
	length_AB = 0
	while ( i < n - 1 ):
		a = mc.xform( joints[i], q = True, piv = True, ws = True )
		b = mc.xform( joints[ i + 1 ], q = True, piv = True, ws = True )
		x = b[0] - a[0]
		y = b[1] - a[1]
		z = b[2] - a[2]
		v = [x,y,z]
		length_AB += mag(v)
		i += 1


	print('\nlength_AB is: {0}'.format(length_AB))

	#... compair length A and B
	vec_a = mc.xform( joints[0], q = True, piv = True, ws = True )
	vec_b = mc.xform( joints[1], q = True, piv = True, ws = True )
	x = vec_b[0] - vec_a[0]
	y = vec_b[1] - vec_a[1]
	z = vec_b[2] - vec_a[2]
	vec_AB = [x,y,z]

	print('\nlength A is: {0}'.format(mag(vec_AB)))


	#... compair length B and C
	vec_b = mc.xform( joints[1], q = True, piv = True, ws = True )
	vec_c = mc.xform( joints[2], q = True, piv = True, ws = True )
	x = vec_b[0] - vec_c[0]
	y = vec_b[1] - vec_c[1]
	z = vec_b[2] - vec_c[2]
	vec_BC = [x,y,z]

	print('\nlength B is: {0}'.format(mag(vec_BC)))




	if mag(vec_BC) > mag(vec_AB):
	    print('\nThere is length of upper is LESS than lower')
	    #mc.error('There is length of upper is less than lower')
	elif mag(vec_BC) == mag(vec_AB):
		mc.error('There is length of upper is EQUAL')
	else:
	    print('\nThere is length of upper is MORE than lower, You shall Pass...')

	#-----------------------------------------------------------------------------------------------------------------------------#
	#...get the distance from 0 to the ikh for compensage length 
	x = lPoints[0] - gPoint[0]
	y = lPoints[1] - gPoint[1]
	z = lPoints[2] - gPoint[2]
	v = [x,y,z]
	defPos = mag(v)
	if( ( upAxis == 'X' ) and ( lastPos[0] < 0 ) ):
		defPos = defPos * -1
	if( ( upAxis == 'Y' ) and ( lastPos[1] < 0 ) ):
		defPos = defPos * -1
	if( ( upAxis == 'Z' ) and ( lastPos[2] < 0 ) ):
		defPos = defPos * -1
		
	print('\nDefault position is: {0}'.format(defPos))
	#---------------- Create Locator -----------------------------------------------------------------------------------------------#
	#... Create the distance node, otherwise know as x(distance between root and ik)

	loc_check_grp = core.Null('%s_loc_grp'%name)

	if debug == False:

		test_loc = mc.spaceLocator( n = '%s_test_last_point_BAK' % name )
		mc.xform(test_loc, translation=lPoints)
		mc.parent(test_loc, loc_check_grp.name)

	


	#... Create loc and Null Grp
	start_loc = mc.spaceLocator( n = '%s_start_dist_loc' % name )
	mc.xform( '%s_start_dist_loc' % name, t = fPoints, ws = True )

	end_loc = mc.spaceLocator( n = '%s_end_dist_loc' % name )
	mc.xform( '%s_end_dist_loc' % name, t = lPoints, ws = True )

	mc.parent(start_loc, loc_check_grp.name)
	mc.parent(end_loc, loc_check_grp.name)

	if mc.objExists('loc_grp'):
		mc.parent(loc_check_grp.name, 'loc_grp')


	else:
		mc.parent(loc_check_grp.name, 'placement_ctrl')




	#... Parent later
	# mc.select( ctrlName, '%s_end_dist_loc' % name, r = True )
	# mc.parentConstraint( w = 1, mo = True)

	

	

	mc.select( joints[0], '%s_start_dist_loc' % name, r = True )
	mc.parentConstraint( w = 1, mo = True)

	mc.createNode( 'distanceBetween', n = '%s_x_distance' % name )
	mc.connectAttr( '%s_start_dist_loc.translate' % name, '%s_x_distance.point1' % name )
	mc.connectAttr( '%s_end_dist_loc.translate' % name, '%s_x_distance.point2' % name )



	xLength = mc.getAttr('%s_x_distance.distance'%name)
	print('\nxLength is: {0}'.format(xLength))

	#---------------------------------------- Create meta node -----------------------------------------------------------#
	
	meta_node = core.MetaGeneric('%s_distance' %name)

	if MAYA_VERSION == '2018':
		meta_node.setAttribute('Base_Name'  , __name__ , type = 'string')
	elif MAYA_VERSION == '2022':
		meta_node.setAttribute('Base_Name'  , __name__ , type = 'string')
	else:
		meta_node.attr('Base_Name').value = '%s' %(__name__)


	meta_node.addAttribute( ln = 'length_AB', at = "double", k = True)
	meta_node.addAttribute( ln = 'length_A', at = "double", k = True)
	meta_node.addAttribute( ln = 'length_B', at = "double", k = True)
	meta_node.addAttribute( ln = 'length_C', at = "double", k = True)
	meta_node.addAttribute( dataType = 'string' , longName = 'loc_grp')

	mc.setAttr('{0}.length_AB'.format(meta_node.name), length_AB)
	mc.setAttr('{0}.length_C'.format(meta_node.name), xLength)
	mc.setAttr('{0}.length_B'.format(meta_node.name), mag(vec_BC))
	mc.setAttr('{0}.length_A'.format(meta_node.name), mag(vec_AB))


	meta_node.setAttribute('loc_grp', loc_check_grp.name, type = 'string')
	meta_node.setAttribute('Side', side, type = 'string')

	#... connect value by manual

	mc.connectAttr( ikhName + '.message', meta_node.name + '.Rig_Prior' )


	'''
	meta_node = mc.createNode ('network', n = '%s_distance_meta' % name )
	mc.addAttr( meta_node, ln = 'length_AB', at = "double", k = True )
	mc.addAttr( meta_node, ln = 'length_B', at = "double", k = True )
	mc.addAttr( meta_node, ln = 'length_C', at = "double", k = True )

	mc.setAttr('{0}.length_AB'.format(meta_node), length_AB)
	mc.setAttr('{0}.length_C'.format(meta_node), xLength)
	'''


	#-----------------------------------------------------------------------------------------------------------------------------#
	#create the dSoft and softIK attributes on the controller
	#mc.addAttr( ctrlName, ln = 'dSoft', at = "double", min = 0.001, max = 2, dv = 0.001, k = True )
	#mc.addAttr( ctrlName, ln = 'softIK', at = "double", min = 0, max = 20, dv = 0, k = True )
	soft_ctrl = core.Dag(ctrlName)
	soft_ctrl.addAttribute( longName = 'SoftIk', niceName = 'SoftIk' , at ='enum' , en = '###'  , keyable = True)

	mc.addAttr( ctrlName, ln = 'dSoft', at = "double", min = 0.001, max = 4, dv = 0.001, k = True )
	mc.addAttr( ctrlName, ln = 'softIK', at = "double", min = 0, max = 40, dv = 0, k = True )
	# try
	#mc.addAttr( ctrlName, ln = 'dist_val', at = "double", min = 0, max = 20, dv = 0, k = True )
	#mc.addAttr( ctrlName, ln = 'soft_val', at = "double", min = 0, max = 20, dv = 0, k = True )


	#make softIK drive dSoft
	'''
	mc.setDrivenKeyframe( '%s.dSoft' % ctrlName, currentDriver = '%s.softIK' % ctrlName )
	mc.setAttr( '%s.softIK' % ctrlName, 20 )
	mc.setAttr( '%s.dSoft' % ctrlName, 2 )
	mc.setDrivenKeyframe( '%s.dSoft' % ctrlName, currentDriver = '%s.softIK' % ctrlName )
	mc.setAttr( '%s.softIK' % ctrlName, 0 )
	'''

	mc.setDrivenKeyframe( '%s.dSoft' % ctrlName, currentDriver = '%s.softIK' % ctrlName )
	mc.setAttr( '%s.softIK' % ctrlName, inputMax )
	mc.setAttr( '%s.dSoft' % ctrlName, outputMax )
	mc.setDrivenKeyframe( '%s.dSoft' % ctrlName, currentDriver = '%s.softIK' % ctrlName )
	mc.setAttr( '%s.softIK' % ctrlName, 0 )


	#lock and hide dSoft
	#... unhide
	mc.setAttr( '%s.dSoft' % ctrlName, lock = True, keyable = False, cb = False )
	#-----------------------------------------------------------------------------------------------------------------------------#   	
	#set up node network for soft IK
	mc.createNode ('plusMinusAverage', n = '%s_da_pma' % name )
	mc.createNode ('plusMinusAverage', n = '%s_x_minus_da_pma' % name )
	mc.createNode ('multiplyDivide', n = '%s_negate_x_minus_md' % name )
	mc.createNode ('multiplyDivide', n = '%s_divBy_dSoft_md' % name )
	mc.createNode ('multiplyDivide', n = '%s_pow_e_md' % name )
	mc.createNode ('plusMinusAverage', n = '%s_one_minus_pow_e_pma' % name )
	mc.createNode ('multiplyDivide', n = '%s_times_dSoft_md' % name )
	mc.createNode ('plusMinusAverage', n = '%s_plus_da_pma' % name )
	mc.createNode ('condition', n = '%s_da_cond' % name )
	mc.createNode ('plusMinusAverage', n = '%s_dist_diff_pma' % name )
	mc.createNode ('plusMinusAverage', n = '%s_defaultPos_pma' % name )

	#set operations
	mc.setAttr ('%s_da_pma.operation' % name, 2 )
	mc.setAttr ('%s_x_minus_da_pma.operation' % name, 2 )
	mc.setAttr ('%s_negate_x_minus_md.operation' % name, 1 )
	mc.setAttr ('%s_divBy_dSoft_md.operation' % name, 2 )
	mc.setAttr ('%s_pow_e_md.operation' % name, 3 )
	mc.setAttr ('%s_one_minus_pow_e_pma.operation' % name, 2 )
	mc.setAttr ('%s_times_dSoft_md.operation' % name, 1 )
	mc.setAttr ('%s_plus_da_pma.operation' % name, 1 )
	mc.setAttr ('%s_da_cond.operation' % name, 5 )
	mc.setAttr ('%s_dist_diff_pma.operation' % name, 2 )
	mc.setAttr ('%s_defaultPos_pma.operation' % name, 2 )
	if( ( upAxis == 'X' ) and ( defPos > 0 ) ):
		mc.setAttr ('%s_defaultPos_pma.operation' % name, 1 )
	if( upAxis == 'Y'):
		mc.setAttr ('%s_defaultPos_pma.operation' % name, 2 )
	if( ( upAxis == 'Z' ) and ( defPos < 0 ) ):
		mc.setAttr ('%s_defaultPos_pma.operation' % name, 1 )

	#-----------------------------------------------------------------------------------------------------------------------------#   	
	#make connections
	mc.setAttr( '%s_da_pma.input1D[0]' % name, length_AB )#... assign length_AB
	mc.connectAttr( '%s.dSoft' % ctrlName, '%s_da_pma.input1D[1]' % name )


	mc.connectAttr('{0}.length_AB'.format(meta_node), '{0}_da_pma.input1D[0]'.format(name))

	mc.connectAttr( '%s_x_distance.distance' % name, '%s_x_minus_da_pma.input1D[0]' % name )
	mc.connectAttr( '%s_da_pma.output1D' % name, '%s_x_minus_da_pma.input1D[1]' % name )

	mc.connectAttr( '%s_x_minus_da_pma.output1D' % name, '%s_negate_x_minus_md.input1X' % name )
	mc.setAttr( '%s_negate_x_minus_md.input2X' % name, -1 )

	mc.connectAttr( '%s_negate_x_minus_md.outputX' % name, '%s_divBy_dSoft_md.input1X' % name )
	mc.connectAttr( '%s.dSoft' % ctrlName, '%s_divBy_dSoft_md.input2X' % name )

	mc.setAttr( '%s_pow_e_md.input1X' % name, 2.718281828 )
	mc.connectAttr( '%s_divBy_dSoft_md.outputX' % name, '%s_pow_e_md.input2X' % name )

	mc.setAttr( '%s_one_minus_pow_e_pma.input1D[0]' % name, 1 )
	mc.connectAttr( '%s_pow_e_md.outputX' % name, '%s_one_minus_pow_e_pma.input1D[1]' % name )

	mc.connectAttr('%s_one_minus_pow_e_pma.output1D' % name, '%s_times_dSoft_md.input1X' % name )
	mc.connectAttr( '%s.dSoft' % ctrlName, '%s_times_dSoft_md.input2X' % name )

	mc.connectAttr( '%s_times_dSoft_md.outputX' % name, '%s_plus_da_pma.input1D[0]' % name )
	mc.connectAttr( '%s_da_pma.output1D' % name, '%s_plus_da_pma.input1D[1]' % name )

	mc.connectAttr( '%s_da_pma.output1D' % name, '%s_da_cond.firstTerm' % name )
	mc.connectAttr( '%s_x_distance.distance' % name, '%s_da_cond.secondTerm' % name )
	mc.connectAttr( '%s_x_distance.distance' % name, '%s_da_cond.colorIfFalseR' % name )
	mc.connectAttr( '%s_plus_da_pma.output1D' % name, '%s_da_cond.colorIfTrueR' % name )

	mc.connectAttr( '%s_da_cond.outColorR' % name, '%s_dist_diff_pma.input1D[0]' % name )
	mc.connectAttr( '%s_x_distance.distance' % name, '%s_dist_diff_pma.input1D[1]' % name )



	#... no need to compensage default position
	mc.setAttr( '%s_defaultPos_pma.input1D[0]' % name, 0 )
	#... wee will offset later
	# mc.setAttr( '%s_defaultPos_pma.input1D[0]' % name, defPos )






	# -------------------------------------- Test Circle Start
	mc.connectAttr( '%s_dist_diff_pma.output1D' % name, '%s_defaultPos_pma.input1D[1]' % name )

	# mc.connectAttr('%s_defaultPos_pma.output1D' % name, '%s.translate%s' % (ikhName, upAxis) ) # < < < this line cause an cycle

	


	# -------------------------------------- 
	# mc.connectAttr( '%s_dist_diff_pma.output1D' % name, '%s.translate%s' % (ikhName, upAxis) )

	# -------------------------------------- Test Circle End








	#--------------------------------------- Noman edit for compath with stretchy ----------------------------------------------------------#

	#... Create multi double linear
	if side == 'LFT':
		multiplier = -1
	else:
		multiplier = 1


	negative_val = core.MDLWithMul(name = '{0}_neg_mdl'.format(name), dv = multiplier)


	

	#... Create condition
	result_cnd = core.Condition(name = '{0}_result_cnd'.format(name))

	result_cnd.attr('colorIfFalseR').value = 0

	#... Create switch condition for prevent unexpected shift ikh
	softSwitch_cnd = core.Condition(name = '{0}_switch_cnd'.format(name))
	softSwitch_cnd.attr('colorIfFalseR').value = 0
	softSwitch_cnd.attr('operation').value = 2


	
	#... Circle warning here
	#... Connect
	# mc.connectAttr('%s.output ' %negative_val.name, '%s.colorIfTrueR' %result_cnd.name, f = True)
	mc.connectAttr('%s.output ' %negative_val.name, '%s.colorIfTrueR' %softSwitch_cnd.name, f = True)
	mc.connectAttr('%s.outColorR' %softSwitch_cnd.name, '%s.colorIfTrueR' %result_cnd.name, f = True)
	mc.connectAttr('%s.softIK ' %ctrlName, '%s.firstTerm' %softSwitch_cnd.name, f = True)






	mc.connectAttr('%s_defaultPos_pma.output1D' % name, '%s.input1' %negative_val.name )
	

	mc.connectAttr('%s.autoStretch ' %ctrlName, '%s.firstTerm' %result_cnd.name, f = True)




	mc.connectAttr('%s.outColorR' %result_cnd.name, '%s.translate%s' % (ikhName, upAxis), f = True)

	# parent later
	misc.snapPointConst(joints[2], '%s_end_dist_loc'%name)
	offset_parCons = core.pointConstraint( ctrlName , '%s_end_dist_loc' % name , mo = True)



	if priorMeta:

		priorMeta.attr('message') >> meta_node.attr('Rig_Prior')

		# connectAttr -f LegfkIkTwistRigLFT_meta.message softIkLFT_leg_distance_meta.Rig_Prior;


	meta_node.lockAllAttr()
	print('\n#------------------------------ End of softIK Function ---------------------------------------------------#')
	return meta_node.name
	
