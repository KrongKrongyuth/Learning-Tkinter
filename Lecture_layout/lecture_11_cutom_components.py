"""
This is Lecture 11
Custom components
"""

import tkinter as tk
from tkinter import ttk

# Using Class base approch
class Segment(ttk.Frame):
    """
    This class use for create custom component (Class base approch)
    """
    def __init__(self, parent, label_text, button_text, excercise_text):
        super().__init__(parent)

        # Grid layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")

        # Widgets
        tk.Label(self, text = label_text).grid(row = 0, column = 0, sticky = "nsew")
        tk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = "nsew")
        self.entry_zone(button_text = excercise_text).grid(row = 0, column = 2, sticky = "nsew")

        self.pack(expand = True, fill = "both", padx = 10, pady = 10)

    def entry_zone(self, button_text):
        """
        Excercise
        This function use for create entry and button in the segemnet class
        """
        # Frame
        frame = ttk.Frame(self)

        # Widgets
        entry = tk.Entry(frame)
        button = tk.Button(frame, text = button_text)

        # Layout
        entry.pack(fill = "both", expand = True, pady = 20)
        button.pack(fill = "both", expand = True)

        return frame

# Using Function base approch
def create_segment(parent, label_text, button_text):
    """
    This class use for create custom component (Function base approch)
    """
    frame = ttk.Frame(parent)

    # Grid layout
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure((0,1,2), weight = 1, uniform = "a")

    # Widgets
    tk.Label(frame, text = label_text).grid(row = 0, column = 0, sticky = "nsew")
    tk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = "nsew")

    return frame

# Window
window = tk.Tk()
window.title("Widgets and return")
window.geometry("400x600")

# Widgets (Function base)
# create_segment(window, "label", "button").pack(expand = True, fill = "both", padx = 10, pady = 10)
# create_segment(window, "test", "click").pack(expand = True, fill = "both", padx = 10, pady = 10)
# create_segment(window, "hello", "test").pack(expand = True, fill = "both", padx = 10, pady = 10)
# create_segment(window, "bye", "lunch").pack(expand = True, fill = "both", padx = 10, pady = 10)
# create_segment(window, "last one", "exit").pack(expand = True, fill = "both", padx = 10, pady = 10)

# Widgets (Class base)
Segment(window, "label", "button", "A")
Segment(window, "test", "click", "B")
Segment(window, "hello", "test", "C")
Segment(window, "bye", "lunch", "D")
Segment(window, "last one", "exit", "E")

# Excercise
# Create a smaller widget insde of the sement class using function/method
# it should be a container that has an entry field and a button stacked on top od each other
# the button text should be set via the parameters
# all of this should be on the third column

# Run
window.mainloop()
