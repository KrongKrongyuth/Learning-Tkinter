"""
This is Lecture 13
Menu
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 13 Menu")
window.geometry("600x400")

# Create main frame
main_frame = ttk.Frame(window, relief = "ridge", borderwidth = 5)

# Create manu button
menu_button_1 = ttk.Menubutton(main_frame, text = "Menu")
menu_button_2 = ttk.Menubutton(main_frame, text = "Option")

# Create submenu
test_var = tk.BooleanVar(value = False)

# Submenu 1
sub_menu_1 = tk.Menu(menu_button_1, tearoff = 0)
menu_button_1["menu"] = sub_menu_1    # This line use only first submenu
sub_menu_1.add_command(label = "First command", command = lambda: print(test_var.get()))
sub_menu_1.add_checkbutton(label = "First Check Button", onvalue = True, offvalue = False,
                           variable = test_var)

# Submenu 2
sub_menu_2 = tk.Menu(menu_button_1, tearoff = 0)
sub_menu_2.add_command(label = "Secound Command", command = lambda: print("Secound"))

# Submenu 3
sub_menu_3 = tk.Menu(menu_button_1, tearoff = 0)
sub_menu_3.add_command(label = "Third command", command = lambda: print("Third"))

sub_menu_2.add_cascade(label = "Secound Cascade", menu = sub_menu_3)
sub_menu_1.add_cascade(label = "First Cascade", menu = sub_menu_2)  # Create sub-menu like object

# Excercise
excer_int = tk.IntVar(value = 0)

sub_menu_excer = tk.Menu(menu_button_2)
menu_button_2["menu"] = sub_menu_excer
sub_menu_excer.add_radiobutton(label = "1",
                               value = 1,
                               variable = excer_int)
sub_menu_excer.add_radiobutton(label = "2",
                               value = 2,
                               variable = excer_int)
sub_menu_excer.add_separator()  # Add separator line
sub_menu_excer.add_command(label = "Print radio",
                           command = lambda: print(excer_int.get()))

menu_button_1.pack(side = "left")
menu_button_2.pack(side = "left")
main_frame.pack(fill = "x") # Fill the x axis

# Run
window.mainloop()
