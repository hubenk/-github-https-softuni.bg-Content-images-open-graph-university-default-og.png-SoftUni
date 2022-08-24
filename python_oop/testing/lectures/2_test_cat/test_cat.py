"""
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
"""

import unittest

# from cat import Cat


class CatTest(unittest.TestCase):
    valid_name = "Kotka"
    valid_fed = False
    valid_sleepy = False
    valid_size = 0

    def test_is_size_increased_after_eating__and_is_cat_fed(self):
        cat = Cat(self.valid_name)
        expected_fed = True
        expected_sleepy = True
        expected_size = 1

        cat.eat()

        self.assertEqual(expected_fed, cat.fed)
        self.assertEqual(expected_sleepy, cat.sleepy)
        self.assertEqual(expected_size, cat.size)

    def test_raise_error__when_cat_is_already_fed(self):
        cat = Cat(self.valid_name)
        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_raise_error__when_cat_cannot_fall_asleep__if_not_fed(self):
        cat = Cat(self.valid_name)
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_if_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat(self.valid_name)
        self.assertFalse(cat.fed)

        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()