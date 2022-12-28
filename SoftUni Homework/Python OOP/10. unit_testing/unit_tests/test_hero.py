from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('sashko', 99, 100, 200)
        self.enemy = Hero('goshko', 95, 100, 150)

    def test_correct_initialization(self):
        self.assertEqual('sashko', self.hero.username)
        self.assertEqual(99, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(200, self.hero.damage)

    def test_raise_error_if_tries_to_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_raise_error_if_tries_to_fight_without_health(self):
        with self.assertRaises(Exception) as ex:
            self.hero.health = 0
            self.hero.battle(self.enemy)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_raise_error_if_tries_to_fight_enemy_without_health(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual('You cannot fight goshko. He needs to rest', str(ex.exception))

    def test_correct_draw_condition_after_fight(self):
        self.enemy.level = 99
        self.enemy.damage = 200

        self.assertEqual('Draw', self.hero.battle(self.enemy))

    def test_correct_win_condition_after_fight(self):
        self.enemy.level = 1
        self.enemy.damage = 50
        self.assertEqual('You win', self.hero.battle(self.enemy))
        self.assertEqual(100, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(205, self.hero.damage)

    def test_correct_lose_condition_after_fight(self):
        self.hero.level = 1
        self.hero.damage = 50
        self.assertEqual('You lose', self.hero.battle(self.enemy))
        self.assertEqual(96, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(155, self.enemy.damage)

    def test_correct_represent(self):
        expected = 'Hero sashko: 99 lvl\n' \
                   'Health: 100\n' \
                   'Damage: 200\n'

        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()
