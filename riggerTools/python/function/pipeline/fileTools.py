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

try:
	reload  # Python 2.7
	print('This might be python 2.7')
except NameError:
	try:
		from importlib import reload  # Python 3.4+
		print('Python 3.4+')
	except ImportError:
		from imp import reload  # Python 3.0 - 3.3
		print('Python 3.0 - 3.3')








from function.framework.reloadWrapper import reloadWrapper as rlw



import maya.cmds as mc
import os
import pymel.core as pm
import shutil
import time
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import datetime
import maya.mel as mel


# import logging
# logger = logging.getLogger('debug_text')
# logger.setLevel(logging.DEBUG)


from function.pipeline import logger 
rlw(logger)


class fileToolsLogger(logger.MayaLogger):
	LOGGER_NAME = "FileToolsLogger"


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

def createThumbnail(fileType = 'jpg'):
	# Create Thumbnail at current maya file
	currentPath = findCurrentPath()
	# date = datetime.datetime.now()
	# currentDate = date.strftime('%d%m%Y_%H%M')

	fileName = getFileName()[0]
	imageFile = '{0}{1}.{2}'.format(currentPath,fileName,fileType)
	mimage = om.MImage()
	view = omui.M3dView.active3dView()
	view.readColorBuffer(mimage, True)
	mimage.writeToFile(imageFile, fileType)
	print ('Thumbnail has been create at : {0}'.format(imageFile))


# find current maya path
def currentPath():
	path = pm.system.sceneName()
	if path:
		return path
	else:
		mc.warning("There are no file path")




def openContainerFile( path = None ):
	os.startfile(path)

def countJnt():
	num = 0
	bindJnt = mc.ls('*_bind_jnt')
	if bindJnt:
		for each in bindJnt:
			num = num + 1
		print ('The number of bind joint is %i' %num)

		# remain joint
		rJnt = 45 - num
		
		print ('%i joint remaining' %rJnt)
		mc.inViewMessage(amg = "<hl>The number of bind joint is %s</hl>" %num, pos = "midCenterTop", fade = True)





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

	if splitFolderNam == 'hero':
		print ('This is hero file.')
		return True
		
	elif splitFolderNam == 'version':
		print ('This is version file.')
		return False
	else:
		print ('Unknow condition.')
		return None




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
		mel.eval('addRecentFile("%s", "%s")'%(myPath.replace('\\', '/'), fileType))

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
		if each != 'defaultLayer' and each != 'joint' and each != 'controller':
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

def doDeleteSuffix(suffix = '_bak'):
	try:
		mc.ls('*' + suffix)[0]
		mc.delete('*' + suffix)
		fileToolsLogger.info('suffix name "{0}" has been delete.'.format(suffix))
	except:
		fileToolsLogger.info('There is no something to delete.')


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
def noCareSavAsset( mode = 'local', mayaFile = 'ma', fixedName = False ):
	
	

	# use Fixed name just in case
	if fixedName:
		if mc.objExists("rig_grp.asset_name") and mc.getAttr("rig_grp.asset_name"):
			subName_fixed = mc.getAttr("rig_grp.asset_name")
			fileToolsLogger.info('This is having a asset name: {0}'.format(subName_fixed))
		else:
			fileToolsLogger.warning('There are no asset name.')
			return False



	''' new condition to publish file '''
	assetPath = currentFolder()
	fullPath = whereAreMe()
	fileName = ''

	if fixedName:
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


		fileToolsLogger.debug('Hey!!! this is subName:  [{0}]'.format(subName))





	if mode == 'local':

		localPath = 'hero\\'
		SAVE_PATH = assetPath + localPath + subName

		fileToolsLogger.debug('Hey!!! look at this bro:  [%s]    [%s]' %(assetPath,subName))

		# if this folder not exists create folder
		checkExistFolder( filename = SAVE_PATH )

		
		# cancle file type
		if mayaFile == 'ma':
			fileType = 'mayaAscii'
		elif mayaFile == 'mb':
			fileType = 'mayaBinary'
		

		mc.file( rename = SAVE_PATH )
		mc.file( save = True, type = fileType )

		fileToolsLogger.info('file has been saved at: %s.%s' %(SAVE_PATH,mayaFile))
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

		fileToolsLogger.info('file has been saved at: %s.%s' %(SAVE_PATH,'ma'))
		fileToolsLogger.info('file has been saved at: %s.%s' %(SAVE_PATH,'mb'))

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





def impRem():
	allrefs = pm.getReferences(recursive = True )
	for ref in allrefs:
		try:
			allrefs[ref].importContents( removeNamespace = True )
		except RuntimeError:
			pass
	print ('\nImport and clear namespace ...')











# local publish
def localPublish( mayafileType = 'ma' ):



	# remove unused ref
	remUnRef() 

	# import ref
	impRem()

	# delete layer
	# deleteDisplayLayer()

	# add new method for re-organize group struture when publish
	doMoveGrp()

	# move node to target
	doDeleteGrp()	

	# delete '*_bak'
	doDeleteSuffix()

	# obselet
	# doDeleteGrpTmp()
	
	# hide Root
	doHideGrp( 'Root',0 )
	doHideGrp( 'root',0 )

	# count joint
	countJnt()

	# saving
	# savingAsset( mode = 'local' )
	noCareSavAsset( mode = 'local' , mayaFile = mayafileType )

	mc.select(deselect = True)
	
#publish( mode = 'local' )




# global publish
def globalPublish(fixedName = False):

	mesh = mc.ls(type = 'mesh')
	meshName = mc.listRelatives(mesh[0], allParents = True)[0]
	mc.select(meshName , r = True)
	

	# remove unused ref
	remUnRef()

	# import ref
	impRem()

	# hide Root
	doHideGrp( 'Root',0 )
	doHideGrp( 'root',0 )

	# delete layer
	#deleteDisplayLayer()

	# move node to target
	doDeleteGrp()

	# print 'Move group to parent.'
	# delete grp
	# doDeleteGrpTmp()

	# write rig data
	#skinUtil.writeRigData()
	# saving
	noCareSavAsset(mode = 'global',fixedName=fixedName)

	# count joint
	countJnt()

	mc.select(deselect = True)
#publish( mode = 'global' )
