from axionTools.rigging.autoRig.library import backLegRig as blr
reload(blr)

from axionTools.rigging.autoRig.library import spineFkRig
reload(spineFkRig)

from axionTools.rigging.autoRig.library import bipedLegRig
reload(bipedLegRig)

from axionTools.rigging.autoRig.library import localWorldRot as lcw
reload(lcw)


#				#
# Spine Rig
# 
spineFkRig.cogRig(each = ('cog') , parentTo = 'fly_ctrl')
spineFkRig.hipRig(each = ('lowerBody') , parentTo = 'cog_Gimbal_ctrl')
spineFkRig.hipRig(each = ('hip') , parentTo = 'lowerBody_Gimbal_ctrl')
spineFkRig.spineFK(spineList = ('body','upperBody','chest' ) , parentTo = 'cog_Gimbal_ctrl')





#
# Front leg rig LFT
#	


# front leg rig LFT
legGrpLFT = bipedLegRig.bipedRig(

	jntList = ( 				'upLegFrontLFT_bind_jnt',
								'midLegFrontLFT_bind_jnt',
								'ankleFrontLFT_bind_jnt' 			)	,

	pov = 'legPovFrontLFT_tmpJnt'	,		
	side = 'LFT'					,				
	parentTo = 'chestGmbl_ctrl'		,
	placementAttr = 'IK_FK_Arm_L'	,
	part = 'frontLeg'

	)



# front foot roll rig LFT
footNam = bipedLegRig.bipedFootRollRig (
	rootNam = 'ankleFrontLFT_IK_jnt'	,													
	jntLst = ['ballRollFrontLFT_bind_jnt' ,'toeRollFrontLFT_bind_jnt']	,
	footBehav = ['footOutFront','footInFront','heelRollFront','toeRollFront','ballRollFront','ankleFront']	,	
	placementAttr = 'IK_FK_Arm_L'		,														
	side = 'LFT'						,																
	part = 'Frontleg'						,																
	uprIK = legGrpLFT[0],																		
	lwrIK = legGrpLFT[1]				)



# parenting grp

# IK
uprIkJnt = legGrpLFT[0] + '_IK_jnt'
mc.parent(uprIkJnt , 'hips_null_grp')

uprIkCtrl = legGrpLFT[0] + '_IK_Zro_grp'
mc.parent(uprIkCtrl , 'chest_Gimbal_ctrl')

# FK
uprFKJnt = legGrpLFT[0] + '_FK_jnt'
mc.parent(uprFKJnt , 'null_FK_jnt_grp')

uprFkCtrl = legGrpLFT[0] + '_FK_Zro_grp'
mc.parent(uprFkCtrl , 'chest_Gimbal_ctrl')

footZro = footNam + '_IK_Zro_grp'
mc.parent(footZro , 'IK_ctrl_grp')



# connect switch fk / ik to controller
lcw.connectFkIkVis(	attrName = 'IK_FK_Arm_L' , uprNam = legGrpLFT[0]  , footIKGrp = 'footFrontlegLFT_IK_Zro_grp' )






#
# Front leg rig RGT
#	

# front leg rig RGT
legGrpRGT = bipedLegRig.bipedRig(

	jntList = ( 				'upLegFrontRGT_bind_jnt',
								'midLegFrontRGT_bind_jnt',
								'ankleFrontRGT_bind_jnt' 			)	,

	pov = 'legPovFrontRGT_tmpJnt'	,		
	side = 'RGT'					,				
	parentTo = 'chestGmbl_ctrl'		,
	placementAttr = 'IK_FK_Arm_R'	,
	part = 'frontLeg'

	)



# front foot roll rig RGT
footNam = bipedLegRig.bipedFootRollRig (
	rootNam = 'ankleFrontRGT_IK_jnt'	,													
	jntLst = ['ballRollFrontRGT_bind_jnt' ,'toeRollFrontRGT_bind_jnt']	,
	footBehav = ['footOutFront','footInFront','heelRollFront','toeRollFront','ballRollFront','ankleFront']	,	
	placementAttr = 'IK_FK_Arm_R'		,														
	side = 'RGT'						,																
	part = 'Frontleg'						,																
	uprIK = legGrpRGT[0],																		
	lwrIK = legGrpRGT[1]				)



