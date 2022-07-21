'''
Align pivots by Serge Scherbakov.
http://www.serge-scherbakov.com/2012/12/align-pivots.html
Usage:
1. Select Child and Parent
3. Run script 
'''
 
import maya.cmds as cmds
import maya.mel as mel
 
def copyPivot ():
    sourceObj = cmds.ls(sl = True)[len(cmds.ls(sl = True))-1]
    targetObj = cmds.ls(sl = True)[0:(len(cmds.ls(sl = True))-1)]
    parentList = []
    for obj in targetObj:
        if cmds.listRelatives( obj, parent = True):
            parentList.append(cmds.listRelatives( obj, parent = True)[0])
        else:
            parentList.append('')
    if len(cmds.ls(sl = True))<2:
        cmds.error('select 2 or more objects.')
    pivotTranslate = cmds.xform (sourceObj, q = True, ws = True, rotatePivot = True)
    cmds.parent(targetObj, sourceObj)
    cmds.makeIdentity(targetObj, a = True, t = True, r = True, s = True)
    cmds.xform (targetObj, ws = True, pivots = pivotTranslate)
    for ind in range(len(targetObj)):
        if parentList[ind] != '' : 
            cmds.parent(targetObj[ind], parentList[ind])
        else:
            cmds.parent(targetObj[ind], world = True)
     
 
copyPivot()