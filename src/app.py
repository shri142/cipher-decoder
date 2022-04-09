# imports
import main as mn
import tkinter
from string import ascii_letters

# create a title
placeholder_label = mn.tkinter.Label(text = "                                            ", font = ("times", 20), bg = "light blue")
placeholder_label.grid(row =0 , column =0 )

title_label = mn.tkinter.Label(text = "Cryptographic Ciphers", font = ("times", 20), bg = "light grey")
title_label.grid(row =0 , column =1 )

placeholder_label = mn.tkinter.Label(text = "                      ", font = ("times", 20), bg = "light blue")
placeholder_label.grid(row =0 , column =2 )



# loop the program
if __name__ == "__main__":
    mn.root_window.mainloop()
