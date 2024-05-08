def convert_message(message):
    new_message = '' 
    word = '' 
    for sym in message: 
        if sym.isalpha(): 
            word = ''.join([word, sym]) 
        else: 
            new_message = ''.join([new_message, word[::-1], sym]) 
            word = '' 
    return new_message


message = input('Сообщение: ')
new_message = convert_message(message)
print('Новое сообщение: {}'.format(new_message))
