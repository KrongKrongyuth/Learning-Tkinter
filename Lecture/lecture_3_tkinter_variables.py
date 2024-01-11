"""
This is Lecture 3
Tkinter vairable
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    """
    Print string_var value
    """
    print(string_var.get())
    string_var.set("Button pressed!")
    # After pressed the button string_var will change the value

# Window
window = tk.Tk()
window.title("Lecture 3 Tkinter vairable")
window.geometry("400x250")

# tkinter variable
string_var = tk.StringVar(value = "<Fill the input here>")
# value = use for set the initial value
# int_var = tk.IntVar()
# double_var = tk.DoubleVar()
# bool_var = tk.BooleanVar()
# tk can create the variable to store the value in the different type
excercise_var = tk.StringVar(value = "test")

# Widgets
widget_frame = ttk.Frame(master = window)

label = ttk.Label(master = widget_frame,
                  text = "Welcome to Lecture 3",
                  font = "THSarabunPSK 24 bold")

entry = ttk.Entry(master = widget_frame,
                  textvariable = string_var)

button = ttk.Button(master = widget_frame,
                    text = "Button",
                    command = button_func)

detail = ttk.Label(master = widget_frame,
                   text = "After connect with string_var",
                   font = "THSarabunPSK 16")

output = ttk.Label(master = widget_frame,
                   textvariable = string_var,
                   font = "THSarabunPSK 12")
# textvariable use for connect the Entry and Label in real time.

label.pack()
entry.pack()
button.pack()
detail.pack(pady = 10)
output.pack(pady = 5)
widget_frame.pack()

# Excercise
excercise_frame = ttk.Frame(master = window)
excercise_entry_1 = ttk.Entry(master = widget_frame,
                              textvariable = excercise_var)

excercise_entry_2 = ttk.Entry(master = widget_frame,
                              textvariable = excercise_var)

excercise_label = ttk.Label(master = widget_frame,
                            textvariable = excercise_var)

excercise_entry_1.pack()
excercise_entry_2.pack()
excercise_label.pack()
widget_frame.pack()

# Run
window.mainloop()
