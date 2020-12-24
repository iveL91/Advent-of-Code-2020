"""test_aoc_24"""

import unittest
from main import data_input, part_1, part_2


class TestAoC24(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data = data_input("test_data")
        cls.data = data_input("data")

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 0)

    def test_part_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
