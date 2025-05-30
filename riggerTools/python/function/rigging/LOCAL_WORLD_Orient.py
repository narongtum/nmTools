import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.autoRig.base import core
reload(core)


# orient LOCAL WORLD 
# select controller
# specific the world space
def localWorldOrient( worldCtrl = 'placement_ctrl' ):
	sel = mc.ls(sl=1)
	for i in range(len(sel)):
		mc.select(sel[i])
		mc.pickWalk(d='up')
		upSel = mc.pickWalk(d='up')
		upGrp = upSel[0]
		name = core.check_name_style(sel[i])[0]
		# preName = sel[i].split('_')
		# name = preName[0]
		
		grp = name + 'Zro_grp'
		wor = name + 'Wor_grp'
		loc = name + 'Loc_grp'
		rev = name + '_rev'

		pov = name + '_ctrl'
		povShape = core.shapeName(pov)

		

		pConAttrLoc = grp + '_orientConstraint1' + '.' + loc + 'W0'
		pConAttrWor = grp + '_orientConstraint1' + '.' + wor + 'W1'

		#... adding attr for selected controller
		mc.addAttr( povShape , longName = 'localWorld', attributeType = 'short', defaultValue = 0 , max = 1, min = 0,keyable=True)
		
		mc.group(em=1,n=wor)
		mc.group(em=1,n=loc)
		mc.createNode('reverse',n=rev)
		
		mc.parentConstraint(grp,wor,w=1,mo=0)
		mc.parentConstraint(grp,loc,w=1,mo=0)
		mc.delete(wor + '_parentConstraint1')
		mc.delete(loc + '_parentConstraint1')
		
		mc.parent(wor,loc,upGrp)
		#... World to wor
		mc.orientConstraint( worldCtrl, wor,w=1,mo=1 )
		#... Parent to GRP
		mc.orientConstraint(loc,wor,grp,w=0,mo=1)
		#... Connect povCtrl to rev to pCon
		mc.connectAttr(povShape + '.localWorld', rev + '.inputX')
		mc.connectAttr(rev + '.outputX', pConAttrLoc)
		mc.connectAttr(rev + '.inputX', pConAttrWor)
