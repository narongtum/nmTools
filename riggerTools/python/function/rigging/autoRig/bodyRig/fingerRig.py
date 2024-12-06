# FK Five Finger Rig
import maya.cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc
reload(misc)

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)
color_part_dict = mnd.COLOR_part_dict

# just create fk at finger joint
def fingerRig( 			nameSpace = '' 						,
						side = 'LFT', 
						fingerNum = 3 , 
						fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'] , 
						zroName = 'Zro_grp' , 
						charScale = 1 , 
						priorCtrl = ''						,
						priorJnt = ''						,
						parentTo = 'ctrl_grp' ,
						stickNam = '' 					 ):

	core.makeHeader(	'Start of %s%s Rig' %('finger',side)	)

	# Use hand joint name instead
	rawNam = misc.splitName( priorJnt )[0]
	rawNam = rawNam.replace( side,'' )
	handJnt = priorJnt

	# nameSpace = charName + elem
	fGrp = '%s%sFinger%s_grp' %( nameSpace, rawNam, side )
	fJnt = '%s%s%s_tmpJnt' %( nameSpace, rawNam, side )
	logger.info(fJnt)



	# nameSpace = charName + elem
	# fGrp = '%sfinger%s_grp' %( nameSpace,side )
	# fJnt = '%shand%s_tmpJnt' %( nameSpace,side )
	# print fJnt
	# handJnt = '%shand%s_bJnt' %( nameSpace,side )
	# handJnt = priorJnt
	mc.group( n = fGrp, em = 1)
	mc.parentConstraint( handJnt, fGrp, mo = 0, w = 1 , name = nameSpace + handJnt + '_parCons ')
	
	
	for i in range(len(fingerName)): # create & parent [ bJnt ]


		for n in range(fingerNum):
			name = fingerName[i] + '%02d' %(n+1) + side
			tmpJnt = core.Dag( nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_tmpJnt')
			logger.info(tmpJnt.name)
			bJnt = core.Dag( nameSpace + name + '_bJnt')
			jnt = rigTools.jointAt( tmpJnt )#create bJnt at tmpJnt
	
			jnt.rename( bJnt)

			if 'thumb' in fingerName[i]:
				jointLabel = 'thumb'
			elif 'index' in fingerName[i]:
				jointLabel = 'index finger'
			elif 'middle' in fingerName[i]:
				jointLabel = 'mid finger'
			elif 'ring' in fingerName[i]:
				jointLabel = 'ring finger'	
			elif 'pinky' in fingerName[i]:
				jointLabel = 'pinky finger'	

			jnt.setLable( side, jointLabel )
			
			if n > 0:
				upName = nameSpace + fingerName[i] + '%02d' %n + side
				upJnt = core.Dag(upName + '_bJnt')

				bJnt.parent( upJnt )
			elif n == 0:
				bJnt.parent( handJnt )

			
	for i in range(len(fingerName)):
		for n in range(fingerNum):
			name = fingerName[i] + '%02d' %(n+1) + side
			tmpJnt = core.Dag( nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_tmpJnt') 
			#tmpJnt = name + '_tmpJnt'

			bJnt = nameSpace + name + '_bJnt'
			
			if side == 'LFT':
				sideColor = color_part_dict['left'] #... blue
			elif side == 'RGT':
				sideColor = color_part_dict['right'] #... red
				
			ctrl = core.Dag( nameSpace + name + '_ctrl' ) # Create Ctrl
			ctrl.nmCreateController('circle_ctrlShape')
			ctrl.editCtrlShape( axis =  charScale * 0.8 )
			ctrl.color = sideColor
			
			zGrp = rigTools.zeroGroup( ctrl ) # Create zGrp
			# zGrp.name = name + '_zGrp' 
			zGrp.name = nameSpace + name + zroName
			
			zGrp.matchAll( tmpJnt )
			
			if n > 0:
				upName = nameSpace + fingerName[i] + '%02d' %n + side
				upCtrl = core.Dag(upName + '_ctrl')
				zGrp.parent( upCtrl )
			
			elif n == 0: 
				zGrp.parent( fGrp )

			logger.info(nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_parConsXxx')	
			core.parentConstraint( ctrl, bJnt , name = nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_parCons')
	
	handStick_ctrl = core.Dag( stickNam )
	finger_grp = core.Dag( fGrp )





	# get region name from attr grp
	region = mc.getAttr('%s.region' %stickNam )

	# Attr scale name
	if region == 'arm':
		stickScalNam = 'hand'
	else:
		stickScalNam = region

	# connect message of scale grp
	# finger_grp.attr('message') >> stick_ctrl.attr('scale_grp')
	# where is scale_Attr from
	logger.info( 'WHAT IT IS: '+ handStick_ctrl.name )
	scale_Attr = mc.listConnections( handStick_ctrl.name + '.' + 'scale_Attr' )[0]

	# Beware Error !!! solid variation
	handStick_ctrl.attr( scale_Attr ) >> finger_grp.attr( 'sx' )
	handStick_ctrl.attr( scale_Attr ) >> finger_grp.attr( 'sy' )
	handStick_ctrl.attr( scale_Attr ) >> finger_grp.attr( 'sz' )


	mc.parent( fGrp , parentTo)
	mc.select(deselect = True)
	
	return fGrp








#... Finger rig update version

def fingerRigExt( 			nameSpace = '' 						,
							side = 'LFT', 
							fingerNum = 3 , 
							fingerName = ['thumb', 'index', 'middle', 'ring', 'pinky'] , 
							zroName = 'Zro_grp' , 
							charScale = 1 , 
							priorCtrl = ''						,
							priorJnt = ''						,
							parentTo = 'ctrl_grp' ,
							stickNam = '' 					 ):

	core.makeHeader('Start of %s%s Rig' %('finger',side)	)
	logger.info('#### exec module of %s ####' %(__name__))

	# Use hand joint name instead
	rawNam = misc.splitName( priorJnt )[0]
	rawNam = rawNam.replace(side,'')
	handJnt = priorJnt

	# nameSpace = charName + elem
	fGrp = '%s%sFinger%s_grp' %( nameSpace, rawNam, side )
	fJnt = '%s%s%s_tmpJnt' %( nameSpace, rawNam, side )
	logger.info(fJnt)

	mc.group( n = fGrp, em = 1)
	mc.parentConstraint( handJnt, fGrp, mo = 0, w = 1 , name = nameSpace + handJnt + '_parCons ')

	
	
	for i in range(len(fingerName)): # create & parent [ bJnt ]


		for n in range(fingerNum):
			name = fingerName[i] + '%02d' %(n+1) + side
			tmpJnt = core.Dag( nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_tmpJnt')
			logger.info( tmpJnt.name)
			bJnt = core.Dag( nameSpace + name + '_bJnt')
			jnt = rigTools.jointAt( tmpJnt )#create bJnt at tmpJnt
	
			jnt.rename( bJnt)

			if fingerName[i] == 'thumb':
				jointLabel = 'thumb'
			elif fingerName[i] == 'index':
				jointLabel = 'index finger'
			elif fingerName[i] == 'middle':
				jointLabel = 'mid finger'
			elif fingerName[i] == 'ring':
				jointLabel = 'ring finger'	
			elif fingerName[i] == 'pinky':
				jointLabel = 'pinky finger'	

			jnt.setLable( side, jointLabel )
			
			if n > 0:
				upName = nameSpace + fingerName[i] + '%02d' %n + side
				upJnt = core.Dag(upName + '_bJnt')

				bJnt.parent( upJnt )
			elif n == 0:
				bJnt.parent( handJnt )

			
	for i in range(len(fingerName)):
		for n in range(fingerNum):
			name = fingerName[i] + '%02d' %(n+1) + side
			tmpJnt = core.Dag( nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_tmpJnt') 
			#tmpJnt = name + '_tmpJnt'

			bJnt = nameSpace + name + '_bJnt'
			
			if side == 'LFT':
				sideColor = color_part_dict['left'] #... blue
			elif side == 'RGT':
				sideColor = color_part_dict['right'] #... red
				
			ctrl = core.Dag( nameSpace + name + '_ctrl' ) # Create Ctrl
			ctrl.nmCreateController('circle_ctrlShape')
			ctrl.editCtrlShape( axis =  charScale * 0.8 )
			ctrl.color = sideColor
			
			zGrp = rigTools.zeroGroup( ctrl ) # Create zGrp
			# zGrp.name = name + '_zGrp' 
			zGrp.name = nameSpace + name + zroName
			
			zGrp.matchAll( tmpJnt )
			
			if n > 0:
				upName = nameSpace + fingerName[i] + '%02d' %n + side
				upCtrl = core.Dag(upName + '_ctrl')
				zGrp.parent( upCtrl )
			
			elif n == 0: 
				zGrp.parent( fGrp )
				
			core.parentConstraint( ctrl, bJnt , name = nameSpace + name + '_parCons')
	
	handStick_ctrl = core.Dag( stickNam )
	finger_grp = core.Dag( fGrp )

	# get region name from attr grp
	region = mc.getAttr('%s.region' %stickNam )

	# Beware Error !!! solid variation
	handStick_ctrl.attr( 'handScale' ) >> finger_grp.attr( 'sx' )
	handStick_ctrl.attr( 'handScale' ) >> finger_grp.attr( 'sy' )
	handStick_ctrl.attr( 'handScale' ) >> finger_grp.attr( 'sz' )


	mc.parent( fGrp , parentTo)
	mc.select(deselect = True)

	print('#### End of %s %s Rig ####'%(region,side))
	print('\n\n\n\n\n')
	return fGrp











""" this function is for five joint finger """
def baseFingerRig(
					nameSpace = '' ,						
					side = 'LFT',
					fingerNum = 3 ,
					fingerName = ('thumb', 'index', 'middle', 'ring', 'pinky'),
					zroName = 'Zro_grp',
					charScale = 1 ,
					priorCtrl = '',
					priorJnt = 'handLFT_bJnt' ,
					parentTo = 'ctrl_grp',
					stickNam = 'stickNamLFT' ,
					
											):

	






	# from function.rigging.autoRig.base import core
	# reload(core)

	# from function.rigging.autoRig.base import rigTools
	# reload(rigTools)


	if side == 'LFT':
		sideColor = color_part_dict['left'] #... blue
	elif side == 'RGT':
		sideColor = color_part_dict['right'] #... red


	# Use hand joint name instead
	rawNam = misc.splitName( priorJnt )[0]
	rawNam = rawNam.replace(side,'')
	handJnt = priorJnt

	# nameSpace = charName + elem
	fGrp = '%s%sFinger%s_grp' %( nameSpace, rawNam, side )
	fJnt = '%s%s%s_tmpJnt' %( nameSpace, rawNam, side )
	logger.info(fJnt)

	mc.group( n = fGrp, em = 1)
	mc.parentConstraint( handJnt, fGrp, mo = 0, w = 1 , name = nameSpace + handJnt + '_parCons ')


	baseFinger_ctrl_list = []

	# = = = = = create base finger name

	for i in range(len(fingerName)):
		name = fingerName[i] + 'Base' + side
		# must alway have name space in tmpJnt name 
		tmpJnt = core.Dag(nameSpace + name + '_tmpJnt' )

		bJnt = rigTools.jointAt( tmpJnt )

		bJnt.rename(nameSpace + name + '_bJnt')

		# set label
		if 'thumb' in fingerName[i]:
			jointLabel = 'thumb'
		elif 'index' in fingerName[i]:
			jointLabel = 'index finger'
		elif 'middle' in fingerName[i]:
			jointLabel = 'mid finger'
		elif 'ring' in fingerName[i]:
			jointLabel = 'ring finger'	
		elif 'pinky' in fingerName[i]:
			jointLabel = 'pinky finger'	

		bJnt.setLable( side, jointLabel )

		# parent
		bJnt.parent( handJnt )


		#... create controller	

		# if side == 'LFT':
		# 	sideColor = color_part_dict['left'] #... blue
		# elif side == 'RGT':
		# 	sideColor = color_part_dict['right'] #... red

		ctrl = core.Dag( nameSpace + name + '_ctrl' ) # Create Ctrl
		ctrl.nmCreateController('circle_ctrlShape')
		ctrl.editCtrlShape( axis =  charScale * 0.8 )
		ctrl.color = sideColor


		baseZro_grp = rigTools.zroGrpWithOffset( ctrl ) # Create baseZro_grp
		# baseZro_grp.name = name + '_baseZro_grp' 
		baseZro_grp.name = nameSpace + name + zroName

		baseZro_grp.matchAll( bJnt )
		baseZro_grp.parent( fGrp )

		baseFinger_ctrl_list.append(ctrl.name)

		core.parentConstraint( ctrl, bJnt , name = name + '_parCons')




	# # # # # # # # # # # # # # # # # # # # # 	
	# the rest finger zone
	# # # # # # # # # # # # # # # # # # # # # 

	# # # # # # # crate joint
	for i in range(len(fingerName)): 
		for n in range(fingerNum):
			name = fingerName[i] + '%02d' %(n+1) + side
			tmpJnt = core.Dag( nameSpace + name + '_tmpJnt')


			bJnt = rigTools.jointAt( tmpJnt )#create bJnt at tmpJnt

			bJnt.rename( nameSpace + name + '_bJnt')

			if 'thumb' in fingerName[i]:
				jointLabel = 'thumb'
			elif 'index' in fingerName[i]:
				jointLabel = 'index finger'
			elif 'middle' in fingerName[i]:
				jointLabel = 'mid finger'
			elif 'ring' in fingerName[i]:
				jointLabel = 'ring finger'	
			elif 'pinky' in fingerName[i]:
				jointLabel = 'pinky finger'	

			bJnt.setLable( side, jointLabel )
			
			if n > 0:
				upName = nameSpace + fingerName[i] + '%02d' %n + side
				upJnt = core.Dag(upName + '_bJnt')

				bJnt.parent( upJnt )
			elif n == 0: # parent to base finger instead
				# bJnt.parent( handJnt )
				baseFinger = fingerName[i] + 'Base' + side + '_bJnt'
				bJnt.parent( baseFinger )

			
	for i in range(len(fingerName)):
		for n in range(fingerNum):
			name = fingerName[i] + '%02d' %(n+1) + side
			tmpJnt = core.Dag( nameSpace + name + '_tmpJnt') 

			bJnt =  nameSpace + name + '_bJnt'
			
			# if side == 'LFT':
			# 	sideColor = 'red'
			# elif side == 'RGT':
			# 	sideColor = 'blue'
				
			ctrl = core.Dag( nameSpace + name + '_ctrl' ) # Create Ctrl
			ctrl.nmCreateController('circle_ctrlShape')
			ctrl.editCtrlShape( axis =  charScale * 0.8 )
			ctrl.color = sideColor
			
			zGrp = rigTools.zeroGroup( ctrl ) # Create zGrp
			# zGrp.name = name + '_zGrp' 
			zGrp.name = nameSpace + name + zroName
			
			zGrp.matchAll( tmpJnt )
			
			if n > 0:
				upName = nameSpace + fingerName[i] + '%02d' %n + side
				upCtrl = core.Dag(upName + '_ctrl')
				zGrp.parent( upCtrl )
			
			elif n == 0:
				# parent to base joint 
				zGrp.parent(baseFinger_ctrl_list[i])
				# zGrp.parent( fGrp )
			# constraint from controller to bJnt
			core.parentConstraint( ctrl, bJnt , name = nameSpace + fingerName[i] + '%02d' %(n+1) + side + '_parCons')

	mc.parent( fGrp , parentTo)
	mc.select(deselect = True)
	print('\n')
	print ('End of five finger %s rig' %(side ))
	print('\n\n\n\n\n')



	return fGrp





# run after finish finger rig
def connect_finger_value(stickNam = '',fingerName = ('thumb', 'index', 'middle', 'ring', 'pinky'), side = 'LFT', defaultValue = 0.25):
	
	stick_ctrl = core.Dag( stickNam )
	stick_ctrlShape = core.Dag( stick_ctrl.shape )



	for each in fingerName:
		# Create attr in stick controller
		stick_ctrlShape.addAttribute( longName = each + 'Base' , defaultValue = defaultValue , keyable = True )

		offset_one = core.Dag('%s01%sOffset_grp' %(each , side) )
		offset_base = core.Dag('%sBase%sOffset_grp' %(each , side) )
		resistance = core.MDLWithMul('%sBaseResistance%s' %(each,side) , dv = 0.25)

		offset_one.attr('rotateX') >> resistance.attr( 'input1' )
		resistance.attr( 'output' ) >> offset_base.attr('rotateX')
		#... Conect value from stick to MDL
		#... Fixed specname cause error to use variable instead
		stick_ctrlShape.attr( each + 'Base' ) >> resistance.attr('multiply')
	print ('\nEnd of Connect five finger %s rig' %(side ))