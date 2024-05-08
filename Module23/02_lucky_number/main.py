import random


def print_file(file_name):
    print('Содержимое файла {}'.format(file_name))
    with open(file_name) as file:
        for line in file:
            print(line, end='')
    print()


def total_value(file_name):
    total = 0
    try:
        with open(file_name, 'w') as file:
            while total < 777:
                number = int(input('Введите число: '))
                total += number
                file.write('{}\n'.format(number))
                if random.randint(1,13) == 1:
                    raise ValueError
    except ValueError:
        print('Вас постигла неудача!')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    finally:
        print_file(file_name)


total_value('out_file.txt')
