"""test_aoc_07"""

import unittest
from main import data_input, different_letters_in_group, same_letters_in_group, part_1, part_2


class TestAoC07(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")

    def test_different_letters_in_group_1(self):
        result = different_letters_in_group(self.data[0])
        self.assertEqual(result, 3)

    def test_different_letters_in_group_2(self):
        result = different_letters_in_group(self.data[1])
        self.assertEqual(result, 3)

    def test_different_letters_in_group_3(self):
        result = different_letters_in_group(self.data[2])
        self.assertEqual(result, 3)

    def test_different_letters_in_group_4(self):
        result = different_letters_in_group(self.data[3])
        self.assertEqual(result, 1)

    def test_different_letters_in_group_5(self):
        result = different_letters_in_group(self.data[4])
        self.assertEqual(result, 1)

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 11)

    def test_same_letters_in_group_1(self):
        result = same_letters_in_group(self.data[0])
        self.assertEqual(result, 3)

    def test_same_letters_in_group_2(self):
        result = same_letters_in_group(self.data[1])
        self.assertEqual(result, 0)

    def test_same_letters_in_group_3(self):
        result = same_letters_in_group(self.data[2])
        self.assertEqual(result, 1)

    def test_same_letters_in_group_4(self):
        result = same_letters_in_group(self.data[3])
        self.assertEqual(result, 1)

    def test_same_letters_in_group_5(self):
        result = same_letters_in_group(self.data[4])
        self.assertEqual(result, 1)

    def test_part_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
