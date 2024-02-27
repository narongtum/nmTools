import maya.OpenMaya as om


#... I can't find the old function so write the new one

#... find joint in skinCluster
#... find weight
skinCluster='skinCluster16_ACK'
vtx = 'hero_body01.vtx[1731]'
thresholdValue = 0.001
tgt = 'ctrl_default_space'
src = 'chest_space'
# influenceVals   = mc.skinPercent(skinCluster, vtx, q=True, v = True, ib = thresholdValue )
influenceJoint  = mc.skinPercent(skinCluster, vtx, q=True, t=None)
influenceData   = mc.skinPercent(skinCluster, vtx, q=True, v=True)


# Initialize an empty dictionary to store joint and influence value pairs
joint_influence_dict = {}


#... Print the list of joints and their corresponding influence values
for joint, value in zip(influenceJoint, influenceData):
	if value != 0:
		print("Joint:", joint, "Influence Value:", value)
		joint_influence_dict[joint] = value
	else:
		pass


#.... Next Create MetaNode for store weight

from function.rigging.autoRig.base import core
reload(core)


meta = core.MetaBlank(src)

joint_influence_dict

for index, (key, value) in enumerate(joint_influence_dict.items()):
    print(key)
    print(value)
    rIndex = index + 1
    meta.addAttribute(longName = '{0}_{1}'.format(key,rIndex), dv = value)
    








#.... Next find offset vector you can use manual method 

def getDagPath(node=None):
	sel = om.MSelectionList()
	sel.add(node)
	dagPath = om.MDagPath()
	sel.getDagPath(0, dagPath)
	return dagPath

def getLocalOffset(parent, child):
	
	parentWorldMatrix = getDagPath(parent).inclusiveMatrix()
	childWorldMatrix = getDagPath(child).inclusiveMatrix()
	# child World Matrix * invert parent World Matrix = child local matrix
	# return child local matrix
	return childWorldMatrix * parentWorldMatrix.inverse()



	
mulMtx = '{0}_mulMtx'.format(tgt)
dmpMtx = '{0}_dmpMtx'.format(tgt)



localOffset =  getLocalOffset( src, tgt )

offMat = [localOffset(i,j) for i in range(4) for j in range(4)]

# Create
mc.createNode( 'multMatrix', n = mulMtx )
mc.createNode( 'decomposeMatrix', n = dmpMtx )
#  Set and Connect
mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')



#... Next create xform for collect value 

tranform_joint = 'chest_bJnt'

mc.connectAttr('{0}.matrixSum'.format(mulMtx),'{0}.matrixIn[0]'.format(tranform_joint))

xform_mulMtx = mc.createNode( 'multMatrix', name = '{0}_xform_mulMtx'.format(tranform_joint))
mc.connectAttr('{0}.worldMatrix[0]'.format(tranform_joint),'{0}.matrixIn[1]'.format(xform_mulMtx))

