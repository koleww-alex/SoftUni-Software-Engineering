from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASED = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Squeak'

    def feed(self, food):
        edible_food = [Vegetable, Fruit]
        if food.__class__ not in edible_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += (food.quantity * Mouse.WEIGHT_INCREASED)
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASED = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Woof!'

    def feed(self, food):
        edible_food = [Meat]
        if food.__class__ not in edible_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += (food.quantity * Dog.WEIGHT_INCREASED)
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASED = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Meow'

    def feed(self, food):
        edible_food = [Vegetable, Meat]
        if food.__class__ not in edible_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += (food.quantity * Cat.WEIGHT_INCREASED)
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASED = 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    def feed(self, food):
        edible_food = [Meat]
        if food.__class__ not in edible_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += (food.quantity * Tiger.WEIGHT_INCREASED)
        self.food_eaten += food.quantity
