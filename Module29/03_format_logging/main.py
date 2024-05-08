from typing import Callable, Any 
from datetime import datetime
import time
import functools

def timer(cls, func: Callable, format: str) -> Callable:
    '''
    Декоратор рассчитывающий время работы метода
    '''

    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Any:
        date = format
        for symbol in date:
            if symbol.isalpha():
                date = date.replace(symbol, '%' + symbol)
        print("Запускается '{}.{}'. Дата и время запуска: {}".format(
            cls.__name__,
            func.__name__,
            datetime.now().strftime(date)
        ))
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        work_time = end - start
        print("Завершение '{}.{}', время работы = {}s ".format(
            cls.__name__,
            func.__name__,
            round(work_time, 3)
        ))
        return result

    return wrapper


def log_methods(format: str) -> Callable:
    '''
    Декоторатор, который логирует все методы декорируемого класса
    :param format(str): формат даты
    '''

    def wrapper(cls) -> Any:
        for method in dir(cls):
            if not method.startswith('__'):
                cur_method = getattr(cls, method)
                dec_method = timer(cls, cur_method, format)
                setattr(cls, method, dec_method)
        return cls

    return wrapper
    

@log_methods("b d Y - H:M:S")
class A:
    '''
    Базовый класс А
    '''
    def test_sum_1(self) -> int:
        '''
        Метод расчета квадратов

        :return: result
        :rtype: int
        '''

        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    '''
    Класс Б, производный от класса A
    '''

    def test_sum_1(self) -> None:
        '''
        Метод расчета квадратов, наследуется из метода класса A
        '''

        super().test_sum_1()
        print('Тут метод test_sum_1 у наследника')

    def test_sum_2(self) -> int:
        '''
        Второй метод расчета квадратов

        :return: result
        :rtype: int
        '''

        print('Тут метод test_sum_2')
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
