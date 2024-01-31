"""
This is Lecture 1
Introduction to Styling
"""

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    """
    Run the whole app
    """
    def __init__(self, title:str, size:[list, tuple]):
        # Window
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.minsize(size[0], size[1])

        # Style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        # We need to change the main theme for using more styling options

        # Widgets
        self.create_widget().pack(expand = True)
        self.excercise_frame().pack(expand = True)

        # Run
        self.mainloop()

    def create_widget(self):
        """
        Create widgets
        """
        frame = ttk.Frame(self)

        # print(font.families())
        # This will check the font families --> This function need to run in side the window.

        # Style --> Create styling object
        style = ttk.Style()
        print(style.theme_names())    # Check the theme in our os
        # style.theme_use("default")

        style.configure("new.TButton",
                        foreground = "yellow",
                        font = ("STIX Two Math", 20))
        # style.configure("TWidget", background = "color") use for change the theme of whole widgets
        style.map("new.TButton",
                foreground = [("pressed", "red"), ("disabled", "yellow")],
                background = [("pressed", "green"), ("active", "blue")])
        # Setting the style while action occur.

        # Widget
        label = tk.Label(frame,
                        text = "A Label\nThen type on another line",
                        background = "red",
                        foreground = "white",
                        font = ("STIX Two Math", 20),   # font = (font, font_size)
                        justify = "left"    # Justify the text position "left", "center", "right".
                        )
        button = ttk.Button(frame,
                        text = "A Button",
                        style = "new.TButton"   # Set the style to our widgets
                        )

        # Layout
        label.pack()
        button.pack()

        return frame

    def excercise_frame(self):
        """
        add a frame with and height and give it a pink background color
        """
        # Styling
        style = ttk.Style()
        style.configure("excercise.TFrame",
                        background = "pink")
        style.configure("Debug.TLabel",
                        background = "red")

        # Frame
        frame = ttk.Frame(self,
                        width = 100,
                        height = 100,
                        style = "excercise.TFrame")

        # Debug
        # Label = ttk.Label(frame, text =  "Debug", style = "Debug.TLabel")
        # Label.pack(expand = "True", fill = "both")

        return frame

if __name__ == "__main__":
    window_size = (400,300,750,250)
    app = App("Lecture 1 Introduction to Styling", window_size)
