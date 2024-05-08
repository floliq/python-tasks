from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    '''
    Декоторатор где другой декоторая может принимать аргументы
    '''

    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *def_args, **def_kwargs) -> Callable:
    '''
    Декоратор шаблон
    '''

    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор: {} {}'.format(
            def_args,
            def_kwargs
        ))
        return func(*func_args, **func_kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    '''
    Декорируемая функция
    '''

    print("Привет", text, num)


decorated_function("Юзер", 101)
