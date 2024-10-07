'''
all about file handleing

from function.pipeline import fileTools as fileTools 
reload(fileTools)

from function.pipeline \nimport fileTools as fileTools \nreload(fileTools)




from function.rigging.util import misc as misc
reload(misc)

# from function.rigging.skin  import skinUtil
# reload(skinUtil)

# from function.rigging.skin import autoReadWriteSkin as skin
# reload (skin)
'''


# Reload module
from function.framework.reloadWrapper import reloadWrapper as reload



import maya.cmds as mc
import os
import pymel.core as pm
import shutil
import time
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import datetime
import maya.mel as mel
import os.path

# import logging
# logger = logging.getLogger('debug_text')
# logger.setLevel(logging.DEBUG)


from function.pipeline import logger 
reload(logger)


class fileToolsLogger(logger.MayaLogger):
	LOGGER_NAME = "FileToolsLogger"

MAYA_VERSION = mc.about(v=True)	




# # # # # # # # # # # # # # # # # # # # 
#... ask what is state of this file 
# # # # # # # # # # # # # # # # # # # # 
def openRigDatafile():

	from pathlib import Path	
	if fileState() == 'version' or fileState() == 'local_hero':
		print('This is Version Naja.')

		pathFile = mc.file(q=True, sn=True)
		path_lib = Path(pathFile)
		wanted = path_lib.parent.parent  # Go up two levels to get the desired directory
		final_wanted_path = wanted / 'Data'

		if final_wanted_path.exists() and final_wanted_path.is_dir():
			os.startfile(final_wanted_path)

	elif fileState() == 'global_hero':
		print('This is Global hero.')
		pathFile = mc.file(q=True, sn=True)
		path_lib = Path(pathFile)
		wanted = path_lib.parent.parent  # Go up two levels to get the desired directory
		final_wanted_path = wanted / 'Rig' / 'Data'
		if final_wanted_path.exists() and final_wanted_path.is_dir():
			os.startfile(final_wanted_path)
	else:
		print('There are no correct file to open.')










# ========== # 
# Export selection at data folder
# ========== # 

def exportSel( folder_name = 'data' ):

	currentPath = currentFolder()

	name = mc.ls(sl = True)[0]

	if ':' in name:
		finalName = name.split(':')[-1]
	else:
		finalName = name
		


	if fileState() == 'global_hero':

		print('\nThis is Global Hero file.')
		currentPath = findCurrentPath(step = 'current')

		parent_dir = os.path.dirname(os.path.dirname(currentPath))
		#... kept export sel at Rig department
		rig_path = f'Rig\\{folder_name}'

		currentPath = os.path.join(parent_dir,rig_path)

		checkPath_normPath = os.path.normpath(currentPath)
		if os.path.exists(checkPath_normPath):
			print('There are already exists.')
		else:
			print('Folder not found. Creating it now.')
			os.makedirs(checkPath_normPath)

		finalPath = os.path.join(currentPath, finalName + '.ma')
		final_normPath = os.path.normpath(finalPath)
		mc.file ( final_normPath, force = True, options = 'v=0', type = 'mayaAscii', preserveReferences = True, exportSelected = True)
		print ('Asset has been export at: %s' %final_normPath)



	elif fileState() == 'local_hero':

		print('\nThis is Local Hero file.')
		currentPath = findCurrentPath(step = 'current')

		parent_dir = os.path.dirname(os.path.dirname(currentPath))

		currentPath = os.path.join(parent_dir, folder_name)

		checkPath_normPath = os.path.normpath(currentPath)
		if os.path.exists(checkPath_normPath):
			print('There are already exists.')
		else:
			print('Folder not found. Creating it now.')
			os.makedirs(checkPath_normPath)

		finalPath = os.path.join(currentPath, finalName + '.ma')
		final_normPath = os.path.normpath(finalPath)
		mc.file ( final_normPath, force = True, options = 'v=0', type = 'mayaAscii', preserveReferences = True, exportSelected = True)
		print ('Asset has been export at: %s' %final_normPath)



	elif fileState() == 'version':
		print('\nThis is Version file.')
		#... check file already exists
		checkPath = currentPath + folder_name
		checkPath_normPath = os.path.normpath(checkPath)

		if os.path.exists(checkPath_normPath):
			print('There are already exists.')
		else:
			print('Folder not found. Creating it now.')
			os.makedirs(checkPath_normPath)


		# finalPath = currentPath + folder_name + finalName + '.ma'
		finalPath = os.path.join(currentPath, folder_name, finalName + '.ma')

		final_normPath = os.path.normpath(finalPath)
		mc.file ( final_normPath, force = True, options = 'v=0', type = 'mayaAscii', preserveReferences = True, exportSelected = True)
		print ('Asset has been export at: %s' %final_normPath)


	else:
		print('\nThis is Unknow file.')
		currentPath = currentFolder()
		finalPath = os.path.join(currentPath, finalName + '.ma')
		final_normPath = os.path.normpath(finalPath)
		mc.file ( final_normPath, force = True, options = 'v=0', type = 'mayaAscii', preserveReferences = True, exportSelected = True)
		print ('Asset has been export at: %s' %final_normPath)






