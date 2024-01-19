"""
This is Lecture 7
Stacking Order
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 7 Stacking Order")
window.geometry("400x400+750+250")

# Widgets
label_1 = tk.Label(window,
                text = "Label 1",
                background = "green")  # Create Before --> Below
label_2 = tk.Label(window,
                text = "Label 2",
                background = "red")    # Create After --> Above
# From this code we create label_1 before label_2 --> label_1 will on below the label_2

# lift and lower
# label_1.lift()  # .lift() --> elevate the widget to top layer ** OR YOU CAN USE .tkraise()
# label_2.lower() # .lower() --> elevate the widget to bottom layer

button_1 = ttk.Button(window, text = "raise label 1", command = lambda: label_1.tkraise())
button_2 = ttk.Button(window, text = "raise label 2", command = lambda: label_2.tkraise())

# Layout
label_1.place(x = 50, y = 100, width = 200, height = 150)
label_2.place(x = 150, y = 60, width = 140, height = 100)

button_1.place(rely = 1, relx = 0.8, anchor = "se")
button_2.place(rely = 1, relx = 1, anchor = "se")

# Excercise
# add a thrid label and button
label_3 = tk.Label(window, text = "Label 3", background = "orange")
button_3 = tk.Button(window, text = "raise label 3", command = lambda: label_3.tkraise())

label_3.place(x = 150, y = 60, width = 140, height = 100)
button_3.place(rely = 1, relx = 0.6, anchor = "se")

# Run
window.mainloop()
