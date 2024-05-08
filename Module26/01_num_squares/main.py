from collections.abc import Iterable


class Square:
    """
    Класс квадратов чисел

    Args:
        length(int) - передаеться количество числе
    
    Attributes:
        count(int) - счетчик возводимых квадратов
    """

    def __init__(self, length: int) -> None:
        self.__length = length
        self.__count = 0
    
    def get_length(self) -> None:
        """
        Геттер для количества квадратов

        :return: __length
        :rtype: int
        """

        return self.__length

    def get_count(self) -> int:
        """
        Геттер для счетчика возводимого квадрата

        :return: __count
        :rtype: int
        """

        return self.__count
    
    def set_count(self):
        """
        Сеттер для установки счетчика возводимого квадрата, увеличивает значение на 1
        """

        self.__count += 1
    
    def __iter__(self) -> 'Square':
        """
        Возвращает итератор для объекта класса Square.

        :return: Итератор
        :rtype: 'Square'
        """

        self.__count = 0
        return self
    
    def __next__(self) -> int:
        """
        Возвращает следующий элемент в последовательности квадратов чисел.

        :return: self.get_count() ** 2
        :rtype: int
        :raises StopIteration: Если достигнут конец последовательности
        """
        
        if self.get_count() == self.get_length():
            raise StopIteration
        self.set_count()
        return self.get_count() ** 2


def get_squares(length: int) -> Iterable[int]:
    """
    Функция-генератор последовательности квадратов чисел от 1 до указанной длины.

    :param length: Длина последовательности квадратов
    :type length: int
    :return: i ** 2
    :rtype: Iterable[int]
    """

    for i in range(1, length + 1):
        yield i ** 2


n = int(input('Введите число: '))
print('Генератонное выражение')
square_gen = (i ** 2 for i in range(1, n + 1))
for i_num in square_gen:
    print(i_num)
print('Функция-генератор')
for i_num in get_squares(n):
    print(i_num)
print('Класс-итератор')
square_class = Square(n)
for i_num in square_class:
    print(i_num)
