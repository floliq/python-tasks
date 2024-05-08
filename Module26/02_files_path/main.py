from typing import Iterable
import os


def gen_files_path(dir:str = 'c:\\') -> Iterable[str]:
    """
    функция получения путей к файлам от папки

    :param dir: директория
    :type dir: str
    :yield: file_paths
    :rtype: str
    """

    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


path = os.path.abspath(input('Введите директорию: '))
file_paths = gen_files_path(path)
for file in file_paths:
    print(file)
