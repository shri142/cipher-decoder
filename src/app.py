# imports
import main as mn
import tkinter
from string import ascii_letters

# vigenere cipher

from string import ascii_letters

# -----------------------------------------------------------------------------------------------------

# cipher_combo_box
cipher_combo_box = mn.ttk.Combobox(values=[
    "caesar cipher",
    "ROT13",
    "Vigenere cipher"
])
cipher_combo_box.grid(row=4, column=0, padx=35)
cipher_combo_box.current(2)


def get_cipher_combo_box_value():
    cipher_value = cipher_combo_box.get()
    return cipher_value


the_cipher_value = get_cipher_combo_box_value()


# logical functions
# move encrypted text
def move_text_to_decrypt_box():
    # check which cipher was selected
    """
    if combox value == cipher A:
        do function
    elif combox value == cipher B:
        do function
    """
    if (the_cipher_value == "caesar cipher"):
        empty_message = "Error! The encryption box or shifter key box is empty\n"
        moving_text = encryption_box.get("1.0", mn.tkinter.END)
        shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)
        # check if there is a empty error message
        if empty_message in moving_text:
            encryption_box.delete("1.0", mn.tkinter.END)

        elif (len(moving_text) < 2) or len(shifter_key_number) < 2:
            # checking if the text box is empty
            decrption_box.insert("1.0", empty_message)

        else:
            # encrypting the data and inserting it to the decryption box
            decrption_box.insert("1.0", mn.MainWindow.encryption(moving_text, moving_text, int(shifter_key_number)))
            encryption_box.delete("1.0", mn.tkinter.END)
    elif (the_cipher_value == "ROT13"):
        empty_message = "Error! The encryption box or shifter key box is empty\n"
        moving_text = encryption_box.get("1.0", mn.tkinter.END)
        shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)
        # check if there is a empty error message
        if empty_message in moving_text:
            encryption_box.delete("1.0", mn.tkinter.END)

        elif (len(moving_text) < 2) or len(shifter_key_number) < 2:
            # checking if the text box is empty
            decrption_box.insert("1.0", empty_message)

        else:
            # encrypting the data and inserting it to the decryption box
            decrption_box.insert("1.0", mn.MainWindow.encrypt_rot13(moving_text, moving_text, int(shifter_key_number)))
            encryption_box.delete("1.0", mn.tkinter.END)

    elif (the_cipher_value == "Vigenere cipher"):

        pattern = {}
        dictionary = pattern.fromkeys(ascii_letters)
        sorted_dictionary = {}

        # assigning values
        counter = 0
        counter2 = 0
        for key, value in dictionary.items():
            if counter <= 25:
                value = counter
                counter += 1
                sorted_dictionary[key] = value
            else:
                value = counter2
                counter2 += 1
                sorted_dictionary[key] = value

        # print(sorted_dictionary)

        # check the alphabet position
        def check_alphabet_position(letter):
            if letter.isalpha():
                alphabet_postion = sorted_dictionary[letter]
            else:
                alphabet_postion = 0
            return alphabet_postion