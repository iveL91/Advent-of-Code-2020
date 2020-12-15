"""test_aoc_14"""

import unittest
from main import data_input, mask_value_overlap, memory_address_decoder, floating_address_to_addresses, part_1, part_2


class TestAoC14(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("data")
        cls.test_data_1 = data_input("test_data_1")
        cls.test_data_2 = data_input("test_data_2")

    def test_mask_value_overlap_1(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        value = 11
        result = mask_value_overlap(mask, value)
        expected_result = "000000000000000000000000000001001001"
        self.assertEqual(result, expected_result)

    def test_mask_value_overlap_2(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        value = 101
        result = mask_value_overlap(mask, value)
        expected_result = "000000000000000000000000000001100101"
        self.assertEqual(result, expected_result)

    def test_mask_value_overlap_3(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        value = 0
        result = mask_value_overlap(mask, value)
        expected_result = "000000000000000000000000000001000000"
        self.assertEqual(result, expected_result)

    def test_part_1_1(self):
        """()"""
        result = part_1(self.test_data_1)
        self.assertEqual(result, 165)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 12610010960049)

    def test_memory_address_decoder_1(self):
        mask = "000000000000000000000000000000X1001X"
        value = 42
        result = memory_address_decoder(mask, value)
        expected_result = "000000000000000000000000000000X1101X"
        self.assertEqual(result, expected_result)

    def test_memory_address_decoder_2(self):
        mask = "00000000000000000000000000000000X0XX"
        value = 26
        result = memory_address_decoder(mask, value)
        expected_result = "00000000000000000000000000000001X0XX"
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
        floating_address = "00000000000000000000000000000001X0XX"
        result = floating_address_to_addresses(floating_address)
        expected_result = ["000000000000000000000000000000010000",
                           "000000000000000000000000000000010001",
                           "000000000000000000000000000000010010",
                           "000000000000000000000000000000010011",
                           "000000000000000000000000000000011000",
                           "000000000000000000000000000000011001",
                           "000000000000000000000000000000011010",
                           "000000000000000000000000000000011011"]
        self.assertEqual(result, expected_result)

    def test_part_2_1(self):
        """()"""
        result = part_2(self.test_data_2)
        self.assertEqual(result, 208)

    def test_part_2_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 3608464522781)


if __name__ == "__main__":
    unittest.main()
