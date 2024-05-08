import random


class Monster:
    """
    Базовый класс Монстра

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        max_hp(int) - максимальное здоровье (150)
        start_power(int) - начальная сила удара (10)
        hp(int) - здоровье, равна максимальному здоровью
        power(int) -  мощность атаки (урон на один ход), равна начальной силе
        is_alive(bool) - проверка, жив ли монстр
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

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого.

        :param target: цель атаки
        """
        pass

    def is_alive(self):
        """
        Функция проверки жив ли персонаж или нет

        :return: __is_alive
        :rtype: bool
        """
        return self.__is_alive

    def take_damage(self, damage):
        """
        Функция получения урона от врага, если хп заканчивается, монстр умерает

        :param damage: урон
        :type damage: float
        """
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода

        :param friends: союзники
        :param enemies: враги
        """
        pass

    def __str__(self):
        """
        Функция получения состояния героя
        """
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class MonsterBerserk(Monster):
    """
    Класс берсерка. Родитель Монстр

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        maddness(float) - ярость берсерка 
    """

    def __init__(self, name):
        super().__init__(name)
        self.madness = 1

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого. После атаки увлечивается ярость

        :param target: цель атаки
        """
        target.take_damage(self.get_power() * self.madness)
        self.madness += 0.1

    def take_damage(self, power):
        """
        Функция получения урона от врага

        :param damage: урон
        :type damage: float
        """
        self.set_hp(self.get_hp() - power * (self.madness / 2))
        if self.get_hp() < 50:
            self.madness *= 2
        super().take_damage(power)

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода

        :param friends: союзники
        :param enemies: враги
        """
        print(self.name, end=' ')
        self.madness = min(self.madness, 4)
        if not enemies:
            return
        if self.madness < 3:
            print("Атакую того, кто стоит ближе -", enemies[0].name)
            self.attack(enemies[0])
        else:
            target = random.choice(enemies)
            print("BERSERK MODE!!! Уровень безумия - " + str(self.madness) + " Случайно атакую -", target.name)
            print()
            self.attack(target)
        print('\n')


class MonsterHunter(Monster):
    """
    Класс Охотника. Родитель Монстр

    Args:
        name(str) - передаеться имя персонажа
    
    Attributes:
        potion(int) - колво зелье 
    """

    def __init__(self, name):
        super().__init__(name)
        self.potions = 10

    def attack(self, target):
        """
        Функция атаки одного персонажа на другого. После атаки увлечивается ярость

        :param target: цель атаки
        """
        target.take_damage(self.get_power() + (10 - self.potions))

    def take_damage(self, power):
        """
        Функция получения урона от врага

        :param damage: урон
        :type damage: float
        """
        self.set_hp(self.get_hp() - power)
        if random.randint(1, 10) == 1:
            self.potions -= 1
        super().take_damage(power)

    def give_a_potion(self, target):
        """
        Функция передачи зелья

        :param target: цель
        """
        self.potions -= 1
        target.set_hp(target.get_hp() + self.get_power())

    def make_a_move(self, friends, enemies):
        """
        Функция выполнения хода

        :param friends: союзники
        :param enemies: враги
        """
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()

        if min_health < 60 and self.potions > 0:
            print("Исцеляю", target_of_potion.name)
            self.give_a_potion(target_of_potion)
        else:
            if not enemies:
                return
            print("Атакую ближнего -", enemies[0].name)
            self.attack(enemies[0])
        print('\n')
