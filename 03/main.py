"""
    aoc_03
    https://adventofcode.com/2020/day/3
    Time: ca. (21 + 13)min
"""

from __future__ import annotations
from functools import reduce
from operator import mul
from typing import NamedTuple, Sequence


class Vector2D(NamedTuple):
    down: int
    right: int


class Spaceship:
    space_grid: list[list[bool]]

    def __init__(self, position: tuple[int, int] = (0, 0), movement: tuple[int, int] = (1, 3)) -> None:
        self.position = Vector2D(*position)
        self.movement = Vector2D(*movement)
        self.tree_encounters: int = 0

    def __call__(self) -> None:
        self.tree_encounters += self.space_grid[self.position.down][self.position.right]
        self.position = Vector2D(self.position.down+self.movement.down,
                                 (self.position.right+self.movement.right) % len(self.space_grid[0]))

    def fly(self) -> Spaceship:
        while self.position.down < len(self.space_grid):
            self()
        return self


def data_input(filename: str = "data") -> list[list[bool]]:
    with open(filename) as file:
        return [[point == "#" for point in line] for line in file.read().splitlines()]


def prod(numbers: Sequence[int]) -> int:
    return reduce(mul, numbers, 1)


def constructor(movements: list[tuple[int, int]]) -> int:
    return prod([Spaceship(movement=movement).fly().tree_encounters for movement in movements])


def part_1() -> int:
    return constructor([(1, 3)])


def part_2() -> int:
    return constructor([(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])


def main() -> None:
    Spaceship.space_grid = data_input("data")

    p1 = part_1()
    print(f"Part 1: {p1} is {p1 == 294}")

    p2 = part_2()
    print(f"Part 2: {p2} is {p2 == 5774564250}")


if __name__ == "__main__":
    main()

    # import timeit
    # Spaceship.space_grid = data_input("data")
    # print(timeit.timeit("part_1()", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2()", globals=globals(), number=10_000))
