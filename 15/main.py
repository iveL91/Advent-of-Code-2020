"""
    aoc_15
    https://adventofcode.com/2020/day/15
    Time: ca. (27 + 119)min
"""


def data_input(filename: str = "data") -> list[int]:
    with open(filename) as file:
        return [int(number) for number in file.read().split(",")]


def constructor(starting_numbers: list[int], turns: int) -> int:
    spoken_numbers_dict: dict[int, int] = {spoken_number: occurence for occurence,
                                           spoken_number in enumerate(starting_numbers, 1)}

    last_number: int = starting_numbers[-1]
    counter: int = len(spoken_numbers_dict)
    while counter < turns:
        if last_number in spoken_numbers_dict:
            spoken_numbers_dict[last_number], last_number = counter, counter - \
                spoken_numbers_dict[last_number]
        else:
            spoken_numbers_dict[last_number], last_number = counter, 0
        counter += 1
    return last_number


def part_1(starting_numbers: list[int]) -> int:
    return constructor(starting_numbers, 2020)


def part_2(starting_numbers: list[int]) -> int:
    return constructor(starting_numbers, 30_000_000)


def main() -> None:
    starting_numbers = data_input("data")

    p1 = part_1(starting_numbers)
    print(f"Part 1: {p1} is {p1 == 1085}")

    p2 = part_2(starting_numbers)
    print(f"Part 2: {p2} is {p2 == 10652}")


if __name__ == "__main__":
    main()

    # import timeit
    # STARTING_NUMBERS = data_input("data")
    # print(timeit.timeit("part_1(STARTING_NUMBERS)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(STARTING_NUMBERS)", globals=globals(), number=1))
