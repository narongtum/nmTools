# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileManagerMainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1304, 691)
        MainWindow.setMinimumSize(QSize(1282, 616))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1120, 589))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.drive_label = QLabel(self.centralwidget)
        self.drive_label.setObjectName(u"drive_label")

        self.gridLayout.addWidget(self.drive_label, 0, 0, 1, 1)

        self.project_label = QLabel(self.centralwidget)
        self.project_label.setObjectName(u"project_label")

        self.gridLayout.addWidget(self.project_label, 0, 3, 1, 1)

        self.project_spacer = QSpacerItem(200, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.project_spacer, 0, 5, 1, 1)

        self.project_comboBox = QComboBox(self.centralwidget)
        self.project_comboBox.setObjectName(u"project_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.project_comboBox.sizePolicy().hasHeightForWidth())
        self.project_comboBox.setSizePolicy(sizePolicy1)
        self.project_comboBox.setMinimumSize(QSize(200, 0))
        self.project_comboBox.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.project_comboBox, 0, 4, 1, 1)

        self.drive_comboBox = QComboBox(self.centralwidget)
        self.drive_comboBox.setObjectName(u"drive_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.drive_comboBox.sizePolicy().hasHeightForWidth())
        self.drive_comboBox.setSizePolicy(sizePolicy2)
        self.drive_comboBox.setMaximumSize(QSize(60, 20))

        self.gridLayout.addWidget(self.drive_comboBox, 0, 1, 1, 1)

        self.line_project = QFrame(self.centralwidget)
        self.line_project.setObjectName(u"line_project")
        self.line_project.setFrameShape(QFrame.VLine)
        self.line_project.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_project, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.saveBar_horizontal = QHBoxLayout()
        self.saveBar_horizontal.setObjectName(u"saveBar_horizontal")
        self.horizontalSpacer_2 = QSpacerItem(908, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.saveBar_horizontal.addItem(self.horizontalSpacer_2)

        self.save_BTN = QPushButton(self.centralwidget)
        self.save_BTN.setObjectName(u"save_BTN")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.save_BTN.sizePolicy().hasHeightForWidth())
        self.save_BTN.setSizePolicy(sizePolicy3)
        self.save_BTN.setMinimumSize(QSize(100, 50))

        self.saveBar_horizontal.addWidget(self.save_BTN)


        self.gridLayout_2.addLayout(self.saveBar_horizontal, 3, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.Asset_tab = QWidget()
        self.Asset_tab.setObjectName(u"Asset_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.Asset_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.asset_verticalLayout = QVBoxLayout()
        self.asset_verticalLayout.setObjectName(u"asset_verticalLayout")
        self.asset_filter_horizontalLayout = QHBoxLayout()
        self.asset_filter_horizontalLayout.setObjectName(u"asset_filter_horizontalLayout")
        self.horizontalSpacer = QSpacerItem(180, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.asset_filter_horizontalLayout.addItem(self.horizontalSpacer)

        self.asset_filter_text_label = QLabel(self.Asset_tab)
        self.asset_filter_text_label.setObjectName(u"asset_filter_text_label")
        self.asset_filter_text_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.asset_filter_text_label.sizePolicy().hasHeightForWidth())
        self.asset_filter_text_label.setSizePolicy(sizePolicy1)
        self.asset_filter_text_label.setAlignment(Qt.AlignCenter)

        self.asset_filter_horizontalLayout.addWidget(self.asset_filter_text_label)

        self.asset_filter_lineEdit = QLineEdit(self.Asset_tab)
        self.asset_filter_lineEdit.setObjectName(u"asset_filter_lineEdit")

        self.asset_filter_horizontalLayout.addWidget(self.asset_filter_lineEdit)


        self.asset_verticalLayout.addLayout(self.asset_filter_horizontalLayout)

        self.treeView = QTreeView(self.Asset_tab)
        self.treeView.setObjectName(u"treeView")

        self.asset_verticalLayout.addWidget(self.treeView)


        self.horizontalLayout_2.addLayout(self.asset_verticalLayout)

        self.thmbnail_verticalLayout = QVBoxLayout()
        self.thmbnail_verticalLayout.setObjectName(u"thmbnail_verticalLayout")
        self.thumbnail_label = QLabel(self.Asset_tab)
        self.thumbnail_label.setObjectName(u"thumbnail_label")
        self.thumbnail_label.setAlignment(Qt.AlignCenter)

        self.thmbnail_verticalLayout.addWidget(self.thumbnail_label)

        self.thumbnail_list_listWidget = QListWidget(self.Asset_tab)
        self.thumbnail_list_listWidget.setObjectName(u"thumbnail_list_listWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.thumbnail_list_listWidget.sizePolicy().hasHeightForWidth())
        self.thumbnail_list_listWidget.setSizePolicy(sizePolicy5)

        self.thmbnail_verticalLayout.addWidget(self.thumbnail_list_listWidget)

        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.thmbnail_verticalLayout.addItem(self.verticalSpacer)

        self.AssetInfo_label = QLabel(self.Asset_tab)
        self.AssetInfo_label.setObjectName(u"AssetInfo_label")
        self.AssetInfo_label.setAlignment(Qt.AlignCenter)

        self.thmbnail_verticalLayout.addWidget(self.AssetInfo_label)

        self.assetInfo_list_listWidget = QListWidget(self.Asset_tab)
        self.assetInfo_list_listWidget.setObjectName(u"assetInfo_list_listWidget")
        sizePolicy4.setHeightForWidth(self.assetInfo_list_listWidget.sizePolicy().hasHeightForWidth())
        self.assetInfo_list_listWidget.setSizePolicy(sizePolicy4)

        self.thmbnail_verticalLayout.addWidget(self.assetInfo_list_listWidget)


        self.horizontalLayout_2.addLayout(self.thmbnail_verticalLayout)

        self.departmentLib_verticalLayout = QVBoxLayout()
        self.departmentLib_verticalLayout.setObjectName(u"departmentLib_verticalLayout")
        self.global_label = QLabel(self.Asset_tab)
        self.global_label.setObjectName(u"global_label")
        self.global_label.setAlignment(Qt.AlignCenter)

        self.departmentLib_verticalLayout.addWidget(self.global_label)

        self.global_listWidget = QListWidget(self.Asset_tab)
        self.global_listWidget.setObjectName(u"global_listWidget")
        sizePolicy5.setHeightForWidth(self.global_listWidget.sizePolicy().hasHeightForWidth())
        self.global_listWidget.setSizePolicy(sizePolicy5)

        self.departmentLib_verticalLayout.addWidget(self.global_listWidget)

        self.commit_BTN = QPushButton(self.Asset_tab)
        self.commit_BTN.setObjectName(u"commit_BTN")

        self.departmentLib_verticalLayout.addWidget(self.commit_BTN)

        self.department_label = QLabel(self.Asset_tab)
        self.department_label.setObjectName(u"department_label")
        self.department_label.setAlignment(Qt.AlignCenter)

        self.departmentLib_verticalLayout.addWidget(self.department_label)

        self.department_listWidget = QListWidget(self.Asset_tab)
        self.department_listWidget.setObjectName(u"department_listWidget")
        sizePolicy4.setHeightForWidth(self.department_listWidget.sizePolicy().hasHeightForWidth())
        self.department_listWidget.setSizePolicy(sizePolicy4)

        self.departmentLib_verticalLayout.addWidget(self.department_listWidget)


        self.horizontalLayout_2.addLayout(self.departmentLib_verticalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.local_label = QLabel(self.Asset_tab)
        self.local_label.setObjectName(u"local_label")
        self.local_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.local_label)

        self.local_view_listWidget = QListWidget(self.Asset_tab)
        self.local_view_listWidget.setObjectName(u"local_view_listWidget")
        sizePolicy5.setHeightForWidth(self.local_view_listWidget.sizePolicy().hasHeightForWidth())
        self.local_view_listWidget.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.local_view_listWidget)

        self.localCommit_BTN = QPushButton(self.Asset_tab)
        self.localCommit_BTN.setObjectName(u"localCommit_BTN")

        self.verticalLayout.addWidget(self.localCommit_BTN)

        self.version_label = QLabel(self.Asset_tab)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.version_label)

        self.version_view_listWidget = QListWidget(self.Asset_tab)
        self.version_view_listWidget.setObjectName(u"version_view_listWidget")
        sizePolicy4.setHeightForWidth(self.version_view_listWidget.sizePolicy().hasHeightForWidth())
        self.version_view_listWidget.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.version_view_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.tabWidget.addTab(self.Asset_tab, "")
        self.scene_tab = QWidget()
        self.scene_tab.setObjectName(u"scene_tab")
        self.tableView_2 = QTableView(self.scene_tab)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(0, 10, 811, 421))
        self.tabWidget.addTab(self.scene_tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1304, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FileManager", None))
        self.drive_label.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.save_BTN.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.asset_filter_text_label.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.thumbnail_label.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.AssetInfo_label.setText(QCoreApplication.translate("MainWindow", u"AssetInfo", None))
        self.global_label.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.commit_BTN.setText(QCoreApplication.translate("MainWindow", u"Commit", None))
        self.department_label.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.local_label.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.localCommit_BTN.setText(QCoreApplication.translate("MainWindow", u"Local Publish", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Asset_tab), QCoreApplication.translate("MainWindow", u"Asset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scene_tab), QCoreApplication.translate("MainWindow", u"Scene", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

