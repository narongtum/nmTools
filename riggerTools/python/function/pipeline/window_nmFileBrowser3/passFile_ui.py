# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passFileUi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_passFileDialog(object):
    def setupUi(self, passFileDialog):
        if not passFileDialog.objectName():
            passFileDialog.setObjectName(u"passFileDialog")
        passFileDialog.setWindowModality(Qt.WindowModal)
        passFileDialog.resize(238, 146)
        self.passFileVerticalLayout = QVBoxLayout(passFileDialog)
        self.passFileVerticalLayout.setSpacing(2)
        self.passFileVerticalLayout.setContentsMargins(2, 2, 2, 2)
        self.passFileVerticalLayout.setObjectName(u"passFileVerticalLayout")
        self.mainVerticalLayout = QVBoxLayout()
        self.mainVerticalLayout.setSpacing(0)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.jobHorizontalLayout = QHBoxLayout()
        self.jobHorizontalLayout.setSpacing(2)
        self.jobHorizontalLayout.setObjectName(u"jobHorizontalLayout")
        self.jobHorizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.jobLabel = QLabel(passFileDialog)
        self.jobLabel.setObjectName(u"jobLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jobLabel.sizePolicy().hasHeightForWidth())
        self.jobLabel.setSizePolicy(sizePolicy)
        self.jobLabel.setMinimumSize(QSize(0, 0))

        self.jobHorizontalLayout.addWidget(self.jobLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.jobHorizontalLayout.addItem(self.horizontalSpacer)

        self.jobComboBox = QComboBox(passFileDialog)
        self.jobComboBox.setObjectName(u"jobComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.jobComboBox.sizePolicy().hasHeightForWidth())
        self.jobComboBox.setSizePolicy(sizePolicy1)
        self.jobComboBox.setMinimumSize(QSize(175, 0))

        self.jobHorizontalLayout.addWidget(self.jobComboBox)


        self.mainVerticalLayout.addLayout(self.jobHorizontalLayout)

        self.elementHorizontalLayout = QHBoxLayout()
        self.elementHorizontalLayout.setSpacing(2)
        self.elementHorizontalLayout.setObjectName(u"elementHorizontalLayout")
        self.elementHorizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.elementLabel = QLabel(passFileDialog)
        self.elementLabel.setObjectName(u"elementLabel")

        self.elementHorizontalLayout.addWidget(self.elementLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.elementHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.elementLineEdit = QLineEdit(passFileDialog)
        self.elementLineEdit.setObjectName(u"elementLineEdit")
        self.elementLineEdit.setMinimumSize(QSize(175, 0))

        self.elementHorizontalLayout.addWidget(self.elementLineEdit)


        self.mainVerticalLayout.addLayout(self.elementHorizontalLayout)

        self.okHorizontalLayout = QHBoxLayout()
        self.okHorizontalLayout.setSpacing(0)
        self.okHorizontalLayout.setObjectName(u"okHorizontalLayout")
        self.okHorizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.okPushButton = QPushButton(passFileDialog)
        self.okPushButton.setObjectName(u"okPushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.okPushButton.sizePolicy().hasHeightForWidth())
        self.okPushButton.setSizePolicy(sizePolicy2)

        self.okHorizontalLayout.addWidget(self.okPushButton)

        self.canclePushButton = QPushButton(passFileDialog)
        self.canclePushButton.setObjectName(u"canclePushButton")
        sizePolicy2.setHeightForWidth(self.canclePushButton.sizePolicy().hasHeightForWidth())
        self.canclePushButton.setSizePolicy(sizePolicy2)

        self.okHorizontalLayout.addWidget(self.canclePushButton)


        self.mainVerticalLayout.addLayout(self.okHorizontalLayout)

        self.mainVerticalLayout.setStretch(0, 3)
        self.mainVerticalLayout.setStretch(1, 3)
        self.mainVerticalLayout.setStretch(2, 2)

        self.passFileVerticalLayout.addLayout(self.mainVerticalLayout)


        self.retranslateUi(passFileDialog)

        QMetaObject.connectSlotsByName(passFileDialog)
    # setupUi

    def retranslateUi(self, passFileDialog):
        passFileDialog.setWindowTitle(QCoreApplication.translate("passFileDialog", u"passFile", None))
        self.jobLabel.setText(QCoreApplication.translate("passFileDialog", u"Job :", None))
        self.elementLabel.setText(QCoreApplication.translate("passFileDialog", u"Element :", None))
        self.okPushButton.setText(QCoreApplication.translate("passFileDialog", u"OK", None))
        self.canclePushButton.setText(QCoreApplication.translate("passFileDialog", u"Cancle", None))
    # retranslateUi

