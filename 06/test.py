"""test_aoc_06"""

import unittest
from main import data_input, part_1, part_2


class TestAoC06(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(self):
        self.data = data_input("test_data")

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
