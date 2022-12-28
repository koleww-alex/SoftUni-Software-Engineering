from project.library import Library
from unittest import TestCase, main

class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library('Test')
        self.library.books_by_authors = {'Ivan Vazov': ['Pod Igoto']}
        self.library.readers = {}
        self.readers = {'Asen': []}

    def test_correct_initialization(self):
        self.assertEqual('Test', self.library.name)
        self.assertEqual({'Ivan Vazov': ['Pod Igoto']}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_raise_error_if_invalid_name_given(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual('Name cannot be empty string!', str(ve.exception))

    def test_correct_adding_a_book_method(self):
        self.library.add_book('Ivan Vazov', 'Pod Igoto New')
        self.assertEqual({'Ivan Vazov': ['Pod Igoto', 'Pod Igoto New']}, self.library.books_by_authors)
        self.library.add_book('New Author', 'new_title')
        self.assertEqual({'Ivan Vazov': ['Pod Igoto', 'Pod Igoto New'], 'New Author': ['new_title']}, self.library.books_by_authors)
        self.library.add_book('Ivan Vazov', 'Pod Igoto')
        self.assertEqual({'Ivan Vazov': ['Pod Igoto', 'Pod Igoto New'], 'New Author': ['new_title']}, self.library.books_by_authors)
        self.library.add_book('New Author', 'next_new_title')
        self.assertEqual({'Ivan Vazov': ['Pod Igoto', 'Pod Igoto New'], 'New Author': ['new_title', 'next_new_title']}, self.library.books_by_authors)
    def test_raise_error_if_tries_to_add_already_existing_member(self):
        self.library.readers = self.readers
        result = self.library.add_reader('Asen')
        self.assertEqual('Asen is already registered in the Test library.', result)

    def test_correct_adding_a_member_method(self):
        self.library.readers = self.readers
        self.library.add_reader('Pesho')
        self.assertEqual({'Asen': [], 'Pesho': []}, self.library.readers)

    def test_raise_error_if_reader_not_registered(self):
        result = self.library.rent_book('Unknown', 'Ivan Vazov', 'Pod Igoto')
        self.assertEqual('Unknown is not registered in the Test Library.', result)

    def test_raise_error_if_the_given_author_does_not_exist(self):
        self.library.readers = self.readers
        result = self.library.rent_book('Asen', 'Unknown Author', 'unknown_book')
        self.assertEqual("Test Library does not have any Unknown Author's books.", result)

    def test_raise_error_if_the_given_book_does_not_exist(self):
        self.library.readers = self.readers
        result = self.library.rent_book('Asen', 'Ivan Vazov', 'unknown_book')
        self.assertEqual("""Test Library does not have Ivan Vazov's "unknown_book".""", result)

    def test_correct_rent_book_method(self):
        self.library.readers = self.readers
        self.library.books_by_authors = {'Ivan Vazov': ['Pod Igoto'], 'New Author': ['New Book']}
        self.library.rent_book('Asen', 'New Author', 'New Book')
        self.assertEqual({'Asen': [{'New Author': 'New Book'}]}, self.library.readers)
        self.assertEqual({'Ivan Vazov': ['Pod Igoto'], 'New Author': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()