"""
    aoc_12
    https://adventofcode.com/2020/day/12
    Time: ca. (74 + 15)min
"""

import functools
from typing import Callable, NamedTuple


class NavigationInstruction(NamedTuple):
    action: str
    value: int


def data_input(filename: str = "data") -> list[NavigationInstruction]:
    with open(filename) as file:
        return [data_transformation(string) for string in file.read().splitlines()]


def data_transformation(string: str) -> NavigationInstruction:
    return NavigationInstruction(string[0], int(string[1:]))


class Ship:
    directions_dict: dict[str, tuple[int, int]] = {"N": (0, 1),
                                                   "S": (0, -1),
                                                   "E": (1, 0),
                                                   "W": (-1, 0)}

    def __init__(self, navigation_instructions: list[NavigationInstruction]) -> None:
        self.navigation_instructions = navigation_instructions
        self.direction = self.directions_dict["E"]
        self.position = (0, 0)
        self.waypoint_position = (10, 1)

    def new_position(self, navigation_instruction: NavigationInstruction, position: tuple[int, int]) -> tuple[int, int]:
        return tuple_add(
            position, tuple_scalar_mul(navigation_instruction.value, self.directions_dict[navigation_instruction.action]))

    @staticmethod
    def new_direction(navigation_instruction: NavigationInstruction, direction: tuple[int, int]) -> tuple[int, int]:
        if navigation_instruction.action == "L":
            return repeated(
                tuple2D_rotate_90, navigation_instruction.value // 90)(direction)
        # elif navigation_instruction.action == "R":
        return repeated(tuple2D_rotate_90, 4 - navigation_instruction.value // 90)(direction)

    def constructor_move(self, navigation_instruction: NavigationInstruction, position: tuple[int, int], direction: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
        if navigation_instruction.action in ["N", "S", "E", "W"]:
            position = self.new_position(navigation_instruction, position)
        else:  # navigation_instruction.action in ["L", "R"]:
            direction = self.new_direction(navigation_instruction, direction)
        return position, direction

    def move_forward(self, steps: int, direction: tuple[int, int]) -> None:
        self.position = tuple_add(
            self.position, tuple_scalar_mul(steps, direction))

    def move_ship(self, navigation_instruction: NavigationInstruction) -> None:
        self.position, self.direction = self.constructor_move(
            navigation_instruction, self.position, self.direction)

    def move_waypoint_position(self, navigation_instruction: NavigationInstruction) -> None:
        position, direction = self.constructor_move(
            navigation_instruction, self.waypoint_position, self.waypoint_position)
        self.waypoint_position = position if self.waypoint_position != position else direction

    def move(self, navigation_instruction: NavigationInstruction, direction: tuple[int, int], movement: Callable) -> None:
        if navigation_instruction.action == "F":
            self.move_forward(navigation_instruction.value, direction)
        else:
            movement(navigation_instruction)

    def run(self) -> None:
        for navigation_instruction in self.navigation_instructions:
            self.move(navigation_instruction, self.direction, self.move_ship)

    def __call__(self) -> None:
        for navigation_instruction in self.navigation_instructions:
            self.move(navigation_instruction, self.waypoint_position,
                      self.move_waypoint_position)


def tuple_add(tuple_1: tuple[int, ...], tuple_2: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(component_1 + component_2 for component_1, component_2 in zip(tuple_1, tuple_2))


def tuple_scalar_mul(scalar: int, tup: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(scalar * component for component in tup)


def tuple2D_rotate_90(tup: tuple[int, int]) -> tuple[int, int]:
    return -tup[1], tup[0]


def repeated(f: Callable, n: int) -> Callable:
    """From https://stackoverflow.com/questions/22921626/how-to-compose-to-functions-several-times"""
    def repeat(arg):
        return functools.reduce(lambda r, g: g(r), [f] * n, arg)
    return repeat


def manhatten_distance(vector_1: tuple[int, ...], vector_2: tuple[int, ...] = (0, 0)) -> int:
    return sum(abs(component_2 - component_1) for component_1, component_2 in zip(vector_1, vector_2))


def part_1(navigation_instructions: list[NavigationInstruction]) -> int:
    ship = Ship(navigation_instructions)
    ship.run()
    return manhatten_distance(ship.position)


def part_2(navigation_instructions: list[NavigationInstruction]) -> int:
    ship = Ship(navigation_instructions)
    ship()
    return manhatten_distance(ship.position)


def main() -> None:
    navigation_instructions = data_input("data")

    p1 = part_1(navigation_instructions)
    print(f"Part 1: {p1} is {p1 == 2458}")

    p2 = part_2(navigation_instructions)
    print(f"Part 2: {p2} is {p2 == 145117}")


if __name__ == "__main__":
    main()

    # import timeit
    # navigation_instructions = data_input("data")
    # print(timeit.timeit("part_1(navigation_instructions)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(navigation_instructions)", globals=globals(), number=10_000))