# ========== # 
# Add previous job step to rig grp
# ========== # 

def assign_pre_job_step():
	myFile = Scene()
	fileName = myFile.get_scene_name()

	if mc.objExists("rig_grp.preJobStep") == True:
		mc.setAttr("rig_grp.preJobStep", fileName , type="string")
	else:
		pass




# ========== # 
# shading
# ========== # 


def transferShade():
	sel = mc.ls( sl = True )
	mc.hyperShade( smn = True )
	refMat = mc.ls(sl=True)[0]

	for each in sel:
		if not each == sel[0]:

			mc.select( sel , r = True )
			mc.hyperShade( assign = refMat )


def printTexturePath():
	
	fileNodes = mc.ls(type="file")
	# print texture path
	for each in fileNodes:
		mc.select(each, r = True)
		fullName = mc.getAttr(".fileTextureName")
		print (fullName)
	mc.select(deselect = True)


def replaceTex():
# tools for autoplace texture by insert manual texture path


	if MAYA_VERSION == '2018':
		texturePath = raw_input('place your new texture path:')
	elif MAYA_VERSION == '2023':
		texturePath = input('place your new texture path:')

	fileNode = mc.ls(type='file') # list type 'file' in scene
	for f in fileNode: # loop for every fileNode
		mc.select(f,r=True)
		fullPaht = mc.getAttr('.fileTextureName')
		print (fullPaht)
		textureName = fullPaht.split('/')[-1]
		print (textureName)
		projectNewName = texturePath + '\\' + textureName 
		mc.setAttr('.fileTextureName' , projectNewName, type='string')









# pass the text to copy to clipboard 
# Ref: https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard 
def addToClipBoard(text):
	command = 'echo | set /p nul=' + text.strip() + '| clip'
	os.system(command)



def makeHeader(funcName):
	print ('# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n')
	print ('\t\t\t\t\t%s\n' %funcName)
	print ('# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n')


	

class Scene(object):
	"""
	scene info try to use class from digital37
	location: maya.general.scene
	s = scene.Scene()
	s.get_scene_name()
	s.sceneNameShort
	"""
	def __init__(self):
		pass

	def get_scene_name(self):
		self.sceneNameFullPath = pm.system.sceneName()
		self.sceneNameFullPath_noExt = os.path.splitext( self.sceneNameFullPath )[0]
		self.sceneNameShort = os.path.basename( self.sceneNameFullPath )
		self.sceneNameShort_noExt = os.path.splitext( self.sceneNameShort )[0]
		# return mayaFile type 'ma' or 'mb'
		self.scene_ext = os.path.splitext( self.sceneNameShort )[1]
		return self.sceneNameShort_noExt

	def get_file_data(self):
		# same as above but my style
		# return file name and ext
		
		'''
		scenenene = fileTools.Scene()
		aa=scenenene.get_file_data()
		aa[0]
		aa[1]
		'''
		self.fileName_fullPath = pm.system.sceneName()
		self.fileName = os.path.basename( self.fileName_fullPath )
		self.file_ext = os.path.splitext( self.fileName )[1]
		return self.fileName_fullPath,self.fileName,self.file_ext

def getExt(splitwith = '.'):
	path = currentPath()
	ext = path.split( splitwith )[-1]
	return ext


def createThumbnail(width=256, height=256):

	#... Create Thumbnail at current maya file
	currentPath = findCurrentPath()
	fileName = getFileName()[0]

	#... save as jpg first then convert
	jpgImageFile  = '{0}{1}.{2}'.format(currentPath, fileName, 'jpg')

	pngImageFile = '{0}{1}.{2}'.format(currentPath, fileName, 'png')
	
	mimage = om.MImage()
	view = omui.M3dView.active3dView()
	view.readColorBuffer(mimage, True)

	#... Resize the image to the specified width and height
	mimage.resize(width, height)

	#... mimage.writeToFile(imageFile, fileType)
	mimage.writeToFile(jpgImageFile )

	#... Convert the file to PNG
	os.rename(jpgImageFile, pngImageFile)

	print('Thumbnail has been created at: {0}'.format(pngImageFile))


#... find current maya path
def currentPath():
	path = pm.system.sceneName()
	if path:
		return path
	else:
		mc.warning("There are no file path")




def openContainerFile( path = None ):
	os.startfile(path)

