"""
This is Lecture 6
Widgets Size
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 6 Widget Size")
window.geometry("400x300")

# Widget
label_1 = tk.Label(window, text = "Label 1", background = "green")
label_2 = tk.Label(window, text = "Label 2", background = "red", width = 50)

# # Layout
# label_1.pack()
# label_2.pack(fill = "x")

# Grid
window.columnconfigure((0,1), weight = 1, uniform = "a")
window.rowconfigure((0,1), weight = 1, uniform = "a")

label_1.grid(row = 0, column = 0)
label_2.grid(row = 1, column = 0, sticky = "nsew")

# Run
window.mainloop()
