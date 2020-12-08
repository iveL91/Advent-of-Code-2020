"""test_aoc_09"""

import unittest
from main import data_input, part_1, part_2


class TestAoC09(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")

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
