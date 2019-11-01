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

        message = ""

        for is_line, data in DeviceInterface.flash_firmware():
            if is_line:
                self.ui.plainTextEdit.appendPlainText(data)
                QtWidgets.QApplication.processEvents()
                time.sleep(0.02)
            else:
                message = data

        self.ui.message_label.setText(message)
