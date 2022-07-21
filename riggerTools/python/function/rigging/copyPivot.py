# all credits to Serge Scherbakov
# This script allows you to copy object pivot translation and rotation from one object to another one. How to use:
#  - copy code to the script editor "Python tab"
#  - select source object
#  - select target object
#  - execute script
# Works on multiple selection. Align all object pivots with last selected.
import maya.cmds as mc

def copyPivot ():
	sourceObj = mc.ls(sl = True)[len(mc.ls(sl = True))-1]
	targetObj = mc.ls(sl = True)[0:(len(mc.ls(sl = True))-1)]
	parentList = []
	for obj in targetObj:
		if mc.listRelatives( obj, parent = True):
			parentList.append(mc.listRelatives( obj, parent = True)[0])
		else:
			parentList.append('')
	if len(mc.ls(sl = True))<2:
		mc.error('select 2 or more objects.')
	pivotTranslate = mc.xform (sourceObj, q = True, ws = True, rotatePivot = True)
	mc.parent(targetObj, sourceObj)
	mc.makeIdentity(targetObj, a = True, t = True, r = True, s = True)
	mc.xform (targetObj, ws = True, pivots = pivotTranslate)
	for ind in range(len(targetObj)):
		if parentList[ind] != '' : 
			mc.parent(targetObj[ind], parentList[ind])
		else:
			mc.parent(targetObj[ind], world = True)

copyPivot ()