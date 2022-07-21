#FK Finger Rig
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

charScale = mc.getAttr( 'template_ctrl.scaleX' )

def fingerRig( side = 'LFT', fingerNum = 3 , fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'] ):
    
    fGrp = 'finger%s_grp' %side
    fJnt = 'hand%s_tmpJnt' %side
    handJnt = 'hand%s_bJnt' %side
    mc.group( n = fGrp, em = 1)
    mc.parentConstraint( handJnt, fGrp, mo = 0, w = 1)
    
    
    for i in range(len(fingerName)): # create & parent [ bJnt ]
        for n in range(fingerNum):
            name = fingerName[i] + '%02d' %(n+1) + side
            tmpJnt = core.Dag( name + '_tmpJnt')
            bJnt = core.Dag( name + '_bJnt')
            jnt = rigTools.jointAt( tmpJnt )#create bJnt at tmpJnt
            jnt.rename( bJnt)
            
            if n > 0:
                upName = fingerName[i] + '%02d' %n + side
                upJnt = core.Dag(upName + '_bJnt')
                print 'more'
                bJnt.parent( upJnt )
            elif n == 0:
                bJnt.parent( handJnt )
                print 'start'
            
    for i in range(len(fingerName)):
        for n in range(fingerNum):
            name = fingerName[i] + '%02d' %(n+1) + side 
            tmpJnt = name + '_tmpJnt'
            bJnt = name + '_bJnt'
            
            if side == 'LFT':
                sideColor = 'red'
            elif side == 'RGT':
                sideColor = 'blue'
                
            ctrl = core.Dag( name + '_ctrl' ) # Create Ctrl
            ctrl.nmCreateController('circle_ctrlShape')
            
            ctrl.editCtrlShape( axis =  charScale*.3 )
            ctrl.color = sideColor
            
            zGrp = rigTools.zeroGroup( ctrl ) # Create zGrp
            zGrp.name = name + '_zGrp' 
            zGrp.matchAll( tmpJnt )

            if n > 0:
                upName = fingerName[i] + '%02d' %n + side
                upCtrl = core.Dag(upName + '_ctrl')
                zGrp.parent( upCtrl )
            
            elif n == 0: 
                zGrp.parent( fGrp )
                
            core.parentConstraint(ctrl,bJnt)
    return fGrp 
# EXAMPLE
handLFT = fingerRig( side = 'LFT', fingerNum = 3 , fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'] )
handRGT = fingerRig( side = 'RGT', fingerNum = 3 , fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'] )
mc.parent( handLFT, handRGT, 'RIG_GRP' )
