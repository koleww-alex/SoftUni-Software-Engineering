from unittest import TestCase, main

# from Unit_Testing.code_to_test.vehicle import Vehicle


from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(65, 335)

    def test_class_attribute(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_correct_initializing(self):
        self.assertEqual(self.vehicle.fuel, 65)
        self.assertEqual(self.vehicle.horse_power, 335)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_raise_error_if_fuel_is_less_than_distance(self):
        self.vehicle.fuel = 5
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_correct_fuel_used_when_driving(self):
        self.vehicle.fuel = 50
        self.vehicle.drive(20)
        self.assertEqual(25, self.vehicle.fuel)

    def test_raise_error_if_refueled_more_than_possible(self):
        self.vehicle.fuel = 65
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(15)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_correct_refueling(self):
        self.vehicle.fuel = 60
        self.vehicle.refuel(5)
        self.assertEqual(65, self.vehicle.fuel)

    def test_correct_represent(self):
        self.assertEqual('The vehicle has 335 horse power with 65 '
                         'fuel left and august_retake_exam.25 fuel consumption', str(self.vehicle))


if __name__ == '__main__':
    main()
