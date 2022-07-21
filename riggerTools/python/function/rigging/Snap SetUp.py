def Snap(): # Rig Snap Grp
    master = 'armRig_Snap_grp'
    mc.group( em=True, n=master)
    mc.parent(master, 'fly_ctrl')
    # LOCK and HIDE
    attrName = '.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz'
    for a in range(len(attrName)):
        attr = attrName[a]
        name = master
        mc.setAttr( name + attr, lock = True, keyable = False, channelBox = False)

    sideGive = 'LFT','RGT'
    for s in range(2):
        side = sideGive[s]
        nameGive = 'upperArm','lowerArm' ,'hand'
        for i in range(len(nameGive)): #LOCAL grp
            name = nameGive[i] + side
            jnt = name + '_bind_jnt'
            jntIK = name + '_IK_jnt'
            FK = name + '_FK_ctrl'
            IK = name + '_IK_ctrl'
            Loc = name + '_Loc_grp'
            pCons = '_parentConstraint1'
            
            # Setup
            mc.group( em = True, n=Loc)
            mc.parentConstraint( jnt, Loc, w=1, mo=0)
            mc.delete( Loc + pCons)
            mc.parent( Loc, master)
            # pCons From IK
            mc.parentConstraint( jntIK, Loc, w=1, mo=1)
            
        # WORLD grp
        name = 'hand' + side
        jnt = name + '_bind_jnt'
        IK = name + '_IK_ctrl'
        Wor = name + '_Wor_grp'
        Gimbal = name + '_FK_ctrl'
        pCons = '_parentConstraint1'
        mc.group( em = True, n=Wor)
        mc.parentConstraint( IK, Wor, w=1, mo=0)
        mc.delete( Wor + pCons)
        mc.parent( Wor, master)
        # pCons From IK
        mc.parentConstraint( Gimbal, Wor, w=1, mo=1)    
Snap()        