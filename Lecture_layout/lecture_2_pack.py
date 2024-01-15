"""
This is Lecture 2
Pack
"""

import tkinter as tk

# Window
window = tk.Tk()
window.title("Lecture 2 Pack")
window.geometry("600x500+350+350")
window.minsize(width = 400, height = 300)

# Widget
label_1 = tk.Label(window,
                    text = "This is Lecutre",
                    font = "THSarabunPSK 24 bold",
                    background = "red")
label_2 = tk.Label(window, text = "Label 2",background = "blue")
label_3 = tk.Label(window, text = "Last of the labels", background = "green")
button = tk.Button(window, text = "Button")

# Layout
# # label_1.pack(side = "top", fill = "x", pady = 50, padx = 100)
# label_1.pack(side = "left", expand = True, fill = "both")
# label_2.pack(side = "top", expand = True, fill = "both")
# label_3.pack(side = "top", expand = True, fill = "both")
# button.pack(side = "top", expand = True, fill = "both")

# Very important argrument
# * side = ["left", "right", "top", "bottom"] --> The side the widget added to
# * expand = [True, False] -->  Determines the vertical or horizontal space
#                               a widget can occupy.
# * fill = ["x", "y", "both", None] --> Sets how much space the widget will
#                                       occupy.
# * padx --> create space around the widget in x axis
# * pady --> create space around the widget in y axis

# Excercise
label_1.pack(side = "top", expand = True, fill = "both", padx = 15, pady = 15)
label_2.pack(side = "left", expand = True, fill = "both")
label_3.pack(side = "top", expand = True, fill = "both")
button.pack(side = "top", expand = True, fill = "both")

# Run
window.mainloop()
