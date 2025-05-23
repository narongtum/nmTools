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

import re
import pymel.core as pm

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




# from function.pipeline.file_manager.fileManagerCore import SvnMaya



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






DRIVES = [			"D:\\",
					"E:\\"		]

PROJECT_NAME = ['P_sample','P_Regulus']
DEFAULT_PROJECT = PROJECT_NAME[-1]



CORE_VERSION = '0.0.010'





class FileAssetExporter(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(FileAssetExporter, self).__init__(parent or get_maya_main_window())
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setObjectName("FileAssetExporter")
		self.setWindowTitle(f"File Asset Exporter {CORE_VERSION}")


		self.ui.drive_comboBox.addItems(DRIVES)
		self.ui.drive_comboBox.setCurrentText("D:\\")

		self.ui.project_comboBox.addItems(PROJECT_NAME)
		self.ui.project_comboBox.setCurrentText(DEFAULT_PROJECT)

		
		self.ui.getAsset_pushButton.clicked.connect(self.on_get_asset_clicked)
		self.ui.export_1_pushButton.clicked.connect(self.on_export_type1_clicked)
		self.ui.export_2_pushButton.clicked.connect(self.on_export_type2_clicked)
		self.ui.commit_pushButton.clicked.connect(self.on_commit_clicked)

	def on_get_asset_clicked(self):
		prev_name = self.ui.input_path_lineEdit.text()
		QtWidgets.QMessageBox.information(self, "Get Asset", f"Find information about: {prev_name}")

	def on_export_type1_clicked(self):
		name = self.ui.text_1_lineEdit.text()
		checked = self.ui.asset_1_checkBox.isChecked()
		QtWidgets.QMessageBox.information(self, "Export Type 1", f"Export: {name}\nChecked: {checked}")

	def on_export_type2_clicked(self):
		name = self.ui.text_2_lineEdit.text()
		checked = self.ui.asset_2_checkBox.isChecked()
		QtWidgets.QMessageBox.information(self, "Export Type 2", f"Export: {name}\nChecked: {checked}")

	def on_commit_clicked(self):
		QtWidgets.QMessageBox.information(self, "Commit", "Committing data...(demo)")

	def on_get_asset_clicked(self):
		self.update_input_path_with_scene_name()






	def update_input_path_with_scene_name(self):
	    # ดึง path ของไฟล์ Maya ที่กำลังเปิดอยู่
	    maya_file_path = mc.file(query=True, sceneName=True)
	    
	    if not maya_file_path:
	        QtWidgets.QMessageBox.warning(self, "No Scene", "ยังไม่มีไฟล์ Maya ที่เปิดอยู่")
	        return

	    # ดึงชื่อไฟล์ไม่เอา path
	    file_name = os.path.basename(maya_file_path)
	    # ตัดนามสกุลออก (.ma หรือ .mb)
	    name_only, _ = os.path.splitext(file_name)

	    # แสดงผลในช่อง lineEdit
	    self.ui.input_path_lineEdit.setText(name_only)