# parenting grp

# IK
uprIkJnt = legGrpRGT[0] + '_IK_jnt'
mc.parent(uprIkJnt , 'hips_null_grp')

uprIkCtrl = legGrpRGT[0] + '_IK_Zro_grp'
mc.parent(uprIkCtrl , 'chest_Gimbal_ctrl')

# FK
uprFKJnt = legGrpRGT[0] + '_FK_jnt'
mc.parent(uprFKJnt , 'null_FK_jnt_grp')

uprFkCtrl = legGrpRGT[0] + '_FK_Zro_grp'
mc.parent(uprFkCtrl , 'chest_Gimbal_ctrl')

footZro = footNam + '_IK_Zro_grp'
mc.parent(footZro , 'IK_ctrl_grp')



# connect switch fk / ik to controller
lcw.connectFkIkVis(	attrName = 'IK_FK_Arm_R' , uprNam = legGrpRGT[0]  , footIKGrp = 'footFrontlegRGT_IK_Zro_grp' )












#
# Back leg rig LFT
#

backlegLFTNam = blr.backLegRig(   jntList = ( 	'upLegBackLFT_bind_jnt'						,
												'midLegBackLFT_bind_jnt'					,
												'lowLegBackLFT_bind_jnt' 		) 			,

								pov = 'legPovBackLFT_tmpJnt'				,
								side = 'LFT'								,
								parentTo = 'hip_Gimbal_ctrl'				,
								placementAttr = 'IK_FK_Leg_L'								)



# back LFT footRoll
footIKLFT = blr.footRollBackRig(	

				rootNam = 'lowLegBackLFT_IK_jnt'													,
				jntLst = ['ankleBackLFT_bind_jnt' , 'ballRollBackLFT_bind_jnt' ,'toeRollBackLFT_bind_jnt']	,
				footBehav = ['footOutBack','footInBack','heelRollBack','toeRollBack','ballRollBack','ankleBack']		,
				placementAttr = 'IK_FK_Leg_L'													,
				side = 'LFT'																	,
				part = 'leg'																	,
				uprIK = backlegLFTNam[0]														,
				lwrIK = backlegLFTNam[1]														)



							
# 
# Parenting grp
#

uprIkJnt = backlegLFTNam[0] + '_IK_jnt'
mc.parent(uprIkJnt , 'hips_null_grp')

uprFKJnt = backlegLFTNam[0] + '_FK_jnt'
mc.parent(uprFKJnt , 'null_FK_jnt_grp')

uprIkCtrl = backlegLFTNam[0] + '_IK_Zro_grp'
mc.parent(uprIkCtrl , 'hip_Gimbal_ctrl')

uprFKCtrl = backlegLFTNam[0] + '_FK_Zro_grp'
mc.parent(uprFKCtrl , 'hip_Gimbal_ctrl')

lwrIkCtrl = backlegLFTNam[1] + '_IK_Zro_grp'
mc.parent( lwrIkCtrl , footIKLFT + '_IK_ctrl' )

mc.parent( footIKLFT + '_IK_Zro_grp'  , 'fly_ctrl' )


# connect switch fk / ik to controller
lcw.connectFkIkVis(	attrName = 'IK_FK_Leg_L' , uprNam = backlegLFTNam[0]  , footIKGrp = 'footlegLFT_IK_Zro_grp' )




#
# Back leg rig RGT
#

backlegRGTNam = blr.backLegRig(   jntList = ( 	'upLegBackRGT_bind_jnt'						,
												'midLegBackRGT_bind_jnt'					,
												'lowLegBackRGT_bind_jnt' 		) 			,

								pov = 'legPovBackRGT_tmpJnt'				,
								side = 'RGT'								,
								parentTo = 'hip_Gimbal_ctrl'				,
								placementAttr = 'IK_FK_Leg_L'								)
							





# back RGT footRoll
footIKRGT = blr.footRollBackRig(	

				rootNam = 'lowLegBackRGT_IK_jnt'													,
				jntLst = ['ankleBackRGT_bind_jnt' , 'ballRollBackRGT_bind_jnt' ,'toeRollBackRGT_bind_jnt']	,
				footBehav = ['footOutBack','footInBack','heelRollBack','toeRollBack','ballRollBack','ankleBack']		,
				placementAttr = 'IK_FK_Leg_L'													,
				side = 'RGT'																	,
				part = 'leg'																	,
				uprIK = backlegRGTNam[0]														,
				lwrIK = backlegRGTNam[1]														)	




