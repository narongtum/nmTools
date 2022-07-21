# POV parent LOCAL WORLD
import maya.cmds as mc
'''
from function.rigging.feature import localWorldPOV

'''

def createlocalWorld(type = 'pov' , nodeName = '' , parentTo = ''):

	if nodeName == None:
		sel = mc.ls(sl=1)
	else:
		sel = nodeName


	i = 0
	mc.pickWalk(d='up')
	upSel = mc.pickWalk(d='up')
	upGrp = upSel[0]
	preName = sel.split('_')
	name = preName[0]
	print name

	grp = name + '_Zro_grp'
	wor = name + '_Wor_grp'
	loc = name + '_Loc_grp'
	rev = name + '_rev'
	pov = name + '_ctrl'

	'''
	pConAttrLoc = grp + '_orientConstraint1' + '.' + loc + 'W0'
	pConAttrWor = grp + '_orientConstraint1' + '.' + wor + 'W1'

			
	mc.group(em=1,n=wor)
	mc.group(em=1,n=loc)

	mc.createNode('reverse',n=rev)

	mc.parentConstraint( grp,wor , w=1,mo=0 )
	mc.parentConstraint( grp,loc , w=1,mo=0 )
	mc.delete(wor + '_parentConstraint1')
	mc.delete(loc + '_parentConstraint1')

	mc.parent(wor,loc,upGrp)

	
	# World to wor

	if type == 'pov':
		mc.orientConstraint( loc,wor,grp,w=0,mo=1 )
	else:
		mc.parentConstraint( loc,wor,w=1,mo=1 )
		

	

	# Parent to GRP
	mc.parentConstraint(loc,wor,grp,w=0,mo=1)


	# Connect povCtrl to rev to pCon
	mc.connectAttr(pov + '.localWorld', rev + '.inputX')
	mc.connectAttr(rev + '.outputX', pConAttrLoc)
	mc.connectAttr(rev + '.inputX', pConAttrWor)
	'''

	return grp,wor,loc,rev,pov
