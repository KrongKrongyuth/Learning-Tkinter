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

label_1.pack()
widget_frame.pack()

# Run
window.mainloop()
