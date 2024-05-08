from typing import Callable, Any 
import functools

app = dict() 


def callback(route: str) -> Callable:
    '''
    Декоратор вызывающий функцию обратного вызова

    :param route(str): путь
    :return: функция обратного вызова
    '''

    def get_answer(func: Callable) -> Callable:

        app[route] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper
    
    return get_answer


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')