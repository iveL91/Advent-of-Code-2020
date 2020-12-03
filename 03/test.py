"""test_aoc_03"""

import unittest
from main import data_input, Spaceship, part_1, part_2


class TestAoC03(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(self):
        Spaceship.space_grid = data_input("test_data")

    def test_tree_encounters_movement_1_3(self):
        spaceship = Spaceship(movement=(1, 3))
        result = spaceship.fly().tree_encounters
        self.assertEqual(result, 7)

    def test_part_1(self):
        """()"""
        result = part_1()
        self.assertEqual(result, 7)

    def test_tree_encounters_movement_1_1(self):
        spaceship = Spaceship(movement=(1, 1))
        result = spaceship.fly().tree_encounters
        self.assertEqual(result, 2)

    def test_tree_encounters_movement_1_5(self):
        spaceship = Spaceship(movement=(1, 5))
        result = spaceship.fly().tree_encounters
        self.assertEqual(result, 3)

    def test_tree_encounters_movement_1_7(self):
        spaceship = Spaceship(movement=(1, 7))
        result = spaceship.fly().tree_encounters
        self.assertEqual(result, 4)

    def test_tree_encounters_movement_2_1(self):
        spaceship = Spaceship(movement=(2, 1))
        result = spaceship.fly().tree_encounters
        self.assertEqual(result, 2)

    def test_part_2(self):
        """()"""
        result = part_2()
        self.assertEqual(result, 336)


if __name__ == "__main__":
    unittest.main()
