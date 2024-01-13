"""
This is Lecture 8
Canvas
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 8 Canvas")
# window.geometry("600x400")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 8",
                    font = "THSarabunPSK 24 bold")

entry_1 = ttk.Entry(widget_frame)

# Canvas
canvas_1 = tk.Canvas(widget_frame,
                     bg = "White")    # When using canvas we must always set the "bg".

# canvas_1.create_rectangle((left, top, right, bottom))     # This function need tuple.
location_1 = (50, 20, 200, 100)
canvas_1.create_rectangle(location_1,
                          outline = "black",
                          width = 5,
                          fill = 'red')

# canvas_1.create_line(start_x, start_y, end_x, end_y)
location_2 = (0, 0, 100, 150)
canvas_1.create_line(location_2,
                     fill = "black")

# canvas_1.create_oval((left, top, right, botom))
location_3 = (200, 0, 300, 100)
canvas_1.create_oval(location_3,
                     outline = "black",
                     fill = "blue")
canvas_1.create_arc(location_3,
                    fill  = "red",
                    start = 45,
                    extent = 180,
                    style = tk.PIESLICE,    # tk.PIESLICE, tk.CHORD, tk.ARC
                    outline = "yellow",
                    width = 10)
# create_acr --> use after create_oval for create the segment of circle.
# start = start_degree, extent = end_degree.

# canvas_1.create_polyfon((x1, y1, x2, y2, x3, y3))
# location_4 = (0, 0, 100, 200, 300, 50)
# canvas_1.create_polygon(location_4,
#                         outline = "black",
#                         fill = "gray")

canvas_1.create_text((50,50),
                     text = "This is some text",
                     fill = "green",
                     width = 110)

# Create window using canvas
canvas_1.create_window((150, 100),
                       window = ttk.Label(widget_frame,
                                          text = "This is text in a canvas"))

button_1 = ttk.Button(widget_frame,
                      text = "Button")

# Excercise
# Use event binding to create a basic paint app
def draw(event):
    """
    This function use for drawing on canvas.
    """
    x, y = event.x, event.y
    excer_canvas.create_oval((x - bruch_size/2, y - bruch_size/2, x + bruch_size/2, y + bruch_size/2),
                             fill = "Black",
                             width = 0)

bruch_size = 10
excer_canvas = tk.Canvas(widget_frame,
                         bg = "white")
excer_canvas.bind("<Button-1>", func = draw)

label_1.pack()
entry_1.pack()
button_1.pack()
canvas_1.pack()
excer_canvas.pack()
widget_frame.pack()

# Run
window.mainloop()
