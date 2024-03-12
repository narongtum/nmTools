from PySide2 import QtWidgets
import importlib
from function.pipeline.file_manager import fileManagerCore
import sys

# def isWindowOpen(window_title):
# 	app = QtWidgets.QApplication.instance()
# 	if not app:
# 		return False

# 	for widget in app.topLevelWidgets():
# 		if isinstance(widget, QtWidgets.QMainWindow) and widget.windowTitle() == window_title:
# 			if widget.isVisible():
# 				print('If the window visible')
# 				return True
# 			else:
# 				print('If the window exists but is not visible, close it')
# 				widget.close()
# 				return False

# 	return False


def isWindowOpen(window_title):
	app = QtWidgets.QApplication.instance()
	if not app:
		return False

	for widget in app.topLevelWidgets():
		if isinstance(widget, QtWidgets.QMainWindow) and widget.windowTitle() == window_title:
			if widget.isVisible():
				return True
			else:
				widget.close()
				return False

	return False


for widget in QtWidgets.QApplication.topLevelWidgets():
    if isinstance(widget, QtWidgets.QMainWindow) and widget.windowTitle() == "FileManager":
        print (widget)


def run_file_manager():
	try:
		importlib.reload(fileManagerCore)

		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])

		# Check if the window is already open
		if isWindowOpen("FileManager"):
			print("FileManager is already open. Bringing it to the front...")
			for widget in QtWidgets.QApplication.topLevelWidgets():
				if isinstance(widget, QtWidgets.QMainWindow) and widget.windowTitle() == "FileManager":
					if widget.isMinimized():
						widget.showNormal()  #... Restore the window if it's minimized
					widget.activateWindow()	#... Activate the window
					widget.raise_() #... Bring the window to the front
					return True

		# Create a new instance of the FileManager window
		file_browser = fileManagerCore.FileManager()
		file_browser.show()
		print("Starting event loop...")
		app.exec_()

	except Exception as e:
		print("Error:", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)


if __name__ == "__main__":
	run_file_manager()
