from PySide2 import QtWidgets, QtCore

"""
This is sucess filter model
"""

#DRIVE = "E:/"
DRIVE = "D:/svn_true/P_Regulus"
class FilterProxyModel(QtCore.QSortFilterProxyModel):
	def __init__(self, parent=None):
		super(FilterProxyModel, self).__init__(parent)
		self._pattern = ""

	@property
	def pattern(self):
		return self._pattern

	@pattern.setter
	def pattern(self, value):
		self._pattern = value
		self.invalidateFilter()

	def filterAcceptsRow(self, sourceRow, sourceParent):
		if not self.pattern:
			return True

		sourceModel = self.sourceModel()
		index = sourceModel.index(sourceRow, 0, sourceParent)
		filePath = sourceModel.filePath(index)
		fileName = sourceModel.fileName(index)

		if self.pattern.lower() in fileName.lower():
			return True

		if sourceModel.isDir(index):
			childCount = sourceModel.rowCount(index)
			for i in range(childCount):
				if self.filterAcceptsRow(i, index):
					return True

		return False


class MyTreeView(QtWidgets.QMainWindow):
	def __init__(self):
		super(MyTreeView, self).__init__()

		self.lineEdit = QtWidgets.QLineEdit()
		self.lineEdit.setPlaceholderText('Search...')
		self.lineEdit.textChanged.connect(self.filter_model)

		self.model = QtWidgets.QFileSystemModel()
		self.model.setRootPath(DRIVE)

		self.proxyModel = FilterProxyModel()
		self.proxyModel.setSourceModel(self.model)

		self.treeView = QtWidgets.QTreeView()
		self.treeView.setModel(self.proxyModel)
		self.treeView.setRootIndex(self.proxyModel.mapFromSource(self.model.index(DRIVE)))
		self.treeView.setSortingEnabled(True)

		central_widget = QtWidgets.QWidget()
		layout = QtWidgets.QVBoxLayout(central_widget)
		layout.addWidget(self.lineEdit)
		layout.addWidget(self.treeView)
		self.setCentralWidget(central_widget)

	def filter_model(self, text):
		self.proxyModel.pattern = text


if __name__ == "__main__":
	try:
		app = QtWidgets.QApplication.instance()
		if not app:
			app = QtWidgets.QApplication([])
		# it make Maya change color style
		#app.setStyle('Fusion')
		fileBrowser = MyTreeView()
		fileBrowser.show()
		print("Starting event loop...")
		app.exec_()

	except Exception as e:
		print("Error:", e)
		import traceback
		traceback.print_exc()
		sys.exit(-1)

"""
In this updated code, we create a custom FilterProxyModel that inherits from QSortFilterProxyModel. The FilterProxyModel overrides the filterAcceptsRow method to implement the filtering logic. 

It checks if the pattern (text entered in the QLineEdit) is present in the file or directory name and recursively checks child items.

In the MyTreeView class, we create an instance of FilterProxyModel and set it as the proxy model for the QTreeView. The textChanged signal of the QLineEdit is connected to the filter_model method, 

which updates the pattern in the proxy model, triggering the filtering.

Now, when you enter text in the QLineEdit, the tree view will filter and show only the items matching the entered text.
"""