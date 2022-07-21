import maya.cmds as mc
# Result : controller texture switch
# PS : Select File Name of the texture by desire order 

petNameMat = 'head_girl01_mat'
ctrl = 'neck_ctrl'
attrNam = 'femaleFace'
gender = 'girl'

sel = mc.ls(sl=True)
for i in range(len(sel)):
	 fileName = sel[i]
	 con = '%sfaceSwap%02d_con' %(gender , (i+1))
	 mc.createNode( 'condition', name = con )
	 mc.setAttr( con + '.secondTerm', (i+1))
	 mc.setAttr( con + '.operation', 0 )
	 mc.connectAttr( fileName + '.outColor', con + '.colorIfTrue' )
	 if i >0:
			 preCon = '%sfaceSwap%02d_con' %(gender,(i))
			 mc.connectAttr( preCon + '.firstTerm', con + '.firstTerm')
			 mc.connectAttr( preCon + '.outColor', con + '.colorIfFalse')
			 if i+1 == len(sel): # Find last Con
					 mc.connectAttr( con + '.outColor', petNameMat + '.color' )
					 print 'FINAL'
					 print i+1
	 elif i == 0:
			 mc.connectAttr( ctrl + '.'+attrNam , con + '.firstTerm')