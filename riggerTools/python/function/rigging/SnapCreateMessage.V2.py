def MessageSetup():
    # Message Setup FOR SNAP IK TO FK POSE
    import maya.cmds as mc
    giveSide = 'LFT','RGT'
    for s in range(2): # for Arm Message Attr Setup
        side = giveSide[s]
        attrList = ['FKctrl', 'FKpov', 'IKctrl', 'IKpov', 'IKrot']
        itemList = ['hand'+side+'_bind_jnt','lowerArm' +side+ '_bind_jnt','hand' +side+ '_IK_ctrl','arm' +side+ '_pov_ctrl','hand' +side+ '_Wor_grp']
        ctrl = 'hand' + side + '_IK_ctrl'
        for i in range(len(attrList)):
            # Namming
            attr = attrList[i]
            item = itemList[i]
            # Create Message Attr 
            print ctrl
            print attr
            print item
            print '----'
            mc.addAttr(ctrl, at='message', ln = attr)
            # Connect Message to node
            mc.connectAttr(item + '.message', ctrl + '.' + attr)
    
    for s in range(2): # For Arm Message Attr Setup
        side = giveSide[s]
        attrList = ['FKctrl', 'FKpov', 'IKctrl', 'IKpov', 'IKrot']
        itemList = ['toes'+side+'_bind_jnt','lowerLeg' +side+ '_bind_jnt','foot' +side+ '_IK_ctrl','leg' +side+ '_pov_ctrl','foot' +side+ '_Wor_grp']
        ctrl = 'foot' + side + '_IK_ctrl'
        for i in range(len(attrList)):
            # Namming
            attr = attrList[i]
            item = itemList[i]
            # Create Message Attr 
            print ctrl
            print attr
            print item
            print '----'
            mc.addAttr(ctrl, at='message', ln = attr)
            # Connect Message to node
            mc.connectAttr(item + '.message', ctrl + '.' + attr)
    print 'Message Has Been Sent >>>> '
MessageSetup()