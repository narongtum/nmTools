from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.components.fingerRig import eh_finger_mainCurlRig as finOffRig
reload(finOffRig)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

import maya.cmds as mc

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


# =================================
# - Exec Function for main(all) finger -
# =================================

def mainFingerCurlRig(      nameSpace ,             
							fingerbehavior = None  , 
							fingerName = ('thumb','index','middle','ring','pinky') , 
							side = 'LFT'  , 
							numCtrl = 3 , zroNam = 'Zro_grp' , 
							offsetNam = 'Offset_grp'        ,
							stickNam = 'armStickLFT_ctrl'   ,
							handNam = 'handLFT_bJnt'        ):

	core.makeHeader('main Finger Curl Rig')

	if fingerbehavior is None:
		fingerbehavior = mnd.FINGER_dict['fingerbehavior']

	# Check if stick controller exists
	if not mc.objExists(stickNam):
		logger.error(f"Stick controller '{stickNam}' does not exist! Aborting finger curl setup.")
		return
	
	stick_ctrl = core.Dag( stickNam )
	if not stick_ctrl.shape:
		logger.error(f"Stick controller '{stickNam}' has no shape node! Aborting finger curl setup.")
		return
		
	stick_ctrlShape = core.Dag( stick_ctrl.shape )

	# Add namespace safely
	fingerNameWithNs = [f"{nameSpace}{each}" for each in fingerName]

	# =================================
	# - Global finger Curl LFT -
	# =================================


	# Declair name variable
	fingerNameWithNs, fingerbehavior, side, numCtrl, zroNam, offsetNam, stickNam = finOffRig.defineVariable( fingerbehavior, fingerNameWithNs, side, numCtrl, zroNam, offsetNam, stickNam )

	# [1] create each offset group
	# run relax function    
	
	offsetLst = finOffRig.createOffsetGrp(  side , fingerNameWithNs , numCtrl , zroNam , offsetNam )


	# [2]
	# create multiply divide for each finger behavior except relax 
	finOffRig.creaePostStore( nameSpace , side , fingerbehavior  )


	# [3] create multiplyDivide for relax behavior
	# find multiplier number
	for each in fingerNameWithNs:

		amp = 1
		if 'thumb' in each:
			amp = 1.1
		elif 'index' in each:
			amp = 2.1
		elif 'middle' in each:
			amp = 3.1
		elif 'ring' in each:
			amp = 4.1
		elif 'pinky' in each:
			amp = 5.1

		finOffRig.creRelax( side, finName = each,   amp = amp )


	# [3.2] create multiplyDivide add for cup behavior
	# find multiplier number
	for each in fingerNameWithNs:

		amp = 1
		if 'thumb' in each:
			amp = 0 # thumb not move in cup preset
		elif 'index' in each:
			amp = 0.1
		elif 'middle' in each:
			amp = 0.8
		elif 'ring' in each:
			amp = 1.3
		elif 'pinky' in each:
			amp = 1.9

		finOffRig.creCup( side, finName = each,   amp = amp )




	# [4.2]
	# connect MDV connection to each offset grp in x axis
	# we can't change 'X' to lower case because of it will crash error
	ampRxGrp = finOffRig.connectToOffGrp( fingerNameWithNs,  fingerbehavior ,  numCtrl, side , offsetLst , axis = 'X' , type = 'rotate' )


	# [11]
	# [11.5] #Connect spread to offset just of grp 01
	# Create offset group for Z axis
	finOffRig.connectToOffGrp( fingerNameWithNs,  fingerbehavior ,  numCtrl, side , offsetLst , axis = 'Z' , type = 'rotate')

	
	# [11]  testing add translate x
	ampGrp = finOffRig.connectToOffGrp( fingerNameWithNs,  fingerbehavior ,  numCtrl, side , offsetLst , axis = 'X' , type = 'translate')
	print ('Multiply value for finger.')
	# Set new value for amp grp of wide finger esp
	for each in ampGrp:
		# set value for number 01 only
		if '01Tx' in each:
			logger.info(each)
			if 'index' in each:
				mc.setAttr(f'{each}.multiply', 0.11)
			elif 'middle' in each:
				mc.setAttr(f'{each}.multiply', 0.04)
			elif 'ring' in each:
				mc.setAttr(f'{each}.multiply', -0.04)
			elif 'pinky' in each:
				mc.setAttr(f'{each}.multiply', -0.11)
			elif 'thumb' in each:
				mc.setAttr(f'{each}.multiply', 0.04)
			else:
				mc.setAttr(f'{each}.multiply', 1)
		else:
			mc.setAttr(f'{each}.multiply', 1)


	# [6.5]
	# add finger curl attr name to stick.shape
	for each in ampRxGrp:
		# Get value from MDL node
		multiply_Val = mc.getAttr( f"{each}.multiply" )

		try:
			# Create name for attr name in stick.shape
			indexAmp = each.index( 'Amp' )
			# Result : index02TxLFTAmp_mdl >>> [:indexIn] >>> index02TxLFT >>> [-3] >>> index02Tx
			cleanNam = ( each[:indexAmp-3] )
			# Add value multiplier here
			stick_ctrlShape.addAttribute( longName = cleanNam , defaultValue = multiply_Val , keyable = True )


			mc.connectAttr(	f'{stick_ctrlShape.name}.{cleanNam}' , f'{each}.multiply' )
			logger.info(f'{stick_ctrlShape.name}.{cleanNam}' +'>>>'+ f'{each}.multiply')
		except ValueError:
			logger.warning(f"Could not parse 'Amp' in string '{each}', skipping stick.shape attribute creation.")

	# [4.3] add separator attr
	# Fixing nicename having red warning about '-'
	misc.addAttribute( objects = [  str(stick_ctrl.name) ] , longName = ['fingerBar'], niceName = ['_'] , at ='enum' , en = 'Finger' , lock = True , keyable = True)


	# [6]
	# Create stick attr 
	finOffRig.doCreateAttr( stick_ctrl.name , fingerbehavior  )








	# [7.1] 
	# Create connect spread , roll , fist to stick execept relax
	finOffRig.normalConnect( nameSpace , stick_ctrl.name , fingerbehavior ,side)


	# [8]
	# connection stick ctrl to for relax mdv
	for each in fingerNameWithNs:
		finOffRig.conxAdv( stick_ctrl.name, side, finger = 'relax', position = f'{each}Relax' )


	# [8.2] Add for cup connection stick ctrl to for relax mdv
	for each in fingerNameWithNs:
		finOffRig.conxAdv( stick_ctrl.name, side, finger = 'cup', position = f'{each}Cup' )

	# [9]
	# connect mdv >>> all offset_RX_grp
	# Using new condition 
	# if numCtrl = 3  
	# we need result : 01 ,02 ,03

	

	valueCtrl = [f'{i:02d}' for i in range(1, numCtrl + 1)]

	for num in valueCtrl:
		finOffRig.connectPma(  nameSpace  ,fingerNameWithNs,side  ,   numCtrl, nameOfPost = ('fist','roll'),  numVal = num   )
		print (f'connect to all grp {num}')



	# teswt for test for wide
	finOffRig.connectPma(  nameSpace  ,fingerNameWithNs,side	,	numCtrl, nameOfPost = ( ['wide'] ),	numVal = '01' , type = 'translate'	)

	# Add spread finger behavior
	finOffRig.connectSpreadPma( 	nameSpace ,fingerNameWithNs , side , nameOfPost = ['spread'], 
									numVal ='01' , axis = 'Z' ,numCtrl = numCtrl)


	# [10.1]
	for each in fingerNameWithNs:
		finOffRig.doConnectRelax( side, figName = each  , finPst = 'Relax'  , numCtrl = numCtrl )


	# [10.5] add for cup finger
	for each in fingerNameWithNs:
		finOffRig.doConnectRelax( side, figName = each  , finPst = 'Cup'  , numCtrl = numCtrl , inputIndex = (5,6,7) )

	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #
	# 				Adding message to attr
	# = = = = = = = = = = = = = = = = = = = = = = = = = = = #

	
	print ('\n\t# = = = = = = update message\n')


	metaName = mnd.MESSAGE_dict['meta'][0]
	attr_path = f'{stick_ctrl.name}.{metaName}'
	print(attr_path)

	if mc.objExists(attr_path):
		connections = mc.listConnections(attr_path)
		if connections:
			meta_node = connections[0]
			if mc.objExists(meta_node):
				keys_list = list(mnd.FINGER_dict.keys())
				second_key = keys_list[1]
		
				finger_behavior = mnd.FINGER_dict[second_key]
		
				if not mc.objExists(f"{meta_node}.{second_key}"):
					mc.addAttr(meta_node, dataType = 'string' , longName = second_key )
				mc.setAttr(f"{meta_node}.{second_key}", finger_behavior, type = 'string')
				mc.setAttr(f"{meta_node}.{second_key}", lock = True)
	else:
		logger.warning(f"Attribute {attr_path} does not exist. Skipping meta node update.")

	print (f'#### End of lobal finger curl {side} Rig ####')
	print('\n\n\n\n\n')
