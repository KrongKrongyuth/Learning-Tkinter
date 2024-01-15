"""
This is Lecture 5
Buttons (with arguments)
"""

import tkinter as tk
from tkinter import ttk

def button_func(parameter):
    """
    This function use with button --> have an argrument.
    """
    print("A button was preesed!")
    print("Value of entry is :",parameter.get())

def outer_func(parameter):
    """
    This function use for using with parameter
    """
    def inner_func():
        """
        This function use to print the value of entry_string
        """
        print("A button was preesed!")
        print("Value of entry is :",parameter.get())
    return inner_func

# Window
window = tk.Tk()
window.title("Lecture 5 Button (with arguments)")
window.geometry("400x250")

# Widgets
widget_frame = ttk.Frame(window)

entry_string = tk.StringVar(value = "test")

entry = ttk.Entry(widget_frame,
                  textvariable = entry_string)

button_1 = ttk.Button(widget_frame,
                    text = "< Button_1 >",
                    command = lambda : button_func(entry_string))

button_2 = ttk.Button(widget_frame,
                    text = "< Button_2 >",
                    command = outer_func(entry_string))

entry.pack()
button_1.pack()
button_2.pack()
widget_frame.pack()

# Run
window.mainloop()
