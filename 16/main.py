"""
    aoc_16
    https://adventofcode.com/2020/day/16
    Time: ca. (53 + 64)min
"""

import re
from functools import reduce
from operator import mul
from typing import Iterable, NamedTuple


class Data(NamedTuple):
    properties: dict[str, list[tuple[int, int]]]
    your_ticket: list[int]
    nearby_tickets: list[list[int]]


def data_input(filename: str = "data") -> Data:
    with open(filename) as file:
        return data_transformation(file.read())


def data_transformation(string: str) -> Data:
    lst = [split.split("\n") for split in string.split("\n\n")]

    property_dict: dict[str, list[tuple[int, int]]] = {}
    pattern = re.compile(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)")
    for prop in lst[0]:
        if matches := re.search(pattern, prop):
            property_dict[matches.group(1)] = [(int(matches.group(2)), int(matches.group(3))),
                                               (int(matches.group(4)), int(matches.group(5)))]

    return Data(properties=property_dict,
                your_ticket=[int(number) for number in lst[1][1].split(",")],
                nearby_tickets=[[int(number) for number in ticket.split(",")] for ticket in lst[2][1:]])


def in_range(number: int, lower: int, upper: int) -> bool:
    return lower <= number <= upper


def valid_number(number: int, properties_ranges: Iterable[Iterable[tuple[int, int]]]) -> bool:
    for property_ranges in properties_ranges:
        for property_range in property_ranges:
            if in_range(number, *property_range):
                return True
    return False


def ticket_scanning_error_rate(nearby_tickets: Iterable[Iterable[int]], property_dict: dict[str, list[tuple[int, int]]]) -> int:
    return sum(number for ticket in nearby_tickets for number in ticket if not valid_number(number, property_dict.values()))


def part_1(data: Data) -> int:
    return ticket_scanning_error_rate(data.nearby_tickets, data.properties)


def valid_ticket(ticket: Iterable[int], properties_ranges: Iterable[Iterable[tuple[int, int]]]) -> bool:
    for number in ticket:
        if not valid_number(number, properties_ranges):
            return False
    return True


def valid_property(property_ranges: Iterable[tuple[int, int]], values: Iterable[int]) -> bool:
    for value in values:
        for property_range in property_ranges:
            if in_range(value, *property_range):
                break
        else:
            return False
    return True


def possible_properties(values: Iterable[int], property_dict: dict[str, list[tuple[int, int]]]) -> list[str]:
    return [prop for prop, property_ranges in property_dict.items() if valid_property(property_ranges, values)]


def determine_unique_property(column_dict: dict[int, list[str]]) -> dict[str, int]:
    properties_taken: set[str] = set()
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


def fields(data: Data) -> dict[str, int]:
    valid_tickets = [ticket for ticket in data.nearby_tickets
                     if valid_ticket(ticket, data.properties.values())]

    amount_propoerties = len(data.your_ticket)
    # column_dict = {column_index: possible_properties(
    #     [ticket[column_index] for ticket in valid_tickets], data["properties"]) for column_index in range(amount_propoerties)}
    column_dict = {}
    for column_index in range(amount_propoerties):
        column = [ticket[column_index] for ticket in valid_tickets]
        column_dict[column_index] = possible_properties(
            column, data.properties)

    return determine_unique_property(column_dict)

def prod(numbers: Iterable[int]) -> int:
    return reduce(mul, numbers, 1)


def part_2(data: Data) -> int:
    return prod(data.your_ticket[value] for key, value in fields(data).items() if key.startswith("departure"))


def main() -> None:
    data = data_input("data")

    p1 = part_1(data)
    print(f"Part 1: {p1} is {p1 == 20060}")

    p2 = part_2(data)
    print(f"Part 2: {p2} is {p2 == 2843534243843}")


if __name__ == "__main__":
    main()

    # import timeit
    # DATA = data_input("data")
    # print(timeit.timeit("part_1(DATA)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(DATA)", globals=globals(), number=1_000))
