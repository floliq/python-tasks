import time
import functools
from typing import Callable


class LoggerDecorator:
    '''
    Класс декоторатор, который выводит в консоль 
    информацию о времени выполнения функции, аргументы и результат
    
    Attributes:
        func: декорируемая функция
    '''

    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Callable:
        '''
        Метод расчета времени работы функции, аргументов и результата функции
        '''

        start_time = time.time()  
        result = self.func(*args, **kwargs)
        end_time = time.time()  
        execution_time = end_time - start_time
        print('Вызов функции {}\nАргументы: {}, {}\nРезультат: {}\nВремя выполнения: {} секунд'.format(
            self.func.__name__,
            args,
            kwargs,
            result,
            execution_time
        ))


@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    '''
    Функция производящая расчеты

    :param arg1: первый аргумент
    :type arg1: int
    :param arg2: второй аргумент
    :type arg2: int
    :return: result
    :rtype: int
    '''
    
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


result = complex_algorithm(10, 50)
