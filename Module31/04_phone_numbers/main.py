import re


def check_numbers() -> None:
    """
    Функция получения валидных телефонов
    """
    
    # мог не создавать список, а просто i + 1
    numbers_text = ['первый', 'второй', 'третий', 'четвертый', 'пятый']
    for i in range(len(numbers)):
        if re.match('[8-9]\d{9}', numbers[i]):
            print('{} номер: всё в порядке'.format(numbers_text[i]))
        else:
            print('{} номер: не подходит'.format(numbers_text[i]))


numbers = ['9999999999', '999999-999', '99999x9999']
check_numbers()
