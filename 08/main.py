"""
    aoc_08
    https://adventofcode.com/2020/day/8
    Time: ca. (23 + 11)min
"""


def data_input(filename: str = "data") -> list[list[str]]:
    with open(filename) as file:
        return [line.split() for line in file.read().splitlines()]


class HandheldGameConsole:
    instructions: list[list[str]]

    def __init__(self) -> None:
        self.acc: int = 0
        self.positions: list[int] = [0]
        self.breaker: bool = False

    def run(self) -> None:
        while True:
            if self.positions[-1] >= len(self.instructions):
                break

            operation = self.instructions[self.positions[-1]][0]
            operation_value = int(self.instructions[self.positions[-1]][1])
            if operation == "acc":
                self.acc += operation_value
                if not (new_position := self.positions[-1]+1) in self.positions:
                    self.positions.append(new_position)
                else:
                    self.breaker = True
                    break
            elif operation == "jmp":
                if not (new_position := self.positions[-1]+operation_value) in self.positions:
                    self.positions.append(new_position)
                else:
                    self.breaker = True
                    break
            elif operation == "nop":
                if not (new_position := self.positions[-1]+1) in self.positions:
                    self.positions.append(new_position)
                else:
                    self.breaker = True
                    break


def constructor(instructions: list[list[str]]) -> HandheldGameConsole:
    HandheldGameConsole.instructions = instructions
    handheld_game_console = HandheldGameConsole()
    handheld_game_console.run()
    return handheld_game_console


def part_1(instructions: list[list[str]]) -> int:
    handheld_game_console = constructor(instructions)
    return handheld_game_console.acc


def part_2(instructions: list[list[str]]) -> int:
    for index, instruction in enumerate(instructions):
        if instruction[0] == "nop":
            new_instructions = instructions.copy()
            new_instructions[index] = ["jmp", instruction[1]]
        elif instruction[0] == "jmp":
            new_instructions = instructions.copy()
            new_instructions[index] = ["nop", instruction[1]]
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
