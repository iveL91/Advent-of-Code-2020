"""
    aoc_11
    https://adventofcode.com/2020/day/11
    Time: ca. (51 + 49)min
"""

from __future__ import annotations
from typing import NamedTuple


def data_input(filename: str = "data") -> list[list[str]]:
    with open(filename) as file:
        return data_transformation(file.read())


def data_transformation(string: str) -> list[list[str]]:
    return [list(seat_row) for seat_row in string.splitlines()]


class Rules(NamedTuple):
    adjacent: bool
    max_occ_seats_around: int


class Seats:
    directions: list[tuple[int, int]] = [
        (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

    def __init__(self, seat_layout: list[list[str]], rules: Rules) -> None:
        self.seat_layout = seat_layout
        self.rules = rules

    @property
    def occupied_seats(self) -> int:
        return sum(symbol == "#" for row in self.seat_layout for symbol in row)

    def occupied_seats_around(self, position: tuple[int, int]) -> int:
        sm: int = 0
        for direction in self.directions:
            new_position = position
            while True:
                new_position = (
                    new_position[0] + direction[0], new_position[1] + direction[1])
                if 0 <= new_position[0] < len(self.seat_layout) and 0 <= new_position[1] < len(self.seat_layout[0]):
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
        new_seat_layout = [[] for _ in self.seat_layout]
        for row_index, seat_row in enumerate(self.seat_layout):
            for column_index, seat in enumerate(seat_row):
                if seat == "L" and not self.occupied_seats_around((row_index, column_index)):
                    new_seat_layout[row_index].append("#")
                elif seat == "#" and self.occupied_seats_around((row_index, column_index)) >= self.rules.max_occ_seats_around:
                    new_seat_layout[row_index].append("L")
                else:
                    new_seat_layout[row_index].append(
                        self.seat_layout[row_index][column_index])
        return Seats(new_seat_layout, self.rules)


def constructor(seats: Seats) -> int:
    while True:
        new_seats = seats.round()
        if new_seats.seat_layout == seats.seat_layout:
            break
        else:
            seats = new_seats
    return new_seats.occupied_seats


def part_1(seat_layout: list[str]) -> int:
    return constructor(Seats(seat_layout, Rules(True, 4)))


def part_2(seat_layout):
    return constructor(Seats(seat_layout, Rules(False, 5)))


def main() -> None:
    seat_layout = data_input("data")

    p1 = part_1(seat_layout)
    print(f"Part 1: {p1} is {p1 == 2483}")

    p2 = part_2(seat_layout)
    print(f"Part 2: {p2} is {p2 == 2285}")


if __name__ == "__main__":
    main()
