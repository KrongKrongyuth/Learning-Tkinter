"""
This is the templete to start with Tkinter
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture",
                    font = "THSarabunPSK 24 bold")

entry_1 = ttk.Entry(widget_frame)

button_1 = ttk.Button(widget_frame,
                      text = "Button")

label_1.pack()
entry_1.pack()
button_1.pack()
widget_frame.pack()

# Run
window.mainloop()
