# This version is add 2nd Tab name "Scene"
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import os
from function.pipeline.file_manager.file_manager_ui import fileManagerMainUI

DRIVES = [		"D:\\",
				"E:\\"		]

PROJECT_NAME = ['P_sample','P_sample02']

class MyFileBrowser(fileManagerMainUI.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(MyFileBrowser, self).__init__()
		self.setupUi(self)
		self.path = None
		
		self.drive_comboBox.setCurrentText(DRIVES[0])
		self.project_comboBox.setCurrentText(PROJECT_NAME[0])

		# Populate Drive and Project combo boxes
		self.populate_drives()
		self.populate_project()
		self.update_project_comboBox()

		# Connect signals
		self.drive_comboBox.currentIndexChanged.connect(self.update_project_comboBox)
		self.project_comboBox.currentIndexChanged.connect(self.populate_treeView)		
		self.populate_treeView()

		#... try to disable line
		# self.asset_dir_TREEVIEW.setSortingEnabled(True)
		self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu)

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

		# Update tree view with new root path
	

	def populate_treeView(self):
		# GPT comment update the self.path variable and call model.setRootPath() before updating the tree view 
		# Update the `self.path` variable whenever the user selects a new project
		self.path = os.path.join(self.drive_comboBox.currentText(), "svn_true", self.project_comboBox.currentText(), "Content")

		# Set up file system model
		model = QtWidgets.QFileSystemModel()
		model.setRootPath(self.path)
		self.asset_dir_TREEVIEW.setModel(model)
		self.asset_dir_TREEVIEW.setRootIndex(model.index(self.path))
		self.asset_dir_TREEVIEW.setSortingEnabled(True)

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
		print("Model root path:...\t\t\t", model.rootPath())

		#... try to disable line
		# Update the `model.setRootPath()` method whenever the user selects a new project
		# model.setRootPath(self.path)
	

	def show_context_menu(self, point):

		# Get the index of the item that was clicked
		index = self.asset_dir_TREEVIEW.indexAt(point)

		# Create a context menu
		menu = QtWidgets.QMenu(self)

		# Add a "New entite" action to the menu
		new_entitie_action = menu.addAction("New Entite...")

		 # Add a "New asset" action to the menu
		new_asset_action = menu.addAction("Create Asset...")

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


	def create_asset(self, index):
		# Get the parent directory of the new asset
		parent_dir = self.asset_dir_TREEVIEW.model().filePath(index)

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
			self.asset_dir_TREEVIEW.update()


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