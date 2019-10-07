from Utils import *

import tkinter as tk
import tkinter.ttk as ttk

class ConfigFrame(tk.Frame):
    # Different options:
    switch_type_choices = ["N.O.", "N.C."]
    mode_choices = ["One-Shot", "Retrigger", "On/Off"]
    num_switches_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
    pulse_width_choices = ["1", "2", "3", "4", "5"]
    max_time_choices = ["60", "70", "80", "90", "100", "110", "120", "130"]
    pull_up_choices = ["10", "20", "30"]
    switch_test_time_choices = ["2", "3", "4", "5", "6", "7", "8"]

    simple_options = [Option("switch_type", "Switch Type:", switch_type_choices),
                      Option("mode", "Operation Mode:", mode_choices),
                      Option("num_switches", "Number of Switches:", num_switches_choices)]

    advanced_options = [Option("pulse_width", "Pulse Width:", pulse_width_choices),
                        Option("max_time", "Max On Time:", max_time_choices, default="100"),
                        Option("pull_up_time", "Pull Up Resistor Time:", pull_up_choices, default="20"),
                        Option("switch_test_time", "Switch Test Time:", switch_test_time_choices, default="5")]

    def __init__(self, root, value_handler, button_pressed_handler, **kwargs):
        super().__init__(root, **kwargs)

        self.value_handler = value_handler
        self.values = dict()
        self.vars = []

        self.config(bd=1, relief=BORDER_TYPE, bg=WHITE_COLOR)
        self.grid_propagate(False)

        # Label the configuration section
        tk.Label(self, text="Circuit Configuration", font=("Helvetica", 18), bg=WHITE_COLOR, fg=BLUE_COLOR_DARK)\
            .grid(row=0, column=1, columnspan=2, pady=(4, 12), sticky='e')

        tabs = ttk.Notebook(self)
        simple = ttk.Frame(tabs)
        advanced = ttk.Frame(tabs, padding=(0,0,0,0))
        tabs.add(simple, text="Basic")
        tabs.add(advanced, text="Advanced")
        tabs.grid(row=1, column=1, columnspan=2)

        for i, option in enumerate(ConfigFrame.simple_options):
            self.values[option.name] = option.default # Set default value of dictionary for each choice
            self.create_option_menu(simple, option, row=i, column=1)

        for i, option in enumerate(ConfigFrame.advanced_options):
            self.values[option.name] = option.default # Set default value of dictionary for each choice
            self.create_option_menu(advanced, option, row=i, column=1)

        # Make the 4th row large to push the button down towards the bottom of the screen
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(3, weight=4)

        program_button = CustomButton(self, text="Program Circuit", command=button_pressed_handler, bg=BLUE_COLOR,
                                   fg=WHITE_COLOR, activebackground=BLUE_COLOR, activeforeground=WHITE_COLOR)
        program_button.grid(row=3, column=2, columnspan=2, sticky="e", padx=4, pady=4)

        defaults_button = CustomButton(self, text="Restore Defaults", command=self.reset_defaults, bg=BLUE_COLOR,
                                   fg=WHITE_COLOR, activebackground=BLUE_COLOR, activeforeground=WHITE_COLOR)
        defaults_button.grid(row=3, column=0, columnspan=2, sticky="w", padx=4, pady=4)

    # Helper function to create a dropdown menu
    def create_option_menu(self, parent, option, row=0, column=0):
        var = tk.StringVar(parent)  # Variable to receive selected value
        var.set(option.default)  # Set default value to first in list
        menu = tk.OptionMenu(parent, var, *option.options)  # Create the menu with the choices

        # Make the menu wider than the strings so that selecting options doesn't change the size, and set colors
        menu.config(width=12, bg=BLUE_COLOR, fg=WHITE_COLOR, activebackground=BLUE_COLOR_LIGHT, activeforeground=WHITE_COLOR)
                               # Units are the width of a "0" in the font
        menu.grid(row=row, column=column, sticky="ew", padx=1, pady=2)  # Make the menu stick to the sides and pad it
        menu["highlightthickness"] = 0
        label = tk.Label(parent, text=option.title, fg=BLUE_COLOR)
        label.grid(row=row, column=column - 1, sticky="e")

        # Helper function to call the user's callback function when the variable changes
        def pass_to_handler(*args):
            self.values[option.name] = var.get()
            self.value_handler(self.values)

        var.trace("w", pass_to_handler)  # Call the helper function when the selected values changes

        self.vars.append(var)

    def reset_defaults(self):
        options = self.simple_options.copy()
        options.extend(self.advanced_options)
        for option, var in zip(options, self.vars):
            var.set(option.default)


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


class WiringFrame(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.config(bd=1, relief=BORDER_TYPE, bg=WHITE_COLOR)

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        instructions = tk.Text(self, background=self['bg'], bd=0)
        instructions.insert(tk.END, "How to Wire Your Circuit\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        instructions.config(state=tk.DISABLED)
        instructions.tag_add("all", 1.0, "end")
        instructions.tag_configure("all", justify='left', font=("Helvetica", 10), lmargin1=12, lmargin2=15, rmargin=7,
                                   spacing2=5, wrap=tk.WORD, foreground=BLUE_COLOR)
        instructions.tag_add("title", 1.0, 2.0)
        instructions.tag_configure("title", justify="center", font=("Helvetica", 18), foreground=BLUE_COLOR_DARK)
        instructions.grid(row=0, column=0, sticky='nsew')