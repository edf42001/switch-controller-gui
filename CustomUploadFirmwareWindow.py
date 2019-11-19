from PyQt5 import QtWidgets, QtCore
from DeviceInterface import DeviceInterface
import time


class CustomUploadFirmwareWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = None  # will be set by main window

    def flash_firmware(self, values):
        QtWidgets.QApplication.processEvents()  # update the window's appearance

        DeviceInterface.modify_hex_firmware_file(values)  # update the firmware file

        message = ""

        for is_line, data in DeviceInterface.flash_firmware():  # stream the flasher's output
            if is_line:  # if the data from the tuple recieved is a line of text
                self.ui.plainTextEdit.appendPlainText(data)  # add the text to the window
                QtWidgets.QApplication.processEvents()  # the text won't update unless this line is here
                time.sleep(0.02)  # small pause for effect
            else:
                message = data  # otherwise the data was the ending message

        self.ui.message_label.setText(message)  # display the ending message

    def closeEvent(self, event):
        self.parent().upload_firmware_window = None  # Remove parent's reference when closed
