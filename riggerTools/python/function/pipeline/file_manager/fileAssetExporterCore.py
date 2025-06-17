from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from function.framework.reloadWrapper import reloadWrapper as reload
from function.pipeline.file_manager.file_manager_ui.fileExporterFinalUI import Ui_MainWindow
import os
#...  logging system 
import logging
from function.pipeline import logger 
reload(logger)

from function.pipeline import fileTools   
reload(fileTools)

import re
import pymel.core as pm

from function.asset import exportFBX 
reload(exportFBX)

from function.pipeline import svnMaya as svn 
reload(svn)


class FileManagerLog(logger.MayaLogger):
	LOGGER_NAME = "Hero ManagerLog"
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
FILE_CONFIG_PATH = os.path.join(directory, fileName)




try:
	#... Check if the file exists
	if os.path.exists(FILE_CONFIG_PATH):
		FileManagerLog.debug("Config File exists.")
		import fileManager_config as config
		reload(config)
		DRIVES = config.DRIVES
		PROJECT_NAME = config.PROJECT_NAME
		PROJECT_DICT_DETAIL = config.PROJECT_DETAIL
		GROUP_NAMES = config.GROUP_NAMES
	else:
		DRIVES = [			"D:\\",
							"E:\\"		]

		PROJECT_NAME = ['P_RP','P_Regulus']
		GROUP_NAMES = ['Model_grp', 'Export_grp']

except:
	print('There are no config file.')









def get_maya_main_window():
	main_window_ptr = omui.MQtUtil.mainWindow()
	return wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)


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














DEFAULT_PROJECT = PROJECT_NAME[1]
TITLE_WINDOW_NAME = 'Hero Exporter'
CORE_VERSION = '0.0.010'




