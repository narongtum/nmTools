from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import os

from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline.file_manager.file_manager_ui import printMe_ui
reload(printMe_ui)

# from function.framework.Qtpy.Qt import QtWidgets, QtCore, QtGui
# from function.framework.Qtpy.Qt.QtWidgets import *


class PrintMeWindow(QtWidgets.QMainWindow,printMe_ui.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setObjectName("myWindow")
		self.setupUi(self)
		self.pushButton.clicked.connect(self.print_me)

	def print_me(self):
		print("printMe\n")






'''

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	fileBrowser = MyFileBrowser()
	fileBrowser.show()
	app.exec_()


'''




if __name__ == "__main__":
	try:
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])
		ui = PrintMeWindow()
		ui.show()
		print("Starting event loop...")
		app.exec_()
		#sys.exit(app.exec_())
		
	except Exception as e:
		print("Error: Error Error", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)


'''
# simple version
if __name__ == '__main__' :
	app = QtWidgets.QApplication.instance()
	ui = PrintMeWindow()
	ui.show()
	app.exec_()

'''	


'''


if __name__ == '__main__':
	#app = QtWidgets.QApplication([])
	app = QtWidgets.QApplication.instance()
	qt_app = PrintMeWindow()
	qt_app.show()
	app.exec_()
'''