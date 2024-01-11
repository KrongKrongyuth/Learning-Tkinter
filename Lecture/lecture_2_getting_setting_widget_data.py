"""
This is Lecture 2
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    """
    Get tge content of the entry
    """
    entry_text = entry.get()

    # Update the label
    # label.config(text = "Some other text")
    # label.configure(text = "Some other text")
    label["text"] = entry_text      # This code work the same as above.
    entry['state'] = 'disable'      # This use for make entry work at once.
    # To ckeck what anything we can do with widget you must use function below.
    # print(label.configure(), end = "\n\n")
    # print(entry.configure(), end = "\n\n")
    # print(button.configure(), end = "\n\n")
def reset_button():
    """
    Reset to defult setting
    """
    label["text"] = "This is the label"
    entry["state"] = "enable"

# Window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("400x150")

# Widgets
widget_frame = ttk.Frame(master = window)

label = ttk.Label(master = widget_frame,
                  text = "This is the label",
                  font = "THSarabunPSK 24 bold")

entry = ttk.Entry(master = widget_frame)

button = ttk.Button(master = widget_frame,
                    text = "Print",
                    command = button_func)

exercise_button = ttk.Button(master = widget_frame,
                             text = "Reset",
                             command = reset_button)

label.pack()
entry.pack()
button.pack()
exercise_button.pack()
widget_frame.pack()

# Run
window.mainloop()
