import maya.cmds as mc

# Change matarial and attr name
# Drag and Drop texture file to the shader editor 
# Select texture File Name and run

petNameMat = 'face_tamarinmonkey01_mat'
ctrl = 'face_ctrl'
attrName = 'face'

sel = mc.ls(sl=True)
for i in range(len(sel)):
	fileName = sel[i]
	con = 'faceSwap%02d_con' %(i+1)
	mc.createNode( 'condition', name = con )
	mc.setAttr( con + '.secondTerm', (i+1))
	mc.setAttr( con + '.operation', 0 )
	mc.connectAttr( fileName + '.outColor', con + '.colorIfTrue' )
	if i >0:
		preCon = 'faceSwap%02d_con' %(i)
		mc.connectAttr( preCon + '.firstTerm', con + '.firstTerm')
		mc.connectAttr( preCon + '.outColor', con + '.colorIfFalse')
		if i+1 == len(sel): # Find last Con
			mc.connectAttr( con + '.outColor', petNameMat + '.color' )
			print 'FINAL'
			print i+1
	elif i == 0:
		mc.connectAttr( ctrl + '.%s' %attrName , con + '.firstTerm')
		