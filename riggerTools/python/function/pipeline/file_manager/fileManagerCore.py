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

import subprocess
import sys
from function.framework.reloadWrapper import reloadWrapper as reload
from function.pipeline import logger 
reload(logger)
import re
class FileManagerLog(logger.MayaLogger):
	LOGGER_NAME = "FileManagerLog"
	
import maya.cmds as mc




DRIVES = [		"D:\\",
				"E:\\"		]

PROJECT_NAME = ['P_sample','P_sample03','P_Regulus']

DICTIONARY_TEMPLATE = {		

							"base_path":""				,
							"entitie_type":""			,
							"entitie_name":""			,
							"full_entity_name":""		,
							"comment":""				,
							"department_name":""

							}

# DEPT_NAME 		= 	['Model', 'Rig']
DEPT_NAME 			= 	['Model', 'Rig','ConceptArt', 'Texture', 'VFX', 'Anim']
# DEPT_EMPTY 		= 	['ConceptArt', 'ConceptArt', 'Texture', 'VFX', 'Anim']
DEPT_EMPTY 			= 	['Commit']
JOB_TEMPLATE 		= 	['Version', 'Data', 'Output', 'Commit']
EXCLUDE_VIEW_ITEM 	= 	['data.json', 'thumb.png', 'Commit']
STATIC_FOLDER 		= 	['Content','Version']
DEFAULT_PROJECT 	= 	'P_Regulus'
PADDING 			= 	4
MAYA_EXT 			= 	'ma'
USE_VARIATION 		= 	True
IMAGE_FORMAT		= 	'thumb.png'

