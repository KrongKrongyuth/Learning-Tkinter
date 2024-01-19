"""
This is Lecture 8
Toggling Widget
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry("600x400")
window.title("Hide widgets")

# # Place
# def toggle_label_place():
#     global label_visible
#     if label_visible:
#         label.place_forget()
#         label_visible = False
#     else:
#         label.place(relx = 0.5, rely = 0.5, anchor = "center")
#         label_visible = True

# button = ttk.Button(window, text = "toggle Label", command = toggle_label_place)
# button.place(x = 10, y = 10)

# label_visible = True
# label = ttk.Label(window, text = "A Label")
# label.place(relx = 0.5, rely = 0.5, anchor = "center")

# # Grid
# def toggle_label_grid():
#     global label_visible

#     if label_visible:
#         label.grid_forget()
#         label_visible = False
#     else:
#         label.grid(column = 1, row = 0)
#         label_visible = True

# window.columnconfigure((0,1), weight = 1, uniform = "a")
# window.rowconfigure(0, weight = 1, uniform = "a")

# button = ttk.Button(window, text = "toggle Label", command = toggle_label_grid)
# button.grid(column = 0, row = 0)

# label_visible = True
# label = ttk.Label(window, text = "A Label")
# label.grid(column = 1, row = 0)

# Pack
def toggle_label_pack():
    """
    This function use for toggle in pack method
    """
    global LABEL_VISIBLE

    if LABEL_VISIBLE:
        label.pack_forget()
        # frame.pack(expand = True, before = button)
        LABEL_VISIBLE = False
    else:
        # frame.pack_forget()
        # label.pack(expand = True, before = button)
        label.pack(expand = True)
        LABEL_VISIBLE = True
    # Excercise: fix the coce so that the button stays at the bottom

LABEL_VISIBLE = True
label = ttk.Label(window, text = "A Label")
label.pack(expand = True)

button = ttk.Button(window, text = "toggle Label", command = toggle_label_pack)
button.pack(side = "bottom")

frame = ttk.Frame(window)
# Run
window.mainloop()
