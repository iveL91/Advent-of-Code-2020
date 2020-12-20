"""
    aoc_20
    https://adventofcode.com/2020/day/20
    Time: ca. (139 + 116)min
"""
from __future__ import annotations
import itertools

from functools import reduce
from operator import mul

from typing import Iterable, NamedTuple, Optional


class Borders(NamedTuple):
    north: list[str]
    east: list[str]
    south: list[str]
    west: list[str]


class Neighbors(NamedTuple):
    north: Optional[int]
    east: Optional[int]
    south: Optional[int]
    west: Optional[int]


def tuple_add(tuple_1: tuple[int, ...], tuple_2: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(component_1 + component_2 for component_1, component_2 in zip(tuple_1, tuple_2))


def tuple_negative(tup: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-component for component in tup)


class Tile:
    def __init__(self, image_grid: list[str], number: int):
        self.image_grid = image_grid
        self.number = number
        self.borders: dict[tuple[int, int], list[str]] = {(-1, 0): self.image_grid[0],  # north
                                                          # east
                                                          (0, 1): [row[-1] for row in self.image_grid],
                                                          # south
                                                          (1, 0): self.image_grid[-1],
                                                          # west
                                                          (0, -1): [row[0] for row in self.image_grid]
                                                          }
        self.position = (0, 0)
        self.neighbors = {(-1, 0): None,
                          (0, 1): None,
                          (1, 0): None,
                          (0, -1): None
                          }

    def rotate_90(self) -> Tile:
        return Tile(grid_rotate_90(self.image_grid),
                    self.number)

    def flip_horizontal(self) -> Tile:
        return Tile(grid_flip_horizontally(self.image_grid),
                    self.number)

    def flip_vertical(self) -> Tile:
        return Tile(grid_flip_vertically(self.image_grid),
                    self.number)

    def __repr__(self) -> str:
        return f"Tile {self.number}"


def grid_rotate_90(grid: list[str]) -> list[str]:
    return ["".join([grid[i][-j-1] for i, _ in enumerate(grid)])
            for j, _ in enumerate(grid[0])]


def grid_flip_horizontally(grid: list[str]) -> list[str]:
    return [grid[-i-1] for i, _ in enumerate(grid)]


def grid_flip_vertically(grid: list[str]) -> list[str]:
    return ["".join([row[-i-1] for i, _ in enumerate(grid[0])]) for row in grid]


def data_input(filename: str) -> list[Tile]:
    with open(filename) as file:
        return [data_transformation(tile_string) for tile_string in file.read().split("\n\n")]


def data_transformation(tile_string: str) -> Tile:
    tile_string_split: list[str] = tile_string.splitlines()
    number = int(tile_string_split[0].split(" ")[1][:-1])
    image_grid = tile_string_split[1:]
    return Tile(image_grid, number)


def check_for_neighborhood(tile_1: Tile, tile_2: Tile) -> bool:
    for second_border_direction, second_border in tile_2.borders.items():
        if not tile_1.neighbors[tuple_negative(second_border_direction)] and second_border == tile_1.borders[tuple_negative(second_border_direction)]:
            tile_2.position = tuple_add(
                tile_1.position, tuple_negative(second_border_direction))
            tile_1.neighbors[tuple_negative(
                second_border_direction)] = tile_2.number
            tile_2.neighbors[second_border_direction] = tile_1.number
            return True
    return False


def prod(numbers: Iterable[int]) -> int:
    return reduce(mul, numbers, 1)


def position_tiles(tiles: list[Tile]) -> dict[tuple[int, int], Tile]:
    flips = [lambda tile: tile, lambda tile: tile.flip_horizontal(
    ), lambda tile: tile.flip_vertical()]
    rotations = [lambda tile: tile, lambda tile: tile.rotate_90(), lambda tile: tile.rotate_90(
    ).rotate_90(), lambda tile: tile.rotate_90().rotate_90().rotate_90()]

    grid_tiles = {(0, 0): tiles[0]}
    free_tiles = tiles[1:]

    new_free_tiles = free_tiles.copy()
    while new_free_tiles:
        free_tiles = new_free_tiles
        for tile in free_tiles:
            for bounded_tile in grid_tiles.values():
                breaker = False
                for flip, rotation in itertools.product(flips, rotations):
                    new_tile = flip(rotation(tile))
                    if check_for_neighborhood(bounded_tile, new_tile):
                        grid_tiles[new_tile.position] = new_tile
                        new_free_tiles.remove(tile)
                        breaker = True
                        break
                if breaker:
                    break
    return grid_tiles


def grid_tiles_size(grid_positions) -> tuple[tuple[int]]:
    min_up_down = min(coordinates[0] for coordinates in grid_positions)
    max_up_down = max(coordinates[0] for coordinates in grid_positions)
    min_left_right = min(coordinates[1] for coordinates in grid_positions)
    max_left_right = max(coordinates[1] for coordinates in grid_positions)
    return (min_up_down, max_up_down), (min_left_right, max_left_right)


def part_1(tiles: list[Tile]) -> int:
    grid_positions_tiles = position_tiles(tiles)
    mins_maxs = grid_tiles_size(grid_positions_tiles.keys())
    pro = prod(grid_positions_tiles[(
        ele1, ele2)].number for ele1, ele2 in itertools.product(*mins_maxs))
    image = create_image({position: eliminate_borders_from_grid(
        tile.image_grid) for position, tile in grid_positions_tiles.items()})
    return pro


def eliminate_borders_from_grid(grid: list[str]) -> list[str]:
    return [row[1:-1] for row in grid[1:-1]]


def add_grids_horizontally(grid_1: list[str], grid_2: list[str]) -> list[str]:
    return [row_1 + row_2 for row_1, row_2 in zip(grid_1, grid_2)]


def add_grids_vertically(grid_1: list[str], grid_2: list[str]) -> list[str]:
    return grid_1 + grid_2


def create_image(grid_dict: dict[tuple[int, int], list[str]]) -> list[str]:
    mins_maxs = grid_tiles_size(grid_dict.keys())
    new_grid = []
    for up_down_index in range(mins_maxs[0][0], mins_maxs[0][1]+1):
        new_line_grid = grid_dict[(up_down_index, mins_maxs[1][0])]
        for left_right_index in range(mins_maxs[1][0]+1, mins_maxs[1][1]+1):
            new_line_grid = add_grids_horizontally(
                new_line_grid, grid_dict[(up_down_index, left_right_index)])
        new_grid += new_line_grid
    return new_grid


def pattern_positon_list(pattern: list[str]) -> list[tuple[int, int]]:
    lst = []
    for index_up_down, row in enumerate(pattern):
        for index_left_right, character in enumerate(row):
            if character == "#":
                lst.append((index_up_down, index_left_right))
    return lst


def part_2(tiles: list[Tile]) -> int:
    sea_monser_pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()
    grid_positions_tiles = position_tiles(tiles)
    image = create_image({position: eliminate_borders_from_grid(
        tile.image_grid) for position, tile in grid_positions_tiles.items()})

    sea_monster_pattern_lst = pattern_positon_list(sea_monser_pattern)

    grid_list = pattern_positon_list(image)
    flips = [lambda grid: grid, lambda grid: grid_flip_horizontally(grid
                                                                    ), lambda grid: grid_flip_vertically(grid)]
    rotations = [lambda grid: grid, lambda grid: grid_rotate_90(grid), lambda grid: grid_rotate_90(
        grid_rotate_90(grid)), lambda grid: grid_rotate_90(grid_rotate_90(grid_rotate_90(grid)))]

    for flip, rotation in itertools.product(flips, rotations):
        new_sea_monster_pattern = flip(rotation(sea_monser_pattern))
        sea_monster_height = len(new_sea_monster_pattern)
        sea_monster_length = len(new_sea_monster_pattern[0])
        sea_monster_pattern_lst = pattern_positon_list(new_sea_monster_pattern)

        for row_index in range(0, len(image) - sea_monster_height):
            for column_index in range(0, len(image[0]) - sea_monster_length):
                pattern_list = [(position[0]+row_index, position[1]+column_index)
                                for position in sea_monster_pattern_lst]
                grid_list = overlap(grid_list, pattern_list)

    return len(grid_list)


def overlap(grid_list: list[tuple[int, int]], pattern_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    for position in pattern_list:
        if position not in grid_list:
            return grid_list

    for position in pattern_list:
        grid_list.remove(position)

    return grid_list


def main() -> None:
    tiles = data_input("data")
    p1 = part_1(tiles)
    print(f"Part 1: {p1} is {p1 == 18482479935793}")

    tiles = data_input("data")
    p2 = part_2(tiles)
    print(f"Part 2: {p2} is {p2 == 2118}")


if __name__ == "__main__":
    main()
