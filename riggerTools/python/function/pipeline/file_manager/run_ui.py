"""
run_ui.py
Module for Portal safely invoking FileManager and FileAssetExporter UI in Maya.
"""



'''
from function.pipeline.file_manager import run_ui
reload(run_ui)
run_ui.run_file_exporter()

run_ui.run_file_manager()

'''
from PySide2 import QtWidgets, QtCore
import importlib
import sys
import logging
from maya import cmds as mc

from function.framework.reloadWrapper import reloadWrapper as reload
from function.pipeline import logger
reload(logger)

from function.pipeline.file_manager import fileManagerCore
from function.pipeline.file_manager import fileAssetExporterCore
importlib.reload(fileAssetExporterCore)

from function.pipeline.file_manager.fileAssetExporterCore import FileAssetExporter





class BuildUILog(logger.MayaLogger):
	LOGGER_NAME = "BuildUILog"

def get_open_windows_by_name(target_name):
	app = QtWidgets.QApplication.instance()
	result = []
	if app:
		for widget in app.topLevelWidgets():
			if isinstance(widget, QtWidgets.QMainWindow):
				BuildUILog.debug(f"Object Name: {widget.objectName()}")
				BuildUILog.info(f"Window Title: {widget.windowTitle()}")
				if widget.objectName() == target_name:
					result.append(widget)
	return result

def run_file_manager():
	try:
		importlib.reload(fileManagerCore)
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])

		open_windows = get_open_windows_by_name("FileManager")
		if open_windows:
			BuildUILog.debug("FileManager is already open. Bringing it to the front...")
			win = open_windows[0]
			if win.isMinimized():
				win.showNormal()
			win.raise_()
			win.activateWindow()
			return True
		else:
			BuildUILog.debug("FileManager may not open before.")
			file_browser = fileManagerCore.FileManager()
			file_browser.setObjectName("FileManager")
			file_browser.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
			file_browser.show()

	except Exception as e:
		print("Error:", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)

def run_file_exporter():
	try:
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])

		open_windows = get_open_windows_by_name("FileAssetExporter")
		if open_windows:
			BuildUILog.debug("FileExporter is already open. Bringing it to the front...")
			win = open_windows[0]
			if win.isMinimized():
				win.showNormal()
			win.raise_()
			win.activateWindow()
			return True
		else:
			BuildUILog.debug("FileExporter may not open before.")
			exporter_window = FileAssetExporter()
			exporter_window.setObjectName("FileAssetExporter")
			exporter_window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
			exporter_window.show()

	except Exception as e:
		print("Error:", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)
