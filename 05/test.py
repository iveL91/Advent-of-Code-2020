"""test_aoc_05"""

import unittest
from main import data_input, find_row, find_column, seat_id, part_1, part_2


class TestAoC05(unittest.TestCase):
    """()"""

    def test_find_row_1(self):
        result = find_row("FBFBBFFRLR")
        self.assertEqual(result, 44)

    def test_find_row_2(self):
        result = find_row("BFFFBBFRRR")
        self.assertEqual(result, 70)

    def test_find_row_3(self):
        result = find_row("FFFBBBFRRR")
        self.assertEqual(result, 14)

    def test_find_row_4(self):
        result = find_row("BBFFBBFRLL")
        self.assertEqual(result, 102)

    def test_find_column_1(self):
        result = find_column("FBFBBFFRLR")
        self.assertEqual(result, 5)

    def test_find_column_2(self):
        result = find_column("BFFFBBFRRR")
        self.assertEqual(result, 7)

    def test_find_column_3(self):
        result = find_column("FFFBBBFRRR")
        self.assertEqual(result, 7)

    def test_find_column_4(self):
        result = find_column("BBFFBBFRLL")
        self.assertEqual(result, 4)

    def test_seat_id_1(self):
        """()"""
        result = seat_id("FBFBBFFRLR")
        self.assertEqual(result, 357)

    def test_seat_id_2(self):
        """()"""
        result = seat_id("BFFFBBFRRR")
        self.assertEqual(result, 567)

    def test_seat_id_3(self):
        """()"""
        result = seat_id("FFFBBBFRRR")
        self.assertEqual(result, 119)

    def test_seat_id_4(self):
        """()"""
        result = seat_id("BBFFBBFRLL")
        self.assertEqual(result, 820)

    def test_part_1(self):
        """()"""
        seats = data_input("data")
        result = part_1(seats)
        self.assertEqual(result, 976)

    def test_part_2(self):
        """()"""
        seats = data_input("data")
        result = part_2(seats)
        self.assertEqual(result, 685)


if __name__ == "__main__":
    unittest.main()
