import tkinter as tk

root = tk.Tk()
root.title("My Window")
root.geometry("320x240")

config_frame = tk.Frame(root, width=200, height=400, background="#ffdddd")
config_frame.grid_propagate(False)
config_frame.grid(row=0, column=0)


def create_option_menu(parent, choices, handler, row=0, column=0):
    var = tk.StringVar(root)
    var.set(choices[0])
    menu = tk.OptionMenu(parent, var, *choices)
    menu.grid(row=row, column=column)

    def pass_to_handler(*args):
        handler(var.get())

    var.trace("w", pass_to_handler)


num_switches = 1

def handle_num_switches_choice(value):
    num_switches = int(value)
    print(num_switches)


num_switches_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
create_option_menu(config_frame, num_switches_choices, handle_num_switches_choice, row=0, column=1)
tk.Label(config_frame, text="Select Number of Switches").grid(row=0, column=0)


operation_type = "Sequential"


def handle_operation_type_choice(value):
    operation_type = value
    print(operation_type)


operation_type_choices = ["Sequential", "Simultaneous", "Latching"]
create_option_menu(config_frame, operation_type_choices, handle_operation_type_choice, row=1, column=1)
tk.Label(config_frame, text="Choose Mode of Operation").grid(row=1, column=0)

root.mainloop()