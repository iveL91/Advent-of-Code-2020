"""
    aoc_13
    https://adventofcode.com/2020/day/13
    Time: ca. (15 + 55)min
"""

from math import lcm
from typing import NamedTuple


class Bus(NamedTuple):
    id: int
    offset: int


def data_input(filename: str = "data") -> tuple[int, list[Bus]]:
    with open(filename) as file:
        return data_transformation(file.read())


def data_transformation(string: str) -> tuple[int, list[Bus]]:
    lines: list[str] = string.splitlines()
    return int(lines[0]), string_to_buses(lines[1])


def string_to_buses(string: str) -> list[Bus]:
    return [Bus(int(number), time) for time, number in enumerate(string.split(",")) if number != "x"]


def part_1(data: tuple[int, list[Bus]]) -> int:
    min_wait: int = data[1][0].id
    min_id: int = 0
    for number in data[1]:
        if (diff := number[0] * (data[0] // number[0] + 1) - data[0]) < min_wait:
            min_wait = diff
            min_id = number[0]
    return min_wait * min_id


def part_2(buses: list[Bus]) -> int:
    step: int = 1
    new_index: int = 0
    x: int = 0
    while True:
        for index, bus in enumerate(buses[new_index:], new_index):
            if ((x+bus.offset) / bus.id).is_integer():
                step = lcm(step, bus.id)
                new_index = index
            else:
                break
        else:
            break
        x += step
    return x


def main() -> None:
    data = data_input("data")

    p1 = part_1(data)
    print(f"Part 1: {p1} is {p1 == 2845}")

    p2 = part_2(data[1])
    print(f"Part 2: {p2} is {p2 == 487905974205117}")


if __name__ == "__main__":
    main()

    # import timeit
    # data = data_input("data")
    # print(timeit.timeit("part_1(data)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(data[1])", globals=globals(), number=10_000))