def countJnt(suffix = '*_bJnt'):
	num = 0
	bindJnt = mc.ls(suffix)

	if bindJnt:
		for each in bindJnt:
			num = num + 1
		fileToolsLogger.info('The number of bind joint is %i' %num)

		# remain joint
		rJnt = 45 - num
		
		fileToolsLogger.info('%i joint remaining\n' %rJnt)
		fileToolsLogger.info('%i joint number is\n' %num)
		mc.inViewMessage(amg = "<hl>The number of bind joint is %s</hl>" %num, pos = "midCenterTop", fade = True)
	else:
		fileToolsLogger.info('There are no joint to count.')




def countJntExt(suffix = '*_bJnt'):
	suffix = '*_bJnt'
	bindJnt = mc.ls(suffix)
	for each in bindJnt:
		print('Joint name is: {0}\n'.format(each))

	fileToolsLogger.info('The number of bind joint is : {0}\n'.format(len(bindJnt)))


# hastag variable for decorate
hashSign = '#' * 25


# check what is this file hero or version 
# return True or False

def ifHero():
	# folder = currentFolder()
	# dataRaw = getAssetData()
	# mayaFileName = dataRaw[0][-1]
	pathFile = mc.file( q=1,sn=1)
	splitFolderNam = pathFile.split('/')[-2]

	print (splitFolderNam)

	if splitFolderNam == 'hero' or splitFolderNam == 'Commit':
		print ('This is hero file.')
		return True
		
	elif splitFolderNam == 'version':
		print ('This is version file.')
		return False
	else:
		print ('Unknow condition.')
		return None





def fileState():
	"""
	Determines the type of file based on its folder location and the existence of a specific file.

	This function checks the current file in Maya, analyzes the folder in which it resides, 
	and determines if the file is either a "global hero", "local hero", or a "version" file. 
	It also checks for the existence of a `data.json` file in the parent directory to differentiate 
	between global and local hero files.

	Returns:
		str: 
			- 'global_hero' if the file is located in a 'hero' or 'commit' folder and the `data.json` file exists.
			- 'local_hero' if the file is located in a 'hero' or 'commit' folder but the `data.json` file does not exist.
			- 'version' if the file is located in a 'version' folder.
			- 'unknown' if the folder name doesn't match any known conditions or if no file is open.

	Raises:
		None
	"""

	pathFile = mc.file(q=True, sn=True)

	if not pathFile:  # Handle if no file is open or path is empty
		print("No file is currently open or invalid path.")
		return 'unknown'

	splitFolderNam = pathFile.split('/')[-2].lower()  # Normalize the case

	if splitFolderNam in ['hero', 'commit']:
		print('This is a hero file.')
		
		# Get the parent directory two levels up
		parent_dir = os.path.dirname(os.path.dirname(pathFile))
		data_json = 'data.json'

		# Join and normalize the path
		file_path = os.path.join(parent_dir, data_json)
		file_path = os.path.normpath(file_path)

		# Check if the file exists
		if os.path.exists(file_path):
			print(f"\nThe file exists at: {file_path}\nThis is a Global Hero file :).")
			return 'global_hero'
		else:
			print(f"\nThe file does not exist at: {file_path}\nThis is a Local Hero file.")
			return 'local_hero'

	elif splitFolderNam == 'version':
		print('This is a version file.')
		return 'version'
		
	else:
		print('Unknown condition.')
		return 'unknown'



		










# Open current maya directory for browse another file that in same level
def openCurrentMayaDir():
	folder = currentBackFolder()
	singleFilter = "All Files (*.*)"

	try:
		fileNameDir = mc.fileDialog2( fileFilter = singleFilter, dialogStyle = 2, fileMode = 1, okCaption = 'Open' ,startingDirectory = folder)[0]
		# mc.file(	fileNameDir, force = True , ignoreVersion = True, type =  "mayaAscii" , open = True     )
		mc.file(	fileNameDir, force = True , ignoreVersion = True , open = True     )

	

		myPath = mc.file( query = True, sceneName = True )

		if myPath.endswith('.ma'):
			fileType = 'mayaAscii'
		elif myPath.endswith('.mb'):
			fileType = 'mayaBinary'
			
		# Must convert slashes before calling to the mel:
		mel.eval('addRecentFile("%s", "%s")'%(myPath.replace('\\', '/'), fileType)) # not work

		
		# recent_files = mc.optionVar(q='RecentFilesList')
		# if not recent_files:
		# 	recent_files = []
		# myPathList = [myPath.replace('\\', '/')]  
		# recent_files.insert(0, myPathList)
		# mc.optionVar(sv=('RecentFilesList', ';'.join(recent_files)))
		# mc.optionVar(sv=('defaultRecentFileType', fileType))
		# fileToolsLogger.info('\nsaving recent file...')
		





		# option for python version
		# mc.optionVar(stringValueAppend=('RecentFilesList', '{0}'.format(myPath.replace('\\', '/'), myPath)	)	)


	except :
		print ('\nCancle Progress...')



