"""test_aoc_16"""

import unittest
from main import data_input, valid_number, part_1, valid_ticket, fields, part_2


class TestAoC16(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("data")
        cls.data_1 = data_input("test_data_1")
        cls.data_2 = data_input("test_data_2")

    def test_valid_number_true_1(self):
        result = valid_number(
            self.data_1.nearby_tickets[0][0], self.data_1.properties.values())
        self.assertTrue(result)

    def test_valid_number_true_2(self):
        result = valid_number(
            self.data_1.nearby_tickets[0][1], self.data_1.properties.values())
        self.assertTrue(result)

    def test_valid_number_true_3(self):
        result = valid_number(
            self.data_1.nearby_tickets[0][2], self.data_1.properties.values())
        self.assertTrue(result)

    def test_valid_number_false_1(self):
        result = valid_number(
            self.data_1.nearby_tickets[1][1], self.data_1.properties.values())
        self.assertFalse(result)

    def test_valid_number_false_2(self):
        result = valid_number(
            self.data_1.nearby_tickets[2][0], self.data_1.properties.values())
        self.assertFalse(result)

    def test_valid_number_false_3(self):
        result = valid_number(
            self.data_1.nearby_tickets[3][2], self.data_1.properties.values())
        self.assertFalse(result)

    def test_part_1_1(self):
        """()"""
        result = part_1(self.data_1)
        self.assertEqual(result, 71)

    def test_part_1_2(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 20060)

    def test_valid_ticket(self):
        result = valid_ticket(
            self.data_1.nearby_tickets[0], self.data_1.properties.values())
        self.assertTrue(result)

    def test_fields_1(self):
        result = fields(self.data_2)
        expected_result = {"row": 0,
                           "class": 1,
                           "seat": 2}
        self.assertEqual(result, expected_result)

    def test_fields_2(self):
        result = fields(self.data)
        expected_result = {'arrival platform': 0,
                           'departure station': 1,
                           'departure track': 2,
                           'type': 3,
                           'class': 4,
                           'departure location': 5,
                           'arrival track': 6,
                           'duration': 7,
                           'departure platform': 8,
                           'zone': 9,
                           'row': 10,
                           'departure time': 11,
                           'route': 12,
                           'wagon': 13,
                           'seat': 14,
                           'departure date': 15,
                           'arrival station': 16,
                           'arrival location': 17,
                           'price': 18,
                           'train': 19}
        self.assertEqual(result, expected_result)

    def test_part_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 2843534243843)


if __name__ == "__main__":
    unittest.main()
