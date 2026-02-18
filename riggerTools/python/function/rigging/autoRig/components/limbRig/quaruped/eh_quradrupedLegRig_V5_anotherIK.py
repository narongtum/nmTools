#... Another multi IK method rear pow rig


import maya.cmds as mc
from function.rigging.autoRig.base import core
from function.rigging.autoRig.base import rigTools
from function.rigging.util import misc as misc
from function.rigging.autoRig.bodyRig import midLockModule
from function.rigging.autoRig.bodyRig import createIKStretch as create
from function.rigging.tools import proc as pc
import logging

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

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
showInfo=True
ribbon=True
ribbonRes='low'
ribbonName=('upLeg', 'lwrLeg')
charScale=1
region='backLeg'
alongAxis='y'
povShape='sphereAxis'
doubleIK=('L_hip_pxyJnt', 'L_knee_pxyJnt', 'L_ankle_pxyJnt')


core.makeHeader('Start of %s%s Rig' % ('QuadrupedLegRig', side))


color_part_dict = mnd.COLOR_part_dict


if side == 'LFT':
    colorSide = color_part_dict['left']   
elif side == 'RGT':
    colorSide = color_part_dict['right']
else:
    colorSide = color_part_dict['primary']






heel = core.Dag( tmpJnt[6])
footOut = core.Dag( tmpJnt[7])
footIn = core.Dag( tmpJnt[8])









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
ball_ikJnt.name =   rawName[5] + side + '_ikJnt'
toe_ikJnt.name =   rawName[6] + side + '_ikJnt'





# Parenting Main Chain
knee_ikJnt.parent(hip_ikJnt)
hock_ikJnt.parent(knee_ikJnt)
ankle_ikJnt.parent(hock_ikJnt)
ball_ikJnt.parent(ankle_ikJnt)
toe_ikJnt.parent(ball_ikJnt)






#... IK1  Thight -> Hock - Use RP Solver
hock_ikh = core.IkRp(startJoint=hip_ikJnt, endEffector=hock_ikJnt)
hock_ikh.name = rawName[0]  + side + '_ikh'
hock_ikh.eff = rawName[0]  + side + '_eff'
hock_ikh.attr('v').value = showInfo


#... IK2  Hock -> Ankle - Use SP Solver
ankle_ikh = core.DoIk( startJoint = hock_ikJnt , endEffector = ankle_ikJnt , solverType = 'ikSCsolver' )
ankle_ikh.name = rawName[2]  + side + '_ikh'
ankle_ikh.eff = rawName[2]  + side + '_eff'
ankle_ikh.attr('v').value = showInfo



#... IK3  Ankle -> Ball - Use SP Solver
ball_ikh = core.DoIk( startJoint = ankle_ikJnt , endEffector = ball_ikJnt , solverType = 'ikSCsolver' )
ball_ikh.name = rawName[5]  + side + '_ikh'
ball_ikh.eff = rawName[5]  + side + '_eff'
ball_ikh.attr('v').value = showInfo




#... IK4  Ball -> Toe - Use SP Solver
toe_ikh = core.DoIk( startJoint = ball_ikJnt , endEffector = toe_ikJnt , solverType = 'ikSCsolver' )
toe_ikh.name = rawName[6]  + side + '_ikh'
toe_ikh.eff = rawName[6]  + side + '_eff'
toe_ikh.attr('v').value = showInfo





# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# Check type is for animal or human
# Result : return string
# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

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












footBehav = [ 'footOut','footIn','heelRoll','toeRoll','ballRoll','ankle' ,'rollBackAnkle']

ctrlName = nameSpace + footBehav[5] + legType + 'IK' + side  
ankleIk_ctrl = core.Dag(ctrlName +  '_ctrl')
ankleIk_ctrl.nmCreateController( 'square_ctrlShape' )
ankleIk_ctrl.rotateShape( rotate = (90,90,0) )
ankleIk_ctrl.editCtrlShape( axis = charScale * 10 )
ankleIk_ctrl.setColor( colorSide )
# Create zero group
ankleIkZro_grp = rigTools.zeroGroup( ankleIk_ctrl )
ankleIkZro_grp.name = ctrlName + 'Zro_grp'
# Snap position
ankleIkZro_grp.snapPoint( ankle_ikJnt )





# Create ball roll controller
ctrlName = nameSpace + footBehav[4] +legType+ 'Ik'  + side
ballRoll_ctrl = core.Dag(ctrlName  + '_ctrl')
ballRoll_ctrl.nmCreateController( 'ballRoll%s_IK_ctrlShape' %side )
ballRoll_ctrl.editCtrlShape( axis = charScale * 1.25 )
ballRoll_ctrl.setColor('yellow')
# Create zero group
ballRollZro_grp = rigTools.zeroGroup( ballRoll_ctrl )
ballRollZro_grp.name = ctrlName + 'Zro_grp'



# Create footOut controller
ctrlName = nameSpace + footBehav[0] +legType+ 'IK'  + side 
footOut_ctrl = core.Dag(ctrlName+ '_ctrl')
footOut_ctrl.nmCreateController( 'sphere_ctrlShape' )
footOut_ctrl.editCtrlShape( axis = charScale * 1.25 )
footOut_ctrl.setColor('yellow')
# Create zero group
footOutZro_grp = rigTools.zeroGroup( footOut_ctrl )
footOutZro_grp.name = ctrlName + 'Zro_grp'



# Create footIn controller
ctrlName = nameSpace + footBehav[1]+legType+ 'IK'  + side 
footIn_ctrl = core.Dag(ctrlName + '_ctrl' )
footIn_ctrl.nmCreateController( 'sphere_ctrlShape' )
footIn_ctrl.editCtrlShape( axis = charScale * 1.25 )
footIn_ctrl.setColor('yellow')
# Create zero group
footInZro_grp = rigTools.zeroGroup( footIn_ctrl )
footInZro_grp.name = ctrlName + 'Zro_grp'



# Create footHeel controller
ctrlName = nameSpace + footBehav[2]  +legType+ 'IK' + side 
footHeel_ctrl = core.Dag(ctrlName + '_ctrl')
footHeel_ctrl.nmCreateController( 'sphere_ctrlShape'  )
footHeel_ctrl.editCtrlShape( axis = charScale * 1.25 )
footHeel_ctrl.setColor('yellow')
# Create zero group
footHeelZro_grp = rigTools.zeroGroup( footHeel_ctrl )
footHeelZro_grp.name =ctrlName  +  'Zro_grp'



# Create toeRoll controller
ctrlName = nameSpace + footBehav[3]  +legType+ 'IK' + side  
footToe_ctrl = core.Dag(ctrlName +  '_ctrl')
footToe_ctrl.nmCreateController( 'sphere_ctrlShape' )
footToe_ctrl.editCtrlShape( axis = charScale * 1.25 )
footToe_ctrl.setColor('yellow')
# Create zero group
footToeZro_grp = rigTools.zeroGroup( footToe_ctrl )
footToeZro_grp.name = ctrlName + 'Zro_grp'



# Snap each grp to joint prosition
footOutZro_grp.snap( footOut ) 
footInZro_grp.snap( footIn ) 
footHeelZro_grp.snap( heel ) 
ballRollZro_grp.snap( ball)
footToeZro_grp.snap( toe )





# Footin ---> footOut
footInZro_grp.parent( footOut_ctrl )
# Heel roll ---> footIn
footHeelZro_grp.parent( footIn_ctrl )
# Toe ---> Heel
footToeZro_grp.parent( footHeel_ctrl )
# Ball  ---> Toe
ballRollZro_grp.parent( footToe_ctrl )