class FileAssetExporter(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(FileAssetExporter, self).__init__(parent or get_maya_main_window())
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setObjectName("FileAssetExporter")
		self.setWindowTitle(f"{TITLE_WINDOW_NAME} {CORE_VERSION}")


		self.ui.drive_comboBox.addItems(DRIVES)
		self.ui.drive_comboBox.setCurrentText("D:\\")

		self.ui.project_comboBox.addItems(PROJECT_NAME)
		self.ui.project_comboBox.setCurrentText(DEFAULT_PROJECT)

		self.ui.getAsset_pushButton.clicked.connect(self.on_get_asset_clicked)
		self.ui.export_1_pushButton.clicked.connect(self.on_export_type1_clicked)
		self.ui.export_2_pushButton.clicked.connect(self.on_export_type2_clicked)

		self.fbx_folder_path = None
		self.ui.commit_pushButton.clicked.connect(self.on_commit_clicked)
		self.ui.add_pushButton.clicked.connect(self.on_add_clicked)



	def on_get_asset_clicked(self):
		self.update_input_path_with_scene_name()






	def update_input_path_with_scene_name(self):
		#... Get the path of the currently opened Maya file
		maya_file_path = mc.file(query=True, sceneName=True)

		
		if not maya_file_path:
			QtWidgets.QMessageBox.warning(self, "No Scene", "There are no Maya files open yet.")
			return

		#... check condition for working on HERO file only

		file_type = fileTools.fileState()
		FileManagerLog.info(f'this is file_type: {file_type}')

		if file_type == 'version':
			QtWidgets.QMessageBox.warning(self, "File Type Error", "Current Must be a Hero file.")
			return False
		elif file_type == 'local_hero':
			QtWidgets.QMessageBox.warning(self, "File Type Error", "Current Must be a Hero file.")
			return False

		elif file_type == 'global_hero':
			FileManagerLog.info('this is global_hero let check another ')

			#... Extract file name without path
			file_name = os.path.basename(maya_file_path)
			#... Remove the extension (.ma or .mb)
			name_only, _ = os.path.splitext(file_name)
			#... Display in the lineEdit field
			self.ui.input_path_lineEdit.setText(name_only)


		#... Recheck the project name
		project_name = fileTools.currentProject()
		if project_name != None:
			FileManagerLog.info('this is global_hero let check another ')
			self.ui.project_comboBox.setCurrentText(project_name)
			current_project = self.ui.project_comboBox.currentText()


			self.apply_project_config_to_ui(current_project)

			#... specific naming for only P_Regulus project




	def apply_project_config_to_ui(self, project_name):
		project_config = PROJECT_DICT_DETAIL.get(project_name)

		if not project_config:
			QtWidgets.QMessageBox.warning(self, "Project Not Found", f"No config found for '{project_name}'")
			return

		#  Set naming 01
		self.ui.text_replace_01_lineEdit.setText(project_config["FILE_01_NAMING_REPLACE"])
		self.ui.text_with_01_lineEdit.setText(project_config["FILE_01_NAMING_WITH"])
		self.ui.asset_1_checkBox.setChecked(True)

		original_name = self.ui.input_path_lineEdit.text()
		if original_name:
			result_01 = original_name.replace(
				project_config["FILE_01_NAMING_REPLACE"],
				project_config["FILE_01_NAMING_WITH"]
			)
			self.ui.text_result_01_lineEdit.setText(result_01)

		#...  Check typeNum before set naming 02
		if project_config.get("typeNum") != "1":
			self.ui.text_replace_02_lineEdit.setText(project_config.get("FILE_02_NAMING_REPLACE", ""))
			self.ui.text_with_02_lineEdit.setText(project_config.get("FILE_02_NAMING_WITH", ""))
			self.ui.asset_2_checkBox.setChecked(True)

			if original_name:
				result_02 = original_name.replace(
					project_config.get("FILE_02_NAMING_REPLACE", ""),
					project_config.get("FILE_02_NAMING_WITH", "")
				)
				self.ui.text_result_02_lineEdit.setText(result_02)
		else:
			#... Clear channel naming 02 is exists
			self.ui.text_replace_02_lineEdit.clear()
			self.ui.text_with_02_lineEdit.clear()
			self.ui.text_result_02_lineEdit.clear()
			self.ui.asset_2_checkBox.setChecked(False)










	def on_export_type1_clicked(self):
		found_targets = []

		# Search case-insensitive
		all_transforms = mc.ls(type='transform')
		for name in GROUP_NAMES:
			for obj in all_transforms:
				if obj.lower() == name.lower():
					found_targets.append(obj)

		if not found_targets:
			QtWidgets.QMessageBox.warning(self, "Not Found", "No matching 'Export_grp' and 'Model_grp' found in scene.")
			return

		# Select object 
		mc.select(clear=True)
		mc.select(found_targets)

		# Unparent to world if parent exists
		for node in found_targets:
			parent = mc.listRelatives(node, parent=True)
			if parent:
				mc.parent(node, world=True)


		#... selected
		mc.select(found_targets)
		#... get new name
		FBX_new_name = self.ui.text_result_01_lineEdit.text()

		#... get destination export part
		self.fbx_folder_path = fileTools.findAppropriateFBXFolder()

		FileManagerLog.debug(f'\n{found_targets}')
		FileManagerLog.debug(f'\n{FBX_new_name}')
		FileManagerLog.debug(f'\n{self.fbx_folder_path}')

		if not FBX_new_name.strip():
			QtWidgets.QMessageBox.warning(self, "No Name", "Please generate export name before exporting.")
			return

		exportFBX.exportFBX_with_path(found_targets, fileName = FBX_new_name, path = self.fbx_folder_path)

	def on_export_type2_clicked(self):
		# name = self.ui.text_2_lineEdit.text()
		# checked = self.ui.asset_2_checkBox.isChecked()
		found_targets = mc.ls(sl=True)
		if not found_targets:
			QtWidgets.QMessageBox.warning(self, "Not Found", "No matching 'Export_grp' and 'Model_grp' found in scene.")
			return	
		FBX_new_name = self.ui.text_result_02_lineEdit.text()
		self.fbx_folder_path = fileTools.findAppropriateFBXFolder()
		exportFBX.exportFBX_with_path(found_targets, fileName = FBX_new_name, path = self.fbx_folder_path)
		QtWidgets.QMessageBox.information(self, "Export Type 2", f"Export: {name}\nChecked: {checked}")

	def on_commit_clicked(self):
		if not self.fbx_folder_path:
			QtWidgets.QMessageBox.warning(self, "No Path", "Please export first to define path.")
			return
		try:	
			svn_maya = svn.SvnMaya()
			svn_maya.execute_cmd('commit', file_path = self.fbx_folder_path, close_on_end=0, logmsg='')
			QtWidgets.QMessageBox.information(self, "Commit", f"Committing to path:\n{self.fbx_folder_path}")

		except Exception as e:
			QtWidgets.QMessageBox.critical(self, "SVN Commit Failed", str(e))

	def on_add_clicked(self):
		if not self.fbx_folder_path:
			QtWidgets.QMessageBox.warning(self, "No Path", "Please export first to define path.")
			return

		svn_maya = svn.SvnMaya()
		svn_maya.execute_cmd('add', file_path = self.fbx_folder_path, close_on_end=0, logmsg='')

		QtWidgets.QMessageBox.information(self, "Add", f"Adding to path:\n{self.fbx_folder_path}")
