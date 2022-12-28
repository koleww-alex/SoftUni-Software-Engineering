from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        return None

    @abstractmethod
    def calculate_area(self):
        return None


class Circle(Shape):

    def __init__(self, radius: int):
        super().__init__()

        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def calculate_area(self):
        return pi * (self.__radius ** 2)


class Rectangle(Shape):

    def __init__(self, height: int, width: int):
        super().__init__()

        self.__height = height
        self.__width = width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)

    def calculate_area(self):
        return self.__height * self.__width


circle = Circle(5)
rectangle = Rectangle(10, 20)

print(circle.calculate_area())
print(circle.calculate_perimeter())

print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
