
import tkinter
from tkinter import ttk
from string import ascii_letters

# main class

class MainWindow(tkinter.Tk):
    """ This is the main window, a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ The main window properties """
        # main window title
        self.title("Cryptographic Ciphers")
        # main window size
        self.geometry("1320x420")
        # main window color
        self.configure(background = "light blue")

    # encrption function
    def encryption(self, message, shifter_key):
        encryption_result = ""

        # go through every character
        for i in range(len(message)):
            letter = message[i]
            if (letter.isalpha()):
                if (letter.isupper()):
                    encryption_result += chr((ord(letter) + shifter_key - 65)%26 +65)
                elif (letter.islower()):
                    encryption_result += chr((ord(letter) + shifter_key - 97)%26 +97)
            elif (letter.isnumeric()):
                encryption_result += letter
            else:
                if (letter == " "):
                    encryption_result += " "
                if (letter == "."):
                    encryption_result += "."

        return encryption_result



root_window = MainWindow()

if __name__ == "__main__":
    root_window.mainloop()




