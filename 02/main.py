"""
    aoc_02
    https://adventofcode.com/2020/day/2
    Time: ca. 23min
"""

from typing import NamedTuple


class PasswordInstruction(NamedTuple):
    numbers: tuple[int, int]
    letter: str
    password: str


def data_input(filename: str = "data") -> list[PasswordInstruction]:
    with open(filename) as file:
        return [password_instruction_transformation(line) for line in file.readlines()]


def password_instruction_transformation(password_instruction: str) -> PasswordInstruction:
    password_instruction_list = password_instruction.split()
    numbers = tuple(int(number)
                    for number in password_instruction_list[0].split("-"))
    letter = password_instruction_list[1].strip(":")
    password = password_instruction_list[2]
    return PasswordInstruction(numbers, letter, password)


def valid_old_password(password_instruction: PasswordInstruction) -> bool:
    bounds, letter, password = password_instruction
    lower_bound, upper_bound = bounds
    counter = password.count(letter)
    return lower_bound <= counter and counter <= upper_bound


def valid_new_password(password_instruction: PasswordInstruction) -> bool:
    positions, letter, password = password_instruction
    first_position, second_position = positions
    return (password[first_position-1] == letter and password[second_position-1] != letter) or (password[first_position-1] != letter and password[second_position-1] == letter)


def part_1(password_instructions: list[PasswordInstruction]) -> int:
    return sum(valid_old_password(password_instruction) for password_instruction in password_instructions)


def part_2(password_instructions: list[PasswordInstruction]) -> int:
    return sum(valid_new_password(password_instruction) for password_instruction in password_instructions)


def main() -> None:
    password_instructions = data_input("data")

    p1 = part_1(password_instructions)
    print(f"Part 1: {p1} is {p1 == 460}")

    p2 = part_2(password_instructions)
    print(f"Part 2: {p2} is {p2 == 251}")


if __name__ == "__main__":
    main()

    # import timeit
    # data = data_input()
    # print(timeit.timeit("part_1(data)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(data)", globals=globals(), number=10_000))
