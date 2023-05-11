from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import json
import os
from function.pipeline.file_manager.file_manager_ui import fileManagerMainUI

from function.pipeline import logger 
reload(logger)

class FileManagerLog(logger.MayaLogger):
	LOGGER_NAME = "FileManagerLog"





DRIVES = [		"D:\\",
				"E:\\"		]

PROJECT_NAME = ['P_sample','P_sample02']

DICTIONARY_TEMPLATE = {		

							"base_path":""				,
							"entitie_type":""			,
							"entitie_name":""			,
							"full_entity_name":""		,
							"comment":""				,
							"department_name":""

							}

# DEPT_NAME 		= 	[ 'Model', 'Rig']
DEPT_NAME 		= 	[ 'Model', 'Rig','ConceptArt', 'Texture', 'VFX', 'Anim']
# DEPT_EMPTY 		= 	[ 'ConceptArt', 'ConceptArt', 'Texture', 'VFX', 'Anim']
DEPT_EMPTY 		= 	['Commit']
JOB_TEMPLATE 	= 	[ 'Version', 'Data', 'Output', 'Commit']


class FileManager(fileManagerMainUI.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(FileManager, self).__init__()
		self.setupUi(self)
		self.path = None

		# Define model as an instance variable
		self.model = None
		
		self.drive_comboBox.setCurrentText(DRIVES[0])
		self.project_comboBox.setCurrentText(PROJECT_NAME[0])

		# Populate Drive and Project combo boxes
		self.populate_drives()
		self.populate_project()
		self.update_project_comboBox()

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
			self.path = os.path.join(selected_drive, "svn_true", selected_project, "Content")
		except FileNotFoundError:
			print("Invalid project name!")
			self.path = os.path.join(selected_drive, "svn_true", PROJECT_NAME[0], "Content")
		print("Show project path:...\t\t\t", self.path)

		# Update the selected project variable with the current selection
		selected_project = self.project_comboBox.currentText()
		print("Show project name _123_:...\t\t\t", selected_project)


		if selected_project == None:
			print('There are no Project name')
		print("Show selected_Project:...\t\t\t", selected_project)	

		# Populate Project comboBox
		self.project_comboBox.clear()
		self.project_comboBox.addItems(PROJECT_NAME)

		# Set the selected project in the Project comboBox
		self.project_comboBox.setCurrentText(selected_project)


	
	# Try to make return directory when clicked in treeview
	def on_treeview_clicked(self, index):

		# For department QListWidget
		# Get the file name and path from the model
		file_path = self.model.filePath(index)
		print(file_path)

		#  Checks if the item is a file or not.
		if os.path.isfile(file_path):
			FileManagerLog.debug('This is file for sure')
			return
		else:
			FileManagerLog.debug('This is folder for sure')
			data_file = os.path.join(file_path, 'data.json')
			if os.path.exists(data_file):
				FileManagerLog.info('\nThis maybe asset folder we looking for.')
				self.load_asset_departments(file_path)

				# For local commit QListWidget
				self.load_local_commit(file_path)

	def load_local_commit(self, folder_path):
		# Clear the list widget
		self.asset_department_listWidget.clear()



	# def on_department_clicked(self, item):
	# 	current_item = self.asset_department_listWidget.currentItem()
	# 	selected_text = current_item.text()

	# 	current_index = self.asset_dir_TREEVIEW.currentIndex()
	# 	full_path = self.model.filePath(current_index)

	# 	FileManagerLog.info("Selected Department: {0}".format(selected_text))
	# 	FileManagerLog.info("Full Path: {0}".format(full_path))
	# 	return full_path

	def on_department_clicked(self, item):
		selected_item = self.asset_department_listWidget.currentItem()

		# Return departments name
		department_text = selected_item.text()
		FileManagerLog.debug("Return departments name: {0}".format(department_text) )
		asset_path = self.get_full_path()
		self.handle_selected_path(asset_path)
		version_folder = os.path.join(asset_path, department_text, 'Version')

		# Check if exists
		if os.path.exists(version_folder):
			# Corrective back and forward slash together
			version_folder = os.path.normpath(version_folder)
			FileManagerLog.debug("Version_folder path: {0}".format(version_folder) )

			# Clear the QListWidget
			self.asset_version_view_listWidget.clear()

			# If the selection has 'Version' folder
			if not os.path.isfile(version_folder):

				version_file_list = os.listdir(version_folder)
				
				self.asset_version_view_listWidget.addItems(version_file_list)
		else:
			FileManagerLog.info('The folder Version does not exists.')
			# self.asset_version_view_listWidget.clear()
			# department_select = os.path.join(asset_path, department_text)
			# department_file_list = os.listdir(department_select)
			# self.asset_version_view_listWidget.addItems(department_file_list)

		


	# # Share a method that returns the path of the selected
	# def get_full_path(self, selected_text):
	# 	# Construct the full path based on the selected text
	# 	full_path = os.path.join(self.path, selected_text)
	# 	self.handle_selected_path(full_path)
	# 	return full_path

	def get_full_path(self):
		current_index = self.asset_dir_TREEVIEW.currentIndex()
		full_path = self.model.filePath(current_index)
		FileManagerLog.debug("Return full path: {0}".format(full_path) )
		return full_path




	def handle_selected_path(self, path):
		# Do something with the selected path
		FileManagerLog.info("handle_selected_path: {0}".format(path) )
		

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
			for each in items:
				if each != 'data.json': # exclude file 'data.json'
					departments.append(each)
			self.asset_department_listWidget.addItems(departments)


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
		self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) #... repetitive code with __init__
		self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu) #... repetitive code with __init__

		# Print some information for debugging purposes
		print("\nPopulating tree view with file system model...")
		print("populate_treeView project path:... _456_\t\t\t", self.path)
		print("Model root path:...\t\t\t", self.model.rootPath())

		# Show department listWidget when selected asset
		# self.asset_department_listWidget.addItems(['Model', 'Rig', 'ConceptArt', 'Texture', 'VFX', 'Anim'])
		# print("\nShow department...")
	

	def show_context_menu(self, point):

		# Get the index of the item that was clicked
		index = self.asset_dir_TREEVIEW.indexAt(point)

		# Create a context menu
		menu = QtWidgets.QMenu(self)

		# Add a "New entite" action to the menu
		new_entitie_action = menu.addAction("New Entite...")

		 # Add a "New asset" action to the menu
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
				print("\tType:\t{0}".format('Asset'))

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


if __name__ == "__main__":
	try:
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])
		fileBrowser = FileManager()
		fileBrowser.show()
		print("Starting event loop...")
		app.exec_()
		#sys.exit(app.exec_())
		
	except Exception as e:
		print("Error: Error Error", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)