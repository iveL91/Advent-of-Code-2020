"""
    aoc_05
    https://adventofcode.com/2020/day/5
    Time: ca. (21 + 8)min
"""


def data_input(filename: str = "data") -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def find_x(seat: str, row: bool) -> int:
    if row:
        identifiers = seat[:-3]
        letter_identifier = "B"
        rng = 128
    else:
        identifiers = seat[-3:]
        letter_identifier = "R"
        rng = 8

    result: int = 0
    for index, letter in enumerate(identifiers):
        if letter == letter_identifier:
            result += rng // (2 ** (index + 1))
    return result


def find_row(seat: str) -> int:
    return find_x(seat, row=True)


def find_column(seat: str) -> int:
    return find_x(seat, row=False)


def seat_id(seat: str) -> int:
    return 8 * find_row(seat) + find_column(seat)


def part_1(seats: list[str]) -> int:
    return max(seat_id(seat) for seat in seats)


def check_missing_seat_id(seats: list[str]) -> int:
    seat_ids = [seat_id(seat) for seat in seats]
    for number in range(8*(0+1), 8*(128-1)):  # No first and last row
        if number not in seat_ids:
            return number
    raise ValueError


def part_2(seats: list[str]) -> int:
    return check_missing_seat_id(seats)


def main() -> None:
    seats = data_input("data")

    p1 = part_1(seats)
    print(f"Part 1: {p1} is {p1 == 976}")

    p2 = part_2(seats)
    print(f"Part 2: {p2} is {p2 == 685}")


if __name__ == "__main__":
    main()

    # import timeit
    # SEATS = data_input("data")
    # print(timeit.timeit("part_1(SEATS)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(SEATS)", globals=globals(), number=10_000))
