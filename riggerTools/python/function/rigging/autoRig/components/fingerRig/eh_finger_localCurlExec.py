
import maya.cmds as mc
import logging

from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.autoRig.components.fingerRig import eh_finger_localCurlRig as finLocRig
reload(finLocRig)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)


def creEachFingerGrp( nameSpace='', parentTo='ctrl_grp', side='', stickNam='' ):
	'''
	Create Main empty grp with name
	@param side: side
	'''
	region = 'arm'
	if mc.objExists(f"{stickNam}.region"):
		region = mc.getAttr(f"{stickNam}.region")
	else:
		logger.warning(f"Attribute 'region' not found on '{stickNam}'. Defaulting to '{region}'.")

	SticklocalFinger_grp = core.Null( f"{nameSpace}{region}LocalStick{side}Zro_grp" )
	SticklocalFinger_grp.parent( parentTo )
	return SticklocalFinger_grp.name


def creHandStick( nameSpace='', fingerName='', side='', charScale=1, parentTo=''):
	'''
	Create Local small stick controller
	'''
	name = f"{nameSpace}{fingerName}local{side}"
	localFinger_ctrl = core.Dag( f"{name}_ctrl" )
	localFinger_ctrl.nmCreateController('stick_ctrlShape')
	
	localFingerZro_grp = rigTools.zeroGroup( localFinger_ctrl )
	localFingerZro_grp.name = f"{name}Zro_grp"
	
	print ('\n\tcreHandStick')

	localFinger_ctrl.editCtrlShape( axis = charScale * 1.2 )
	localFinger_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' ,'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' ,'v')
	localFinger_ctrl.color = 'softBlue'
	localFinger_ctrl.hideArnoldNode()
	localFinger_ctrl.rotateOrder = 'xzy'

	bindFinger = f"{nameSpace}{fingerName}01{side}_bJnt"
	if not mc.objExists(bindFinger):
		logger.error(f"Bind finger joint '{bindFinger}' not found!")
		return None

	# Parenting and positioning
	localFingerZro_grp.matchPosition( bindFinger )
	localFingerZro_grp.matchRotation( bindFinger )

	# Relative rotation
	if side == 'LFT':
		localFingerZro_grp.attr('rotateX').value += 90
	elif side == 'RGT':
		localFingerZro_grp.attr('rotateX').value -= 90
	else:
		mc.warning('Please verify side.')
		return None

	priorJnt_parCons = core.parentConstraint( bindFinger , localFingerZro_grp , mo = True)
	priorJnt_parCons.name = f"{nameSpace}{fingerName}Local{side}Grp_parCons"

	localFingerZro_grp.parent( parentTo )

	# add for small stick attr
	localFinger_ctrl.addAttribute( longName = 'fingerBar' , niceName = '-' , at ='enum', en = 'Finger' , keyable = True )
	localFinger_ctrl.addAttribute( longName = 'roll' , defaultValue = 0 , keyable = True )
	localFinger_ctrl.addAttribute( longName = 'stretch' , defaultValue = 0 , keyable = True )

	print (localFinger_ctrl.name)
	return localFinger_ctrl.name


def creLocalFingerAttr( nameSpace, fingerName, side, ctrlName, numCtrl=3 ):

	print ('\n\tcreLocalFingerAttr')
	print (f'numCtrl is:{numCtrl}')

	# Create pma
	finLocRig.connect_LocOffGrp( nameSpace, fingerName, side, numCtrl=numCtrl, axis='Y', type='translate' )

	# Create mdv
	finLocRig.creaeLocalPostStore( nameSpace, side, fingerName, fingerbehavior='stretch' )

	# Connect ctrl >>> mdv
	finLocRig._normalLocalCon( nameSpace, fingerName, side, ctrlName, fingerbehavior='stretch' )

	# mdv >>> offsetPma
	for i in range(1, numCtrl + 1):
		numVal = f"{i:02d}"
		finLocRig.connectLocalPma( nameSpace, fingerName, side, nameOfPost=['stretch'], numVal=numVal, axis='Y', type='translate', numCtrl=numCtrl )

	# End of Stretch
	# Roll 
	finLocRig.creaeLocalPostStore( nameSpace, side, fingerName, fingerbehavior='roll' )
	
	# ctrl >>> mdv
	finLocRig._normalLocalCon( nameSpace, fingerName, side, ctrlName, fingerbehavior='roll' )

	numOfctrl = [f"{i:02d}" for i in range(1, numCtrl + 1)]

	# mdv >>> pma
	finLocRig.conLocRollPma( nameSpace, fingerName, side, nameOfPost='roll', numOfctrl=numOfctrl, axis='X', type='rotate', inIndex='5' )
	# End of roll
	

def runLocalFingerRig( nameSpace='', fingerName='', side='', charScale=1, parentTo='', numCtrl=3):
	stickNam = creHandStick( nameSpace=nameSpace, fingerName=fingerName, side=side, charScale=charScale, parentTo=parentTo )
	if stickNam:
		creLocalFingerAttr( nameSpace=nameSpace, fingerName=fingerName, side=side, ctrlName=stickNam, numCtrl=numCtrl )


# Add function that collect function of this file.
def localFingerAllRig( nameSpace, parentTo, side, fingerName, charScale, numCtrl, stickNam ):
	localStick_grp = creEachFingerGrp( nameSpace=nameSpace, parentTo=parentTo, side=side, stickNam=stickNam )
	for finger in fingerName:
		runLocalFingerRig( 		nameSpace=nameSpace,
								fingerName=finger, 
								side=side, 
								charScale=charScale, 
								numCtrl=numCtrl,
								parentTo=localStick_grp )
	print ('\n\t# = = = = = = = = = Local Finger Rig Complete = = = = = = = = = #\n')
