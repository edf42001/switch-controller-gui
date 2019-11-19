from PyQt5 import QtWidgets
from CustomMainWindow import CustomMainWindow
from GUIs.MainWindow import Ui_SwitchControllerWindow
import sys
import traceback


# Errors occuring in QT were not printing to console. This fixes that
def my_exception_hook(exctype, value, tb):
    # Write the exception to a file as well
    with open("crash_report.txt", 'w+') as f:
        traceback.print_exception(exctype, value, tb, file=f)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, tb)
    sys.exit(1)


if __name__ == "__main__":
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustomMainWindow()  # Create instance of the custom main window
    ui = Ui_SwitchControllerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    MainWindow.ui = ui  # Give the main window access to its ui
    MainWindow.store_defaults()  # Record the default values

    sys.exit(app.exec_())
