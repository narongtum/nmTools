#     __________________
# - -/__ Update __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# Add bake specific ply for switch visibility

# import sys
# sys.path.append(r'D:\True_Axion\Tools\mayaTools\python')

import pymel.core as pm
import maya.mel as mel
import maya.cmds as mc
import os

from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline import fileTools as fileTools 
reload(fileTools)

from function.pipeline import data_dict as data
reload(data)

# import socket
# localMachine = socket.gethostname()

from function.pipeline import logger 
reload(logger)

PROJECT_NAME = 'Generic'
version = 1.22
WINDOWNAME = 'animExWin'

# 1. group 'geo_grp' collect all of the skin
# 2. except than that if have '*_ply' bake the key



class ExportLogger(logger.MayaLogger):
	LOGGER_NAME = PROJECT_NAME

class function:

	def getTimeLine(self,*args):
		# TimeLine Query 
		startTime = mc.playbackOptions( min = True,q = True )
		endTime = mc.playbackOptions( max = True,q = True )



		mc.textField('startTexFld', edit = True, tx = startTime)
		mc.textField('endTexFld',edit = True, tx = endTime)
		return (startTime, endTime) 


	def setTimeLine(self,*args):
		# Set The Query Time
		getStartTime = mc.textField('startTexFld', tx = True, q = True)
		getEndTime = mc.textField('endTexFld', tx = True, q = True)

		try:
			getStartTime = float(getStartTime)
			getEndTime = float(getEndTime)
		except:
			mc.error('Invalid literal for float.')
				
		# print(	"{0}{1}".format('Data type is: ',type(startTime))	)
		ExportLogger.debug("{0}{1}".format('Data type is: ',type(getStartTime)))



		mc.playbackOptions(min = getStartTime,max = getEndTime)
		


	def openContainFile( self , *args ):
		FOLDER_PATH = mc.textField( 'pathField', tx = True, q = True)
		# MovingJellyLogger.info(FOLDER_PATH)

		# folder = fileTools.currentBackFolder()
		# folder += r'preview\\'
		if os.path.exists( FOLDER_PATH ):
			fileTools.openContainerFile( path = FOLDER_PATH )
		else:
			CoreLogger.info('file not exists.')
			pass
			# MovingJellyLogger.info('The file does not exist.')

	def importRef(self,*args):
		allrefs = pm.getReferences(recursive = True )
		for ref in allrefs:
			try:
				allrefs[ref].importContents( removeNamespace = True )
			except RuntimeError:
				print ("\nCan't Import ...")
				pass
		print ('\nImport and clear namespace ...')

	def bakeAnim(self,*args):

		# Get Time From outside
		startText =  mc.textField('startTexFld', tx = True, q = True)
		endText = mc.textField('endTexFld', tx = True, q = True)

		


		#... IF YOU WANT TO BAKE VISIBILITY MESH
		#... JUST ADD 'bake_mesh' ATTR TO YOUR MESH

		#... bake visible mesh
		bakeAttrs = ['visibility']
		# check if having ply suffix

		
		time = ( startText , endText )

		# Check the bake condition
		# If not DELETE mesh


		# lists all the transform nodes in the scene
		transforms = mc.ls(type='transform') 
		# filters out all the non-polymesh nodes
		polyMeshes = mc.filterExpand(transforms, sm = 12 )
		# remove duplicate name
		polyMeshes = list(set(polyMeshes)) 
		bake_mesh = []
		del_mesh = []

		for each in polyMeshes:
			if mc.objExists('{0}.bake_mesh'.format(each)):
				bake_mesh.append(each)
			else:
				del_mesh.append(each)



		# bake_mesh = [each for each in polyMeshes if mc.objExists('{0}.bake_mesh'.format(each)) else ]

		if bake_mesh:
			mc.select(bake_mesh, add=True)
			bake_obj = mc.ls(sl=True)
			mc.playbackOptions(min = startText)
			mc.playbackOptions(max = endText)

			# bake key
			mc.bakeResults(bake_obj, simulation = True, t= time, disableImplicitControl = True, preserveOutsideKeys = True, at=bakeAttrs)
		else:
			ExportLogger.debug('There are no poly bake for visibility.')






		# ...
		# Qury bake joint
		# ...

		if mc.objExists( 'Root' ):
			mc.setAttr( 'Root.v', 1)
			bakeJnt = mc.ls('*_bind_jnt','Root','*_prop_jnt') # call _jnt
			rootJnt = 'Root'
		elif mc.objExists( 'root' ):
			mc.setAttr( 'root.v', 1)
			bakeJnt = mc.ls('*_bJnt','root','*_propJnt') # call _jnt
			rootJnt = 'root'
		else:
			mc.error("Asset are 'Root' or 'root' in the scene, Please call Rigger for Help.")

		#... bake UE prop joint	
		if mc.objExists("rig_grp.Engine"):
			ExportLogger.debug('There are having Ik joint.')
			if mc.getAttr("rig_grp.Engine") == 1:
				add_unreal_ik_jnt = ('ik_hand_gun', 'ik_hand_l', 'ik_hand_r', 'ik_foot_l', 'ik_foot_r')
				for each in add_unreal_ik_jnt:
					bakeJnt.append(each)


		if mc.checkBox('bakeBlendshape', query=True, value=True):
			print('this is check')

			#.... bake key for blendshape
			if mc.objExists('face_bsh'):
				ExportLogger.debug('found face_bsh')
				mc.select('face_bsh', r=True)
				if mc.objExists('eye_bsh'):
					mc.select('eye_bsh', add=True)
				mc.bakeResults(preserveOutsideKeys = True, simulation = True, t= time )
				ExportLogger.debug('bake key for blendshape.')
		else:
			print('this is uncheck')
			# mc.error('this is uncheck')

		
		# bakeAttrs = ["tx","ty","tz","rx","ry","rz"]
		bakeAttrs = ["tx","ty","tz","rx","ry","rz","sx","sy","sz"]

		print (bakeAttrs) 

		mc.bakeResults(bakeJnt, simulation = True, t= time, at=bakeAttrs)

		ExportLogger.debug('BakeResults.')




		ExportLogger.debug('Deleteing skin and bake key to mesh visibility.')



		try:
			if mc.objExists('rig_grp'):
				mc.delete('rig_grp')
			if mc.objExists('geo_grp'):
				mc.delete('geo_grp')

			
			



			
		except RuntimeError:
			ExportLogger.debug("Can not find 'rig_grp'/n")






	def getPath(self,*args):
		# Get path
		path = fileTools.findCurrentPath()
		path = path.replace('\\','/')
		return path


	def exportFBX(self,*args):

		if mc.objExists( 'Root' ):
			rootJnt = 'Root'
		elif mc.objExists( 'root' ):
			rootJnt = 'root'
			
		# get path from field
		path = mc.textField( 'pathField', tx = True, q = True)

		# get current
		# path = self.getPath()

		# get file name from field
		fileName = mc.textField( 'nameField', tx = True, q = True)

		# fileName = self.getSceneName()
		path = path + '\\'
				
		mc.select( rootJnt, add = True)

		if mc.objExists( 'Export_grp' ):
			export_grp = 'Export_grp'
		elif mc.objExists( 'export_grp' ):
			export_grp = 'export_grp'
		elif mc.objExists( 'root' ):
			export_grp = 'root'

		if export_grp == None:
			me.error('There are no proper export name')


		mc.select( export_grp, add = True)
		# mc.error('There are no proper export name')


		#... Set time length
		ExportLogger.debug('Set the time length: {0}'.format(path))
		setTime = function()
		setTime.setTimeLine()

		#... reset Take001 to file name
		clipName = mc.textField( 'animClip', tx = True, q = True )
		startTime = mc.textField( 'startTexFld', tx = True, q = True )
		endTime = mc.textField( 'endTexFld', tx = True, q = True )
		
		cleanUpExporterCommand = 'FBXExportSplitAnimationIntoTakes -c'
		clearExporterCommand = 'FBXExportDeleteOriginalTakeOnSplitAnimation -v true'
		createExportClipCommand = ' FBXExportSplitAnimationIntoTakes -v "{0}" {1} {2}'.format( clipName, startTime, endTime ) 
		
		mel.eval( cleanUpExporterCommand )
		mel.eval( clearExporterCommand )
		mel.eval( createExportClipCommand )




		#... Export obj
		exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '
		path = path.replace('\\','/')
		ExportLogger.info('This path result%s ' %path)

		exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
		exportCommand += exportFBXPath

		ExportLogger.info('This Export result%s' %exportCommand)

		# Exec
		mel.eval( exportCommand )
		print ('>>> %s has been export.'%fileName)
		ExportLogger.debug('This is export command: {0}'.format(exportCommand))
		fileTools.openContainerFile( path = path )
		# Deselect
		mc.select(deselect = True)

		print ('# # # %s Export Complete # # #' %PROJECT_NAME)
		mc.deleteUI(WINDOWNAME)




