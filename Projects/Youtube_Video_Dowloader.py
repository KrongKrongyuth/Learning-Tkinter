"""
This is Youtube Video Dowloader with GUI.

In this project i use pytube and tkinter
to dowload video and create a simple gui.
"""

import tkinter as tk
from icecream import ic
from tkinter import ttk
from pytube import YouTube, Playlist, Search

VERSION = 1

class Video():
    """
    This class have a bunch of functions that use for
    video dowloading
    """
    def __init__(self, video_source = None):
        self.video_source = video_source
        self.video_title = None
        self.video_url = None

        self.source_classify(self.video_source)

    def source_classify(self, source = None):
        """
        This function will classify input source into url or title
        """
        print("\nsource_classify Running...\n")
        if source is not None :
            if "https://www.youtube.com" in source or "https://youtu.be" in source :
                self.video_url = source
            else :
                self.video_title = source
        else : return "YOUR SOURCE IS INVALID"

    def video_search(self):
        """
        This function use for Youtube search
        """
        print("\nvideo_search Running...\n")
        video_list, search_result = [], None
        if self.video_title is not None :
            search_result = Search(self.video_title).results
            for video in search_result:
                video_list.append((video.title, video.watch_url))
            return video_list
        if self.video_url is not None :
            search_result = [(YouTube(self.video_url).title, YouTube(self.video_url).watch_url)]
            return search_result
        if self.video_title is None and self.video_url is None :
            return "YOUR SOURCE IS INVALID"

    def video_dowload(self, video_link = None, load_type = None, output_path = None):
        """
        This function use for dowload the video
        """
        print("\nvideo_dowload Running...\n")
        if (video_link is not None) and (load_type is not None):
            dowload_type = {"Audio only": 0,
                            "Lowest resolution": 1,
                            "Highest resolution": 2}
            video_selected = YouTube(video_link)
            if dowload_type[load_type] == 0 :
                video_selected.streams.get_audio_only().download(output_path = output_path)
            elif dowload_type[load_type] == 1 :
                video_selected.streams.get_lowest_resolution().download(output_path = output_path)
            elif dowload_type[load_type] == 2 :
                video_selected.streams.get_highest_resolution().download(output_path = output_path)
        elif ((video_link is None) or (load_type is None)) and (self.video_url is not None) :
            video_selected = YouTube(self.video_url)
            video_selected.streams.get_highest_resolution().download(output_path = output_path)
        else : return "YOUR SOURCE IS INVALID"

class App():
    """
    This class use for create Tkinter layout
    """
    def __init__(self):
        self.main_window()

    def main_window(self):
        """
        Combine all the widget to create main window.
        """
        # Window
        window = tk.Tk()
        window.title("Youtube Video Dowloader")
        window.geometry("600x500+750+350")

        # Tkinter variables
        self.video_link = tk.StringVar(value = None)

        # Widget
        self.widget_menu(display = window)
        self.widget_label(display = window)
        self.widget_entry(display = window)
        self.widget_table(display = window)

        # Run
        window.mainloop()

    def widget_menu(self, display):
        """
        Create menu bar widget
        """
        # Menu Bar
        menu_bar = ttk.Frame(display, relief = "raised", borderwidth = 2)
        app_menu = ttk.Menubutton(menu_bar, text = "About this app")

        # Setting Submenu
        setting_submenu = tk.Menu(app_menu, tearoff = False)
        setting_submenu.add_command(label = "Fullscreen", command = lambda: display.attributes("-fullscreen", True))

        # Main Submenu
        main_submenu = tk.Menu(app_menu, tearoff = False)
        app_menu["menu"] = main_submenu
        main_submenu.add_cascade(label = "Setting", menu = setting_submenu)
        main_submenu.add_separator()
        main_submenu.add_command(label = "Quit", command = lambda: display.quit())

        # Pack
        app_menu.pack(side = "left")
        menu_bar.pack(side = "top", fill = "x")

    def widget_label(self, display):
        """
        Create label widget
        """
        # Frame
        title_frame = ttk.Frame(display, relief = "raised", borderwidth = 2)

        # Widgets
        title_label = ttk.Label(title_frame,
                                text = "Youtube Video Dowloader",
                                font = "THSarabunPSK 30 bold",
                                background = "red")

        # Pack
        title_label.pack(side = "top")
        title_frame.pack(side = "top", fill = "x", pady = 30)

    def widget_entry(self, display):
        """
        Create entry widget
        """
        # Frame
        entry_frame = ttk.Frame(display, relief = "raised", borderwidth = 2)

        # Widgets
        source_entry = ttk.Entry(entry_frame, textvariable = self.video_link)
        entry_label = ttk.Label(entry_frame,
                                text = "Video source (Link/Title).",
                                font = "THSarabunPSK 18")
        entry_button = ttk.Button(entry_frame,
                                text = "Search",
                                command = lambda: self.widget_table(display))

        # Pack
        entry_label.pack(side = "top")
        source_entry.pack(side = "left")
        entry_button.pack(side = "left")
        entry_frame.pack(side = "top")

    def widget_table(self, display):
        """
        Create table to show the video list
        """
        # Frame
        table_frame = ttk.Frame(display, relief = "raised", borderwidth = 2)

        # Widgets
        video_table = ttk.Treeview(table_frame,
                                columns = ("title", "link"),
                                show = "headings")
        video_table.heading("title", text = "Video Title")
        video_table.heading("link", text = "Video Link")

        # Insert data into table
        if self.video_link is not None:
            self.table_insert(table = video_table, promp = self.video_link.get())

        video_table.pack(side = "top", fill = "both")
        table_frame.pack(side = "top", fill = "both", pady = 20)

    def table_insert(self, table, promp):
        """
        This fucntion use for insert data into table
        """
        # Video List
        video_list = ic(Video(promp).video_search())

        # Insert table
        for order in range(len(video_list)) :
            table.insert(parent = "", index = order, values = video_list[order])

class Run():
    """
    This classes use for manage the flow of our program
    """
    def __init__(self):
        self.main()

    def start(self):
        """
        Print Starting status
        """
        print("\nRunning...\n")

    def end(self):
        """
        Print Ending status
        """
        print("\nEnding...\n")

    def main(self):
        """
        Main function
        """
        self.start()
        App()
        # vi = Video(video_source = "Kodoku - Insomnia")
        # for search_list in vi.video_search():
        #     print(f"\nVideo title: {search_list[0]}\nVideo url: {search_list[1]}\n")
        # vi.video_dowload(video_link = vi.video_search()[0][1], type = "Highest resolution")
        self.end()

if __name__ == "__main__":
    Run()

# search_result = Search("Kodoku - Insomnia")
# video_list = search_result.results
# for video in video_list:
#     print(f"\nVideo title: {video.title}\nVideo url: {video.watch_url}\n")
# video_test = YouTube(video_list[0]).streams.get_highest_resolution().download()

# video = YouTube("https://www.youtube.com/watch?v=9l7NBtxB-r8")
# print(video.streams)
