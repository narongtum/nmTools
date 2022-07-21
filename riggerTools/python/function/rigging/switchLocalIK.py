# Untimate Switch local IK auto create
import maya.cmds as mc

# crate dropdown
giveSide = 'LFT','RGT'
sys = 'hand'
headGrp = 'local_IK_grp'

# for EH project
#giveGrp = 'world','neck','chest','cog'

giveGrp = 'world','head','neck','chest','cog'
#giveCtrl = 'fly','head','neck','upperChest','cog'

# for EH project
giveCtrl = 'fly','neck','chest','cog'
mc.group(n= headGrp, em=1)
mc.parent(headGrp,'IK_ctrl_grp')
for s in range(len(giveSide)):
   side = giveSide[s]
   for i in range(len(giveGrp)):
       # Create Name
       localGrp = giveGrp[i]
       name = sys + side + '_IK' + '_' + localGrp
       zro = sys + side + '_IK_Zro_grp'
       IKctrl = sys + side + '_IK_ctrl'
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
       mc.connectAttr(IKctrl + '.localSwitch' ,con + '.secondTerm')
       mc.connectAttr(con + '.outColor.outColorR', pConAttr)