#... try to run by line

import maya.cmds as mc
from function.rigging.autoRig.base import core
from function.rigging.autoRig.base import rigTools
from function.rigging.util import misc as misc
from function.rigging.autoRig.bodyRig import midLockModule
from function.rigging.autoRig.bodyRig import createIKStretch as create
from function.rigging.tools import proc as pc
import logging

from function.framework.reloadWrapper import reloadWrapper as reload
#... Reload modules
reload(core)
reload(rigTools)
reload(misc)

logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


nameSpace=''
parentTo='ctrl_grp'
side='LFT'
tmpJnt=(
	'upLegBackLFT_tmpJnt', 'midLegBackLFT_tmpJnt', 'ankleBackLFT_tmpJnt',
	'legPovBackLFT_tmpJnt', 'ballRollBackLFT_tmpJnt', 'toeRollBackLFT_tmpJnt',
	'heelRollBackLFT_tmpJnt', 'footOutBackLFT_tmpJnt', 'footInBackLFT_tmpJnt', 'lowLegBackLFT_tmpJnt'
)
priorJnt='hip_bJnt'
ikhGrp='ikh_grp'
noTouchGrp='noTouch_grp'
nullGrp='snapNull_grp'
showInfo=False
ribbon=True
ribbonRes='low'
ribbonName=('upLeg', 'lwrLeg')
charScale=1
region='backLeg'
alongAxis='y'
povShape='sphereAxis'
doubleIK=('L_hip_pxyJnt', 'L_knee_pxyJnt', 'L_ankle_pxyJnt')


# Check for doubleIK argument
if doubleIK is None:
	mc.error('The "doubleIK" argument is required for QuadrupedLegRig doubleIK setup. Please specify the doubleIK settings.')
	#return

core.makeHeader('Start of %s%s Rig' % ('QuadrupedLegRig', side))


hip = core.Dag(tmpJnt[0])
knee = core.Dag(tmpJnt[1])
hock = core.Dag(tmpJnt[9])
ankle = core.Dag(tmpJnt[2])
pov = core.Dag(tmpJnt[3])
ball = core.Dag(tmpJnt[4])
toe = core.Dag(tmpJnt[5])


# Create Main Joint Chain (Hip -> Knee -> Hock -> Ankle)
hip_ikJnt = rigTools.jointAt(hip)
knee_ikJnt = rigTools.jointAt(knee)
hock_ikJnt = rigTools.jointAt(hock)
ankle_ikJnt = rigTools.jointAt(ankle)
ball_ikJnt = rigTools.jointAt(ball)
toe_ikJnt = rigTools.jointAt(toe)

# Naming
rawName = []
for each in [tmpJnt[0], tmpJnt[1], tmpJnt[9], tmpJnt[2], tmpJnt[3], tmpJnt[4], tmpJnt[5]]:
	tmp = each.split('_')[0][:-3]
	rawName.append(tmp)
	

# Naming ikJnt
hip_ikJnt.name =   rawName[0] + side + '_ikJnt'
knee_ikJnt.name =   rawName[1] + side + '_ikJnt'
hock_ikJnt.name =   rawName[2] + side + '_ikJnt'
ankle_ikJnt.name =   rawName[3] + side + '_ikJnt'
ball_ikJnt.name =   rawName[4] + side + '_ikJnt'
toe_ikJnt.name =   rawName[5] + side + '_ikJnt'





# Parenting Main Chain
knee_ikJnt.parent(hip_ikJnt)
hock_ikJnt.parent(knee_ikJnt)
ankle_ikJnt.parent(hock_ikJnt)
ball_ikJnt.parent(ankle_ikJnt)
toe_ikJnt.parent(ball_ikJnt)


# Create Proxy Joint Chain (Hip -> Knee -> Ankle)
# User provides specific placement for Double IK in doubleIK argument
# doubleIK = [upLegDoubleIk, midLegDoubleIk, ankleDoubleIk]

if len(doubleIK) < 3:
	mc.error('The "doubleIK" argument must contain at least 3 joints: [Hip, Knee, Ankle].')

dIk_hip = core.Dag(doubleIK[0])
dIk_knee = core.Dag(doubleIK[1])
dIk_ankle = core.Dag(doubleIK[2])

pxyHip_pxyJnt = rigTools.jointAt(dIk_hip)
pxyKnee_pxyJnt = rigTools.jointAt(dIk_knee)
pxyAnkle_pxyJnt = rigTools.jointAt(dIk_ankle)

pxyHip_pxyJnt.name = 'proxy' + rawName[0] + side + '_pxyJnt'
pxyKnee_pxyJnt.name = 'proxy' + rawName[1] + side + '_pxyJnt'
pxyAnkle_pxyJnt.name = 'proxy' + rawName[3] + side + '_pxyJnt'

