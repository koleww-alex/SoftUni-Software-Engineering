from project.client import Client
from project.meals.meal import Meal


# from exam_preparation.august_retake_exam.project.client import Client
# from exam_preparation.august_retake_exam.project.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __get_client_by_phone_number(self, phone_number):
        return [c for c in self.clients_list if c.phone_number == phone_number][0]

    def __is_client_register_check(self, phone_number: str):
        if phone_number in [c.phone_number for c in self.clients_list]:
            return True

    def __get_meal_by_name(self, name: str):
        return [d for d in self.menu if d.name == name][0]

    def register_client(self, phone_number: str):
        if self.__is_client_register_check(phone_number):
            raise Exception('The client has already been registered!')

        client = Client(phone_number)
        self.clients_list.append(client)
        return f'Client {phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        dishes_on_menu = ['Starter', 'MainDish', 'Dessert']
        for meal in meals:
            if meal.__class__.__name__ in dishes_on_menu:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        output = [m.details() for m in self.menu]

        return '\n'.join(output)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantity):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        if not self.__is_client_register_check(client_phone_number):
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for name, quantity in meal_names_and_quantity.items():
            if name not in [d.name for d in self.menu]:
                raise Exception(f'{name} is not on the menu!')

            current_meal = self.__get_meal_by_name(name)
            if quantity > current_meal.quantity:
                raise Exception(f'Not enough quantity of {current_meal.__class__.__name__}: {name}!')

        client = self.__get_client_by_phone_number(client_phone_number)
        for name, quantity in meal_names_and_quantity.items():
            current_meal = self.__get_meal_by_name(name)
            current_meal.quantity -= quantity
            client.shopping_cart.append(current_meal)
            client.bill += (current_meal.price * quantity)
            client.products[name] = quantity

        return f'Client {client_phone_number} successfully ordered' \
               f' {", ".join(dish.name for dish in client.shopping_cart)} for {client.bill:.2f}lv.'

    def cancel_order(self, client_phone_number: str):
        client = self.__get_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        for name, quantity in client.products.items():
            for meal in self.menu:
                if name == meal.name:
                    meal.quantity += quantity

        client.bill = 0.0
        client.shopping_cart = []
        client.products = {}
        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number):
        client = self.__get_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0.0
        self.RECEIPT_ID += 1
        return f'Receipt #{self.RECEIPT_ID} with total amount of {paid_money:.2f}' \
               f' was successfully paid for {client_phone_number}.'

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'
