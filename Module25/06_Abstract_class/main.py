from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Класс Фигуры. Наследуется от ABC
    """

    @abstractmethod
    def area(self):
        """
        Абстрактный метод расчета площади
        """
        pass


class Circle(Shape):
    """
    Класс круга, наследующийся от класса фигура

    Args:
        radius(int) - передаеться радиус круга
    """

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        """
        Геттер для получения радиуса круга

        :return: __radius
        :rtype: float
        """
        return self.__radius

    def area(self):
        """
        Метод расчета площади круга. Наследует метод у класса фигуры

        :return: 3.14 * self.get_radius() ** 2
        :rtype: float
        """
        super().area()
        return 3.14 * self.get_radius() ** 2


class Rectangle(Shape):
    """
    Класс Прямоугольник, наследующийся от класса фигура

    Args:
        width(float) - передаеться длина прямоугольника
        height(float) - передаеться ширина прямоугольника
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        """
        Геттер для получения длины прямоугольника

        :return: __width
        :rtype: float
        """
        return self.__width

    def get_height(self):
        """
        Геттер для получения ширины прямоугольника

        :return: __height
        :rtype: float
        """
        return self.__height

    def area(self):
        """
        Метод расчета площади прямоугольника. Наследует метод у класса фигуры

        :return: self.get_width() * self.get_height()
        :rtype: float
        """
        super().area()
        return self.get_width() * self.get_height()


class Triangle(Shape):
    """
    Класс треугольник, наследующийся от класса фигура

    Args:
        width(float) - передаеться основание треугольника
        height(float) - передаеться высота треугольника
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        """
        Геттер для получения основания треугольника

        :return: __width
        :rtype: float
        """
        return self.__width

    def get_height(self):
        """
        Геттер для получения высоты треугольника

        :return: __height
        :rtype: float
        """
        return self.__height

    def area(self):
        """
        Метод расчета площади прямоугольника. Наследует метод у класса фигуры

        :return: (self.get_width() * self.get_height()) / 2
        :rtype: float
        """
        super().area()
        return (self.get_width() * self.get_height()) / 2


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
