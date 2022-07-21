
import maya.cmds as mc

def connectFkIkVis(	attrName = '' , uprNam = '' , footIKGrp = ''):
	'''connectFkIkVis(	attrName = 'IK_FK_Arm_L' , uprNam = backlegLFTNam[0] , footIKGrp = footIKLFT )'''

	#footIKGrp = footIKGrp + '_IK_Zro_grp'
	uprNamFK = uprNam + '_FK_Zro_grp'
	uprNamIK = uprNam + '_IK_Zro_grp'
	revNam = mc.createNode( 'reverse', name = uprNam + '_rev')
	mc.connectAttr( 'placement_ctrl.%s' %attrName  , uprNamFK+'.visibility'  )
	mc.connectAttr( 'placement_ctrl.%s' %attrName  , revNam+'.inputX' )
	mc.connectAttr( revNam+'.outputX' , uprNamIK+'.visibility'  )
	mc.connectAttr( revNam+'.outputX' , footIKGrp+'.visibility'  )