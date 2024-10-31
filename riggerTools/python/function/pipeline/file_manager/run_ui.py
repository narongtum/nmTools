from PySide2 import QtWidgets, QtCore  # Add QtCore here
import importlib
from function.pipeline.file_manager import fileManagerCore
import sys
from function.framework.reloadWrapper import reloadWrapper as reload

#...  logging system 
import logging

from function.pipeline import logger 
reload(logger)

class BuildUILog(logger.MayaLogger):
	LOGGER_NAME = "BuildUILog"



from maya import cmds as mc






def getdWindowTitle():
	window_titles = []

	app = QtWidgets.QApplication.instance()
	if app:
		#... Iterate through all top-level widgets
		for widget in app.topLevelWidgets():
			if isinstance(widget, QtWidgets.QMainWindow):
				BuildUILog.debug(f"Object Name: {widget.objectName()}")
				BuildUILog.info(f"Window Title: {widget.windowTitle()}")
				window_titles.append(widget.windowTitle())
				BuildUILog.debug(f"Widget Address: {widget}")
			
		 
		return window_titles
	else:
		return False




#... not use anymore
def isWindowOpen(window_title):
	app = QtWidgets.QApplication.instance()
	if not app:
		return False

	for widget in app.topLevelWidgets():
		if isinstance(widget, QtWidgets.QMainWindow) and widget.windowTitle() == window_title:
			if widget.isVisible():
				print('Windows is Open.')
				return True
			else:
				widget.close()
				print('Windows is Close.')
				return False
	print('Windows is Close. Windows is Close.')
	# mc.error('Break')
	return False




def run_file_manager():
	try:
		importlib.reload(fileManagerCore)
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])




		#... Check if the window is already open
		if getdWindowTitle() != []:
			BuildUILog.debug("FileManager is already open. Bringing it to the front...")

			#... Find title name
			TITLE = getdWindowTitle()[0]
			
			for widget in QtWidgets.QApplication.topLevelWidgets():
				if isinstance(widget, QtWidgets.QMainWindow) and widget.windowTitle() == TITLE:
					if widget.isMinimized():
						widget.showNormal()  #... Restore the window if it's minimized
					widget.activateWindow()	#... Activate the window
					widget.raise_() #... Bring the window to the front
					return True
		else:

			BuildUILog.debug("FileManager may not open before.")
			# Create a new instance of the FileManager window
			file_browser = fileManagerCore.FileManager()
			#... Ensure that the instance is properly deleted from memory
			file_browser.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
			file_browser.show()
			BuildUILog.debug("Starting event loop...")
			app.exec_()

	except Exception as e:
		print("Error:", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)


if __name__ == "__main__":
	run_file_manager()
