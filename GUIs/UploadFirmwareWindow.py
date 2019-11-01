# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UploadFirmwareWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UploadFirmwareWindow(object):
    def setupUi(self, UploadFirmwareWindow):
        UploadFirmwareWindow.setObjectName("UploadFirmwareWindow")
        UploadFirmwareWindow.resize(172, 127)
        UploadFirmwareWindow.setBaseSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(UploadFirmwareWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(8)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_label.setFont(font)
        self.message_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.message_label.setObjectName("message_label")
        self.horizontalLayout.addWidget(self.message_label)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        UploadFirmwareWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UploadFirmwareWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 172, 18))
        self.menubar.setObjectName("menubar")
        UploadFirmwareWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UploadFirmwareWindow)
        self.statusbar.setObjectName("statusbar")
        UploadFirmwareWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UploadFirmwareWindow)
        self.close_button.clicked.connect(UploadFirmwareWindow.close)
        QtCore.QMetaObject.connectSlotsByName(UploadFirmwareWindow)

    def retranslateUi(self, UploadFirmwareWindow):
        _translate = QtCore.QCoreApplication.translate
        UploadFirmwareWindow.setWindowTitle(_translate("UploadFirmwareWindow", "Uploading Firmware..."))
        self.message_label.setText(_translate("UploadFirmwareWindow", "Uploading Firmware..."))
        self.close_button.setText(_translate("UploadFirmwareWindow", "Close"))
