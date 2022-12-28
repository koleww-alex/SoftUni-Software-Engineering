from unit_testing.project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_initialization(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, self.toy_store.toy_shelf)

    def test_raise_error_if_shelf_does_not_exist_when_adding(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('Unknown', 'Barbie')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_raise_error_if_toy_with_the_same_name_is_placed_on_shelf(self):
        self.toy_store.toy_shelf['A'] = 'Barbie'
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Barbie')

        self.assertEqual('Toy is already in shelf!', str(ex.exception))

    def test_raise_error_if_shelf_is_taken(self):
        self.toy_store.toy_shelf['A'] = 'Barbie'
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Spider Man')

        self.assertEqual('Shelf is already taken!', str(ex.exception))

    def test_correct_add_toy_execute(self):
        result = self.toy_store.add_toy('A', 'Spider Man')
        expected = {
            "A": 'Spider Man',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.toy_store.toy_shelf)
        self.assertEqual('Toy:Spider Man placed successfully!', result)

    def test_raise_error_if_shelf_does_not_exist_when_removing(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('Unknown', 'Batman')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_raise_error_if_toy_with_different_name_is_on_shelf(self):
        self.toy_store.toy_shelf['A'] = 'Barbie'
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'Spider Man')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_correct_remove_toy_method_execute(self):
        self.toy_store.toy_shelf['A'] = 'Barbie'
        before = {
            "A": 'Barbie',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(before, self.toy_store.toy_shelf)
        result = self.toy_store.remove_toy('A', 'Barbie')
        self.assertEqual('Remove toy:Barbie successfully!', result)
        after = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(after, self.toy_store.toy_shelf)


if __name__ == '__main__':
    main()
