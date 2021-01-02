"""
    aoc_07
    https://adventofcode.com/2020/day/7
    Time: ca. (136 + 41)min
"""

import re


def data_input(filename: str = "data") -> dict[str, list[tuple[str, int]]]:
    with open(filename) as file:
        result: dict[str, list[tuple[str, int]]] = {}
        for line in file.read().splitlines():
            result |= line_to_dict(line)
        return result


def line_to_dict(line: str) -> dict[str, list[tuple[str, int]]]:
    pattern_bag = re.compile(r"(\w+ \w+) bags contain")
    if b := re.search(pattern_bag, line):
        bag = b.group(1)
    else:
        bag = ""

    pattern_inside_bag = re.compile(r"(\d+) (\w+ \w+) bag")
    inside_bags = re.findall(pattern_inside_bag, line)
    return {bag: [(inside_bag[1], int(inside_bag[0])) for inside_bag in inside_bags]} if inside_bags else {bag: [("", 0)]}


class Bag:
    bag_rules: dict[str, list[tuple[str, int]]] = {}

    def __init__(self, name) -> None:
        self.name = name
        self.containing: set[str] = set()
        self.not_containing: set[str] = set()
        self.amount: int = 0

    def contains_one(self, possible_bag) -> None:
        if possible_bag not in self.containing and possible_bag not in self.not_containing:
            for inside_bag in self.bag_rules[possible_bag]:
                if not inside_bag[0]:
                    self.not_containing.add(possible_bag)
                    break
                if inside_bag[0] == self.name or inside_bag[0] in self.containing:
                    self.containing.add(possible_bag)
                    break

                self.contains_one(inside_bag[0])
                if inside_bag[0] in self.containing:
                    self.containing.add(possible_bag)
                    break
            else:
                self.not_containing.add(possible_bag)

    def contains(self) -> None:
        for bag in self.bag_rules:
            self.contains_one(bag)

    def amount_containing(self, start_name: str, start_value: int = 1) -> None:
        if start_name:
            for inside_bag in self.bag_rules[start_name]:
                if inside_bag[1]:
                    self.amount += start_value * inside_bag[1]
                    self.amount_containing(
                        inside_bag[0], start_value * inside_bag[1])


def part_1(bag: str = "shiny gold") -> int:
    my_bag = Bag(bag)
    my_bag.contains()
    return len(my_bag.containing)


def part_2(bag: str = "shiny gold") -> int:
    my_bag = Bag(bag)
    my_bag.amount_containing(my_bag.name)
    return my_bag.amount


def main() -> None:
    Bag.bag_rules = data_input("data")

    p1 = part_1()
    print(f"Part 1: {p1} is {p1 == 179}")

    p2 = part_2()
    print(f"Part 2: {p2} is {p2 == 18925}")


if __name__ == "__main__":
    main()

    # import timeit
    # Bag.bag_rules = data_input("data")
    # print(timeit.timeit("part_1()", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2()", globals=globals(), number=10_000))
