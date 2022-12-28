from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie('StarWars', 1989, 10)
        self.movie.actors = ['Darth Vader', 'Anakin Skywalker']
    def test_correct_initialization(self):
        self.assertEqual('StarWars', self.movie.name)
        self.assertEqual(1989, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual(['Darth Vader', 'Anakin Skywalker'], self.movie.actors)

    def test_raise_error_if_invalid_name_is_given(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual('Name cannot be an empty string!', str(ve.exception))

    def test_raise_error_if_invalid_year_is_given(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1500

        self.assertEqual('Year is not valid!', str(ve.exception))

    def test_add_same_actor_twice(self):
        result = self.movie.add_actor('Darth Vader')
        self.assertEqual('Darth Vader is already added in the list of actors!', result)

    def test_correct_add_actor(self):
        self.movie.add_actor('Test')
        self.assertEqual(['Darth Vader', 'Anakin Skywalker', 'Test'], self.movie.actors)

    def test_first_case_of__gt__method(self):
        self.other_movie = Movie('Indiana Jones', 2002, 8)
        result = self.movie > self.other_movie
        self.assertEqual('"StarWars" is better than "Indiana Jones"', result)

    def test_second_case_of__gt__method(self):
        self.other_movie = Movie('Indiana Jones', 2002, 11)
        result = self.movie > self.other_movie
        self.assertEqual('"Indiana Jones" is better than "StarWars"', result)

    def test_correct__repr__method(self):
        expected = f"Name: StarWars\n" \
               f"Year of Release: 1989\n" \
               f"Rating: 10.00\n" \
               f"Cast: Darth Vader, Anakin Skywalker"
        self.assertEqual(expected, repr(self.movie))

if __name__ == '__main__':
    main()
