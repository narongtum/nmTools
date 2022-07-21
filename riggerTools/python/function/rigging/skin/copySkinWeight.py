
# reload module
from function.framework.reloadWrapper import reloadWrapper as reload



# import mel
import maya.mel as mm
import maya.cmds as mc

# copy selected weight
# select source and destination

# move to skin util
def copyWeight():
	sels = mc.ls(sl=True)
	# query influence joint
	jnts = mc.skinCluster(sels[0], query=True, influence=True)
	# find skincluster in destination skin
	oldSkin = mm.eval('findRelatedSkinCluster("%s")' % sels[1])

	# check if have skin
	if oldSkin:
		# use arg for editable
		mc.skinCluster(oldSkin, edit=True, unbind=True)
	else:
		print ('%s is not have any skincluster' % sels[1])

	# toSelectedBones(tsb) = geometry will be bound to the selected bones only.
	# assign same skin cluster to destination
	newSkin = mc.skinCluster(jnts, sels[1], toSelectedBones = True)[0]

	# select source and destination
	mc.select(sels[0], replace=True)
	mc.select(sels[1], add=True)

	# copy weight
	mc.copySkinWeights( noMirror = True, surfaceAssociation = 'closestPoint', influenceAssociation ='closestJoint' )

# option for using copySkin from Nico
def copyWeightArg(source, destination):
	# find skinCluster
	# selection = mc.ls(sl=True)
	# source = selection[0]
	# destination = selection[1]
	skinCluster_source = mel.eval('findRelatedSkinCluster '+source)
	infList = mc.skinCluster(skinCluster_source, q=True, inf=True )

	# check if new skin has skinCluster if yes delete
	skinCluster_destination = mel.eval('findRelatedSkinCluster '+destination)
	if skinCluster_destination:
		mc.setAttr(skinCluster_destination+'.envelope', 0)
		mc.delete(skinCluster_destination)
		print('Delete skinCluster >>> {0}'.format(skinCluster_destination))
	# copyweight
	skinCluster_destination = mc.skinCluster(destination, infList, toSelectedBones=True)
	mc.copySkinWeights(source, destination, noMirror = True, surfaceAssociation = 'closestPoint', influenceAssociation = 'oneToOne')
	print('Copy weighting from  "{0}" >>> "{1}" was successful.'.format(source, destination))
