def code_string(user_text):
    result = ''
    count = 1
    for i in range(len(user_text) - 1):
        if user_text[i] == user_text[i + 1]:
            count += 1
        else:
            result += user_text[i] + str(count)
            count = 1
    result += user_text[-1] + str(count)
    return result


text = input('Введите строку: ')
code_text = code_string(text)
print('Закодированная строка: {}'.format(code_text))
