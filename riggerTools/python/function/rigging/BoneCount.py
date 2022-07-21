Sel = len(mc.ls(sl = True))
if Sel == 0: # IF THIRE NO SELCTION
    if mc.joint('Root' , exists = True):
        mc.select('Root',hi=True)
        amountJnt = len(mc.ls(sl = True))
        amoutBindJnt = len(mc.ls('*bind_jnt'))
        numJnt = 'NUMBER OF JOINT >>> %d' %amountJnt
        bindJnt = 'BIND JOINT >>> %d' %amoutBindJnt
        mc.select(cl=True)
        print numJnt
        print bindJnt
    else:
        print 'No Object Select'
    
else:
    mc.select(hi=True)
    amountJnt = len(mc.ls(sl = True))
    amoutBindJnt = len(mc.ls('*bind_jnt'))
    numJnt = 'NUMBER OF JOINT >>> %d' %amountJnt
    bindJnt = 'BIND JOINT >>> %d' %amoutBindJnt
    mc.select(cl=True)
    print numJnt
    print bindJnt
    
    
