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
        UploadFirmwareWindow.resize(282, 181)
        self.centralwidget = QtWidgets.QWidget(UploadFirmwareWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        UploadFirmwareWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UploadFirmwareWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 18))
        self.menubar.setObjectName("menubar")
        UploadFirmwareWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UploadFirmwareWindow)
        self.statusbar.setObjectName("statusbar")
        UploadFirmwareWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UploadFirmwareWindow)
        UploadFirmwareWindow.terminal_line_recieved['QString'].connect(self.plainTextEdit.appendPlainText)
        QtCore.QMetaObject.connectSlotsByName(UploadFirmwareWindow)

    def retranslateUi(self, UploadFirmwareWindow):
        _translate = QtCore.QCoreApplication.translate
        UploadFirmwareWindow.setWindowTitle(_translate("UploadFirmwareWindow", "Uploading Firmware..."))
        self.plainTextEdit.setPlainText(_translate("UploadFirmwareWindow", "Hello I am uploading firmware niw yaehaeas\\\\\n"
"adsa"))