# Parenting Proxy Chain
pxyKnee_pxyJnt.parent(pxyHip_pxyJnt)
pxyAnkle_pxyJnt.parent(pxyKnee_pxyJnt)

# Orient joints for proxy chain (Standard Y-axis down the bone)
# Check if dIk joints have orientation? Usually auto-rig re-orients.
#mc.select(pxyHip_pxyJnt.name, r=True)
#mc.joint(e=True, orientJoint='yzx', secondaryAxisOrient='yup', children=True, zeroScaleOrient=True)




#... IK1
# 2. Proxy Chain IK (Hip -> Ankle) - Use RP Solver
proxy_ikh = core.IkRp(startJoint=pxyHip_pxyJnt, endEffector=pxyAnkle_pxyJnt)
# proxy_ikh.name = rawName[0]  + side + 'Pxy_ikh'
proxy_ikh.name = 'ikHandle4'

proxy_ikh.eff = rawName[0]  + side + 'Pxy_eff'
#proxy_ikh.attr('v').value = 0






# Create IK Handles
#... IK2
# 1. Main Chain IK (Upper: Hip -> Hock) - Use RP Solver
# Note: In the text logic, it says "startJoint = hip, endEffector = hock"
main_ikh = core.IkRp(startJoint=hip_ikJnt, endEffector=hock_ikJnt)
# main_ikh.name = rawName[0] + side + '_ikh'
main_ikh.name = 'ikHandle5'
main_ikh.eff = rawName[0] + side + '_eff'
#main_ikh.attr('v').value = 0 # Hide it



#... IK3
# (Upper: Hock -> Ankle)
ball_ikh = core.IkRp(startJoint=hock_ikJnt, endEffector=ankle_ikJnt)
# ball_ikh.name = rawName[2] + side + '_ikh'
ball_ikh.name = 'ikHandle6'
ball_ikh.eff = rawName[2] + side + '_eff'
#ball_ikh.attr('v').value = 0 # Hide it


#... IK4
toe_ikh = core.DoIk( startJoint = ball_ikJnt , endEffector = toe_ikJnt , solverType = 'ikRPsolver' )
# toe_ikh.name = rawName[5] + side + '_ikh'
toe_ikh.name = 'ikHandle7'
toe_ikh.eff = rawName[5] + side + '_eff'
toe_ikh.attr('v').value = 1

'''

# Group for IKs
ik_grp = core.Null(nameSpace + 'ik' + side + '_grp')
main_ikh.parent(ik_grp)
proxy_ikh.parent(ik_grp)

if priorJnt:
	hip_ikJnt.parent(priorJnt) # Parent main chain to root
	# Proxy chain usually follows the main rig or a specific group, let's parent to the priorJnt for now or a specific group
	# For now, let's parent proxy chain start to the same parent as main chain
	# But usually proxy chain might need to be hidden and just drive things
	# pxyHip_pxyJnt.parent(priorJnt) # Actually, let's keep it separate or put it in a mechanism group
	pass

'''


#... Create controller

rootName = rawName[0]

colorSide = 'blue'
rootName =  rootName + 'Ik' + side
ikRoot = core.Dag(rootName + '_ctrl')
ikRoot.nmCreateController('cube_ctrlShape')

ikRoot.editCtrlShape( axis = charScale * 15.5 )
ikRoot.setColor(colorSide)
IkRootZro_grp = rigTools.zeroGroup( ikRoot )
IkRootZro_grp.name = rootName + 'Zro_grp'
IkRootZro_grp.snapPoint(hip_ikJnt)

ikRootGmbl_ctrl = core.createGimbal( ikRoot )
# ========== # constraint to bind joint
rootIk_parCons = core.parentConstraint( ikRootGmbl_ctrl ,hip_ikJnt, mo=True   )
rootIk_parCons.name = region + side + 'Jnt_parCons'


rootPxyIk_parCons = core.parentConstraint( ikRootGmbl_ctrl ,pxyHip_pxyJnt, mo=True   )
rootPxyIk_parCons.name = region +'Pxy' + side + 'Jnt_parCons'






#... hock ctrl
name = nameSpace + rawName[2] 
hock_ctrl = core.Dag( name +'Ik'+ side + '_ctrl' )
hock_ctrl.nmCreateController('cube_ctrlShape')
hock_ctrl.editCtrlShape( axis = charScale * 2.1 )
hock_ctrl.setColor(colorSide)

hockZro_grp = rigTools.zeroGroup( hock_ctrl )
hockZro_grp.name = rawName[2]  + 'Zro_grp'
hockZro_grp.snapPoint(hock)




