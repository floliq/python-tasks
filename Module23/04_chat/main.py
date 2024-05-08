def read_chat(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            messages = file.readlines()
            print(''.join(messages))
    except FileNotFoundError:
        print('Чат пуст, начните общение \n')


def write_in_chat(file_name):
    new_message = input('Введите сообщение: ')
    with open (file_name, 'a', encoding='utf-8') as file:
        file.write('{}: {}\n'.format(username, new_message))


username = input('Введите ваше имя: ')
while True:
    print('Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2')
    responce = input("Введите 1 или 2: ")
    if responce == '1':
        read_chat('chat.txt')
    elif responce == '2':
        write_in_chat('chat.txt')
    else:
        print('Неизвестная команда\n')
