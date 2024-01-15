"""
This is Lecture 9
Treeview (Tables)
"""

import tkinter as tk
from tkinter import ttk
from random import choice   # choice use for random element from array/tuple

# Window
window = tk.Tk()
window.title("Lecture 9 Treeview (Tables)")

# Data
first_names = ["Bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna", "Lisa"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook", "Taylor", "Walker", "Clack"]

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 9",
                    font = "THSarabunPSK 24 bold")

entry_1 = ttk.Entry(widget_frame)

button_1 = ttk.Button(widget_frame,
                      text = "Button")

# Treeview
table_1 = ttk.Treeview(widget_frame,
                       columns = ("First", "Last", "Email"),
                       show = "headings")
# show = "headings" --> use for show the element on the left side
table_1.heading("First", text = "First name")
table_1.heading("Last", text = "Surname")
table_1.heading("Email", text = "Email")

# Inseart values into a table
# table_1.insert(parent = "", index = 0, values = ("John", "Doe", "JohnDoe@email.com"))
# insert single line
# parent = "" --> insert data to the main table
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = str(first) + (last) + "@email.com"
    data = [first, last, email]
    table_1.insert(parent = "", index = i, values = data)

table_1.insert(parent = "", index = tk.END, values = ("XXXXX", "YYYYY", "ZZZZZ"))
# tk.END --> use for navigate to the end of the table

# Events
def item_select(_):
    """
    This function use for select multiple items from table
    """
    print(table_1.selection())
    for row_index in table_1.selection():
        print(table_1.item(row_index)["values"])
def delete_items(_):
    """
    This function use for delete the items from table
    """
    row = table_1.selection()
    for row_index in row:
        table_1.delete(row_index)
# table_1.bind("<<TreeviewSelect>>", lambda event: print(table_1.selection()))
# table_1.selection() --> use for determine what is the row that we are selected
table_1.bind("<<TreeviewSelect>>", item_select)
table_1.bind("<Delete>", delete_items)

label_1.pack()
entry_1.pack()
button_1.pack()
table_1.pack(fill = "both", expand = True)
widget_frame.pack()

# Run
window.mainloop()
