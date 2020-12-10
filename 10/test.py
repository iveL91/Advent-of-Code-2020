"""test_aoc_10"""

import unittest
from main import data_input, n_jolt_differences, part_1, part_2


class TestAoC10(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.adapters_1 = data_input("test_data_1")
        cls.adapters_2 = data_input("test_data_2")

    def test_one_jolt_differences_1(self):
        result = n_jolt_differences(self.adapters_1, 1)
        self.assertEqual(result, 7)

    def test_one_jolt_differences_2(self):
        result = n_jolt_differences(self.adapters_2, 1)
        self.assertEqual(result, 22)

    def test_three_jolt_differences_1(self):
        result = n_jolt_differences(self.adapters_1, 3)
        self.assertEqual(result, 5)

    def test_three_jolt_differences_2(self):
        result = n_jolt_differences(self.adapters_2, 3)
        self.assertEqual(result, 10)

    def test_part_1_1(self):
        """()"""
        result = part_1(self.adapters_1)
        self.assertEqual(result, 35)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.adapters_2)
        self.assertEqual(result, 220)

    def test_part_2_1(self):
        """()"""
        result = part_2(self.adapters_1)
        self.assertEqual(result, 8)

    def test_part_2_2(self):
        """()"""
        result = part_2(self.adapters_2)
        self.assertEqual(result, 19208)


if __name__ == "__main__":
    unittest.main()
