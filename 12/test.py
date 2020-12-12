"""test_aoc_12"""

import unittest
from main import data_input, data_transformation, Ship, part_1, part_2


class TestAoC12(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.navigation_instructions = data_input("test_data")
        cls.ship = Ship(cls.navigation_instructions)

    def test_move_north_1(self):
        navigation_instruction = data_transformation("N1")
        self.ship.position = (0, 0)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (0, 1))

    def test_move_north_2(self):
        navigation_instruction = data_transformation("N1")
        self.ship.position = (1, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (1, 2))

    def test_move_south_1(self):
        navigation_instruction = data_transformation("S1")
        self.ship.position = (0, 0)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (0, -1))

    def test_move_south_2(self):
        navigation_instruction = data_transformation("S1")
        self.ship.position = (1, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (1, 0))

    def test_move_east_1(self):
        navigation_instruction = data_transformation("E1")
        self.ship.position = (0, 0)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (1, 0))

    def test_move_east_2(self):
        navigation_instruction = data_transformation("E1")
        self.ship.position = (1, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (2, 1))

    def test_move_west_1(self):
        navigation_instruction = data_transformation("W1")
        self.ship.position = (0, 0)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (-1, 0))

    def test_move_west_2(self):
        navigation_instruction = data_transformation("W1")
        self.ship.position = (1, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.position, (0, 1))

    def test_move_rotate_left_90_1(self):
        navigation_instruction = data_transformation("L90")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (-1, 0))

    def test_move_rotate_left_90_2(self):
        navigation_instruction = data_transformation("L90")
        self.ship.position = (0, 0)
        self.ship.direction = (-1, 0)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (0, -1))

    def test_move_rotate_left_180(self):
        navigation_instruction = data_transformation("L180")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (0, -1))

    def test_move_rotate_left_270(self):
        navigation_instruction = data_transformation("L270")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (1, 0))

    def test_move_rotate_right_90(self):
        navigation_instruction = data_transformation("R90")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (1, 0))

    def test_move_rotate_right_180(self):
        navigation_instruction = data_transformation("R180")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (0, -1))

    def test_move_rotate_right_270(self):
        navigation_instruction = data_transformation("R270")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_ship(navigation_instruction)
        self.assertEqual(self.ship.direction, (-1, 0))

    def test_move_forward_1(self):
        navigation_instruction = data_transformation("F2")
        self.ship.position = (0, 0)
        self.ship.direction = (0, 1)
        self.ship.move_forward(
            navigation_instruction.value, self.ship.direction)
        self.assertEqual(self.ship.position, (0, 2))

    def test_move_forward_2(self):
        navigation_instruction = data_transformation("F2")
        self.ship.position = (0, 0)
        self.ship.direction = (1, 0)
        self.ship.move_forward(
            navigation_instruction.value, self.ship.direction)
        self.assertEqual(self.ship.position, (2, 0))

    def test_move_forward_3(self):
        navigation_instruction = data_transformation("F2")
        self.ship.position = (0, 0)
        self.ship.direction = (0, -1)
        self.ship.move_forward(
            navigation_instruction.value, self.ship.direction)
        self.assertEqual(self.ship.position, (0, -2))

    def test_move_forward_4(self):
        navigation_instruction = data_transformation("F2")
        self.ship.position = (0, 0)
        self.ship.direction = (-1, 0)
        self.ship.move_forward(
            navigation_instruction.value, self.ship.direction)
        self.assertEqual(self.ship.position, (-2, 0))

    def test_part_1(self):
        """()"""
        result = part_1(self.navigation_instructions)
        self.assertEqual(result, 25)

    def test_part_2(self):
        """()"""
        result = part_2(self.navigation_instructions)
        self.assertEqual(result, 286)


if __name__ == "__main__":
    unittest.main()