def saveCurrentMayaDir():
	folder = currentBackFolder()
	singleFilter = "All Files (*.*)"

	try:
		fileNameDir = mc.fileDialog2( fileFilter = singleFilter, dialogStyle = 1, fileMode = 0, okCaption = 'Save' ,startingDirectory = folder)[0]
		mc.file( rename = fileNameDir )
		ext = fileNameDir[-2:]

		if ext == 'mb':
			mayaFileType = 'mayaBinary'
		else:
			mayaFileType = 'mayaAscii'

		fileToolsLogger.info('Files type is: {0}'.format(mayaFileType))
		fileToolsLogger.info('Files has been saved at: {0}'.format(fileNameDir))
		mc.file( force = True , ignoreVersion = True, type =  mayaFileType , save = True )
		# mc.file( force = True , ignoreVersion = True, save = True )
	except :
		print ('\nCancle Progress...')





# automate copy usersetup for artist
def copyMayaFiles():
	#dest = os.path.join( os.path.expanduser("~"), "Documents", "maya", "2018" )
	dest = os.path.join( os.path.expanduser("~"), "maya" )
	if os.path.exists( dest ):
		#shutil.copy( r'P:\sysTool\maya\2012-x64\Maya.env', '%s' % dest )
		shutil.copy( r'D:\True_Axion\Tools\riggerTools\maya\scripts\userSetup.mel', '%s\\scripts' % dest )
		shutil.copy( r'D:\True_Axion\Tools\riggerTools\maya\scripts\userSetup.py', '%s\\scripts' % dest )
		print ('Copy maya userSetup to %s' %dest)
		print ("\nDO NOT CLOSE...")
		time.sleep(2)
		

# if __name__ == '__main__':
# 	copyMayaFiles()





# find address of maya file only
def whereAreMe(path = None):
	path = mc.file(q=True, sn = True)
	return path


# find where is file
# up 2 step from this file exists
# ex 
# file path  = "D:\project\EVERGLEAM HILL\asset\char\NPC\bob\rig\version\npc_bob01.rig.hero.0001.ma"
# addPath "\\data//"
# return 'D:\\project\\EVERGLEAM HILL\\asset\\char\\NPC\\bob\\rig\\data\\'



def desinatePath(addPath = ''):
	where = whereAreMe()
	clean_path = os.path.normpath(where)
	spPath = clean_path.split("\\")
	reElem = "\\"+spPath[-2]+"\\"+spPath[-1]
	dataPath = 	clean_path.replace(reElem,'') 
	ASSET_PATH = dataPath + addPath
	return ASSET_PATH



# check if folder is exists
# if not exist there will be 'create' folder following file path
# notice  os.path.dirname(filename) will return backslash folder not current folder
def checkExistFolder(filename = None):
	if not os.path.exists(os.path.dirname(filename)):
		try:
			os.makedirs(os.path.dirname(filename))
			print ('Folder create...')
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	else:
		print ('The folder has exists.')
		return True




def currentFilePath(filename = None):
	if not os.path.exists(filename):
		try:
			os.makedirs(filename)
			print ('folder %s not found' %filename)
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	else:
		print ('The folder has already exists.')



def deleteDisplayLayer():
	displayLayer = mc.ls(type = 'displayLayer')
	for each in displayLayer:
		# if each != 'defaultLayer' and each != 'joint' and each != 'controller':
		if each != 'defaultLayer' and each.endswith("_lyr") == False:
			print ('%s Deleteing %s layer...' %(hashSign,each))
			mc.delete(each)
		else:
			print ('\n No displayLayer to delete...')




def doDeleteGrpTmp():
	if mc.objExists('delete_grp'):
		mc.delete('delete_grp')
	else:
		print("No delete_grp found")
		pass







def doDeletePrefix(prefix = 'bak_'): #... delete by prefix name 
	try:
		list_del = mc.ls(prefix + '*')
		mc.delete(list_del)
		fileToolsLogger.info('prefix name "{0}" has been deleted...'.format(prefix))
	except:
		fileToolsLogger.info('There is no something to delete.')




def doDeleteSuffix(suffix = '_bak'): #... delete by suffix name 
	try:
		mc.ls('*' + suffix)[0]
		mc.delete('*' + suffix)
		fileToolsLogger.info('suffix name "{0}" has been deleted...'.format(suffix))
	except:
		fileToolsLogger.info('There is no something to delete.')




