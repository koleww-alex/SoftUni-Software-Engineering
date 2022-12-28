from project.meals.meal import Meal


# from exam_preparation.august_retake_exam.project.meals.meal import Meal

class MainDish(Meal):

    def __init__(self, name: str, price: float, quantity=50):
        super().__init__(name, price, quantity)

    def details(self):
        return f'Main Dish {self.name}: {self.price:.2f}lv/piece'
