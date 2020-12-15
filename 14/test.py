"""test_aoc_14"""

import unittest
from main import data_input, uint_b36, int_to_uint_b36, floating_address_to_addresses, part_1, part_2


class TestAoC14_1(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("data")
        cls.test_data = data_input("test_data_1")
        uint_b36.overwrite_instructions = {"0": True,
                                           "1": True,
                                           "X": False}

    def test_mask_value_overlap_1(self):
        mask = uint_b36("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = int_to_uint_b36(11)
        result = mask + value
        expected_result = uint_b36("000000000000000000000000000001001001")
        self.assertEqual(result, expected_result)

    def test_mask_value_overlap_2(self):
        mask = uint_b36("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = int_to_uint_b36(101)
        result = mask + value
        expected_result = uint_b36("000000000000000000000000000001100101")
        self.assertEqual(result, expected_result)

    def test_mask_value_overlap_3(self):
        mask = uint_b36("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = int_to_uint_b36(0)
        result = mask + value
        expected_result = uint_b36("000000000000000000000000000001000000")
        self.assertEqual(result, expected_result)

    def test_part_1_1(self):
        """()"""
        result = part_1(self.test_data)
        self.assertEqual(result, 165)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 12610010960049)


class TestAoC14_2(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("data")
        cls.test_data = data_input("test_data_2")
        uint_b36.overwrite_instructions = {"0": False,
                                           "1": True,
                                           "X": True}

    def test_memory_address_decoder_1(self):
        mask = uint_b36("000000000000000000000000000000X1001X")
        value = int_to_uint_b36(42)
        result = mask + value
        expected_result = uint_b36("000000000000000000000000000000X1101X")
        self.assertEqual(result, expected_result)

    def test_memory_address_decoder_2(self):
        mask = uint_b36("00000000000000000000000000000000X0XX")
        value = int_to_uint_b36(26)
        result = mask + value
        expected_result = uint_b36("00000000000000000000000000000001X0XX")
        self.assertEqual(result, expected_result)

    def test_floating_address_to_addresses_1(self):
        floating_address = "000000000000000000000000000000X1101X"
        result = floating_address_to_addresses(floating_address)
        expected_result = ["000000000000000000000000000000011010",
                           "000000000000000000000000000000011011",
                           "000000000000000000000000000000111010",
                           "000000000000000000000000000000111011"]
        self.assertEqual(result, expected_result)

    def test_floating_address_to_addresses_2(self):
        floating_address = uint_b36("00000000000000000000000000000001X0XX")
        result = floating_address_to_addresses(floating_address)
        lst = ["000000000000000000000000000000010000",
               "000000000000000000000000000000010001",
               "000000000000000000000000000000010010",
               "000000000000000000000000000000010011",
               "000000000000000000000000000000011000",
               "000000000000000000000000000000011001",
               "000000000000000000000000000000011010",
               "000000000000000000000000000000011011"]
        expected_result = [uint_b36(string) for string in lst]
        self.assertEqual(result, expected_result)

    def test_part_2_1(self):
        """()"""
        result = part_2(self.test_data)
        self.assertEqual(result, 208)

    def test_part_2_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 3608464522781)


if __name__ == "__main__":
    unittest.main()
