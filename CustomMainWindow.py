from PyQt5 import QtWidgets
from DeviceInterface import DeviceInterface


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = None
        self.defaults = []

    def program_button_clicked(self):
        values = self._get_values()

        print(values)

        DeviceInterface.modify_hex_firmware_file(values)
        DeviceInterface.flash_firmware()


    def defaults_button_clicked(self):
        self.ui.num_outputs.setCurrentIndex(self.defaults[0] - 1)
        self.ui.output_mode.setCurrentIndex(self.defaults[1])
        self.ui.pulse_width.setValue(self.defaults[2])
        self.ui.max_on_time.setValue(self.defaults[3])
        self.ui.pull_up_time.setValue(self.defaults[4])
        self.ui.switch_test_time.setValue(self.defaults[5])

    """ Functions below here are not called by events happening in GUI"""

    def _get_values(self):
        num_outputs = self.ui.num_outputs.currentIndex() + 1
        output_mode = self.ui.output_mode.currentIndex()

        pulse_width = self.ui.pulse_width.value()
        max_on_time = self.ui.max_on_time.value()
        pull_up_time = self.ui.pull_up_time.value()
        switch_test_time = self.ui.switch_test_time.value()

        return [num_outputs, output_mode, pulse_width, max_on_time, pull_up_time, switch_test_time]

    def store_defaults(self):
        self.defaults = self._get_values()
