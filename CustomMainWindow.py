from PyQt5 import QtWidgets, QtGui
from CustomUploadFirmwareWindow import CustomUploadFirmwareWindow
from GUIs.UploadFirmwareWindow import Ui_UploadFirmwareWindow


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = None
        self.defaults = []
        self.values = []
        self.upload_firmware_window = None

        self.setFocus()  # For some reason switch_test_time was getting the focus

        self.setWindowIcon(QtGui.QIcon('favicon.ico'))

    def program_button_clicked(self):
        self.values = self._get_values()

        self.open_upload_firmware_window()
        self.upload_firmware_window.flash_firmware(self.values)

    def defaults_button_clicked(self):
        self.ui.switch_type.setCurrentIndex(self.defaults[0])  # In the firmware switch_type is the first variable
        self.ui.output_mode.setCurrentIndex(self.defaults[1])
        self.ui.num_outputs.setCurrentIndex(self.defaults[2] - 1)
        self.ui.pulse_width.setValue(self.defaults[3])
        self.ui.max_on_time.setValue(self.defaults[4])
        self.ui.pull_up_time.setValue(self.defaults[5])
        self.ui.switch_test_time.setValue(self.defaults[6])

    """ Functions below here are not activated by events happening in GUI"""

    def _get_values(self):
        switch_type = self.ui.output_mode.currentIndex()  # In the firmware switch_type is the first variable
        output_mode = self.ui.output_mode.currentIndex()
        num_outputs = self.ui.num_outputs.currentIndex() + 1

        pulse_width = self.ui.pulse_width.value()
        max_on_time = self.ui.max_on_time.value()
        pull_up_time = self.ui.pull_up_time.value()
        switch_test_time = self.ui.switch_test_time.value()

        return [switch_type, output_mode, num_outputs, pulse_width, max_on_time, pull_up_time, switch_test_time]

    def store_defaults(self):
        self.defaults = self._get_values()

    def open_upload_firmware_window(self):
        ui = Ui_UploadFirmwareWindow()
        UploadFirmwareWindow = CustomUploadFirmwareWindow(parent=self)
        ui.setupUi(UploadFirmwareWindow)
        UploadFirmwareWindow.ui = ui

        self.upload_firmware_window = UploadFirmwareWindow

        position = self.geometry()

        self.upload_firmware_window.setGeometry(max(position.x()-350, 0), max(position.y()-100, 0), 1200, 600)
        self.upload_firmware_window.show()



