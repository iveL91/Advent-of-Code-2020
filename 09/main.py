"""
    aoc_09
    https://adventofcode.com/2020/day/9
    Time: ca. (30 + 13)min
"""


def data_input(filename: str = "data") -> list[int]:
    with open(filename) as file:
        return [int(number) for number in file.read().splitlines()]


def check_sum_of_pair(lst: list[int], number: int) -> bool:
    for index_1, num_1 in enumerate(lst):
        rest_lst = lst[:index_1] + lst[index_1+1:]
        for num_2 in rest_lst:
            if num_1 + num_2 == number:
                return True
    return False


def constructor(xmas_outputs: list[int], n: int = 25) -> int:
    preamble = xmas_outputs[:n]
    for number in xmas_outputs[n:]:
        if check_sum_of_pair(preamble, number):
            preamble = preamble[1:] + [number]
        else:
            return number
    raise ValueError


def part_1(xmas_outputs: list[int]) -> int:
    return constructor(xmas_outputs)


def encryption_weakness_min_max(xmas_outputs: list[int], invalid_number: int) -> tuple[int, int]:
    for start_position, _ in enumerate(xmas_outputs):
        end_position: int = start_position + 1
        sm: int = 0
        while sm < invalid_number:
            sm += xmas_outputs[end_position]
            end_position += 1
            if sm == invalid_number:
                return min(xmas_outputs[start_position:end_position]), max(xmas_outputs[start_position:end_position])
    raise ValueError


def encryption_weakness(xmas_outputs: list[int], invalid_number: int) -> int:
    return sum(encryption_weakness_min_max(xmas_outputs, invalid_number))


def part_2(xmas_outputs: list[int], invalid_number: int) -> int:
    return encryption_weakness(xmas_outputs, invalid_number)


def main() -> None:
    xmas_outputs = data_input("data")

    p1 = part_1(xmas_outputs)
    print(f"Part 1: {p1} is {p1 == 18272118}")

    p2 = part_2(xmas_outputs, p1)
    print(f"Part 2: {p2} is {p2 == 2186361}")


if __name__ == "__main__":
    main()

    # import timeit
    # xmas_outputs = data_input("data")
    # p1 = part_1(xmas_outputs)
    # print(timeit.timeit("part_1(xmas_outputs)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(xmas_outputs, p1)", globals=globals(), number=1_000))
