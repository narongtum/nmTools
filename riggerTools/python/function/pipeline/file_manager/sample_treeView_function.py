from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from function.pipeline.file_manager.file_manager_ui import sample_treeView_ui



class MyTreeView(sample_treeView_ui.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(MyTreeView, self).__init__()
		self.setupUi(self)
		self.populate()

	def populate(self):
		path = r"D:\Blender"
		model = QtWidgets.QFileSystemModel()
		model.setRootPath((QtCore.QDir.rootPath())) 
		self.treeView.setModel(model)
		self.treeView.setRootIndex(model.index(path))
		self.treeView.setSortingEnabled(True)


if __name__ == "__main__":
	try:
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])

		app.fileBrowser = MyTreeView()
		app.fileBrowser.show()
		print("Starting event loop...")
		app.exec_()

	except Exception as e:
		print("Error:", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)


