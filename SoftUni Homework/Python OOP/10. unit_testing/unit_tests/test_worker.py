from unittest import TestCase, main

# from Unit_Testing.code_to_test.test_worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker('Alex', 10_000, 100)

    def test_correct_initializing(self):
        self.assertEqual('Alex', self.worker.name)
        self.assertEqual(10_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)

    def test_if_error_is_raised_when_working_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_worker_successfully_receives_monthly_payment(self):
        self.worker.work()
        self.assertEqual(10_000, self.worker.money)

    def test_if_worker_uses_energy_when_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_if_worker_receives_energy_when_resting(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_if_the_represent_data_is_correct(self):
        self.assertEqual('Alex has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
