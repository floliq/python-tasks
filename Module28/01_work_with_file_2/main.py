import os
from typing import TextIO


class File:
    """
    Класс Файл

    Args:
        file_name(str) - название файла
        mode(str) - право доступа к файлу
    """

    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    @property
    def file_name(self) -> str:
        """
        Геттер для получения названия файла

        :return: __file_name
        :rtype: str
        """

        return self._file_name

    def __enter__(self) -> TextIO:
        '''
        Функция срабатывающая до запуска context manager
        
        :return: self
        :rtype: TextIO
        '''

        if not os.path.exists(self.file_name):
            print('Файл не существует')
            open(self.file_name, 'w').close()
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        '''
        Функция выполняющая после выполнения context manager

        :return: True
        :rtype: bool
        '''

        self.file.close() 
        if exc_type is OSError:
            return True


with File('test.txt') as file:
    file.write('hello world')
