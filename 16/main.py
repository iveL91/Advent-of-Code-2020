"""
    aoc_16
    https://adventofcode.com/2020/day/16
    Time: ca. (53 + 64)min
"""

import re
from functools import reduce
from operator import mul
from typing import Sequence


def data_input(filename: str = "data") -> dict[str, list]:
    with open(filename) as file:
        return data_transformation(file.read())


def data_transformation(string: str) -> dict[str, list]:
    lst = [split.split("\n") for split in string.split("\n\n")]
    dct = {}

    property_dict = {}
    pattern = re.compile(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)")
    for property in lst[0]:
        matches = re.search(pattern, property)
        property_dict[matches.group(1)] = [(int(matches.group(2)), int(matches.group(3))),
                                           (int(matches.group(4)), int(matches.group(5)))]

    dct["properties"] = property_dict
    dct[lst[1][0][:-1]] = [int(number) for number in lst[1][1].split(",")]
    dct[lst[2][0][:-1]] = [[int(number) for number in ticket.split(",")]
                           for ticket in lst[2][1:]]
    return dct


def in_range(number: int, lower: int, upper: int) -> bool:
    return lower <= number <= upper


def valid_number(number: int, property_ranges: Sequence[tuple[int, int]]) -> bool:
    for valid_ranges in property_ranges:
        for valid_range in valid_ranges:
            if in_range(number, *valid_range):
                return True
    return False


def ticket_scanning_error_rate(nearby_tickets: list[list[int]], property_dict: dict[str, list[tuple[int, int]]]) -> int:
    return sum(number for ticket in nearby_tickets for number in ticket if not valid_number(number, property_dict.values()))


def part_1(data: dict[str, list]) -> int:
    return ticket_scanning_error_rate(data["nearby tickets"], data["properties"])


def valid_ticket(ticket: Sequence[int], property_ranges: Sequence[tuple[int, int]]) -> bool:
    for number in ticket:
        if not valid_number(number, property_ranges):
            return False
    return True


def valid_property(property_ranges: Sequence[tuple[int, int]], values: Sequence[int]) -> bool:
    for value in values:
        for property_range in property_ranges:
            if in_range(value, *property_range):
                break
        else:
            return False
    return True


def possible_properties(value_list: list[int], property_dict: dict[str, list[tuple[int, int]]]) -> list[str]:
    return [property for property, property_ranges in property_dict.items() if valid_property(property_ranges, value_list)]


def determine_unique_property(column_dict: dict[int, list[str]]) -> dict[str, int]:
    properties_taken = set()
    amount_columns = len(column_dict)
    while len(properties_taken) < amount_columns:
        for column_index, properties in column_dict.items():
            if len(properties) == 1:
                properties_taken.add(properties[0])
            else:
                for property_taken in properties_taken:
                    if property_taken in properties:
                        properties.remove(property_taken)
                column_dict[column_index] = properties
    return {prop[0]: index for index, prop in column_dict.items()}


def prod(numbers: Sequence[int]) -> int:
    return reduce(mul, numbers, 1)


def part_2(data: dict[str, list]) -> int:
    valid_tickets = [ticket for ticket in data["nearby tickets"]
                     if valid_ticket(ticket, data["properties"].values())]

    amount_propoerties = len(data["your ticket"])
    # column_dict = {column_index: possible_properties(
    #     [ticket[column_index] for ticket in valid_tickets], data["properties"]) for column_index in range(amount_propoerties)}
    column_dict = {}
    for column_index in range(amount_propoerties):
        column = [ticket[column_index] for ticket in valid_tickets]
        column_dict[column_index] = possible_properties(
            column, data["properties"])

    prop_index_dict = determine_unique_property(column_dict)
    return prod(data["your ticket"][value] for key, value in prop_index_dict.items() if key.startswith("departure"))


def main() -> None:
    data = data_input("data")

    p1 = part_1(data)
    print(f"Part 1: {p1} is {p1 == 20060}")

    p2 = part_2(data)
    print(f"Part 2: {p2} is {p2 == 2843534243843}")


if __name__ == "__main__":
    main()

    # import timeit
    # data = data_input("data")
    # print(timeit.timeit("part_1(data)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(data)", globals=globals(), number=1_000))
