import tkinter

from tkinter import *
from string import ascii_letters

# main class

class MainWindow(tkinter.Tk):
    """ This is the main window, a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ The main window properties """
        # main window title
        self.title("Cipher decoder")
        # main window size
        self.geometry("730x500")
        # main window color
        self.configure(background = "white")



root_window = MainWindow()

if __name__ == "__main__":
    root_window.mainloop()




