from collections.abc import Iterable
import os


def get_files_lines(dir:str = 'c:\\') -> Iterable[int]:
    """
    функция-генератор получения количество строк в файле
    
    :param dir: директория
    :type dir: str
    :yield: count
    :rtype: int
    """
    
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.py'):
                file_name = os.path.join(root, file)
                count = 0
                with open(file_name, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            count += 1
                yield count


path = os.path.abspath(input('Введите директорию: '))
lines_count = get_files_lines(path)
for count in lines_count:
    print(count)
