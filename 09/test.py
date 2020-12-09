"""test_aoc_09"""

import unittest
from main import data_input, check_sum_of_pair, constructor, encryption_weakness_min_max, encryption_weakness


class TestAoC09(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.xmas_outputs_1 = list(range(1, 26))
        cls.xmas_outputs_2 = data_input("test_data")

    def test_check_sum_of_pair_valid_1(self):
        result = check_sum_of_pair(self.xmas_outputs_1, 26)
        self.assertTrue(result)

    def test_check_sum_of_pair_valid_2(self):
        result = check_sum_of_pair(self.xmas_outputs_1, 49)
        self.assertTrue(result)

    def test_check_sum_of_pair_invalid_1(self):
        result = check_sum_of_pair(self.xmas_outputs_1, 100)
        self.assertFalse(result)

    def test_check_sum_of_pair_invalid_2(self):
        result = check_sum_of_pair(self.xmas_outputs_1, 50)
        self.assertFalse(result)

    def test_constructor(self):
        result = constructor(self.xmas_outputs_2, 5)
        self.assertEqual(result, 127)

    def test_encryption_weakness_min_max(self):
        invalid_number = constructor(self.xmas_outputs_2, 5)
        result = encryption_weakness_min_max(self.xmas_outputs_2, invalid_number)
        self.assertEqual(result, (15, 47))

    def test_encryption_weakness(self):
        invalid_number = constructor(self.xmas_outputs_2, 5)
        result = encryption_weakness(self.xmas_outputs_2, invalid_number)
        self.assertEqual(result, 62)


if __name__ == "__main__":
    unittest.main()
