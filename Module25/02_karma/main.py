import random
import os

WIN_POINTS = 500


class KillError(Exception):
    """
    Класс KillError. Родитель: Exception
    """

    pass


class DrunkError(Exception):
    """
    Класс DrunkError. Родитель: Exception
    """

    pass


class CarCrashError(Exception):
    """
    Класс CarCrashError. Родитель: Exception
    """
    
    pass


class GluttonyError(Exception):
    """
    Класс GluttonyError. Родитель: Exception
    """

    pass


class DepressionError(Exception):
    """
    Класс DepressionError. Родитель: Exception
    """

    pass


class Buddist:
    """
    Класс будиста

    Args:
        karma(int) - количество кармы у будиста, по-умолчанию 0
    """

    def __init__(self, karma = 0):
        self.__karma = karma

    def get_karma(self):
        """
        Геттер для получения количества кармы

        :return: __karma
        :rtype: int
        """
        return self.__karma

    def set_karma(self, karma):
        """
        Сеттер для установления количества кармы

        :param karma: количество кармы
        :type karma: int
        """
        self.__karma += karma


def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)


def one_day():
    if random.randint(1, 10) == 1:
        dice = random.choice([KillError('Убился'), DrunkError('Напился'), CarCrashError('Разбился на машине'),
                               GluttonyError('Объелся'), DepressionError('Впал в депрессию')])
        raise dice
    else:
        return random.randint(1, 7)


file_name = 'karma.log'
delete_file(file_name)
player = Buddist()
day = 0
with open(file_name, 'a', encoding='utf-8') as file:
    while player.get_karma() <  WIN_POINTS:
        try:
            day += 1
            karma = one_day()
            if not karma:
                pass
            else:
                player.set_karma(karma)
                print('День {} Игрок прожил день без грехов, получено кармы {} его карма {}'.format(
                    day,
                    karma,
                    player.get_karma(),
                ))
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            error = str(exc)
            print(f'День {day} совершен грех: {error}')
            file.write(f'День {day} совершен грех: {error}\n')
