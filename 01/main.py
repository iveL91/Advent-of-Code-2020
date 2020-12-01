"""
    aoc_01
    https://adventofcode.com/2020/day/1
"""

import itertools
from functools import reduce
from operator import mul
from typing import Sequence, Tuple


def data_input(filename: str = "data") -> str:
    with open(filename) as file:
        return file.read()


def data_transformation(data: str) -> list[int]:
    return [int(line) for line in data.split()]


def find_numbers_sum_equal_year(data: list[int], n: int, year: int = 2020) -> Tuple[int, ...]:
    for numbers in itertools.combinations(data, n):
        if sum(numbers) == year:
            return numbers
    else:
        raise ValueError


def prod(numbers: Sequence[int]) -> int:
    return reduce(mul, numbers, 1)


def constructor(data: list[int], n: int) -> int:
    return prod(find_numbers_sum_equal_year(data, n))


def part_1(data: list[int]) -> int:
    return constructor(data, 2)


def part_2(data: list[int]) -> int:
    return constructor(data, 3)


def main() -> None:
    data = data_transformation(data_input())

    p1 = part_1(data)
    print(f"Part 1: {p1} is {p1 == 388075}")

    p2 = part_2(data)
    print(f"Part 2: {p2} is {p2 == 293450526}")


if __name__ == "__main__":
    main()

    # import timeit
    # data = data_transformation(data_input())
    # print(timeit.timeit("part_1(data)", globals=globals(), number=1000))
    # print(timeit.timeit("part_2(data)", globals=globals(), number=1000))
