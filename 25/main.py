"""
    aoc_25
    https://adventofcode.com/2020/day/25
    Time: ca. (26 + /)min
"""


def data_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(number) for number in file.read().splitlines()]


def transforming_subject_number(subject_nubmer: int, loop_size: int) -> int:
    value = 1
    for _ in range(loop_size):
        value *= subject_nubmer
        value %= 20201227
    return value


def determine_loop_size(public_key: int) -> int:
    loop_size = 0
    value = 1
    subject_number = 7
    while value != public_key:
        loop_size += 1
        value *= subject_number
        value %= 20201227
    return loop_size


def part_1(public_keys: list[int]) -> int:
    loop_size_card = determine_loop_size(public_keys[0])
    return transforming_subject_number(public_keys[1], loop_size_card)
    # loop_size_door = determine_loop_size(public_keys[1])
    # return transforming_subject_number(public_keys[0], loop_size_door)


def main() -> None:
    public_keys = data_input("data")

    p1 = part_1(public_keys)
    print(f"Part 1: {p1} is {p1 == 18608573}")


if __name__ == "__main__":
    main()

    # import timeit
    # PUBLIC_KEYS = data_input("data")
    # print(timeit.timeit("part_1(PUBLIC_KEYS)", globals=globals(), number=100))
