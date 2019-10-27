from PyQt5 import QtWidgets


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = None

    def program_button_clicked(self):
        num_outputs = self.ui.num_outputs.currentIndex() + 1
        output_mode = self.ui.output_mode.currentIndex()

        pulse_width = self.ui.pulse_width.value()
        max_on_time = self.ui.max_on_time.value()
        pull_up_time = self.ui.pull_up_time.value()
        switch_test_time = self.ui.switch_test_time.value()

        print(num_outputs, output_mode, pulse_width, max_on_time, pull_up_time, switch_test_time)