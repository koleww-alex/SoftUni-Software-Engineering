from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    WEIGHT_INCREASED = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    def feed(self, food):
        edible_food = [Meat]
        if food.__class__ not in edible_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += (food.quantity * Owl.WEIGHT_INCREASED)
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASED = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Cluck'

    def feed(self, food):
        edible_food = [Vegetable, Fruit, Meat, Seed]
        if food.__class__ not in edible_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += (food.quantity * Hen.WEIGHT_INCREASED)
        self.food_eaten += food.quantity
