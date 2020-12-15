"""
    aoc_14
    https://adventofcode.com/2020/day/14
    Time: ca. (38 + 46)min
"""

from __future__ import annotations


def data_input(filename: str = "data") -> list[list[str]]:
    with open(filename) as file:
        return [line.split(" = ") for line in file.read().splitlines()]


class uint_b36(str):
    overwrite_instructions: dict[str, bool]

    def __int__(self) -> int:
        return int(self, 2)

    def __new__(cls, bin_string: str):
        if len(bin_string) > 36:
            raise ValueError
        string = "0" * (36 - len(bin_string)) + bin_string
        return super(uint_b36, cls).__new__(cls, string)

    def __add__(self, other: uint_b36) -> uint_b36:  # overlap
        new_string = ""
        for mask_digit, string_value in zip(self, other):
            new_string += mask_digit if self.overwrite_instructions[mask_digit] else string_value
        return uint_b36(new_string)


def int_to_uint_b36(integer: int) -> uint_b36:
    return uint_b36(bin(integer)[2:])


def floating_address_to_addresses(floating_address: uint_b36) -> list[uint_b36]:
    lst: list[str] = [floating_address]
    for char in floating_address:
        if char == "X":
            lst = [string.replace(char, str(value), 1)
                   for string in lst for value in [0, 1]]
    return [uint_b36(string) for string in lst]


def determine_positions(mask: uint_b36, position_instruction: str, version: int) -> list[uint_b36]:
    if version == 1:
        return [int_to_uint_b36(int(position_instruction[4:-1]))]

    floating_position = mask + int_to_uint_b36(int(position_instruction[4:-1]))
    return floating_address_to_addresses(floating_position)


def determine_mem(data: list[list[str]], version: int = 1) -> dict[uint_b36, uint_b36]:
    mem: dict[uint_b36, uint_b36] = {}
    mask = uint_b36("")
    for lst in data:
        if lst[0] == "mask":
            mask = uint_b36(lst[1])
            continue

        position_instruction, value_str = lst
        value = uint_b36(bin(int(value_str))[2:])
        positions = determine_positions(mask, position_instruction, version)

        for position in positions:
            mem[position] = mask + value if version == 1 else value
    return mem


def constructor(data: list[list[str]], version: int) -> int:
    mem = determine_mem(data, version)
    return sum(int(value) for value in mem.values())


def part_1(data: list[list[str]]) -> int:
    uint_b36.overwrite_instructions = {"0": True,
                                       "1": True,
                                       "X": False}
    return constructor(data, 1)


def part_2(data: list[list[str]]) -> int:
    uint_b36.overwrite_instructions = {"0": False,
                                       "1": True,
                                       "X": True}
    return constructor(data, 2)


def main() -> None:
    data = data_input("data")

    p1 = part_1(data)
    print(f"Part 1: {p1} is {p1 == 12610010960049}")

    p2 = part_2(data)
    print(f"Part 2: {p2} is {p2 == 3608464522781}")


if __name__ == "__main__":
    main()

    # import timeit
    # data = data_input("data")
    # print(timeit.timeit("part_1(data)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(data)", globals=globals(), number=100))
