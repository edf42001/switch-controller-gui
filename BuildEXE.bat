pyinstaller --onefile --name SwitchControllerGUI --icon=GUIs/Images/Bear.ico --windowed main.py


:: This version bundles the resources into the .exe
:: pyinstaller --onefile --name SwitchControllerGUI --add-data DeviceInterface\GUIModifiedFirmware.hex;DeviceInterface --add-data DeviceInterface\ProgramSwitchController.bat;DeviceInterface --icon=GUIs/Images/favicon.ico --windowed main.py