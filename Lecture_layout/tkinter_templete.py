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
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "This is Lecutre",
                    font = "THSarabunPSK 24 bold")

label_1.pack()
widget_frame.pack()

# Run
window.mainloop()
