from collections import OrderedDict
from typing import Union


class LRUCache:
    """
    Класс хранилища

    Args:
        capacity(int) - объем хранилища
    
    Attributes:
        cache_dict(OrderedDict) - словарь с ключами и значениями хранилища
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache_dict = OrderedDict()

    @property
    def capacity(self) -> int:
        """
        Геттер для получения размера хранилища

        :return: __capacity
        :rtype: int
        """

        return self._capacity

    @property
    def cache_dict(self) -> OrderedDict:
        """
        Геттер для получения словаря в хранилище

        :return: __cache_dict
        :rtype: OrderedDict
        """

        return self._cache_dict

    @property
    def cache(self) -> Union[tuple, str]:
        """
        Геттер для получения значения из словаря в хранилище

        :return: значение из словаря в хранилище
        :rtype: Union[tuple, str]
        """

        return next(iter(self.cache_dict.items())) if self.cache_dict else 'Пусто'

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        """
        Сеттер для значения из словаря в хранилище

        :param new_elem: кортеж из ключа и значения
        :type new_elem: tuple
        """

        if len(self.cache_dict) == self.capacity:
            self.cache_dict.popitem(last=False)
        self.cache_dict[new_elem[0]] = new_elem[1]

    def print_cache(self) -> None:
        """
        Функция вывода хранилища
        """

        print('LRU Cache:')
        for key, value in self.cache_dict.items():
            print('{} : {}'.format(key, value))

    def get(self, value: str) -> Union[str, tuple]:
        """
        Функция получения значения из хранилища

        :param value: ключ в хранилище
        :type value: str
        :return: значение в хранилище
        :rtype: Union[str, tuple]
        """

        if value in self.cache_dict:
            self.cache_dict.move_to_end(value)
            return self.cache_dict[value]
        return 'Такого ключа нет в кэше'


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
