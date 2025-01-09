'''
from function.asset import exportFBX 
reload(exportFBX)
'''
import pymel.core as pm

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.skin import skinUtil as skinUtil
reload(skinUtil)

from function.pipeline import fileTools as fileTools 
reload(fileTools)

import maya.cmds as mc
import maya.mel as mel

import sys








# Export FBX version no need to bake joint to key
# Select joint and select Mesh

'''
from function.asset import exportFBX
reload(exportFBX)
selection = mc.ls(sl=True)
exportFBX.exportFBXnoConnection(selection, fileName = selection[-1])
'''
def exportFBXnoConnection(selection, fileName = ''):
	
	#... verify if anything is selected

	path = fileTools.findCurrentPath()
	path = path.replace('\\','/')

	if not fileName: #... If not have file name use file instead
		name = fileTools.Scene()
		fileName = name.get_scene_name()

	sys.stdout.write('# Preparing to write FBX file...\n')
	folder = path + "%s"%fileName + ".fbx" 
	pm.mel.eval('FBXExportInputConnections -v 0')
	pm.mel.eval('FBXExport -f "%s" -s'%folder)

	fileTools.openContainerFile( path = path )



def exportFBX_with_path(selection, fileName = '', path = ''):
	
	#... verify if anything is selected
	if selection:

		if not fileName: # If not have file name use file instead
			name = fileTools.Scene()
			fileName = name.get_scene_name()

		sys.stdout.write('# Preparing to write FBX file...\n')
		folder = path + "%s"%fileName + ".fbx" 
		pm.mel.eval('FBXExportInputConnections -v 0')
		pm.mel.eval('FBXExport -f "%s" -s'%folder)

		fileTools.openContainerFile( path = path )








# export FBX to one file use with ply suffix
def fbxExporterOneFile(	jnt_suffix = '_bJnt', 
						mesh_suffix = '_ply', 
						fileName = 'arati_skelMesh'):


	# check root joint name

	if mc.objExists('Root'):
		rootJnt = 'Root'
	elif mc.objExists('root'):
		rootJnt = 'root'
	else:
		mc.error("Please check root joint naming convention." )
		#return None



	# check the exists of bind joint
	if mc.ls('*{0}'.format(jnt_suffix), r=True):
		print ('There are exists suffix joint.')
	else:
		mc.error('There are no suffix joint found.')

	print ('The suffix joint name should be: %s' %jnt_suffix)




	skinUtil.selectBindJnt(naming = jnt_suffix)
	try:
		mc.select('*_rbnBJnt', add = True)
	except:
		pass

	selected_jnt = mc.ls(sl=True)

	try:
		# Key frame 0 and 1
		mc.currentTime(0)
		mc.setKeyframe()

		mc.currentTime(1)
		mc.setKeyframe()


	except:
		print ('There are already key. Skipping')
		pass


	# in case already delete rig_grp
	if mc.objExists('rig_grp'):
		mc.delete( 'rig_grp' )
		print ('Deleting rig_grp...')






	mc.select(selected_jnt, r=True)


	mc.currentTime(0)
	mc.delete( timeAnimationCurves = True ,staticChannels = True )


	mc.currentTime(1)
	mc.delete( timeAnimationCurves = True ,staticChannels = True )



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



	mc.select( '*{0}'.format(mesh_suffix), r = True )
	mc.select( rootJnt , add = True ) 



	# Get file name if not specify
	if not fileName:		
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


	print ('# # # Export Complete # # #')
	fileTools.openContainerFile( path = path )

	











