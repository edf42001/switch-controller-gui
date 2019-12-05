from PyQt5 import QtWidgets
from CustomUploadFirmwareWindow import CustomUploadFirmwareWindow
from GUIs.UploadFirmwareWindow import Ui_UploadFirmwareWindow
import subprocess
import os.path


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = None  # Reference to own ui. Will be set externally
        self.defaults = []  # default values for controls
        self.values = []  # current values stored
        self.upload_firmware_window = None  # Reference to the firmware uploading window

        self.setFocus()  # For some reason switch_test_time was getting the focus. Fix.

    def program_button_clicked(self):  # when the upload firmware button is clicked
        self.values = self._get_values()  # read the current values

        self.open_upload_firmware_window()  # open the firmware window
        self.upload_firmware_window.flash_firmware(self.values)  # have it upload the firmware

    def defaults_button_clicked(self):  # restore defaults button pressed
        self.ui.switch_type.setCurrentIndex(self.defaults[0])  # In the firmware switch_type is the first variable
        self.ui.output_mode.setCurrentIndex(self.defaults[1])
        self.ui.num_outputs.setCurrentIndex(self.defaults[2] - 1)  # Since (1) output switch is index 0 in the box
        self.ui.pulse_width.setValue(self.defaults[3])
        self.ui.max_on_time.setValue(self.defaults[4])
        self.ui.pull_up_time.setValue(self.defaults[5])
        self.ui.switch_test_time.setValue(self.defaults[6])

    def menu_item_clicked(self, action):  # An option on the help menu pressed
        item = action.text()  # read the name
        path = os.path.join("Resources/Tutorials", item + ".pdf")
        path = os.path.abspath(path)  # find the corresponding pdf file

        if os.path.exists(path):
            subprocess.Popen([path], shell=True)  # Open the PDF in a web browser
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Sorry, that help file wasn't found")
            msg.setInformativeText("\"" + item + ".pdf\"")
            msg.setWindowTitle("Oops")
            msg.exec_()

    """ Functions below here are not activated by events happening in GUI"""

    def _get_values(self):  # get current active values for all controls
        switch_type = self.ui.output_mode.currentIndex()  # In the firmware switch_type is the first variable
        output_mode = self.ui.output_mode.currentIndex()
        num_outputs = self.ui.num_outputs.currentIndex() + 1  # index 0 is 1 output

        pulse_width = self.ui.pulse_width.value()
        max_on_time = self.ui.max_on_time.value()
        pull_up_time = self.ui.pull_up_time.value()
        switch_test_time = self.ui.switch_test_time.value()

        return [switch_type, output_mode, num_outputs, pulse_width, max_on_time, pull_up_time, switch_test_time]

    def store_defaults(self):  # store the starting values as the defaults
        self.defaults = self._get_values()

    def open_upload_firmware_window(self):
        if self.upload_firmware_window:  # Close the window if it's already open
            self.upload_firmware_window.close()

        ui = Ui_UploadFirmwareWindow()
        UploadFirmwareWindow = CustomUploadFirmwareWindow(parent=self)
        ui.setupUi(UploadFirmwareWindow)
        UploadFirmwareWindow.ui = ui  # give the window a reference to it's ui
        self.upload_firmware_window = UploadFirmwareWindow

        position = self.geometry()  # try to position the window over the current one
        self.upload_firmware_window.setGeometry(max(position.x()-50, 0), max(position.y()-100, 0), 1200, 600)
        self.upload_firmware_window.show()
