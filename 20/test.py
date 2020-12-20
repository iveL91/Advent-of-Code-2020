"""test_aoc_20"""

import unittest
from main import data_input, part_1, part_2


class TestAoC20(unittest.TestCase):
    """()"""

    # @classmethod
    # def setUpClass(cls):
    #     cls.test_data = data_input("test_data")
    #     cls.data = data_input("data")

    def test_part_1_1(self):
        """()"""
        tiles = data_input("test_data")
        result = part_1(tiles)
        self.assertEqual(result, 20899048083289)

    def test_part_1_2(self):
        """()"""
        tiles = data_input("data")
        result = part_1(tiles)
        self.assertEqual(result, 18482479935793)

    def test_part_2_1(self):
        """()"""
        tiles = data_input("test_data")
        result = part_2(tiles)
        self.assertEqual(result, 273)

    def test_part_2_2(self):
        """()"""
        tiles = data_input("data")
        result = part_2(tiles)
        self.assertEqual(result, 2118)


if __name__ == "__main__":
    unittest.main()
