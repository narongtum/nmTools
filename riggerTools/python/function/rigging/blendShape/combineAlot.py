import maya.cmds as mc


allBshLst= [u'face_close_eye_R_bsh',
 u'face_mouth_oo_bsh',
 u'face_look_stun_bsh',
 u'face_look_down_bsh',
 u'face_look_up_bsh',
 u'face_look_R_L_side_bsh',
 u'face_look_R_side_bsh',
 u'face_look_R_R_side_bsh',
 u'face_look_L_R_side_bsh',
 u'face_look_L_side_bsh',
 u'face_look_L_L_side_bsh',
 u'face_eyebown_angry_bsh',
 u'face_eyebown_angry_L_bsh',
 u'face_eyebown_angry_R_bsh',
 u'face_eyebown_down_bsh',
 u'face_eyebown_down_L_bsh',
 u'face_eyebown_down_R_bsh',
 u'face_eyebown_up_bsh',
 u'face_eyebown_up_L_bsh',
 u'face_eyebown_up_R_bsh',
 u'face_mouth_sad_bsh',
 u'face_mouth_smile_bsh',
 u'face_mouth_O_bsh',
 u'face_mouth_A_bsh',
 u'face_mouth_U_bsh',
 u'face_mouth_R_bsh',
 u'face_mouth_E_bsh',
 u'face_upset_eye_bsh',
 u'face_happy_eye_bsh',
 u'face_happy_eye_L_bsh',
 u'face_happy_eye_R_bsh',
 u'face_close_eye_bsh',
 u'face_close_eye_L_bsh',
 u'face_browdown_L_bsh',
 u'face_browdown_R_bsh',
 u'face_browInnerUp_bsh',
 u'face_brow_raiser_L_bsh',
 u'face_brow_raiser_R_bsh',
 u'face_cheekPuff_bsh',
 u'face_eyeSquint_L_bsh',
 u'face_eyeSquint_R_bsh',
 u'face_eyeWide_L_bsh',
 u'face_eyeWide_R_bsh',
 u'face_LeftwardJaw_bsh',
 u'face_DropJaw_bsh',
 u'face_RightwardJaw_bsh',
 u'face_mounthFrown_bsh',
 u'face_mounthFrown_L_bsh',
 u'face_mounthFrown_R_bsh',
 u'face_mounthFunnel_bsh',
 u'face_mounthPucker_bsh',
 u'face_mounthSmile_L_bsh',
 u'face_mounthSmile_R_bsh',
 u'face_PRESET_Angry_1_bsh',
 u'face_PRESET_Brow_Angry_bsh',
 u'face_PRESET_Brow_Sad_bsh',
 u'face_PRESET_Cry_1_bsh',
 u'face_PRESET_Smug_face_1_bsh',
 u'face_PRESET_Smug_face_2_bsh' ,
 'face_default_bsh']
 
 
 
 

 
 
for each in allBshLst:
	if mc.objExists(each):

		# Reset transfromation
		mc.setAttr( each + '.translateX' , 0)
		mc.setAttr( each + '.translateY' , 0)

		# List child
		member = mc.listRelatives( each ,children=1)    
		print member[0]

		# Combine
		mc.polyUnite( member[0], member[1], ch = False , n='result' )
		mc.delete(each)
		mc.rename('result' , each)
	else:
		print '%s blendshape not found' %each
		continue


