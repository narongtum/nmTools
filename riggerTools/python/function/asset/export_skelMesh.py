# export rig FBX

'''
from function.asset import export_skelMesh as esm 
reload(esm)
'''

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.skin import skinUtil as skinUtil
reload(skinUtil)

from function.pipeline import fileTools as fileTools 
reload(fileTools)

import maya.cmds as mc
import maya.mel as mel



def exportRig_fbx( ignoreJnt = False ,jnt_suffix = '_bJnt', mesh_suffix = '_ply', fileName = '' ):

	# check root joint name
	if mc.objExists('Root'):
		rootJnt = 'Root'
	elif mc.objExists('root'):
		rootJnt = 'root'
	elif mc.objExists('rootExtra'):
		rootJnt = 'rootExtra'
	else:
		mc.error("Please check root joint naming convention." )
		#return None



	if ignoreJnt == False:
		# check the exists of bind joint
		if mc.ls('*{0}'.format(jnt_suffix), r=True):
			print ('There are exists suffix joint.')
		else:
			mc.error('There are no suffix joint found.')

		print ('The suffix joint name should be: %s' %jnt_suffix)


		skinUtil.selectBindJnt(naming = jnt_suffix)

	# incase having ribbon joint
	try:
		mc.select('*_rbnBJnt', add = True)
	except:
		pass

	

	try:
		selected_jnt = mc.ls(sl=True)
		# Key frame 0 and 1
		mc.bakeResults(selected_jnt, t=(0, 1), dic=False, preserveOutsideKeys=True, simulation=True)

	except:
		print ('There are already key. Skipping')
		pass


	# in case already delete rig_grp
	if mc.objExists('rig_grp'):
		mc.delete( 'rig_grp' )
		print ('Deleting rig_grp...')





	'''
	mc.select(selected_jnt, r=True)

	mc.currentTime(0)
	mc.delete( timeAnimationCurves = True ,staticChannels = True )

	mc.currentTime(1)
	mc.delete( timeAnimationCurves = True ,staticChannels = True )
	'''


	# Get path
	path = fileTools.findCurrentPath()
	path = path.replace('\\','/')


	exportCommand = ''


	# Export object	
	exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '






	mc.select( '*{0}'.format(mesh_suffix), r = True )
	selected_mesh = mc.ls(sl=True)

	for each in selected_mesh:

		# Unhide object
		if mc.getAttr('{0}.visibility'.format(each)):
			pass
		else:
			mc.setAttr('{0}.visibility'.format(each), True )


	# select mesh
	mc.select( '*{0}'.format(mesh_suffix), r = True )

	# select joint
	if ignoreJnt == False:
		mc.select( rootJnt , add = True ) 
	elif ignoreJnt == True:
		mc.select( mc.ls(type='joint'), r = True )
		# mc.select( '*{0}'.format(mesh_suffix), r = True )

	if fileName:
		pass
	# check asset name
	elif not fileName:
		if mc.objExists('geo_grp.asset_name'):
			print ('Got name for geo_grp')
			fileName = mc.getAttr('geo_grp.asset_name')

		else:
			name = fileTools.Scene()
			fileName = name.get_scene_name()


	exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
	exportCommand += exportFBXPath
	print (exportCommand)


	# Exec
	mel.eval( exportCommand )
	print ('>>> %s has been export.'%fileName)


	# Deselect
	mc.select(deselect = True)


	print ('# # # Export file at {0}  # # #'.format(exportFBXPath))
	fileTools.openContainerFile( path = path )


	# sent FBX rig file to here
	# D:\True_Axion_Unity_Project\trash_game\Assets\Local Asset\Models\Default Asset\Characters\Dodo\Mesh
	
	
	
# exportRig_fbx(jnt_suffix = '_bJnt', mesh_suffix = '_ply', fileName = '' )