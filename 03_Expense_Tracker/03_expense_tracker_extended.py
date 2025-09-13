# -----------------------------------------------
# + Author: George Ezzat
# -----------------------------------------------

import datetime
import os
from collections import defaultdict
from termcolor import colored as cr

# -----------------------------------------------


def clear_screen():
    if os.name == 'nt':  # 'nt' refers to Windows
        os.system('cls')
    else:  # 'posix' for Unix-like systems (Linux, macOS)
        os.system('clear')


# -----------------------------------------------


def header():
    clear_screen()
    print(cr('-' * 25, color='cyan'))
    print(cr('Expense Tracker'.center(25), color='cyan'))
    print(cr('-' * 25, color='cyan'))


# -----------------------------------------------


def main_screen():
    header()
    print('1. Add an expense')
    print('2. Show total expenses')
    print('3. Show total expenses grouped by category')
    print('4. List all expenses')
    print('5. List category expenses')
    print('6. Extract all expenses as csv')
    print('0. Exit')


# -----------------------------------------------


def valid_number(prompt, integer=True):
    try:
        if integer:
            valid = int(input(prompt).strip())
        else:
            valid = float(input(prompt).strip())
        return valid
    except:
        print(cr('\nInvalid Number!\n', color='red', attrs=['bold']))
        return valid_number(prompt, integer)


# -----------------------------------------------


def add_expense():
    amount = valid_number('Enter amount: ', integer=False)
    category = input('Enter category: ').strip()

    return {'amount': amount, 'category': category}


# -----------------------------------------------


def show_total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


# -----------------------------------------------


def show_total_expenses_by_category(expenses):
    expenses_by_category = defaultdict(float)

    for expense in expenses:
        expenses_by_category[expense['category']] += expense['amount']

    length = f"{len(expenses_by_category)}"
    for i, (category, amount) in enumerate(expenses_by_category.items(), start=1):
        print(f"{i:0{len(length)}} >> Category: {category} - Amount: {amount}")


# -----------------------------------------------


def list_all_expenses(expenses):
    length = f"{len(expenses)}"
    for i, expense in enumerate(expenses, start=1):
        len(expenses)
        print(f"{i:0{len(length)}} >> Category: {expense['category']} - Amount: {expense['amount']}")


# -----------------------------------------------


def list_category_expenses(expenses):
    category = input('Enter category: ').strip()
    category_expenses = list(filter(lambda expense: expense['category'] == category, expenses))

    if not category_expenses:
        print('No Expanses for this category!')
        return

    list_all_expenses(category_expenses)


# -----------------------------------------------


def extract_as_csv(expenses):
    file_name = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    lines = [f"{i},{expense['category']},{expense['amount']}\n" for i, expense in enumerate(expenses, start=1)]
    with open(file_name, 'w') as f:
        f.write('number,category,amount\n')
        f.writelines(lines)


# -----------------------------------------------


def expense_tracker():
    expenses = []

    main_screen()
    choice = valid_number('\nEnter your choice: ')
    while choice:

        if choice == 1:
            expenses.append(add_expense())
            print('The expense has been added successfully.')

        elif choice == 2:
            print(f'\nTotal Expenses: {show_total_expenses(expenses)}')

        elif choice == 3:
            show_total_expenses_by_category(expenses)

        elif choice == 4:
            list_all_expenses(expenses)

        elif choice == 5:
            list_category_expenses(expenses)

        elif choice == 6:
            extract_as_csv(expenses)
            print('The expense history has been exported successfully.')

        else:
            print(cr('\nInvalid Choice!\n', color='red', attrs=['bold']))
            main_screen()
            choice = valid_number('\nEnter your choice: ')
            continue

        input('\nPress Enter to continue...')
        main_screen()
        choice = valid_number('\nEnter your choice: ')


# -----------------------------------------------


# App Execution
if __name__ == '__main__':
    expense_tracker()
