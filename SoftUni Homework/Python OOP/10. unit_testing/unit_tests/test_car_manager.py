from unittest import TestCase, main

# from Unit_Testing.code_to_test.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Subaru', 'WRX', 15, 65)

    def test_correct_initializing(self):
        self.assertEqual('Subaru', self.car.make)
        self.assertEqual('WRX', self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)

    def test_raise_error_if_make_is_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_raise_error_if_model_is_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_raise_error_if_fuel_consumption_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_raise_error_if_fuel_capacity_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_raise_error_if_fuel_amount_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_raise_error_if_invalid_fuel_amount_is_given_when_refueling(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_correct_amount_fueling(self):
        self.car.fuel_amount = 0
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_correct_fueling(self):
        self.car.refuel(100)
        self.assertEqual(65, self.car.fuel_amount)

    def test_raise_error_when_tries_to_drive_without_enough_fuel(self):
        self.car.fuel_amount = 20
        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_correct_fuel_amount_used_when_driving(self):
        self.car.fuel_amount = 65
        self.car.drive(50)
        self.assertEqual(57.5, self.car.fuel_amount)


if __name__ == '__main__':
    main()
