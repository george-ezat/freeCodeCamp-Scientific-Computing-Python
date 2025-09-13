# -----------------------------------------------
# + Author: George Ezzat
# -----------------------------------------------

import os
from termcolor import colored as cr
import string

# -----------------------------------------------
# Caesar Cipher
# -----------------------------------------------


def caesar_cipher(message, offset, encrypt=True):
    # Determine encryption (1) or decryption (-1) direction
    direction = 1 if encrypt else -1
    alphabet = string.ascii_lowercase
    final_message = ""

    for char in message.lower():
        if not char.isalpha():  # Non-alphabetic characters remain unchanged
            final_message += char
        else:
            # Calculate new position with wrap-around using modulo
            index = (alphabet.find(char) + offset * direction) % len(alphabet)
            final_message += alphabet[index]

    return final_message


# -----------------------------------------------
# Vigenere Cipher
# -----------------------------------------------

def vigenere_cipher(message, key, encrypt=True):
    # Determine encryption (1) or decryption (-1) direction
    direction = 1 if encrypt else -1
    alphabet = string.ascii_lowercase
    final_message = ""

    key_index = 0
    for char in message.lower():
        if not char.isalpha():  # Non-alphabetic characters remain unchanged
            final_message += char
        else:
            # Get current key character (cycling through key)
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculate offset based on key character position
            offset = alphabet.find(key_char)
            # Calculate new position with wrap-around using modulo
            index = (alphabet.find(char) + offset * direction) % len(alphabet)
            final_message += alphabet[index]

    return final_message

# -----------------------------------------------
# Terminal Interface
# -----------------------------------------------


def clear_screen():
    if os.name == "nt":  # "nt" refers to Windows
        os.system("cls")
    else:  # "posix" for Unix-like systems (Linux, macOS)
        os.system("clear")


# -----------------------------------------------


def header():
    clear_screen()
    print(cr("-" * 20, color="cyan"))
    print(cr("Ciphers".center(20), color="cyan"))
    print(cr("-" * 20, color="cyan"))


# -----------------------------------------------


def menu():
    header()
    print("Choose an option:")
    print("1. Caesar Cipher - Encrypt")
    print("2. Caesar Cipher - Decrypt")
    print("3. Vigenere Cipher - Encrypt")
    print("4. Vigenere Cipher - Decrypt")
    print("0. Exit")


# -----------------------------------------------


def get_choice():
    try:
        choice = int(input("\nEnter your choice (0-4): ").strip())
        if choice not in [0, 1, 2, 3, 4]:
            raise Exception
        return choice
    except:
        print(cr("\nInvalid choice!", color="red", attrs=["bold"]))
        return get_choice()


# -----------------------------------------------


def get_offset():
    try:
        offset = int(input("Enter the offset (number): ").strip())
        return offset
    except ValueError:
        print(cr("\nInvalid offset. Please enter a number.\n", color="red", attrs=["bold"]))
        return get_offset()


# -----------------------------------------------


def get_key():
    try:
        key = input("Enter the key (letters only): ").strip().lower()
        if not key.isalpha():
            raise Exception
        return key
    except:
        print(cr("\nInvalid key. Key must contain only letters.\n", color="red", attrs=["bold"]))
        return get_key()


# -----------------------------------------------

def ciphers():
    menu()
    choice = get_choice()

    while choice:
        message = input("Enter your message: ").strip()

        if choice in [1, 2]:  # Caesar Cipher
            offset = get_offset()
            if choice == 1:
                print(cr(f"\nEncrypted Message: {caesar_cipher(message, offset)}", color="green", attrs=["bold"]))
            else:
                print(cr(f"\nDecrypted Message: {caesar_cipher(message, offset, False)}", color="blue", attrs=["bold"]))

        elif choice in [3, 4]:  # Vigenere Cipher
            key = get_key()
            if choice == 3:
                print(cr(f"\nEncrypted message: {vigenere_cipher(message, key)}", color='green', attrs=['bold']))
            else:
                print(cr(f"\nDecrypted message: {vigenere_cipher(message, key, encrypt=False)}", color='blue', attrs=['bold']))

        input("\nPress Enter to continue...")
        menu()
        choice = get_choice()

    clear_screen()


# ---------------------------------------------------


# App Execution
if __name__ == "__main__":
    ciphers()