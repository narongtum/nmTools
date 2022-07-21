'''
Corrective Blendshape Model Sculpt Helper UI
Version 1.0
Created by Noah Alzayer
Last Modified 7/27/13
nalzay89@gmail.com
www.noahalzayer.net

To use- run win and go.
'''

import pymel.core as pm
from functools import partial
import na_bsCorrectiveSculpt
reload(na_bsCorrectiveSculpt)

def win(*args):
    
    win='bsCorrectiveWindow'
    
    if pm.window(win, q=True, exists=True):
        pm.deleteUI(win)
        if pm.window(win, q=True, exists=True):
            pm.deleteUI(win)
    
    win=pm.window(win, t='Corrective Blendshape Model Helper', sizeable=False, rtf=True)
    
    mainLwt = pm.columnLayout(w=350)
    
    #Sculpt Frame
    pm.frameLayout('Sculpt', bgc=[0,0,0], bs='out', w=350)
    pm.text('To start, simply select the base mesh you wish to sculpt.\nPress "Start Sculpt". Once done, press "Extract Shape"')
    
    pm.rowColumnLayout(nc=2, cw=[(1,175), (2,170)])
    pm.separator(h=3, st='none')
    pm.separator(h=3, st='none')
    
    pm.button('Start Sculpt', c=na_bsCorrectiveSculpt.cbsStart)
    pm.button('Extract Shape', c=na_bsCorrectiveSculpt.cbsTrans)
    pm.separator(st='none', h=10)
    
    #Utilities Frame
    pm.frameLayout('Other Utilities', bgc=[0,0,0], p=mainLwt, cll=True, cl=True, bs='in', w=350)
    colLwt = pm.columnLayout(rs=5, adj=True)
    
    #Clear Tweaks Sub-frame
    pm.frameLayout('Clear Tweaks', p=colLwt, cll=True, cl=True)
    pm.separator(h=2, st='none')
    pm.button('Run', c=na_bsCorrectiveSculpt.clearTweaks)
    pm.separator(st='none')
    
    
    #Mirror Shape Sub-frame
    mirFrmLwt = pm.frameLayout('Mirror Shape', p=colLwt, cll=True, cl=True)
    pm.separator(h=2, st='none')
    mirRcLwt = pm.rowColumnLayout(nc=2, cw=[(1,170), (2,170)], cs=(2,10))
    
    pm.columnLayout(rs=1, adj=True, p=mirRcLwt)
    pm.text('Target', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,25), (2,140)])
    mirTargBtn = pm.button(l=' + ')
    mirTargTf = pm.textField()
    mirTargBtn.setCommand(partial(populateFromSel, mirTargTf))
    
    pm.columnLayout(rs=1, adj=True, p=mirRcLwt)
    pm.text('Base', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,25), (2,130)])
    mirBaseBtn = pm.button(l=' + ')
    mirBaseTf = pm.textField()
    mirBaseBtn.setCommand(partial(populateFromSel, mirBaseTf))
    
    pm.button('Run', p=mirFrmLwt, c=partial(mirrorRun, mirTargTf, mirBaseTf))
    pm.separator(st='none', p=mirFrmLwt)
    
    #Hook Up Sub-frame
    huFrmLwt = pm.frameLayout('Hook Up Shapes', p=colLwt, cll=True, cl=True)
    pm.separator(h=2, st='none')
    pm.text('To use this tool, fill out the lower section, \nselect the mesh you wish to add as a target, then run\n')
    huRcLwt = pm.rowColumnLayout(nc=2, cw=[(1,170), (2,160)], cs=(2,10))
    
    huCol1 = pm.columnLayout(rs=1, adj=True, p=huRcLwt)
    pm.text('Base', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,20), (2,145)])
    huBaseBtn = pm.button(l=' + ')
    huBaseTf = pm.textField()
    
    pm.setParent(huCol1)
    pm.separator(h=10, st='none')
    pm.text('Driver', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,20), (2,145)])
    huDriverBtn = pm.button(l=' + ')
    huDriverTf = pm.textField()
    huDriverBtn.setCommand(partial(populateFromSel, huDriverTf))
    
    huCol2 = pm.columnLayout(rs=1, adj=True, p=huRcLwt)
    pm.text('Blendshape Deformer', al='center')
    bsOpt = pm.optionMenu(l='')
    pm.menuItem(l='<Create New>')
    
    huBaseTf.changeCommand(partial(populateBsMen, huBaseTf.getText(), bsOpt))
    huBaseTf.enterCommand(partial(populateBsMen, huBaseTf.getText(), bsOpt))
    huBaseBtn.setCommand(partial(populateFromSel, huBaseTf, bsOpt))
    
    pm.setParent(huCol2)
    pm.separator(h=15, st='none')
    pm.text('     Attribute (RMB for Options)', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,20), (2,135)])
    pm.text(l='.   ')
    huAttrTf = pm.textField()
    attrPop = pm.popupMenu(button=3)
    pm.menuItem('Enter Driver First')
    attrPop.postMenuCommand(partial(populateAttrMen, huDriverTf, attrPop, huAttrTf))
    
    
    pm.setParent(huFrmLwt)
    pm.separator()
    pm.text('Key Info')
    
    kiRcLwt = pm.rowColumnLayout(nc=2, cw=[(1,165), (2,165)], cs=(2,10))
    
    pm.columnLayout(rs=1, adj=True, p=kiRcLwt)
    pm.text('Driver value for weight=0:', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,25), (2,137)])
    kiZeroBtn = pm.button(l=' > ')
    kiZeroFf = pm.floatField(v=0)
    kiZeroBtn.setCommand(partial(floatFieldFromDriver, huDriverTf, huAttrTf, kiZeroFf))
    
    pm.columnLayout(rs=1, adj=True, p=kiRcLwt)
    pm.text('Driver value for weight=1:', al='center')
    pm.rowColumnLayout(nc=2, cw=[(1,25), (2,130)])
    kiOneBtn = pm.button(l=' > ')
    kiOneFf = pm.floatField(v=90)
    kiOneBtn.setCommand(partial(floatFieldFromDriver, huDriverTf, huAttrTf, kiOneFf))
    
    pm.setParent(kiRcLwt)
    pm.separator(h=7, st='none');pm.separator(h=7, st='none')
    kiZeroTan = pm.optionMenu()
    pm.menuItem(l='spline');pm.menuItem(l='linear');pm.menuItem(l='clamped');pm.menuItem(l='stepped');
    pm.menuItem(l='flat');pm.menuItem(l='plateau');pm.menuItem(l='auto')
    kiOneTan = pm.optionMenu()
    pm.menuItem(l='spline');pm.menuItem(l='linear');pm.menuItem(l='clamped');pm.menuItem(l='stepped');
    pm.menuItem(l='flat');pm.menuItem(l='plateau');pm.menuItem(l='auto')
    pm.separator(h=7, st='none');pm.separator(h=7, st='none')
    priCb = pm.checkBox('Pre Infinity')
    poiCb = pm.checkBox('Post Infinity')
    
    pm.button(l='Run', p=huFrmLwt, c=partial(hookupRun, huBaseTf, bsOpt, huDriverTf, huAttrTf, kiZeroFf, 
                                             kiOneFf, kiZeroTan, kiOneTan, priCb, poiCb))
    pm.separator(st='none', p=mirFrmLwt)
    
    #Info Sub-frame
    pm.frameLayout('Information', p=colLwt, cll=True, cl=True)
    pm.separator(st='none')
    pm.button('About', w=340, c=aboutWin)
    pm.separator(st='none')
    
    pm.showWindow(win)


