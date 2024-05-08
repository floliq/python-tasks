import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    Декоратор, который кэширует результаты вызова функции
    и позволяет избежать повторных вычислений для одних и тех же аргументов.

    :param func: декорируемая функция
    :return: декорированная функция
    """

    results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in results:
            return results[args]
        results[args] = func(*args, **kwargs)
        return results[args]

    return wrapper


@cache
def fibonacci(number):
    """
    Функция вычисления чисел Фибоначчи.

    :param number: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """

    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
