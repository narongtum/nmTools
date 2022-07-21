def Snap(): # Create SNAP NULL GRP
    giveSYS = 'arm','leg'
    for i in range(len(giveSYS)):
        SYS = giveSYS[i]
        master = SYS + 'Rig_Snap_grp'
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
            if SYS == 'arm':
                nameGive = 'upperArm','lowerArm','hand'
            if SYS == 'leg':
                nameGive = 'upperLeg','lowerLeg','foot'
            for i in range(len(nameGive)): #LOCAL grp
                name = nameGive[i] + side
                jnt = name + '_bind_jnt'
                jntIK = name + '_IK_jnt'
                FK = name + '_FK_ctrl'
                IK = name + '_IK_ctrl'
                Loc = name + '_Loc_grp'
                null = name + '_Loc_null'
                pCons = '_parentConstraint1'
                grp = name + '_FK_Zro_grp'
                
                # Setup
                mc.group( em = True, n=Loc)
                mc.group( em = True, n=null)
                mc.parent( null,Loc)
                mc.parentConstraint( jnt, Loc, w=1, mo=0)
                mc.delete( Loc + pCons)
                # pCons From IK
                mc.parentConstraint( jntIK, null, w=1, mo=1)
    
                if i == 0:
                    if nameGive[0] == 'upperArm':
                        main = 'shoulder' + side + '_Loc_grp'
                        mainShd = 'shoulder' + side + '_bind_jnt'
                        mc.group( em=True, n=main)
                        mc.parentConstraint( mainShd, main, w=1, mo=0)
                        mc.delete(main + pCons)
                        mc.parent( main, master)
                        mc.parent( Loc, main)
                        mc.orientConstraint( grp, Loc, w=1, mo=1)
                    if nameGive[0] == 'upperLeg':
                        mc.parent( Loc, master)
                    
                if i > 0:
                    main = nameGive[i-1] + side + '_Loc_null'
                    mc.parent( Loc, main)               
                        
                        
            # WORLD grp
            if SYS == 'arm':
                name = 'hand' + side
            if SYS == 'leg':
                name = 'foot' + side
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