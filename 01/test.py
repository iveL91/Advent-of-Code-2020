"""test_aoc_01"""

import unittest
from main import data_input, find_numbers_sum_equal_year, part_1, part_2


class TestAoC01(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")

    def test_find_numbers_equal_year_length_2(self):
        result = find_numbers_sum_equal_year(self.data, 2)
        self.assertEqual(result, (1721, 299))

    def test_find_numbers_equal_year_length_3(self):
        result = find_numbers_sum_equal_year(self.data, 3)
        self.assertEqual(result, (979, 366, 675))

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 514579)

    def test_part_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 241861950)


if __name__ == "__main__":
    unittest.main()
