	# POV parent LOCAL WORLD
localWorldPOV():
	sel = mc.ls(sl=1)
	for i in range(len(sel)):
		mc.select(sel[i])
		mc.pickWalk(d='up')
		upSel = mc.pickWalk(d='up')
		upGrp = upSel[0]
		preName = sel[i].split('_')
		name = preName[0] + '_pov'
		
		grp = name + '_Zro_grp'
		wor = name + '_Wor_grp'
		loc = name + '_Loc_grp'
		rev = name + '_rev'
		pov = name + '_ctrl'
		pConAttrLoc = grp + '_parentConstraint1' + '.' + loc + 'W0'
		pConAttrWor = grp + '_parentConstraint1' + '.' + wor + 'W1'

		
		mc.group(em=1,n=wor)
		mc.group(em=1,n=loc)
		mc.createNode('reverse',n=rev)
		
		mc.parentConstraint(grp,wor,w=1,mo=0)
		mc.parentConstraint(grp,loc,w=1,mo=0)
		mc.delete(wor + '_parentConstraint1')
		mc.delete(loc + '_parentConstraint1')
		
		mc.parent(wor,loc,upGrp)
		# World to wor
		mc.parentConstraint('fly_ctrl',wor,w=1,mo=1)
		# Parent to GRP
		mc.parentConstraint(loc,wor,grp,w=0,mo=1)
		# Connect povCtrl to rev to pCon
		mc.connectAttr(pov + '.localWorld', rev + '.inputX')
		mc.connectAttr(rev + '.outputX', pConAttrLoc)
		mc.connectAttr(rev + '.inputX', pConAttrWor)
