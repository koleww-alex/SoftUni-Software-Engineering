from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plant = Plantation(6)
        self.plant.plants = {'Ivan': ['rose', 'sunflower', 'violet'], 'Asen': ['rose', 'sunflower', 'violet']}
        self.plant.workers = ['Ivan', 'Asen']
    def test_correct_initialization(self):
        self.assertEqual(6, self.plant.size)
        self.assertEqual({'Ivan': ['rose', 'sunflower', 'violet'], 'Asen': ['rose', 'sunflower', 'violet']}, self.plant.plants)
        self.assertEqual(['Ivan', 'Asen'], self.plant.workers)

    def test_raise_error_if_size_is_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.size = -2

        self.assertEqual('Size must be positive number!', str(ve.exception))

    def test_raise_error_if_tries_to_add_same_worker_twice(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker('Ivan')

        self.assertEqual('Worker already hired!', str(ve.exception))

    def test_successful_hiring(self):
        result = self.plant.hire_worker('Gosho')
        self.assertEqual(['Ivan', 'Asen', 'Gosho'], self.plant.workers)
        self.assertEqual('Gosho successfully hired.', result)

    def test_correct__len__method(self):
        self.assertEqual(6, len(self.plant))

    def test_raise_error_if_unknown_worker_tries_to_plant(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.planting('Error', 'some_plant')

        self.assertEqual('Worker with name Error is not hired!', str(ve.exception))

    def test_raise_error_if_tries_to_add_more_flowers_when_full(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.planting('Ivan', 'violets')

        self.assertEqual('The plantation is full!', str(ve.exception))

    def test_worker_planting_plant(self):
        self.plant.size = 10
        result = self.plant.planting('Ivan', 'test_flower')
        self.assertEqual({'Ivan': ['rose', 'sunflower', 'violet', 'test_flower'],
                          'Asen': ['rose', 'sunflower', 'violet']}, self.plant.plants)
        self.assertEqual('Ivan planted test_flower.', result)

    def test_worker_planting_his_first_plant(self):
        self.plant.size = 10
        self.plant.workers.append('Andrey')
        result = self.plant.planting('Andrey', 'my_first_flower')
        self.assertEqual({'Ivan': ['rose', 'sunflower', 'violet'],
                          'Asen': ['rose', 'sunflower', 'violet'],
                          'Andrey': ['my_first_flower']}, self.plant.plants)
        self.assertEqual("Andrey planted it's first my_first_flower.", result)

    def test_correct__str__represent(self):
        expected = 'Plantation size: 6\n' \
                   'Ivan, Asen\n' \
                   'Ivan planted: rose, sunflower, violet\n' \
                   'Asen planted: rose, sunflower, violet'

        self.assertEqual(expected, str(self.plant))

    def test_correct__repr__represent(self):
        expected = 'Size: 6\n' \
                   'Workers: Ivan, Asen'

        self.assertEqual(expected, repr(self.plant))


if __name__ == '__main__':
    main()
