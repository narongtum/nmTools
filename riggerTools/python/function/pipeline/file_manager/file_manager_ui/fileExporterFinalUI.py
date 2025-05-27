# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileExporterFinal.ui'
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
        MainWindow.resize(1090, 280)
        MainWindow.setMinimumSize(QSize(760, 280))
        MainWindow.setMaximumSize(QSize(5700, 3660))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.separater_1_line = QFrame(self.centralwidget)
        self.separater_1_line.setObjectName(u"separater_1_line")
        self.separater_1_line.setFrameShape(QFrame.HLine)
        self.separater_1_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.separater_1_line, 2, 0, 1, 1)

        self.separater_2_line = QFrame(self.centralwidget)
        self.separater_2_line.setObjectName(u"separater_2_line")
        self.separater_2_line.setFrameShape(QFrame.HLine)
        self.separater_2_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.separater_2_line, 4, 0, 1, 1)

        self.getAsset_gridLayout = QGridLayout()
        self.getAsset_gridLayout.setSpacing(0)
        self.getAsset_gridLayout.setObjectName(u"getAsset_gridLayout")
        self.getAsset_gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.getAsset_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.getAsset_1_horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.getAsset_gridLayout.addItem(self.getAsset_1_horizontalSpacer, 0, 8, 1, 1)

        self.input_path_lineEdit = QLineEdit(self.centralwidget)
        self.input_path_lineEdit.setObjectName(u"input_path_lineEdit")

        self.getAsset_gridLayout.addWidget(self.input_path_lineEdit, 0, 5, 1, 1)

        self.previous_text_label = QLabel(self.centralwidget)
        self.previous_text_label.setObjectName(u"previous_text_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_text_label.sizePolicy().hasHeightForWidth())
        self.previous_text_label.setSizePolicy(sizePolicy)
        self.previous_text_label.setMinimumSize(QSize(90, 0))

        self.getAsset_gridLayout.addWidget(self.previous_text_label, 0, 4, 1, 1)

        self.getAsset_pushButton = QPushButton(self.centralwidget)
        self.getAsset_pushButton.setObjectName(u"getAsset_pushButton")

        self.getAsset_gridLayout.addWidget(self.getAsset_pushButton, 0, 1, 1, 1)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setVisible(False)

        self.getAsset_gridLayout.addWidget(self.toolButton, 0, 2, 1, 1)

        self.getAsset_2_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.getAsset_gridLayout.addItem(self.getAsset_2_horizontalSpacer, 0, 0, 1, 1)

        self.getAsset_3_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.getAsset_gridLayout.addItem(self.getAsset_3_horizontalSpacer, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setVisible(False)

        self.getAsset_gridLayout.addWidget(self.pushButton, 0, 7, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.getAsset_gridLayout.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.getAsset_gridLayout.setColumnStretch(0, 1)

        self.gridLayout_2.addLayout(self.getAsset_gridLayout, 1, 0, 1, 1)

        self.export_horizontalLayout = QHBoxLayout()
        self.export_horizontalLayout.setObjectName(u"export_horizontalLayout")
        self.add_pushButton = QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.export_horizontalLayout.addWidget(self.add_pushButton)

        self.commit_pushButton = QPushButton(self.centralwidget)
        self.commit_pushButton.setObjectName(u"commit_pushButton")

        self.export_horizontalLayout.addWidget(self.commit_pushButton)

        self.export_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.export_horizontalLayout.addItem(self.export_horizontalSpacer)


        self.gridLayout_2.addLayout(self.export_horizontalLayout, 5, 0, 1, 1)

        self.body_gridLayout = QGridLayout()
        self.body_gridLayout.setObjectName(u"body_gridLayout")
        self.body_gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.export_2_pushButton = QPushButton(self.centralwidget)
        self.export_2_pushButton.setObjectName(u"export_2_pushButton")

        self.body_gridLayout.addWidget(self.export_2_pushButton, 1, 9, 1, 1)

        self.export_name_01_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.body_gridLayout.addItem(self.export_name_01_horizontalSpacer, 0, 10, 1, 1)

        self.export_1_pushButton = QPushButton(self.centralwidget)
        self.export_1_pushButton.setObjectName(u"export_1_pushButton")

        self.body_gridLayout.addWidget(self.export_1_pushButton, 0, 9, 1, 1)

        self.text_result_01_lineEdit = QLineEdit(self.centralwidget)
        self.text_result_01_lineEdit.setObjectName(u"text_result_01_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_result_01_lineEdit.sizePolicy().hasHeightForWidth())
        self.text_result_01_lineEdit.setSizePolicy(sizePolicy1)
        self.text_result_01_lineEdit.setMinimumSize(QSize(180, 0))

        self.body_gridLayout.addWidget(self.text_result_01_lineEdit, 0, 8, 1, 1)

        self.replace_01_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.body_gridLayout.addItem(self.replace_01_horizontalSpacer, 0, 3, 1, 1)

        self.text_with_01_lineEdit = QLineEdit(self.centralwidget)
        self.text_with_01_lineEdit.setObjectName(u"text_with_01_lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_with_01_lineEdit.sizePolicy().hasHeightForWidth())
        self.text_with_01_lineEdit.setSizePolicy(sizePolicy2)
        self.text_with_01_lineEdit.setMinimumSize(QSize(80, 0))
        self.text_with_01_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.body_gridLayout.addWidget(self.text_with_01_lineEdit, 0, 5, 1, 1)

        self.with_01_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.body_gridLayout.addItem(self.with_01_horizontalSpacer, 0, 6, 1, 1)

        self.export_replace_02_label = QLabel(self.centralwidget)
        self.export_replace_02_label.setObjectName(u"export_replace_02_label")

        self.body_gridLayout.addWidget(self.export_replace_02_label, 1, 1, 1, 1)

        self.export_with_02_label = QLabel(self.centralwidget)
        self.export_with_02_label.setObjectName(u"export_with_02_label")

        self.body_gridLayout.addWidget(self.export_with_02_label, 1, 4, 1, 1)

        self.export_with_01_label = QLabel(self.centralwidget)
        self.export_with_01_label.setObjectName(u"export_with_01_label")

        self.body_gridLayout.addWidget(self.export_with_01_label, 0, 4, 1, 1)

        self.export_result_01_label = QLabel(self.centralwidget)
        self.export_result_01_label.setObjectName(u"export_result_01_label")

        self.body_gridLayout.addWidget(self.export_result_01_label, 0, 7, 1, 1)

        self.export_result_02_label = QLabel(self.centralwidget)
        self.export_result_02_label.setObjectName(u"export_result_02_label")

        self.body_gridLayout.addWidget(self.export_result_02_label, 1, 7, 1, 1)

        self.asset_2_checkBox = QCheckBox(self.centralwidget)
        self.asset_2_checkBox.setObjectName(u"asset_2_checkBox")

        self.body_gridLayout.addWidget(self.asset_2_checkBox, 1, 0, 1, 1)

        self.text_replace_02_lineEdit = QLineEdit(self.centralwidget)
        self.text_replace_02_lineEdit.setObjectName(u"text_replace_02_lineEdit")
        sizePolicy2.setHeightForWidth(self.text_replace_02_lineEdit.sizePolicy().hasHeightForWidth())
        self.text_replace_02_lineEdit.setSizePolicy(sizePolicy2)
        self.text_replace_02_lineEdit.setMinimumSize(QSize(80, 0))
        self.text_replace_02_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.body_gridLayout.addWidget(self.text_replace_02_lineEdit, 1, 2, 1, 1)

        self.export_replace_01_label = QLabel(self.centralwidget)
        self.export_replace_01_label.setObjectName(u"export_replace_01_label")

        self.body_gridLayout.addWidget(self.export_replace_01_label, 0, 1, 1, 1)

        self.asset_1_checkBox = QCheckBox(self.centralwidget)
        self.asset_1_checkBox.setObjectName(u"asset_1_checkBox")

        self.body_gridLayout.addWidget(self.asset_1_checkBox, 0, 0, 1, 1)

        self.text_replace_01_lineEdit = QLineEdit(self.centralwidget)
        self.text_replace_01_lineEdit.setObjectName(u"text_replace_01_lineEdit")
        sizePolicy2.setHeightForWidth(self.text_replace_01_lineEdit.sizePolicy().hasHeightForWidth())
        self.text_replace_01_lineEdit.setSizePolicy(sizePolicy2)
        self.text_replace_01_lineEdit.setMinimumSize(QSize(80, 0))
        self.text_replace_01_lineEdit.setMaximumSize(QSize(120, 20))

        self.body_gridLayout.addWidget(self.text_replace_01_lineEdit, 0, 2, 1, 1)

        self.text_with_02_lineEdit = QLineEdit(self.centralwidget)
        self.text_with_02_lineEdit.setObjectName(u"text_with_02_lineEdit")
        sizePolicy2.setHeightForWidth(self.text_with_02_lineEdit.sizePolicy().hasHeightForWidth())
        self.text_with_02_lineEdit.setSizePolicy(sizePolicy2)
        self.text_with_02_lineEdit.setMinimumSize(QSize(80, 0))
        self.text_with_02_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.body_gridLayout.addWidget(self.text_with_02_lineEdit, 1, 5, 1, 1)

        self.replace_02_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.body_gridLayout.addItem(self.replace_02_horizontalSpacer, 1, 3, 1, 1)

        self.with_02_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.body_gridLayout.addItem(self.with_02_horizontalSpacer, 1, 6, 1, 1)

        self.text_result_02_lineEdit = QLineEdit(self.centralwidget)
        self.text_result_02_lineEdit.setObjectName(u"text_result_02_lineEdit")
        sizePolicy1.setHeightForWidth(self.text_result_02_lineEdit.sizePolicy().hasHeightForWidth())
        self.text_result_02_lineEdit.setSizePolicy(sizePolicy1)
        self.text_result_02_lineEdit.setMinimumSize(QSize(180, 0))

        self.body_gridLayout.addWidget(self.text_result_02_lineEdit, 1, 8, 1, 1)

        self.export_name_02_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.body_gridLayout.addItem(self.export_name_02_horizontalSpacer, 1, 10, 1, 1)


        self.gridLayout_2.addLayout(self.body_gridLayout, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.drive_label = QLabel(self.centralwidget)
        self.drive_label.setObjectName(u"drive_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.drive_label.sizePolicy().hasHeightForWidth())
        self.drive_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.drive_label)

        self.drive_comboBox = QComboBox(self.centralwidget)
        self.drive_comboBox.setObjectName(u"drive_comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.drive_comboBox.sizePolicy().hasHeightForWidth())
        self.drive_comboBox.setSizePolicy(sizePolicy4)
        self.drive_comboBox.setMaximumSize(QSize(60, 20))

        self.horizontalLayout.addWidget(self.drive_comboBox)

        self.line_project = QFrame(self.centralwidget)
        self.line_project.setObjectName(u"line_project")
        self.line_project.setFrameShape(QFrame.VLine)
        self.line_project.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_project)

        self.project_label = QLabel(self.centralwidget)
        self.project_label.setObjectName(u"project_label")
        sizePolicy.setHeightForWidth(self.project_label.sizePolicy().hasHeightForWidth())
        self.project_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.project_label)

        self.project_comboBox = QComboBox(self.centralwidget)
        self.project_comboBox.setObjectName(u"project_comboBox")
        sizePolicy3.setHeightForWidth(self.project_comboBox.sizePolicy().hasHeightForWidth())
        self.project_comboBox.setSizePolicy(sizePolicy3)
        self.project_comboBox.setMinimumSize(QSize(200, 0))
        self.project_comboBox.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.project_comboBox)

        self.project_spacer = QSpacerItem(500, 17, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.project_spacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.empty_verticalLayout = QVBoxLayout()
        self.empty_verticalLayout.setObjectName(u"empty_verticalLayout")
        self.empty_verticalSpacer = QSpacerItem(20, 220, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.empty_verticalLayout.addItem(self.empty_verticalSpacer)


        self.gridLayout_2.addLayout(self.empty_verticalLayout, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HeroExporter 0.0.001", None))
        self.previous_text_label.setText(QCoreApplication.translate("MainWindow", u"Previous Name", None))
        self.getAsset_pushButton.setText(QCoreApplication.translate("MainWindow", u"Get Asset", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.add_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.commit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Commit", None))
        self.export_2_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.export_1_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.export_replace_02_label.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.export_with_02_label.setText(QCoreApplication.translate("MainWindow", u"With", None))
        self.export_with_01_label.setText(QCoreApplication.translate("MainWindow", u"With", None))
        self.export_result_01_label.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.export_result_02_label.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.asset_2_checkBox.setText(QCoreApplication.translate("MainWindow", u"File Type 2", None))
        self.export_replace_01_label.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.asset_1_checkBox.setText(QCoreApplication.translate("MainWindow", u"File Type1", None))
        self.drive_label.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Project", None))
    # retranslateUi

