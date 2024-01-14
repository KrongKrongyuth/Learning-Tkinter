"""
This is Lecture 11
Frames & Parenting
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 11 Frames & Parenting")
window.geometry("1000x1000")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 11",
                    font = "THSarabunPSK 24 bold")

# Frame
frame = ttk.Frame(window,
                  width = 400,
                  height = 500,
                  borderwidth = 10,
                  relief = tk.GROOVE)
frame.pack_propagate(False) # Use the width and height from default setting
# relief --> use for set the type of boarder

# Master setting
label_2 = ttk.Label(frame,
                    text = "Label in frame")

button_1 = ttk.Button(frame,
                      text = "button in frame")

label_outside = ttk.Label(window,
                          text = "label outside frame")

# Excercise
# Create another frame with a label, a button and an entry and place it to the right
# of the other widgets

excer_frame = ttk.Frame(window)

excer_label = ttk.Label(excer_frame,
                        text = "This is an excer label")

excer_button = ttk.Button(excer_label,
                          text = "This is an excer button")

excer_entry = ttk.Entry(excer_label,
                        text = "This is an excer entry")

label_1.pack()
widget_frame.pack()

label_2.pack()
button_1.pack()
frame.pack(side = "left")

excer_label.pack(side = "right")
excer_button.pack(side = "right")
excer_entry.pack(side = "right")
excer_frame.pack(side = "right")

label_outside.pack()

# Run
window.mainloop()