class FileManager(fileManagerMainUI.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(FileManager, self).__init__()
		self.setupUi(self)
		self.path = None
		FileManagerLog.debug('Run this first...')

		# Define model as an instance variable
		self.model = None
		
		

		# Populate Drive and Project combo boxes
		self.populate_drives()
		self.populate_project()
		# self.update_project_comboBox() # It seems redundance with connect update_project_comboBox

		FileManagerLog.debug('Than this...')
		self.drive_comboBox.setCurrentText(DRIVES[0])
		self.project_comboBox.setCurrentText(DEFAULT_PROJECT)


		# Set "Asset" tab as default
		self.entite_TAB.setCurrentIndex(0)  

		# Connect signals
		self.drive_comboBox.currentIndexChanged.connect(self.update_project_comboBox)
		# Connect project
		self.project_comboBox.currentIndexChanged.connect(self.populate_treeView)	

		# Called whenever a new item is clicked
		self.populate_treeView()

		# Connect the on_treeview_clicked method to the clicked signal
		self.asset_dir_TREEVIEW.clicked.connect(self.on_treeview_clicked)

		# Connect the on_department_clicked method to the clicked signal
		self.asset_department_listWidget.itemClicked.connect(self.on_department_clicked)

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

		# Set up context menu
		self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) #... repetitive code with __init__
		self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu) #... repetitive code with __init__

		self.asset_version_view_listWidget.itemDoubleClicked.connect(self.handle_double_click)

		# # Try to use as another class but not work
		# self.asset_version_view_listWidget.itemDoubleClicked.connect(MayaHandler.handle_double_click)

		# self.handler = MayaHandler(asset_path, MAYA_EXT)
		# self.handler.handle_double_click()

	def handle_double_click(self, item):
		file_path = self.get_deep_path()
		FileManagerLog.debug('This is get_full_path: {0}'.format(file_path))

		# Check file extension
		file_name, extension = os.path.splitext(file_path)

		if extension:
			if extension == '.mb' or extension == '.ma':
				self.maya_open(file_path)
			else:
				os.startfile(filePath)
		else:
			FileManagerLog.debug('There are no extension ?.')


		
		


	def show_step_context(self, position):
		# Create Jobs
		contextMenu = QtWidgets.QMenu(self)
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
			FileManagerLog.debug('There are no step list why?_140_')





		# Disconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_version_view_listWidget.customContextMenuRequested.disconnect(self.show_step_context)

		# Show the context menu at the specified position
		contextMenu.exec_(self.asset_version_view_listWidget.mapToGlobal(position))

		# Reconnect the signal-slot connection for the customContextMenuRequested signal
		self.asset_version_view_listWidget.customContextMenuRequested.connect(self.show_step_context)


			
	def handle_dynamic_context(self):
		# Get the selected action
		action = self.sender()
		# Get the data (selected context option) from the action
		selected_context = action.data()

		# Create a confirmation dialog
		confirmation_dialog = QMessageBox(self)
		confirmation_dialog.setIcon(QMessageBox.Question)
		confirmation_dialog.setText(f"Are you sure you want to save this step job: {selected_context}?")
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

			for element in my_list:
				# split name and extension using regular expression
				# Warning !!! Weak condition
				match = re.search(r'_(\w+)\.(\d+)\.ma$|\.mb$', element)
				if match:
					name = match.group(1)
					name = name.split('_')[-1]
					version = int(re.search(r'\.(\d+)\.ma$|\.mb$', element).group(1))
					if name not in result or version > int(result[name][1]): # zfill later
						# result[name] = [element, str(version).zfill(3)]
						result[name] = [element, version]
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




	def filter_proper_version_list(self):
	# Make list to proper version workspace listWidget
	# 1. cut off if naming is not having prior folder name
	# 2. if file is not ma or mb

				# Get full path
		asset_path = self.get_full_path()
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
		if selected_project == 'P_Regulus':
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
		asset_path_text = self.get_full_path()
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


		if selected_project == 'P_Regulus':
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
			FileManagerLog.debug('None_Variation_asset_name_352_: {0}\t{1}\t'.format(asset_name, job_name))

		FileManagerLog.debug('THIS IS >>>\t\t\tresult_job_element:\t\t\t {0}'.format(result_job_element))
		FileManagerLog.debug('THIS IS TYPE>>>\t\t\tresult_job_element:\t\t\t {0}'.format(type(result_job_element)))

		if result_job_element != False:
			step_list = result_job_element['step']
			if step_name in step_list:

				index = step_list.index(step_name)

				max_version = result_job_element['max_version'][index]
				max_version += 1
				max_version = str(max_version).zfill(PADDING)

				FileManagerLog.debug('If having already step name: {0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT))

			else:
				max_version = str(1).zfill(PADDING)
				FileManagerLog.debug('If new file not found: {0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT))
		else:
			max_version = str(1).zfill(PADDING)
			FileManagerLog.debug('If new file not found: {0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT))		

		new_file_name =  '{0}_{1}.{2}.{3}'.format(final_file_name, step_name, max_version, MAYA_EXT)



		new_full_path = os.path.normpath(os.path.join(asset_path_text, department_text, STATIC_FOLDER[1], new_file_name))
		version_folder_path = os.path.normpath(os.path.join(asset_path_text, department_text, STATIC_FOLDER[1]))

		FileManagerLog.debug('THIS IS new_full_path: {0}'.format(new_full_path)) 
		self.maya_save(new_full_path, MAYA_EXT)

		# To refresh version viewport
		self.asset_version_view_listWidget.clear()
		# Update version listWidget viewport
		self.show_version_entite(version_folder_path)

		FileManagerLog.debug('File saving at: {0}'.format(new_full_path)) 
		return True


	def maya_open(self, file_path):
		file_name = file_path.split('\\')[-1]
		if mc.file(query = True, anyModified=True):
			reply = QMessageBox.question(			# Use self as the parent
													self ,
													'Save Chganges' ,
													'Current file has unsaved changes. Do you want to save? {0}'.format(file_name) ,
													QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No
												)

			if reply == QMessageBox.Save:
				mc.file(save=True, type='mayaAscii')

			elif reply == QMessageBox.Cancel:
				return

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

	def maya_save(self, filepath, MAYA_EXT):

		if MAYA_EXT == 'ma':
			maya_type = 'mayaAscii'
		elif MAYA_EXT == 'mb':
			maya_type = 'mayaBinary'


		mc.file(rename=filepath)
		mc.file(save=True, force=True, type=maya_type)
		FileManagerLog.debug('FILE SAVE AT: {0}'.format(filepath)) 
		self.maya_add_recen_file(filepath, MAYA_EXT)
		return True




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

	def show_job_explorer(self):
		asset_path_text = self.get_full_path()
		new_department_text = self.asset_department_listWidget.currentItem().text()
		new_folder_path = os.path.join(asset_path_text, new_department_text, STATIC_FOLDER[1])
		new_folder_path = self.handle_selected_path(new_folder_path)

		FileManagerLog.debug('This is open explorer path: {0}'.format(new_folder_path))

		# Open the selected folder in the file explorer in hardway
		if new_folder_path:
			if sys.platform == "win32": # Windows
				subprocess.Popen(f'explorer "{new_folder_path}"')
			elif sys.platform == "darwin": # macOS
				subprocess.Popen(["open", new_folder_path])
			else: # Linux 
				subprocess.Popen(["xdg-open", new_folder_path])	
					

	# Create jobs for department
	def create_jobs(self):
		jobs_name, okPressed = QInputDialog.getText(self, "Create Jobs", "Enter folder name:")
		if okPressed and jobs_name:
			# Create the folder at the department level
			# new_department_text = self.asset_department_listWidget.currentItem().text()
			asset_path = self.get_full_path()
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
			
			


	
	def display_images(self,image_paths):
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
			# self.asset_thumbnail_IMAGE_LABEL.clear()





	def populate_drives(self):
		self.drive_comboBox.clear()
		self.drive_comboBox.addItems(DRIVES)


	def populate_project(self):
		self.project_comboBox.clear()
		self.project_comboBox.addItems(PROJECT_NAME)


	def update_project_comboBox(self):

		selected_drive = self.drive_comboBox.currentText()
		selected_project = self.project_comboBox.currentText()


		print("\nThis is Run When start")
		# Set selected drive and project as root path
		try:
			self.path = os.path.join(selected_drive, "svn_true", DEFAULT_PROJECT, "Content")
		except FileNotFoundError:
			FileManagerLog.error("Invalid project name!")
			self.path = os.path.join(selected_drive, "svn_true", PROJECT_NAME[0], "Content")
		print("Show project path:...\t\t\t", self.path)

		# Update the selected project variable with the current selection
		selected_project = self.project_comboBox.currentText()
		print("Show project name _255_:...\t\t\t", selected_project)


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

		### will shift to method #####
		# Check if exists
		if os.path.exists(version_folder):
			# Corrective back and forward slash together
			version_folder = os.path.normpath(version_folder)
			FileManagerLog.debug("Version_folder path: {0}".format(version_folder) )



			# If the selection has 'Version' folder
			if not os.path.isfile(version_folder):

				version_file_list = os.listdir(version_folder)			
				self.asset_version_view_listWidget.addItems(version_file_list)
				# local_commit_folder = os.path.join(asset_path, department_text, 'Commit')
				# self.load_local_commit(local_commit_folder)
		else:
			FileManagerLog.info('The folder Version does not exists.')
			pass

	
	# Try to make return directory when clicked in treeview
	def on_treeview_clicked(self, index):

		self.asset_local_view_listWidget.clear()
		self.asset_global_listWidget.clear()
		self.asset_department_listWidget.clear()
		self.asset_version_view_listWidget.clear()

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
				global_commit_folder = os.path.join(file_path, 'Commit')

				if os.path.exists(global_commit_folder):
					self.load_global_commit(global_commit_folder)

				# Show thumbnail
				thumbnail_path = os.path.join(file_path, 'thumb.png')
				self.display_images(thumbnail_path)
				
			'''
			# Show version folder when also click Department on Treeview
			# Disable for this make confusion

			else:
				
				parent_path = os.path.dirname(file_path)
				if os.path.exists(os.path.join(parent_path, 'data.json')):
					FileManagerLog.debug('There must be department folder on treeView for sure: {0}'.format(parent_path))

					# Then show list in version widget
					version_folder_path = os.path.join(file_path, 'Version')
					FileManagerLog.debug(version_folder_path)
					self.show_version_entite(version_folder_path)
					# Split folder for making nanming working file
				else:
					FileManagerLog.debug('There must be normal folder')
			'''




				# Do not expand the asset folder if already expanded(still not work)
				# if self.asset_dir_TREEVIEW.isExpanded(index):
				# 	self.asset_dir_TREEVIEW.setExpanded(index, False)




	def on_department_clicked(self, item):

		# Get selected department
		selected_item = self.asset_department_listWidget.currentItem()
		# Return departments name
		department_text = selected_item.text()
		FileManagerLog.debug("Return departments name: {0}".format(department_text) )

		# Get root path
		asset_path = self.get_full_path()
		# self.handle_selected_path(asset_path)

		version_folder = os.path.join(asset_path, department_text, 'Version')

		### will shift to method #####
		self.show_version_entite(version_folder)

		local_commit_folder = os.path.join(asset_path, department_text, 'Commit')

		# If folder 'Commit' exist then continue
		if os.path.exists(local_commit_folder):
			self.load_local_commit(local_commit_folder)
		else:
			pass



	def on_version_clicked(self):
		# Get root path
		asset_path = self.get_full_path()
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
		FileManagerLog.debug("\nFound Local Commit: {0}".format(local_commit_list) )



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



	def get_full_path(self): # Method to get full path from treeView
		# Construct the full path based on the selected text
		current_index = self.asset_dir_TREEVIEW.currentIndex()
		full_path = self.model.filePath(current_index)
		full_path = os.path.normpath(full_path)
		FileManagerLog.debug("Return full path: {0}".format(full_path) )
		return full_path


	def get_deep_path(self):
		# Return full path to work file and extension		
		current_index = self.asset_dir_TREEVIEW.currentIndex()
		full_path = self.model.filePath(current_index)
		department_text = self.asset_department_listWidget.currentItem().text()

		# Get current selected in Version listWidget
		selected_task = self.asset_version_view_listWidget.currentItem()
		selected_task_text = selected_task.text()

		current_version_clicked = os.path.join(full_path, department_text, STATIC_FOLDER[1], selected_task_text)
		current_version_clicked = os.path.normpath(current_version_clicked)

		FileManagerLog.debug("Return current_version_clicked name: {0}".format(current_version_clicked) )

		return current_version_clicked





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



	def populate_treeView(self):

		# GPT comment update the self.path variable and call model.setRootPath() before updating the tree view 
		# Update the `self.path` variable whenever the user selects a new project
		self.path = os.path.join(self.drive_comboBox.currentText(), "svn_true", self.project_comboBox.currentText(), "Content")

		# Set up file system model
		# model = QtWidgets.QFileSystemModel()
		# model.setRootPath(self.path)

		# Store model as an instance variable
		self.model = QtWidgets.QFileSystemModel()  
		self.model.setRootPath(self.path)

		# Hide some file formats, such as ".pyc" and ".o" files
		self.model.setNameFilters(['*.pyc', '*.o'])
		self.model.setNameFilterDisables(False)

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
		print("\nPopulating tree view with file system model...")
		print("populate_treeView project path:... _456_\t\t\t", self.path)
		print("Model root path:...\t\t\t", self.model.rootPath())

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
		content_index = directories.index("Content")

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




	def create_data_JSON(self, base_path, entitie_type, entitie_name, full_entity_name, department_name, comment ):
		# Write to dictionary
		entitie_dict = DICTIONARY_TEMPLATE
		entitie_dict["base_path"] = base_path
		entitie_dict["entitie_type"] = entitie_type
		entitie_dict["entitie_name"] = entitie_name
		entitie_dict["full_entity_name"] = full_entity_name
		entitie_dict["department_name"] = department_name
		entitie_dict["comment"] = comment
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
				print("\tThere are no folder in here Continue.")

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
				print("\tThis is asset path:\t{0}".format(new_asset_path))

				# 'Asset' or 'Scene'
				print("\tType:\t{0}".format('Asset-718-'))

				# Asset_name 
				print("\tAsset name:\t{0}".format(asset_name))
				
				# "fullEntityName"
				fullEntityName = self.get_full_entity_name(new_asset_path)
				# comment (not require)

				# extension(not use)

				# Get department name
				department_name = self.get_department_name(new_asset_path)
				FileManagerLog.info('This is department_name:\t\t{0}')
			
				# Write to json file
				entite_dict = self.create_data_JSON(new_asset_path, 'Asset', asset_name, fullEntityName, department_name, "")
				print (entite_dict)
				self.write_entite_folder(entite_dict)

			else:
				print("\tThere are already folder skipped.")
				pass

				# Refresh the view to show the new asset folders
				self.asset_dir_TREEVIEW.update()

# NO USE CLASS Try to use as another class but not work
class MayaHandler:
	def __init__(self, asset_path, MAYA_EXT):
		self.asset_path = asset_path
		self.MAYA_EXT = MAYA_EXT


	def handle_double_click(self, asset_path, MAYA_EXT):
		print(f"Performing action for asset path: {self.asset_path}{self.MAYA_EXT}")





