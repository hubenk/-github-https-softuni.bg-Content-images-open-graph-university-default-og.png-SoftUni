from list import IntegerList

import unittest

class IntegerListTest(unittest.TestCase):

    def test_init__with_non_integer(self):
        integer = IntegerList(2.55, "test", [1, 2], {1: "a", 2: "b"})

        self.assertEqual([], integer._IntegerList__data)

    def test_init__with_valid_integer(self):
        integer = IntegerList(1, 20, 304, 4050)

        self.assertEqual([1, 20, 304, 4050], integer._IntegerList__data)

    def test_init__with_no_entry(self):
        integer = IntegerList()

        self.assertEqual([], integer._IntegerList__data)

    def test_get_data_method_is_working(self):
        integer = IntegerList(2, 4, 600)
        result = integer.get_data()

        self.assertEqual([2, 4, 600], result)

    def test_add_method__with_valid_entry(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)
        expected_result = [2]

        result = integer.add(2)

        self.assertEqual(expected_result, result)

    def test_add_method__with_invalid_entry__raises_error(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            integer.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_method__with_valid_index(self):
        integer = IntegerList(1, 20, 304, 4050)
        expected_result = integer._IntegerList__data[3]

        result = integer.remove_index(3)

        self.assertEqual(expected_result, result)

    def test_remove_index_method__with_invalid_entry_raises_error(self):
        integer = IntegerList(1, 20, 304, 4050)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method__with_valid_index(self):
        integer = IntegerList(1, 20, 304, 4050)
        expected_result = 20

        result = integer.get(1)

        self.assertEqual(expected_result, result)

    def test_get_method__with_invalid_index_raises_error(self):

        integer = IntegerList(1, 20, 304, 4050)

        with self.assertRaises(IndexError) as ex:
            integer.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method__with_valid_entry(self):
        integer = IntegerList(1, 20, 304, 4050)
        valid_index = 2
        valid_element = 5

        integer.insert(valid_index, valid_element)

        self.assertEqual(valid_element, integer._IntegerList__data[valid_index])

    def test_insert_method__with_invalid_index_raises_error(self):
        integer = IntegerList(1, 20, 304, 4050)
        invalid_index = 5
        valid_element = 6

        with self.assertRaises(IndexError) as ex:
            integer.insert(invalid_index, valid_element)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method__with_invalid_integer_raises_error(self):
        integer = IntegerList(1, 20, 304, 4050)
        valid_index = 3
        invalid_element = 6.7

        with self.assertRaises(ValueError) as ex:
            integer.insert(valid_index, invalid_element)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_method__with_valid_entry(self):
        integer = IntegerList(1, 20, 304, 4050)
        biggest_integer = 4050

        result = integer.get_biggest()

        self.assertEqual(biggest_integer, result)

    def test_get_index_method_with_valid_entry(self):
        integer = IntegerList(1, 20, 304, 4050)
        valid_element = 20
        expected_index = 1

        result = integer.get_index(valid_element)

        self.assertEqual(expected_index, result)


if __name__ == '__main__':
    unittest.main()