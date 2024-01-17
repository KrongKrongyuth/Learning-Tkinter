"""
This is Lecture 5
Place
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 5 Place")
window.geometry("400x600+750+250")

# Widgets
label1 = tk.Label(window, text = "Label 1", background = "red")
label2 = tk.Label(window, text = "Label 2", background = "blue")
label3 = tk.Label(window, text = "Label 3", background = "green")
button = ttk.Button(window, text = "Button")

# Layout
label1.place(x = 300, y = 100, width = 100, height = 200)
label2.place(relx = 0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5)
# When use relx and rely it will scale along the window
label3.place(x = 80, y = 60, width = 160, height = 300)
button.place(relx = 1, rely = 1, anchor = "se")

# Frame
frame = ttk.Frame(window)
frame_label = tk.Label(frame, text = "Frame label", background = "yellow")
frame_button = tk.Button(frame, text = "Frame Button")

# Frame Layout
frame_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)
frame_button.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

# Excercise
# Create a label and place it right in the center of the window
# the label should be half as wide as the window and be 200px tall
excer_label = tk.Label(window, text = "Excercise Label", background = "orange")
excer_label.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.3, anchor = "center")

# Run
window.mainloop()
