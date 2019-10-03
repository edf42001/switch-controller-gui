import tkinter as tk


class ConfigFrame(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.parent = root
        # Label the configuration section
        tk.Label(self, text="Circuit Configuration", font=("Helvetica", 18)).grid(row=0, column=0, columnspan=4, pady=4)

        # Create a menu for the number of switches and give it a label
        num_switches_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
        tk.Label(self, text="Number of Switches:").grid(row=1, column=0, sticky="e")
        self.create_option_menu(self, num_switches_choices, handle_num_switches_choice, row=1, column=1)

        # Create a menu for the mode of operation and give it a label
        operation_type_choices = ["Sequential", "Simultaneous", "Latching"]
        tk.Label(self, text="Mode of Operation:").grid(row=2, column=0, sticky="e")
        self.create_option_menu(self, operation_type_choices, handle_operation_type_choice, row=2, column=1)

        # Make the 4th row large to push the button down towards the bottom of the screen
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(2, weight=1)

        flash_button = tk.Button(self, text="Flash Firmware", command=handle_flash_button, background="#ffccff")
        flash_button.grid(row=4, column=3, sticky="ew", padx=4, pady=4)

    # Helper function to create a dropdown menu
    @staticmethod
    def create_option_menu(parent, choices, handler, row=0, column=0):
        var = tk.StringVar(parent)  # Variable to recieve selected value
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


# Function that runs when the "Flash Firmware" button is pressed
def handle_flash_button():
    print("button pressed")
