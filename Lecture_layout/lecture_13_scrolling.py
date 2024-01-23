"""
This is lecture 13
Scrolling
"""

import tkinter as tk
from tkinter import ttk
from random import randint, choice

class App(tk.Tk):
    """
    Run whole program
    """
    def __init__(self, title:str, size:[tuple, list]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.minsize(size[0], size[1])

        # Widget
        canvas = tk.Canvas(self,
                        background = "white",
                        scrollregion = (0,0,2000,5000))
        canvas.create_line(0,0,2000,5000, fill = "green", width = 10)
        for i in range(100):
            left = randint(0,2000)
            top = randint(0,5000)
            right = left + randint(10,500)
            bottom = top + randint(10,500) 
            color = choice(("red", "green", "blue", "yellow", "orange"))
            canvas.create_rectangle(left, top, right, bottom, fill = color)

        # Scrollbar
        scrollbar_y = ttk.Scrollbar(self, orient = "vertical", command = canvas.yview)
        canvas.configure(yscrollcommand = scrollbar_y.set)
        scrollbar_x = ttk.Scrollbar(self, orient = "horizontal", command = canvas.xview)
        canvas.configure(xscrollcommand = scrollbar_x.set)

        # Mousewheel scrolling
        canvas.bind("<MouseWheel>", lambda evnet: canvas.yview_scroll(-evnet.delta, "units"))
        canvas.bind("<Control-MouseWheel>", lambda evnet: canvas.xview_scroll(-evnet.delta, "units"))

        # Text
        text = tk.Text(self)
        for i in range(1, 200):
            text.insert(f"{i}.0", f"text: {i} \n")
        scrollbar_text = ttk.Scrollbar(self, orient = "vertical", command = text.yview)
        text.configure(yscrollcommand = scrollbar_text.set)
        text.bind("<MouseWheel>", lambda evnet: text.yview_scroll(-evnet.delta, "units"))

        # Treeview
        table = ttk.Treeview(self, columns = ["Firstname", "Surname"], show = "headings")
        table.heading("Firstname", text = "First Name")
        table.heading("Surname", text = "Last Name")
        first_name = ["Krong", "Aranya"]
        last_name = ["Krongyuth", "Frans"]
        for i in range(100):
            data = [choice(first_name), choice(last_name)]
            table.insert(parent = "",index = tk.END, values = data)
        scrollbar_table = ttk.Scrollbar(self, orient = "vertical", command = table.yview)
        table.configure(yscrollcommand = scrollbar_table.set)
        table.bind("<MouseWheel>", lambda event: table.yview_scroll(-event.delta, "units"))

        # Layout
        # text.pack(expand = True, fill = "both")
        # scrollbar_text.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

        canvas.pack(expand = True, fill = "both")
        scrollbar_y.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")
        scrollbar_x.place(relx = 0, rely = 1, relwidth = 1, anchor = "sw")

        # table.pack(expand = True, fill = "both")
        # scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

        self.mainloop()

if __name__ == "__main__":
    app = App("Lecture 13 Scrolling", (600,400,750,250))