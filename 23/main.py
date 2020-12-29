"""
    aoc_23
    https://adventofcode.com/2020/day/23
    Time: ca. (48 + )min
"""

import collections


class CupGame:
    def __init__(self, cups: list[int], length: int) -> None:
        self.cups = collections.deque(cups + list(range(10, length)), length)

    @property
    def destination_cup(self) -> int:
        not_available_cups = [self.cups[i] for i in range(4)]
        result = self.cups[0]
        while result in not_available_cups:
            result -= 1
            if not result:
                result = len(self.cups)
        return result

    def move(self) -> None:
        destination_cup = self.destination_cup
        self.cups.rotate(-1)
        destination_cup_index = self.cups.index(destination_cup)
        for _ in range(3):
            self.cups.insert(destination_cup_index, self.cups.popleft())

    def run(self, moves: int = 100):
        for _ in range(moves):
            self.move()

    def labels_after_1(self) -> int:
        index_1 = self.cups.index(1)
        self.cups.rotate(-index_1)
        return int("".join(str(number) for number in list(self.cups)[1:]))


def data_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(number) for number in file.read()]


def part_1(cups: list[int], runs: int = 100) -> int:
    cup_game = CupGame(cups, 10)
    cup_game.run(runs)
    return cup_game.labels_after_1()


def part_2(cups: list[int]) -> int:
    pass


def main() -> None:
    cups = data_input("data")

    p1 = part_1(cups)
    print(f"Part 1: {p1} is {p1 == 97632548}")

    # p2 = part_2(cups)
    # print(f"Part 2: {p2} is {p2 == 0}")


if __name__ == "__main__":
    main()

    # import timeit
    # CUPS = data_input("data")
    # print(timeit.timeit("part_1(CUPS)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(CUPS)", globals=globals(), number=1))
