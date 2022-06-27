# import sys
# sys.path.append(r'D:\True_Axion\Tools\mayaTools\python')

import pymel.core as pm
import maya.mel as mel
import maya.cmds as mc
import os

from function.framework.reloadWrapper import reloadWrapper as reloader


from function.pipeline import fileTools as fileTools 
reloader(fileTools)

from function.pipeline import data
reloader(data)

# import socket
# localMachine = socket.gethostname()

from function.pipeline import logger 
reloader(logger)

PROJECT_NAME = 'Generic'
version = 1.0

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
				pass
		print ('\nImport and clear namespace ...')

	def bakeAnim(self,*args):

		# Get Time From outside
		startText =  mc.textField('startTexFld', tx = True, q = True)
		endText = mc.textField('endTexFld', tx = True, q = True)

		#bake visible mesh
		bakeAttrs = ['visibility']
		# check if having ply suffix
		try:
			mc.select("*_ply", add=True)
		except:
			mc.error('There are no suffix {0}'.format("*_ply"))

		# mc.select("*_ply", add=True) # why select alot of ply
		bake_obj = mc.ls(sl=True)
		
		mc.playbackOptions(min = startText)
		mc.playbackOptions(max = endText)
		time = ( startText , endText )
		
		mc.bakeResults(bake_obj, simulation = True, t= time, disableImplicitControl = True, preserveOutsideKeys = True, at=bakeAttrs)


		if mc.objExists( 'Root' ):
			mc.setAttr( 'Root.v', 1)
			bakeJnt = mc.ls('*_bind_jnt','Root','*_prop_jnt') # call _jnt
			rootJnt = 'Root'
		elif mc.objExists( 'root' ):
			mc.setAttr( 'root.v', 1)
			bakeJnt = mc.ls('*_bJnt','root','*_propJnt') # call _jnt
			rootJnt = 'root'
		elif mc.objExists( 'rootExtra' ):
			mc.setAttr( 'rootExtra.v', 1)
			bakeJnt = mc.ls('*_bJnt','root','*_propJnt') # call _jnt
			rootJnt = 'rootExtra'

		else:
			mc.error("There are 'Root' or 'root' in the scene, Please consult Rigger.")


		
		# bakeAttrs = ["tx","ty","tz","rx","ry","rz"]
		bakeAttrs = ["tx","ty","tz","rx","ry","rz","sx","sy","sz"]

		print (bakeAttrs) 

		mc.bakeResults(bakeJnt, simulation = True, t= time, at=bakeAttrs)

		# Delete Rig GRP
		mc.delete('rig_grp')

		# Delete geo GRP
		if mc.objExists('geo_grp'):
			mc.delete('geo_grp')		


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
		elif mc.objExists( 'rootExtra' ):
			rootJnt = 'rootExtra'		
			
		# get path from field
		path = mc.textField( 'pathField', tx = True, q = True)

		# get current
		# path = self.getPath()

		# get file name from field
		fileName = mc.textField( 'nameField', tx = True, q = True)

		# fileName = self.getSceneName()
		path = path + '\\'
		# MovingJellyLogger.info(path)
		# MovingJellyLogger.info(fileName)

		# condition of jelly visibility
		try:
			mc.select( '*_ply', r = True )
		except:
			ExportLogger.info('There are no suffix {0}'.format("*_ply"))
				
		mc.select( rootJnt, add = True)


		# Set time length
		ExportLogger.debug('Set the time length: {0}'.format(path))
		setTime = function()
		setTime.setTimeLine()


		# Export obj
		exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '
		path = path.replace('\\','/')
		# MovingJellyLogger.info('This path result%s ' %path)

		exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
		exportCommand += exportFBXPath

		# MovingJellyLogger.info('This Export result%s' %exportCommand)

		# Exec
		mel.eval( exportCommand )
		print ('>>> %s has been export.'%fileName)
		ExportLogger.debug('This is export command: {0}'.format(exportCommand))
		fileTools.openContainerFile( path = path )
		# Deselect
		mc.select(deselect = True)

		print ('# # # %s Export Complete # # #' %PROJECT_NAME)




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

		# MovingJellyLogger.warning('This is funtion %s.' %path)
		
		
		# Make a new window
		if mc.window('pbWin', exists = True):
			mc.deleteUI('pbWin')
	
		dWin = mc.window('pbWin', title="{0} Anim Export {1}".format(PROJECT_NAME,version) , iconName ='PB', widthHeight=(300, 200), s = 1, mm = 0, mxb = 0, mw = False )
		
		mc.frameLayout( label='Export Options',collapsable=False, mw=5, mh=5 )
		mc.columnLayout( adjustableColumn=True )
		
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 150),(2, 150)])
		
		mc.text( label='Start :', h = 20)
		mc.text( label='End :', h = 20 )
		mc.textField('startTexFld', tx = '' , h = 30)
		mc.textField('endTexFld', tx = '', h = 30 )
		
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )
		
		mc.button( label='GetTime' , command = self.function.getTimeLine,h=30)
		mc.button( label='SetTime' , command = self.function.setTimeLine,h=30)
		
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )

		
		
		#Create Space
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )
		
		mc.setParent("..")
		
		# BOTTON FOR CLICK
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 50),(2, 250)])
		
		mc.text( label='Path :', h = 25 )
		mc.textField( 'pathField' , fi = path )   
		mc.text( label='Name :', h = 25 )
		mc.textField( 'nameField', fi = name )     
		
		mc.text( label='', h = 8 )
		mc.setParent("..")
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 300),(2, 150)])

		# CONNECT FRAME
		# mc.button( label = 'Connect Frame', command = self.function.setCamera ,w = 250, h = 30)
		# mc.text( label ='', h = 8 )

		# FOR PLAYBLAST
		# mc.button( label = 'Playblast', command = self.function.playBlast ,w=300, h=50 )
		# mc.text( label ='', h = 8 )

		# FOR BROWSE
		# mc.button( label = 'Open folder', command = self.function.openContainFile ,w = 250, h = 30)

		mc.button( label='Import Reference', command = self.function.importRef ,w=50, h=50 )
		mc.button( label='Bake Anim', command = self.function.bakeAnim ,w=50, h=50 )  
		mc.button( label='Export Anim', command = self.function.exportFBX ,w=50, h=50 )  


		mc.showWindow( dWin )
	

# Manual run
# run = Ui()
# run.createGUI()

# from function.asset import genericAnimExporter as gae
# reloader(gae)

# run = gae.Ui()
# run.createGUI()