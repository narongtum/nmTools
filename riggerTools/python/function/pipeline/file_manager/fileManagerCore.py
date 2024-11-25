from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import json
import os
from function.pipeline.file_manager.file_manager_ui import fileManagerMainUI
# Thumbnail
from PySide2.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMenu, QInputDialog, QMessageBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QDir, QSortFilterProxyModel

import maya.OpenMaya as om
import maya.OpenMayaUI as omui

import subprocess
import sys
from function.framework.reloadWrapper import reloadWrapper as reload

#...  ogging system 
import logging
from function.pipeline import logger 
reload(logger)

import re
import pymel.core as pm

from function.pipeline import fileTools
reload(fileTools)

from function.rigging.readWriteCtrlSizeData import run as runWrite
reload(runWrite)

# from function.rigging.skin.nsSkinClusterIO import nsSkinClusterIO_reFunc as skinIO
# reload(skinIO)

try:
	from shiboken2 import wrapInstance
except:
	from sid import wrapInstance as wrapInstance

from function.rigging.skin import roundSkinWeight as rsw
reload(rsw)

import fnmatch

class FileManagerLog(logger.MayaLogger):
	LOGGER_NAME = "FileManagerLog"





FileManagerLog.set_level(logging.DEBUG)
	
import maya.cmds as mc
MAYA_VERSION = int(mc.about(v=True))



#.... Check there is config file in document

# Get the user's home directory
user_home = os.path.expanduser("~")

# Define the directory path relative to the user's home directory
directory = os.path.join(user_home, 'Documents', 'maya', 'scripts')

# Define the file name
fileName = 'fileManager_config.py'

# Create the full file path
file_path = os.path.join(directory, fileName)




#... Static variable
THUMBNAIL_NAME		= 	'thumb.png'
PADDING 			= 	4





# Check if the file exists
if os.path.exists(file_path):
	FileManagerLog.debug("File exists.")
	import fileManager_config as config

	DRIVES = config.DRIVES
	PROJECT_NAME = config.PROJECT_NAME
	DICTIONARY_TEMPLATE = config.DICTIONARY_TEMPLATE
	#... Top folder name
	BASE_FOLDER = config.BASE_FOLDER
	ASSET_TOP_FOLDER = config.ASSET_TOP_FOLDER
	SCENE_TOP_FOLDER = config.ASSET_TOP_FOLDER
	#... Directory name
	DEPT_NAME = config.DEPT_NAME
	DEPT_EMPTY = config.DEPT_EMPTY
	JOB_TEMPLATE = config.JOB_TEMPLATE
	EXCLUDE_VIEW_ITEM = config.EXCLUDE_VIEW_ITEM
	STATIC_FOLDER = config.STATIC_FOLDER
	DEFAULT_PROJECT = config.DEFAULT_PROJECT
	MAYA_EXT = config.MAYA_EXT
	USE_VARIATION = config.USE_VARIATION
	SVN_BIN_PATH = config.SVN_BIN_PATH
	HIDE_FORMAT = config.HIDE_FORMAT

	FileManagerLog.debug("using {0} as a default project.".format(DEFAULT_PROJECT))

else:
	FileManagerLog.debug("File does not exist using default config.")




	#... Using default config
	DRIVES = [		"D:\\",
					"E:\\"		]

	PROJECT_NAME = ['P_sample','P_jobby','P_Regulus']

	DICTIONARY_TEMPLATE = {		

								"base_path":""				,
								"entitie_type":""			,
								"entitie_name":""			,
								"full_entity_name":""		,
								"comment":""				,
								"department_name":""		,
								"add_path_SVN":""

								}

	BASE_FOLDER = "svn_true"
	ASSET_TOP_FOLDER = "Content"
	SCENE_TOP_FOLDER = "Sequence"

	
	# DEPT_NAME 		= 	['Model', 'Rig']
	DEPT_NAME 			= 	['Model', 'Rig', 'Anim']
	# DEPT_EMPTY 		= 	['ConceptArt', 'ConceptArt', 'Texture', 'VFX', 'Anim']
	DEPT_EMPTY 			= 	['Commit','Texture', 'ConceptArt','FBX']
	JOB_TEMPLATE 		= 	['Version', 'Data', 'Output', 'Commit', 'FBX']
	EXCLUDE_VIEW_ITEM 	= 	['data.json', THUMBNAIL_NAME, 'Commit']
	STATIC_FOLDER 		= 	[ASSET_TOP_FOLDER, 'Version', 'Commit']
	DEFAULT_PROJECT 	= 	'P_Regulus'
	
	MAYA_EXT 			= 	'ma'
	USE_VARIATION 		= 	('P_Regulus')
	SVN_BIN_PATH 		= r"C:\Program Files\TortoiseSVN\bin"
	HIDE_FORMAT = ['*.pyc', '*.o']
	









import maya.OpenMayaUI as OpenMayaUI

#... get this window alway on top
#... chad vernon said about parent window on top at 1:16 (crateing the remapping dialog)
def getMayaMainWindow():
	main_window_ptr = OpenMayaUI.MQtUtil.mainWindow() #... find maya pointer
	if MAYA_VERSION >= 2022:
		pointer = wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
	else:
		pointer = wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
	return pointer


#... try for enable filter widget
class FilterProxyModel(QtCore.QSortFilterProxyModel):
	def __init__(self, parent=None):
		super(FilterProxyModel, self).__init__(parent)
		self._pattern = ""

	@property
	def pattern(self):
		return self._pattern

	@pattern.setter
	def pattern(self, value):
		self._pattern = value
		self.invalidateFilter()

	def filterAcceptsRow(self, sourceRow, sourceParent):
		if not self.pattern:
			return True

		sourceModel = self.sourceModel()
		index = sourceModel.index(sourceRow, 0, sourceParent)
		filePath = sourceModel.filePath(index)
		fileName = sourceModel.fileName(index)

		if self.pattern.lower() in fileName.lower():
			return True

		if sourceModel.isDir(index):
			childCount = sourceModel.rowCount(index)
			for i in range(childCount):
				if self.filterAcceptsRow(i, index):
					return True

		return False



