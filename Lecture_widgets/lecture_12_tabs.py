"""
This is Lecture 12
Tabs
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 12 Tabs")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 12",
                    font = "THSarabunPSK 24 bold")

# Tabs/Notebook
notebook = ttk.Notebook(widget_frame)

tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1,
                   text = "Text in tab 1")
button1 = ttk.Button(tab1,
                     text = "Button in tab1")

label1.pack()
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2,
                   text = "Text in tab 2")
entry2 = ttk.Entry(tab2,
                   text = "Entry in tab 2")

label2.pack()
entry2.pack()

notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")

# Excercise
# Add another tab with some buttons and text inside
tab_excer = ttk.Frame(notebook)
excer_label = ttk.Label(tab_excer, text = "This is excercise tab")
excer_button_1 = ttk.Button(tab_excer, text = "< Button-1 >")
excer_button_2 = ttk.Button(tab_excer, text = "< Button-2 >")

excer_label.pack()
excer_button_1.pack()
excer_button_2.pack()

notebook.add(tab_excer, text = "excercise tab")

label_1.pack()
notebook.pack()
widget_frame.pack()

# Run
window.mainloop()
