"""
This is Lecture 1 : Basic widget in tkinter.
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    """
    This function use with button
    """
    return print("A button was pressed!")

# Create a window
window = tk.Tk()
window.title("Lecture 1")
window.geometry("800x600")

# Create widgets
# Create frame
widget_frame = tk.Frame(master = window)

# ttk widgets
label = ttk.Label(master = widget_frame,
                  text = "This is a test.")
label.pack()

# Create text_box widget (tk widget)
text_box = tk.Text(master = widget_frame)   # text widget
text_box.pack()
# .pack() use for place the widget on the top center of the frame

# Create ttk entry
entry_box = ttk.Entry(master = widget_frame)
entry_box.pack()

# Create label and button
label_hello = ttk.Label(master = widget_frame,
                        text = "My label")
button_hello = ttk.Button(master = widget_frame,
                          text = "Print Hello",
                          command = lambda: print("Hello!"))
label_hello.pack()
button_hello.pack()

# Create ttk button
button = ttk.Button(master = widget_frame,
                    text = "A Button",
                    command = button_func)
button.pack()

# pack the frame
widget_frame.pack()

# Run
window.mainloop()   # Task of mainloop() -> Updates the gui and Chcek for event
