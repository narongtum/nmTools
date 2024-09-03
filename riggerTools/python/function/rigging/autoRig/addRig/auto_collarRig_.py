
#... ring
side  = 'LFT'
#... name
type = 'upperLeg'
#... len joint
len_jnt = 1
#... world orient
worldOrient = True

start=mc.spaceLocator(n=side+'_'+type+'_start_locator')[0]
end=mc.spaceLocator(n=side+'_'+type+'_end_locator')[0]

if not mc.objExists(type+'_center_locator'):
	mc.spaceLocator(n=type+'_center_locator')
	mc.setAttr(type+'_center_locator.v',0)

ringLen=0

for a in mc.ls('*'+type+'_start_locator'):
	ringLen=ringLen+1
mc.addAttr(start,ln='type',dt='string',k=1)
mc.setAttr(start+'.type',cb=1,k=0)
mc.setAttr(start+'.type',str(ringLen),type='string')

for a in mc.ls('*'+type+'_start_locator'):
	if mc.getAttr(a+'.type')==str(ringLen-1):
		old_side=a.split('_')[0]
for a in mc.ls('*'+type+'_start_locator'):
	if mc.getAttr(a+'.type')==str(1):
		startLoc=a

mc.move(0,1,0,end)

if not mc.objExists(type+'_group'):
	grp=mc.createNode('transform',n=type+'_group')
	vectorGrp=mc.createNode('transform',n=type+'_joints_group',p=grp)
	mc.parent(type+'_center_locator',grp)
else:
	grp=type+'_group'
	vectorGrp=type+'_vector_group'

mc.parent(start,grp)
len_jnt=int(len_jnt)
ry=0

