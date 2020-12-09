"""
    aoc_11
    https://adventofcode.com/2020/day/11
    Time: ca. ( + )min
"""


def data_input(filename: str = "data") -> str:
    with open(filename) as file:
        return file.read()


def part_1():
    pass


def part_2():
    pass


def main() -> None:
    data = data_input("test_data")

    p1 = part_1()
    print(f"Part 1: {p1} is {p1 == 0}")

    p2 = part_2()
    print(f"Part 2: {p2} is {p2 == 0}")


if __name__ == "__main__":
    main()
