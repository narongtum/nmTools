
import maya.cmds as mc

from function.rigging.autoRig.bodyRig import finger_localCurlRig as finLocRig
reload(finLocRig)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

def creEachFingerGrp(  nameSpace='' , parentTo = 'ctrl_grp', side = '' , stickNam = '' ):
	'''
	Create Main empty grp with name
	@param finger: string of finger name
	@param side: side
	@param charScale: float
	'''
	# nameSpace = charName + elem
	region = mc.getAttr('%s.region' %stickNam )
	SticklocalFinger_grp = core.Null( nameSpace + region + 'LocalStick' + side + 'Zro' + '_grp' )
	SticklocalFinger_grp.parent( parentTo )
	return SticklocalFinger_grp.name




def creHandStick( nameSpace='' , fingerName = '' , side = '' , charScale = 1 , parentTo = ''):
	'''
	Create Local small stick controller

	'''
	# nameSpace = charName + elem

	name = nameSpace + fingerName + 'local' + side
	localFinger_ctrl = core.Dag(  name + '_ctrl' )
	localFinger_ctrl.nmCreateController('stick_ctrlShape')
	localFingerZro_grp = rigTools.zeroGroup( localFinger_ctrl )
	localFingerZro_grp.name = name + 'Zro_grp'
	print '''\n
	creHandStick
	'''


	localFinger_ctrl.editCtrlShape( axis = charScale * 1.2 )
	localFinger_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' ,'v')
	localFinger_ctrl.color = 'softBlue'
	localFinger_ctrl.hideArnoldNode()
	localFinger_ctrl.rotateOrder = 'xzy'

	# Parenting and positioning
	localFingerZro_grp.matchPosition( nameSpace + fingerName + '01' + side + '_bJnt' )
	localFingerZro_grp.matchRotation( nameSpace + fingerName + '01' + side + '_bJnt')

	# Relative rotation
	bindFinger = nameSpace + fingerName + '01' + side + '_bJnt'
	if side == 'LFT':
		localFingerZro_grp.attr('rotateX').value +=90
	elif side == 'RGT':
		localFingerZro_grp.attr('rotateX').value -=90
	else:
		mc.warning('Please verify side.')
		return None

	priorJnt_parCons = core.parentConstraint( bindFinger , localFingerZro_grp , mo = True)
	priorJnt_parCons.name = nameSpace + fingerName + 'Local'+ side + 'Grp' + '_parCons'

	localFingerZro_grp.parent( parentTo )

	# add for small stick attr
	localFinger_ctrl.addAttribute( longName = 'fingerBar' , niceName = '-'   , at ='enum', en = 'Finger' , keyable = True )
	localFinger_ctrl.addAttribute( longName = 'roll' , defaultValue = 0 , keyable = True )
	localFinger_ctrl.addAttribute( longName = 'stretch' , defaultValue = 0 , keyable = True )

	print localFinger_ctrl.name
	return str(localFinger_ctrl.name)



def creLocalFingerAttr( nameSpace, fingerName, side, ctrlName, numCtrl = 3 ):

	print ('''\n
	creLocalFingerAttr
	''')

	print ('numCtrl is:%d' %numCtrl)


	# nameSpace = charName + elem
	# fingerName = nameSpace + fingerName
	'''
	Create attribute for finger

	'''

	# beyond this this is for each finger
	# Stretch 
	# Create pma
	finLocRig.connect_LocOffGrp( nameSpace ,fingerName  , side  , numCtrl = numCtrl  , axis = 'Y' , type = 'translate' )

	# Create mdv
	finLocRig.creaeLocalPostStore( nameSpace ,side , fingerName   , fingerbehavior = 'stretch' )

	# Connect ctrl >>> mdv
	finLocRig._normalLocalCon( nameSpace ,fingerName , side  , ctrlName  , fingerbehavior = 'stretch'  )

	if numCtrl == 3:
		# mdv >>> offsetPma
		finLocRig.connectLocalPma( nameSpace ,fingerName , side , nameOfPost = ['stretch'] , numVal = '01' , axis = 'Y' , type = 'translate',numCtrl = numCtrl)
		finLocRig.connectLocalPma( nameSpace ,fingerName , side , nameOfPost = ['stretch'] , numVal = '02' , axis = 'Y' , type = 'translate',numCtrl = numCtrl)
		finLocRig.connectLocalPma( nameSpace ,fingerName , side , nameOfPost = ['stretch'] , numVal = '03' , axis = 'Y' , type = 'translate',numCtrl = numCtrl)

	elif numCtrl == 2:
		finLocRig.connectLocalPma( nameSpace ,fingerName , side , nameOfPost = ['stretch'] , numVal = '01' , axis = 'Y' , type = 'translate',numCtrl = numCtrl)
		finLocRig.connectLocalPma( nameSpace ,fingerName , side , nameOfPost = ['stretch'] , numVal = '02' , axis = 'Y' , type = 'translate',numCtrl = numCtrl)


	# End of Stretch
	# Roll 
	finLocRig.creaeLocalPostStore(  nameSpace ,side ,fingerName  ,fingerbehavior = 'roll' )
	# ctrl >>> mdv
	finLocRig._normalLocalCon( nameSpace ,fingerName  , side  , ctrlName   , fingerbehavior = 'roll'  )

	if numCtrl == 3:
		numOfctrl = ['01','02','03']
		
	elif numCtrl == 2:
		numOfctrl = ['01','02']

	# mdv >>> pma
	finLocRig.conLocRollPma( nameSpace ,fingerName, side  , nameOfPost = 'roll' , numOfctrl = numOfctrl , axis = 'X' , type = 'rotate' , inIndex = '5')
	# End of roll
	
	
	
	
def runLocalFingerRig( nameSpace= '', fingerName = '' , side = '' , charScale = 1 , parentTo = '',numCtrl=3):
	stickNam = creHandStick( nameSpace = nameSpace , fingerName = fingerName , side = side , charScale = charScale , parentTo = parentTo )
	creLocalFingerAttr(  nameSpace = nameSpace , fingerName = fingerName , side = side   , ctrlName = stickNam ,numCtrl=numCtrl  )



# Add function that collect function of this file.
def localFingerAllRig( nameSpace, parentTo, side, fingerName, charScale, numCtrl, stickNam ):
	localStick_grp = creEachFingerGrp(  nameSpace=nameSpace , parentTo = parentTo, side = side ,stickNam=stickNam )
	for finger in fingerName:
		runLocalFingerRig( 		nameSpace = nameSpace 			,
								fingerName = finger 	, 
								side = side 			, 
								charScale = charScale 	, 
								numCtrl = numCtrl 	,
								parentTo = localStick_grp )
	print '''\n
	# = = = = = = = = = Local Finger Rig Complete = = = = = = = = = #
	'''
