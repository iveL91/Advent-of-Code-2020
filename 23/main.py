"""
    aoc_23
    https://adventofcode.com/2020/day/23
    Time: ca. (48 + /)min
"""


class CupGame:
    def __init__(self, cups: list[int], length: int) -> None:
        cups = cups + list(range(10, length+1))
        self.cups_dict = dict(zip(cups, cups[1:]+[cups[0]]))
        self.current_cup = cups[0]

    def determine_destination_cup(self, not_available_cups: list[int]) -> int:
        destination_cup = self.current_cup
        while destination_cup in not_available_cups:
            destination_cup -= 1
            if not destination_cup:
                destination_cup = len(self.cups_dict)
        return destination_cup

    def move(self) -> None:
        first_pick_up = self.cups_dict[self.current_cup]
        second_pick_up = self.cups_dict[first_pick_up]
        last_pick_up = self.cups_dict[second_pick_up]
        after_pick_ups = self.cups_dict[last_pick_up]
        destination_cup = self.determine_destination_cup(
            [self.current_cup, first_pick_up, second_pick_up, last_pick_up])
        after_destination_cup = self.cups_dict[destination_cup]

        self.cups_dict[destination_cup] = first_pick_up
        self.cups_dict[last_pick_up] = after_destination_cup
        self.cups_dict[self.current_cup] = after_pick_ups
        self.current_cup = after_pick_ups

    def run(self, moves: int) -> None:
        for _ in range(moves):
            self.move()

    def labels_after_1(self) -> int:
        after = self.cups_dict[1]
        labels = str(after)
        for _ in range(7):
            after = self.cups_dict[after]
            labels += str(after)
        return int(labels)

    def two_cups_after_1(self) -> tuple[int, int]:
        return self.cups_dict[1], self.cups_dict[self.cups_dict[1]]


def data_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(number) for number in file.read()]


def constructor(cups: list[int], runs: int, length: int = 9) -> CupGame:
    cup_game = CupGame(cups, length)
    cup_game.run(runs)
    return cup_game


def part_1(cups: list[int], runs: int = 100) -> int:
    cup_game = constructor(cups, runs)
    return cup_game.labels_after_1()


def part_2(cups: list[int]) -> int:
    length: int = 1_000_000
    runs: int = 10_000_000
    cup_game = constructor(cups, runs, length)
    cup_1, cup_2 = cup_game.two_cups_after_1()
    return cup_1 * cup_2


def main() -> None:
    cups = data_input("data")

    p1 = part_1(cups)
    print(f"Part 1: {p1} is {p1 == 97632548}")

    p2 = part_2(cups)
    print(f"Part 2: {p2} is {p2 == 412990492266}")


if __name__ == "__main__":
    main()

    # import timeit
    # CUPS = data_input("data")
    # print(timeit.timeit("part_1(CUPS)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(CUPS)", globals=globals(), number=1))
