"""
This is Lecture 10
Classes
"""

import tkinter as tk
from tkinter import ttk

# add tk.Tk in side the argrument to make App() to ac like "window" -> make App() be child
class App(tk.Tk):
    """
    This class use for Lecture 10 Classes
    """
    def __init__(self, title:str, size:[tuple,list]):
        # main setup
        super().__init__()
        # .super() will make me access to the __init__ attribute from parent class
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()

class Menu(ttk.Frame):
    """
    This class use for create Menu Frame
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

        # Widget
        self.create_widgets()

    def create_widgets(self):
        """
        This method use for create widgets in Menu Frame.
        """
        menu_button1 = tk.Button(self, text = "Button 1")
        menu_button2 = tk.Button(self, text = "Button 2")
        menu_button3 = tk.Button(self, text = "Button 3")

        menu_slider1 = ttk.Scale(self, orient = "vertical")
        menu_slider2 = ttk.Scale(self, orient = "vertical")

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text = "Check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text = "Check 2")

        entry = ttk.Entry(self)

        # Create the grid
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        # Place
        menu_button1.grid(row = 0, column = 0, sticky = "nsew", columnspan = 2)
        menu_button2.grid(row = 0, column = 2, sticky = "nsew")
        menu_button3.grid(row = 1, column = 0, sticky = "nsew", columnspan = 3)

        menu_slider1.grid(row = 2, column = 0, sticky = "nsew", rowspan = 2, pady = 20)
        menu_slider2.grid(row = 2, column = 2, sticky = "nsew", rowspan = 2, pady = 20)

        # Toggle layout
        toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = "nsew")
        menu_toggle1.pack(side = "left", expand = True)
        menu_toggle2.pack(side = "left", expand = True)

        # Entry layout
        entry.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = "center")

    def create_layout(self):
        """
        This method use for create layout for every widgets
        """

class Main(ttk.Frame):
    """
    This class use for create Main Frame
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.3, rely = 0, relwidth = 0.7, relheight = 1)

        # Widgets as Classes
        EntryFrame(parent = self,
                label_text = "Label 1",
                label_bg = "red",
                button_text = "Button 1")   # Create entry_frame1
        EntryFrame(parent = self,
                label_text = "Label 2",
                label_bg = "blue",
                button_text = "Button 2")   # Create entry_frame2

class EntryFrame(ttk.Frame):
    """
    This class is the excercise to create entry_frame
    """
    def __init__(self, parent, label_text:str, label_bg:str, button_text:str):
        super().__init__(parent)

        # Attribute
        self.lb_tx = label_text
        self.lb_bg = label_bg
        self.bt_tx = button_text

        # Frame packing
        self.pack(side = "left", expand = True, fill = "both")

        # Widget
        main_label = tk.Label(self, text = self.lb_tx, background = self.lb_bg)
        main_button = tk.Button(self, text = self.bt_tx)

        # Layout
        main_label.pack(expand = True, fill = "both")
        main_button.pack(expand = True, fill = "both", pady = 10)

App("Lecture 10 Classes", (600, 600))
