import tkinter as tk
from Frames import ConfigFrame, InstructionsFrame, WiringFrame

# Variables user can select on the GUI
num_switches = 1  # Number of switches in the toy
operation_type = "Sequential"  # Method microcontroller uses to control switch outputs


# Handles when the number of switches parameter is changed
def handle_value_change(values):
    switch_type = values["switch_type"]
    mode = values["mode"]
    num_switches = int(values['num_switches'])
    pulse_width = int(values["pulse_width"])
    max_time = int(values["max_time"])
    pull_up_time = int(values["pull_up_time"])
    switch_test_time = int(values["switch_test_time"])

    print(num_switches, pulse_width, max_time)


# Function that runs when the "Flash Firmware" button is pressed
def handle_program_button():
    print("button pressed")


root_width, root_height = 1280, 657

root = tk.Tk()
root.title("Replay For Kids Circuit Programmer")
root.iconbitmap("favicon.ico")


root.geometry("{}x{}".format(root_width, root_height))
root.minsize(int(root_width/2), int(root_height/2))


# Create a frame for the configuration settings and put it to the left
config_frame = ConfigFrame(root, handle_value_change, handle_program_button)
instructions_frame = InstructionsFrame(root)
wiring_frame = WiringFrame(root)

root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=2)
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)

config_frame.grid(row=1, column=1, sticky="nsew")
instructions_frame.grid(row=0, column=1, sticky="nsew")
wiring_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")

root.mainloop()  # Start the GUI
