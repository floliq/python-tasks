class MyDict(dict):
    """
    Класс Cобственного словаря. Родитель: dict
    """

    def get(self, key, default=None):
        """
        Функция получения значения словаря, метод get() наследуется от родителя

        :param key: ключ для поиска в словаре
        :param default: значение которое вернется если запрошенного ключа нет в словаре
        :return: значение по заданному ключу или None если такого ключа нет
        """

        return super().get(key, 0)

 
my_dict = MyDict({'x': 2, 'y': 22})
print(my_dict.get('z'), my_dict.get('y'))
