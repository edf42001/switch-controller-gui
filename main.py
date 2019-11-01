from PyQt5 import QtWidgets
from CustomMainWindow import CustomMainWindow
from GUIs.MainWindow import Ui_SwitchControllerWindow
import sys


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    # print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == "__main__":
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustomMainWindow()
    ui = Ui_SwitchControllerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    MainWindow.ui = ui
    MainWindow.store_defaults()

    sys.exit(app.exec_())