#... delete every give name upper or lower case
def doDeletePrefixExt(prefix='bak_'):
	# Get a list of all objects in the scene
	all_objs = mc.ls()

	# Filter the list to include only objects with the given prefix
	matching_objs = [obj for obj in all_objs if obj.lower().startswith(prefix.lower())]

	# Delete the matching objects
	if matching_objs:
		mc.delete(matching_objs)
		print('Objects with prefix "{}" deleted.'.format(prefix))
	else:
		print('No objects with prefix "{}" found.'.format(prefix))


#... delete every give name upper or lower case
def doDeleteSuffixExt(suffix='_bak'):
	# Get a list of all objects in the scene
	all_objs = mc.ls()

	# Filter the list to include only objects with the given suffix
	matching_objs = [obj for obj in all_objs if obj.lower().endswith(suffix.lower())]

	# Delete the matching objects
	if matching_objs:
		mc.delete(matching_objs)
		print('Objects with suffix "{}" deleted.'.format(suffix))
	else:
		print('No objects with suffix "{}" found.'.format(suffix))


# def doDeleteMisc(name = 'BaseAnimation'):
# 	if mc.objExists(name):
# 		mc.delete(name)
# 		print("\n %s has been deleted." %name)

def delete_anim_layer():
	# Get a list of all animation layers
	anim_layers = mc.ls(type='animLayer')

	# Delete each animation layer
	for anim_layer in anim_layers:
		if mc.objExists(anim_layer):
			mc.delete(anim_layer)



def doHideGrp(jntName,num):
	if mc.objExists(jntName):
		print("\nHide visibility of %s " %jntName)
		mc.setAttr('%s.visibility' %jntName, num)
	else:
		print("%s does not exists." %jntName)
	


def fileData():
	rigPath = whereAreMe()  



def splitName( name = '' , splitwith = '' ):
	newName = []
	newName = name.split(splitwith)
	listName = _splitNameSide (listName = newName )
	print ('splite string with %s' %splitwith)
	return listName




def _splitNameSide( listName = [] ):
	storeValue = []
	if 'LFT' in listName[0]:
		print ('this is LFT')
		listName.append(listName[0][:-3])
		listName.append('LFT')
		

	elif 'RGT' in listName[0]:
		print ('this is RGT')
		listName.append(listName[0][:-3])
		listName.append('RGT')
		
	else:
		print ('\nThere are no side to split.')
	return listName



# Folder handeling 

# auto find propery folder
def addFolderPath(addPath = ''):
	where = whereAreMe()
	clean_path = os.path.normpath(where)
	spPath = clean_path.split("\\")
	reElem = "\\"+spPath[-2]+"\\"+spPath[-1]
	dataPath = 	clean_path.replace(reElem,'') 
	FOLDER_PATH = dataPath + addPath
	return FOLDER_PATH




# find current folder that maya file exists (backward 2 step)
def currentFolder():
	# find asset path
	path = whereAreMe()
	clean_path = os.path.normpath(path)
	splitPath = clean_path.split("\\")
	reElem = "\\" + splitPath[-2] + "\\" + splitPath[-1]
	dataPath = 	clean_path.replace(reElem,'')
	dataPath = dataPath + "\\"
	return dataPath



# find current folder (backward 1 step where folder is belong)
def currentBackFolder():
	# find asset path
	path = whereAreMe()
	clean_path = os.path.normpath(path)
	splitPath = clean_path.split("\\")
	reElem = "\\" + splitPath[-1]
	dataPath = 	clean_path.replace(reElem,'')
	dataPath = dataPath + "\\"
	return dataPath



def findCurrentPath(step = 'current'):
	# just merge above function of currentFolder and currentBackFolder together
	# find asset path
	path = whereAreMe()
	clean_path = os.path.normpath(path)
	splitPath = clean_path.split("\\")


	if step == 'backward': # backward to folder
		reElem = "\\" + splitPath[-2] + "\\" + splitPath[-1]
		dataPath = 	clean_path.replace(reElem,'')
		dataPath = dataPath + "\\"
		print (hashSign)
		print ('Folder path is :  {0}'.format(dataPath))
		return dataPath

	else: # Current folder
		reElem = "\\" + splitPath[-1]
		dataPath = 	clean_path.replace(reElem,'')
		dataPath = dataPath + "\\"
		print (hashSign)
		print ('Folder path is :  {0}'.format(dataPath))
		return dataPath


def getFileName():
	path = whereAreMe()
	clean_path = os.path.normpath(path)
	filename = clean_path.split("\\")[-1]
	ext = filename.split(".")[-1]
	filename = filename.replace('.' + ext , '')
	return filename , ext

# find current maya file name
def getAssetData():
	''' return list of path and file name'''
	path = whereAreMe()
	clean_path = os.path.normpath(path)
	splitPath = clean_path.split("\\")
	filename = splitName(splitPath[-1], splitwith = '.' )
	return splitPath,filename
	#return (name, version, job, department)

