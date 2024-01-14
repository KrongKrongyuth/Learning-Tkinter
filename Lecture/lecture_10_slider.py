"""
This is Lecture 10
Slider and Progress Bar
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Window
window = tk.Tk()
window.title("Lecture 10 Slider&Progress Bar")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 10",
                    font = "THSarabunPSK 24 bold")

# Slider
scale_double = tk.DoubleVar(value = 50)

scale_1 = ttk.Scale(widget_frame,
                    command = lambda value: print(value),
                    from_ = 0,
                    to = 100,
                    length = 300,
                    orient = "vertical",
                    variable = scale_double)

# Progress Bar
progress_1 = ttk.Progressbar(widget_frame,
                             variable = scale_double,
                             maximum = 100,
                             length = 300,
                             orient = "horizontal",
                             mode = "determinate")
# progress_1.start()  # Automatic start the progress. progress_1.strat(stepsize)
# progress_1.stop()   # Use for automaticly stop the progress bar

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(widget_frame,
                                          width = 100,
                                          height = 10)

# Excercise
# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the brogress bar
excer_frame = ttk.Frame(window)

excer_int = tk.IntVar()

excer_progress = ttk.Progressbar(excer_frame,
                                 variable = excer_int,
                                 maximum = 100,
                                 orient = "vertical")

excer_slider = ttk.Scale(excer_frame,
                         variable = excer_int,
                         from_ = 0,
                         to = 100,
                         orient = "vertical")

excer_label = ttk.Label(excer_frame,
                        textvariable = str(excer_int))

excer_progress.start()

label_1.pack()
scale_1.pack()
progress_1.pack()
scrolled_text.pack()
widget_frame.pack()
excer_progress.pack(side = "left")
excer_slider.pack(side = "left")
excer_label.pack(side = "left")
excer_frame.pack(pady = 10)

# Run
window.mainloop()
