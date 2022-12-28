from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Beche', 'cat', 'meow')

    def test_correct_initializing(self):
        self.assertEqual('Beche', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_correct_kingdom_represent(self):
        self.assertEqual('Beche makes meow', self.mammal.make_sound())

    def test_getter(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_correct_info_represent(self):
        self.assertEqual('Beche is of type cat', self.mammal.info())


if __name__ == '__main__':
    main()
