# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'printMe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# from function.framework.Qtpy.Qt.QtWidgets import *
# from function.framework.Qtpy.Qt import QtWidgets, QtCore, QtGui

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		if not MainWindow.objectName():
			MainWindow.setObjectName(u"MainWindow")
		MainWindow.resize(342, 318)
		# self.centralwidget = QtWidgets(MainWindow)
		self.centralwidget = QWidget(MainWindow)

		self.centralwidget.setObjectName(u"centralwidget")
		self.horizontalLayout = QHBoxLayout(self.centralwidget)
		self.horizontalLayout.setObjectName(u"horizontalLayout")

		self.centralwidget.setObjectName(u"myWindow")
		MainWindow.setObjectName(u"myWindow")

		self.gridLayout = QGridLayout()
		self.gridLayout.setObjectName(u"gridLayout")
		self.pushButton = QPushButton(self.centralwidget)
		self.pushButton.setObjectName(u"pushButton")
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy)

		self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


		self.horizontalLayout.addLayout(self.gridLayout)

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(MainWindow)
		self.menubar.setObjectName(u"menubar")
		self.menubar.setGeometry(QRect(0, 0, 342, 21))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(MainWindow)
		self.statusbar.setObjectName(u"statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)

		QMetaObject.connectSlotsByName(MainWindow)
	# setupUi

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
		self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PrintMe", None))
	# retranslateUi