def _getAssetFolder():
	''' return all of each step file folder path '''
	rigPath = whereAreMe()
	extractList = splitName(name = rigPath , splitwith = '/')
	projectName = extractList[0] + '/' + extractList[1] + '/' + extractList[2] + '/' 
	assetType = extractList[3] + '/' + extractList[4] + '/' + extractList[5] + '/' 
	assetname = extractList[6] + '/' 
	departmentName = extractList[7] + '/'
	fileName = extractList[8]

	return projectName, assetType, assetname, departmentName, fileName


	
	'''if mode == 'global'
					path = whereAreMe()
			
					clean_path = os.path.normpath(path)
					splitPath = clean_path.split("\\")
					filename = splitName(splitPath[-1],splitwith = '.' )
					# tomorrow fix here
					filename = filename[0] + '.' + filename[1] + '.hero'
					print 'filename is : %s' %filename
			
					return filename
			
				else mode == 'local'
					path = whereAreMe()
			
					clean_path = os.path.normpath(path)
					splitPath = clean_path.split("\\")
					filename = splitName(splitPath[-1],splitwith = '.' )
					# tomorrow fix here
					name = filename[0]
					department = filename[1]
					job = filename[2]
					filename = name+'.'+department+'.'+job'''



def savingAsset(mode = 'local'):
	assetPath = currentFolder()
	spliteName = getAssetData()


	assetName = spliteName[1][0] 
	department = spliteName[1][1]  
	step = spliteName[1][2] 

	# filename should be something like slot.rig.skel.0001.ma having 5 entity

	# slot is asset name
	# rig is department
	# skel is pipeline step
	# 0001 is version
	# ma is ext


	if mode == 'global':
		# newFilename = spliteName[0] + '.' + spliteName[1]+ '.' + 'hero'
		newFilename = assetName + '.' + 'rig' + '.' + 'hero'
		print (newFilename)
		SAVE_PATH = assetPath + newFilename


	elif mode == 'local':
		print (spliteName)

		newFilename = assetName + '.' + department + '.' + step
		localPath = 'hero\\'
		SAVE_PATH = assetPath + localPath + newFilename

	
	elif mode == 'global_something':
		newFilename = assetName + '.rig'
		print (newFilename)
		SAVE_PATH = assetPath + newFilename
	

	# if this folder not exists create folder
	checkExistFolder( filename = SAVE_PATH )
	mc.file( rename = SAVE_PATH )
	mc.file( save = True, type = 'mayaAscii' )

	print ('file has been saved at: %s' %SAVE_PATH)




# Execute saving file
def noCareSavAsset( mode = 'local', mayaFile = 'ma', fixedName = False):

	if fixedName:
		# use Fixed name just in case
		if mc.objExists("rig_grp.asset_name") and mc.getAttr("rig_grp.asset_name") != '':
			subName_fixed = mc.getAttr("rig_grp.asset_name")
			
			fileToolsLogger.info('This is having a asset name: {0}'.format(subName_fixed))
		else:
			fileToolsLogger.warning('There are no asset name in rig_grp.')
			# return False
			



	''' new condition to publish file '''
	assetPath = currentFolder()
	fullPath = whereAreMe()
	fileName = ''

	if fixedName and mc.objExists("rig_grp.asset_name"):
		subName = subName_fixed
		
	else:
		
		'''
		fileName = fullPath.split('/')[-1]
		# remove [-2] step and [-1] ext entites
		ext = '.' + fileName.split('.')[-2]+'.' + fileName.split('.')[-1]
		# got file name without ext
		subName =   fileName.replace(ext,'')
		'''
		sac = Scene()
		fileName = sac.get_scene_name()
		subName = fileName.split('.')[0]


		fileToolsLogger.debug('This is subName:  [{0}]'.format(subName))





	if mode == 'local':

		localPath = 'hero\\'
		SAVE_PATH = assetPath + localPath + subName

		fileToolsLogger.debug('This is path file:  [%s]    [%s]' %(assetPath,subName))

		# if this folder not exists create folder
		checkExistFolder( filename = SAVE_PATH )

		
		# cancle file type
		if mayaFile == 'ma':
			fileType = 'mayaAscii'
		elif mayaFile == 'mb':
			fileType = 'mayaBinary'
		

		mc.file( rename = SAVE_PATH )
		mc.file( save = True, type = fileType )

		fileToolsLogger.info('File has been saved at: %s.%s' %(SAVE_PATH,mayaFile))
		# print ('file has been saved at: %s.%s' %(SAVE_PATH,mayaFile))



	elif mode == 'global':

		# insert string hero
		if not fixedName:
			subName += '_hero'

		fileToolsLogger.debug('Hey!!! look at this bro:   [%s]      [%s]' %(assetPath,subName))
		SAVE_PATH = assetPath  + subName


		# if this folder not exists create folder
		checkExistFolder( filename = SAVE_PATH )

		
		mc.file( rename = SAVE_PATH )
		mc.file( save = True, type = 'mayaBinary' )
		mc.file( save = True, type = 'mayaAscii' )


		# print ('file has been saved at: %s.%s' %(SAVE_PATH,'mb'))
		# print ('file has been saved at: %s.%s' %(SAVE_PATH,'mb'))

		fileToolsLogger.info('File has been saved at: %s.%s' %(SAVE_PATH,'ma'))
		fileToolsLogger.info('File has been saved at: %s.%s' %(SAVE_PATH,'mb'))

	else:
		mc.warning('There are no match condition.')




