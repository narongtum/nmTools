#... using wtAddMatrix for make something like rivet

import maya.OpenMaya as om

from function.rigging.autoRig.base import core
reload(core)




#... I can't find the old function so write the new one number3 
#... find joint in skinCluster
skinCluster='sphere_skc'
vtx = 'body_ply.vtx[1185] '
thresholdValue = 0.001

#... driven slave child follower or whatever object
target = 'rivet01_jnt'
#... Influence object there have a lot of joint in one VTX
#influence_obj = 'breast01RGT_bJnt'

#.... name for main function
targetName = core.findBaseName(target)








#... find joint weight
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




#.... Assign influence joint 
print( joint_influence_dict.keys() )
influence_obj = list(joint_influence_dict.keys())



#.... Next Create MetaNode for store weight
from function.rigging.autoRig.base import core
reload(core)

#... Store value to meta
meta = core.MetaBlank(targetName)
joint_influence_dict

for index, (key, value) in enumerate(joint_influence_dict.items()):
    print(key)
    print(value)
    rIndex = index + 1
    meta.addAttribute(longName = '{0}_{1}'.format(key,rIndex), dv = value)





#.... Next find offset vector you can use manual method 

#... Useful function
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




for each in influence_obj:

	#... find base name
	influName = core.findBaseName(each)
	baseName = influName 

	#... Create offset mult matrix

	#... CreateNode
	mulMtx = '{0}_offset_mulMtx'.format(baseName)
	mc.createNode( 'multMatrix', n = mulMtx )


	#... get world matrix to [0]
	parentWorldMatrix = getDagPath(target).inclusiveMatrix()
	parentWorldMatrix_val = [parentWorldMatrix(i,j) for i in range(4) for j in range(4)]
	mc.setAttr( mulMtx + '.matrixIn[0]', parentWorldMatrix_val , type = 'matrix')


	#... get world matrix to [1]
	invert_Matrix = getDagPath(each).inclusiveMatrix()
	invert_Matrix_val = [invert_Matrix.inverse()(i,j) for i in range(4) for j in range(4)]
	mc.setAttr( mulMtx + '.matrixIn[1]', invert_Matrix_val , type = 'matrix')


	#... Next create XFORM for collect value 
	xform_mulMtx = mc.createNode( 'multMatrix', name = '{0}_xform_mulMtx'.format(baseName))
	mc.connectAttr('{0}.matrixSum'.format(mulMtx),'{0}.matrixIn[0]'.format(xform_mulMtx))
	mc.connectAttr('{0}.worldMatrix[0]'.format(each),'{0}.matrixIn[1]'.format(xform_mulMtx))











#... Create wtAddMatrix
weight_matrix = core.WtAddMatrix(influence_obj)




#...Create Invert space for make it static
#... CreateNode
invert_name = '{0}_invert'.format(baseName)
invert_mulMtx = core.MultMatrix(invert_name)

#mc.createNode( 'multMatrix', name = invert_mulMtx )

'''
mc.connectAttr('{0}.matrixSum'.format(weight_matrix),'{0}.matrixIn[0]'.format(invert_mulMtx.name))
decompost = core.DecomposeMatrix('{0}'.format(baseName))
invert_mulMtx.attr('matrixSum') >> decompost.attr('inputMatrix')



'''


#... create null grp
offset_grp = '{0}_offsetGrp'.format(baseName)
offset_grp = core.Null(offset_grp)


invert_mulMtx.attr('matrixSum') >> offset_grp.attr('offsetParentMatrix')



#.... parent invert to mult matrix just in case
offset_grp.attr('parentInverseMatrix[0]') >> invert_mulMtx.attr('matrixIn[1]')


decompost.attr('outputTranslate') >> offset_grp.attr('translate')
decompost.attr('outputRotate') >> offset_grp.attr('rotate')
decompost.attr('outputScale') >> offset_grp.attr('scale')


#... TODO
# merge matrix * invert parent matrix in one node