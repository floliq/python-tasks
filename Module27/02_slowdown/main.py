import time
import functools
from typing import Callable, Any


def loading(seconds: int) -> Callable[[Callable], Callable]:
    """
    Декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

    :param seconds: количество секунд, которое нужно ждать
    :return: декорированная функция
    """

    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args, **kwargs) -> Any:
            print('загрузка...')
            time.sleep(seconds)
            func(*args, **kwargs)

        return inner
    
    return wrapper


@loading(3)
def complete_loading():
    print('загрузка завершена')


complete_loading()
