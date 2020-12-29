"""test_aoc_23"""

import unittest
from main import data_input, CupGame, part_1, part_2


class TestAoC23(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data = data_input("test_data")
        cls.data = data_input("data")

    def test_part_1_1(self):
        """()"""
        result = part_1(self.test_data, 10)
        self.assertEqual(result, 92658374)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.test_data)
        self.assertEqual(result, 67384529)

    def test_part_1_3(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 97632548)

    # def test_part_2_1(self):
    #     """()"""
    #     result = part_2(self.test_data)
    #     self.assertEqual(result, 149245887792)

    # def test_part_2_2(self):
    #     """()"""
    #     result = part_2(self.data)
    #     self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
