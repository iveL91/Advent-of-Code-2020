"""test_aoc_02"""

import unittest
from main import data_input, password_instruction_transformation, valid_old_password, part_1, valid_new_password, part_2


class TestAoC02(unittest.TestCase):
    """()"""

    def test_valid_old_password_1(self):
        password = password_instruction_transformation("1-3 a: abcde")
        result = valid_old_password(password)
        self.assertEqual(result, True)

    def test_valid_old_password_2(self):
        password = password_instruction_transformation("1-3 b: cdefg")
        result = valid_old_password(password)
        self.assertEqual(result, False)

    def test_valid_old_password_3(self):
        password = password_instruction_transformation("2-9 c: ccccccccc")
        result = valid_old_password(password)
        self.assertEqual(result, True)

    def test_part_1(self):
        """()"""
        data = data_input("test_data")
        result = part_1(data)
        self.assertEqual(result, 2)

    def test_valid_new_password_1(self):
        password = password_instruction_transformation("1-3 a: abcde")
        result = valid_new_password(password)
        self.assertEqual(result, True)

    def test_valid_new_password_2(self):
        password = password_instruction_transformation("1-3 b: cdefg")
        result = valid_new_password(password)
        self.assertEqual(result, False)

    def test_valid_new_password_3(self):
        password = password_instruction_transformation("2-9 c: ccccccccc")
        result = valid_new_password(password)
        self.assertEqual(result, False)

    def test_part_2(self):
        """()"""
        data = data_input("test_data")
        result = part_2(data)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
