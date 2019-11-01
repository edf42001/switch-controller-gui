import subprocess
import os


def modify_hex_firmware_file(values, start_row=23, start_col=9, length=16):
    """ Function to modify the constant configuration values in a compiled hex file"""

    filename = "DeviceInterface/GUIModifiedFirmware.hex"

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


def flash_firmware():
    flasher_path = "DeviceInterface/ProgramSwitchController.bat"
    firmware_path = "DeviceInterface/GUIModifiedFirmware.hex"
    flasher_path = os.path.abspath(flasher_path)

    firmware_path = os.path.abspath(firmware_path)
    p = subprocess.Popen([flasher_path, firmware_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         universal_newlines=True)

    fet_disconnected = False
    cant_find_flasher = False

    while True:
        output = p.stdout.readline()
        if output == '' and p.poll() is not None:
            break

        yield True, output[:-1]

        if output.startswith("* Couldn't find any connected USB FETs!"):
            fet_disconnected = True
        elif output.startswith("The system cannot find the") or output.startswith("'MSP430Flasher.exe' is not"):
            cant_find_flasher = True

    if fet_disconnected:
        yield False, "Error: Please Connect USB And Try Again"
    elif cant_find_flasher:
        yield False, "Error: Please Install MSP430Flasher And Try Again"
    else:
        yield False, "Success! Done Uploading"
