"""test_aoc_08"""

import unittest
from main import data_input, constructor, part_1, part_2


class TestAoC08(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 5)

    def test_constructor_infinite_loop(self):
        instructions = self.data.copy()
        instructions[0] = "jmp +0".split()
        handheld_game_console = constructor(instructions)
        self.assertTrue(handheld_game_console.breaker)

    def test_constructor_finite_loop(self):
        instructions = self.data.copy()
        instructions[-2] = "nop -4".split()
        handheld_game_console = constructor(instructions)
        self.assertFalse(handheld_game_console.breaker)

    def test_part_2(self):
        """()"""
        result = part_2(self.data)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()
