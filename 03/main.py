"""
    aoc_03
    https://adventofcode.com/2020/day/3
    Time: ca. (21 + 13)min
"""


from functools import reduce
from operator import mul
from typing import Sequence


class Spaceship:
    space_grid: list[list[int]]

    def __init__(self, position: tuple[int, int] = (0, 0), movement: tuple[int, int] = (1, 3)) -> None:
        self.position = position
        self.movement = movement

    def __call__(self) -> None:
        self.position = (self.position[0]+self.movement[0],
                         (self.position[1]+self.movement[1]) % (len(self.space_grid[0])-1))


def data_input(filename: str = "data") -> list[list[int]]:
    with open(filename) as file:
        return [[0 if point == "." else 1 for point in line] for line in file.readlines()]


def tree_encounters(spaceship: Spaceship) -> int:
    counter: int = 0
    while spaceship.position[0] < len(spaceship.space_grid):
        if spaceship.space_grid[spaceship.position[0]][spaceship.position[1]] == 1:
            counter += 1
        spaceship()
    return counter


def prod(numbers: Sequence[int]) -> int:
    return reduce(mul, numbers, 1)


def part_1() -> int:
    spaceship = Spaceship()
    return tree_encounters(spaceship)


def part_2():
    movements = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    counters: list[int] = []
    for movement in movements:
        spaceship = Spaceship(movement=movement)
        counters.append(tree_encounters(spaceship))
    return prod(counters)


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
