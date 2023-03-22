import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

import math
#... find magnitude
def mag( v ):
	return( math.sqrt( pow( v[0], 2) + pow( v[1], 2) + pow( v[2], 2)))

upAxis = 2
primaryAxis = 2 
ikhName= 'ankleIkRGT_ikh'# ikhNam
side = 'RGT' #side
region = 'leg' #region
ctrlName = 'footIkRGT_ctrl' # lowerIk_ctrl.name
inputMax = 40
outputMax = 4








name = 'softIk{0}_{1}'.format(side, region)
stretch = False

#primary axis options
if( primaryAxis == 1):
	primaryAxis = 'X'
if( primaryAxis == 2):
	primaryAxis = 'Y'
if( primaryAxis == 3):
	primaryAxis = 'Z'



#finds name for joints
startJoint = mc.listConnections( ikhName + ".startJoint" )
endEffector = mc.listConnections( ikhName + ".endEffector" )
endJoint = mc.listConnections( endEffector, d = False, s = True )

#selects joint chain effected by IKH
mc.select( startJoint, hi = True )
mc.select( endJoint, hi = True, d = True )
mc.select( endEffector, d = True )
mc.select( endJoint, tgl = True )

#lists the joints
joints = []
joints = mc.ls( sl = True )
n = len(joints)
#------------------ Filter something not joint -------------------------------------------------------------------#
for each in range(n):
    print(each)
    
    if mc.nodeType(joints[each]) != 'joint':
        del_lana = each

# remove unwanted         
joints.pop(del_lana)        
n = len(joints)        




#gives position value for joints
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
#find the dchain = sum of bone lengths
i = 0
dChain = 0
while ( i < n - 1 ):
	a = mc.xform( joints[i], q = True, piv = True, ws = True )
	b = mc.xform( joints[ i + 1 ], q = True, piv = True, ws = True )
	x = b[0] - a[0]
	y = b[1] - a[1]
	z = b[2] - a[2]
	v = [x,y,z]
	dChain += mag(v)
	i += 1


print('\ndChain is: {0}'.format(dChain))

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
#-----------------------------------------------------------------------------------------------------------------------------#
#create the distance node, otherwise know as x(distance between root and ik)
mc.spaceLocator( n = '%s_start_dist_loc' % name )
mc.xform( '%s_start_dist_loc' % name, t = fPoints, ws = True )
mc.spaceLocator( n = '%s_end_dist_loc' % name )
mc.xform( '%s_end_dist_loc' % name, t = lPoints, ws = True )

mc.select( ctrlName, '%s_end_dist_loc' % name, r = True )
mc.parentConstraint( w = 1, mo = True)
# mc.select( joints[0], '%s_start_dist_loc' % name, r = True )
# mc.parentConstraint( w = 1, mo = True)

mc.createNode( 'distanceBetween', n = '%s_x_distance' % name )
mc.connectAttr( '%s_start_dist_loc.translate' % name, '%s_x_distance.point1' % name )
mc.connectAttr( '%s_end_dist_loc.translate' % name, '%s_x_distance.point2' % name )



xLength = mc.getAttr('%s_x_distance.distance'%name)
print('\nxLength is: {0}'.format(xLength))

#---------------------------------------- Create meta node -----------------------------------------------------------#
from function.rigging.autoRig.base import core
reload(core)
meta_node = core.MetaGeneric('%s_distance' %name)
meta_node.attr('Base_Name').value = 'L_softIK'
meta_node.addAttribute( ln = 'dChain', at = "double", k = True)
meta_node.addAttribute( ln = 'aChain', at = "double", k = True)
meta_node.addAttribute( ln = 'bChain', at = "double", k = True)
meta_node.addAttribute( ln = 'xChain', at = "double", k = True)
mc.setAttr('{0}.dChain'.format(meta_node.name), dChain)
mc.setAttr('{0}.xChain'.format(meta_node.name), xLength)
mc.setAttr('{0}.bChain'.format(meta_node.name), mag(vec_BC))
mc.setAttr('{0}.aChain'.format(meta_node.name), mag(vec_AB))
#... connect value by manual
mc.connectAttr( ikhName + '.message', meta_node.name + '.Rig_Prior' )


'''
meta_node = mc.createNode ('network', n = '%s_distance_meta' % name )
mc.addAttr( meta_node, ln = 'dChain', at = "double", k = True )
mc.addAttr( meta_node, ln = 'bChain', at = "double", k = True )
mc.addAttr( meta_node, ln = 'xChain', at = "double", k = True )

mc.setAttr('{0}.dChain'.format(meta_node), dChain)
mc.setAttr('{0}.xChain'.format(meta_node), xLength)
'''


#-----------------------------------------------------------------------------------------------------------------------------#
#create the dSoft and softIK attributes on the controller
#mc.addAttr( ctrlName, ln = 'dSoft', at = "double", min = 0.001, max = 2, dv = 0.001, k = True )
#mc.addAttr( ctrlName, ln = 'softIK', at = "double", min = 0, max = 20, dv = 0, k = True )
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
mc.setAttr( '%s_da_pma.input1D[0]' % name, dChain )#... assign dChain
mc.connectAttr( '%s.dSoft' % ctrlName, '%s_da_pma.input1D[1]' % name )


mc.connectAttr('{0}.dChain'.format(meta_node), '{0}_da_pma.input1D[0]'.format(name))

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

mc.connectAttr( '%s_dist_diff_pma.output1D' % name, '%s_defaultPos_pma.input1D[1]' % name )

mc.connectAttr('%s_defaultPos_pma.output1D' % name, '%s.translate%s' % (ikhName, upAxis) )
#--------------------------------------- Noman edit for compath with stretchy ----------------------------------------------------------#

#... Create multi double linear
if side == 'LFT':
	multiplier = -1
else:
	multiplier = 1


negative_val = core.MDLWithMul(name = '{0}_neg_mdl'.format(name), dv = multiplier)

# create condition
result_cnd = core.Condition(name = '{0}_result_cnd'.format(name))

result_cnd.attr('colorIfFalseR').value = 0



mc.connectAttr('%s_defaultPos_pma.output1D' % name, '%s.input1' %negative_val.name )
mc.connectAttr('%s.output ' %negative_val.name, '%s.colorIfTrueR' %result_cnd.name, f = True)

mc.connectAttr('%s.autoStretch ' %ctrlName, '%s.firstTerm' %result_cnd.name, f = True)

mc.connectAttr('%s.outColorR' %result_cnd.name, '%s.translate%s' % (ikhName, upAxis), f = True)
#-----------------------------------------------------------------------------------------------------------------------------#