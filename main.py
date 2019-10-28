from PyQt5 import QtWidgets
from CustomMainWindow import CustomMainWindow
from GUIs.MainWindow import Ui_SwitchControllerWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SwitchControllerWindow = CustomMainWindow()
    ui = Ui_SwitchControllerWindow()
    ui.setupUi(SwitchControllerWindow)
    SwitchControllerWindow.show()

    SwitchControllerWindow.ui = ui
    SwitchControllerWindow.store_defaults()

    sys.exit(app.exec_())
