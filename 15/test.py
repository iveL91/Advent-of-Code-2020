"""test_aoc_15"""

import unittest
from main import data_input, part_1, part_2


class TestAoC15(unittest.TestCase):
    """()"""

    def test_part_1_1(self):
        """()"""
        starting_numbers = [0, 3, 6]
        result = part_1(starting_numbers)
        self.assertEqual(result, 436)

    def test_part_1_2(self):
        """()"""
        starting_numbers = [1, 3, 2]
        result = part_1(starting_numbers)
        self.assertEqual(result, 1)

    def test_part_1_3(self):
        """()"""
        starting_numbers = [2, 1, 3]
        result = part_1(starting_numbers)
        self.assertEqual(result, 10)

    def test_part_1_4(self):
        """()"""
        starting_numbers = [1, 2, 3]
        result = part_1(starting_numbers)
        self.assertEqual(result, 27)

    def test_part_1_5(self):
        """()"""
        starting_numbers = [2, 3, 1]
        result = part_1(starting_numbers)
        self.assertEqual(result, 78)

    def test_part_1_6(self):
        """()"""
        starting_numbers = [3, 2, 1]
        result = part_1(starting_numbers)
        self.assertEqual(result, 438)

    def test_part_1_7(self):
        """()"""
        starting_numbers = [3, 1, 2]
        result = part_1(starting_numbers)
        self.assertEqual(result, 1836)

    def test_part_1_8(self):
        """()"""
        starting_numbers = data_input("data")
        result = part_1(starting_numbers)
        self.assertEqual(result, 1085)

    def test_part_2_1(self):
        """()"""
        starting_numbers = [0, 3, 6]
        result = part_2(starting_numbers)
        self.assertEqual(result, 175594)

    def test_part_2_2(self):
        """()"""
        starting_numbers = [1, 3, 2]
        result = part_2(starting_numbers)
        self.assertEqual(result, 2578)

    def test_part_2_3(self):
        """()"""
        starting_numbers = [2, 1, 3]
        result = part_2(starting_numbers)
        self.assertEqual(result, 3544142)

    def test_part_2_4(self):
        """()"""
        starting_numbers = [1, 2, 3]
        result = part_2(starting_numbers)
        self.assertEqual(result, 261214)

    def test_part_2_5(self):
        """()"""
        starting_numbers = [2, 3, 1]
        result = part_2(starting_numbers)
        self.assertEqual(result, 6895259)

    def test_part_2_6(self):
        """()"""
        starting_numbers = [3, 2, 1]
        result = part_2(starting_numbers)
        self.assertEqual(result, 18)

    def test_part_2_7(self):
        """()"""
        starting_numbers = [3, 1, 2]
        result = part_2(starting_numbers)
        self.assertEqual(result, 362)

    def test_part_2_8(self):
        """()"""
        starting_numbers = data_input("data")
        result = part_2(starting_numbers)
        self.assertEqual(result, 10652)


if __name__ == "__main__":
    unittest.main()
