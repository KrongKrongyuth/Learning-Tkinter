"""
This is Lecture 1
Pack
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 1 Pack")
window.geometry("600x500+350+350")
window.minsize(width = 400, height = 300)

# Widget
widget_frame = ttk.Frame(window, relief = "ridge", borderwidth = 10)

label_1 = ttk.Label(widget_frame,
                    text = "This is Lecutre 1",
                    font = "THSarabunPSK 24 bold")

label_2 = ttk.Label(window, text = "Label 2",
                    background = "red")
label_3 = ttk.Label(window, text = "Label 3",
                    background = "blue")

# Pack
# label_1.pack()
# label_2.pack(side = "left", expand = True, fill = "both")
# label_3.pack(side = "left")
# widget_frame.pack(side = "left", expand = True, fill = "x")

# Grid
# window.columnconfigure(0, weight = 1)   # Create 1 column as index 0
# window.columnconfigure(1, weight = 1)   # Create 1 column as index 1
# window.columnconfigure(2, weight = 2)   # Create 2 column as index 2
# window.rowconfigure(0, weight = 1)      # Create 1 row as index 0

# label_2.grid(row = 0, column = 1, sticky = "nsew")
# label_3.grid(row = 1, column = 1, columnspan = 2, sticky = "nsew")

# Place
label_2.place(x = 100,y = 200, width = 200, height = 100)
label_3.place(relx = 0.5,rely = 0.5,
              relwidth = 1,
              anchor = "nw")    # [relx,rely] -> min [0,0] -> max [1,1]

# Run
window.mainloop()