def populateAttrMen(*args):
    if args[0].getText():
        args[1].deleteAllItems()
        for i in pm.listAttr(args[0].getText(), k=True):
            pm.menuItem(i, p=args[1], c=partial(fillAttrField, args[2], str(i)))


def fillAttrField(*args):
    args[0].setText(args[1])


def floatFieldFromDriver(*args):
    
    val = pm.getAttr('%s.%s'%(args[0].getText(), args[1].getText()))
    args[2].setValue(val)


def populateFromSel(*args):
    
    sel = pm.ls(sl=True)
    if not sel:
        pm.error('Nothing is selected')
    
    args[0].setText(str(sel[0]))
    
    if len(args) == 3:
        populateBsMen(args[1], str(sel[0]))


def populateBsMen(*args):
    
    bs = []
    
    #getting blendshapes
    for i in pm.listHistory(args[-1]):
        if pm.objectType(i, isType='blendShape'):
            bs.append(str(i))
    print bs
    #clearing then re-populating the menu
    args[-2].clear()
    pm.menuItem(l='<Create New>', p=args[-2])
    
    for i in bs:
        pm.menuItem(l=i, p=args[-2])


def hookupRun(*args):
    
    baseTf, bsMen, driverTf, attrTf, zeroWtFf, oneWtFf, itMen, otMen, priCb, poiCb, ph= args
    
    #Check to make sure something's selected
    if not pm.ls(sl=True):
        pm.error('Nothing is selected')
    
    #Interpreting the blendshape menu
    if bsMen.getValue() == '<Create New>':
        bs = None
    else:
        bs=bsMen.getValue()
    
    na_bsCorrectiveSculpt.cbsHookup(base = baseTf.getText(), bs=bs, shape=pm.ls(sl=True)[0], 
        driver='%s.%s'%(driverTf.getText(), attrTf.getText()), driveRange=[zeroWtFf.getValue(), oneWtFf.getValue()],
        tan=[itMen.getValue(), otMen.getValue()], infinity=[priCb.getValue(), poiCb.getValue()])


def mirrorRun(*args):
    
    na_bsCorrectiveSculpt.cbsMirror(args[0].getText(), args[1].getText())


def aboutWin(*args):
    win = 'aboutWin'
    
    if pm.window(win, q=True, exists=True):
        pm.deleteUI(win)
    win=pm.window(win, t='About Channel Wizard', sizeable=False, rtf=True, mnb=False, mxb=False)
    
    pm.rowColumnLayout(nc=1)
    pm.text('\nYou are using the Corrective Blendshape Model Helper v1.0\nIt was created by Noah Alzayer\n\n\n')
    pm.text('  This is his website where you can see other (hopefully) cool things he\'s done:     \n')
    pm.text(l='http://noahalzayer.wordpress.com/', hyperlink=True)
    pm.text('\n\nYou can also yell at him if things don\'t work at:\n')
    pm.text('nalzay89@gmail.com\n', hl=True)
    
    pm.showWindow(win)