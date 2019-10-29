@echo off

set firmware_file=%1

CLS
cd c:\ti\msp430flasher_1.2.3
MSP430Flasher.exe -i USB -n MSP430G2101 -w %firmware_file% -v
pause
 
