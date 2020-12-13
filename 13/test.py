"""test_aoc_13"""

import unittest
from main import data_input, string_to_buses, part_1, part_2


class TestAoC13(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 295)

    def test_part_2_1(self):
        """()"""
        result = part_2(self.data[1])
        self.assertEqual(result, 1068781)

    def test_part_2_2(self):
        """()"""
        string = "17,x,13,19"
        buses = string_to_buses(string)
        result = part_2(buses)
        self.assertEqual(result, 3417)

    def test_part_2_3(self):
        """()"""
        string = "67,7,59,61"
        buses = string_to_buses(string)
        result = part_2(buses)
        self.assertEqual(result, 754018)

    def test_part_2_4(self):
        """()"""
        string = "67,x,7,59,61"
        buses = string_to_buses(string)
        result = part_2(buses)
        self.assertEqual(result, 779210)

    def test_part_2_5(self):
        """()"""
        string = "67,7,x,59,61"
        buses = string_to_buses(string)
        result = part_2(buses)
        self.assertEqual(result, 1261476)

    def test_part_2_6(self):
        """()"""
        string = "1789,37,47,1889"
        buses = string_to_buses(string)
        result = part_2(buses)
        self.assertEqual(result, 1202161486)


if __name__ == "__main__":
    unittest.main()
