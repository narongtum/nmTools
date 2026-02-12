# 01_quardpedRearLegRig_doubleIK_01_start_v001

# find new method to rig animal back leg rig "digitigrade" leg

import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.pipeline import logger 
reload(logger)

class LegLogger(logger.MayaLogger):
	LOGGER_NAME = "digitigradeLegRig"


nameSpace = ''
priorJnt = ''
ribbon = False

nameSpace = nameSpace 		
parentTo = 'ctrl_grp' 		
side = 'LFT'			
region = 'backLeg'	
# get the temp joint	
tmpJnt = ('hipLFT_tmpJnt','kneeLFT_tmpJnt','hockLFT_tmpJnt','ankleLFT_tmpJnt','legPovBackLFT_tmpJnt')
pxyKneeJnt = 'proxyKneeLFT_tmpJnt'
priorJnt = ''			
ikhGrp = 'ikh_grp' 					
noTouchGrp = 'noTouch_grp' 			
nullGrp = 'snapNull_grp'			
showInfo = False  					
ribbon = ribbon						
ribbonRes = 'low'				
ribbonName = ('upFrontLeg', 'lwrFrontLeg')
charScale = 1






if len(tmpJnt) != 5:
	mc.error('the joint number is not match.')






hip = core.Dag( tmpJnt[0] )
knee = core.Dag( tmpJnt[1] )
hock = core.Dag( tmpJnt[2] )
ankle = core.Dag( tmpJnt[3] )
pov = core.Dag( tmpJnt[4] )

pxyKnee = core.Dag( pxyKneeJnt )
#pxyHip = core.Dag( tmpJnt[0] )
#pxyAnkle = core.Dag( tmpJnt[3] )

hipName = hip.makeRawName()
kneeName = knee.makeRawName()
hockName = hock.makeRawName()
ankleName = ankle.makeRawName()
povName = pov.makeRawName()

# Create joint at Hip
hip_ikJnt = rigTools.jointAt( hip )
knee_ikJnt = rigTools.jointAt( knee )
hock_ikJnt = rigTools.jointAt( hock )
ankle_ikJnt = rigTools.jointAt( ankle )


if 'Front' in tmpJnt[0]:
	print ('This is animal.')
	legType = 'frontLeg'
	position = 'Front'

elif 'Back' in tmpJnt[0]:
	legType = 'backLeg'
	position = 'Back'
	
else :
	print ('This is human Leg like.')
	legType = 'leg'
	


hip_ikJnt.name = nameSpace + hipName + side + '_ikJnt'
knee_ikJnt.name = nameSpace + kneeName + side + '_ikJnt'
hock_ikJnt.name = nameSpace + hockName + side + '_ikJnt'
ankle_ikJnt.name = nameSpace + ankleName + side +'_ikJnt'

# Parent it
knee_ikJnt.parent( hip_ikJnt )
hock_ikJnt.parent( knee_ikJnt )
ankle_ikJnt.parent( hock_ikJnt )





# proxy ik joint 
pxyKnee_pxyJnt = rigTools.jointAt( pxyKnee )
pxyHip_pxyJnt = rigTools.jointAt( hip )
pxyAnkle_pxyJnt = rigTools.jointAt( ankle )

pxyKneeName = pxyKnee.makeRawName()

pxyKnee_pxyJnt.name = nameSpace + pxyKneeName + side + '_pxyJnt'
pxyHip_pxyJnt.name = nameSpace + 'proxy'+ hipName + side + '_pxyJnt'
pxyAnkle_pxyJnt.name = nameSpace + 'proxy'+ ankleName + side +'_pxyJnt'


# Parent 
pxyKnee_pxyJnt.parent( pxyHip_pxyJnt )
pxyAnkle_pxyJnt.parent( pxyKnee_pxyJnt )

# set orient y along
mc.select(pxyHip_pxyJnt.name,r=True)
mc.joint(e=True, orientJoint = 'yzx', secondaryAxisOrient = 'yup', children=True, zeroScaleOrient=True)


# Set ikh
main_ikh = core.IkRp(	startJoint = hip_ikJnt ,endEffector = hock_ikJnt	)
main_ikh.name = hipName + side + '_ikh'
main_ikh.eff = hipName + side + '_eff'
main_ikh.attr('v').value = 1



# Set ikh of proxy
proxy_ikh = core.IkRp(	startJoint = pxyHip_pxyJnt ,endEffector = pxyAnkle_pxyJnt	)
proxy_ikh.name = hipName+ 'Proxy' + side + '_ikh'
proxy_ikh.eff = hipName + 'Proxy'+ side + '_eff'
proxy_ikh.attr('v').value = 1


ik_grp = core.Null( 'ik_grp')
main_ikh.parent(ik_grp)
proxy_ikh.parent(ik_grp)



part = 'leg'
ctrlType = 'Ik'
# Create ik rig grp
# part = nameSpace + legType
ankle_ik_pos = core.Null( part + ctrlType + 'Ctrl' + side + '_grp' )
ankle_ik_pos.snapPoint( ankle_ikJnt )
# ankle_ik_pos.parent( legRig_grp )


# lowerLegIK_ctrl = core.Dag( name +'Ik'+ side + '_ctrl' )
ANKLE_IK_CTRL = core.Dag('ANKLE_IK_CTRL')
ANKLE_IK_CTRL.nmCreateController('circle_ctrlShape')

ANKLE_IK_CTRL.snap(ankle_ik_pos)
ANKLE_IK_CTRL.parent(ankle_ik_pos)




hock_ik_pos = core.Null( 'hock_ik_pos')
hock_ik_pos.snap( pxyAnkle_pxyJnt )

HOCK_IK_CTRL = core.Dag('HOCK_IK_CTRL')
HOCK_IK_CTRL.nmCreateController('cube_ctrlShape')
HOCK_IK_CTRL.snap( hock_ik_pos )
HOCK_IK_CTRL.parent(hock_ik_pos)

hock_ik_pos.parent(ANKLE_IK_CTRL)





# make hock_ik_pos grp  aimcon >>>>>  proxyKnee   , ANKLE_IK_CTRL is world up
hock_aimCons = core.aimConstraint( pxyKnee_pxyJnt, hock_ik_pos, mo = False , aimVector = (0,1,0) ,upVector = (0,0,1)  ,worldUpType = "objectrotation", worldUpObject = ANKLE_IK_CTRL.name )





core.aimConstraint( HOCK_IK_CTRL , hock_ikJnt , mo = True , aimVector = (0,1,0) ,upVector = (0,0,1)  ,worldUpType = "objectrotation", worldUpObject = ANKLE_IK_CTRL.name )


# now create constraint for ikh as usual
core.parentConstraint(HOCK_IK_CTRL, main_ikh,mo=True)

core.parentConstraint(ANKLE_IK_CTRL, proxy_ikh,mo=True)


povZro_grp = core.Null( nameSpace + 'knee' + legType.capitalize() + side + 'Zro_grp' )
# Create POV Controller
name = nameSpace + povName + legType.capitalize() + side
pov_ctrl = core.Dag( name + '_ctrl' )
pov_ctrl.nmCreateController('legLFT_pov_ctrlShape')
pov_ctrl.editCtrlShape( axis = charScale * 0.8 )
pov_ctrl.setColor('yellow')

mc.parent( pov_ctrl.name , povZro_grp  )
# Snap with orient and prosition
povZro_grp.snap(pov)


core.poleVectorConstraint( pov_ctrl , main_ikh )