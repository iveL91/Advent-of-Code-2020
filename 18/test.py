"""test_aoc_18"""

import unittest
from main import data_input, reduction, part_1, part_2


class TestAoC18(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data = data_input("test_data")
        cls.data = data_input("data")

    def test_reduction_1(self):
        term = self.test_data[0]
        result = int(reduction(term))
        self.assertEqual(result, 71)

    def test_reduction_2(self):
        term = self.test_data[1]
        result = int(reduction(term))
        self.assertEqual(result, 51)

    def test_reduction_3(self):
        term = self.test_data[2]
        result = int(reduction(term))
        self.assertEqual(result, 26)

    def test_reduction_4(self):
        term = self.test_data[3]
        result = int(reduction(term))
        self.assertEqual(result, 437)

    def test_reduction_5(self):
        term = self.test_data[4]
        result = int(reduction(term))
        self.assertEqual(result, 12240)

    def test_reduction_6(self):
        term = self.test_data[5]
        result = int(reduction(term))
        self.assertEqual(result, 13632)

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 67800526776934)

    def test_advanced_reduction_1(self):
        term = self.test_data[0]
        result = int(reduction(term, 2))
        self.assertEqual(result, 231)

    def test_advanced_reduction_2(self):
        term = self.test_data[1]
        result = int(reduction(term, 2))
        self.assertEqual(result, 51)

    def test_advanced_reduction_3(self):
        term = self.test_data[2]
        result = int(reduction(term, 2))
        self.assertEqual(result, 46)

    def test_advanced_reduction_4(self):
        term = self.test_data[3]
        result = int(reduction(term, 2))
        self.assertEqual(result, 1445)

    def test_advanced_reduction_5(self):
        term = self.test_data[4]
        result = int(reduction(term, 2))
        self.assertEqual(result, 669060)

    def test_advanced_reduction_6(self):
        term = self.test_data[5]
        result = int(reduction(term, 2))
        self.assertEqual(result, 23340)

    def test_advanced_reduction_7(self):
        term = self.data[128]
        result = int(reduction(term, 2))
        self.assertEqual(result, 12936)

    # def test_advanced_reduction_8(self):
    #     term = self.data[1]
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 403200)

    # def test_advanced_reduction_9(self):
    #     term = self.data[2]
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 32411)

    # def test_advanced_reduction_10(self):
    #     term = self.data[3]
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 1246921686)

    # def test_advanced_reduction_11(self):
    #     term = self.data[4]
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 437184)

    # def test_advanced_reduction_12(self):
    #     term = self.data[5]
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 133650)

    # def test_advanced_reduction_13(self):
    #     term = self.data[7]
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 24076)

    # def test_advanced_reduction_14(self):
    #     term = "(3 + 4 * (8 + 4 * (7 * 4 + (5 * 6 + 3) + 3 * (3 + 4)))) + 3"
    #     result = int(reduction(term, 2))
    #     self.assertEqual(result, 214035)

    def test_part_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 340789638435483)


if __name__ == "__main__":
    unittest.main()
