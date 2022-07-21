# Untimate CLOTH SWAP With Click
import maya.cmds as mc
sel = mc.ls(sl=True)
# NAME GIVING
mainCtrl = 'char_ctrl'
sepSel = sel[0].split('_')
frontName = sepSel[0]
endName = sepSel[1]

#mc.listConnections('maleFace01_pma.input2D', destination = 0)

#mc.attributeQuery('input2D[13].input2Dx', node = 'maleFace01_pma' , c =True)

#mc.connectAttr('rev_01.output.outputX','maleFace01_pma.input2D[13].input2Dx' )

if frontName == 'hat':
    giveType = ['hat','ub','lb','fw']
elif frontName == 'head':
    giveType = ['head','ub','lb','fw']
else:
    print 'Please Select Head or Hat'
    
#giveName = ['assasin01'] # ADD NAME
giveName = [endName] # SelectName
enAttr = 'none:all:' + giveType[0] + ':ub:lb:fw'

# Create Type List
for n in range(len(giveName)):
    name = giveName[n]
    mainAttr = mainCtrl + '.' + name
    set = 'cl_' + name
    ubCon = name + '_ub_con'
    lbCon = name + '_lb_con'
    colrFls = '.colorIfFalse.colorIfFalse'
    colrTru = '.colorIfTrue.colorIfTrue'
    colrOut = '.outColor.outColor'
    
    # add Attr
    mc.addAttr( mainCtrl, longName  = name, at = 'enum', keyable = True, en = enAttr)
    # Connect set Vis
    mc.connectAttr(mainAttr, set + '.v')
    # Create Node
    mc.createNode('condition', n = ubCon)
    mc.createNode('condition', n = lbCon)
    # Set Attr
    mc.setAttr(ubCon + '.secondTerm' ,1)
    mc.setAttr(lbCon + '.secondTerm' ,1)
    # Connect to Main
    mc.connectAttr(mainAttr, ubCon + '.firstTerm')
    mc.connectAttr(mainAttr, lbCon + '.firstTerm')

    for t in range(len(giveType)):
        type = giveType[t]
        armor =  type + '_' + name
        amrCon = armor + '_con'
        count = t+2
        # Create and Set Node
        mc.createNode('condition', n = amrCon)
        mc.setAttr(amrCon + '.secondTerm', count)
        giveChanel = ('R','G','B')
        for a in range(len(giveChanel)):
            chanel = giveChanel[a]
            mc.setAttr(amrCon + colrTru + chanel,1)
            mc.setAttr(amrCon + colrFls + chanel,0)
        # Let Connect
        mc.connectAttr(mainAttr, amrCon + '.firstTerm')
        # IF is TYPE
        if t <= 1 :
            allCon = ubCon
            if t == 0:
                colr = 'R'
            elif t == 1:
                colr = 'G'
            #elif t == 2:
                #colr = 'B'
        elif t >= 2:
            allCon = lbCon
            if t == 2:
                colr = 'R'
            elif t == 3:
                colr = 'G'
        # Let Connect IN
        mc.setAttr(allCon + colrTru + colr, 1)
        # Let Connect OUT
        mc.connectAttr(amrCon + colrOut + 'R', allCon + colrFls + colr)
        mc.connectAttr(set + '.v', allCon + colrTru + colr)
        mc.connectAttr(allCon + colrOut + colr,armor + '.v')