for a in range (1,len_jnt+1):
	dir=str(a)
	r=360.0/len_jnt
	if not mc.objExists(type+'_'+dir+'_base_joint_locator'):
		jnt_pos=mc.spaceLocator(n=type+'_'+dir+'_base_joint_locator')[0]
	jnt_pos=type+'_'+dir+'_base_joint_locator'
	mc.setAttr(jnt_pos+'.ry',ry)
	ry=ry+r
	if not mc.objExists(type+'_'+str(a+1)+'_setRange'):
		if not mc.objExists(grp+'.addAngle'):
			mc.addAttr(grp,sn='addAngle',k=1)
			mc.addAttr(grp,sn='volume',k=1)
			mc.setAttr(grp+'.addAngle',k=0,cb=1)
			mc.setAttr(grp+'.volume',k=0,cb=1)
			mc.setAttr(grp+'.addAngle',90)
		if not mc.objExists(grp+'.'+type+'_'+dir+'_psd'):
			mc.addAttr(grp,sn=type+'_'+dir+'_psd',k=1)
			mc.setAttr(grp+'.'+type+'_'+dir+'_psd',k=0,cb=1)
	if not mc.objExists(type+'_'+dir+'_base_joint'):
		jnt_1=mc.joint(jnt_pos,n=type+'_'+dir+'_base_joint')
		mc.setAttr(jnt_pos+'Shape.v',0)
		mc.setAttr(jnt_1+'.jointOrientX',-90)
		if not mc.objExists(type+'_'+dir+'_skin_joint'):
			jnt_2=mc.joint(end,n=type+'_'+dir+'_skin_joint')
		if worldOrient:
			mc.orientConstraint(grp,jnt_2)
		mc.parent(type+'_'+dir+'_skin_joint',jnt_1)
		if not mc.objExists(type+'_'+dir+'_pose_vector_locator'):
			dup=mc.spaceLocator(n=type+'_'+dir+'_pose_vector_locator')[0]
			mc.setAttr(dup+'.v',0)
			mc.parent(dup,jnt_1)
			mc.setAttr(dup+'.tz',1)
			mc.move(0,0,1,jnt_pos,os=1)
			mc.delete(mc.parentConstraint(jnt_pos,dup))
		if not mc.listRelatives(jnt_1,p=1):
			mc.parent(jnt_1,mc.listRelatives(start,p=1))
		mc.parent(dup,vectorGrp)
		mc.parent(jnt_pos,vectorGrp)
	#
	if not mc.objExists(side+'_'+type+'_base_vector_plusMinusAverage'):
		pma_1=mc.createNode('plusMinusAverage',n=side+'_'+type+'_base_vector_plusMinusAverage')
		mc.setAttr(pma_1+'.operation',2)
		mc.connectAttr(start+'Shape.worldPosition',pma_1+'.input3D[0]')
		mc.connectAttr(end+'Shape.worldPosition',pma_1+'.input3D[1]')

	
	distance=mc.createNode('distanceBetween',n=side+'_'+type+'_'+dir+'_distanceBetween')
	mc.connectAttr(type+'_'+dir+'_base_joint_locatorShape.worldPosition',distance+'.point1')
	mc.connectAttr(start+'Shape.worldPosition',distance+'.point2')
	mc.connectAttr(grp+'.worldInverseMatrix',distance+'.inMatrix1')
	mc.connectAttr(grp+'.worldInverseMatrix',distance+'.inMatrix2')
	
	dist=mc.getAttr(distance+'.distance')
	maxDistance=mc.createNode('condition',n='{0}_{1}_distance_{2}_condition'.format(side,type,dir))
	mc.connectAttr(distance+'.distance',maxDistance+'.firstTerm')
	mc.connectAttr(distance+'.distance',maxDistance+'.colorIfTrueR')
	mc.setAttr(maxDistance+'.operation',4)
	mc.setAttr(maxDistance+'.secondTerm',dist)
	mc.setAttr(maxDistance+'.colorIfFalseR',dist)
	
	if not mc.objExists(type+'_'+dir+'_distance_setRange'):
		remapDistance=mc.createNode('setRange',n=type+'_'+dir+'_distance_setRange')
		mc.connectAttr(grp+'.volume',remapDistance+'.minX')
		mc.connectAttr(maxDistance+'.outColorR',remapDistance+'.valueX')
		
		distancePos=mc.createNode('distanceBetween',n=type+'_'+dir+'_pos_distanceBetween')
		mc.connectAttr(type+'_center_locatorShape.worldPosition',distancePos+'.point1')
		mc.connectAttr(jnt_pos+'Shape.worldPosition',distancePos+'.point2')
		mc.connectAttr(grp+'.worldInverseMatrix',distancePos+'.inMatrix1')
		mc.connectAttr(grp+'.worldInverseMatrix',distancePos+'.inMatrix2')
		doubleDist=mc.createNode('multDoubleLinear',n=side+'_'+type+'_'+dir+'_multDoubleLinear')
		mc.connectAttr(distancePos+'.distance',doubleDist+'.input1')
		mc.connectAttr(doubleDist+'.output',remapDistance+'.oldMaxX')
		mc.setAttr(doubleDist+'.input2',2)
		mc.connectAttr(distancePos+'.distance',maxDistance+'.secondTerm')
		mc.connectAttr(distancePos+'.distance',maxDistance+'.colorIfFalseR')
		
	pma_2=mc.createNode('plusMinusAverage',n=side+'_'+type+'_'+dir+'_plusMinusAverage')
	mc.setAttr(pma_2+'.operation',2)
	mc.connectAttr(start+'Shape.worldPosition',pma_2+'.input3D[0]')
	mc.connectAttr(type+'_'+dir+'_pose_vector_locatorShape.worldPosition',pma_2+'.input3D[1]')
	angle=mc.createNode('angleBetween',n=side+'_'+type+'_'+dir+'_angleBetween')
	maxAngle=mc.createNode('condition',n='{0}_{1}_angle_{2}_condition'.format(side,type,dir))
	mc.connectAttr(side+'_'+type+'_base_vector_plusMinusAverage.output3D',angle+'.vector1')
	mc.connectAttr(side+'_'+type+'_'+dir+'_plusMinusAverage.output3D',angle+'.vector2')
	mc.connectAttr(angle+'.angle',maxAngle+'.firstTerm')
	mc.connectAttr(angle+'.angle','{0}_{1}_angle_{2}_condition.colorIfTrueR'.format(side,type,dir))
	mc.setAttr(maxAngle+'.operation',4)
	mc.setAttr(maxAngle+'.colorIfFalseR',mc.getAttr(angle+'.angle'))
	mc.setAttr(maxAngle+'.secondTerm',mc.getAttr(angle+'.angle'))
	side_ls=0
	for s in mc.ls('*_{0}_base_vector_plusMinusAverage'.format(type)):
		side_ls=side_ls+1
	if side_ls>1:
		mc.connectAttr(distance+'.distance','{0}_{1}_distance_{2}_condition.secondTerm'.format(old_side,type,dir),f=1)
		mc.connectAttr(distance+'.distance','{0}_{1}_distance_{2}_condition.colorIfFalseR'.format(old_side,type,dir),f=1)
		
		mc.connectAttr(angle+'.angle','{0}_{1}_angle_{2}_condition.secondTerm'.format(old_side,type,dir),f=1)
		mc.connectAttr(angle+'.angle','{0}_{1}_angle_{2}_condition.colorIfFalseR'.format(old_side,type,dir),f=1)
	if side_ls>2:
		for a in mc.ls('*'+type+'_start_locator'):
			if mc.getAttr(a+'.type')==str(ringLen-2):
				side_pre=a.split('_')[0]
		mc.connectAttr(angle+'.angle','{0}_{1}_angle_{2}_condition.firstTerm'.format(old_side,type,dir),f=1)
		mc.connectAttr(angle+'.angle','{0}_{1}_angle_{2}_condition.colorIfTrueR'.format(old_side,type,dir),f=1)
		mc.connectAttr('{0}_{1}_angle_{2}_condition.outColorR'.format(side_pre,type,dir),'{0}_{1}_angle_{2}_condition.secondTerm'.format(old_side,type,dir),f=1)
		mc.connectAttr('{0}_{1}_angle_{2}_condition.outColorR'.format(side_pre,type,dir),'{0}_{1}_angle_{2}_condition.colorIfFalseR'.format(old_side,type,dir),f=1)
		mc.connectAttr('{0}_{1}_angle_{2}_condition.outColorR'.format(old_side,type,dir),type+'_'+dir+'_setRange.valueX',f=1)
		mc.connectAttr('{0}_{1}_angle_{2}_condition.outColorR'.format(old_side,type,dir),type+'_'+dir+'_setRange.valueY',f=1)
		mc.connectAttr('{0}_{1}_angle_{2}_condition.outColorR'.format(old_side,type,dir),type+'_'+dir+'_setRange.valueZ',f=1)
		
		mc.connectAttr(distance+'.distance','{0}_{1}_distance_{2}_condition.firstTerm'.format(old_side,type,dir),f=1)
		mc.connectAttr(distance+'.distance','{0}_{1}_distance_{2}_condition.colorIfTrueR'.format(old_side,type,dir),f=1)
		mc.connectAttr('{0}_{1}_distance_{2}_condition.outColorR'.format(side_pre,type,dir),'{0}_{1}_distance_{2}_condition.secondTerm'.format(old_side,type,dir),f=1)
		mc.connectAttr('{0}_{1}_distance_{2}_condition.outColorR'.format(side_pre,type,dir),'{0}_{1}_distance_{2}_condition.colorIfFalseR'.format(old_side,type,dir),f=1)
		mc.connectAttr('{0}_{1}_distance_{2}_condition.outColorR'.format(old_side,type,dir),type+'_'+dir+'_distance_setRange.valueX',f=1)
	if not mc.objExists(type+'_'+dir+'_setRange'):
		angleValue=mc.getAttr(angle+'.angle')
		setRange=mc.createNode('setRange',n=type+'_'+dir+'_setRange')
		mc.connectAttr(maxAngle+'.outColorR',setRange+'.valueX')
		mc.connectAttr(maxAngle+'.outColorR',setRange+'.valueY')
		mc.connectAttr(maxAngle+'.outColorR',setRange+'.valueZ')
		mc.setAttr(grp+'.'+'volume',angleValue)
		mc.setAttr(setRange+'.'+'minZ',1)
		mc.connectAttr(setRange+'.outValueX',jnt_1+'.rx')
		mc.connectAttr(remapDistance+'.'+'outValueX',setRange+'.oldMaxX')
		mc.connectAttr(remapDistance+'.'+'outValueX',setRange+'.oldMaxY')
		mc.connectAttr(remapDistance+'.'+'outValueX',setRange+'.oldMaxZ')
		mc.connectAttr(grp+'.'+'addAngle',setRange+'.minX')
		mc.connectAttr(grp+'.'+'addAngle',setRange+'.minY')
		mc.connectAttr(setRange+'.outValueZ',grp+'.'+type+'_'+dir+'_psd')
mc.parent(end,start)