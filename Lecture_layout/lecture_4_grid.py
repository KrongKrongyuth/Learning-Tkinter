"""
This is Lecture 
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture")
window.geometry("600x500+350+350")
window.minsize(width = 400, height = 300)

# Widget
label_1 = tk.Label(window, text = "Label 1", background = "red")
label_2 = tk.Label(window, text = "Label 2", background = "blue")
label_3 = tk.Label(window, text = "Label 3", background = "green")
label_4 = tk.Label(window, text = "Label 4", background = "yellow")
button_1 = tk.Button(window, text = "Button 1")
button_2 = tk.Button(window, text = "Button 2")
entry = ttk.Entry(window)

# Define a grid
# window.columnconfigure(index, weight = how_wide_of_column)
window.columnconfigure((0,1,2), weight = 1, uniform = "a")
window.columnconfigure(3, weight = 2, uniform = "a")
window.rowconfigure(0, weight = 1, uniform = "a")
window.rowconfigure(1, weight = 1, uniform = "a")
window.rowconfigure(2, weight = 1, uniform = "a")
window.rowconfigure(3, weight = 3, uniform = "a")

# Place a widget
label_1.grid(row = 0, column = 0, sticky = "nsew")
label_2.grid(row = 1, column = 1, rowspan = 3, sticky = "nsew")
label_3.grid(row = 1, column = 0, columnspan = "3", sticky = "nsew", padx = 20, pady = 10)
label_4.grid(row = 3, column = 3, sticky = "se")

# Excercise
# add the button and the entry field
button_1.grid(row = 0, column = 3, sticky = "nsew")
button_2.grid(row = 2, column = 2, sticky = "nsew")
entry.grid(row = 3, column = 3)

# Run
window.mainloop()
