def check_file(name):
    prefixes = tuple('@№$%^&*()')
    formats = ('.txt', '.docx')
    if name.startswith(prefixes):
        print('Ошибка: название начинается на один из специальных символов')
    elif not name.endswith(formats):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('Файл назван верно.')
    

name_file = input('Название файла: ')
check_file(name_file)
