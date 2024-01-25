"""
This is Lecture 15
Multiple Window
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Excercise
# class Extra(tk.Toplevel):
#     """
#     Create extra window
#     """
#     def __init__(self, title:str, size:[list, tuple]):
#         super().__init__()
#         self.title(title)
#         self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
#         self.minsize(size[0], size[1])

#         # Widgets
#         ttk.Label(self, text = "A Label").pack()
#         ttk.Button(self, text = "A Button").pack()
#         ttk.Label(self, text = "Another Label").pack(expand = True)

#     def destroy(self):
#         """
#         Destroy the window
#         """
#         return self.destroy()

class App(tk.Tk):
    """
    Run whole program
    """
    def __init__(self, title:str, size:[list, tuple]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.minsize(size[0], size[1])

        # Widgets
        label_1 = tk.Button(self, text = "Open main window",
                            command = lambda: self.create_window("Extra Window", [300,400,100,50]))
        label_2 = tk.Button(self, text = "Close main window",
                            command = self.close_window)
        label_3 = tk.Button(self, text = "Create yes/no window",
                            command = self.ask_yes_no)

        # Layout
        label_1.pack(expand = True)
        label_2.pack(expand = True)
        label_3.pack(expand = True)

        self.mainloop()

    # https://docs.python.org/3/library/tkinter.messagebox.html --> messagebox details
    def ask_yes_no(self):
        # answer = messagebox.askquestion("Title", "Body")    # Return str of "yes" and "no"
        # print(answer)
        # messagebox.showinfo("Info title", "Some information")
        messagebox.showerror("Info title", "Some information")

    def create_window(self, title:str, size:[list, tuple]):
        self.extra_window = tk.Toplevel()
        self.extra_window.title("extra")
        self.extra_window.title(title)
        self.extra_window.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.extra_window.minsize(size[0], size[1])

        # Widgets
        ttk.Label(self.extra_window, text = "A Label").pack()
        ttk.Button(self.extra_window, text = "A Button").pack()
        ttk.Label(self.extra_window, text = "Another Label").pack(expand = True)

    def close_window(self):
        self.extra_window.destroy()

if __name__ == "__main__":
    app = App("Lecture 15 Multiple Window", (600,500,750,250))