from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.pipeline import fileTools 
reload(fileTools)

from function.rigging.skin import skinUtil
reload(skinUtil)

import json

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)

import maya.mel as mm

# for use 'partial' function for callback
import functools


class buildUI():
	def __init__(self):
		self.width = 200
		self.height = 200
		self.ui = 'skinData' # no not leave space because it will unknow windowID
		self.winID = '%sWin' %self.ui

	def show(self):
		print (self.winID)

		if mc.window(self.winID, exists=True):
			print ('it already exist. delete it')
			mc.deleteUI(self.winID)

		mc.window( self.winID , title=self.ui, widthHeight=(self.width, self.height), sizeable=False )
		mc.rowColumnLayout(numberOfColumns=2)
		mc.button(h=100,w=100,label="Export general \nmesh data", command = self.click_writeRigData, ann = "Export mesh general data")
		mc.button(h=100,w=100,label="Import skin \njoint list", command = self.click_importSkinJntList , ann = "Import joint into selected mesh(Just add no skin data.)")
		mc.button(h=100,w=100,label="Write \nVTX sel", command = self.click_writeVTXselected , ann = "Write selected Vertex")

		mc.showWindow()


	def click_writeRigData( self ,partFileName):
		 # write skin joint list data 
		 # using for new naming condition only

		partFileName = mc.file( q = True , sn = True )
		splitfileName = partFileName.split('/')
		preName = splitfileName[len(splitfileName)-1]

		name = preName.split('.ma')[0]
		# PART FINDER
		folderPath = partFileName.split('/'+name)[0]

		
		DATA = skinUtil._listJntSkinCluster()
		FILE_NAME = DATA['polyName'] + '_generalData' + '.json'

		if fileTools.ifHero():
			
			SAVE_PATH  = fileTools.desinatePath('\\data\\skinData\\')
			print ('this is a book'+SAVE_PATH)
		else:
			SAVE_PATH  = fileTools.desinatePath('\\data\\skinData\\')
			# if not exists create folder
			fileTools.checkExistFolder(SAVE_PATH)

		print (SAVE_PATH)
		FILE_PATH = SAVE_PATH + FILE_NAME

		f = open(	FILE_PATH, "w"	)
		f.write(	json.dumps( DATA , sort_keys=2, indent=4, )	)
		f.close()

		print ('File was save at: %s' %FILE_PATH)
		print ('\n')
		fileTools.makeHeader('Write complete')



	#broswe file skin data
	# just add skin joint list to mesh not import skin data
	def click_importSkinJntList(self,sel):
		sel = mc.ls(sl=True)[0]

		if not sel:
			print ('Please select something.')
			return False

		# check if have skin
		oldSkin = mm.eval('findRelatedSkinCluster("%s")' %sel)
		if oldSkin:
			# use arg for editable
			mc.skinCluster(oldSkin, edit = True, unbind = True)
		else:
			print ('%s is not have any skincluster' %sel)


		# get skin joint list
		jsonFilter = "*.json"
		try:
			folderPath = fileTools.currentFolder()
			if folderPath:
				fileNameDir = mc.fileDialog2( fileFilter = jsonFilter, dialogStyle = 2, fileMode = 1, okCaption = 'Open',dir =folderPath)[0]
			else:
				fileNameDir = mc.fileDialog2( fileFilter = jsonFilter, dialogStyle = 2, fileMode = 1, okCaption = 'Open')[0]
			if fileNameDir != "":
				if '/' in fileNameDir:
					clean_file = fileNameDir.replace('/','\\\\')
					print (clean_file)
					vertexData 	= 	wcd.loadData( clean_file )
					#print vertexData
					for key in vertexData.keys():
						if ( key == 'skinJnt' ):						
							skinJntList = vertexData['skinJnt']

				else:
					return False


					
		except:
			print ('Something went wrong Cancle progress...')
			return False





		print ('now we got mesh and skin joint list')
		mc.skinCluster( skinJntList, sel, toSelectedBones=True )
		fileTools.makeHeader('Add skin joint list complete')


	def click_writeVTXselected(self,DATA):
		DATA = mc.ls(sl=True)
		if 'vtx' not in DATA[0]:
			mc.error('This not vtx selection for sure.')

		if fileTools.ifHero():
			SAVE_PATH  = fileTools.desinatePath('\\data\\')
			print ('this is Hero file'+ SAVE_PATH)
		else:
			SAVE_PATH  = fileTools.desinatePath('\\data\\')
			#... if not exists create folder
			fileTools.checkExistFolder(SAVE_PATH)


		number = DATA[0].split('[')[1].split(':')[0]

		SP_NAME = DATA[0].split('.')[0]
		FILE_NAME = SP_NAME + '_' + number
		print(FILE_NAME)

		# FILE_NAME = DATA[0]

		# FILE_PATH = SAVE_PATH + FILE_NAME + '.py'

		# with open(FILE_PATH, 'w') as py_file:
		# 	py_file.write(''.join(DATA))

		FILE_PATH = SAVE_PATH + FILE_NAME + '.json'
		f = open(FILE_PATH, "w")
		f.write(json.dumps( DATA , sort_keys=2, indent=4, ))
		f.close()

		print ('File was save at: %s' %FILE_PATH)
		print ('\n')




def run():
	ui = buildUI()
	ui.show()





# run()




