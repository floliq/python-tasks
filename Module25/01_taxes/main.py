class Property:
    """
    Базовый класс имущества для уплаты налогов

    Args:
        worth(int) - передаеться стоимость имущества
    """

    def __init__(self, worth):
        self.__worth = self.set_worth(worth)

    def get_worth(self):
        """
        Геттер для получения стоимости имущества

        :return: __worth
        :rtype: int
        """
        return self.__worth

    def set_worth(self, worth):
        """
        Сеттер для установления стоимости имущества

        :param worth: стоимость ищущества
        :type worth: int
        """
        return worth

    def check_tax(self):
        """
        Функция расчета суммы налога
        """
        pass


class Apartment(Property):
    """
    Класс Квартира. Родитель: Имущество

    Args:
        worth(int) - передаеться стоимость имущества
    """

    def __init__(self, worth):
        super().__init__(worth)

    def check_tax(self):
        """
        Функция расчета суммы налога 1/1000
        """
        return round(self.get_worth() - (self.get_worth() - self.get_worth() / 1000), 2)


class Car(Property):
    """
    Класс Машина. Родитель: Имущество

    Args:
        worth(int) - передаеться стоимость имущества
    """

    def __init__(self, worth):
        super().__init__(worth)

    def check_tax(self):
        """
        Функция расчета суммы налога 1/200
        """
        return round(self.get_worth() - (self.get_worth() - self.get_worth() / 200), 2)


class CountryHouse(Property):
    """
    Класс Дача. Родитель: Имущество

    Args:
        worth(int) - передаеться стоимость имущества
    """

    def __init__(self, worth):
        super().__init__(worth)

    def check_tax(self):
        """
        Функция расчета суммы налога 1/500
        """
        return round(self.get_worth() - (self.get_worth() - self.get_worth() / 500), 2)


money = int(input('Введите вашу сумму денег: '))
flat_price = int(input('Введите стоимость вашей квартиры: '))
flat = Apartment(flat_price)
print('Ваша сумма налога за квартиру {}'.format(flat.check_tax()))
car_price = int(input('Введите стоимость вашего автомобиля: '))
car = Car(car_price)
print('Ваш налог с автомобиля {}'.format(car.check_tax()))
house_price = int(input('Введите стоимость вашей дачи: '))
house = CountryHouse(house_price)
print('Ваш налог с дачи {}'.format(house.check_tax()))
total_tax = flat.check_tax() + car.check_tax() + house.check_tax()
if money < total_tax:
    need_money = total_tax - money
    print('Вам не хватает денег на уплату налогов {}$'.format(need_money))
else:
    saved_money = money - total_tax
    print('Вам хватило денег на уплату налогов, у вас осталось {}$'.format(saved_money))
