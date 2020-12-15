"""
    aoc_14
    https://adventofcode.com/2020/day/14
    Time: ca. (38 + 46)min
"""

from typing import Callable, NewType, Union


def data_input(filename: str = "data") -> list[list[str]]:
    with open(filename) as file:
        return [line.split(" = ") for line in file.read().splitlines()]


# u_int_b36 = NewType('u_int_b36', str)

# class uint_b36(str):
#     def to_int(self) -> int:
#         return int(self, 2)
            

# class BitmaskSystem:
#     def __init__(self) -> None:
#         self.mask: uint_b36 = uint_b36("")
#         self.mem: dict[uint_b36, uint_b36] = {}

#     def update(self, instruction) -> None:
#         if instruction[0] == "mask":
#             self.mask = instruction[1]
#         else:
#             pass
            



def bin_36_to_int(bin_36_string: str) -> int:
    return int(bin_36_string, 2)


def int_to_bin_36(integer: int) -> str:
    return "0" * (36 - len(bin(integer)[2:])) + bin(integer)[2:]


def mask_value_overlap(mask: str, value: int) -> str:
    value_36 = int_to_bin_36(value)
    result = ""
    for digit_mask, digit_value in zip(mask, value_36):
        if digit_mask == "X":
            result += digit_value
        else:
            result += digit_mask
    return result


def determine_positions(mask: str, position_instruction: str, version: int) -> list[int]:
    if version == 1:
        return [int_to_bin_36(int(position_instruction[4:-1]))]

    floating_position = memory_address_decoder(
        mask, int(position_instruction[4:-1]))
    return [bin_36_to_int(position_str)
            for position_str in floating_address_to_addresses(floating_position)]


def new(mask: str, position_instruction: str) -> list[int]:
    floating_position = memory_address_decoder(
        mask, int(position_instruction[4:-1]))
    return [bin_36_to_int(position_str)
            for position_str in floating_address_to_addresses(floating_position)]


def determine_mem(data: list[list[str]], version: int = 1) -> dict[int, str]:
    mem: dict[int, str] = {}
    mask = ""
    for lst in data:
        if lst[0] == "mask":
            mask = lst[1]
            continue

        position_instruction, value_str = lst
        value = int(value_str)
        positions = determine_positions(mask, position_instruction, version)

        for position in positions:
            mem[position] = mask_value_overlap(mask, value)
    return mem


def memory_address_decoder(mask: str, value: int) -> str:
    value_36 = int_to_bin_36(value)
    result = ""
    for digit_mask, digit_value in zip(mask, value_36):
        if digit_mask == "0":
            result += digit_value
        else:
            result += digit_mask
    return result


def replace_char_in_str(string: str, position: int, value: Union[str, int]) -> str:
    return string[:position] + str(value) + string[position+1:]


def floating_address_to_addresses(floating_address: str) -> list[str]:
    lst = [floating_address]
    for position, char in enumerate(floating_address):
        if char == "X":
            lst = [replace_char_in_str(string, position, value)
                   for string in lst for value in [0, 1]]
    return lst


def determine_new_mem(data: list[list[str]]) -> dict[int, str]:
    # return determine_mem(data, 2)
    mem: dict[int, str] = {}
    mask: str = ""
    for lst in data:
        if lst[0] == "mask":
            mask = lst[1]
            continue

        position_instruction, value_str = lst
        value = int(value_str)
        positions = determine_positions(mask, position_instruction, 2)

        for position_str in positions:
            mem[position_str] = int_to_bin_36(value)
    return mem


def constructor(data: list[list[str]], det_mem: Callable[[list[list[str]]], dict[int, str]]) -> int:
    mem = det_mem(data)
    return sum(bin_36_to_int(value) for value in mem.values())


def part_1(data: list[list[str]]) -> int:
    return constructor(data, determine_mem)


def part_2(data: list[list[str]]) -> int:
    return constructor(data, determine_new_mem)


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
