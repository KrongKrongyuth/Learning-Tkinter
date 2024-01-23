"""
This is Lecture 12
Responsive Layout
"""

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    """
    Create window/Run whole program
    """
    def __init__(self, title:str, size:[tuple, list]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.minsize(size[0], size[1])

        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = "both")

        SizeNotifier(self, {1200: self.create_large_layout,
                            600: self.create_medium_layout,
                            300: self.create_small_layout})

        self.mainloop()

    def create_small_layout(self):
        """
        Create small Layout
        """
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        tk.Label(self.frame,
                text = "Label 1",
                background = "red"
                ).pack(expand = True, fill = "both", padx = 10, pady = 5)
        tk.Label(self.frame,
                text = "Label 2",
                background = "green"
                ).pack(expand = True, fill = "both", padx = 10, pady = 5)
        tk.Label(self.frame,
                text = "Label 3",
                background = "blue"
                ).pack(expand = True, fill = "both", padx = 10, pady = 5)
        tk.Label(self.frame,
                text = "Label 4",
                background = "orange"
                ).pack(expand = True, fill = "both", padx = 10, pady = 5)
        self.frame.pack(expand = True, fill = "both")

    def create_medium_layout(self):
        """
        Create medium Layout
        """
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight = 1, uniform = "a")
        self.frame.rowconfigure((0,1), weight = 1, uniform = "a")
        self.frame.pack(expand = True, fill = "both")

        tk.Label(self.frame,
                text = "Label 1",
                background = "red"
                ).grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = 10)
        tk.Label(self.frame,
                text = "Label 2",
                background = "green"
                ).grid(column = 1, row = 0, sticky = "nsew", padx = 10, pady = 10)
        tk.Label(self.frame,
                text = "Label 3",
                background = "blue"
                ).grid(column = 0, row = 1, sticky = "nsew", padx = 10, pady = 10)
        tk.Label(self.frame,
                text = "Label 4",
                background = "orange"
                ).grid(column = 1, row = 1, sticky = "nsew", padx = 10, pady = 10)
        self.frame.pack(expand = True, fill = "both")

    def create_large_layout(self):
        """
        Create large Layout
        """
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1,2,3), weight = 1, uniform = "a")
        self.frame.rowconfigure(0, weight = 1, uniform = "a")
        self.frame.pack(expand = True, fill = "both")

        tk.Label(self.frame,
                text = "Label 1",
                background = "red"
                ).grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = 10)
        tk.Label(self.frame,
                text = "Label 2",
                background = "green"
                ).grid(column = 1, row = 0, sticky = "nsew", padx = 10, pady = 10)
        tk.Label(self.frame,
                text = "Label 3",
                background = "blue"
                ).grid(column = 2, row = 0, sticky = "nsew", padx = 10, pady = 10)
        tk.Label(self.frame,
                text = "Label 4",
                background = "orange"
                ).grid(column = 3, row = 0, sticky = "nsew", padx = 10, pady = 10)
        self.frame.pack(expand = True, fill = "both")

class SizeNotifier:
    """
    Use for changing the size of layout
    """
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = dict(sorted(size_dict.items()))
        self.current_min_size = None
        self.window.bind("<Configure>", self.check_size)
        # <Configure> return x,y and position of the window.

        self.window.update()

        min_height = self.window.winfo_height()
        min_width = list(self.size_dict)[0]
        self.window.minsize(min_width, min_height)


    def check_size(self, event):
        """
        Checking scale of the window
        """
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
                checked_size = min_size

        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[self.current_min_size]()     # Call the method right here.

if __name__ == "__main__":
        App("Lecture 12 Responsive Layout", (400,300,750,250))
