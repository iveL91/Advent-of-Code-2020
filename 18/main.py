"""
    aoc_18
    https://adventofcode.com/2020/day/18
    Time: ca. (133 +  147)h
"""

import re
from operator import add, mul


def data_input(filename: str = "data") -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def find_parantheses(string: str) -> str:
    counter = 0
    try:
        first = string.index("(")
    except ValueError:
        return ""
    for index, char in enumerate(string[first:], first):
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        else:
            continue
        if not counter:
            return string[first:index+1]
    else:
        raise ValueError


def find_add(string: str) -> str:
    pattern = re.compile(r"\d+ \+ \d+")
    match = re.findall(pattern, string)
    return match[0] if match else None


def calculation(term: str, version: int = 1) -> str:
    if parantheses_terms := find_parantheses(term):
        term = term.replace(parantheses_terms,
                            calculation(parantheses_terms[1:-1], version), 1)
        return calculation(term, version)

    if version == 2 and (add_term := find_add(term)):
        term = term.replace(add_term, calculation(add_term), 1)
        return calculation(term, version)

    if len(symbols := term.split(" ")) > 1:
        operators = {"+": add, "*": mul}
        result = str(operators[symbols[1]](int(symbols[0]), int(symbols[2])))

        if len(symbols) > 3:
            new_term = " ".join([result] + symbols[3:])
            result = calculation(new_term, version)
        return result

    return term


def part_1(terms: list[str]) -> int:
    return sum(int(calculation(term)) for term in terms)


def part_2(terms: list[str]) -> int:
    return sum(int(calculation(term, 2)) for term in terms)


def main() -> None:
    terms = data_input("data")

    p1 = part_1(terms)
    print(f"Part 1: {p1} is {p1 == 67800526776934}")

    p2 = part_2(terms)
    print(f"Part 2: {p2} is {p2 == 340789638435483}")


if __name__ == "__main__":
    main()

    # import timeit
    # terms = data_input("data")
    # print(timeit.timeit("part_1(terms)", globals=globals(), number=1_000))
    # print(timeit.timeit("part_2(terms)", globals=globals(), number=1_000))
