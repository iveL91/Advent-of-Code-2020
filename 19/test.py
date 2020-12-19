"""test_aoc_19"""

import unittest
from main import data_input, part_1_test, part_1, part_2


class TestAoC19(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.test_data_1 = data_input("test_data_1")
        cls.test_data_2 = data_input("test_data_2")
        cls.data = data_input("data")

#     def test_determine_rules(self):
#         rules_string = '''0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"'''
#         rules_list = rules_string.splitlines()
#         result = determine_rules(determine_rules)
#         expected_result = {}
#         self.assertEqual(result, expected_result)

    def test_part_1_1(self):
        """()"""
        result = part_1_test(self.test_data_1)
        self.assertEqual(result, 2)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 171)

    def test_part_2_1(self):
        """()"""
        result = part_2(self.test_data_2)
        self.assertEqual(result, 12)

    def test_part_2_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 369)


if __name__ == "__main__":
    unittest.main()