#... ankle ctrl
name = nameSpace + rawName[3] 
ankle_ctrl = core.Dag( name +'Ik'+ side + '_ctrl' )
ankle_ctrl.nmCreateController('cube_ctrlShape')
ankle_ctrl.editCtrlShape( axis = charScale * 1.5 )
ankle_ctrl.setColor(colorSide)

ankleZro_grp = rigTools.zeroGroup( ankle_ctrl )
ankleZro_grp.name = rawName[3]  + 'Zro_grp'
ankleZro_grp.snapPoint(ankle)



#... create reverse ankle joint

ankleRev_ikJnt = rigTools.jointAt(ankle)
ballRev_ikJnt = rigTools.jointAt(ball)
ankleRev_ikJnt.name =  rawName[3]+'Rev' + side + '_ikJnt'
ballRev_ikJnt.name =  rawName[5]+'Rev' + side + '_ikJnt'
ankleRev_ikJnt.parent(ballRev_ikJnt)




#... IK5
ballRev_ikh = core.DoIk( startJoint = ballRev_ikJnt , endEffector = ankleRev_ikJnt , solverType = 'ikSCsolver' )
# ballRev_ikh.name = rawName[5] + side+'Rev' + '_ikh'
ballRev_ikh.eff = rawName[5] + side+'Rev' + '_eff'
ballRev_ikh.attr('v').value = showInfo 

ballRev_ikh.name = 'ikHandle8'


#... IK5
rootName = rawName[6]
colorSide = 'blue'
rootName =  rootName + 'Ik' + side
ikRoot = core.Dag(rootName + '_ctrl')
ikRoot.nmCreateController('cube_ctrlShape')

ikRoot.editCtrlShape( axis = charScale * 15.5 )
ikRoot.setColor(colorSide)
IkRootZro_grp = rigTools.zeroGroup( ikRoot )
IkRootZro_grp.name = rootName + 'Zro_grp'
IkRootZro_grp.snapPoint(ball)

ikRootGmbl_ctrl = core.createGimbal( ikRoot )
# ========== # constraint to bind joint
rootIk_parCons = core.parentConstraint( ikRootGmbl_ctrl ,hip_ikJnt, mo=True   )
rootIk_parCons.name = region + side + 'Jnt_parCons'












