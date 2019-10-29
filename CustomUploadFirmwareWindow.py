from PyQt5 import QtWidgets
from DeviceInterface import DeviceInterface
import time

class CustomUploadFirmwareWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = None

    def flash_firmware(self, values):
        QtWidgets.QApplication.processEvents()

        DeviceInterface.modify_hex_firmware_file(values)

        for line in DeviceInterface.flash_firmware():
            self.ui.plainTextEdit.appendPlainText(line)
            QtWidgets.QApplication.processEvents()

            time.sleep(0.02)

        self.ui.message_label.setText("Success! Done Uploading")