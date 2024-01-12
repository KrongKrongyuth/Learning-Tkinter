"""
This is Lecture 7
Combobox and Spinbox
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 7 Combobox and Spinbox")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 7",
                    font = "THSarabunPSK 24 bold")

entry_1 = ttk.Entry(widget_frame)

button_1 = ttk.Button(widget_frame,
                      text = "Button")

# Combobox
items = ('1', '2', '3')
item_string = tk.StringVar(value = items[0])
combo_1 = ttk.Combobox(widget_frame,
                       textvariable = item_string)
# combo_1.configure(values = items)     # We can use this too.
combo_1['value'] = items

# Events
combo_1.bind("<<ComboboxSelected>>",
             lambda event : combo_label.config(text = f"Selected value: {item_string.get()}"))
# combo_label = ttk.Label(widget_frame,
#                         text = "Select the number",
#                         textvariable = item_string,
#                         font = "THSarabunPSK 18 bold")

combo_label = ttk.Label(widget_frame,
                        text = "Select the number",
                        font = "THSarabunPSK 18 bold")

# Spinbox
spin_value = tk.IntVar(value = 12)
spinbox_1 = ttk.Spinbox(widget_frame,
                        textvariable = spin_value,
                        from_ = 3,
                        to = 20,
                        increment = 3,
                        command = lambda: print(spin_value.get()))
# increment --> Use for incremet number by 3 per 1 click
spinbox_1.bind("<<Increment>>", lambda evnet: print("Up"))
# <<Increment>> --> Do function when click on up button
spinbox_1.bind("<<Decrement>>", lambda evnet: print("Down"))
# <<Decrement>> --> Do function when click on down button

# Excercise
# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased
excer_value = ("A", "B", "C", "D", "E")
excer_string = tk.StringVar(value = "Unselected")
excer_spinbox = ttk.Spinbox(widget_frame,
                            values = excer_value,
                            textvariable = excer_string)
excer_spinbox.bind("<<Decrement>>", lambda event: print(excer_string.get()))

label_1.pack()
entry_1.pack()
button_1.pack()
combo_1.pack(pady = 5)
combo_label.pack()
spinbox_1.pack()
excer_spinbox.pack()
widget_frame.pack()

# Run
window.mainloop()
