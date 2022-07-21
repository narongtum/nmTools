'''

from function.rigging.autoRig.library import localWorldRot as lcw
reload(lcw)

'''

import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)

def localWorldOrient(nameList = ('','')):
	# orient LOCAL WORLD
	for i in range(len(nameList)):
	    
		if '_FK_' in nameList[i] or '_IK_' in nameList[i]:	
			preName = nameList[i].split('_')
			name = preName[0] + '_' + preName[1]
			mc.select(nameList[i])
			mc.pickWalk(d='up')
			upSel = mc.pickWalk(d='up')
		
		
		elif '_' in nameList[i]:
			preName = nameList[i].split('_')
			name = preName[0]
			mc.select(nameList[i])
			mc.pickWalk(d='up')
			upSel = mc.pickWalk(d='up')
		

		else:
			name = nameList[i]
			mc.select(name + '_ctrl')
			mc.pickWalk(d='up')
			upSel = mc.pickWalk(d='up')
			
		# Name
		grp = name + '_Zro_grp'
		wor = name + '_Wor_grp'
		loc = name + '_Loc_grp'
		rev = name + '_rev'
		pov = name + '_ctrl'
		upGrp = upSel[0]
		pConAttrLoc = grp + '_orientConstraint1' + '.' + loc + 'W0'
		pConAttrWor = grp + '_orientConstraint1' + '.' + wor + 'W1'
		
		# Create att if exist
		if mc.attributeQuery( 'localWorld' ,node = nameList[i], exists = 1):
			print 'localWorld Exists'
    
		else:
			mc.addAttr( nameList[i] , longName = 'localWorld' , defaultValue = 0 , minValue = 0, maxValue = 1 )
			mc.setAttr('%s.%s' %( nameList[i] , 'localWorld' ), keyable = True)

		mc.group(em=1,n=wor)
		mc.group(em=1,n=loc)
		mc.createNode('reverse',n=rev)
		# Func
		misc.snapParentConst( grp,wor )
		misc.snapParentConst( grp,loc )
		mc.parent(wor,loc,upGrp)
		# World to wor
		mc.orientConstraint('fly_ctrl',wor,w=1,mo=1)
		# Parent to GRP
		mc.orientConstraint(loc,wor,grp,w=0,mo=1)
		# Connect povCtrl to rev to pCon
		mc.connectAttr(pov + '.localWorld', rev + '.inputX')
		mc.connectAttr(rev + '.outputX', pConAttrLoc)
		mc.connectAttr(rev + '.inputX', pConAttrWor)

		mc.select(deselect = True)
		  
#Test Function

'''
localWorldOrient(nameList = ('neck01_ctrl','neck02_ctrl'))
'''


def connectFkIkVis( attrName = '' , uprNam = '' , footIKGrp = ''):
	'''connectFkIkVis(  attrName = 'IK_FK_Arm_L' , uprNam = backlegLFTNam[0] , footIKGrp = footIKLFT )'''

	#footIKGrp = footIKGrp + '_IK_Zro_grp'
	uprNamFK = uprNam + '_FK_Zro_grp'
	uprNamIK = uprNam + '_IK_Zro_grp'
	revNam = mc.createNode( 'reverse', name = uprNam + '_rev')
	mc.connectAttr( 'placement_ctrl.%s' %attrName  , uprNamFK+'.visibility'  )
	mc.connectAttr( 'placement_ctrl.%s' %attrName  , revNam+'.inputX' )
	mc.connectAttr( revNam +'.outputX' , uprNamIK+'.visibility'  )
	mc.connectAttr( revNam +'.outputX' , footIKGrp+'.visibility'  )