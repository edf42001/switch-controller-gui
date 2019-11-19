:: Change the following line to the location of your executables, or remove it if they are on your PATH
set path=C:\Users\edf42001\Anaconda3\envs\replaykids\Scripts

%path%\pyuic5.exe MainWindow.ui -o MainWindow.py
%path%\pyuic5.exe UploadFirmwareWindow.ui -o UploadFirmwareWindow.py

%path%\pyrcc5.exe resources.qrc -o ..\resources_rc.py