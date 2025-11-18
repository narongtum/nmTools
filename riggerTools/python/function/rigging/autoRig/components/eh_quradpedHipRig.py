
def quradpedHipRig( 	nameSpace = '' , 
						parentTo = 'ctrl_grp'   , 
						tmpJnt = 	( 	'body_tmpJnt','hip_tmpJnt' , 
										'upperBody_tmpJnt' , 'chest_tmpJnt' , 
										'lowerBody_tmpJnt' )	,
						charScale = ''	 ):

	#... because of this is  Quadruped hipSpine merge hip and spine together 
	#charScale = 2					

	#... Create joint and rename to root
	rootJnt = core.Joint()
	rootJnt.name = nameSpace + 'root'


	#... Create spine joint
	lowerBody = core.Dag( tmpJnt[4] )
	chest = core.Dag( tmpJnt[3] )
	upperBody = core.Dag( tmpJnt[2] )
	hip = core.Dag( tmpJnt[1] )
	body = core.Dag( tmpJnt[0] )


	#... Create joint at Hip
	body_bJnt = rigTools.jointAt( body )
	lowerBody_bJnt = rigTools.jointAt( lowerBody )
	chest_bJnt = rigTools.jointAt( chest )
	upperBody_bJnt = rigTools.jointAt( upperBody )
	hip_bJnt = rigTools.jointAt( hip )


	lwrName = lowerBody.makeRawName()
	hipName = hip.makeRawName()
	bodyName = body.makeRawName()
	uprName = upperBody.makeRawName()
	chestName = chest.makeRawName()


	#hip_bJnt.rename('hip_bJnt')
	body_bJnt.name = nameSpace + bodyName+ '_bJnt'
	lowerBody_bJnt.name = nameSpace + lwrName + '_bJnt'
	chest_bJnt.name = nameSpace + chestName + '_bJnt'
	upperBody_bJnt.name = nameSpace + 'upperBody_bJnt'
	hip_bJnt.name = nameSpace + 'hip_bJnt'



	#... new hirachy
	#... body > upper > chest
	#... cog > lower > hip
	#... Parenting
	hip_bJnt.parent( lowerBody_bJnt )
	chest_bJnt.parent( upperBody_bJnt )

	upperBody_bJnt.parent( body_bJnt )
	lowerBody_bJnt.parent( body_bJnt )
	body_bJnt.parent( rootJnt )


	# Specify Group name
	# Specify temp joint name
	# find charscale
	# Create Main group
	name = nameSpace + 'hipSpineRig'
	hipRig_grp = core.Null()
	hipRig_grp.rename( name + '_' + 'grp')







	# Create COG controller to the hip animal reason
	part = nameSpace + 'cog'
	cog_ctrl = core.Dag( part + '_ctrl' )
	cog_ctrl.nmCreateController('cog_ctrlShape')
	cogZro_grp = rigTools.zeroGroup( cog_ctrl )
	cogZro_grp.name = part + 'CtrlZro_grp'
	cog_ctrl.editCtrlShape( axis = charScale * 2.8 )
	cogGmbl_ctrl = core.createGimbal( cog_ctrl )
	cog_ctrl.color = color_part_dict['secondary'] #...'white'
	cog_ctrl.rotateOrder = 'xzy'
	cogGmbl_ctrl.rotateOrder = 'xzy'
		
	# Parenting cog controller to cog_tmpJnt
	cogZro_grp.matchPosition( hip_bJnt )
	cog_ctrl.matchRotation( hip_bJnt  )





	print (lowerBody_bJnt.name) 
	# create lowerBody controller
	lowerBodyZro_grp , lowerBody_ctrl, lowerBody_gmblCtrl  = rigTools._creControl( 	nameSpace = nameSpace , name = lowerBody_bJnt.name  , 
													ctrlShape = 'neck_ctrlShape', charScale = 1.8 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = cogGmbl_ctrl.name , 
													rotation = (90,0,0)  )


	# create hip controller
	hipZro_grp , hip_ctrl , hip_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = hip_bJnt.name  , 
													ctrlShape = 'hips_ctrlShape', charScale = 1.9 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = lowerBody_gmblCtrl  , 
													rotation = (90,0,0)  )


	# create  body
	bodyZro_grp , body_ctrl, body_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = body_bJnt.name   , 
													ctrlShape = 'neck_ctrlShape', charScale = 2 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = cogGmbl_ctrl  , 
													rotation = (90,0,0)  )
													

	# create  upperBody
	upperBodyZro_grp , upperBody_ctrl, upperBody_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = upperBody_bJnt.name   , 
													ctrlShape = 'neck_ctrlShape', charScale = 2.2 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = body_gmblCtrl  , 
													rotation = (90,0,0)  )
													
																								
	# create  chest
	chestZro_grp , chest_ctrl, chest_gmblCtrl = rigTools._creControl( 	nameSpace = nameSpace , name = chest_bJnt.name   , 
													ctrlShape = 'cube_ctrlShape', charScale = 20.5 , 
													color = color_part_dict['primary'] , rotateOrder = 'xzy', parentTo = upperBody_gmblCtrl  , 
													rotation = (90,0,0)  )



	# move cog under to hipRig_grp
	cogZro_grp.parent( hipRig_grp )
	hipRig_grp.parent( parentTo )

	print ('\n#### End of %s Rig ####' %(part))
	print('\n\n\n\n\n')
	return chest_bJnt.name , hip_bJnt.name