'''





# Create Controls

# Ankle IK Control
ctrlType = 'Ik'
part = nameSpace + region

# Position for Ankle Ctrl
ankle_ik_pos = core.Null(part + ctrlType + 'Ctrl' + side + '_grp')
ankle_ik_pos.snapPoint(ankle_ikJnt)

ankle_ik_ctrl = core.Dag(nameSpace + 'ANKLE' + '_IK_' + side + '_ctrl')
ankle_ik_ctrl.nmCreateController('cube_ctrlShape')
ankle_ik_ctrl.editCtrlShape(axis=charScale * 4.0)
ankle_ik_ctrl.setColor('yellow')

# Zero Group for Ankle Ctrl
ankle_ik_zro = rigTools.zeroGroup(ankle_ik_ctrl)
ankle_ik_zro.snap(ankle_ik_pos)

# Hock IK Control (This is the "bend" control for the double IK)
hock_ik_pos = core.Null(nameSpace + 'HOCK' + '_IK_' + side + '_pos')
hock_ik_pos.snap(pxyAnkle_pxyJnt) # Snap to proxy ankle (which is same pos as real ankle)

hock_ik_ctrl = core.Dag(nameSpace + 'HOCK' + '_IK_' + side + '_ctrl')
hock_ik_ctrl.nmCreateController('sphere_ctrlShape') # Changed shape for distinction
hock_ik_ctrl.editCtrlShape(axis=charScale * 1.5)
hock_ik_ctrl.setColor('yellow')

hock_ik_zro = rigTools.zeroGroup(hock_ik_ctrl)
hock_ik_zro.snap(hock_ik_pos)

# Parenting Controls
hock_ik_zro.parent(ankle_ik_ctrl) # Hock control moves with Ankle control
ankle_ik_zro.parent(parentTo)


# Double IK Logic - Connections

# 1. Proxy IK Handle follows Ankle Control
core.parentConstraint(ankle_ik_ctrl, proxy_ikh, mo=True)

# 2. Hock Control drives the Main IK Handle (Hip->Hock)
# But Hock Control position is relative to Ankle.
# The Main IK Handle needs to follow the Hock Control for translation?
# Wait, the text says: "This IK handle (Lower/Hock) should be constrained to... this top joint here (pointing to something?)"

# Re-reading the text/code logic carefully:
# "one IK Handle There (Main Chain Upper), one from here down to here (Main Chain Lower?)"

# Let's look at 01_quardpedRearLegRig_doubleIK_01_start_v001.py again.
# It has `main_ikh` (Hip->Hock).
# It has `proxy_ikh` (ProxyHip->ProxyAnkle).
# It has `HOCK_IK_CTRL` parented under `ANKLE_IK_CTRL`.
# It has `core.aimConstraint( HOCK_IK_CTRL , hock_ikJnt ... )` ?? No wait.

# "hock_aimCons = core.aimConstraint( pxyKnee_pxyJnt, hock_ik_pos ... )"
# The `hock_ik_pos` (which holds HOCK_IK_CTRL?) aims at the Proxy Knee?

# Key logic from 01...py:
# core.parentConstraint(HOCK_IK_CTRL, main_ikh, mo=True)
# core.parentConstraint(ANKLE_IK_CTRL, proxy_ikh, mo=True)

# So:
# Ankle Ctrl moves Proxy IK -> Proxy Chain moves.
# Hock Ctrl moves Main IK -> Main Chain moves.

# But how does Proxy Chain influence Main Chain?
# Usually, the "Hock" position is determined by the Proxy Chain's properties or just manual placement?
# In true Double IK, the mid-joint (Hock) of the main chain should try to align with the line between Knee and Ankle of the proxy chain?

# In the provided 01...py script, it seems simple:
# Main IK handle is parent constrained to HOCK_IK_CTRL.
# Proxy IK handle is parent constrained to ANKLE_IK_CTRL.
# But where does HOCK_IK_CTRL go? It's under ANKLE_IK_CTRL.
# So you move Ankle, everything moves. You can adjust Hock manually.

# Is there an automatic behavior?
# "hock_aimCons = core.aimConstraint( pxyKnee_pxyJnt, hock_ik_pos ... )"
# This aims the group holding the Hock Ctrl towards the Proxy Knee.
# This implies that as you move the Ankle, the Hock Control's *orientation* or *position* (if it was translation) changes?
# Aim constraint changes rotation.

# Let's replicate this specific logic from 01...py:

# Group for Hock IK aiming
# hock_ik_pos (Group) -> HOCK_IK_CTRL (Ctrl) -> HOCK_IK_Zro (Grp) ? No.
# Structure in 01...py:
# hock_ik_pos (Null) -> Parented to ANKLE_IK_CTRL
# HOCK_IK_CTRL (Dag) -> Parented to hock_ik_pos

# My structure:
# ankle_ik_ctrl
#   -> hock_ik_img_grp (The aiming group)
#       -> hock_ik_zro
#           -> hock_ik_ctrl

hock_ik_aim_grp = core.Null(nameSpace + 'HOCK' + '_IK_' + side + '_aim_grp')
hock_ik_aim_grp.snap(hock_ik_zro)
hock_ik_aim_grp.parent(ankle_ik_ctrl)
hock_ik_zro.parent(hock_ik_aim_grp)

# Aim Constraint:
# "hock_ik_pos grp aimcon >>>>> proxyKnee"
# Target: pxyKnee_pxyJnt
# Object: hock_ik_aim_grp
# WorldUp: ANKLE_IK_CTRL (Object Rotation)
core.aimConstraint(pxyKnee_pxyJnt, hock_ik_aim_grp, mo=False, 
				   aimVector=(0, 1, 0), upVector=(0, 0, 1), 
				   worldUpType="objectrotation", worldUpObject=ankle_ik_ctrl.name)
				   
# Constraints for IK Handles
core.parentConstraint(hock_ik_ctrl, main_ikh, mo=True)
core.parentConstraint(ankle_ik_ctrl, proxy_ikh, mo=True)


# POV (Pole Vector)
povZro_grp = core.Null(nameSpace + 'knee' + region + side + 'Zro_grp')
pov_ctrl_obj = core.Dag(nameSpace + 'POV' + '_' + side + '_ctrl')

if povShape == 'sphereAxis':
	pov_ctrl_obj.nmCreateController('legLFT_pov_ctrlShape')
elif povShape == 'pyramid':
	pov_ctrl_obj.nmCreateController('pyramid_ctrlShape')
	pov_ctrl_obj.rotateShape(rotate=(90, 0, 0))
	
pov_ctrl_obj.editCtrlShape(axis=charScale * 0.8)
pov_ctrl_obj.setColor('yellow')

povZro_grp.snap(pov)
pov_ctrl_obj.parent(povZro_grp)

# Pole Vector Constraints
# Main IK PV
core.poleVectorConstraint(pov_ctrl_obj, main_ikh)
# Proxy IK PV
core.poleVectorConstraint(pov_ctrl_obj, proxy_ikh)


# Cleanup
# Hide proxy joints?
pxyHip_pxyJnt.attr('v').value = 0

print('Include Double IK success!!')

'''