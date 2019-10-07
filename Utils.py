import tkinter as tk

BORDER_TYPE = tk.GROOVE
BLUE_COLOR = "#15317e"
BLUE_COLOR_LIGHT = "#1e409e"
BLUE_COLOR_DARK = "#132866"
WHITE_COLOR = "#f0f0f0"


class Option:
    def __init__(self, name, title, options, default=None):
        self.name = name
        self.title = title
        self.options = options
        if default:
            self.default = default
        else:
            self.default = options[0]


class CustomButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = BLUE_COLOR_LIGHT

    def on_leave(self, e):
        self['background'] = BLUE_COLOR



