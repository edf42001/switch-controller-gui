from PyQt5 import QtWidgets
from CustomMainWindow import CustomMainWindow
from QTGui import Ui_SwitchControllerWindow
# Variables user can select on the GUI
num_switches = 1  # Number of switches in the toy
operation_type = "Sequential"  # Method microcontroller uses to control switch outputs


# Handles when the number of switches parameter is changed
def handle_value_change(values):
    switch_type = values["switch_type"]
    mode = values["mode"]
    num_switches = int(values['num_switches'])
    pulse_width = int(values["pulse_width"])
    max_time = int(values["max_time"])
    pull_up_time = int(values["pull_up_time"])
    switch_test_time = int(values["switch_test_time"])

    print(num_switches, pulse_width, max_time)


# Function that runs when the "Flash Firmware" button is pressed
def handle_program_button():
    print("button pressed")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SwitchControllerWindow = CustomMainWindow()
    ui = Ui_SwitchControllerWindow()
    ui.setupUi(SwitchControllerWindow)
    SwitchControllerWindow.show()

    SwitchControllerWindow.ui = ui

    sys.exit(app.exec_())
