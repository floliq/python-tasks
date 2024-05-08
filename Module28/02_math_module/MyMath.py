import math


class MyMath:
    '''
    Класс MyMath
    '''

    @classmethod
    def circle_len(cls, radius: float) -> float:
        '''
        Классовый метод получения длины круга

        :return: длина круга
        :rtype: float
        '''

        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        '''
        Классовый метод получения площади круга

        :return: площадь круга
        :rtype: float
        '''

        return math.pi * radius ** 2

    @classmethod
    def volume_cube(cls, width: float) -> float:
        '''
        Классовый метод получения объема круга

        :return: объем круга
        :rtype: float
        '''

        return width ** 3

    @classmethod
    def volume_sphere(cls, radius: float) -> float:
        '''
        Классовый метод получения площади поверхности сферы

        :return: площадь поверхности сферы
        :rtype: float
        '''

        return 4 / 3 * math.pi * radius ** 3
