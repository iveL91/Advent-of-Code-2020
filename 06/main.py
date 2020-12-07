"""
    aoc_06
    https://adventofcode.com/2020/day/6
    Time: ca. (23 + 3)min
"""

from string import ascii_lowercase


def data_input(filename: str = "data") -> list[list[str]]:
    with open(filename) as file:
        return [group_string_to_list(answers) for answers in file.read().split("\n\n")]


def group_string_to_list(group_string: str) -> list[str]:
    return group_string.split("\n")


def different_letters_in_group(group_answers: str) -> int:
    return len(set().union(*[set(answer) for answer in group_answers]))


def same_letters_in_group(group_answers: str) -> int:
    return len(set(ascii_lowercase).intersection(*[set(answer) for answer in group_answers]))


def part_1(answers):
    return sum(different_letters_in_group(group_answers) for group_answers in answers)


def part_2(answers):
    return sum(same_letters_in_group(group_answers) for group_answers in answers)


def main() -> None:
    answers = data_input("data")

    p1 = part_1(answers)
    print(f"Part 1: {p1} is {p1 == 6587}")

    p2 = part_2(answers)
    print(f"Part 2: {p2} is {p2 == 3235}")


if __name__ == "__main__":
    main()

    # import timeit
    # seats = data_input("data")
    # print(timeit.timeit("part_1(seats)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(seats)", globals=globals(), number=10_000))
