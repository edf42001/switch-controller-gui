# Switch Controller GUI

The Switch Controller GUI is a program to help volunters upload firmware to the Switch Controller, a device that will allow multiple switches inside an electronic toy to be controlled by one external switch so that children with disabilites can more easily engage with the toy.

The Switch Controller GUI was programmed with PyQT5 and the QT Designer. You can download an open source version of QT here: https://www.qt.io/download and follow this youtube tutorial to install the QT Designer: https://www.youtube.com/watch?v=FVpho_UiDAY. 

To edit the program, open the _.ui_ files found in the _GUIs_ folder in QT Designer. When ready to convert the ui to python code, run the _ConvertToPython.bat_ file. (Note: You will probably need to edit this file to point to the location of the pyuic5 and pyrrc5 scripts installed with PyQT5 on your computer). Running this script will create _MainWindow.py_, _UploadFirmwareWindow.py_, and _resources_rc.py_, which should not be edited.

To build the executable, I used Pyinstaller, which can be installed with `pip install pyinstaller`. To build the exe simply run _BuildEXE.bat_, which may also have to be modified if pyinstaller is not in your system PATH.

To edit the firmware uploaded to the microcontroller, first make you code changes in your IDE. Have your IDE create an Intel HEX firmware file named _GUIModifiedFirmware.hex_, and also have it create the associated .map file _GUIModifiedFirmware.map_. Move both of these files to the _Resources_ folder so the GUI can upload the new firmware.