def doDeleteGrp():
	# reorganize group structer after publish
	if mc.objExists('delete_grp'):

		listDelete = mc.listRelatives('delete_grp', children=True)
		# list all of member in delete grp
		if listDelete:
			for each in listDelete:
				if mc.objExists('%s_parentConstraint1' %each):
					
					desName = mc.listConnections( '%s_parentConstraint1.target[0].targetParentMatrix' %each )
					# destination name that we want to parent

					print ('%s having parentConstraint'  %desName[0])
					mc.delete('%s_parentConstraint1' %each)
					mc.delete('%s_scaleConstraint1' %each)
					
					mc.parent( each, desName)
					print ('\nParenting: %s >>>>>> %s' %(each, desName))
					
				else:
					print ('\n%s not has any constraint it will be delete' %each)
					mc.delete(each)
					continue


			print ('Checking done doing delete group...')
			mc.delete('delete_grp')
		else:
			print ("remove reference ")
	else:
		print("No delete_grp found.")





def doMoveGrp():
	if mc.objExists('move_grp'):
		# new method for reorganize
		listMovGrp = mc.listRelatives('move_grp', children=True)

		if listMovGrp:
			for each in listMovGrp:
				if mc.objExists('%s_parentConstraint1' %each): # if having any parentConstraint

					desName = mc.listConnections( '%s_parentConstraint1.target[0].targetParentMatrix' %each )

					mc.delete('%s_parentConstraint1' %each)
					mc.delete('%s_scaleConstraint1' %each)

					member = mc.listRelatives(each, children=True)
					
					if member:	
						for eachMem in member:
							print (eachMem)
							mc.parent( eachMem, desName)
							print ('\nParenting: %s >>>>>> %s' %(eachMem, desName))
					else:
						print ('\n%s not has any constraint it will be delete.' %each)
						mc.delete(each)


				else:
					print ('\n%s not has any constraint it will be delete.' %each)
					mc.delete(each)
					continue
			print ('moving done delete moving group')
			mc.delete('move_grp')

	else:
		print ('No move_grp found skip process.')






def remUnRef():
	if mc.objExists('delete_grp'):
		listDelete = mc.listRelatives('|delete_grp', children=True)
		if listDelete:
			for each in listDelete:
				if ':' in each:
					nameSpace = None
					nameObj = None
					print ('this is %s' %each)
					nameSpace = each.split(':')[0]
					nameObj = each.split(':')[1]
					
					if mc.objExists('%s_parentConstraint1' %nameObj) and mc.objExists('%s_scaleConstraint1' %nameObj):
						print( 'yeah there are have connection do nothing')
						
						
					else:
						print ('no connection let remove them')
						try:
							refNode = mc.referenceQuery( each , referenceNode = True )
							fileName = mc.referenceQuery( refNode , filename = True )
							mc.file( fileName , rr = True )
						except:
							 print ('skip the redundance referenceNode')

			mc.delete('delete_grp') # delete at lase
		else:
			print("No delete_grp found.")

	else:
		print("No delete_grp found.")




#####################################################
#       import and remove namespace              
#####################################################
def impRem():
	allrefs = pm.getReferences(recursive = True )
	for ref in allrefs:
		try:
			allrefs[ref].importContents( removeNamespace = True )
		except RuntimeError:
			pass
	print ('\nImport and clear namespace ...')


# the original
def remove_unused_influences(skinCls, targetInfluences=[]):
	'''
	Snippet to removeUnusedInfluences in Autodesk Maya using Python.
	The MEL version runs slowly, over every influence one at a time.
	"targetInfluences" allows you to directly specify which influences to remove.
	This will only remove targets which are not currently being used.
	'''
	# mc.skinCluster(skinCls, e=True, removeInfluence=unusedInfluences)
	skinCls = []
	targetInfluences=[]
	print(type(skinCls))
	allInfluences = mc.skinCluster(skinCls, q=True, inf=True)
	weightedInfluences = mc.skinCluster(skinCls, q=True, wi=True)
	unusedInfluences = [inf for inf in allInfluences if inf not in weightedInfluences]
	if targetInfluences:
		unusedInfluences = [
				inf for inf in allInfluences
				if inf in targetInfluences
				if inf not in weightedInfluences
				]
	mc.skinCluster(skinCls, e=True, removeInfluence=unusedInfluences)



