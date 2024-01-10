import tkinter as tk        # Give the basic logic
# from tkinter import ttk   # Give the basic widget
import ttkbootstrap as ttk  # Give the basic widget more than normal ttk
from typing import Final    # Use for create permanent variable

class temp_convert() :

    kelvin_constant: Final[float] = 273.15  # Create permanent

    def convert_to_fah(self) :
        # print(entry.get())        # entry.get() will get the value in entry box --> NOT COMMONLY USE
        # print(entry_int.get())    # get the data from entey_int instead
        cel_temp = entry_int.get()
        fah_temp = (9/5 * cel_temp) + 32
        return output_string.set(str(fah_temp) + "  Fahrenheit")

    def convert_to_kel(self) :
        cel_temp = entry_int.get()
        kel_temp = cel_temp + self.kelvin_constant
        return output_string.set(str(kel_temp) + "  Kelvin")

temp = temp_convert()

# Window --> Create Window
# window = tk.Tk()
window = ttk.Window(themename = "journal")      # Using window function from ttkbootstrap (We can use the ready-made theme from ttkbootstrap)
window.title("Temperature Converter")           # Change application tile
window.geometry("500x200")                      # Config the window size Syntax -> window.geometry("WidthxHeight")

# Widget(Title)
title_frame = ttk.Frame()
title_label = ttk.Label(master = title_frame, 
                        text = "Celsius to Fahrenheit", 
                        font = "Calibri 24 bold")
title_detail = ttk.Label(master = title_frame, 
                         text = "You can enter the temperature in Celsius and select to \n\tconvert it to Fahrenheit or kelvin.",
                         font = "Calibri")
# Create text title place on the "master" window
# Config the fontsize by using parameter font = "font_name font_size bold"
title_label.pack()       # Show the title widget on the screen
title_detail.pack()
title_frame.pack()

# Widget(Input field) --> Entry Field, Button
input_frame = ttk.Frame(master = window)                                # Create the frame that we can put widget into
entry_int = tk.IntVar()                                                 # Create the variable that can contain int data
entry = ttk.Entry(master = input_frame, textvariable = entry_int)       # Create Entry box, textvariable -> move the data from entry into some vairable in this case is entey_int
fah_button = ttk.Button(master = input_frame, 
                        text = "To Fahrenheit", 
                        command = temp.convert_to_fah)                  # Create button with command (Do not call the function because pressing the button will call the function instead)
kel_button = ttk.Button(master = input_frame, 
                        text = "To Kelvin", 
                        command = temp.convert_to_kel)
entry.pack(side = "left", padx = 10)                                    # Pack Entry box into left side of input_frame
fah_button.pack(side = "left", padx = 5)                                # Pack button into input_frame (below the entry), In this case after we are using side = "left" it will place next to each other.
kel_button.pack(side = "left")
input_frame.pack(pady = 10)                                             # Pack input_frame into window (below the label 10 pixels)
# ** Program will place the layout following by order of pack()

# Widget(Output)
output_frame = ttk.Frame()
output_string = tk.StringVar()
output_label = ttk.Label(master = output_frame, 
                         text = "Output", 
                         font = "Calibri 24",)
output_show = ttk.Label(master = output_frame,
                        textvariable = output_string,
                        font = "Calibri 24 bold")
output_label.pack()
output_show.pack(pady = 5)
output_frame.pack(pady = 5)

# Run
window.mainloop()