"""
    aoc_08
    https://adventofcode.com/2020/day/8
    Time: ca. (23 + 11)min
"""


from typing import Callable, NamedTuple


class OperationArgument(NamedTuple):
    operation: str
    argument: str


def data_input(filename: str = "data") -> list[OperationArgument]:
    with open(filename) as file:
        return [OperationArgument(*line.split()) for line in file.read().splitlines()]


class HandheldGameConsole:
    instructions: list[OperationArgument]

    def __init__(self) -> None:
        self.acc: int = 0
        self.position: int = 0
        self.visited_positions: list[int] = [self.position]
        self.breaker: bool = False
        self.command_dict: dict[str, Callable] = {
            "acc": accCommand(self),
            "jmp": jmpCommand(self),
            "nop": nopCommand(self)
        }

    @property
    def operation(self) -> str:
        return self.instructions[self.position].operation

    @property
    def argument(self) -> int:
        return int(self.instructions[self.position].argument)

    def run(self) -> None:
        while not self.breaker:
            if self.position >= len(self.instructions):
                break
            self.command_dict[self.operation]()


class HandheldGameConsoleCommand:
    def __init__(self, handheld_game_console: HandheldGameConsole) -> None:
        self.handheld_game_console = handheld_game_console


class accCommand(HandheldGameConsoleCommand):
    def __call__(self) -> None:
        self.handheld_game_console.acc += self.handheld_game_console.argument
        if not (new_position := self.handheld_game_console.position + 1) in self.handheld_game_console.visited_positions:
            self.handheld_game_console.position = new_position
            self.handheld_game_console.visited_positions.append(
                self.handheld_game_console.position)
        else:
            self.handheld_game_console.breaker = True


class jmpCommand(HandheldGameConsoleCommand):
    def __call__(self) -> None:
        if not (new_position := self.handheld_game_console.position + self.handheld_game_console.argument) in self.handheld_game_console.visited_positions:
            self.handheld_game_console.position = new_position
            self.handheld_game_console.visited_positions.append(
                self.handheld_game_console.position)
        else:
            self.handheld_game_console.breaker = True


class nopCommand(HandheldGameConsoleCommand):
    def __call__(self) -> None:
        if not (new_position := self.handheld_game_console.position + 1) in self.handheld_game_console.visited_positions:
            self.handheld_game_console.position = new_position
            self.handheld_game_console.visited_positions.append(
                self.handheld_game_console.position)
        else:
            self.handheld_game_console.breaker = True


def constructor(instructions: list[OperationArgument]) -> HandheldGameConsole:
    HandheldGameConsole.instructions = instructions
    handheld_game_console = HandheldGameConsole()
    handheld_game_console.run()
    return handheld_game_console


def part_1(instructions: list[OperationArgument]) -> int:
    handheld_game_console = constructor(instructions)
    return handheld_game_console.acc


def part_2(instructions: list[OperationArgument]) -> int:
    change_dict: dict[str, str] = {
            "nop": "jmp",
            "jmp": "nop"
        }
    for index, instruction in enumerate(instructions):
        if new_operation := change_dict.get(instruction.operation, None):
            new_instructions = instructions.copy()
            new_instructions[index] = OperationArgument(new_operation, instruction.argument)
        else:
            continue

        handheld_game_console = constructor(new_instructions)

        if not handheld_game_console.breaker:
            return handheld_game_console.acc
    raise ValueError


def main() -> None:
    instructions = data_input("data")

    p1 = part_1(instructions)
    print(f"Part 1: {p1} is {p1 == 1930}")

    p2 = part_2(instructions)
    print(f"Part 2: {p2} is {p2 == 1688}")


if __name__ == "__main__":
    main()

    # import timeit
    # instructions = data_input("data")
    # print(timeit.timeit("part_1(instructions)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(instructions)", globals=globals(), number=1_000))
