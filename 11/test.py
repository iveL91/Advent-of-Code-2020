"""test_aoc_11"""

import unittest
from main import data_input, data_transformation, Seats, Rules, part_1, part_2


class TestAoC11(unittest.TestCase):
    """()"""

    @classmethod
    def setUpClass(cls):
        cls.seat_layout = data_input("test_data")
        cls.seats_1 = Seats(cls.seat_layout, Rules(True, 4))
        cls.seats_2 = Seats(cls.seat_layout, Rules(False, 5))

    def test_occupied_seats_around_adjacent(self):
        seats = self.seats_1.round()
        result = seats.occupied_seats_around((1, 0))
        self.assertEqual(result, 3)

    def test_round_1_1(self):
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

    def test_round_1_2(self):
        new_seats = self.seats_1
        for _ in range(2):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##""")
        self.assertEqual(result, expected_result)

    def test_round_1_3(self):
        new_seats = self.seats_1
        for _ in range(3):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
""")
        self.assertEqual(result, expected_result)

    def test_round_1_4(self):
        new_seats = self.seats_1
        for _ in range(4):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
""")
        self.assertEqual(result, expected_result)

    def test_round_1_5(self):
        new_seats = self.seats_1
        for _ in range(5):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
""")
        self.assertEqual(result, expected_result)

    def test_part_1(self):
        """()"""
        result = part_1(self.seat_layout)
        self.assertEqual(result, 37)

    def test_occupied_seats_around_1(self):
        seat_layout = data_transformation(""".......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
""")
        seats = Seats(seat_layout, Rules(False, 5))
        result = seats.occupied_seats_around((4, 3))
        self.assertEqual(result, 8)

    def test_occupied_seats_around_2(self):
        seat_layout = data_transformation(""".............
.L.L.#.#.#.#.
.............
""")
        seats = Seats(seat_layout, Rules(False, 5))
        result = seats.occupied_seats_around((1, 1))
        self.assertEqual(result, 0)

    def test_occupied_seats_around_3(self):
        seat_layout = data_transformation(""".##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
""")
        seats = Seats(seat_layout, Rules(False, 5))
        result = seats.occupied_seats_around((3, 3))
        self.assertEqual(result, 0)

    def test_round_2_1(self):
        result = self.seats_2.round().seat_layout
        expected_result = data_transformation("""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""")
        self.assertEqual(result, expected_result)

    def test_round_2_2(self):
        new_seats = self.seats_2
        for _ in range(2):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
""")
        self.assertEqual(result, expected_result)

    def test_round_2_3(self):
        new_seats = self.seats_2
        for _ in range(3):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
""")
        self.assertEqual(result, expected_result)

    def test_round_2_4(self):
        new_seats = self.seats_2
        for _ in range(4):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
""")
        self.assertEqual(result, expected_result)

    def test_round_2_5(self):
        new_seats = self.seats_2
        for _ in range(5):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
""")
        self.assertEqual(result, expected_result)

    def test_round_2_6(self):
        new_seats = self.seats_2
        for _ in range(6):
            new_seats = new_seats.round()
        result = new_seats.seat_layout
        expected_result = data_transformation("""#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
""")
        self.assertEqual(result, expected_result)

    def test_part_2(self):
        """()"""
        result = part_2(self.seat_layout)
        self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest.main()
