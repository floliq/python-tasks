def check_cap_and_dig(user_password):
    capitalize = False
    digit_count = 0
    for letter in user_password:
        if letter.isupper():
            capitalize = True
        if letter.isdigit():
            digit_count += 1
    return capitalize, digit_count


def check_pass(user_password):
    cap, digit = check_cap_and_dig(user_password)
    return len(user_password) >= 8 and cap and digit >= 3

    
while True:
    password = input('Введите пароль: ').strip()
    if not check_pass(password):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
