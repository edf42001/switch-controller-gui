# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SwitchControllerWindow(object):
    def setupUi(self, SwitchControllerWindow):
        SwitchControllerWindow.setObjectName("SwitchControllerWindow")
        SwitchControllerWindow.resize(811, 481)
        SwitchControllerWindow.setMaximumSize(QtCore.QSize(1000, 570))
        SwitchControllerWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/Bear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SwitchControllerWindow.setWindowIcon(icon)
        SwitchControllerWindow.setIconSize(QtCore.QSize(30, 30))
        self.widget = QtWidgets.QWidget(SwitchControllerWindow)
        self.widget.setObjectName("widget")
        self.gridlayout = QtWidgets.QGridLayout(self.widget)
        self.gridlayout.setObjectName("gridlayout")
        self.num_outputs = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_outputs.setFont(font)
        self.num_outputs.setToolTip("")
        self.num_outputs.setObjectName("num_outputs")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.num_outputs.addItem("")
        self.gridlayout.addWidget(self.num_outputs, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridlayout.addWidget(self.label_12, 9, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.switch_type = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.switch_type.setFont(font)
        self.switch_type.setToolTip("")
        self.switch_type.setObjectName("switch_type")
        self.switch_type.addItem("")
        self.switch_type.addItem("")
        self.gridlayout.addWidget(self.switch_type, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridlayout.addWidget(self.pushButton, 8, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(510, 340))
        self.textBrowser.setBaseSize(QtCore.QSize(1000, 0))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.gridlayout.addWidget(self.textBrowser, 2, 5, 8, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line, 5, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.program_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.program_button.sizePolicy().hasHeightForWidth())
        self.program_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.program_button.setFont(font)
        self.program_button.setObjectName("program_button")
        self.gridlayout.addWidget(self.program_button, 9, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8, 4, 2, 1, 1)
        self.pull_up_time = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pull_up_time.sizePolicy().hasHeightForWidth())
        self.pull_up_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pull_up_time.setFont(font)
        self.pull_up_time.setMinimum(1)
        self.pull_up_time.setMaximum(255)
        self.pull_up_time.setProperty("value", 20)
        self.pull_up_time.setObjectName("pull_up_time")
        self.gridlayout.addWidget(self.pull_up_time, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridlayout.addWidget(self.label_10, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.output_mode = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_mode.setFont(font)
        self.output_mode.setToolTip("")
        self.output_mode.setObjectName("output_mode")
        self.output_mode.addItem("")
        self.output_mode.addItem("")
        self.output_mode.addItem("")
        self.gridlayout.addWidget(self.output_mode, 4, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridlayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridlayout.addWidget(self.label_9, 8, 2, 1, 1)
        self.switch_test_time = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switch_test_time.sizePolicy().hasHeightForWidth())
        self.switch_test_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.switch_test_time.setFont(font)
        self.switch_test_time.setMinimum(1)
        self.switch_test_time.setMaximum(255)
        self.switch_test_time.setProperty("value", 5)
        self.switch_test_time.setObjectName("switch_test_time")
        self.gridlayout.addWidget(self.switch_test_time, 9, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.max_on_time = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_on_time.sizePolicy().hasHeightForWidth())
        self.max_on_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.max_on_time.setFont(font)
        self.max_on_time.setMinimum(1)
        self.max_on_time.setMaximum(255)
        self.max_on_time.setProperty("value", 100)
        self.max_on_time.setObjectName("max_on_time")
        self.gridlayout.addWidget(self.max_on_time, 7, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridlayout.addWidget(self.label_11, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridlayout.addWidget(self.label_15, 0, 0, 1, 6)
        self.pulse_width = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pulse_width.sizePolicy().hasHeightForWidth())
        self.pulse_width.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pulse_width.setFont(font)
        self.pulse_width.setMinimum(1)
        self.pulse_width.setMaximum(255)
        self.pulse_width.setProperty("value", 1)
        self.pulse_width.setObjectName("pulse_width")
        self.gridlayout.addWidget(self.pulse_width, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridlayout.addWidget(self.label_13, 3, 0, 1, 1)
        SwitchControllerWindow.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(SwitchControllerWindow)
        self.statusbar.setObjectName("statusbar")
        SwitchControllerWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(SwitchControllerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 18))
        self.menubar.setObjectName("menubar")
        SwitchControllerWindow.setMenuBar(self.menubar)
        self.actionHello = QtWidgets.QAction(SwitchControllerWindow)
        self.actionHello.setObjectName("actionHello")

        self.retranslateUi(SwitchControllerWindow)
        self.num_outputs.setCurrentIndex(1)
        self.switch_type.setCurrentIndex(0)
        self.program_button.clicked.connect(SwitchControllerWindow.program_button_clicked)
        self.pushButton.clicked.connect(SwitchControllerWindow.defaults_button_clicked)
        self.menubar.triggered['QAction*'].connect(SwitchControllerWindow.menu_item_clicked)
        QtCore.QMetaObject.connectSlotsByName(SwitchControllerWindow)

    def retranslateUi(self, SwitchControllerWindow):
        _translate = QtCore.QCoreApplication.translate
        SwitchControllerWindow.setWindowTitle(_translate("SwitchControllerWindow", "Switch Controller Programmer"))
        self.num_outputs.setItemText(0, _translate("SwitchControllerWindow", "1"))
        self.num_outputs.setItemText(1, _translate("SwitchControllerWindow", "2"))
        self.num_outputs.setItemText(2, _translate("SwitchControllerWindow", "3"))
        self.num_outputs.setItemText(3, _translate("SwitchControllerWindow", "4"))
        self.num_outputs.setItemText(4, _translate("SwitchControllerWindow", "5"))
        self.num_outputs.setItemText(5, _translate("SwitchControllerWindow", "6"))
        self.num_outputs.setItemText(6, _translate("SwitchControllerWindow", "7"))
        self.num_outputs.setItemText(7, _translate("SwitchControllerWindow", "8"))
        self.label_12.setToolTip(_translate("SwitchControllerWindow", "The switch test time plus the resistor pull-up time is the time\n"
"between tests of a closed switch in increments of ~100 milliseconds."))
        self.label_12.setText(_translate("SwitchControllerWindow", "?"))
        self.label_4.setText(_translate("SwitchControllerWindow", "Max On Time:"))
        self.switch_type.setItemText(0, _translate("SwitchControllerWindow", "Normally Open"))
        self.switch_type.setItemText(1, _translate("SwitchControllerWindow", "Normally Closed"))
        self.pushButton.setText(_translate("SwitchControllerWindow", "Restore Defaults"))
        self.label.setText(_translate("SwitchControllerWindow", "Output Mode:"))
        self.label_5.setText(_translate("SwitchControllerWindow", "Resistor Pull Up Time:"))
        self.textBrowser.setHtml(_translate("SwitchControllerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1) Select configuration values for the toy\'s switch controller</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2) Connect the TI Lanchpad and switch controller as shown</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Images/Images/LaunchpadSwitchController.jpg\" /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3) Click the &quot;Program Circuit&quot; button</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">* To restore default values click the &quot;Restore Defaults&quot; button</span></p></body></html>"))
        self.label_6.setText(_translate("SwitchControllerWindow", "Switch Test Time:"))
        self.label_3.setText(_translate("SwitchControllerWindow", "Pulse Width:"))
        self.program_button.setText(_translate("SwitchControllerWindow", "Program Circuit"))
        self.label_8.setToolTip(_translate("SwitchControllerWindow", "One-shot: Every push turns on the next output in sequence for a short\n"
"    pulse.\n"
"Retriggerable one-shot: Every push turns on the next output in\n"
"    sequence as long as the push button is held.\n"
"On-off: The push turns on the next output in sequence and keeps it on\n"
"    until the switch is released and pushed again."))
        self.label_8.setText(_translate("SwitchControllerWindow", "?"))
        self.label_10.setToolTip(_translate("SwitchControllerWindow", "To save the batteries, the maximum time an output can remain on can\n"
"be configured in increments of ~100 milliseconds."))
        self.label_10.setText(_translate("SwitchControllerWindow", "?"))
        self.label_2.setText(_translate("SwitchControllerWindow", "Number of Outputs:"))
        self.output_mode.setItemText(0, _translate("SwitchControllerWindow", "One Shot"))
        self.output_mode.setItemText(1, _translate("SwitchControllerWindow", "Retriggerable"))
        self.output_mode.setItemText(2, _translate("SwitchControllerWindow", "On/Off"))
        self.label_14.setToolTip(_translate("SwitchControllerWindow", "Normally Open (N.O.) - The connection is normally open and closes when the switch is pushed\n"
"Normally Closed (N.C.) - The connection is normally closed and opens when the switch is pushed"))
        self.label_14.setText(_translate("SwitchControllerWindow", "?"))
        self.label_9.setToolTip(_translate("SwitchControllerWindow", "The time the resistor is pulled up before the closed switch state can\n"
"be tested. Time in ~.1 milliseconds."))
        self.label_9.setText(_translate("SwitchControllerWindow", "?"))
        self.label_7.setToolTip(_translate("SwitchControllerWindow", "The number of switches to control in the sequence."))
        self.label_7.setText(_translate("SwitchControllerWindow", "?"))
        self.label_11.setToolTip(_translate("SwitchControllerWindow", "The one shot pulse width can be configured in increments of ~100\n"
"milliseconds."))
        self.label_11.setText(_translate("SwitchControllerWindow", "?"))
        self.label_15.setText(_translate("SwitchControllerWindow", "<html><head/><body><p align=\"center\"><img src=\":/Images/Images/RFK_logo_ONE-LINE_med.png\" width=\"500\"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p></body></html>\n"
"<!---Use a few non-breaking spaces to make the image look more centered---!>"))
        self.label_13.setText(_translate("SwitchControllerWindow", "Switch Type:"))
        self.actionHello.setText(_translate("SwitchControllerWindow", "Hello"))
import resources_rc
