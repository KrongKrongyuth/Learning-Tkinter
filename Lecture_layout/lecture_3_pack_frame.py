"""
This is Lecture 3
Pack + Frames
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 3 Pack + Frames")
window.geometry("600x500+750+250")
window.minsize(width = 300, height = 200)

# Widgets
frame_1 = ttk.Frame(window)
frame_2 = ttk.Frame(window)
frame_3 = ttk.Frame(frame_2)

# Frame 1 widget
label_1 = tk.Label(frame_1, text = "Label 1", background = "red")
label_2 = tk.Label(frame_1, text = "Label 2", background = "blue")

# Window widget
label_3 = tk.Label(window, text = "Label 3", background = "green")

# Frame 2 widget
button_1 = tk.Button(frame_2, text = "Button 1")
label_4 = tk.Label(frame_2, text = "Label_4", background = "orange")
button_2 = tk.Button(frame_2, text = "Button 2")

# Frame 3 widget
button_3 = tk.Button(frame_3, text = "Button 3")
button_4 = tk.Button(frame_3, text = "Button 4")
button_5 = tk.Button(frame_3, text = "Button 5")

# Pack
label_1.pack(side = "left", expand = True, fill = "both")
label_2.pack(side = "left", expand = True, fill = "both")
frame_1.pack(side = "top", expand = True, fill = "both")

label_3.pack(side = "top", expand = True)

button_1.pack(side = "left", expand = True, fill = "both")
label_4.pack(side = "left", expand = True, fill = "both")
button_2.pack(side = "left", expand = True, fill = "both")
frame_2.pack(side = "top", expand = True, fill = "both", padx = 10, pady = 10)

button_3.pack(side = "top", expand = True, fill = "both")
button_4.pack(side = "top", expand = True, fill = "both")
button_5.pack(side = "top", expand = True, fill = "both")
frame_3.pack(side = "right", expand = True, fill = "both")

# Run
window.mainloop()
