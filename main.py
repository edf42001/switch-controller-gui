import tkinter as tk
from ConfigFrame import ConfigFrame

root_width, root_height = 1280, 657

root = tk.Tk()
root.title("My Window")
root.iconbitmap("favicon.ico")


root.geometry("{}x{}".format(root_width, root_height))
root.minsize(int(root_width/2), int(root_height/2))

# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)

# Create a frame for the configuration settings and put it to the left
config_frame = ConfigFrame(root, background="#ffcccc")
instructions_frame = tk.Frame(root, background="#ccffcc")
wiring_frame = tk.Frame(root, background="#ccccff")
config_frame.grid_propagate(False)

root.grid_rowconfigure(0, weight=5)
root.grid_rowconfigure(1, weight=2)
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)

config_frame.grid(row=1, column=1, sticky="nsew")
instructions_frame.grid(row=0, column=1, sticky="nsew")
wiring_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")

root.mainloop()  # Start the GUI
