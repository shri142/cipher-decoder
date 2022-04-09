# imports
import main as mn
import tkinter
from string import ascii_letters

# create a title
placeholder_label = mn.tkinter.Label(text = "                                   ", font = ("times", 20), bg = "light grey")
placeholder_label.grid(row =0 , column =0 )

title_label = mn.tkinter.Label(text = "Cryptographic Ciphers", font = ("times", 20), bg = "light grey")
title_label.grid(row =0 , column =1 )

placeholder_label = mn.tkinter.Label(text = "                               ", font = ("times", 20), bg = "light grey")
placeholder_label.grid(row =0 , column =2 )


# encryption_message
encryption_message = mn.tkinter.Label(text = "Encrypt", font = ("times", 17), pady = 20, bg = "light blue")
encryption_message.grid(row = 1, column = 0, sticky = mn.tkinter.W)

# decryption_message
decryption_message = mn.tkinter.Label(text = "Decrypt", font = ("times", 17), pady = 20, bg = "light blue")
decryption_message.grid(row = 1, column = 2, sticky = mn.tkinter.E)



# loop the program
if __name__ == "__main__":
    mn.root_window.mainloop()
