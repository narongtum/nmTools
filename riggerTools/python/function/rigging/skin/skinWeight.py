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
		print '%s is not have any skincluster' % sels[1]

	# toSelectedBones(tsb) = geometry will be bound to the selected bones only.
	# assign same skin cluster to destination
	newSkin = mc.skinCluster(jnts, sels[1], toSelectedBones=True)[0]

	# select source and destination
	mc.select(sels[0], replace=True)
	mc.select(sels[1], add=True)

	# copy weight
	mc.copySkinWeights(noMirror = True, surfaceAssociation = 'closestPoint',
					   influenceAssociation ='closestJoint')
