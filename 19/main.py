"""
    aoc_19
    https://adventofcode.com/2020/day/19
    Time: ca. (125 + 123)min
"""

from typing import Union


def data_input(filename: str) -> list[str]:
    with open(filename) as file:
        return file.read().split("\n\n")


def concat_lst(lst: list[str]) -> str:
    result = ""
    for element in lst:
        result += element
    return result


def determine_new_rule(rule: list, transformed_rules) -> list:
    while True:
        new_rule = []
        for value_list in rule:
            new_rule += list_transform(value_list, transformed_rules)
        if new_rule == rule:
            return new_rule
        else:
            rule = new_rule


def list_transform(lst: list[str], transformed_rules) -> list[str]:
    new_list = []
    for index, element in enumerate(lst):
        if element in transformed_rules:
            for ele in transformed_rules[element]:
                new_list.append(lst[:index] + [ele] + lst[index+1:])
            return new_list
    return [lst]


def initialize_rules(rules_list):
    rules: dict[str, Union[list[tuple[str, str]], str]] = {}
    for rule in rules_list:
        rule_split = rule.split(": ")
        rules[rule_split[0]] = [values.split(
            " ") for values in rule_split[1].split(" | ")]

    transformed_rules = {}
    for key, value_list in rules.items():
        for values in value_list:
            for value in values:
                if value == '"a"':
                    transformed_rules[key] = ["a"]
                if value == '"b"':
                    transformed_rules[key] = ["b"]

    for key in transformed_rules:
        del rules[key]

    return rules, transformed_rules


def check_complete_transformation(rule: list[list[str]]) -> bool:
    for option in rule:
        for element in option:
            if not element.isalpha():
                return False
    return True


def determine_rules(rules_list):
    rules, transformed_rules = initialize_rules(rules_list)
    while len(rules):
        delete_keys = set()
        for key, rule in rules.items():
            rules[key] = determine_new_rule(rule, transformed_rules)
            if check_complete_transformation(rules[key]):
                new_list = []
                for lst in rules[key]:
                    new_list.append(concat_lst(lst))
                transformed_rules[key] = new_list
                delete_keys.add(key)

        for key in delete_keys:
            del rules[key]

    return transformed_rules


def valid_string(string: str, transformed_rules, version: int) -> bool:
    length_42 = len(transformed_rules["42"][0])
    length_31 = len(transformed_rules["42"][0])
    if not string.startswith(tuple(transformed_rules["42"])) or not (string[length_42:].startswith(tuple(transformed_rules["42"])) and string[length_42:].endswith(tuple(transformed_rules["31"]))):
        return False

    string = string[2*length_42:-length_31]

    if version == 1:
        return string == ""

    while len(string) > 0:
        if string.startswith(tuple(transformed_rules["42"])):
            string = string[length_42:]
        else:
            return False
        if string.endswith(tuple(transformed_rules["31"])):
            string = string[:-length_31]
    return True


def part_1_test(data):
    rules_list = data[0].splitlines()
    transformed_rules = determine_rules(rules_list)
    strings = data[1].splitlines()
    return sum(string in transformed_rules["0"] for string in strings)


def constructor(data, version: int) -> int:
    rules_list = data[0].splitlines()
    transformed_rules = determine_rules(rules_list)
    strings = data[1].splitlines()
    return sum(valid_string(string, transformed_rules, version) for string in strings)


def part_1(data):
    return constructor(data, 1)


def part_2(data):
    return constructor(data, 2)


def main() -> None:
    data = data_input("data")

    p1 = part_1(data)
    print(f"Part 1: {p1} is {p1 == 171}")

    p2 = part_2(data)
    print(f"Part 2: {p2} is {p2 == 369}")


if __name__ == "__main__":
    main()

    # import timeit
    # DATA = data_input("data")
    # print(timeit.timeit("part_1(DATA)", globals=globals(), number=10))
    # print(timeit.timeit("part_2(DATA)", globals=globals(), number=10))
