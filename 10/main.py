"""
    aoc_10
    https://adventofcode.com/2020/day/10
    Time: ca. (21 + 16)min
"""

from typing import NamedTuple


class Adapter(NamedTuple):
    joltage_rating: int


def data_input(filename: str = "data") -> list[Adapter]:
    with open(filename) as file:
        adapters = sorted([Adapter(int(number))
                           for number in file.read().splitlines()])
        charging_outlet = Adapter(0)
        built_in_adapter = Adapter(adapters[-1].joltage_rating + 3)
        return [charging_outlet] + adapters + [built_in_adapter]


def n_jolt_differences(adapters: list[Adapter], n: int) -> int:
    n_jolt_differences: int = 0
    for adapter_1, adapter_2 in zip(adapters, adapters[1:]):
        joltage_rating_difference = adapter_2.joltage_rating - adapter_1.joltage_rating
        if joltage_rating_difference == n:
            n_jolt_differences += 1

    return n_jolt_differences


def part_1(adapters: list[Adapter]) -> int:
    return n_jolt_differences(adapters, 1) * n_jolt_differences(adapters, 3)


def part_2(adapters: list[Adapter]) -> int:
    arrangements_dct: dict[Adapter, int] = {adapters[-2]: 1}

    for adapter in adapters[:-2][::-1]:
        adapter_arrangements: int = 0
        for jolt_difference in range(1, 4):
            if (new_adapter := Adapter(adapter.joltage_rating + jolt_difference)) in adapters:
                adapter_arrangements += arrangements_dct[new_adapter]
        arrangements_dct[adapter] = adapter_arrangements

    return arrangements_dct[adapters[0]]


def main() -> None:
    adapters = data_input("data")

    p1 = part_1(adapters)
    print(f"Part 1: {p1} is {p1 == 1836}")

    p2 = part_2(adapters)
    print(f"Part 2: {p2} is {p2 == 43406276662336}")


if __name__ == "__main__":
    main()

    # import timeit
    # adapters = data_input("data")
    # print(timeit.timeit("part_1(adapters)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(adapters)", globals=globals(), number=10_000))