class FileManager(fileManagerMainUI.Ui_MainWindow, QtWidgets.QMainWindow):
	_instance = None

	# Initialize the parent class and set up the UI
	def __init__(self):
		
		parent = getMayaMainWindow()
		super(FileManager, self).__init__(parent=parent)
		self.setupUi(self)
		self.path = None
		FileManagerLog.debug('Run this first...')

		# Define model as an instance variable
		# self.model = None


		#... My existing code

		# Create an instance of the SvnMaya class
		self.svn_maya = SvnMaya()
		

		#... Populate Drive and Project combo boxes
		self.populate_drives()
		self.populate_project()
		# self.update_project_comboBox() #... It seems redundance with connect update_project_comboBox

		FileManagerLog.debug('Set default project...')
		self.drive_comboBox.setCurrentText(DRIVES[0])
		self.project_comboBox.setCurrentText(DEFAULT_PROJECT)


		# selected_project = self.project_comboBox.currentText() #... no need

		#...  Set menu bar
		self.setupMenuBar()

		#... Set "Asset" tab as default
		self.entite_TAB.setCurrentIndex(0)  

		#... Connect project signals
		self.drive_comboBox.currentIndexChanged.connect(self.update_project_comboBox)

		# Called whenever a new item is clicked
		self.populate_ASSET_treeView()

		#... Connect project
		self.project_comboBox.currentIndexChanged.connect(self.populate_ASSET_treeView)	

		#... if maya open and set project correctly 
		#... set combo box to that

		if self.is_scene_open():
			current_scene_path = pm.system.sceneName()
			current_scene_path = os.path.normpath(current_scene_path)
			path_elements = current_scene_path.split(os.path.sep)
			if path_elements[2] in PROJECT_NAME:
				FileManagerLog.debug(f'# line: 266 # # Set Project to: {path_elements[2]}')
				self.project_comboBox.setCurrentText(path_elements[2])


				#... make set current drive that scene open
				current_drive = path_elements[0] + '\\'
				if current_drive in DRIVES:
					FileManagerLog.debug(f'# line: 275 # # Set Drive to: {current_drive}')
					current_drive_index = DRIVES.index(current_drive)
					self.drive_comboBox.setCurrentText(DRIVES[current_drive_index])
					



		# Connect the on_treeview_clicked method to the clicked signal
		self.asset_dir_TREEVIEW.clicked.connect(self.on_treeview_clicked)

		# Connect The 'on_department_clicked' method to the clicked signal
		self.asset_department_listWidget.itemClicked.connect(self.on_department_clicked)

		#... Connect entity scene to treeview
		self.populate_SCENE_treeView()
		self.dir_scene_TREEVIEW.clicked.connect(self.on_treeview_SCENE_clicked)


		# # Connect the on_version_clicked method to the left clicked signal
		# # No need to use anymore disable for now
		# self.asset_version_view_listWidget.itemClicked.connect(self.on_version_clicked)

		# # Create jobs at department level
		# self.asset_department_listWidget = QListWidget()
		# self.setCentralWidget(self.asset_department_listWidget)

		# Show context for department widget
		self.asset_department_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.asset_department_listWidget.customContextMenuRequested.connect(self.show_job_context_menu)

		# Show context for version widget
		self.asset_version_view_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.asset_version_view_listWidget.customContextMenuRequested.connect(self.show_step_context)

		#... Show context for global widget
		self.asset_global_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.asset_global_listWidget.customContextMenuRequested.connect(self.handle_right_click_global_widget)

		#... Show context for local widget
		self.asset_local_view_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.asset_local_view_listWidget.customContextMenuRequested.connect(self.handle_right_click_local_widget)

		#... Set up context menu
		self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) #... repetitive code with __init__
		self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu) #... repetitive code with __init__

		#... Handle double click
		self.asset_version_view_listWidget.itemDoubleClicked.connect(self.handle_double_click)

		self.asset_local_view_listWidget.itemDoubleClicked.connect(self.handle_double_click_local_widget)

		self.asset_global_listWidget.itemDoubleClicked.connect(self.handle_double_click_global_widget)

		# Connect the function to the clicked signal button
		self.asset_localCommit_BTN.clicked.connect(self.push_btn_local_publish)

		# Connect the function to the clicked signal button
		self.asset_commit_BTN.clicked.connect(self.push_btn_global_publish)

	def is_scene_open(self):
		current_scene = mc.file(query=True, sceneName=True)
		return bool(current_scene)

	# def closeEvent(self, event):
	# 	# Remove the window instance from the list of open windows
	# 	self.open_windows.remove(self)
	# 	# Call the base class closeEvent to ensure proper cleanup
	# 	super(FileManager, self).closeEvent(event)
		
	def setupMenuBar(self):
		file_menu = self.menuFile
		toos_menu = self.menuTools

		#... Create 'thumbnail' action and add it to the 'File' menu
		create_thumbnail_action = FileManagerActions.createThumbnailAction(self, self.create_thumbnail)
		file_menu.addAction(create_thumbnail_action)

		# Create 'Print A' action and add it to the 'File' menu
		print_b_action = FileManagerActions.createPrintBAction(self, self.printB)
		toos_menu.addAction(print_b_action)	

		save_ctrl_shape_action = FileManagerActions.saveCtrlShapeAction(self, self.save_ctrl_shape)
		toos_menu.addAction(save_ctrl_shape_action)

		load_ctrl_shape_action = FileManagerActions.loadCtrlShapeAction(self, self.load_ctrl_shape)
		toos_menu.addAction(load_ctrl_shape_action)
		toos_menu.addSeparator()
		save_skinWeight_action = FileManagerActions.saveSkinWeightAction(self, self.save_skin_data)
		toos_menu.addAction(save_skinWeight_action)

		load_skinWeight_action = FileManagerActions.loadSkinWeightAction(self, self.load_skin_data)
		toos_menu.addAction(load_skinWeight_action)


	def printA(self):
		print("Print A")

	def printB(self):
		print("Print B")

	# def filter_model(self, text):
	# 	self.proxyModel.pattern = text

	def filter_model(self, text):
		# Apply the filter to the proxy model
		search_pattern = f"*{text}*"  # Wildcards allow partial matches
		self.proxyModel = QtCore.QSortFilterProxyModel()
		self.proxyModel.setFilterWildcard(search_pattern)

	def handle_double_click(self, item):
		# Double click is mean open
		file_path = self.get_deep_path() #... get path from selected in UI
		FileManagerLog.debug('This is _get_full_path: {0}'.format(file_path))

		# Check file extension
		file_name, extension = os.path.splitext(file_path)

		
		if extension == '.mb' or extension == '.ma':
			self.maya_open(file_path)
		else:
			FileManagerLog.debug('There are no extension ?.')
			os.startfile(file_path)

	#....
	#.... MENU BAR
	#....

	def create_thumbnail(self, fileType='png', width=256, height=256, fileName = 'thumb'):
		maya_file_path = mc.file( query=True , sn=True )

		if maya_file_path:

			folder_path = os.path.dirname(maya_file_path)

			parent_folder = os.path.basename(folder_path)

		#... if There is in 'VERSION' folder
		if parent_folder == STATIC_FOLDER[1]:
			FileManagerLog.debug("The folder containing named 'Version'.")

			folder_path = os.path.dirname(folder_path)
			asset_path = os.path.dirname(folder_path)

			# Department path
			asset_name = os.path.basename(asset_path)

			if os.path.exists(os.path.join(asset_path, 'data.json')):
				FileManagerLog.debug('This file is valid Go on ')
				save_path = asset_path


		#... There is in 'COMMIT' folder maybe Global or Local commit
		elif parent_folder == STATIC_FOLDER[2]:
			FileManagerLog.debug("	There is Local Commit file.")

			FileManagerLog.debug("	folder_path path is >>> {0}".format(folder_path))

			#... Check is global or local commit file
			back_folder_path = os.path.dirname(folder_path)
			FileManagerLog.debug("	back_folder_path path is >>> {0}".format(back_folder_path))

			asset_name = os.path.dirname(back_folder_path)


			#... Check valid data
			if os.path.exists(os.path.join(back_folder_path, 'data.json')): #... This is Global commit
				FileManagerLog.debug('\t425-This file is Global Commit >>> {0}'.format(back_folder_path))
				save_path = back_folder_path
			else: #... This is Local commit get correct dir
				save_path = os.path.dirname(back_folder_path)



		#... Create Thumbnail at current maya file
		# final_save_path = '{0}{1}.{2}'.format(save_path, fileName, fileType)


		# save_path = os.path.normpath(os.path.join(save_path,'{0}.{1}'.format(fileName, fileType)))
		save_full_path = os.path.normpath(os.path.join(save_path,'{0}.{1}'.format(fileName, fileType)))

		
		print(f'this is save_path: {save_path}')
		#... normalize path before execute
		save_path = os.path.join(save_path, '')

		# save_path = os.path.normpath(save_path)

		# mc.error(save_path)


		# fileTools.createThumbnail_ext(fileName, fileType)
		fileTools.createThumbnail_ext(currentPath=save_path, fileName=fileName)


		'''
		import maya.OpenMaya as om
		import maya.OpenMayaUI as omui
		mimage = om.MImage()
		view = omui.M3dView.active3dView()
		view.readColorBuffer(mimage, True)

		# Resize the image to the specified width and height
		mimage.resize(width, height)

		mimage.writeToFile(save_path, fileType)
		print('Thumbnail has been created at: {0}'.format(save_path))
		'''


		save_full_path = os.path.normpath(save_full_path)


		#... Asking SVN
		reply = QMessageBox(self)
		reply.setWindowTitle('Commit Changes')
		reply.setText('Do you want to commit thumbnail to SVN ?\n\t')

		commit_button = reply.addButton('Commit', QMessageBox.AcceptRole)
		save_button = reply.addButton('Just Save', QMessageBox.AcceptRole)
		reply.addButton(QMessageBox.Cancel)	

		result = reply.exec_()	
		if reply.clickedButton() == commit_button:

			#... Add SVN
			self.svn_maya.execute_cmd('add', file_path = save_full_path, close_on_end=0, logmsg='')

			#...Commit SVN
			self.svn_maya.execute_cmd('commit', file_path = save_full_path, close_on_end=0, logmsg='')

		elif reply.clickedButton() == save_button:
			pass


	#... Save and Load controller shape data
	def save_ctrl_shape(self):
		# print("Print B")
		runWrite.savingData()

	def load_ctrl_shape(self):
		runWrite.loadingData(self)

	#... Save and Load skin data
	def save_skin_data(self):
		skinIO.saveSkin()

	def load_skin_data(self):
		skinIO.loadSkin()





		

	#... Handle right click for global widget
	def show_global_widget_explorer(self):
		asset_path_text = self._get_full_path()		
		full_path = os.path.join(asset_path_text, STATIC_FOLDER[2])
		FileManagerLog.debug('this is new_folder_path: \t\t {0}'.format(full_path))
		self._open_folder_path(full_path)

	def handle_right_click_global_widget(self, position):
		contextMenu = QtWidgets.QMenu(self)

		#... Add show in Explorer
		showInExplorer_action = QtWidgets.QAction("Show in Explorer", self)
		# Link to method
		showInExplorer_action.triggered.connect(self.show_global_widget_explorer)
		contextMenu.addAction(showInExplorer_action)

		#... Add Reference action
		reference_action = QtWidgets.QAction("Reference selected this file...", self)
		# Link to method
		reference_action.triggered.connect(self.handle_reference_global_widget)
		contextMenu.addAction(reference_action)

		# Disconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_global_listWidget.customContextMenuRequested.disconnect(self.handle_right_click_global_widget)

		contextMenu.exec_(self.asset_global_listWidget.mapToGlobal(position))

		# Reconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_global_listWidget.customContextMenuRequested.connect(self.handle_right_click_global_widget)


	def handle_reference_global_widget(self):
		file_path = self.get_deep_path_global_commit()
		FileManagerLog.debug("Return file_path name: {0}".format(file_path) )
		self.maya_reference_noAsk(file_path)


	def get_deep_path_global_commit(self):
		asset_path_text = self._get_full_path()
		# full_department_path = self._get_department_path()

		global_commit = self.asset_global_listWidget.currentItem()
		global_commit_text = global_commit.text()

		full_path = os.path.join(asset_path_text, STATIC_FOLDER[2], global_commit_text)
		full_path = os.path.normpath(full_path)

		FileManagerLog.debug("Return full_path name: {0}".format(full_path) )
		return full_path

	#... right click and reference
	def handle_reference_version_widget(self):
		file_path = self.get_deep_path()
		FileManagerLog.debug("Return file path name: {0}".format(file_path))
		self.maya_reference_noAsk(file_path)


	def show_local_widget_explorer(self):

		asset_path_text = self._get_full_path()
		FileManagerLog.debug('this is asset_path_text: \t\t {0}'.format(asset_path_text))

		new_department_text = self.asset_department_listWidget.currentItem().text()
		FileManagerLog.debug('this is new_department_text: \t\t {0}'.format(new_department_text))

		new_folder_path = os.path.join(asset_path_text, new_department_text, STATIC_FOLDER[2])

		FileManagerLog.debug('this is new_folder_path: \t\t {0}'.format(new_folder_path))
		self._open_folder_path(new_folder_path)

		




	def handle_right_click_local_widget(self, position):

		contextMenu = QtWidgets.QMenu(self)

		# Add show in Explorer
		local_commit_showInExplorer_action = QtWidgets.QAction("Show in Explorer", self)
		# Link to method
		local_commit_showInExplorer_action.triggered.connect(self.show_local_widget_explorer)
		contextMenu.addAction(local_commit_showInExplorer_action)

		# Add Reference action
		reference_action = QtWidgets.QAction("Reference selected this file...", self)
		# Link to method
		reference_action.triggered.connect(self.handle_reference_local_widget)
		contextMenu.addAction(reference_action)

		# Disconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_local_view_listWidget.customContextMenuRequested.disconnect(self.handle_right_click_local_widget)

		contextMenu.exec_(self.asset_local_view_listWidget.mapToGlobal(position))

		# Reconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_local_view_listWidget.customContextMenuRequested.connect(self.handle_right_click_local_widget)



	def handle_reference_local_widget(self):
		file_path = self.get_deep_path_local_commit()
		self.maya_reference(file_path)

	def handle_double_click_global_widget(self):
		#... Double click is mean open
		full_path = self._get_full_path()

		global_commit = self.asset_global_listWidget.currentItem()
		global_commit_text = global_commit.text()

		file_path = os.path.join(full_path, STATIC_FOLDER[2], global_commit_text)
		file_path = os.path.normpath(file_path)

		FileManagerLog.debug('This is file_path >>> {0}'.format(file_path))
		#... Next try to open file

		file_name, extension = os.path.splitext(file_path)

		if extension == '.mb' or extension == '.ma':
			self.maya_open(file_path)
		else:
			FileManagerLog.debug('File are no extension ?.')
			os.startfile(file_path)


	def handle_double_click_local_widget(self, item):
		# Double click is mean open
		file_path = self.get_deep_path_local_commit()
		FileManagerLog.debug('This is _get_full_path: {0}'.format(file_path))

		# Check file extension
		file_name, extension = os.path.splitext(file_path)

		if extension == '.mb' or extension == '.ma':
			self.maya_open(file_path)
		else:
			FileManagerLog.debug('There are no extension ?.')
			os.startfile(file_path)	

			

	# Show Context menu for Version widget
	def show_local_version_explorer(self):

		asset_path_text = self._get_full_path()
		FileManagerLog.debug('this is asset_path_text: \t\t {0}'.format(asset_path_text))

		new_department_text = self.asset_department_listWidget.currentItem().text()
		FileManagerLog.debug('this is new_department_text: \t\t {0}'.format(new_department_text))

		new_folder_path = os.path.join(asset_path_text, new_department_text, STATIC_FOLDER[1])

		FileManagerLog.debug('this is new_folder_path: \t\t {0}'.format(new_folder_path))
		self._open_folder_path(new_folder_path)
		

	#... [update] Add handle right click version widget
	def show_step_context(self, position):

		# Create Jobs
		contextMenu = QtWidgets.QMenu(self)

		# Add show in Explorer
		setp_showInExplorer_action = QtWidgets.QAction("Show in Explorer", self)
		# Link to method
		setp_showInExplorer_action.triggered.connect(self.show_local_version_explorer)
		contextMenu.addAction(setp_showInExplorer_action)

		#... Add Reference action
		reference_action = QtWidgets.QAction("Reference selected this file...", self)
		# Link to method
		reference_action.triggered.connect(self.handle_reference_version_widget)
		contextMenu.addAction(reference_action)


		createStep_action = QtWidgets.QAction("Create New Step...", self)
		# Link to method
		createStep_action.triggered.connect(self.create_job_step)
		contextMenu.addAction(createStep_action)



		result_job_element = self.query_step_list()
		FileManagerLog.debug('There are alway step list why?_122_: \t\t {0}'.format(result_job_element))

		if result_job_element:

			step_list = result_job_element['step']

			# Define the dynamic context options
			dynamic_context = step_list



			# Create actions for each dynamic context option
			for option in dynamic_context:
				action = QtWidgets.QAction(option, self)
				# Set the action's data to the selected option
				action.setData(option)
				# Connect the action's triggered signal to a slot
				action.triggered.connect(self.handle_dynamic_context)
				contextMenu.addAction(action)
		else:
			FileManagerLog.debug('There are no step list_236_')



		# Disconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_version_view_listWidget.customContextMenuRequested.disconnect(self.show_step_context)

		# Show the context menu at the specified position
		contextMenu.exec_(self.asset_version_view_listWidget.mapToGlobal(position))

		# Reconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_version_view_listWidget.customContextMenuRequested.connect(self.show_step_context)


	#... right click at version widget
	def handle_dynamic_context(self):
		# Get the selected action
		action = self.sender()
		# Get the data (selected context option) from the action
		selected_context = action.data()

		# Create a confirmation dialog
		confirmation_dialog = QMessageBox(self)
		confirmation_dialog.setIcon(QMessageBox.Question)
		confirmation_dialog.setText(f"Are you sure you want to save this step job\n\t{selected_context} ?")
		confirmation_dialog.setWindowTitle("Confirmation")
		confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		confirmation_dialog.setDefaultButton(QMessageBox.No)

		# Execute the dialog and get the user's choice
		choice = confirmation_dialog.exec_()

		if choice == QMessageBox.Yes:
			# User confirmed, perform the save operation
			# Perform the desired operation based on the selected context
			print(f"Selected context: {selected_context}")
			# Replace the print statement with your own logic for handling the selected context
			self.create_name_saving(selected_context)

		else:
			# User cancelled, do nothing or handle accordingly
			pass





	def find_step_and_version(self, my_list): # Find Step name and max value of this version
		FileManagerLog.debug('my_list >>> 187 >>> : {0}'.format(my_list))
		if my_list != None:
			result_job_element = {
								"step": [],
								"max_version": []
													}
			result = {}

			# Try to find another method for list that include more '_' in name
			current_index = self.asset_dir_TREEVIEW.currentIndex()
			full_path = self.model.filePath(current_index)

			full_path = os.path.normpath(full_path)

			full_path = full_path.split('\\')
			FileManagerLog.debug('\n\n\nGot full_path: {0}'.format(full_path))
			department_text = self.asset_department_listWidget.currentItem().text()

			if self.project_comboBox.currentText() in USE_VARIATION:
				use_name = full_path[-2] + '_' + full_path[-1] + '_' + department_text + '_'	
			else:
				use_name = full_path[-1] + '_' + department_text + '_'

			line_number = sys._getframe().f_lineno
			FileManagerLog.debug('\nGot Result({1}): {0}'.format(full_path, line_number))
			FileManagerLog.debug('Got use_name: {0}'.format(use_name))

			
			FileManagerLog.debug('Got Result: {0}\n\n\n'.format(department_text))


			# filter out not proper name
			filtered_list = [name for name in my_list if name.startswith(use_name)]

			# Useing new condition
			for element in filtered_list:

				

				# Replace with proper folder structer name
				replace_name = element.replace(use_name,'')
				replace_name = replace_name.split('.')

				if len(replace_name) == 3:
					name = replace_name[0]	

					FileManagerLog.debug('\nGot replace_name: {0}'.format(replace_name[0]))
					FileManagerLog.debug('Got element: {0}\n'.format(element))
					version = int(re.search(r'\.(\d+)\.ma$|\.mb$', element).group(1))
					if name not in result or version > int(result[name][1]):
						result[name] = [element, version]



				else:
					FileManagerLog.error('{0} is wrong here.'.format(use_name))
					continue


				





			if result == {}:
				FileManagerLog.debug('result_job_element_209_: {0}'.format('There are no right naming to Query'))
				return False





			for name in result:
				result_job_element["step"].append(name)
				result_job_element["max_version"].append(result[name][1])
			FileManagerLog.debug('result_job_element_144_: {0}'.format(result_job_element))
			return result_job_element
		else:
			return False

	def query_step_list(self): # Use to query list for context menu

		step_filter_list = self.filter_proper_version_list()
		FileManagerLog.debug('This should be False_256 \t\t>>>\t\t : {0}'.format(step_filter_list))

		result_job_element = self.find_step_and_version(step_filter_list)

		if step_filter_list == None:		
			FileManagerLog.debug('This should be None: {0}'.format(result_job_element))
			return False

		else:
			FileManagerLog.debug('This should be Exists: {0}'.format(result_job_element))
			return result_job_element


	def push_btn_global_publish(self):
		#... Publish global file that Maya currenly open

		try:
			asset_path = self._get_full_path()
			department_text = self.asset_department_listWidget.currentItem().text()

			global_path = os.path.join(asset_path, STATIC_FOLDER[2])
			global_path = os.path.normpath(global_path)

			
			global_path_list = global_path.split(os.path.sep)
			FileManagerLog.debug('This is global_path_list ( {0} )'.format(global_path_list))

			selected_project = self.project_comboBox.currentText()

			if selected_project in USE_VARIATION:

				global_commit_name = global_path_list[-3] + '_' + global_path_list[-2] + '_' + department_text

			else:
				global_commit_name = global_path_list[-2] + '_' + department_text


			FileManagerLog.debug('\nThis is global_path ( {0} )'.format(global_path))
			FileManagerLog.debug('This is global_commit_name ( {0} )'.format(global_commit_name))

			save_full_path = os.path.join(global_path, global_commit_name)

			line_number = sys._getframe().f_lineno
			FileManagerLog.debug('({0})Do something before maya file commit.....'.format(line_number))


			reply = QMessageBox(self)
			reply.setWindowTitle('Commit Changes')
			reply.setText('Do you want to commit file to SVN ?\n\t{0}'.format(global_commit_name))


			commit_button = reply.addButton('Commit', QMessageBox.AcceptRole)
			save_button = reply.addButton('Just Save', QMessageBox.AcceptRole)
			reply.addButton(QMessageBox.Cancel)	

			result = reply.exec_()	
			# Do global_commit_name	
			if reply.clickedButton() == commit_button:

				# 1.Procress manage scene
				do_global_commit()			

				# 2.Maya Save
				FileManagerLog.debug('save_full_path: {0}  ,  MAYA_EXT: {1}'.format(save_full_path,(MAYA_EXT)))
				#... update return logmsg for SVN
				save_full_path, logmsg = self.maya_save(global_path, global_commit_name, MAYA_EXT, 'global')

				# 3.Add SVN
				self.svn_maya.execute_cmd('add', file_path=save_full_path+'.'+MAYA_EXT, close_on_end=0, logmsg=logmsg)

				# 4.Commit SVN
				self.svn_maya.execute_cmd('commit', file_path=save_full_path+'.'+MAYA_EXT, close_on_end=0, logmsg=logmsg)

				# 5.Update localWidget viewport
				self.load_global_commit(global_path)

			elif reply.clickedButton() == save_button:
				# 1.Procress manage scene
				do_global_commit()

				# 2.Maya Save
				FileManagerLog.debug('save_full_path: {0}, MAYA_EXT: {1}'.format(save_full_path,(MAYA_EXT)))
				self.maya_save(global_path, global_commit_name, MAYA_EXT, 'global')

				# 3.Update localWidget viewport
				self.load_global_commit(global_path)

			elif result == QMessageBox.Rejected:
					print('Cancel button clicked')
					pass




		except Exception as e:
			print("Error:", e)
			FileManagerLog.error('Path file not valid name please check: {0}'.format(global_path))




	def push_btn_local_publish(self):

		# TODO: Create check what is type of this file

		# Get full path that current open in maya
		maya_file_path = mc.file( query=True , sn=True )


		full_path = self._get_full_path()
		department_text = self.asset_department_listWidget.currentItem().text()
		full_path = os.path.join(full_path, department_text, STATIC_FOLDER[2])


		if maya_file_path:
			# try:
			file_ext = os.path.basename(maya_file_path)
			FileManagerLog.debug('This is file_ext_302_: {0}'.format(file_ext))

			# Splits a pathname into a pair (root, ext)
			file_name = os.path.splitext(file_ext)[0]

			# Check if righ naming version (****.0001.ma) of this pipeline 
			check_digit = (os.path.splitext(file_ext)[0]).split('.')[-1]

			if check_digit.isdigit():

				# Check if valid name 
				digits = [count for count in check_digit if count.isdigit()]
				padding_count = len(digits)

				if padding_count == PADDING:

				# if file_name.split('.')[-1].isdigit():# Check if valid name 
					
					local_commit_name = file_name.split('.')[0]

					FileManagerLog.debug('This is local_commit_name: {0}'.format(local_commit_name))
					# do the naming and publish
					# cut '.000x' and replace with step job
					# Ex. 		 003_Lucille    01       Rig  skel.ma
					# 	 		[assetname]_[variation]_[job]_[step]
					# 		Do something when publish

			else:
				FileManagerLog.debug('This not valid name: using original ( {0} )'.format(file_name))
				local_commit_name = file_name
				pass

			# Saving file to local commit location

			FileManagerLog.debug('save file at: ({0}) and file name is ({1})'.format(full_path, local_commit_name))
			save_full_path = os.path.join(full_path, local_commit_name)


			line_number = sys._getframe().f_lineno
			FileManagerLog.debug('({0})Do something before maya file commit.....'.format(line_number))






			reply = QMessageBox(self)
			reply.setWindowTitle('Commit Changes')
			reply.setText('Do you want to commit file to SVN ?\n\t{0}'.format(local_commit_name))


			commit_button = reply.addButton('Commit', QMessageBox.AcceptRole)
			save_button = reply.addButton('Just Save', QMessageBox.AcceptRole)
			reply.addButton(QMessageBox.Cancel)	

			result = reply.exec_()	

			# Local commit action
			if reply.clickedButton() == commit_button:
				# 1. Procress manage scene
				do_local_commit()

				# 2. Maya Save
				FileManagerLog.debug('save_full_path: {0}  ,  MAYA_EXT: {1}'.format(save_full_path, (MAYA_EXT)))
				FileManagerLog.debug('full_path: {0}\n local_commit_name: {1}\n MAYA_EXT: {2}'.format(full_path, local_commit_name, MAYA_EXT))
				save_path, logmsg = self.maya_save(full_path, local_commit_name, MAYA_EXT, 'local')

				FileManagerLog.debug('this is logmsg: {0}'.format(logmsg))
				# mc.error('WHAT')

				#... update return logmsg for SVN
				# 3. Add SVN
				self.svn_maya.execute_cmd('add', file_path=save_full_path+'.'+MAYA_EXT, close_on_end=0, logmsg=logmsg)

				# 4. Commit SVN
				self.svn_maya.execute_cmd('commit', file_path=save_full_path+'.'+MAYA_EXT, close_on_end=0, logmsg=logmsg)

				# 5. Update localWidget viewport
				self.load_local_commit(full_path)

			elif reply.clickedButton() == save_button:
				# 1. Procress manage scene
				line_number = sys._getframe().f_lineno
				FileManagerLog.debug('({0})Do local commit'.format(line_number))
				do_local_commit()


				# 2. Maya Save
				FileManagerLog.debug('save_full_path: {0}  ,  MAYA_EXT: {1}'.format(save_full_path,(MAYA_EXT)))
				self.maya_save(full_path, local_commit_name, MAYA_EXT, 'local')

				# 3. Update localWidget viewport
				self.load_local_commit(full_path)

			elif result == QMessageBox.Rejected:
					print('Cancel button clicked')
					pass



	
		

			'''except Exception as e:
													FileManagerLog.debug('File not valid name please check: {0}'.format(maya_file_path))
													print("Error:", e)'''
				

		else:
			FileManagerLog.debug('The current file not maya saving file do it later.')
			return False

	def update_project_name(self):
		FileManagerLog.debug(f'\tUI has change project name to >>> {self.project_comboBox.currentText()}')


		current_scene_path = pm.system.sceneName()
		
		# Check where is the scene is saved
		if current_scene_path:
			# Normalize the path
			current_scene_path = os.path.normpath(current_scene_path)

			# Split the path to extract relevant information
			path_elements = current_scene_path.split(os.path.sep)
			FileManagerLog.debug('	This is path_elements >>> {0}'.format(path_elements))
			
			# Extract the asset and department names
			asset_name = path_elements[-4]
			department_name = path_elements[-3]

			#... Extract Project names (updated)
			project_name = path_elements[2]
			FileManagerLog.debug('	This is project_name >>> {0}'.format(project_name))
			FileManagerLog.debug('	[{0}] <<<   >>> [{1}]'.format(project_name, self.project_comboBox.currentText()))

			if project_name != self.project_comboBox.currentText(): #... in case for make can change project with already open scene other project
				FileManagerLog.debug('	[{0}] <<< is not equal set project to  >>> [{1}]'.format(project_name, self.project_comboBox.currentText()))
				#... change project
				# self.project_comboBox.setCurrentText(self.project_comboBox.currentText()) 
			else:
				FileManagerLog.debug('{0} is same as {1}'.format(project_name, self.project_comboBox.currentText()))
				pass
			FileManagerLog.debug('# # # update_project_name # # #')		


	def check_exists_maya(self):

		'''
		Check the curenty maya file that already open is in the proper file manager path
		'''

		maya_file_path = mc.file( query=True , sn=True )

		if maya_file_path:

			folder_path = os.path.dirname(maya_file_path)

			parent_folder = os.path.basename(folder_path)

			

			#... ensures that the code works correctly regardless of the underlying operating system.

			#... There open in 'VERSION' folder

			if parent_folder == STATIC_FOLDER[1]:
				FileManagerLog.debug("The folder containing named 'Version'.")

				folder_path = os.path.dirname(folder_path)
				asset_path = os.path.dirname(folder_path)

				# Department path
				asset_name = os.path.basename(asset_path)

				if os.path.exists(os.path.join(asset_path, 'data.json')):
					FileManagerLog.debug('This file is valid Go on ')

					self.update_to_browser(asset_path)

					self.populate_version_from_open_scene(asset_path)


					

			#... If open in 'COMMIT' folder

			elif parent_folder == STATIC_FOLDER[2]:
				FileManagerLog.debug("	Their is Commit file.")

				#... check is global or local commit file
				back_folder_path = os.path.dirname(folder_path)
				FileManagerLog.debug("	back_folder_path path is >>> {0}".format(back_folder_path))

				#... Check valid data
				if os.path.exists(os.path.join(back_folder_path, 'data.json')):

					#... This is global commit
					FileManagerLog.debug('	1143 -This file is Global Commit >>> {0}'.format(back_folder_path))

					#... Show Asset name at global widget
					#... Make auto selected Asset name for make script continue to work
					asset_index = self.model.index(back_folder_path)
					self.asset_dir_TREEVIEW.selectionModel().setCurrentIndex(asset_index, QtCore.QItemSelectionModel.ClearAndSelect)
					# Make the treeView scroll to the selected item
					self.asset_dir_TREEVIEW.scrollTo(asset_index, QtWidgets.QAbstractItemView.PositionAtTop)

					#... Show file on global widget
					self.load_global_commit(folder_path)





				else:
					FileManagerLog.debug('This file Local Commit')

					# Extract the desired part of the path
					assetName_path = os.path.dirname(back_folder_path)


					#... Select Asset Name
					FileManagerLog.debug('	1167-	This is assetName_path >>> {0}'.format(assetName_path))
					asset_index = self.model.index(assetName_path)
					self.asset_dir_TREEVIEW.selectionModel().setCurrentIndex(asset_index, QtCore.QItemSelectionModel.ClearAndSelect)
					self.asset_dir_TREEVIEW.scrollTo(asset_index, QtWidgets.QAbstractItemView.PositionAtTop)

					#... Select Department Name

					#... normalize path first
					back_folder_path = os.path.normpath(back_folder_path)
					path_elements = back_folder_path.split(os.path.sep)
					FileManagerLog.debug('	1177-	This is Department Name >>> {0}'.format(path_elements[-1]))

					#... Add department here
					self.asset_department_listWidget.addItem(path_elements[-1])
					department_item = self.asset_department_listWidget.findItems(path_elements[-1], QtCore.Qt.MatchExactly)
					self.asset_department_listWidget.setCurrentItem(department_item[0])

					#... Populate asset Info
					data_file = os.path.join(assetName_path, 'data.json')
					with open(data_file, "r") as file:
						json_data = json.load(file)
					self.assetInfo_list_listWidget.addItem(json_data['comment'])

					#... Populate thumbnail
					thumbnail_path = os.path.join(assetName_path, THUMBNAIL_NAME)
					self.display_images(thumbnail_path)

					global_path = os.path.join(assetName_path, STATIC_FOLDER[2])
					self.load_global_commit(global_path)


					self.load_local_commit(folder_path)
					#... Make auto selected asset name for make script continue to work


			else:
				pass

	#... If user already open scene 
	def update_to_browser(self, file_path):
		'''
		Check the curenty maya file that already open is in the proper file manager path
		'''

		FileManagerLog.debug("	The Scene is already open: {0}".format(file_path))

		# Convert the desired directory path to a model index
		index = self.model.index(file_path)

		if index.isValid():
			self.asset_dir_TREEVIEW.selectionModel().setCurrentIndex(index, QtCore.QItemSelectionModel.ClearAndSelect)

			#... Make the treeView scroll to the selected item
			self.asset_dir_TREEVIEW.scrollTo(index, QtWidgets.QAbstractItemView.PositionAtTop)

			
		## Expand the QTreeView to the parent item of the desired directory
		# self.asset_dir_TREEVIEW.expand(index.parent())

		## Get the model index of the desired directory
		# desired_index = self.model.index(file_path)

		## Select the item at the model index
		# self.asset_dir_TREEVIEW.selectionModel().setCurrentIndex(desired_index, QtCore.QItemSelectionModel.ClearAndSelect)




	def populate_version_from_open_scene(self, file_path):
		FileManagerLog.debug('# # # # # # # # # # # # # # # #')
		#... Mimic the behavior like a user manually clicking on an item in the UI
		
		FileManagerLog.debug('	This is file_path >>> {0}'.format(file_path))
		# Get the current Maya scene file path
		current_scene_path = pm.system.sceneName()
		
		# Check where is the scene is saved
		if current_scene_path:
			# Normalize the path
			current_scene_path = os.path.normpath(current_scene_path)

			# Split the path to extract relevant information
			path_elements = current_scene_path.split(os.path.sep)
			FileManagerLog.debug('	This is path_elements >>> {0}'.format(path_elements))
			
			# Extract the asset and department names
			asset_name = path_elements[-4]
			department_name = path_elements[-3]

			# Convert the desired directory path to a model index
			FileManagerLog.debug('	922 - This is file_path >>> {0}'.format(file_path))
			asset_index  = self.model.index(file_path)

			# Create a QItemSelection for the asset item
			selection = QtCore.QItemSelection(asset_index, asset_index)

			# Emit the clicked signal on the asset item
			self.asset_dir_TREEVIEW.clicked.emit(asset_index)
			FileManagerLog.debug('Click signal emitted')

			# Set the current selection in asset_dir_TREEVIEW
			self.asset_dir_TREEVIEW.selectionModel().select(selection, QtCore.QItemSelectionModel.ClearAndSelect)


			#... Add department here
			self.asset_department_listWidget.addItem(department_name)
			department_item = self.asset_department_listWidget.findItems(department_name, QtCore.Qt.MatchExactly)
			FileManagerLog.debug('	Make selected department item.')
			self.asset_department_listWidget.setCurrentItem(department_item[0])


			#... Populate version widget
			version_folder = os.path.join(file_path, department_name, STATIC_FOLDER[1])
			
			version_folder = os.path.normpath(version_folder)
			FileManagerLog.debug('	This is version_folder >>> {0}'.format(version_folder))
			self.show_version_entite(version_folder)


			#... Populate currenly selected file in asset_version_view_listWidget
			
			FileManagerLog.debug('	This is path_elements >>> {0}'.format(path_elements[-1]))
			asset_name = path_elements[-1]
			version_item = self.asset_version_view_listWidget.findItems(asset_name, QtCore.Qt.MatchExactly)
			FileManagerLog.debug('	This is version_item >>> {0}'.format(version_item))
			if version_item:
				self.asset_version_view_listWidget.setCurrentItem(version_item[0])


			#... Populate asset Info
			data_file = os.path.join(file_path, 'data.json')
			with open(data_file, "r") as file:
				json_data = json.load(file)
			self.assetInfo_list_listWidget.addItem(json_data['comment'])

			#... Populate thumbnail
			thumbnail_path = os.path.join(file_path, THUMBNAIL_NAME)
			self.display_images(thumbnail_path)

			#... Populate global
			#... Query to show asset at global widget
			global_commit_folder = os.path.join(file_path, STATIC_FOLDER[2], )
			#... If folder 'Commit' exist then continue
			if os.path.exists(global_commit_folder):
				self.load_global_commit(global_commit_folder)
			else:
				pass

			#... Populate local
			local_commit_folder = os.path.join(file_path, department_name, STATIC_FOLDER[2])

			# If folder 'Commit' exist then continue
			if os.path.exists(local_commit_folder):
				self.load_local_commit(local_commit_folder)
			else:
				pass






	def filter_proper_version_list(self):

	#... Make list to proper version workspace listWidget
	#... 1. cut off if naming is not having prior folder name
	#... 2. if file is not ma or mb

		# Get full path
		asset_path = self._get_full_path()
		department_text = self.asset_department_listWidget.currentItem().text()

		department_path = os.path.join(asset_path, department_text)
		department_path = os.path.normpath(department_path)
		job_step_list = os.path.join(department_path, STATIC_FOLDER[1])
		job_step_list = os.listdir(job_step_list)
		FileManagerLog.debug('This job_step_list: {0}'.format(job_step_list))

		# Extract entite name [-2]step for filter
		FileManagerLog.debug('THIS IS asset_path\t\t >>>\t\t: {0}'.format(asset_path))

		path_list = asset_path.split('\\')

		



		selected_project = self.project_comboBox.currentText()

		# I don't know how to manage this 
		# if selected_project == 'P_Regulus':
		if selected_project in USE_VARIATION:

			path_check = path_list[-2] + '_' + path_list[-1]
			pattern_esc = r'{0}.*\.(ma|mb)'.format(re.escape(path_check))
		else:
			path_check = path_list[-1]
			pattern_esc = r'{0}.*\.(ma|mb)'.format(re.escape(path_check))

			
		# Making list to find jobs step
		step_filter_list = []
		for each in job_step_list:
			# Filter for *.ma or *.mb and proper naming only
			# if re.search(r'\.ma$|\.mb$', each):
			if re.match(pattern_esc, each):

				step_filter_list.append(each)

		if step_filter_list:
			return step_filter_list
		else:
			FileManagerLog.debug('There are no proper naming to return')
			False




	def create_job_step(self):

		# shift to above
		# Open Dialog
		step_name, okPressed = QInputDialog.getText(self, "Create Step", "Enter Step name:")

		if okPressed and step_name:
			self.create_name_saving(step_name)



	def create_name_saving(self,step_name):
		
		# Get full path
		asset_path_text = self._get_full_path()
		department_text = self.asset_department_listWidget.currentItem().text()

		new_folder_path = os.path.join(asset_path_text, department_text)

		new_folder_path = os.path.normpath(new_folder_path)




		step_filter_list = self.filter_proper_version_list()
		FileManagerLog.debug('step_filter_list: {0}'.format(step_filter_list))

		result_job_element = self.find_step_and_version(step_filter_list)
		FileManagerLog.debug('THIS IS result_job_element: {0}'.format(result_job_element)) 



		selected_project = self.project_comboBox.currentText()

		split_path_list = new_folder_path.split('\\')
		# Project Regulus is use wired naming 
		# We can't use '01' or '02' variation name as a Asset name 
		# So add [Asset_name]_[Variation]_[Job] instead [Asset_name]_[Job]

		FileManagerLog.debug('I want this: {0}'.format(split_path_list))








		# if selected_project == 'P_Regulus':
		if selected_project in USE_VARIATION:
		
			asset_name = split_path_list[-3]
			variation_name = split_path_list[-2]
			job_name = split_path_list[-1]
			FileManagerLog.debug('Variation_asset_name: {0}\t variation_name: {1}\t job_name: {2}'.format(asset_name, variation_name, job_name))

			# Join the strings with an underscore
			final_file_name = asset_name + '_' + variation_name + '_' + job_name
			FileManagerLog.debug('final_file_name: {0}'.format(final_file_name))

		else:

			FileManagerLog.debug('There is not REGULUS using original naming')
			asset_name = split_path_list[-2]
			job_name = split_path_list[-1]
			final_file_name = asset_name + '_' + job_name
			line_number = sys._getframe().f_lineno
			FileManagerLog.debug('None_Variation_asset_name_{2}_: {0}\t{1}\t'.format(asset_name, job_name,line_number))

		FileManagerLog.debug('THIS IS >>>\t\t\tresult_job_element:\t\t\t {0}'.format(result_job_element))
		FileManagerLog.debug('THIS IS TYPE>>>\t\t\tresult_job_element:\t\t\t {0}'.format(type(result_job_element)))

		if result_job_element != False:
			step_list = result_job_element['step']
			if step_name in step_list:

				index = step_list.index(step_name)

				max_version = result_job_element['max_version'][index]
				max_version += 1
				max_version = str(max_version).zfill(PADDING)

				line_number = sys._getframe().f_lineno

				FileManagerLog.debug('({4})If having already step name: {0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT, line_number))

			else:
				max_version = str(1).zfill(PADDING)
				FileManagerLog.debug('If new file not found: {0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT))
		else:
			max_version = str(1).zfill(PADDING)
			FileManagerLog.debug('If new file not found: {0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT))		

		new_file_name =  '{0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT)



		save_full_path = os.path.normpath(os.path.join(asset_path_text, department_text, STATIC_FOLDER[1], new_file_name))

		save_path = os.path.normpath(os.path.join(asset_path_text, department_text, STATIC_FOLDER[1]))

		version_folder_path = os.path.normpath(os.path.join(asset_path_text, department_text, STATIC_FOLDER[1]))

		line_number = sys._getframe().f_lineno
		FileManagerLog.debug('({1})THIS IS save_full_path: {0}'.format(save_full_path,line_number))

		#... using saving version 
		self.maya_save_version(save_path, new_file_name, MAYA_EXT)
		# self.maya_save(save_path, new_file_name, MAYA_EXT)

		#... To refresh version viewport
		self.asset_version_view_listWidget.clear()
		#... Update version listWidget viewport
		self.show_version_entite(version_folder_path)

		FileManagerLog.debug('File saving at: {0}'.format(save_full_path)) 
		return True


	def maya_open(self, file_path):
		file_name = file_path.split('\\')[-1]

		#... find current maya file
		maya = General()
		current_scene_name = maya.get_scene_name()

		if mc.file(query = True, anyModified=True):
			reply = QMessageBox.question(			# Use self as the parent
													self ,
													'Save Chganges' ,
													'Current file has unsaved changes. Do you want to save? {0}'.format(current_scene_name) ,
													QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No
												)

			if reply == QMessageBox.Save:
				mc.file(save=True, type='mayaAscii')

			elif reply == QMessageBox.Cancel:
				return
		#... open maya file
		mc.file(file_path, o=True, f=True)
		# add recent file when open
		# self.addRecenfile( file_path )


	def maya_add_recen_file(self, filepath, MAYA_EXT):

		if MAYA_EXT == 'ma':
			maya_type = 'mayaAscii'
		elif MAYA_EXT == 'mb':
			maya_type = 'mayaBinary'


		import maya.mel as mel
		filepath = filepath.replace('\\','/')
		mel.eval('addRecentFile("{0}","{1}");'.format(filepath, maya_type))

	#... this method is for publish saving only
	#... change to return path for make it more dynamic
	def maya_save(self, save_path, save_name, MAYA_EXT, mode):
		logmsg = ''

		if MAYA_EXT == 'ma':
			maya_type = 'mayaAscii'
		elif MAYA_EXT == 'mb':
			maya_type = 'mayaBinary'

		if mode == 'global':
			print('This is global file.')
			#... get Specific name when publish
			if mc.objExists("rig_grp.enable") == True:
				if mc.getAttr("rig_grp.asset_name") != '':
					FileManagerLog.debug('asset_name no data skipped')

					if mc.getAttr("rig_grp.enable") == True:
						if mc.getAttr("rig_grp.asset_name") != None:
							save_name = mc.getAttr("rig_grp.asset_name")
							FileManagerLog.debug('\nSpecific naming found >>> {}'.format(save_name))
				else:
					pass
			else:
				FileManagerLog.debug('Not found naming specific. skipped')
			pass

		#... if having logmsg pass it to SVN
		if mc.objExists("rig_grp.logmsg") == True:
			if mc.getAttr("rig_grp.logmsg") != '':
				logmsg = mc.getAttr("rig_grp.logmsg")
				FileManagerLog.info('\nGet message.')
				#... clear message after publish
				mc.setAttr('rig_grp.logmsg', '', type='string')



		FileManagerLog.debug('save_path: {}\nsave_name: {}'.format(save_path, save_name))
		save_full_path = os.path.join(save_path, save_name)
		mc.file(rename=save_full_path)
		mc.file(save=True, force=True, type=maya_type)
		FileManagerLog.debug('FILE SAVE AT: {0}'.format(save_full_path)) 
		self.maya_add_recen_file(save_full_path, MAYA_EXT)
		return save_full_path, logmsg


	#... this method is for saving for version only
	def maya_save_version(self, save_path, save_name, MAYA_EXT):

		if MAYA_EXT == 'ma':
			maya_type = 'mayaAscii'
		elif MAYA_EXT == 'mb':
			maya_type = 'mayaBinary'

		FileManagerLog.debug('save_path: {}\nsave_name: {}'.format(save_path,save_name))
		save_full_path = os.path.join(save_path, save_name)
		mc.file(rename=save_full_path)
		mc.file(save=True, force=True, type=maya_type)
		FileManagerLog.debug('FILE SAVE AT: {0}'.format(save_full_path)) 
		self.maya_add_recen_file(save_full_path, MAYA_EXT)
		return True

	def maya_reference_noAsk(self, file_path):
		folder, file_name = os.path.split(file_path)
		file_name, file_ext = os.path.splitext(file_name)
		mc.file(file_path, reference=True, namespace=file_name)



	def maya_reference(self, file_path):
		folder, file_name = os.path.split(file_path)
		file_name, file_ext = os.path.splitext(file_name)
		reply = QMessageBox.question(
														self ,
														'Confirm' ,
														'Do you want to reference {0} ?'.format(file_name)   ,
														QMessageBox.Yes | QMessageBox.No, QMessageBox.No
													)
		if reply == QMessageBox.Yes:
			mc.file(file_path, reference=True, namespace=file_name)





	# Context menu for asset_department_listWidget
	def show_job_context_menu(self, position):
		# Create Jobs
		contextMenu = QtWidgets.QMenu(self)
		createJobs_action = QtWidgets.QAction("Create Jobs", self)
		# Link to method
		createJobs_action.triggered.connect(self.create_jobs)
		contextMenu.addAction(createJobs_action)

		# Add show in Explorer
		showInExplorer_action = QtWidgets.QAction("Show in Explorer", self)
		# Link to method
		showInExplorer_action.triggered.connect(self.show_job_explorer)
		contextMenu.addAction(showInExplorer_action)

		# Disconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_department_listWidget.customContextMenuRequested.disconnect(self.show_job_context_menu)

		contextMenu.exec_(self.asset_department_listWidget.mapToGlobal(position))

		# Reconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_department_listWidget.customContextMenuRequested.connect(self.show_job_context_menu)



	def show_job_explorer(self):# Change policy to open folder directly instead open 'Version' folder

		asset_path_text = self._get_full_path()
		new_department_text = self.asset_department_listWidget.currentItem().text()
		new_folder_path = os.path.join(asset_path_text, new_department_text)
		# new_folder_path = os.path.join(asset_path_text, new_department_text, STATIC_FOLDER[1])

		# if not os.path.exists(new_folder_path):
		# 	new_folder_path = os.path.join(asset_path_text, new_department_text)

		self._open_folder_path(new_folder_path)






	def _open_folder_path(self, input_path):
		# Check path is exists
		if not os.path.exists(input_path):
			FileManagerLog.debug('{0} is not exists'.format(input_path))
			return
		else:
			if sys.platform == "win32": # Windows
				subprocess.Popen(f'explorer "{input_path}"')
			elif sys.platform == "darwin": # macOS
				subprocess.Popen(["open", input_path])
			else: # Linux 
				subprocess.Popen(["xdg-open", input_path])	



					

	# Create jobs for department
	def create_jobs(self):
		jobs_name, okPressed = QInputDialog.getText(self, "Create Jobs", "Enter folder name:")
		if okPressed and jobs_name:
			# Create the folder at the department level
			# new_department_text = self.asset_department_listWidget.currentItem().text()
			asset_path = self._get_full_path()
			new_folder_path = os.path.join(asset_path, jobs_name)
			new_folder_path = self.handle_selected_path(new_folder_path)

			if not os.path.exists(new_folder_path):
				self.asset_department_listWidget.clear()

				# Create new folder
				# os.makedirs(new_folder_path)

				for job_type in JOB_TEMPLATE:
					job_each_path = os.path.join(new_folder_path, job_type)
					os.makedirs(job_each_path, exist_ok=True)



				FileManagerLog.debug('This is department_name -113- {0}'.format(new_folder_path))
				# Code to create the folder using the folderPath

				
				# Populate the list widget with the latest folders or items
				items = os.listdir(asset_path)


				# Exclude unwanted item
				items_excluded = [dept for dept in items if dept not in EXCLUDE_VIEW_ITEM ]
				FileManagerLog.debug('This is department_name -125- {0}'.format(items_excluded))
				self.asset_department_listWidget.addItems(items_excluded)

			else:
				FileManagerLog.warning('Cannot create a file when that file already exists.')
			
			


	
	def display_images(self, image_paths):
		if image_paths is not None:
			FileManagerLog.debug(image_paths)
			self.asset_thumbnail_IMAGE_LABEL.setScaledContents(True)
			pixmap = QPixmap(image_paths)
			# self.asset_thumbnail_IMAGE_LABEL.setPixmap(pixmap)
			self.asset_thumbnail_IMAGE_LABEL.setPixmap(pixmap.scaled(self.asset_thumbnail_IMAGE_LABEL.size(), aspectRatioMode=Qt.KeepAspectRatio))
			self.asset_thumbnail_IMAGE_LABEL.repaint()
			QApplication.processEvents()
		else:
			FileManagerLog.debug('There are nothing to show.')
			# Clear thumbnail afer click at another folder
			self.asset_thumbnail_IMAGE_LABEL.clear()





	def populate_drives(self):
		self.drive_comboBox.clear()
		self.drive_comboBox.addItems(DRIVES)


	def populate_project(self):
		self.project_comboBox.clear()
		self.project_comboBox.addItems(PROJECT_NAME)

	#... initialization when open file manager
	def update_project_comboBox(self):

		selected_drive = self.drive_comboBox.currentText()
		selected_project = self.project_comboBox.currentText()

		FileManagerLog.info("\nThis is Run When start")
		#... Set selected drive and project as root path
		try:
			self.path = os.path.join(selected_drive, BASE_FOLDER, DEFAULT_PROJECT, ASSET_TOP_FOLDER)
		except FileNotFoundError:
			FileManagerLog.error("Invalid project name!")
			self.path = os.path.join(selected_drive, BASE_FOLDER, PROJECT_NAME[0], ASSET_TOP_FOLDER)

		FileManagerLog.info("Show project path:...\t\t\t", self.path)

		#... Update the selected project variable with the current selection
		selected_project = self.project_comboBox.currentText()
		print("Show project name _1744_:...\t\t\t", selected_project)


		if selected_project == None:
			print('There are no Project name')
		print("Show selected_Project:...\t\t\t", selected_project)	

		# Populate Project comboBox
		self.project_comboBox.clear()
		self.project_comboBox.addItems(PROJECT_NAME)

		# Set the selected project in the Project comboBox
		self.project_comboBox.setCurrentText(selected_project)



	def show_version_entite(self, version_folder):
		# Clear the QListWidget
		self.asset_version_view_listWidget.clear()
		# self.asset_local_view_listWidget.clear()

		### will shift to method #####
		# Check if exists
		if os.path.exists(version_folder):
			# Corrective back and forward slash together
			version_folder = os.path.normpath(version_folder)
			FileManagerLog.debug("Version_folder path: {0}".format(version_folder) )



			#... If the selection is a directory
			if not os.path.isfile(version_folder):
				#... Get the list of files in the directory
				version_file_list = os.listdir(version_folder)			
				# self.asset_version_view_listWidget.addItems(version_file_list)
				print("Hide file extension ['*.pyc', '*.o', '*.png', '.mayaSwatches'] for me please")


				#... Filter out files that match any patterns in HIDE_FORMAT
				filtered_file_list = [
				file_name for file_name in version_file_list
				if not any(fnmatch.fnmatch(file_name, pattern) for pattern in HIDE_FORMAT)
				]

				#... Add the filtered files to the QListWidget
				self.asset_version_view_listWidget.addItems(filtered_file_list)



		else:
			FileManagerLog.info('The folder Version does not exists.')
			pass

	
	#... Try to make return directory when clicked in treeview
	def on_treeview_clicked(self, index):
		#... refresh everytime that click at treeview
		self.asset_local_view_listWidget.clear()
		self.asset_global_listWidget.clear()
		self.asset_department_listWidget.clear()
		self.asset_version_view_listWidget.clear()
		self.assetInfo_list_listWidget.clear()


		# Get the file name and path from the model
		file_path = self.model.filePath(index)
		FileManagerLog.debug('This is file path {0}'.format(file_path))




		#  Checks if the item is a file or not.
		if os.path.isfile(file_path):
			FileManagerLog.debug('This is file for sure')

			return
		else:
			FileManagerLog.debug('This is folder for sure')
			data_file = os.path.join(file_path, 'data.json')
			self.display_images(None)

			# Check if having 'data.json' mean is asset folder for sure
			if os.path.exists(data_file):
				FileManagerLog.debug('That is "ASSET" we looking for.')
				self.load_asset_departments(file_path)

				
				# If folder 'Commit' exist then continue
				global_commit_folder = os.path.join(file_path, STATIC_FOLDER[2])

				if os.path.exists(global_commit_folder):
					self.load_global_commit(global_commit_folder)

				# Show thumbnail
				thumbnail_path = os.path.join(file_path, THUMBNAIL_NAME)
				self.display_images(thumbnail_path)

				# Do not expand the asset folder if already expanded(Still... not work)
				if self.asset_dir_TREEVIEW.isExpanded(index):
					self.asset_dir_TREEVIEW.setExpanded(index, False)
					FileManagerLog.debug('Please do not expanded.')

				#... show data json file to widget
				with open(data_file, "r") as file:
					json_data = json.load(file)

				self.assetInfo_list_listWidget.addItem(json_data['comment'])


			#... Fail for now
			# #... Make filter Start
			# filter_text = self.asset_filter_lineEdit.text()

			# proxy_model = QSortFilterProxyModel()
			# proxy_model.setSourceModel(self.model)

			# proxy_model.setFilterRegExp(filter_text)
			# proxy_model.setFilterKeyColumn(0)

			# #... Set the proxy model on the asset_dir_TREEVIEW
			# self.asset_dir_TREEVIEW.setModel(proxy_model)


			# #... Set the root index to show the filtered results
			# root_index = self.asset_dir_TREEVIEW.model().index(QDir.currentPath())
			# self.asset_dir_TREEVIEW.setRootIndex(root_index)

			# #... Make filter End

				


	def on_treeview_SCENE_clicked(self, index):
		file_path = self.model.filePath(index)
		FileManagerLog.debug('This is scene file path {0}'.format(file_path))			





	def on_department_clicked(self, item):

		# Clear viewport
		self.asset_local_view_listWidget.clear()
		self.asset_global_listWidget.clear()

		# Get selected department
		selected_item = self.asset_department_listWidget.currentItem()
		# Return departments name
		department_text = selected_item.text()
		FileManagerLog.debug("Return departments name: {0}".format(department_text) )

		# Get root path
		asset_path = self._get_full_path()
		# self.handle_selected_path(asset_path)

		version_folder = os.path.join(asset_path, department_text, 'Version')


		#... Query to show asset at global widget
		global_commit_folder = os.path.join(asset_path, STATIC_FOLDER[2], )
		#... If folder 'Commit' exist then continue
		if os.path.exists(global_commit_folder):
			self.load_global_commit(global_commit_folder)
		else:
			pass


		### will shift to method #####
		self.show_version_entite(version_folder)

		local_commit_folder = os.path.join(asset_path, department_text, STATIC_FOLDER[2])

		# If folder 'Commit' exist then continue
		if os.path.exists(local_commit_folder):
			self.load_local_commit(local_commit_folder)
		else:
			pass



	def on_version_clicked(self):
		# Get root path
		asset_path = self._get_full_path()
		# self.handle_selected_path(asset_path)

		
		# Get selected department
		selected_item = self.asset_department_listWidget.currentItem()

		if selected_item:# If select via department widget
			# Return departments name
			department_text = selected_item.text()
			FileManagerLog.debug("Return asset_department_listWidget name: {0}".format(department_text) )

			# Get current selected in Version listWidget
			selected_task = self.asset_version_view_listWidget.currentItem()
			selected_task_text = selected_task.text()
			FileManagerLog.debug("Return asset_version_view_listWidget name: {0}".format(selected_task_text) )

			current_version_clicked = os.path.join(asset_path, department_text, STATIC_FOLDER[1], selected_task_text)
			current_version_clicked = self.handle_selected_path(current_version_clicked)

			# Do something with the selected path
			FileManagerLog.debug("Do something with the selected path_438_: {0}".format(current_version_clicked) )
			current_version_clicked = os.path.normpath(current_version_clicked)
			split_path_list = current_version_clicked.split('\\')
			FileManagerLog.debug("Split path_441_: {0}".format(split_path_list) )
			version_element = split_path_list[-1]
			version_element_list = version_element.split('.')
			extension = version_element_list[-1] 
			version_number = version_element_list[-2]
			element_name = version_element_list[-3]

			# Split
			element_name_list = element_name.split('_')

			FileManagerLog.debug("Split EXTENSION: {0}".format(extension) )
			FileManagerLog.debug("Split version_number: {0}".format(version_number) )
			FileManagerLog.debug("Split element_name: {0}".format(element_name) )
			FileManagerLog.debug("Step name: {0}".format(element_name_list[-1]) )

		else:# If select via treeview 
			FileManagerLog.debug(": {0}".format('That maybe selected via treeView') )
			FileManagerLog.debug('This is file path {0}'.format(asset_path))

			selected_task = self.asset_version_view_listWidget.currentItem()
			selected_task_text = selected_task.text()

			current_version_clicked = os.path.join(asset_path, 'Version', selected_task_text)
			current_version_clicked = self.handle_selected_path(current_version_clicked)



	def load_local_commit(self, folder_path):
		local_commit_list = []

		# Clear the list widget
		self.asset_local_view_listWidget.clear()	

		# Get the list of files and directories in the specified path
		items = os.listdir(folder_path)
		for each in items:
			local_commit_list.append(each)
		self.asset_local_view_listWidget.addItems(local_commit_list)
		FileManagerLog.debug("Found Local Commit: {0}".format(local_commit_list) )



	def load_global_commit(self, folder_path):
		global_commit_list = []

		# Clear the list widget
		self.asset_global_listWidget.clear()

		# Get the list of files and directories in the specified path
		items = os.listdir(folder_path)

		for each in items:
			global_commit_list.append(each)
		self.asset_global_listWidget.addItems(global_commit_list)
		FileManagerLog.debug("Found Global Commit: {0}".format(global_commit_list) )



	def _get_full_path(self):
		# Construct the full path based on the selected text on treeview
		current_index = self.asset_dir_TREEVIEW.currentIndex()
		full_path = self.model.filePath(current_index)
		full_path = os.path.normpath(full_path)
		FileManagerLog.debug("Return full path: {0}".format(full_path) )
		return full_path

	def _get_full_path_pm(self):
		#... Construct the full path no care treeview is selected
		current_scene_path = pm.system.sceneName()
		full_path = os.path.normpath(current_scene_path)
		return full_path

	def get_deep_path(self):
		# Return full path to work file and extension		
		current_index = self.asset_dir_TREEVIEW.currentIndex()
		full_path = self.model.filePath(current_index)
		department_text = self.asset_department_listWidget.currentItem().text()

		# Get current selected in Version listWidget
		selected_name = self.asset_version_view_listWidget.currentItem()
		selected_task_text = selected_name.text()

		current_version_clicked = os.path.join(full_path, department_text, STATIC_FOLDER[1], selected_task_text)
		current_version_clicked = os.path.normpath(current_version_clicked)

		FileManagerLog.debug("Return current_version_clicked name: {0}".format(current_version_clicked) )

		return current_version_clicked


	def get_deep_path_local_commit(self):
		full_department_path = self._get_department_path()

		local_commit = self.asset_local_view_listWidget.currentItem()
		local_commit_text = local_commit.text()

		current_clicked = os.path.join(full_department_path, STATIC_FOLDER[2], local_commit_text)
		current_clicked = os.path.normpath(current_clicked)

		FileManagerLog.debug("Return current_clicked name: {0}".format(current_clicked) )
		return current_clicked


	def _get_department_path(self):
		full_path = self._get_full_path()
		department_text = self.asset_department_listWidget.currentItem().text()
		full_department_path = os.path.join(full_path, department_text)
		return full_department_path



	def handle_selected_path(self, path):# Do something with the selected path
		norm_path = os.path.normpath(path)
		FileManagerLog.info("\nNormalize path: {0}".format(norm_path) )
		return norm_path
		

	def load_asset_departments(self, folder_path):
		# Clear the list widget
		self.asset_department_listWidget.clear()


		# Look for the data.json file in the folder
		data_file = os.path.join(folder_path, 'data.json')

	

		'''
		# Choice 1: read department name from dict
		if os.path.isfile(data_file):
			with open(data_file, 'r') as f:
				data = json.load(f)
				if 'department_name' in data:
					# Add the departments to the list widget
					departments = data['department_name']
					FileManagerLog.info('\n146')
					self.asset_department_listWidget.addItems(departments)
		'''

		# Choice 2: read folder list in dir
		if os.path.isfile(data_file):
			departments = []
			items = os.listdir(folder_path)
			FileManagerLog.debug('this is item {0}'.format(items))
			# Exclude unwanted item
			items_excluded = [dept for dept in items if dept not in EXCLUDE_VIEW_ITEM ]
			self.asset_department_listWidget.addItems(items_excluded)



	def populate_ASSET_treeView(self):


		print('\tChange project name')
		#...initializing model and populate the tree view
		self.model = QtWidgets.QFileSystemModel()
		self.model.setRootPath(self.path)
		self.asset_dir_TREEVIEW.setModel(self.model)

		self.asset_filter_lineEdit.setPlaceholderText('Search...')
		self.asset_filter_lineEdit.textChanged.connect(self.filter_model)


		#... Update the `self.path` variable with the selected project path
		self.path = os.path.join(self.drive_comboBox.currentText(), BASE_FOLDER, self.project_comboBox.currentText(), ASSET_TOP_FOLDER)

		self.check_exists_maya()

		# self.update_project_name()



		#.... Hide some file formats, such as ".pyc" and ".o" files from tree view
		self.model.setNameFilters(HIDE_FORMAT)
		self.model.setNameFilterDisables(False)
		print(f"Hide file extension {HIDE_FORMAT} for me please")


		# Set the model on the tree view
		self.asset_dir_TREEVIEW.setModel(self.model)
		self.asset_dir_TREEVIEW.setRootIndex(self.model.index(self.path))
		print("Model root path:...\t\t\t", self.model.rootPath())




		# Sort the items alphabetically from A to Z and allow sorting in both directions
		self.asset_dir_TREEVIEW.setSortingEnabled(True)
		self.asset_dir_TREEVIEW.sortByColumn(0, QtCore.Qt.AscendingOrder)
		self.asset_dir_TREEVIEW.header().setSortIndicator(0, QtCore.Qt.AscendingOrder)
		self.asset_dir_TREEVIEW.header().setSortIndicatorShown(True)



		# Hide the second, third and fourth columns
		self.asset_dir_TREEVIEW.setColumnHidden(1, True) # size
		self.asset_dir_TREEVIEW.setColumnHidden(2, True) # type
		self.asset_dir_TREEVIEW.setColumnHidden(3, True) # date modified


		# Set up context menu
		# self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) #... repetitive code with __init__
		# self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu) #... repetitive code with __init__

		# Print some information for debugging purposes

		FileManagerLog.info("Populating tree view with file system model...")
		FileManagerLog.info("populate Asset project path:...\t\t\t{0}".format(self.path))
		FileManagerLog.info("Model root path:...\t\t\t{0}".format(self.model.rootPath()	))

		# Show department listWidget when selected asset
		# self.asset_department_listWidget.addItems(['Model', 'Rig', 'ConceptArt', 'Texture', 'VFX', 'Anim'])
		# print("\nShow department...")
	


	def populate_SCENE_treeView(self):

		# # initializing model and populate the tree view
		self.model = QtWidgets.QFileSystemModel()
		self.model.setRootPath(self.path)
		self.dir_scene_TREEVIEW.setModel(self.model)

		# GPT comment update the self.path variable and call model.setRootPath() before updating the tree view 
		# Update the `self.path` variable whenever the user selects a new project
		self.path = os.path.join(self.drive_comboBox.currentText(), BASE_FOLDER, self.project_comboBox.currentText(), SCENE_TOP_FOLDER)

		self.check_exists_maya()


		# Hide some file formats, such as ".pyc" and ".o" files
		self.model.setNameFilters(HIDE_FORMAT)
		self.model.setNameFilterDisables(False)

		# Set the model on the tree view
		self.dir_scene_TREEVIEW.setModel(self.model)
		self.dir_scene_TREEVIEW.setRootIndex(self.model.index(self.path))
		print("Model root path:...\t\t\t", self.model.rootPath())

		# Sort the items alphabetically from A to Z and allow sorting in both directions
		self.dir_scene_TREEVIEW.setSortingEnabled(True)
		self.dir_scene_TREEVIEW.sortByColumn(0, QtCore.Qt.AscendingOrder)
		self.dir_scene_TREEVIEW.header().setSortIndicator(0, QtCore.Qt.AscendingOrder)
		self.dir_scene_TREEVIEW.header().setSortIndicatorShown(True)

		#... Hide the second, third and fourth columns
		self.dir_scene_TREEVIEW.setColumnHidden(1, True) # size
		self.dir_scene_TREEVIEW.setColumnHidden(2, True) # type
		# self.dir_scene_TREEVIEW.setColumnHidden(3, True) # date modified


		#... Set up context menu
		# self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) #... repetitive code with __init__
		# self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu) #... repetitive code with __init__

		#... Print some information for debugging purposes

		FileManagerLog.info("Populating tree view with file system model...")
		FileManagerLog.info("populate_treeView project path:...\t\t\t{0}".format(self.path))
		FileManagerLog.info("Model root path:...\t\t\t{0}".format(self.model.rootPath()	))

		# Show department listWidget when selected asset
		# self.asset_department_listWidget.addItems(['Model', 'Rig', 'ConceptArt', 'Texture', 'VFX', 'Anim'])
		# print("\nShow department...")





	def show_context_menu(self, point):
		# Disconnect the asset_dir_TREEVIEW signal
		self.asset_dir_TREEVIEW.clicked.disconnect(self.on_treeview_clicked)

		# Get the index of the item that was clicked
		index = self.asset_dir_TREEVIEW.indexAt(point)

		# Create a context menu
		menu = QtWidgets.QMenu(self)

		# Add a "Create entite" action to the menu
		new_entitie_action = menu.addAction("Create Entite...")

		 # Add a "Create asset" action to the menu
		new_asset_action = menu.addAction("Create Asset...")

		# Add a "Show in explorer" action to the menu
		show_in_explorer_action = menu.addAction("Show in Explorer")

		# Check if the context menu is already open
		if menu.isVisible():
			# Close the context menu
			menu.close()

		# Show the context menu and get the chosen action
		chosen_action = menu.exec_(self.asset_dir_TREEVIEW.mapToGlobal(point)) 


		
		# If "New entite" was chosen, create a new entite
		if chosen_action == new_entitie_action:
			self.create_entite(index)

		# If "New asset" was chosen, create a new asset
		if chosen_action == new_asset_action:
			self.create_asset(index)

		# If "Show in explorer" was chosen, open the folder in the file explorer
		if chosen_action == show_in_explorer_action:
			# Get the filepath of the selected item
			filepath = self.asset_dir_TREEVIEW.model().filePath(index)

			# Open the folder in the file explorer
			if os.path.isdir(filepath):
				os.startfile(filepath)

		# Reconnect the asset_dir_TREEVIEW signal after the chosen action is handled
		self.asset_dir_TREEVIEW.clicked.connect(self.on_treeview_clicked)


	def create_entite(self, index):
		# Get the filepath of the selected item
		parent_dir = self.asset_dir_TREEVIEW.model().filePath(index)
		print("Parent_dir:", parent_dir)

		# Get the parent directory of the new entite
		# parent_dir = self.asset_dir_TREEVIEW.model().filepath(index)

		# Prompt the user to enter a entite name
		entitie_name, ok = QtWidgets.QInputDialog.getText(self, "New Entite", "Enter folder name:")

		# If the user entered a name, create the folder
		if ok and entitie_name:
			# Create full path to new folder
			new_folder_path = os.path.join(parent_dir, entitie_name)

			# Create new folder
			os.makedirs(new_folder_path)

			# Refresh the view to show the new folder
			self.asset_dir_TREEVIEW.update()


	def get_full_entity_name(self, base_path):

		# base_path = os.path.normpath(base_path)

		directories = base_path.split("/")

		# find suffix
		content_index = directories.index(ASSET_TOP_FOLDER)

		for i in range (0,content_index+1):
			del directories[0]
		 
		directories.pop()

		# Join the directories back together to form a path.
		edited_path = "/".join(directories)

		edited_path = os.path.join("/", edited_path)
		print(edited_path)
		return edited_path

	def get_department_name(self, new_asset_path):

		folders_list = os.listdir(new_asset_path)

		for folder in folders_list:

			if folder == 'data.json':

				folder.remove(folders_list)

		return folders_list




	def create_data_JSON(self, base_path, entitie_type, entitie_name, full_entity_name, department_name, comment, add_path_SVN ):
		# Write to dictionary
		entitie_dict = DICTIONARY_TEMPLATE
		entitie_dict["base_path"] = base_path
		entitie_dict["entitie_type"] = entitie_type
		entitie_dict["entitie_name"] = entitie_name
		entitie_dict["full_entity_name"] = full_entity_name
		entitie_dict["department_name"] = department_name
		entitie_dict["comment"] = comment
		entitie_dict["add_path_SVN"] = add_path_SVN

		return entitie_dict


	def write_entite_folder(self, dictionary):

		with open("{0}/data.json".format(dictionary["base_path"]), "w") as f:
			json.dump(dictionary, f, indent=2)

		print('\n### Write file complete ###')
		return True


	def create_asset(self, index):
		# Get the parent directory of the new asset
		parent_dir = self.asset_dir_TREEVIEW.model().filePath(index)

		# Prompt the user to enter an asset name
		asset_name, ok = QtWidgets.QInputDialog.getText(self, "Create Asset", "Enter asset name:")

		# If the user entered a name, create the asset folders
		if ok and asset_name:

			# Create full path to new asset folder
			new_asset_path = os.path.join(parent_dir, asset_name)

			# If asset exists
			if not os.path.exists(new_asset_path):
				FileManagerLog.debug("\tThere are no folder in here Continue.")

				# Normalize path
				new_asset_path = os.path.normpath(new_asset_path)
				new_asset_path = new_asset_path.replace('\\', '/')

				# Create asset folders
				# Iterate over jobs and create the directories
				for job in DEPT_NAME:
					job_path = os.path.join(new_asset_path, job)
					os.makedirs(job_path, exist_ok = True)
					for job_type in JOB_TEMPLATE:
						job_each_path = os.path.join(job_path, job_type)
						os.makedirs(job_each_path, exist_ok=True)

				if DEPT_EMPTY:
					for job in DEPT_EMPTY:
						job_path = os.path.join(new_asset_path, job)
						os.makedirs(job_path, exist_ok = True)

				# Store entity data to json file here
				# new_asset_path 
				FileManagerLog.debug("\tThis is asset path:\t{0}".format(new_asset_path))

				# 'Asset' or 'Scene'
				FileManagerLog.debug("\tType:\t{0}".format('Asset-718-'))

				# Asset_name 
				FileManagerLog.debug("\tAsset name:\t{0}".format(asset_name))
				
				# "fullEntityName"
				fullEntityName = self.get_full_entity_name(new_asset_path)
				# comment (not require)

				# extension(not use)

				# Get department name
				department_name = self.get_department_name(new_asset_path)
				FileManagerLog.info('This is department_name:\t\t{0}')



				# Write Add path for SVN
				add_path_for_SVN = []

				# Add root Asset folder
				add_path_for_SVN.append(os.path.normpath(new_asset_path)) 

				# Add 'Commit' Asset folder
				folder_global_path = os.path.normpath(os.path.join(new_asset_path, STATIC_FOLDER[2]))
				add_path_for_SVN.append(folder_global_path)

				
				for each in department_name:
					if each in DEPT_EMPTY:
						continue
					else:
						folder_version_path = os.path.normpath(os.path.join(new_asset_path, each, STATIC_FOLDER[1]))
						folder_commit_path = os.path.normpath(os.path.join(new_asset_path, each, STATIC_FOLDER[2]))
						add_path_for_SVN.append(folder_version_path)
						add_path_for_SVN.append(folder_commit_path)



			
				# Write to json file
				entite_dict = self.create_data_JSON(new_asset_path, 'Asset', asset_name, fullEntityName, department_name,"", add_path_for_SVN)
				FileManagerLog.debug(entite_dict)
				self.write_entite_folder(entite_dict)

				reply = QMessageBox(self)
				reply.setWindowTitle('Commit Changes')
				reply.setText('Do you want to commit thumbnail to SVN ?\n\t')

				commit_button = reply.addButton('Add', QMessageBox.AcceptRole)
				save_button = reply.addButton('Just Create', QMessageBox.AcceptRole)
				reply.addButton(QMessageBox.Cancel)	

				result = reply.exec_()	
				if reply.clickedButton() == commit_button:

					FileManagerLog.debug("\tThis is File path:\t{0}".format(add_path_for_SVN[0]))

					#... Add SVN
					self.svn_maya.execute_cmd('add', file_path = add_path_for_SVN[0], close_on_end=0, add_fixed_folder = True)

					#...Commit SVN
					# self.svn_maya.execute_cmd('commit', file_path = add_path_for_SVN[0], close_on_end=0, logmsg='')

				elif reply.clickedButton() == save_button:
					FileManagerLog.debug("\tJust Create Do nothing.")
					pass




				




			else:
				print("\tThere are already folder skipped.")
				pass

				# Refresh the view to show the new asset folders
				self.asset_dir_TREEVIEW.update()



class General():
	def __init__(self):
		pass

	def get_scene_name(self):
		scene_path = pm.system.sceneName()
		if scene_path:
			# Get the file name with extension
			self.Scene_Name = os.path.basename(scene_path)
		else:
			self.Scene_Name = None
			
		return self.Scene_Name  # Return the scene name

	def get_workspace(self):
		self.WorkSpace_RootDir = pm.workspace(q=1,rd=1)
		FileManagerLog.debug('self.WorkSpace_RootDir:\t%s',self.WorkSpace_RootDir)
		# self.RuleEntry_SourceImages = pm.workspace('sourceImages',fileRuleEntry=1,q=1 )
		# FileManagerLog.debug('self.RuleEntry_SourceImages:\t%s',self.RuleEntry_SourceImages)
		# self.RuleEntry_3dPaintTextures = pm.workspace('3dPaintTextures',fileRuleEntry=1,q=1 )
		# self.RuleEntry_Scenes = pm.workspace('scene',fileRuleEntry=1,q=1 )
		# FileManagerLog.debug('self.RuleEntry_Scenes:\t%s',self.RuleEntry_Scenes)

	def log_list(self,inputList):
		if inputList :
			s = ''
			if inputList :
				try :
					s += str(inputList)
				except :
					FileManagerLog.warning('can not convert inputList to string')
				for i in inputList :
					s += '\t' + str(i)
			FileManagerLog.debug(s)
		else:
			FileManagerLog.debug('log_list:input is None')


	def get_texture_file(self):
		self.Texture_Files = set()
		# Get texture file
		texturesList = cmds.ls(textures=True)
		if texturesList :
			for tex in texturesList:
				if cmds.attributeQuery( 'fileTextureName',node=tex,exists=1 ):
					texFile = cmds.getAttr( (tex+'.fileTextureName') )
					print ('texFile:',texFile)
					self.Texture_Files.add(texFile)
		self.log_list( self.Texture_Files )

	def get_reference_file(self):
		# check scene name is not set or not
		if pm.system.sceneName():
			# Get reference file
			self.Reference_File = set( cmds.file(q=True,l=True) )
			self.log_list( self.Reference_File )        
		
	
	def convert_to_relative(self,parten,inputStr):
		'''
		example: convertToRelative('sourceimages','C:/AW/Maya5.0/sourceimages/maya.exe')
		result: 'sourceimages/maya.exe'
		'''
		#p = re.compile('^.*/sourceimages')
		inputStr = inputStr.replace('\\','/')
		returnStr = re.sub( ('^.*/' + parten), parten, inputStr )
		print (inputStr,'\t',returnStr)
		return returnStr

#... SVN Part

class SvnMaya:
	def __init__(self):
		pass
	def execute_cmd(self, cmd_type, file_path, close_on_end, add_fixed_folder = False, logmsg = ''):

		file_path = os.path.normpath(file_path)
		# Create a variable to store the command line
		# command_line = r'cd "{0}" && TortoiseProc.exe /command:{1} /path:"{2}" /logmsg:"{3}" /closeonend:{4}'.format(SVN_BIN_PATH, cmd_type, file_path, log_message, close_on_end)
		if add_fixed_folder == False:
			# command_line = r'cd "{0}" && TortoiseProc.exe /command:{1} /path:"{2}" /closeonend:{3}'.format(SVN_BIN_PATH, cmd_type, file_path, close_on_end)
			command_line = r'cd "{0}" && TortoiseProc.exe /command:{1} /path:"{2}" /logmsg:"{4}" /closeonend:{3}'.format(SVN_BIN_PATH, cmd_type, file_path, close_on_end, logmsg )
		else:
			FileManagerLog.debug('Specific "Add" folder.')
			command_line = r'cd "{0}" && TortoiseProc.exe /command:{1} /path:"{2}" /closeonend:{3} --depth=files /nodlg'.format(SVN_BIN_PATH, cmd_type, file_path, close_on_end, logmsg)

		# Execute the command line
		subprocess.run(command_line, shell=True)







def createThumbnail(width=256, height=256, currentPath='', fileName = 'thumb'):
	
	#... Create Thumbnail at current maya file
	imageFile = '{0}{1}.{2}'.format(currentPath, fileName, 'jpg')

	pngImageFile = '{0}{1}.{2}'.format(currentPath, fileName, 'png')
	
	mimage = om.MImage()
	view = omui.M3dView.active3dView()
	view.readColorBuffer(mimage, True)

	#... Resize the image to the specified width and height
	mimage.resize(width, height)

	mimage.writeToFile(imageFile)

	#... Convert the file to PNG
	os.rename(imageFile, pngImageFile)

	print('Thumbnail has been created at: {0}'.format(imageFile))




def do_pipeline_round_skinWeight(group_names = ['Export_grp', 'Model_grp']):
	if mc.objExists("rig_grp.round_skinweight") == True and mc.getAttr("rig_grp.round_skinweight") == True:
		mesh = fileTools.find_mesh_in_grp(group_names=group_names)
		for each in mesh:
			rsw.roundSkinWeight(digit=3, selection=each)
			FileManagerLog.info('Pipeline do roundSkinWeight Done...\n')
	else:
		pass









def do_local_commit():
	ngSkin = mc.ls('ngSkinToolsData_*')
	if ngSkin:
		import ngSkinTools2
		# remove all ngSkinTools custom nodes in a scene
		ngSkinTools2.operations.removeLayerData.remove_custom_nodes()
		FileManagerLog.info('Delete ngSkinTools2...\n')
	else:
		FileManagerLog.info('There are no ngSkinTools skipped...\n')

	#... Remove unused ref
	fileTools.remUnRef() 

	#... Import ref
	fileTools.impRem()

	#... Delete layer
	fileTools.deleteDisplayLayer()

	#... Add new method for re-organize group struture when publish
	fileTools.doMoveGrp()

	#... Move node to target
	fileTools.doDeleteGrp()	

	#... delete '*_bak'
	FileManagerLog.debug('Do Delete prefix.')
	#... Add delete suffix and prefix 
	fileTools.doDeleteSuffixExt(suffix ='_X')
	fileTools.doDeletePrefixExt(prefix = 'X_')


	# Hide Root
	# fileTools.doHideGrp( 'Root',0 )
	# fileTools.doHideGrp( 'root',0 )

	#... count joint
	fileTools.countJnt()

	#... Hold for now cause invalid
	# fileTools.delete_unused_skin_suffix()

	# fileTools.delete_unused_material() 

	# fileTools.doDeleteMisc(name = 'BaseAnimation')
	#... clear anim layer
	fileTools.delete_anim_layer()

	mc.select(deselect = True)


def do_global_commit():
	#... Assign previous name to rig_grp
	fileTools.assign_pre_job_step()

	#... Remove unused ref
	fileTools.remUnRef()

	#... Import ref
	fileTools.impRem()

	#... Hide Root
	fileTools.doHideGrp( 'Root',0 )
	fileTools.doHideGrp( 'root',0 )
	fileTools.doHideGrp( 'root_weapon',0 )
	fileTools.doHideGrp( 'Root_JNT',0 )



	#... hide proxy joint
	fileTools.do_hide_objects(suffix = '_pxyJnt')
	fileTools.do_hide_objects(suffix = '_loc')



	#... delete delete grp
	fileTools.doDeleteGrp()	

	#... round skinweight
	do_pipeline_round_skinWeight()
	FileManagerLog.info('do_pipeline_round_skinWeight...\n')

	#... Count joint
	fileTools.countJnt()
	mc.select(deselect = True)	



class FileManagerActions:
	@staticmethod
	def createThumbnailAction(parent, callback):
		create_thumbnail_open = QtWidgets.QAction("Create thumbnail", parent)
		create_thumbnail_open.triggered.connect(callback)
		return create_thumbnail_open

	@staticmethod
	def createPrintBAction(parent, callback):
		print_b_action = QtWidgets.QAction("Rigger Tools", parent)
		print_b_action.triggered.connect(callback)
		return print_b_action

	@staticmethod
	def saveCtrlShapeAction(parent, callback):
		write_ctrl_action = QtWidgets.QAction("Write Controller", parent)
		write_ctrl_action.triggered.connect(callback)
		return write_ctrl_action

	@staticmethod
	def loadCtrlShapeAction(parent, callback):
		load_ctrl_action = QtWidgets.QAction("Load Controller", parent)
		load_ctrl_action.triggered.connect(callback)
		return load_ctrl_action

	@staticmethod
	def saveSkinWeightAction(parent, callback):
		save_skinWeight_action = QtWidgets.QAction("Save Skinweight", parent)
		save_skinWeight_action.triggered.connect(callback)
		return save_skinWeight_action

	@staticmethod
	def loadSkinWeightAction(parent, callback):
		load_skinWeight_action = QtWidgets.QAction("Load Skinweight", parent)
		load_skinWeight_action.triggered.connect(callback)
		return load_skinWeight_action




'''

#...
#... this is example for using python and SVN by GPT
#...

def run_tortoise_svn_command(svn_bin_path, cmd_type, file_path, logmsg='', close_on_end=0):
	command = [
		os.path.join(svn_bin_path, 'TortoiseProc.exe'),
		f'/command:{cmd_type}',
		f'/path:{file_path}',
		f'/logmsg:{logmsg}',
		f'/closeonend:{close_on_end}'
	]
	
	try:
		result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		print(result.stdout)
	except subprocess.CalledProcessError as e:
		print(f"Error running command: {e.cmd}")
		print(f"Return code: {e.returncode}")
		print(f"Output: {e.output}")
		print(f"Error output: {e.stderr}")

run_tortoise_svn_command(SVN_BIN_PATH, cmd_type, file_path, logmsg, close_on_end)
'''
