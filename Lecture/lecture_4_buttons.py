"""
This is Lecture 4
Buttons
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    """
    This function use with normal button
    """
    return print("a basic button")

# Window
window = tk.Tk()
window.title("Lecture 4 Buttons")
window.geometry("400x250")

# Button
widget_frame = ttk.Frame(master = window)

button_string = tk.StringVar(value = "A button with string var")

button = ttk.Button(master = widget_frame,
                    command = button_func,
                    textvariable = button_string)

# Check buttons
check_var = tk.IntVar()

check = ttk.Checkbutton(master = widget_frame,
                        text = "checkbox 1",
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue = 5)
# variable = tkinter_vairable --> Use for store the value if
#                                 the box is tick.
# onvalue = value --> will return the value if the box is tick.
# offvalue = value --> will reuturn the value if the box is not tick.

# Radio buttons
radio_var = tk.StringVar()

radio_1 = ttk.Radiobutton(master = widget_frame,
                          text = "Radiobutton 1",
                          value = "radio 1",
                          variable = radio_var,
                          command = lambda: print(radio_var.get()))

radio_2 = ttk.Radiobutton(master = widget_frame,
                          text = "Radiobutton 2",
                          value = 2,
                          variable = radio_var,
                          command = lambda: print(radio_var.get()))
# We always config the value of radiobutton because if not it will
# interact as the same time.
# *** The very useful features of Radiobutton is "only one"
# button is ever activated. ***

button.pack()
check.pack()
radio_1.pack()
radio_2.pack()
widget_frame.pack()

# Excercise
def excer_func():
    """
    Use for ticking off the check button
    """
    excer_bool_var.set(False)

excercise_frame = ttk.Frame(master = window)

excer_bool_var = tk.BooleanVar()
excer_string_var = tk.StringVar()

excercise_radio_1 = ttk.Radiobutton(master = excercise_frame,
                                    text = "ExcerciseRadio 1",
                                    value = "A",
                                    variable = excer_string_var,
                                    command = excer_func)

excercise_radio_2 = ttk.Radiobutton(master = excercise_frame,
                                    text = "ExcerciseRadio 2",
                                    value = "B",
                                    variable = excer_string_var,
                                    command = excer_func)

excercise_check = ttk.Checkbutton(master = excercise_frame,
                                  text = "Excercise CheckBox",
                                  variable = excer_bool_var,
                                  command = lambda : print(excer_string_var.get()))

excercise_output = ttk.Label(master = excercise_frame,
                             textvariable = excer_string_var)

excercise_radio_1.pack()
excercise_radio_2.pack()
excercise_check.pack()
excercise_output.pack(pady = 5)
excercise_frame.pack(pady = 10)

# Run
window.mainloop()
