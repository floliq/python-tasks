import random


class Hero:
    """
    Базовый класс героя

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        max_hp(int) - максимальное здоровье (150)
        start_power(int) - начальная сила удара (10)
        hp(int) - здоровье, равна максимальному здоровью
        power(int) -  мощность атаки (урон на один ход), равна начальной силе
        is_alive(bool) - проверка, жив ли герой
    """

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        """
        Геттер для получения здоровьтя

        :return: __hp
        :rtype: int
        """
        return self.__hp

    def set_hp(self, new_value):
        """
        Сеттер для установки здоровья

        :param new_value: новое значение здоровья
        :type new_value: int
        """
        self.__hp = max(new_value, 0)

    def get_power(self):
        """
        Геттер для силы удара

        :return: __power
        :rtype: int
        """
        return self.__power

    def set_power(self, new_power):
        """
        Сеттер для установки силы удара

        :param new_power: новое значение силы удара
        :type new_power: int
        """
        self.__power = new_power

    def is_alive(self):
        """
        Функция проверки жив ли персонаж или нет

        :return: __is_alive
        :rtype: bool
        """
        return self.__is_alive

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого.

        :param target: цель атаки
        :raise NotImplementedError: если не переопределен метод attack в потомках
        """
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        """
        Функция получения урона от врага, если хп заканчивается, герой умерает

        :param damage: урон
        :type damage: int
        """
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода, с каждым ходом игрок становится сильнее

        :param friends: союзники
        :param enemies: враги
        """
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        """
        Функция получения состояния героя

        :raise NotImplementedError: если не переопределен метод __str__ в потомках
        """
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    """
    Класс Целителя. Родитель Герой

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        magic_power(float) - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3) 
    """

    def __init__(self, name):
        super().__init__(name)
        self.__magic_power = self.get_power() * 3

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого. Может атаковать врага, но атакует только в половину силы self.__power

        :param target: цель атаки
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        """
        Функция получения урона от врага, если хп заканчивается, герой умерает. Т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)

        :param damage: урон
        :type damage: int
        """
        self.set_hp(self.get_hp() - (1.2 * damage))
        super().take_damage(damage)

    def heal(self, target):
        """
        Функция исцеления союзника. Увеличивает здоровье цели на величину равную своей магической силе

        :param target: цель исцеления
        """
        target.set_hp(target.get_hp() + self.get_magic_power())

    def get_magic_power(self):
        """
        Геттер для получения магической силы

        :return: __magic_power
        :rtype: int
        """
        return self.__magic_power

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода, исцеляет союзников, либо атакует врага

        :param friends: союзники
        :param enemies: враги
        """
        if  len(enemies) > 0:
            for friend in friends:
                if friend.get_hp() < 150:
                    self.heal(friend)
                else:
                    target = random.choice(enemies)
                    self.attack(target)
            super().make_a_move(friends, enemies)

    def __str__(self):
        """
        Функция получения состояния героя
        """
        return f'Name: {self.name} | HP: {self.get_hp()}'

class Tank(Hero):
    """
    Класс Танка. Родитель Герой

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        defence(int) - показатель защиты, изначально равен 1, может увеличиваться и уменьшаться
        shield_up(bool) - поднят ли щит, танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    """

    def __init__(self, name):
        super().__init__(name)
        self.__defence = 1
        self.__shield_up = False

    def get_defence(self):
        """
        Геттер для получения показателя защиты

        :return: __defence
        :rtype: int
        """
        return self.__defence

    def set_defence(self, value):
        self.__defence = value
        """
        Сеттер для установки показателя защиты

        :param value: новое значение показателя защиты
        :type value: int
        """

    def get_shield_up(self):
        """
        Геттер для получения поднятого щита

        :return: __shield_up
        :rtype: bool
        """
        return self.__shield_up

    def set_shield_up(self, value):
        """
        Сеттер для установки поднятого щита

        :param value: новое значение поднятого щита
        :type value: bool
        """
        self.__shield_up = value

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого. Атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)

        :param target: цель атаки
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        """
        Функция получения урона от врага, если хп заканчивается, герой умерает. Весь входящий урон делится на показатель защиты (damage/self.defense)
        и только потом отнимается от здоровья

        :param damage: урон
        :type damage: int
        """
        self.set_hp(self.get_hp() - (damage / self.get_defence()))
        super().take_damage(damage)

    def raise_shield(self):
        """
        Функция Поднятия щита.
        Если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
        """
        if not self.get_shield_up():
            self.set_shield_up(True)
            self.set_defence(self.get_defence() * 2)
            self.set_power(self.get_power() / 2)
            print('{} поднимает щит!'.format(self.name))

    def lower_shield(self):
        """
        Функция опускания щита.
        Если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
        """
        if self.get_shield_up():
            self.set_shield_up(False)
            self.set_defence(self.get_defence() / 2)
            self.set_power(self.get_power() * 2)
            print('{} опускает щит!'.format(self.name))

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода, атакует врага и подымает щит

        :param friends: союзники
        :param enemies: враги
        """
        if  len(enemies) > 0:
            target = random.choice(enemies)
            self.attack(target)
            if not self.get_shield_up():
                self.raise_shield()
            super().make_a_move(friends, enemies)

    def __str__(self):
        """
        Функция получения состояния героя
        """
        return f'Name: {self.name} | HP: {self.get_hp()}'


class Attacker(Hero):
    """
    Класс Убийца. Родитель Герой

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        power_multiply(float) - оэффициент усиления урона (входящего и исходящего)
    """
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.__power_multiply = 1

    def get_power_multiply(self):
        """
        Геттер для получения коэф услиления урока

        :return: __power_multiply
        :rtype: float
        """
        return self.__power_multiply

    def set_power_multiply(self, value):
        """
        Сеттер для установки коэф услиления урока

        :param value: новое значение коэф услиления урока
        :type value: float
        """
        self.__power_multiply = value

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого. Наносит урон равный показателю силы (self.__power) 
        умноженному на коэффициент усиления урона (self.power_multiply) после нанесения урона - вызывается метод ослабления power_down.
        
        :param target: цель атаки
        """
        target.take_damage(self.get_power() * self.get_power_multiply())

    def take_damage(self, damage):
        """
        Функция получения урона от врага, если хп заканчивается, герой умерает. получает урон равный входящему урона умноженному на половину
        коэффициента усиления урона - damage * (self.power_multiply / 2)

        :param damage: урон
        :type damage: int
        """
        self.set_hp(self.get_hp() - (damage * (self.get_power_multiply() / 2)))
        super().take_damage(damage)

    def power_up(self):
        """
        Функция усиления множителя урока.Увеличивает коэффициента усиления урона в 2 раза
        """
        self.set_power_multiply(self.get_power_multiply() * 2)

    def power_down(self):
        """
        Функция ослабления множителя урока. Уменьшает коэффициента усиления урона в 2 раза
        """
        self.set_power_multiply(self.get_power_multiply() / 2)

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода, усиляет коэф множителя урона или атакует врага

        :param friends: союзники
        :param enemies: враги
        """
        if len(enemies) > 0:
            target = random.choice(enemies)
            if self.get_power_multiply() < 5:
                self.power_up()
            else:
                self.attack(target)
            super().make_a_move(friends, enemies)

    def __str__(self):
        """
        Функция получения состояния героя
        """
        return f'Name: {self.name} | HP: {self.get_hp()}'
