"""
    aoc_11
    https://adventofcode.com/2020/day/11
    Time: ca. (51 + 49)min
"""

from __future__ import annotations
from typing import NamedTuple


def data_input(filename: str = "data") -> list[str]:
    with open(filename) as file:
        return data_transformation(file.read())


def data_transformation(string: str) -> list[str]:
    return string.splitlines()


class Rules(NamedTuple):
    adjacent: bool
    max_occ_seats_around: int


class Seats:
    directions: list[tuple[int, int]] = [
        (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

    def __init__(self, seat_layout: list[str], rules: Rules) -> None:
        self.seat_layout = seat_layout
        self.rules = rules

    @property
    def occupied_seats(self) -> int:
        return sum(symbol == "#" for row in self.seat_layout for symbol in row)

    def position_inside_layout(self, position: tuple[int, int]) -> bool:
        return 0 <= position[0] < len(self.seat_layout) and 0 <= position[1] < len(self.seat_layout[0])

    def occupied_seats_around(self, position: tuple[int, int]) -> int:
        sm: int = 0
        for direction in self.directions:
            new_position = position
            while True:
                new_position = (
                    new_position[0] + direction[0], new_position[1] + direction[1])
                if self.position_inside_layout(new_position):
                    if self.seat_layout[new_position[0]][new_position[1]] == "#":
                        sm += 1
                        break
                    if self.seat_layout[new_position[0]][new_position[1]] == "L":
                        break
                else:
                    break
                if self.rules.adjacent:
                    break
        return sm

    def round(self) -> Seats:
        new_seat_layout = ["" for _ in self.seat_layout]
        for row_index, seat_row in enumerate(self.seat_layout):
            for column_index, seat in enumerate(seat_row):
                if seat == "L" and not self.occupied_seats_around((row_index, column_index)):
                    new_seat_layout[row_index] += "#"
                elif seat == "#" and self.occupied_seats_around((row_index, column_index)) >= self.rules.max_occ_seats_around:
                    new_seat_layout[row_index] += "L"
                else:
                    new_seat_layout[row_index] += self.seat_layout[row_index][column_index]
        return Seats(new_seat_layout, self.rules)


def constructor(seats: Seats) -> int:
    while True:
        new_seats = seats.round()
        if new_seats.seat_layout == seats.seat_layout:
            break
        seats = new_seats
    return new_seats.occupied_seats


def part_1(seat_layout: list[str]) -> int:
    return constructor(Seats(seat_layout, Rules(adjacent=True, max_occ_seats_around=4)))


def part_2(seat_layout: list[str]) -> int:
    return constructor(Seats(seat_layout, Rules(adjacent=False, max_occ_seats_around=5)))


def main() -> None:
    seat_layout = data_input("data")

    p1 = part_1(seat_layout)
    print(f"Part 1: {p1} is {p1 == 2483}")

    p2 = part_2(seat_layout)
    print(f"Part 2: {p2} is {p2 == 2285}")


if __name__ == "__main__":
    main()

    # import timeit
    # SEAT_LAYOUT = data_input("data")
    # print(timeit.timeit("part_1(SEAT_LAYOUT)", globals=globals(), number=1))
    # print(timeit.timeit("part_2(SEAT_LAYOUT)", globals=globals(), number=1))
