# -----------------------------------------------
# + Author: George Ezzat
# -----------------------------------------------

import os
import string
from secrets import choice
from random import shuffle
from termcolor import colored as cr

# -----------------------------------------------

# --- Constants ---
# Defines the total pool of characters available for unique generation.

ALL_PRINTABLE_CHARS = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
MAX_UNIQUE_LENGTH = len(ALL_PRINTABLE_CHARS) # This is 94


# -----------------------------------------------


def clear_screen():
    """Clears the console screen."""
    # "nt" refers to windows
    # else >> 'posix' for Unix-like systems (Linux, macOS)
    os.system('cls' if os.name == 'nt' else 'clear')


# -----------------------------------------------


def header():
    """Prints the application header."""
    clear_screen()
    print(cr('-' * 20, color='cyan'))
    print(cr('Password Generator'.center(20), color='cyan'))
    print(cr('-' * 20, color='cyan'))


# -----------------------------------------------


def get_user_choice(prompt):
    """
    Gets a 'yes' or 'no' answer from the user.
    Defaults to 'yes' if the user just presses Enter.
    """
    answer = input(prompt).strip().upper()
    return answer == 'Y' or not answer # 'not answer' handles the Enter key


# -----------------------------------------------


def get_valid_length(allow_duplicates):
    """
    Prompts the user for a valid password length and returns it.
    """

    while True:
        try:
            length = int(input('Enter password length: ').strip())
            if length <= 0:
                print(cr('\nLength must be a positive number.\n', color='red', attrs=['bold']))
                continue
            if not allow_duplicates and length > MAX_UNIQUE_LENGTH:
                print(cr(f'\nInvalid Length!\n', color='red', attrs=['bold']))
                print(cr(f'Note: Max length for unique-characters password is {MAX_UNIQUE_LENGTH}.\n', color='yellow', attrs=['bold']))
                continue
            return length
        except ValueError:
            print(cr('\nInvalid input! Please enter a number.\n', color='red', attrs=['bold']))


# -----------------------------------------------


def generate_password(length, constraints, allow_duplicates):
    """
    Generates a password that meets the specified constraints.
    """

    # 1. Build the full character pool
    allowed_chars = list(string.ascii_lowercase)
    password = []
    for chars, is_enabled in constraints.items():
        if is_enabled:
            allowed_chars.extend(chars)
            password.append(choice(chars))

    # 2. Fill the rest of the password length according to duplicates allowance
    remaining_length = length - len(password)
    if allow_duplicates:
        password.extend([choice(allowed_chars) for _ in range(remaining_length)])
    else:
        # shuffle and slice method
        filler_chars = list(set(allowed_chars) - set(password))
        shuffle(filler_chars)
        password.extend(filler_chars[:remaining_length])

    # 3. Shuffle and Return
    shuffle(password)
    return ''.join(password)


# -----------------------------------------------


def password_generator_app():
    """Main function to run the password generator application."""

    header()
    print(cr(f'Info:\n - Max length for unique-characters password is {MAX_UNIQUE_LENGTH}.\n - Press "Enter" for default options (Yes).\n', color='yellow'))

    constraints = {
        string.digits: get_user_choice("Include numbers? (Y/n) "),
        string.ascii_uppercase: get_user_choice("Include uppercase letters? (Y/n) "),
        string.punctuation: get_user_choice("Include special characters? (Y/n) "),
    }

    allow_duplicates = get_user_choice("Allow duplicate characters? (Y/n) ")
    length = get_valid_length(allow_duplicates)

    password = generate_password(length, constraints, allow_duplicates)

    print('\nYour password is:', cr(f"{password}", color='green', attrs=['bold']))

# -----------------------------------------------


# App Execution
if __name__ == '__main__':
    password_generator_app()
