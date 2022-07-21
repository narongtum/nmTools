# Untimate Switch local IK auto create
import maya.cmds as mc
giveSide = 'LFT','RGT'
sys = 'hand'
#sys = 'ankle'
headGrp = 'space_IK_grp'
giveGrp = 'world','neck','chest','cog'
giveCtrl = 'placement','neck','spine04','cog'


mc.group(n= headGrp, em=1)
mc.parent(headGrp,'ikh_grp')
for s in range(len(giveSide)):
    side = giveSide[s]

    IK = sys + 'Ik' + side + '_ctrl'

    mc.addAttr( IK, longName = "space", at = 'enum', keyable=True , en = "world:neck:chest:cog")
    for i in range(len(giveGrp)):
        # Create Name
        localGrp = giveGrp[i]
        name = sys + side + '_IK' + '_' + localGrp
        zro = sys + 'Ik' + side + 'Zro_grp'
        IKctrl = sys + 'Ik' + side + '_ctrl'
        ctrl = giveCtrl[i] + '_ctrl'
        grp = name + '_grp'
        con = name + '_con'
        pCon = zro + '_parentConstraint1'
        pConAttr = pCon + '.' + grp + 'W%d' %i

        # Function
        mc.group(n=grp, em=1)
        mc.parent(grp,headGrp)
        # snap
        mc.parentConstraint(zro,grp,mo=0,w=1)
        mc.delete(grp + '_parentConstraint1')
        # body -> grp
        mc.parentConstraint(ctrl,grp,mo=1,w=1)
        # grp -> zro
        mc.parentConstraint(grp,zro,mo=1,w=0)
        # Create Node and connect
        mc.createNode('condition',n=con)
        
        mc.setAttr(con + '.firstTerm',i)
        mc.setAttr(con + '.colorIfTrueR',1)
        mc.setAttr(con + '.colorIfFalseR',0)
        mc.connectAttr(IKctrl + '.space' ,con + '.secondTerm')
        mc.connectAttr(con + '.outColor.outColorR', pConAttr)
        
        
        
        
        