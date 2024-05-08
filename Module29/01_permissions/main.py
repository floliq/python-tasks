from typing import Callable, Any
import functools


user_permissions = ['admin']

def check_permission(permision: str) -> Callable:
    '''
    Декоратор проверяющий доступ к функции
    '''
    # TODO используйте символ "двойные кавычки" для докстрингов: """ ... """
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                if permision in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError as err:
                print('У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(
                    func.__name__
                ))

        return wrapper

    return decorator


@check_permission('admin')
def delete_site() -> None:
    '''
    Функция удаления сайта
    '''

    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    '''
    Функция добавление комментария
    '''

    print('Добавляем комментарий')


delete_site()
add_comment()
