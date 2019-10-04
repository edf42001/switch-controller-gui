import tkinter as tk
from Frames import ConfigFrame, InstructionsFrame

# Variables user can select on the GUI
num_switches = 1  # Number of switches in the toy
operation_type = "Sequential"  # Method microcontroller uses to control switch outputs


# Handles when the number of switches parameter is changed
def handle_num_switches_choice(value):
    num_switches = int(value)
    print(num_switches)


# Handles when the operation type parameter is changed
def handle_operation_type_choice(value):
    operation_type = value
    print(operation_type)


# Function that runs when the "Flash Firmware" button is pressed
def handle_flash_button():
    print("button pressed")


root_width, root_height = 1280, 657

root = tk.Tk()
root.title("Replay For Kids Circuit Programmer")
root.iconbitmap("favicon.ico")


root.geometry("{}x{}".format(root_width, root_height))
root.minsize(int(root_width/2), int(root_height/2))


# Create a frame for the configuration settings and put it to the left
config_frame = ConfigFrame(root, handle_num_switches_choice, handle_operation_type_choice, handle_flash_button)
instructions_frame = InstructionsFrame(root)

wiring_frame = tk.Frame(root, background="#f0f0f0")

root.grid_rowconfigure(0, weight=5)
root.grid_rowconfigure(1, weight=3)
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)

config_frame.grid(row=1, column=1, sticky="nsew")
instructions_frame.grid(row=0, column=1, sticky="nsew")
wiring_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")

root.mainloop()  # Start the GUI
