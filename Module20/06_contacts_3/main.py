def add_contact():
    full_name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if full_name not in contacts:
        phone = int(input('Введите номер телефона:'))
        contacts[full_name] = phone
    else:
        print('Такой человек уже есть в контактах.')
    print('Текущий словарь контактов: {}'.format(contacts))


def find_contact():
    surname = input('Введите фамилию для поиска: ')
    for key, phone in contacts.items():
        if surname.lower() == key[-1].lower():
            print('{name} {surname} {phone}'.format(
                name=key[0],
                surname=key[1],
                phone=phone
            ))


contacts = dict()
while True:
    print('Введите номер действия:\n 1. Добавить контакт\n 2. Найти человека ')
    choice =  int(input())
    if choice == 1:
        add_contact()
    elif choice ==2:
        find_contact()
    else:
        print('Неправильное действие!')