from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart('Test', 1000)

    def test_correct_initialization(self):
        self.assertEqual('Test', self.shopping_cart.shop_name)
        self.assertEqual(1000, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_raise_error_if_name_is_incorrect(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'asd123'

        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

    def test_correct_name(self):
        self.shopping_cart.shop_name = 'Alex'
        self.assertEqual('Alex', self.shopping_cart.shop_name)

    def test_raise_error_adding_product_with_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('apple', 120)

        self.assertEqual('Product apple cost too much!', str(ve.exception))

    def test_correct_adding_product(self):
        test = self.shopping_cart.add_to_cart('apple', 50)
        self.assertEqual({'apple': 50}, self.shopping_cart.products)
        self.assertEqual('apple product was successfully added to the cart!', test)

    def test_raise_error_if_removing_unknown_product(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('apple')

        self.assertEqual('No product with name apple in the cart!', str(ve.exception))

    def test_correct_removing_product(self):
        self.shopping_cart.products['paprika'] = 10
        self.shopping_cart.products['cucumber'] = 2
        test = self.shopping_cart.remove_from_cart('paprika')
        self.assertEqual({'cucumber': 2}, self.shopping_cart.products)
        self.assertEqual('Product paprika was successfully removed from the cart!', test)

    def test_correct_merge_on_two_instances(self):
        self.bigger_shopping_cart = ShoppingCart('Test', 10_000)
        self.bigger_shopping_cart.products['merge'] = 1
        self.test = self.shopping_cart + self.bigger_shopping_cart

        self.assertEqual(11_000, self.test.budget)
        self.assertEqual('TestTest', self.test.shop_name)
        self.assertEqual({'merge': 1}, self.test.products)

    def test_raise_error_if_bill_is_more_than_budget(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.products['expensive_product'] = 2000
            self.shopping_cart.buy_products()

        self.assertEqual('Not enough money to buy the products! Over budget with 1000.00lv!', str(ve.exception))

    def test_successful_purchase(self):
        self.shopping_cart.products['cucumber'] = 200
        self.assertEqual('Products were successfully bought! Total cost: 200.00lv.', self.shopping_cart.buy_products())


if __name__ == '__main__':
    main()