def exportFBX( folder = 'fbx/' , suffix = '*_bind_jnt' ,rootJnt = 'Root'):
	''' export pet or standalone to folder fbx'''
	if fileTools.ifHero():
		
		

		# Key frame 0 and 1
		mc.currentTime(0)
		skinUtil.selectBindJnt(naming = suffix)
		mc.setKeyframe()

		mc.currentTime(1)
		skinUtil.selectBindJnt(naming = suffix )
		mc.setKeyframe()

		# Select and delete
		#mc.select(  , r = True )
		print ('Deleting rig_grp...')
		mc.delete( 'rig_grp' )

		# find meshName
		allTransform = mc.ls( type = 'transform' )
		filePath = fileTools.getAssetData()
		assetList = filePath[-1][0]


		meshName = []
		for each in allTransform:
			if assetList in each:
				print (each)
				meshName.append( each )
				continue
			
		mc.select( meshName, replace = True )    
		mc.select( rootJnt , add = True )   
			
		# Export obj	
		exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '
		path = fileTools._getAssetFolder()

		# Check folder is exists if not create one
		checkPath = path[0] + path[1] + path[2] + folder
		fileTools.checkExistFolder(checkPath)



		# Export obj	
		exportFBXPath = '"' + path[0] + path[1] + path[2] + folder + meshName[0] + '.fbx' + '"'
		exportCommand += exportFBXPath

		# Exec
		mel.eval( exportCommand )
		# Deselect
		mc.select(deselect = True)

	else:
		mc.warning( "You must commit to hero file first." )



# Export FBX file no matter where is source file it will be same folder of the source file
# warning naming due to pipeline
def noCareExporter():



	# check root joint name

	if mc.objExists('Root'):
		rootJnt = 'Root'
	elif mc.objExists('root'):
		rootJnt = 'root'
	else:
		mc.warning("Please check root joint naming convention." )
		return None




	# check the exists of bind joint
	if mc.ls('*_bind_jnt', r=True):

		suffix = '*_bind_jnt'

	elif mc.ls('*_bJnt', r=True):
		suffix = '*_bJnt'
	else:
		mc.warning("Please check bind joint naming convention." )
		return None


	print ('The suffix joint name should be: %s' %suffix)



	 


	polySelected = mc.ls(sl=True)
	alreadyKey = ''
	if not polySelected:
		mc.warning("Please Select polygon first." )
		return None


	skinUtil.selectBindJnt(naming = suffix)


	try:
		# Key frame 0 and 1
		mc.currentTime(0)
		skinUtil.selectBindJnt(naming = suffix)
		mc.setKeyframe()

		mc.currentTime(1)
		skinUtil.selectBindJnt(naming = suffix )
		mc.setKeyframe()


	except:
		print ('There are already key. Skipping')

		pass







	# in case already delete rig_grp
	if mc.objExists('rig_grp'):
		mc.delete( 'rig_grp' )
		print ('Deleting rig_grp...')

	mc.currentTime(0)
	skinUtil.selectBindJnt(naming = suffix)
	mc.delete( timeAnimationCurves = True ,staticChannels = True )

	mc.currentTime(1)
	skinUtil.selectBindJnt(naming = suffix )
	mc.delete( timeAnimationCurves = True ,staticChannels = True )





	if not mc.objExists(rootJnt):
		rootJnt = 'root'


	# Get path
	path = fileTools.findCurrentPath()
	path = path.replace('\\','/')


	for each in polySelected:

		# Unhide object
		if mc.getAttr('{0}.visibility'.format(each)):
			pass
		else:
			mc.setAttr('{0}.visibility'.format(each), True )


		# Export object	
		exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '


		ifParent = mc.listRelatives(each, parent=True)

		if ifParent:
			mc.parent(each, world = True)
		elif ifParent == None:
			print ("{0} is already a child of the parent, 'world'. ".format(each))






		mc.select( each, replace = True )
		mc.select( rootJnt , add = True ) 


		# Get file name
		fileName = each
		# fileName = fileTools.getAssetData()[-1][0]


		exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
		exportCommand += exportFBXPath
		print (exportCommand)


		# Exec
		mel.eval( exportCommand )
		print ('>>> %s has been export.'%fileName)

		# Deselect
		mc.select(deselect = True)

		
	print ('# # # Export Complete # # #')
	fileTools.openContainerFile( path = path )