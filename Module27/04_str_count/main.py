from typing import Callable, Any
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, который подсчитывает количество вызовов декорируемой функции.

    :param func: декорируемая функция
    :return: декорированная функция
    """
      
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('Функция {} была вызвана: {} раз'.format(func.__name__, wrapper.count))
        return res
    
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('test')


test()
test()
test()
