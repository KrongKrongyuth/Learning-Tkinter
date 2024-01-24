"""
This is Lecture 14
Scrollable Widgets
"""

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    """
    Run the whole program
    """
    def __init__(self, title:str, size:[list, tuple]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.minsize(size[0], size[1])

        # # Canvas (with widgets)
        # canvas = tk.Canvas(self, background = "white")
        # canvas.create_window((50,50), window = ttk.Label(canvas, text = "A Label"))
        # canvas.create_window((50,80), window = ttk.Button(canvas, text = "A Button"))
        # # canvas.create_window(position, window)

        # # Layout
        # canvas.pack(expand = True, fill = "both")

        text_list = [("label", "button"),
                    ("thing", "click"),
                    ("third", "something"),
                    ("label1", "button2"),
                    ("label2", "button3"),
                    ("label3", "button3"),
                    ("label4", "button3"),
                    ("label5", "button3"),
                    ("label5", "button3"),
                    ("label5", "button3")]
        list_frame = ListFrame(self, text_list, 100)

        self.mainloop()

class ListFrame(ttk.Frame):
    """
    Contain the widget in the frame
    """
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand = True, fill = "both")

        # Widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # Canvas
        self.canvas = tk.Canvas(self, background = "red", scrollregion = (0,0,self.winfo_width(),self.list_height))
        self.canvas.pack(expand = True, fill = "both")

        # Display frame
        self.frame = ttk.Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand = True, fill = "both", pady = 4, padx = 10)

        # self.canvas.create_window((0,0),
        #                         window = self.frame,
        #                         anchor = "nw",
        #                         width = self.winfo_width(),
        #                         height = self.list_height)
        # We create widget on frame and display it on canvas window.

        # Events
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-(event.delta), "units"))
        self.bind("<Configure>", self.update_size)  # Make frame responsive with window size

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-(event.delta), "units"))
        else:
            height = self.winfo_height()
            self.canvas.unbind_all("<MouseWheel>")

        self.canvas.create_window(
            (0,0),
            window = self.frame,
            anchor = "nw",
            width = self.winfo_width(),
            height = self.list_height
        )

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # Grid layout
        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        # Widgets
        ttk.Label(frame, text = f"#{index}").grid(row = 0, column = 0)
        ttk.Label(frame, text = f"#{item[0]}").grid(row = 0, column = 1)
        ttk.Button(frame, text = f"{item[1]}").grid(row = 0, column = 2, columnspan = 3, sticky = "nsew")

        return frame

if __name__ == "__main__":
    app = App("Lecture 14 Scrollable Widgets", (500,400,750,250))