class Ui:
	def __init__(self):
		self.function = function()
	
	def createGUI(self,*args):


		
		# Find folder and important dir
		# partFileName = mc.file( q = True , sn = True )
		scene_anim = fileTools.Scene()
		scene_anim.get_scene_name()
		partFileName = scene_anim.sceneNameFullPath

		splitfileName = partFileName.split('/')
		preName = splitfileName[ len(splitfileName)-1 ]

		# find maya extention
		MayaExt = preName.split('.')[-1]
		
		# name = preName.split( MayaExt )[0]
		name = scene_anim.sceneNameShort_noExt





		path = fileTools.findCurrentPath()
		path = path.replace('\\','/')

			
		'''
		path += r'\\preview\\'
		'''

		# normalize path
		path = os.path.normpath( path )

		# ExportLogger.warning('This is funtion %s.' %path)
		
		
		# Make a new window
		if mc.window(WINDOWNAME, exists = True):
			mc.deleteUI(WINDOWNAME)
	
		dWin = mc.window(WINDOWNAME, title="{0} Anim Export {1}".format(PROJECT_NAME,version) , iconName ='PB', widthHeight=(300, 200), s = 1, mm = 0, mxb = 0, mw = False )
		
		mc.frameLayout( label='Export Options',collapsable=False, mw=5, mh=5 )
		mc.columnLayout( adjustableColumn=True )
		
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 150),(2, 150)])


		
		mc.text( label='Start :', h = 20)
		mc.text( label='End :', h = 20 )
		mc.textField('startTexFld', tx = '' , h = 30)
		mc.textField('endTexFld', tx = '', h = 30 )

		#... auto assign value first
		self.function.getTimeLine()
		
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )
		
		mc.button( label='GetTime' , command = self.function.getTimeLine,h=30)
		mc.button( label='SetTime' , command = self.function.setTimeLine,h=30)
		
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )

		
		
		#...Create Space
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )
		
		mc.setParent("..")
		
		#... BOTTON FOR CLICK
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 50),(2, 250)])
		
		mc.text( label='Path :', h = 25 )
		mc.textField( 'pathField' , fi = path )   
		mc.text( label='Name :', h = 25 )
		mc.textField( 'nameField', fi = name )

		#... clip field
		mc.text( label='Clip :', h = 25 )
		mc.textField( 'animClip', fi = name )

		
		mc.text( label='', h = 8 )
		mc.setParent("..")
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 300),(2, 150)])

		#... CONNECT FRAME
		# mc.button( label = 'Connect Frame', command = self.function.setCamera ,w = 250, h = 30)
		# mc.text( label ='', h = 8 )

		#... FOR PLAYBLAST
		# mc.button( label = 'Playblast', command = self.function.playBlast ,w=300, h=50 )
		# mc.text( label ='', h = 8 )

		#... FOR BROWSE
		mc.columnLayout(adjustableColumn=True)
		mc.checkBox('bakeBlendshape', label='Bake Blendshape', value=True)
		mc.setParent("..")
		
		mc.button( label='Import Reference', command = self.function.importRef ,w=50, h=50 )
		mc.button( label='Bake Anim', command = self.function.bakeAnim ,w=50, h=50 )  
		mc.button( label='Export Anim', command = self.function.exportFBX ,w=50, h=50 )  


		mc.showWindow( dWin )
	
'''
Manual run
run = Ui()
run.createGUI()

from function.asset import genericAnimExporter as gae
reload(gae)

run = gae.Ui()
run.createGUI()
'''