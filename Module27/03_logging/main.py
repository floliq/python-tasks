from datetime import datetime
from typing import Callable, Any
import functools


def logging(func: Callable) -> Callable:
    """
    Декоратор, который логирует вызовы декорируемой функции.

    :param func: декорируемая функция
    :return: декорированная функция
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            print('Название функции {}'.format(func.__name__))
            print('Документация:\n{}'.format(func.__doc__))
            func(*args, **kwargs)
        except Exception as e:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            message = f'{dt_string} имя функции: {func.__name__}, ошибка {e}'
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write('{}\n'.format(message))
            print(message)

    return wrapper


@logging
def name_error():
    '''Функция ошибки присваивания'''

    x = y


@logging
def div_by_zero():
    '''Функция деления на ноль'''

    x = 2
    y = x / 0


@logging
def good():
    '''Функция присваивания переменной'''

    name = 'Ivan'


name_error()
div_by_zero()
good()
