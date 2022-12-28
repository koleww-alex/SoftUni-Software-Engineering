from unittest import TestCase, main

# from Unit_Testing.code_to_test.list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.test_list = IntegerList(1, 2, 3, '4')

    def test_if_only_integers_are_accepted_in_the_list(self):
        self.assertEqual([1, 2, 3], self.test_list.get_data())

    def test_raise_error_if_item_to_add_is_not_int(self):
        with self.assertRaises(ValueError) as vl:
            self.test_list.add('4')

        self.assertEqual('Element is not Integer', str(vl.exception))

    def test_correct_add_when_adding_int(self):
        self.assertEqual([1, 2, 3, 5], self.test_list.add(5))

    def test_raise_error_when_removing_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.test_list.remove_index(4)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_correct_removing_by_index(self):
        self.test_list.remove_index(2)
        self.assertEqual([1, 2], self.test_list.get_data())

    def test_raise_error_when_getting_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.test_list.get(4)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_correct_get_method(self):
        self.assertEqual(3, self.test_list.get(2))

    def test_raising_error_when_inserting_on_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.test_list.insert(5, 10)

        self.assertEqual('Index is out of range', str(ie.exception))

    def test_raising_error_if_inserted_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ie:
            self.test_list.insert(2, '4')

        self.assertEqual('Element is not Integer', str(ie.exception))

    def test_correct_inserting(self):
        self.test_list.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], self.test_list.get_data())

    def test_get_biggest_number(self):
        self.assertEqual(3, self.test_list.get_biggest())

    def test_correct_index_returned(self):
        self.assertEqual(1, self.test_list.get_index(2))


if __name__ == '__main__':
    main()