def delete_unused_skin_suffix(suffix = '*_skc'):
	'''
	Remove unused influence following suffix 
	can use with polygon or skinCluster
	'''
	if mc.objExists("rig_grp.delete_unused_skin"):
		all_poly_skinCls = mc.ls(suffix)


		if all_poly_skinCls:

			for skinCls in all_poly_skinCls:
				allInfluences = mc.skinCluster(skinCls, q=True, inf=True)
				weightedInfluences = mc.skinCluster(skinCls, q=True, wi=True)
				unusedInfluences = [inf for inf in allInfluences if inf not in weightedInfluences]
				mc.skinCluster(skinCls, e=True, removeInfluence=unusedInfluences)
				for each in unusedInfluences:
					fileToolsLogger.info('Remove Unused Influences for {0} >>> {1}'.format(each, skinCls))

		else:
			print ('There are noting to remove.')
			return False



def delete_unused_material():
	mel.eval('MLdeleteUnused()')
	fileToolsLogger.info('\nUnused material deleted.')




def delete_animation_layer(layer_name):
	if mc.objExists(layer_name):
		mc.delete(layer_name)
		print(f"Deleted animation layer: {layer_name}")
	else:
		print(f"Animation layer {layer_name} does not exist.")







# local publish
def localPublish( mayafileType = 'ma'):

	ngSkin = mc.ls('ngSkinToolsData_*')
	if ngSkin:
		import ngSkinTools2
		# remove all ngSkinTools custom nodes in a scene
		ngSkinTools2.operations.removeLayerData.remove_custom_nodes()
		fileToolsLogger.info('Delete ngSkinTools2...\n')
	else:
		fileToolsLogger.info('There are no ngSkinTools skipped...\n')

	# remove unused ref
	remUnRef() 

	# import ref
	impRem()

	doDeleteSuffixExt(suffix ='_X')
	doDeletePrefixExt(prefix = 'X_')

	# delete layer
	deleteDisplayLayer()

	# add new method for re-organize group struture when publish
	doMoveGrp()

	# move node to target
	doDeleteGrp()	


	#... delete '*_bak'
	fileToolsLogger.debug('Do Delete prefix.')


	# obselet
	# doDeleteGrpTmp()
	
	# hide Root
	doHideGrp( 'Root',0 )
	doHideGrp( 'root',0 )

	# count joint
	countJnt()

	# Hold for now cause invalid
	delete_unused_skin_suffix()

	delete_unused_material()




	
	# saving
	# savingAsset( mode = 'local' )
	noCareSavAsset( mode = 'local' , mayaFile = mayafileType ,fixedName = False)

	mc.select(deselect = True)
	
#publish( mode = 'local' )




#... Global publish
def globalPublish():

	mesh = mc.ls(type = 'mesh')
	meshName = mc.listRelatives(mesh[0], allParents = True)[0]
	mc.select(meshName , r = True)


	#... Remove unused ref
	remUnRef()

	# import ref
	impRem()

	#... delete '*_bak'
	fileToolsLogger.debug('Do Delete prefix.')
	# doDeleteSuffixExt(suffix ='_bak')
	# doDeletePrefixExt(prefix = 'bak_')


	#... hide Root
	doHideGrp( 'Root',0 )
	doHideGrp( 'root',0 )

	#... delete layer
	#deleteDisplayLayer()

	#... move node to target
	doDeleteGrp()

	# print 'Move group to parent.'
	# delete grp
	# doDeleteGrpTmp()

	# write rig data
	#skinUtil.writeRigData()
	# saving
	noCareSavAsset(mode = 'global' ,fixedName = True)

	# count joint
	countJnt()

	mc.select(deselect = True)
#publish( mode = 'global' )




#... find mesh in group

def find_mesh_in_grp(group_names=['Export_grp', 'Model_grp']):
	mesh_grp = []
	
	for group in group_names:
		if mc.objExists(group):  # Check if the group exists
			print(f"Checking group: {group}")
			
			# Get all members (children) of the group
			members = mc.listRelatives(group, allDescendents=True, fullPath=True) or []
			
			for member in members:
				# Check if the member is a mesh
				if mc.nodeType(member) == 'mesh':
					# If it's a mesh, print its transform name (parent object)
					transform = mc.listRelatives(member, parent=True, fullPath=True)
					if transform:
						print(f"Mesh found: {transform[0]}")
						mesh_grp.append(transform[0])
		else:
			print(f"Group '{group}' does not exist.")
	
	return mesh_grp if mesh_grp else False  # Return the list of meshes or False if none found