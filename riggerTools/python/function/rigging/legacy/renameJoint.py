
partName = (
				('head01_ctrl' , 'head_ctrl'),
				('head01_gmbCtrl' , 'head_Gimbal_ctrl'),

				('spine03Fk_ctrl' , 'upperChest_ctrl'),
				('spine02Fk_ctrl' , 'chest_ctrl'),
				('spine01Fk_ctrl' , 'spine_ctrl'),

				# hand fk LFT
				('upperArmFkLFT_ctrl' , 'upperArmLFT_FK_ctrl'),
				('lowerArmFkLFT_ctrl' , 'lowerArmLFT_FK_ctrl'),
				('handFkLFT_ctrl' , 	'handLFT_FK_ctrl'),

				# hand ik LFT
				('handIkLFT_ctrl' , 	'handLFT_IK_ctrl'),

				# leg fk LFT
				('upperLegFkLFT_ctrl','upperLegLFT_FK_ctrl'),
				('lowerLegFkLFT_ctrl','lowerLegLFT_FK_ctrl'),
				('ankleFkLFT_ctrl','footLFT_FK_ctrl'),
				('ballLegFkLFT_ctrl','toesLFT_FK_ctrl'),

				# leg ik LFT
				('footIkLFT_ctrl','footLFT_IK_ctrl'),
				('footOutlegIKLFT_ctrl','footOutLFT_IK_ctrl'),
				('footInlegIKLFT_ctrl','footInLFT_IK_ctrl'),
				('heelRolllegIKLFT_ctrl','heelRollLFT_IK_ctrl'),
				('toeRolllegIKLFT_ctrl','toesRollLFT_IK_ctrl'),
				('ballRolllegIkLFT_ctrl', 'ballRollLFT_IK_ctrl'),



				# hand fk RGT
				('upperArmFkRGT_ctrl' , 'upperArmRGT_FK_ctrl'),
				('lowerArmFkRGT_ctrl' , 'lowerArmRGT_FK_ctrl'),
				('handFkRGT_ctrl' , 	'handRGT_FK_ctrl'),

				# hand ik RGT
				('handIkRGT_ctrl' , 	'handRGT_IK_ctrl'),

				# leg fk RGT
				('upperLegFkRGT_ctrl','upperLegRGT_FK_ctrl'),
				('lowerLegFkRGT_ctrl','lowerLegRGT_FK_ctrl'),
				('ankleFkRGT_ctrl','footRGT_FK_ctrl'),
				('ballLegFkRGT_ctrl','toesRGT_FK_ctrl'),

				# leg ik RGT
				('footIkRGT_ctrl','footRGT_IK_ctrl'),
				('footOutlegIKRGT_ctrl','footOutRGT_IK_ctrl'),
				('footInlegIKRGT_ctrl','footInRGT_IK_ctrl'),
				('heelRolllegIKRGT_ctrl','heelRollRGT_IK_ctrl'),
				('toeRolllegIKRGT_ctrl','toesRollRGT_IK_ctrl'),
				('ballRolllegIkRGT_ctrl', 'ballRollRGT_IK_ctrl')


				)





'''
for each in partName:
	print (each[0] )
	print (each[1])
	print ('and\n')'''




for each in partName:
	try:
		mc.rename( each[0] , each[1] )
	except:
		print each[0] + 'may having a problem'
		continue
	

print 'Change name complete.'




