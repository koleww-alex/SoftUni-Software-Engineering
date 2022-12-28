from unittest import TestCase, main

# from Unit_Testing.code_to_test.test_cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat('Tobche')

    def test_correct_initializing(self):
        self.assertEqual('Tobche', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_raise_error_if_eats_after_its_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_its_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_its_sleepy_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_if_size_is_incremented_when_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_raise_error_if_tries_to_sleep_when_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_sleepy_is_set_to_False_when_slept(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
