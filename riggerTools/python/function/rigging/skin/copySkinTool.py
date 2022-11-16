# maya python scripting tutorial by Bjorn Blaabjerg Sorensen
# this script is not for resale or re-distribution.
# please visit blaabjergb.com for more tutorials and resources.
# edit Sep 2 2015

''' select skinned mesh, then select mesh to transfer to, and run '''

import maya.cmds as cmds
import maya.mel as mm

def objectSel():
	if len(cmds.ls(sl=True)) <2:
		return False
	else:
		objects=cmds.listRelatives(s=True)
		shapeHistory=cmds.listHistory(objects[0], lv=3)
		skc=cmds.ls(shapeHistory, typ='skinCluster')
		target=cmds.ls(sl=True)[-1]
		assignSkc(skc,target)
		return True

def assignSkc(skc,target):
	shapeHistory=cmds.listHistory(target, lv=3)
	oldSkc=cmds.ls(shapeHistory, typ='skinCluster')
	if oldSkc:
		cmds.delete(oldSkc)
	jnt=cmds.skinCluster(skc, weightedInfluence=True, q=True)
	newSkc=cmds.skinCluster(jnt, target)
	cmds.copySkinWeights(ss=skc[0], ds=newSkc[0], nm=True, surfaceAssociation='closestPoint')
	cmds.rename(newSkc,skc[0])
	cmds.select(deselect = True)
	return newSkc

# Nico copy skin
def ncCopySkinWeights(source, target):
	import maya.mel as mel

	skinClusterA = mel.eval('findRelatedSkinCluster '+source)
	infList = mc.skinCluster(skinClusterA, q=True, inf = True ) 

	skinClusterB = mel.eval('findRelatedSkinCluster '+target)

	if skinClusterB != '':
	    mc.setAttr(skinClusterB+'.envelope', 0)
	    mc.delete(skinClusterB)
	    

	# create new skinCluster on new model
	mc.skinCluster(infList,target, tsb = True)
	# copy skin weight to the new one
	mc.copySkinWeights(source, target,noMirror=True, surfaceAssociation = 'closestPoint', influenceAssociation = 'oneToOne')
	print('Copy weight from {0} to {1} was done !!!'.format(source,target))