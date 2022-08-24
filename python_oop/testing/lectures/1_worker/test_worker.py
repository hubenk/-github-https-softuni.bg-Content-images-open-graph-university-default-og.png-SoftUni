"""
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called
•	Test if the get_info method returns the proper string with correct values
"""

from worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    valid_name = "Huben"
    valid_salary = 5000
    valid_energy = 100

    def test_init__name_salary_energy__validation(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)

    def test_energy_increment__after__rest_method_is_called(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        worker.rest()

        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_if_zero_energy_raise_error(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual("Not enough energy.", str(context.exception))

    def test_if_negative_energy_raise_error(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)
        with self.assertRaises(Exception):
            worker.work()


    def test_if_money_is_increased_by_salary_after_work_method(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected_money = worker.money + worker.salary

        worker.work()

        self.assertEqual(expected_money, worker.money)

    def test_is_energy_decreased_after_calling_work_method(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected_energy = self.valid_energy - 1

        worker.work()

        self.assertEqual(expected_energy, worker.energy)

    def test_if__get_info__returns_string_with_correct_values(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected_info = f"{self.valid_name} has saved {self.valid_salary} money."

        worker.work()

        self.assertEqual(expected_info, worker.get_info())


if __name__ == '__main__':
    unittest.main()