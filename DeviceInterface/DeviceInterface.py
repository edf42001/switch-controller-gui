import subprocess
import os.path
from DeviceInterface.exec_utils import subprocess_args, resource_path


def modify_hex_firmware_file(values, start_row=23, start_col=9, length=16):
    """ Function to modify the constant configuration values in a compiled hex file"""

    filename = "Resources/GUIModifiedFirmware.hex"  # get file path

    lines = []
    for line in open(filename, 'r'):  # Read the file
        lines.append(line)

    # Convert the configuration values to hex and combine them in a string
    consts = ""
    for i, value in enumerate(values):
        if value > 255 or value < 0:
            raise Exception("Argument value out of range for a byte")

        consts += hex(value).lstrip("0x")[-2:].upper().rjust(2, '0')  # Convert to hex, left pad with 0s, make uppercase

    # Ensure that the replacement string is the right length by right padding with 0's
    # Length is measured in bytes which are two hex characters
    consts = consts[:length*2].ljust(length*2, '0')

    line = lines[start_row]  # The line storing the constants we are modifying
    new_line = line[:start_col] + consts + line[start_col + length * 2:]  # Insert the new constants
    bytes = new_line[1:-3]  # Extract the bytes used to calculate the checksum

    # Calculate checksum
    sum = 0
    for i in range(0, len(bytes), 2):
        sum += int(bytes[i:i+2], 16)  # Sum bytes
    sum = sum - (1 << sum.bit_length())  # Checksum is the two's complement of sum

    new_line = new_line[:-3] + str(hex(sum))[-2:].upper() + "\n"  # Insert the checksum at the end of the line

    lines[start_row] = new_line  # Modify that line

    # Write the lines back to the file
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)


def flash_firmware():  # flashes firmware to device by running batch file that calls an executable flasher
    flasher_path = os.path.abspath("Resources/ProgramSwitchController.bat")  # path to flash firmware bat file
    firmware_path = os.path.abspath("Resources/GUIModifiedFirmware.hex")  # path to firmware

    # If Resources files are to be stored in the exe instead of in the same folder as the exe
    # flasher_path = resource_path("Resources/ProgramSwitchController.bat")  # path to flash firmware bat file
    # firmware_path = resource_path("Resources/GUIModifiedFirmware.hex")  # path to firmware

    # flash firmware, pass file as parameter
    p = subprocess.Popen([flasher_path, firmware_path], **subprocess_args(), universal_newlines=True)

    fet_disconnected = False  # possible errors
    cant_find_flasher = False
    not_plugged_in = False

    while True:
        output = p.stdout.readline()  # stream line from msp430flasher executable
        if output == '' and p.poll() is not None:
            break

        # remove new line character and return the line (the True indicates that this is a line of text)
        yield True, output[:-1]

        # search for an error message and set flag true if found
        if output.startswith("* Couldn't find any connected USB FETs!"):
            fet_disconnected = True
        elif output.startswith("The system cannot find the") or output.startswith("'MSP430Flasher.exe' is not"):
            cant_find_flasher = True
        elif output.startswith("# ERROR: Could not find device"):
            not_plugged_in = True

    # return result
    if fet_disconnected:
        yield False, "Error: Please Connect USB And Try Again"
    elif cant_find_flasher:
        yield False, "Error: Please Install MSP430Flasher And Try Again"
    elif not_plugged_in:
        yield False, "Error: Please Check The Switch Controller/Launchpad Board Connection"
    else:
        yield False, "Success! Done Uploading"
