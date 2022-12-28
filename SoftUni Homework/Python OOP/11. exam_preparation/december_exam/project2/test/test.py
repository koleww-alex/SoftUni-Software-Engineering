from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team = Team('Test')
        self.team.members = {'Hristo': 29, 'Messi': 33, 'Ronaldo': 34}

    def test_correct_initialization(self):
        self.assertEqual('Test', self.team.name)
        self.assertEqual({'Hristo': 29, 'Messi': 33, 'Ronaldo': 34}, self.team.members)

    def test_raise_error_if_invalid_name_given(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'ivan123'

        self.assertEqual('Team Name can contain only letters!', str(ve.exception))

    def test_correct_added_players(self):
        result = self.team.add_member(Ivan=22, Hristo=29, Peter=24)
        self.assertEqual({'Hristo': 29, 'Messi': 33, 'Ronaldo': 34, 'Ivan': 22, 'Peter':24}, self.team.members)
        self.assertEqual('Successfully added: Ivan, Peter', result)

    def test_raise_error_if_tries_to_remove_not_existing_member(self):
        result = self.team.remove_member('Error')
        self.assertEqual('Member with name Error does not exist', result)

    def test_correct_removing_a_member(self):
        result = self.team.remove_member('Ronaldo')
        self.assertEqual({'Hristo': 29, 'Messi': 33}, self.team.members)
        self.assertEqual('Member Ronaldo removed', result)

    def test_correct__gt__method(self):
        self.other = Team('OtherTest')
        first_case_result = self.team > self.other
        self.assertEqual(True, first_case_result)

        second_case_result = self.other > self.team
        self.assertEqual(False, second_case_result)

    def test_correct__len__method(self):
        self.assertEqual(3, len(self.team))

    def test_correct__add__method(self):
        self.other = Team('OtherTest')
        self.other.members = {'Test': 20}
        merged_team = self.team + self.other
        self.assertEqual('TestOtherTest', merged_team.name)
        self.assertEqual({'Hristo': 29, 'Messi': 33, 'Ronaldo': 34, 'Test': 20}, merged_team.members)

    def test_correct__str__method(self):
        self.team.members = {'Hristo': 29, 'Messi': 33, 'Ronaldo': 34, 'Alabama': 29}
        expected = 'Team name: Test\n' \
                   'Member: Ronaldo - 34-years old\n' \
                   'Member: Messi - 33-years old\n' \
                   'Member: Alabama - 29-years old\n' \
                   'Member: Hristo - 29-years old'

        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    main()