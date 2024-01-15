"""
This is Lecture 6
Events
To read more event command "https://www.pythontutorial.net/tkinter/tkinter-event-binding/"
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecutre 6 Events")
# window.geometry("400x150")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Lecture 6 Events",
                    font = "THSarabunPSK 24 bold")

text_1 = tk.Text(widget_frame)

entry_1 = ttk.Entry(widget_frame)

button_1 = ttk.Button(widget_frame,
                      text = "Button")

# Events
# Structure of event
# widget_frame.bind("<modifier-type-detail>", lambda: print("an event"))

def callback(event):
    """
    callback(evnt) --> Print the location of left clicked

    When we create function that use with "bind()"
    it will automaticly insert 1 argrument in the function
    that why we need to create function with one argrument name "evnet"
    """
    return print(event.x, event.y, event)

window.bind("<KeyPress>", lambda event: print(event.char ,event))   # Get the value from keyboard
widget_frame.bind("<Button-1>", callback)   # <Button-1> mean to left click
text_1.bind("<Motion>", callback)           # <Motion> mean to get the motion of your mouse
entry_1.bind("<FocusIn>", lambda evnet: print("Entry field was selected"))
entry_1.bind("<FocusOut>", lambda evnet: print("Entry field was unselected"))
# <FocusIn>, <FocusOut> return the value when selected/unselected that object.

# Excercise
# Print "Mousewheel" whem the user holds down shift and used the mousewheel while text is selected.
text_1.bind("<Shift-MouseWheel>", lambda event : print("Mousewheel"))

label_1.pack()
text_1.pack()
entry_1.pack()
button_1.pack()
widget_frame.pack()

# Run
window.mainloop()
