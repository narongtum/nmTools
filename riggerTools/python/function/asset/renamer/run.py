from function.asset.renamer import nomanRenamer_ui_GPT as nomanRenamer_ui
reload(nomanRenamer_ui)



from function.framework.Qtpy.Qt import QtCore, QtGui, QtWidgets


def runSiWa():
	Form = QtWidgets.QWidget()
	ui = nomanRenamer_ui.Ui_ReNameUi()
	ui.setupUi(Form)
	Form.show()


def runApp():
	if __name__ == "__main__":
		import sys
		# app = QtWidgets.QApplication.instance()
		#app = QtWidgets.QApplication(sys.argv)
		Form = QtWidgets.QWidget()
		ui = nomanRenamer_ui.Ui_ReNameUi()
		ui.setupUi(Form)
		Form.show()
		# sys.exit(app.exec_())



'''
from function.asset.renamer import run
reload(run)

run.runApp()
'''