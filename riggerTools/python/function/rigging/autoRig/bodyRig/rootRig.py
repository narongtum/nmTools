#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Create Master Template group
# 01_rootRig_cleanup_v008

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

# set logging for debug mode
import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)
# logging.disable(logging.CRITICAL)

def createMasterGrp(nameSpace = '', charScale = '', PROJECT_DICT = {}):

	

	part = 'Master controller'


	core.makeHeader('Start of %s rig' %part)
	
	'''
	# Create empty Node
	rig_grp = core.Null( '%s%srig_grp' %( charName,elem ) )
	# still_grp = core.Null('still_grp')
	jnt_grp = core.Null('%s%sjnt_grp' %( charName,elem ) )
	ikh_grp = core.Null('%s%sikh_grp' %( charName,elem ) )
	ctrl_grp = core.Null('%s%sctrl_grp' %( charName,elem ) )
	# fkJnt_grp = core.Null('fkJnt_grp')
	# ikJnt_grp = core.Null('ikJnt_grp')
	noTouch_grp = core.Null('%s%snoTouch_grp' %( charName,elem ) )
	# Create controller
	master_ctrl = core.Dag( '%s%smaster_ctrl' %( charName,elem) )
	'''

	# Create empty Node
	rig_grp = core.Null( 'rig_grp'  )
	noTouch_grp = core.Null('noTouch_grp' ) # Change still to no touch grp
	# still_grp = core.Null('still_grp')
	jnt_grp = core.Null('jnt_grp' )
	ikh_grp = core.Null('ikh_grp'  )
	ctrl_grp = core.Null('ctrl_grp' )
	loc_grp = core.Null('loc_grp' )
	# fkJnt_grp = core.Null('fkJnt_grp')
	# ikJnt_grp = core.Null('ikJnt_grp')
	
	# Snap null make for FK/IKmatcher
	snapNull_grp = core.Null('snapNull_grp' )

	# Create controller
	master_ctrl = core.Dag( 'master_ctrl'  )



	master_ctrl.nmCreateController( 'placement_ctrlShape' )
	master_ctrl.editCtrlShape( axis = charScale * 1.8 )

	master_ctrl.renameShape( master_ctrl.shape )
	master_ctrl.setColor( 'yellow' )


	# Create controller
	# placement_ctrl = core.Dag( '%s%splacement_ctrl' %( charName , elem ) )
	placement_ctrl = core.Dag( 'placement_ctrl'  )
	placement_ctrl.nmCreateController( 'fly_ctrlShape' )
	
	placement_ctrl.editCtrlShape( axis = charScale * 1.4 )
	#placement_ctrl.addAttribute( ln = 'size' , k = True , dv = 1 )
	placement_ctrl.setColor('white')



	# cancle this scaleable option
	'''
	# connect scale attr of placement
	for attr in ('sx' , 'sy' , 'sz'):
		# size is attr name
		# conncet size to scale(x,y,z) of placement controller
		placement_ctrl.attr('size') >> placement_ctrl.attr( attr )
		
	'''
	# Lock and Hide attr
	for attr in ('sx','sy','sz'):
		master_ctrl.attr(attr).lockHide()


	# parenting grp used parent
	# call parent function
	master_ctrl.parent( rig_grp )
	placement_ctrl.parent( master_ctrl )

	ctrl_grp.parent( placement_ctrl )
	jnt_grp.parent( placement_ctrl )
	ikh_grp.parent( placement_ctrl )
	loc_grp.parent( placement_ctrl )
	# still_grp.parent( rig_grp )
	# fkJnt_grp.parent( jnt_grp )
	# ikJnt_grp.parent( jnt_grp )
	noTouch_grp.parent( rig_grp )

	snapNull_grp.parent( noTouch_grp )

	master_ctrl.rotateOrder = 'xzy'
	placement_ctrl.rotateOrder = 'xzy'


	for attr in ('tx','ty','tz','rx','ry','rz','sx','sy','sz'):
		rig_grp.attr(attr).lockHide()
		# still_grp.attr(attr).lockHide()
		jnt_grp.attr(attr).lockHide()
		ikh_grp.attr(attr).lockHide()
		# fkJnt_grp.attr(attr).lockHide()
		# ikJnt_grp.attr(attr).lockHide()
		noTouch_grp.attr(attr).lockHide()
		loc_grp.attr(attr).lockHide()

	# Add asset data attribute
	#... Add extre matedada
	# rig_grp.addAttribute( dataType = 'string' , longName = 'Project')
	# rig_grp.addAttribute( longName = 'Version', at = 'float'  , min = 0  , keyable = False )
	# rig_grp.addAttribute( dataType = 'string' , longName = 'Base_Dir')
	rig_grp.addAttribute( attributeType = 'bool' , longName = 'enable', defaultValue = 0 , keyable = False )
	rig_grp.addAttribute( attributeType = 'enum', en = 'Player:Enemy:Weapon', longName = 'asset_type', keyable = False   )
	rig_grp.addAttribute( dataType = 'string' , longName = 'asset_name', keyable = False )
	rig_grp.addAttribute( dataType = 'string' , longName = 'weapon_name', keyable = False )
	rig_grp.addAttribute( attributeType = 'bool' , longName = 'delete_unused_skin', minValue = 0, maxValue = 1, defaultValue = 0 , keyable = False )
	rig_grp.addAttribute( attributeType = 'bool' , longName = 'delete_unused_material', minValue = 0, maxValue = 1, defaultValue = 0 , keyable = False )
	rig_grp.addAttribute( attributeType = 'bool' , longName = 'round_skinweight', minValue = 0, maxValue = 1, defaultValue = 0 , keyable = False )
	# rig_grp.addAttribute( attributeType = 'message' , longName = 'Meta_child')
	rig_grp.addAttribute( dataType = 'string' , longName = 'logmsg', keyable = False )
	rig_grp.addAttribute( dataType = 'string' , longName = 'preJobStep', keyable = False )



	# Add metaRoot
	metaNode = core.MetaRoot('root_meta')

	if PROJECT_DICT:
		#... set Metadata for rig grp
		rig_grp.setAttribute('asset_name', PROJECT_DICT['asset_name'], type = 'string' )

		#... set metadata for meta rig
		metaNode.setAttribute('Project'  , PROJECT_DICT['project'] , type = 'string')
		metaNode.setAttribute('Version'  , PROJECT_DICT['version'])
		metaNode.setAttribute('Base_Dir'  , PROJECT_DICT['Base_Dir'] , type = 'string')
		#... connect message
		rig_grp.attr('message') >> metaNode.attr('rig_grp')


	#... Connect to root_meta
	if mc.objExists('rig_grp'):
		mc.connectAttr('rig_grp.asset_name',  'root_meta.rig_grp' , f=True)




	logger.info('#### End of %s Rig ####' %(part))
	print('\n\n\n\n\n')

	return rig_grp