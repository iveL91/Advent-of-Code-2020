"""test_aoc_07"""

import unittest
from main import data_input, Bag, part_1, part_2


class TestAoC07_1(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(self):
        Bag.bag_rules = data_input("test_data")
        self.my_bag = Bag("shiny gold")

    def test_contains_first_level_single_bag_inside(self):
        possible_bag = "bright white"
        self.my_bag.contains_one(possible_bag)
        self.assertTrue(possible_bag in self.my_bag.containing)

    def test_contains_first_level_multiple_bags_inside(self):
        possible_bag = "muted yellow"
        self.my_bag.contains_one(possible_bag)
        self.assertTrue(possible_bag in self.my_bag.containing)

    def test_contains_second_level_multiple_bags_inside_1(self):
        possible_bag = "dark orange"
        self.my_bag.contains()
        self.assertTrue(possible_bag in self.my_bag.containing)

    def test_contains_second_level_multiple_bags_inside_2(self):
        possible_bag = "light red"
        self.my_bag.contains()
        self.assertTrue(possible_bag in self.my_bag.containing)

    def test_part_1(self):
        """()"""
        result = part_1()
        self.assertEqual(result, 4)


class TestAoC07_2(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(self):
        Bag.bag_rules = data_input("test_data_2")

    def test_amount_one_level_single_bag_inside(self):
        result = part_2("dark violet")
        self.assertEqual(result, 0)

    def test_amount_two_levels_single_bag_inside(self):
        result = part_2("dark blue")
        self.assertEqual(result, 2)

    def test_amount_three_levels_single_bag_inside(self):
        result = part_2("dark green")
        self.assertEqual(result, 6)

    def test_part_2(self):
        """()"""
        result = part_2()
        self.assertEqual(result, 126)


if __name__ == "__main__":
    unittest.main()
