"""test_aoc_11"""

import unittest
from main import data_input, data_transformation, Seats, Rules, part_1, part_2


class TestAoC11(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.data = data_input("test_data")
        cls.seats_1 = Seats(cls.data, Rules(True, 4))
        cls.seats_2 = Seats(cls.data, Rules(False, 5))

    def test_part_1(self):
        """()"""
        result = part_1(self.data)
        self.assertEqual(result, 37)

    def test_round_1(self):
        result = self.seats_1.round().seat_layout
        expected_result = data_transformation("""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##""")
        self.assertEqual(result, expected_result)

    def test_occupied_seats_around(self):
        seats = self.seats_1.round()
        result = seats.occupied_seats_around((1, 0))
        self.assertEqual(result, 3)
    
#     def test_new_round_2(self):
#         result = new_round(new_round(self.data))
#         expected_result = data_transformation("""#.LL.LL.L#
# #LLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLLL.L
# #.LLLLL.L#""")
#         self.assertEqual(result, expected_result)

    # def test_part_2(self):
    #     """()"""
    #     result = part_2(self.data)
    #     self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest.main()
