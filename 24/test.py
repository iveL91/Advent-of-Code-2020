"""test_aoc_24"""

import unittest
from main import data_input, part_1, part_2


class TestAoC24(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data = data_input("test_data")
        cls.data = data_input("data")

    def test_part_1_1(self):
        result = part_1(self.test_data)
        self.assertEqual(result, 10)

    def test_part_1_2(self):
        result = part_1(self.data)
        self.assertEqual(result, 373)

    def test_part_2_1(self):
        result = part_2(self.test_data, 1)
        self.assertEqual(result, 15)

    def test_part_2_2(self):
        result = part_2(self.test_data, 2)
        self.assertEqual(result, 12)

    def test_part_2_3(self):
        result = part_2(self.test_data, 3)
        self.assertEqual(result, 25)

    def test_part_2_4(self):
        result = part_2(self.test_data, 4)
        self.assertEqual(result, 14)

    def test_part_2_5(self):
        result = part_2(self.test_data, 5)
        self.assertEqual(result, 23)

    def test_part_2_6(self):
        result = part_2(self.test_data, 6)
        self.assertEqual(result, 28)

    def test_part_2_7(self):
        result = part_2(self.test_data, 7)
        self.assertEqual(result, 41)

    def test_part_2_8(self):
        result = part_2(self.test_data, 8)
        self.assertEqual(result, 37)

    def test_part_2_9(self):
        result = part_2(self.test_data, 9)
        self.assertEqual(result, 49)

    def test_part_2_10(self):
        result = part_2(self.test_data, 10)
        self.assertEqual(result, 37)

    def test_part_2_11(self):
        result = part_2(self.test_data, 20)
        self.assertEqual(result, 132)

    def test_part_2_12(self):
        result = part_2(self.test_data, 30)
        self.assertEqual(result, 259)

    def test_part_2_13(self):
        result = part_2(self.test_data, 40)
        self.assertEqual(result, 406)

    def test_part_2_14(self):
        result = part_2(self.test_data, 50)
        self.assertEqual(result, 566)

    def test_part_2_15(self):
        result = part_2(self.test_data, 60)
        self.assertEqual(result, 788)

    def test_part_2_16(self):
        result = part_2(self.test_data, 70)
        self.assertEqual(result, 1106)

    def test_part_2_17(self):
        result = part_2(self.test_data, 80)
        self.assertEqual(result, 1373)

    def test_part_2_18(self):
        result = part_2(self.test_data, 90)
        self.assertEqual(result, 1844)

    def test_part_2_19(self):
        result = part_2(self.test_data)
        self.assertEqual(result, 2208)

    def test_part_2_20(self):
        result = part_2(self.data)
        self.assertEqual(result, 3917)


if __name__ == "__main__":
    unittest.main()
