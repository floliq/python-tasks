from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    '''
    Декоратор просящий ввести как дела и получает ответ
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs) 
    return wrapper


@how_are_you
def test() -> None:
    '''
    Тестовая функция
    '''

    print('<Тут что-то происходит...>')


@how_are_you
def test2() -> None:
    '''
    Тестовая функция 2
    '''

    print('функция 2')
    print('<Тут что-то происходит...>')


test()
test2()
