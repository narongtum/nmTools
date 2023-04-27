from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import os
from function.pipeline.file_manager.file_manager_ui import fileManagerMainUI

DRIVES = [		"D:\\",
				"E:\\"		]

PROJECT_NAME = ['P_sample','P_sample02']
DEFAULT_DRIVES = DRIVES[0]
DEFAULT_PROJECT = PROJECT_NAME[0]


class MyFileBrowser(fileManagerMainUI.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(MyFileBrowser, self).__init__()
		self.setupUi(self)
		self.path = None
		
		self.drive_comboBox.setCurrentText(DEFAULT_DRIVES)
		self.project_comboBox.setCurrentText(DEFAULT_PROJECT)

		# Populate Drive and Project combo boxes
		self.populate_drives()
		self.populate_project()
		self.update_project_comboBox()

		# Connect signals
		self.drive_comboBox.currentIndexChanged.connect(self.update_project_comboBox)
		self.project_comboBox.currentIndexChanged.connect(self.populate_treeView)
		

		self.populate_treeView()
		self.treeView.setSortingEnabled(True)
		self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.treeView.customContextMenuRequested.connect(self.show_context_menu)



		# Connect the ComboBoxes to the update_treeview function
		# self.drive_comboBox.currentTextChanged.connect(self.update_treeview)
		# self.project_comboBox.currentTextChanged.connect(self.update_treeview)






	def update_treeview(self, text):

		# Set up file system model
		model = QtWidgets.QFileSystemModel()


		# Get the selected drive and project from the ComboBoxes
		drive = self.drive_comboBox.currentText()
		project = self.project_comboBox.currentText()

		# Create the new directory path
		directory_path = drive + ":/" + project

		
		# Set the new root path for the file system model
		model.setRootPath(directory_path)

		# Set the new root index for the tree view
		self.treeView.setRootIndex(model.index(directory_path))


	def populate_drives(self):
		self.drive_comboBox.clear()
		self.drive_comboBox.addItems(DRIVES)
		# for index, drive in enumerate(DRIVES):
		# 	self.drive_comboBox.addItem(drive, index)


	def populate_project(self):
		self.project_comboBox.clear()
		self.project_comboBox.addItems(PROJECT_NAME)
		# for index, project in enumerate(PROJECT_NAME):
		# 	self.project_comboBox.addItem(project, index)


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


		print("Test Drive Path")
		print("Show selected_Drive:...\t\t\t", selected_drive)
		if selected_project == None:
			print('There are no Project name')
		print("Show selected_Project:...\t\t\t", selected_project)	

		# Populate Project comboBox
		self.project_comboBox.clear()
		self.project_comboBox.addItems(PROJECT_NAME)

		# Set the selected project in the Project comboBox
		self.project_comboBox.setCurrentText(selected_project)

		# Update tree view with new root path
		

			


	def populate_treeView(self):

		# Set up file system model
		model = QtWidgets.QFileSystemModel()
		# model.setRootPath(QtCore.QDir.rootPath())
		model.setRootPath(self.path)
		self.treeView.setModel(model)
		self.treeView.setRootIndex(model.index(self.path))
		self.treeView.setSortingEnabled(True)

		# Set up context menu
		self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.treeView.customContextMenuRequested.connect(self.show_context_menu)

		# Update the `self.path` variable whenever the user selects a new project
		self.path = os.path.join(self.drive_comboBox.currentText(), "svn_true", self.project_comboBox.currentText(), "Content")

		# Update the `model.setRootPath()` method whenever the user selects a new project
		model.setRootPath(self.path)

		# Print some information for debugging purposes
		print("\nPopulating tree view with file system model...")
		print("populate_treeView project path:... _456_\t\t\t", self.path)
		print("Model root path:...\t\t\t\n", model.rootPath())
		




	def show_context_menu(self, point):
		# Get the index of the item that was clicked
		index = self.treeView.indexAt(point)

		# Create a context menu
		menu = QtWidgets.QMenu(self)

		# Add a "New entite" action to the menu
		new_entitie_action = menu.addAction("New Entite...")

		 # Add a "New asset" action to the menu
		new_asset_action = menu.addAction("Create Asset...")

		# Show the context menu and get the chosen action
		chosen_action = menu.exec_(self.treeView.mapToGlobal(point))

		# If "New entite" was chosen, create a new entite
		if chosen_action == new_entitie_action:
			self.create_entite(index)

		# If "New asset" was chosen, create a new asset
		if chosen_action == new_asset_action:
			self.create_asset(index)


	def create_entite(self, index):
		# Get the filepath of the selected item
		parent_dir = self.treeView.model().filePath(index)
		print("parent_dir:", parent_dir)

		# Get the parent directory of the new entite
		# parent_dir = self.treeView.model().filepath(index)

		# Prompt the user to enter a entite name
		entitie_name, ok = QtWidgets.QInputDialog.getText(self, "New Entite", "Enter folder name:")

		# If the user entered a name, create the folder
		if ok and entitie_name:
			# Create full path to new folder
			new_folder_path = os.path.join(parent_dir, entitie_name)

			# Create new folder
			os.makedirs(new_folder_path)

			# Refresh the view to show the new folder
			self.treeView.update()


	def create_asset(self, index):
		# Get the parent directory of the new asset
		parent_dir = self.treeView.model().filePath(index)

		# Prompt the user to enter an asset name
		asset_name, ok = QtWidgets.QInputDialog.getText(self, "Create Asset", "Enter asset name:")

		# If the user entered a name, create the asset folders
		if ok and asset_name:
			# Create full path to new asset folder
			new_asset_path = os.path.join(parent_dir, asset_name)

			# Create asset folders
			os.makedirs(os.path.join(new_asset_path, "Model"))
			os.makedirs(os.path.join(new_asset_path, "Rig"))
			os.makedirs(os.path.join(new_asset_path, "Texture"))

			# Refresh the view to show the new asset folders
			self.treeView.update()





if __name__ == "__main__":
	try:
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])
		fileBrowser = MyFileBrowser()
		fileBrowser.show()
		print("Starting event loop...")
		app.exec_()
		#sys.exit(app.exec_())
		
	except Exception as e:
		print("Error: Error Error", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)