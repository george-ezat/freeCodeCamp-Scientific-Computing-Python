def verify_card_number(card_number):
    digits = list(map(int, list(card_number)))
    reversed_digits = digits[::-1]

    odd_digits_sum = sum(reversed_digits[::2])
    even_digits = [x * 2 for x in reversed_digits[1::2]]
    even_digits = [(x // 10) + (x % 10) if x > 9 else x for x in even_digits]
    even_digits_sum = sum(even_digits)

    return (even_digits_sum + odd_digits_sum) % 10 == 0


def main():
    card_number = input('Enter your card number: ').strip()
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


main()