# 
# Parenting grp
#

uprIkJnt = backlegRGTNam[0] + '_IK_jnt'
mc.parent(uprIkJnt , 'hips_null_grp')

uprFKJnt = backlegRGTNam[0] + '_FK_jnt'
mc.parent(uprFKJnt , 'null_FK_jnt_grp')

uprIkCtrl = backlegRGTNam[0] + '_IK_Zro_grp'
mc.parent(uprIkCtrl , 'hip_Gimbal_ctrl')

uprFKCtrl = backlegRGTNam[0] + '_FK_Zro_grp'
mc.parent(uprFKCtrl , 'hip_Gimbal_ctrl')

lwrIkCtrl = backlegRGTNam[1] + '_IK_Zro_grp'
mc.parent( lwrIkCtrl , footIKRGT + '_IK_ctrl' )

mc.parent( footIKRGT + '_IK_Zro_grp'  , 'fly_ctrl' )



# connect switch fk / ik to controller
lcw.connectFkIkVis(	attrName = 'IK_FK_Leg_R' , uprNam = backlegRGTNam[0]  , footIKGrp = 'footlegRGT_IK_Zro_grp' )




#
# Tail rig
#

spineFkRig.chainFK( chainList = ('tail01' , 'tail02' ,'tail03', 'tail04' ) , parentTo = 'hip_Gimbal_ctrl' ,ctrlType = 'neck_ctrlShape' , ctrlColor = 'red' , scale = [0.9, 0.9, 0.9] 	   )

# neck rig
spineFkRig.chainFK( chainList = ('neck01' , 'neck02' ) , parentTo = 'chest_Gimbal_ctrl' , ctrlType = 'neck_ctrlShape' , ctrlColor = 'red' , scale = [1.5, 1.5, 1.5] 	   )

# head rig
spineFkRig.chainFK( chainList = ('head' , 'nose' ) , parentTo = 'neck02_Gimbal_ctrl' , ctrlType = 'cube_ctrlShape' , ctrlColor = 'yellow' , scale = [6, 6, 6]   )

# ear rig LFT
spineFkRig.chainFK( chainList = ('ear01LFT' , 'ear02LFT', 'ear03LFT' , 'ear04LFT'   ) , parentTo = 'head_Gimbal_ctrl' , ctrlType = 'circle_ctrlShape' , ctrlColor = 'red' , scale = [8, 8, 8]   )

# ear rig RGT
spineFkRig.chainFK( chainList = ('ear01RGT' , 'ear02RGT', 'ear03RGT' , 'ear04RGT'   ) , parentTo = 'head_Gimbal_ctrl' , ctrlType = 'circle_ctrlShape' , ctrlColor = 'blue' , scale = [8, 8, 8]   )







# create local world controller
#lcw.localWorldOrient(    nameList = ('chest_ctrl','neck01_ctrl','head_ctrl','ear01LFT_ctrl','ear01RGT_ctrl','tail01_ctrl' )         )
#Fk ik ctrl is cause an error
lcw.localWorldOrient(    nameList = ('chest_ctrl','neck01_ctrl','head_ctrl','ear01LFT_ctrl','ear01RGT_ctrl','tail01_ctrl' , 'upLegFrontLFT_FK_ctrl' , 'upLegFrontRGT_FK_ctrl' , 'upLegBackLFT_FK_ctrl' , 'upLegBackRGT_FK_ctrl')    )




# Hide fk / ik null grp
for each in ('null_IK_jnt_grp' , 'null_FK_jnt_grp' , 'NOTOUCH_grp'):
	mc.setAttr('%s.visibility' %each , 0)


# Set scale segmentScaleCompensate
bJnt = mc.ls(sl = True)
for each in bJnt:
    mc.setAttr ("%s.segmentScaleCompensate" %each ,0)



# delete TMP
if mc.objExists('TMP_GRP'):
	mc.delete('TMP_GRP')