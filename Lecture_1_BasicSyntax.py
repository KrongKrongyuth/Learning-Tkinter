import tkinter as tk        # Give the basic logic
from tkinter import ttk     # Give the basic widget

def convert() :
    # print(entry.get())        # entry.get() will get the value in entry box --> NOT COMMONLY USE
    # print(entry_int.get())    # get the data from entey_int instead
    cel_temp = entry_int.get()
    fah_temp = (9/5 * cel_temp) + 32
    return output_string.set(str(fah_temp) + "  Fahrenheit")

# Window --> Create Window
window = tk.Tk()
window.title("Demo Tkinter")    # Change application tile
window.geometry("400x200")      # Config the window size Syntax -> window.geometry("WidthxHeight")

# Widget(Title)
title_label = ttk.Label(master = window, text = "Celsius to Fahrenheit", font = "Calibri 24 bold")    
# Create text title place on the "master" window
# Config the fontsize by using parameter font = "font_name font_size bold"
title_label.pack()       # Show the title widget on the screen

# Widget(Input field) --> Entry Field, Button
input_frame = ttk.Frame(master = window)                                            # Create the frame that we can put widget into
entry_int = tk.IntVar()                                                             # Create the variable that can contain int data
entry = ttk.Entry(master = input_frame, textvariable = entry_int)                   # Create Entry box, textvariable -> move the data from entry into some vairable in this case is entey_int
button = ttk.Button(master = input_frame, text = "Convert", command = convert)      # Create button with command (Do not call the function because pressing the button will call the function instead)
entry.pack(side = "left", padx = 10)                                                # Pack Entry box into left side of input_frame
button.pack(side = "left")                                                          # Pack button into input_frame (below the entry), In this case after we are using side = "left" it will place next to each other.
input_frame.pack(pady = 10)                                                         # Pack input_frame into window (below the label 10 pixels)
# ** Program will place the layout following by order of pack()

# Widget(Output)
output_frame = ttk.Frame()
output_string = tk.StringVar()
output_label = ttk.Label(master = output_frame, 
                         text = "Output", 
                         font = "Calibri 24",)
output_show = ttk.Label(master = output_frame,
                        textvariable = output_string,
                        font = "Calibri 24")
output_label.pack()
output_show.pack(pady = 5)
output_frame.pack(pady = 5)

# Run
window.mainloop()