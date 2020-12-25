"""test_aoc_25"""

import unittest
from main import data_input, transforming_subject_number, part_1


class TestAoC25(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data = data_input("test_data")
        cls.data = data_input("data")

    def test_transforming_subject_number_1(self):
        public_key = self.test_data[0]
        result = transforming_subject_number(7, 8)
        self.assertEqual(public_key, result)

    def test_transforming_subject_number_2(self):
        public_key = self.test_data[1]
        result = transforming_subject_number(7, 11)
        self.assertEqual(public_key, result)

    def test_part_1_1(self):
        """()"""
        result = part_1(self.test_data)
        self.assertEqual(result, 14897079)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 18608573)


if __name__ == "__main__":
    unittest.main()
