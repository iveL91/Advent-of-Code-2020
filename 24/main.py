"""
    aoc_24
    https://adventofcode.com/2020/day/24
    Time: ca. (47 + 97)min
"""


from typing import DefaultDict

Instruction = list[tuple[int, int]]

DIRECTIONS: dict[str, tuple[int, int]] = {
    "e": (0, 2),
    "se": (-1, 1),
    "sw": (-1, -1),
    "w": (0, -2),
    "nw": (1, -1),
    "ne": (1, 1)
}


def data_input(filename: str) -> list[Instruction]:
    with open(filename) as file:
        return [data_transformation(line) for line in file.read().splitlines()]


def data_transformation(line: str) -> Instruction:
    instruction: Instruction = []
    while line:
        if line[0] in ["n", "s"]:
            instruction.append(DIRECTIONS[line[:2]])
            line = line[2:]
        else:
            instruction.append(DIRECTIONS[line[0]])
            line = line[1:]
    return instruction


def tuple_add(tuple_1: tuple[int, ...], tuple_2: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(component_1 + component_2 for component_1, component_2 in zip(tuple_1, tuple_2))


def constructor(instructions: list[Instruction]) -> dict[tuple[int, int], bool]:
    tiles: DefaultDict[tuple[int, int], bool] = DefaultDict(bool)
    for instruction in instructions:
        tile_direction = (0, 0)
        for direction in instruction:
            tile_direction = tuple_add(tile_direction, direction)
        tiles[tile_direction] = not tiles[tile_direction]
    return tiles


def count_black_tiles(tiles: dict[tuple[int, int], bool]) -> int:
    return sum(tiles.values())


def part_1(instructions: list[Instruction]) -> int:
    tiles = constructor(instructions)
    return count_black_tiles(tiles)


def determine_amount_neighbors(tile_position: tuple[int, int], extended_tiles: dict[tuple[int, int], bool]) -> int:
    neighbor_values = [extended_tiles[tuple_add(
        tile_position, direction)] for direction in DIRECTIONS.values()]
    return sum(neighbor_values)


def extend_grid(tiles: dict[tuple[int, int], bool]) -> dict[tuple[int, int], bool]:
    additional_tiles = {tuple_add(
        tile_position, direction): False for tile_position in tiles for direction in DIRECTIONS.values()}
    return additional_tiles | tiles


def flipping(tiles: dict[tuple[int, int], bool]) -> dict[tuple[int, int], bool]:
    new_tiles = extend_grid(tiles)
    extended_tiles = extend_grid(new_tiles)

    neighbor_dict = {tile_position: determine_amount_neighbors(
        tile_position, extended_tiles) for tile_position in new_tiles}

    for tile_position, tile_value in new_tiles.items():
        if tile_value and (not neighbor_dict[tile_position] or neighbor_dict[tile_position] > 2):
            new_tiles[tile_position] = not new_tiles[tile_position]
        elif not tile_value and neighbor_dict[tile_position] == 2:
            new_tiles[tile_position] = not new_tiles[tile_position]
    return new_tiles


def part_2(instructions: list[Instruction], days: int = 100) -> int:
    tiles = constructor(instructions)
    for _ in range(days):
        tiles = flipping(tiles)
    return count_black_tiles(tiles)


def main() -> None:
    instructions = data_input("data")

    p1 = part_1(instructions)
    print(f"Part 1: {p1} is {p1 == 373}")

    p2 = part_2(instructions)
    print(f"Part 2: {p2} is {p2 == 3917}")


if __name__ == "__main__":
    main()

    # import timeit
    # INSTRUCTIONS = data_input("data")
    # print(timeit.timeit("part_1(INSTRUCTIONS)", globals=globals(), number=1_000))
    # print(timeit.timeit("part_2(INSTRUCTIONS)", globals=globals(), number=1))
