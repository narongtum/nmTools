import maya.cmds as mc
from function.animation.mirrorAnimation.mirror_animation_studiolib_axis import mirror_animation_pose


nameSpace = 'CH004_Shaman_Rig1'

a1=[-1, 1, 1]
a2=[1, -1, 1]
a3=[1, 1, -1]
a4=[-1, -1, -1]




mc.select('CH004_Shaman_Rig:cog_ctrl')
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a1)




mc.select('CH004_Shaman_Rig:spine01FK_ctrl')
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a1)






mc.select('CH004_Shaman_Rig:clvRGT_ctrl')
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a2)


mc.select('CH004_Shaman_Rig:armRGTIK_ctrl')
mirror_animation_pose(
    target_ns="CH004_Shaman_Rig1", 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a4,  
    auto_key=False
)





mc.select('CH004_Shaman_Rig:clvLFT_ctrl')
mirror_animation_pose(
    target_ns="CH004_Shaman_Rig1", 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a2,  
    auto_key=False
)


mc.select('CH004_Shaman_Rig:armLFTIK_ctrl')
mirror_animation_pose(
    target_ns="CH004_Shaman_Rig1", 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a4
)


#..... all strip
mc.select('CH004_Shaman_Rig:stripF01_ctrl')
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a1)


#..... all strip is a1
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a1)
    
    
 
#.....
mc.select('CH004_Shaman_Rig:footRGTIK_ctrl')
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a1)
    
    
    
mc.select('CH004_Shaman_Rig:footLFTIK_ctrl')
mirror_animation_pose(
    target_ns=nameSpace, 
    side_from="RGT", 
    side_to="LFT",
    mirror_axis=a1)   
    
    