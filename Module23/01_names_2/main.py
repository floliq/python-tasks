def get_count_letters(file_name):
    count = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            try:
                line = line.replace('\n', '')
                if len(line) < 3:
                    raise  ValueError
                count += len(line)
            except ValueError:
                print('Ошибка: менее трёх символов в строке {}.'.format(index + 1))
    return count


count_letters = get_count_letters('people.txt')
print('Общее количество символов: {}'.format(count_letters))
