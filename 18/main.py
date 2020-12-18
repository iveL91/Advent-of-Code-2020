"""
    aoc_18
    https://adventofcode.com/2020/day/18
    Time: ca. (133 +  147)min
"""

import re
from operator import add, mul


def data_input(filename: str = "data") -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def find_first_enclosing_parantheses(string: str) -> str:
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
    raise ValueError


def find_first_add(string: str) -> str:
    pattern = re.compile(r"\d+ \+ \d+")
    match = re.findall(pattern, string)
    return match[0] if match else ""


def find_first_calc(term: str) -> str:
    symbols = term.split(" ")
    if len(symbols) < 3:
        return ""
    return " ".join(symbols[:3])


def calculate_term(term: str) -> str:
    operators = {"+": add, "*": mul}
    symbols = term.split(" ")
    return str(operators[symbols[1]](int(symbols[0]), int(symbols[2])))


def reduction(term: str, version: int = 1) -> str:
    if parantheses_term := find_first_enclosing_parantheses(term):
        term = term.replace(parantheses_term,
                            reduction(parantheses_term[1:-1], version), 1)
        return reduction(term, version)

    if version == 2 and (add_term := find_first_add(term)):
        term = term.replace(add_term, calculate_term(add_term), 1)
        return reduction(term, version)

    if calc_term := find_first_calc(term):
        term = term.replace(calc_term, calculate_term(calc_term), 1)
        return reduction(term, version)

    return term


def part_1(terms: list[str]) -> int:
    return sum(int(reduction(term)) for term in terms)


def part_2(terms: list[str]) -> int:
    return sum(int(reduction(term, 2)) for term in terms)


def main() -> None:
    terms = data_input("data")

    p1 = part_1(terms)
    print(f"Part 1: {p1} is {p1 == 67800526776934}")

    p2 = part_2(terms)
    print(f"Part 2: {p2} is {p2 == 340789638435483}")


if __name__ == "__main__":
    main()

    # import timeit
    # TERMS = data_input("data")
    # print(timeit.timeit("part_1(TERMS)", globals=globals(), number=1_000))
    # print(timeit.timeit("part_2(TERMS)", globals=globals(), number=1_000))
