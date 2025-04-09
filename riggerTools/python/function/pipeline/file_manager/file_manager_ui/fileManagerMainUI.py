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

PROJECT = ''
VERSION = '0.9.023'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1282, 616)
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
        self.drive_GRID = QGridLayout()
        self.drive_GRID.setObjectName(u"drive_GRID")
        self.drive_GRID.setContentsMargins(5, -1, 5, -1)
        self.drive_label = QLabel(self.centralwidget)
        self.drive_label.setObjectName(u"drive_label")

        self.drive_GRID.addWidget(self.drive_label, 0, 0, 1, 1)

        self.project_label = QLabel(self.centralwidget)
        self.project_label.setObjectName(u"project_label")

        self.drive_GRID.addWidget(self.project_label, 0, 3, 1, 1)

        self.project_spacer = QSpacerItem(200, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.drive_GRID.addItem(self.project_spacer, 0, 5, 1, 1)

        self.project_comboBox = QComboBox(self.centralwidget)
        self.project_comboBox.setObjectName(u"project_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.project_comboBox.sizePolicy().hasHeightForWidth())
        self.project_comboBox.setSizePolicy(sizePolicy1)
        self.project_comboBox.setMinimumSize(QSize(200, 0))
        self.project_comboBox.setMaximumSize(QSize(16777215, 20))

        self.drive_GRID.addWidget(self.project_comboBox, 0, 4, 1, 1)

        self.drive_comboBox = QComboBox(self.centralwidget)
        self.drive_comboBox.setObjectName(u"drive_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.drive_comboBox.sizePolicy().hasHeightForWidth())
        self.drive_comboBox.setSizePolicy(sizePolicy2)
        self.drive_comboBox.setMaximumSize(QSize(60, 20))

        self.drive_GRID.addWidget(self.drive_comboBox, 0, 1, 1, 1)

        self.line_project = QFrame(self.centralwidget)
        self.line_project.setObjectName(u"line_project")
        self.line_project.setFrameShape(QFrame.VLine)
        self.line_project.setFrameShadow(QFrame.Sunken)

        self.drive_GRID.addWidget(self.line_project, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.drive_GRID, 0, 0, 1, 1)

        self.drive_LINE = QFrame(self.centralwidget)
        self.drive_LINE.setObjectName(u"drive_LINE")
        self.drive_LINE.setFrameShape(QFrame.HLine)
        self.drive_LINE.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.drive_LINE, 1, 0, 1, 1)

        self.saveBar_horizontal = QHBoxLayout()
        self.saveBar_horizontal.setObjectName(u"saveBar_horizontal")
        self.save_SPACE = QSpacerItem(908, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.saveBar_horizontal.addItem(self.save_SPACE)


        self.gridLayout_2.addLayout(self.saveBar_horizontal, 3, 0, 1, 1)

        self.entite_TAB = QTabWidget(self.centralwidget)
        self.entite_TAB.setObjectName(u"entite_TAB")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.entite_TAB.sizePolicy().hasHeightForWidth())
        self.entite_TAB.setSizePolicy(sizePolicy3)
        self.asset_TAB = QWidget()
        self.asset_TAB.setObjectName(u"asset_TAB")
        self.horizontalLayout_2 = QHBoxLayout(self.asset_TAB)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.asset_verticalLayout = QVBoxLayout()
        self.asset_verticalLayout.setObjectName(u"asset_verticalLayout")
        self.asset_filter_horizontalLayout = QHBoxLayout()
        self.asset_filter_horizontalLayout.setObjectName(u"asset_filter_horizontalLayout")
        self.horizontalSpacer = QSpacerItem(180, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.asset_filter_horizontalLayout.addItem(self.horizontalSpacer)

        self.asset_filter_text_label = QLabel(self.asset_TAB)
        self.asset_filter_text_label.setObjectName(u"asset_filter_text_label")
        self.asset_filter_text_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.asset_filter_text_label.sizePolicy().hasHeightForWidth())
        self.asset_filter_text_label.setSizePolicy(sizePolicy1)
        self.asset_filter_text_label.setAlignment(Qt.AlignCenter)

        self.asset_filter_horizontalLayout.addWidget(self.asset_filter_text_label)

        self.asset_filter_lineEdit = QLineEdit(self.asset_TAB)
        self.asset_filter_lineEdit.setObjectName(u"asset_filter_lineEdit")

        self.asset_filter_horizontalLayout.addWidget(self.asset_filter_lineEdit)


        self.asset_verticalLayout.addLayout(self.asset_filter_horizontalLayout)

        self.asset_dir_TREEVIEW = QTreeView(self.asset_TAB)
        self.asset_dir_TREEVIEW.setObjectName(u"asset_dir_TREEVIEW")

        self.asset_verticalLayout.addWidget(self.asset_dir_TREEVIEW)


        self.horizontalLayout_2.addLayout(self.asset_verticalLayout)

        self.asset_thumbnail_VTL = QVBoxLayout()
        self.asset_thumbnail_VTL.setObjectName(u"asset_thumbnail_VTL")
        self.asset_thumbnail_label = QLabel(self.asset_TAB)
        self.asset_thumbnail_label.setObjectName(u"asset_thumbnail_label")
        self.asset_thumbnail_label.setAlignment(Qt.AlignCenter)

        self.asset_thumbnail_VTL.addWidget(self.asset_thumbnail_label)

        self.asset_thumbnail_IMAGE_LABEL = QLabel(self.asset_TAB)
        self.asset_thumbnail_IMAGE_LABEL.setObjectName(u"asset_thumbnail_IMAGE_LABEL")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.asset_thumbnail_IMAGE_LABEL.sizePolicy().hasHeightForWidth())
        self.asset_thumbnail_IMAGE_LABEL.setSizePolicy(sizePolicy4)
        self.asset_thumbnail_IMAGE_LABEL.setMinimumSize(QSize(168, 168))
        self.asset_thumbnail_IMAGE_LABEL.setMaximumSize(QSize(168, 168))
        self.asset_thumbnail_IMAGE_LABEL.setFrameShape(QFrame.WinPanel)
        self.asset_thumbnail_IMAGE_LABEL.setFrameShadow(QFrame.Sunken)
        self.asset_thumbnail_IMAGE_LABEL.setAlignment(Qt.AlignCenter)

        self.asset_thumbnail_VTL.addWidget(self.asset_thumbnail_IMAGE_LABEL)

        self.verticalSpacer_SPACE = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.asset_thumbnail_VTL.addItem(self.verticalSpacer_SPACE)

        self.AssetInfo_label = QLabel(self.asset_TAB)
        self.AssetInfo_label.setObjectName(u"AssetInfo_label")
        self.AssetInfo_label.setAlignment(Qt.AlignCenter)

        self.asset_thumbnail_VTL.addWidget(self.AssetInfo_label)

        self.assetInfo_list_listWidget = QListWidget(self.asset_TAB)
        self.assetInfo_list_listWidget.setObjectName(u"assetInfo_list_listWidget")
        sizePolicy3.setHeightForWidth(self.assetInfo_list_listWidget.sizePolicy().hasHeightForWidth())
        self.assetInfo_list_listWidget.setSizePolicy(sizePolicy3)

        self.asset_thumbnail_VTL.addWidget(self.assetInfo_list_listWidget)


        self.horizontalLayout_2.addLayout(self.asset_thumbnail_VTL)

        self.asset_level_global_VTL = QVBoxLayout()
        self.asset_level_global_VTL.setObjectName(u"asset_level_global_VTL")
        self.asset_global_label = QLabel(self.asset_TAB)
        self.asset_global_label.setObjectName(u"asset_global_label")
        self.asset_global_label.setAlignment(Qt.AlignCenter)

        self.asset_level_global_VTL.addWidget(self.asset_global_label)

        self.asset_global_listWidget = QListWidget(self.asset_TAB)
        self.asset_global_listWidget.setObjectName(u"asset_global_listWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.asset_global_listWidget.sizePolicy().hasHeightForWidth())
        self.asset_global_listWidget.setSizePolicy(sizePolicy5)

        self.asset_level_global_VTL.addWidget(self.asset_global_listWidget)

        self.asset_commit_BTN = QPushButton(self.asset_TAB)
        self.asset_commit_BTN.setObjectName(u"asset_commit_BTN")

        self.asset_level_global_VTL.addWidget(self.asset_commit_BTN)

        self.asset_department_label = QLabel(self.asset_TAB)
        self.asset_department_label.setObjectName(u"asset_department_label")
        self.asset_department_label.setAlignment(Qt.AlignCenter)

        self.asset_level_global_VTL.addWidget(self.asset_department_label)

        self.asset_department_listWidget = QListWidget(self.asset_TAB)
        self.asset_department_listWidget.setObjectName(u"asset_department_listWidget")
        sizePolicy3.setHeightForWidth(self.asset_department_listWidget.sizePolicy().hasHeightForWidth())
        self.asset_department_listWidget.setSizePolicy(sizePolicy3)

        self.asset_level_global_VTL.addWidget(self.asset_department_listWidget)


        self.horizontalLayout_2.addLayout(self.asset_level_global_VTL)

        self.asset_level_local_VTL = QVBoxLayout()
        self.asset_level_local_VTL.setObjectName(u"asset_level_local_VTL")
        self.asset_local_label = QLabel(self.asset_TAB)
        self.asset_local_label.setObjectName(u"asset_local_label")
        self.asset_local_label.setAlignment(Qt.AlignCenter)

        self.asset_level_local_VTL.addWidget(self.asset_local_label)

        self.asset_local_view_listWidget = QListWidget(self.asset_TAB)
        self.asset_local_view_listWidget.setObjectName(u"asset_local_view_listWidget")
        sizePolicy5.setHeightForWidth(self.asset_local_view_listWidget.sizePolicy().hasHeightForWidth())
        self.asset_local_view_listWidget.setSizePolicy(sizePolicy5)

        self.asset_level_local_VTL.addWidget(self.asset_local_view_listWidget)

        self.asset_localCommit_BTN = QPushButton(self.asset_TAB)
        self.asset_localCommit_BTN.setObjectName(u"asset_localCommit_BTN")

        self.asset_level_local_VTL.addWidget(self.asset_localCommit_BTN)

        self.asset_version_label = QLabel(self.asset_TAB)
        self.asset_version_label.setObjectName(u"asset_version_label")
        self.asset_version_label.setAlignment(Qt.AlignCenter)

        self.asset_level_local_VTL.addWidget(self.asset_version_label)

        self.asset_version_view_listWidget = QListWidget(self.asset_TAB)
        self.asset_version_view_listWidget.setObjectName(u"asset_version_view_listWidget")
        sizePolicy3.setHeightForWidth(self.asset_version_view_listWidget.sizePolicy().hasHeightForWidth())
        self.asset_version_view_listWidget.setSizePolicy(sizePolicy3)

        self.asset_level_local_VTL.addWidget(self.asset_version_view_listWidget)


        self.horizontalLayout_2.addLayout(self.asset_level_local_VTL)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.entite_TAB.addTab(self.asset_TAB, "")
        self.scene_TAB = QWidget()
        self.scene_TAB.setObjectName(u"scene_TAB")
        self.horizontalLayout_4 = QHBoxLayout(self.scene_TAB)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scene_VTL = QHBoxLayout()
        self.scene_VTL.setObjectName(u"scene_VTL")
        self.scene_verticalLayout = QVBoxLayout()
        self.scene_verticalLayout.setObjectName(u"scene_verticalLayout")
        self.scene_filter_HTL = QHBoxLayout()
        self.scene_filter_HTL.setObjectName(u"scene_filter_HTL")
        self.scene_horizontal_SPACE = QSpacerItem(180, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.scene_filter_HTL.addItem(self.scene_horizontal_SPACE)

        self.scene_filter_text_LABEL = QLabel(self.scene_TAB)
        self.scene_filter_text_LABEL.setObjectName(u"scene_filter_text_LABEL")
        self.scene_filter_text_LABEL.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.scene_filter_text_LABEL.sizePolicy().hasHeightForWidth())
        self.scene_filter_text_LABEL.setSizePolicy(sizePolicy1)
        self.scene_filter_text_LABEL.setAlignment(Qt.AlignCenter)

        self.scene_filter_HTL.addWidget(self.scene_filter_text_LABEL)

        self.scene_filter_LINEEDIT = QLineEdit(self.scene_TAB)
        self.scene_filter_LINEEDIT.setObjectName(u"scene_filter_LINEEDIT")

        self.scene_filter_HTL.addWidget(self.scene_filter_LINEEDIT)


        self.scene_verticalLayout.addLayout(self.scene_filter_HTL)

        self.dir_scene_TREEVIEW = QTreeView(self.scene_TAB)
        self.dir_scene_TREEVIEW.setObjectName(u"dir_scene_TREEVIEW")

        self.scene_verticalLayout.addWidget(self.dir_scene_TREEVIEW)


        self.scene_VTL.addLayout(self.scene_verticalLayout)

        self.scene_thmbnail_VTL = QVBoxLayout()
        self.scene_thmbnail_VTL.setObjectName(u"scene_thmbnail_VTL")
        self.scene_thumbnail_label = QLabel(self.scene_TAB)
        self.scene_thumbnail_label.setObjectName(u"scene_thumbnail_label")
        self.scene_thumbnail_label.setAlignment(Qt.AlignCenter)

        self.scene_thmbnail_VTL.addWidget(self.scene_thumbnail_label)

        self.scene_thumbnail_IMAGE_LABEL = QLabel(self.scene_TAB)
        self.scene_thumbnail_IMAGE_LABEL.setObjectName(u"scene_thumbnail_IMAGE_LABEL")
        sizePolicy4.setHeightForWidth(self.scene_thumbnail_IMAGE_LABEL.sizePolicy().hasHeightForWidth())
        self.scene_thumbnail_IMAGE_LABEL.setSizePolicy(sizePolicy4)
        self.scene_thumbnail_IMAGE_LABEL.setMinimumSize(QSize(168, 168))
        self.scene_thumbnail_IMAGE_LABEL.setMaximumSize(QSize(168, 168))
        self.scene_thumbnail_IMAGE_LABEL.setLayoutDirection(Qt.LeftToRight)
        self.scene_thumbnail_IMAGE_LABEL.setFrameShape(QFrame.WinPanel)
        self.scene_thumbnail_IMAGE_LABEL.setFrameShadow(QFrame.Sunken)
        self.scene_thumbnail_IMAGE_LABEL.setAlignment(Qt.AlignCenter)

        self.scene_thmbnail_VTL.addWidget(self.scene_thumbnail_IMAGE_LABEL)

        self.scene_verticalSpacer_SPACE = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.scene_thmbnail_VTL.addItem(self.scene_verticalSpacer_SPACE)

        self.scene_AssetInfo_label = QLabel(self.scene_TAB)
        self.scene_AssetInfo_label.setObjectName(u"scene_AssetInfo_label")
        self.scene_AssetInfo_label.setAlignment(Qt.AlignCenter)

        self.scene_thmbnail_VTL.addWidget(self.scene_AssetInfo_label)

        self.scene_Info_list_LISTWIDGET = QListWidget(self.scene_TAB)
        self.scene_Info_list_LISTWIDGET.setObjectName(u"scene_Info_list_LISTWIDGET")
        sizePolicy3.setHeightForWidth(self.scene_Info_list_LISTWIDGET.sizePolicy().hasHeightForWidth())
        self.scene_Info_list_LISTWIDGET.setSizePolicy(sizePolicy3)

        self.scene_thmbnail_VTL.addWidget(self.scene_Info_list_LISTWIDGET)


        self.scene_VTL.addLayout(self.scene_thmbnail_VTL)

        self.scene_departmentLib_VTL = QVBoxLayout()
        self.scene_departmentLib_VTL.setObjectName(u"scene_departmentLib_VTL")
        self.scene_global_label = QLabel(self.scene_TAB)
        self.scene_global_label.setObjectName(u"scene_global_label")
        self.scene_global_label.setAlignment(Qt.AlignCenter)

        self.scene_departmentLib_VTL.addWidget(self.scene_global_label)

        self.scene_global_listWidget = QListWidget(self.scene_TAB)
        self.scene_global_listWidget.setObjectName(u"scene_global_listWidget")
        sizePolicy5.setHeightForWidth(self.scene_global_listWidget.sizePolicy().hasHeightForWidth())
        self.scene_global_listWidget.setSizePolicy(sizePolicy5)

        self.scene_departmentLib_VTL.addWidget(self.scene_global_listWidget)

        self.scene_commit_BTN = QPushButton(self.scene_TAB)
        self.scene_commit_BTN.setObjectName(u"scene_commit_BTN")

        self.scene_departmentLib_VTL.addWidget(self.scene_commit_BTN)

        self.scene_department_label = QLabel(self.scene_TAB)
        self.scene_department_label.setObjectName(u"scene_department_label")
        self.scene_department_label.setAlignment(Qt.AlignCenter)

        self.scene_departmentLib_VTL.addWidget(self.scene_department_label)

        self.scene_department_listWidget = QListWidget(self.scene_TAB)
        self.scene_department_listWidget.setObjectName(u"scene_department_listWidget")
        sizePolicy3.setHeightForWidth(self.scene_department_listWidget.sizePolicy().hasHeightForWidth())
        self.scene_department_listWidget.setSizePolicy(sizePolicy3)

        self.scene_departmentLib_VTL.addWidget(self.scene_department_listWidget)


        self.scene_VTL.addLayout(self.scene_departmentLib_VTL)

        self.scene_locallib_VTL = QVBoxLayout()
        self.scene_locallib_VTL.setObjectName(u"scene_locallib_VTL")
        self.scene_local_TXT = QLabel(self.scene_TAB)
        self.scene_local_TXT.setObjectName(u"scene_local_TXT")
        self.scene_local_TXT.setAlignment(Qt.AlignCenter)

        self.scene_locallib_VTL.addWidget(self.scene_local_TXT)

        self.scene_local_view_listWidget = QListWidget(self.scene_TAB)
        self.scene_local_view_listWidget.setObjectName(u"scene_local_view_listWidget")
        sizePolicy5.setHeightForWidth(self.scene_local_view_listWidget.sizePolicy().hasHeightForWidth())
        self.scene_local_view_listWidget.setSizePolicy(sizePolicy5)

        self.scene_locallib_VTL.addWidget(self.scene_local_view_listWidget)

        self.scene_localCommit_BTN = QPushButton(self.scene_TAB)
        self.scene_localCommit_BTN.setObjectName(u"scene_localCommit_BTN")

        self.scene_locallib_VTL.addWidget(self.scene_localCommit_BTN)

        self.scene_version_label_TXT = QLabel(self.scene_TAB)
        self.scene_version_label_TXT.setObjectName(u"scene_version_label_TXT")
        self.scene_version_label_TXT.setAlignment(Qt.AlignCenter)

        self.scene_locallib_VTL.addWidget(self.scene_version_label_TXT)

        self.scene_version_view_listWidget = QListWidget(self.scene_TAB)
        self.scene_version_view_listWidget.setObjectName(u"scene_version_view_listWidget")
        sizePolicy3.setHeightForWidth(self.scene_version_view_listWidget.sizePolicy().hasHeightForWidth())
        self.scene_version_view_listWidget.setSizePolicy(sizePolicy3)

        self.scene_locallib_VTL.addWidget(self.scene_version_view_listWidget)


        self.scene_VTL.addLayout(self.scene_locallib_VTL)

        self.scene_VTL.setStretch(0, 3)
        self.scene_VTL.setStretch(1, 1)
        self.scene_VTL.setStretch(2, 1)
        self.scene_VTL.setStretch(3, 2)

        self.horizontalLayout_4.addLayout(self.scene_VTL)

        self.entite_TAB.addTab(self.scene_TAB, "")

        self.gridLayout_2.addWidget(self.entite_TAB, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1282, 21))
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

        self.entite_TAB.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"nmFileManager 0.9.023", None))
        self.drive_label.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.asset_filter_text_label.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.asset_thumbnail_label.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.asset_thumbnail_IMAGE_LABEL.setText("")
        self.AssetInfo_label.setText(QCoreApplication.translate("MainWindow", u"Asset Info", None))
        self.asset_global_label.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.asset_commit_BTN.setText(QCoreApplication.translate("MainWindow", u"Commit", None))
        self.asset_department_label.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.asset_local_label.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.asset_localCommit_BTN.setText(QCoreApplication.translate("MainWindow", u"Local Publish", None))
        self.asset_version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.entite_TAB.setTabText(self.entite_TAB.indexOf(self.asset_TAB), QCoreApplication.translate("MainWindow", u"Asset", None))
        self.scene_filter_text_LABEL.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.scene_thumbnail_label.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.scene_thumbnail_IMAGE_LABEL.setText(QCoreApplication.translate("MainWindow", u"no image show", None))
        self.scene_AssetInfo_label.setText(QCoreApplication.translate("MainWindow", u"Shot Info", None))
        self.scene_global_label.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.scene_commit_BTN.setText(QCoreApplication.translate("MainWindow", u"Commit", None))
        self.scene_department_label.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.scene_local_TXT.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.scene_localCommit_BTN.setText(QCoreApplication.translate("MainWindow", u"Local Publish", None))
        self.scene_version_label_TXT.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.entite_TAB.setTabText(self.entite_TAB.indexOf(self.scene_TAB), QCoreApplication.translate("MainWindow", u"Scene", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

