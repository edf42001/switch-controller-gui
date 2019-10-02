import tkinter as tk

root = tk.Tk()
root.title("My Window")
root.iconbitmap("favicon.ico")
root.geometry("640x480")

# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)

# Create a frame for the configuration settings and put it to the left
config_frame = tk.Frame(root, width=520, height=480, background="#ffdddd")
config_frame.grid_propagate(False)
config_frame.grid(row=0, column=0)

# Helper function to create a dropdown menu
def create_option_menu(parent, choices, handler, row=0, column=0):
    var = tk.StringVar(root)  # Variable to recieve selected value
    var.set(choices[0])  # Set default value to first in list
    menu = tk.OptionMenu(parent, var, *choices)  # Create the menu with the choices
    menu.config(width=15)  # Make the menu wider than the strings so that selecting options doesn't change the size
                           # Units are the width of a "0" in the font
    menu.grid(row=row, column=column, sticky="ew", padx=4, pady=2)  # Make the menu stick to the sides and pad it

    # Helper function to call the user's callback function when the variable changes
    def pass_to_handler(*args):
        handler(var.get())

    var.trace("w", pass_to_handler)  # Call the helper function when the selected values changes


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

# Label the configuration section
tk.Label(config_frame, text="Circuit Configuration", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=4)

# Create a menu for the number of switches and give it a label
num_switches_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
create_option_menu(config_frame, num_switches_choices, handle_num_switches_choice, row=1, column=1)
tk.Label(config_frame, text="Number of Switches:").grid(row=1, column=0, sticky="e")

# Create a menu for the mode of operation and give it a label
operation_type_choices = ["Sequential", "Simultaneous", "Latching"]
create_option_menu(config_frame, operation_type_choices, handle_operation_type_choice, row=2, column=1)
tk.Label(config_frame, text="Mode of Operation:").grid(row=2, column=0, sticky="e")

# Function that runs when the "Flash Firmware" button is pressed
def handle_flash_button():
    print("button pressed")

# Make the 4th row large to push the button down towards the bottom of the screen
config_frame.grid_rowconfigure(4, minsize=140)
flash_button = tk.Button(config_frame, text="Flash Firmware", command=handle_flash_button, background="#ffccff")
flash_button.grid(row=5, column=1, sticky="ew")

root.mainloop()  # Start the GUI
