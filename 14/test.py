"""test_aoc_14"""

import unittest
from main import data_input, mask_value_overlap, memory_address_decoder, part_1, part_2


class TestAoC14(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")

    def test_mask_value_overlap_1(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        value = 11
        result = mask_value_overlap(mask, value)
        expected_result = "000000000000000000000000000001001001"
        self.assertEqual(result, expected_result)

    def test_mask_value_overlap_1(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        value = 101
        result = mask_value_overlap(mask, value)
        expected_result = "000000000000000000000000000001100101"
        self.assertEqual(result, expected_result)

    def test_memory_address_decoder_1(self):
        mask = "000000000000000000000000000000X1001X"
        value = 42
        result = memory_address_decoder(mask, value)
        expected_result = "000000000000000000000000000000X1101X"
        self.assertEqual(result, expected_result)
    

    # def test_part_1(self):
    #     """()"""
    #     result = part_1(self.data)
    #     self.assertEqual(result, 0)

    # def test_part_2(self):
    #     """()"""
    #     result = part_2(self.data)
    #     self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
