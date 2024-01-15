"""
This is Lecutre 14
Window Customizing
"""

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Lecture 14 Window Customizing")
# window.geometry("widthxheigh+left+top")   # Left and top argrument use for set the window location
# window.geometry("600x400+750+250")
window.iconbitmap("my_icon.ico")    # In mac we can't change the icon

# Excercise
# Start the window in the middle of the screen
window_width = 600
window_height = 400
display_width = window.winfo_screenmmwidth()
display_height = window.winfo_screenmmheight()

left = (display_width/2) + (window_width/2)
top = (display_height/2) + (window_height/2)
window.geometry(f"{window_width}x{window_height}+{int(left)}+{int(top)}")

# Window size
window.minsize(width = 300, height = 200)   # Set the minsize
# window.maxsize(width = 800, height = 600) # Set the maxsize
# window.resizable(horizontal, verttcal)
window.resizable(True, False)

# Screen attibutes
print(window.winfo_screenmmwidth())     # Show width
print(window.winfo_screenmmheight())    # Show height

# Window attributes
window.attributes("-alpha", 1)    # Set the window transparency [0,1]. 1 --> Not transparence
window.attributes("-topmost", True) # Put the window to the top layer

# Security event
window.bind("<Escape>", lambda event: window.quit())
# We need to set this command because some of attribute
# can make impossible to close the window.

# Window attributes
# window.attributes("-disable", True)   # Not working in macos
# window.attributes("-fullscreen", True)  # Fullscreen

# Title bar
# window.overrideredirect(True)   # Not show the title bar
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = "se")

# Widget
widget_frame = ttk.Frame(window)

label_1 = ttk.Label(widget_frame,
                    text = "Welcome to Lecture 14",
                    font = "THSarabunPSK 24 bold")

label_1.pack()
widget_frame.pack()

# Run
window.mainloop()
