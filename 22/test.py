"""test_aoc_22"""

import unittest
from main import data_input, part_1, part_2


class TestAoC22(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data = data_input("test_data")
        cls.data = data_input("data")

    def test_part_1_1(self):
        """()"""
        result = part_1(self.test_data)
        self.assertEqual(result, 306)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 32162)

    def test_part_2_1(self):
        """()"""
        result = part_2(self.test_data)
        self.assertEqual(result, 291)

    def test_part_2_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 32534)

if __name__ == "__main__":
    unittest.main()
