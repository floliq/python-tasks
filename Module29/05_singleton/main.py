import functools


def singleton(cls):
    '''
    Декоратор класса, превращает в singleton
    '''

    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.isinstance:
            wrapper_singleton.isinstance = cls(*args, **kwargs)
        return wrapper_singleton.isinstance

    wrapper_singleton.isinstance = None
    return wrapper_singleton


@singleton
class Example:
    '''
    Класс примера
    '''

    pass


my_obj = Example()
my_another_obj = Example()
print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)
