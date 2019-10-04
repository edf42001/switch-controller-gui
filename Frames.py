import tkinter as tk

BORDER_TYPE = tk.GROOVE
BLUE_COLOR = "#15317e"
BLUE_COLOR_LIGHT = "#1e409e"
BLUE_COLOR_DARK = "#132866"
WHITE_COLOR = "#f0f0f0"


class ConfigFrame(tk.Frame):
    def __init__(self, root, num_switches_handler, operation_mode_handler, button_pressed_handler, **kwargs):
        super().__init__(root, **kwargs)

        self.config(bd=1, relief=BORDER_TYPE, bg=WHITE_COLOR)
        self.grid_propagate(False)

        # Label the configuration section
        tk.Label(self, text="Circuit Configuration", font=("Helvetica", 18), bg=WHITE_COLOR, fg=BLUE_COLOR_DARK)\
            .grid(row=0, column=1, columnspan=2, pady=(4, 12), sticky='e')

        # Create a menu for the number of switches and give it a label
        num_switches_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.create_option_menu(self, num_switches_choices, num_switches_handler, "Number of Switches:",
                                row=2, column=2)

        # Create a menu for the mode of operation and give it a label
        operation_type_choices = ["Sequential", "Simultaneous", "Latching"]
        self.create_option_menu(self, operation_type_choices, operation_mode_handler, "Mode of Operation:",
                                row=3, column=2)

        # Make the 4th row large to push the button down towards the bottom of the screen
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(3, weight=4)

        flash_button = tk.Button(self, text="Flash Firmware", command=button_pressed_handler, bg=BLUE_COLOR, fg=WHITE_COLOR)
        flash_button.grid(row=5, column=2, columnspan=2, sticky="e", padx=4, pady=4)

    # Helper function to create a dropdown menu
    @staticmethod
    def create_option_menu(parent, choices, handler, title, row=0, column=0):
        var = tk.StringVar(parent)  # Variable to receive selected value
        var.set(choices[0])  # Set default value to first in list
        menu = tk.OptionMenu(parent, var, *choices)  # Create the menu with the choices

        # Make the menu wider than the strings so that selecting options doesn't change the size, and set colors
        menu.config(width=12, bg=BLUE_COLOR, fg=WHITE_COLOR, activebackground=BLUE_COLOR_LIGHT, activeforeground=WHITE_COLOR)
                               # Units are the width of a "0" in the font
        menu.grid(row=row, column=column, sticky="ew", padx=1, pady=2)  # Make the menu stick to the sides and pad it
        menu["highlightthickness"] = 0
        label = tk.Label(parent, text=title, fg=BLUE_COLOR)
        label.grid(row=row, column=column - 1, sticky="e")
        label['bg'] = label.master['bg']  # Make background match color behind it

        # Helper function to call the user's callback function when the variable changes
        def pass_to_handler(*args):
            handler(var.get())

        var.trace("w", pass_to_handler)  # Call the helper function when the selected values changes


class InstructionsFrame(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.config(bd=1, relief=BORDER_TYPE, bg=WHITE_COLOR)

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        instructions = tk.Text(self, background=self['bg'], bd=0)
        instructions.insert(tk.END, "How to Use This Program\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        instructions.config(state=tk.DISABLED)
        instructions.tag_add("all", 1.0, "end")
        instructions.tag_configure("all", justify='left', font=("Helvetica", 10), lmargin1=12, lmargin2=15, rmargin=7,
                                   spacing2=5, wrap=tk.WORD, foreground=BLUE_COLOR)
        instructions.tag_add("title", 1.0, 2.0)
        instructions.tag_configure("title", justify="center", font=("Helvetica", 18), foreground=BLUE_COLOR_DARK)
        instructions.grid(row=0, column=0, sticky='nsew')
