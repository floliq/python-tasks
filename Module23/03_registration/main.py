import os


def delete_files(files):
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def validate_data(item):
    if len(item) < 3:
        raise IndexError('Мало данных!')
    name, email, age = item
    if not name.isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    elif not age.isdigit() or int(age) < 10 or int(age) > 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    elif '@' not in email or '.' not in email:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')


def check_valid(file_name, good_file, bad_file):
    with open(file_name, encoding='utf-8') as file:
        user_list = [line.replace('\n', '').split(' ') for line in file]
    with open(good_file, 'a', encoding='utf-8') as file_good, \
        open(bad_file, 'a', encoding= 'utf-8') as file_bad:
        for item in user_list:
            try:
                validate_data(item)
                file_good.write('{} {} {}\n'.format(*item))
            except (IndexError, NameError, SyntaxError, ValueError) as errors:
                result = ' '.join(item)
                error = str(errors)
                file_bad.write('{} \t {}\n'.format(result, error))


files = ['registrations_good.log', 'registrations_bad.log']         
delete_files(files)
check_valid('registrations.txt', 'registrations_good.log', 'registrations_bad.log')
