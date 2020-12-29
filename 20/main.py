"""
    aoc_20
    https://adventofcode.com/2020/day/20
    Time: ca. (139 + 116)min
"""
from __future__ import annotations
import functools
import itertools
from functools import reduce
from operator import mul
from typing import Callable, Iterable, Optional


def prod(numbers: Iterable[int]) -> int:
    return reduce(mul, numbers, 1)


def repeated(f: Callable, n: int) -> Callable:
    """From https://stackoverflow.com/questions/22921626/how-to-compose-to-functions-several-times"""
    def repeat(arg):
        return functools.reduce(lambda r, g: g(r), [f] * n, arg)
    return repeat


def tuple_add(tuple_1: tuple[int, ...], tuple_2: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(component_1 + component_2 for component_1, component_2 in zip(tuple_1, tuple_2))


def tuple_negative(tup: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-component for component in tup)


class Grid(list[str]):
    def identity(self) -> Grid:
        return self

    def rotate_90(self) -> Grid:
        return Grid(["".join([self[i][-j-1] for i, _ in enumerate(self)])
                     for j, _ in enumerate(self[0])])

    def flip_horizontally(self) -> Grid:
        return Grid([self[-i-1] for i, _ in enumerate(self)])

    def flip_vertically(self) -> Grid:
        return Grid(["".join([row[-i-1] for i, _ in enumerate(self[0])]) for row in self])

    def eliminate_borders(self) -> Grid:
        return Grid([row[1:-1] for row in self[1:-1]])

    def add_horizontally(self, other) -> Grid:
        return Grid([row_1 + row_2 for row_1, row_2 in zip(self, other)])

    def add_vertically(self, other) -> Grid:
        return Grid(self + other)


class Tile:
    def __init__(self, image_grid: Grid, number: int):
        self.image_grid = image_grid
        self.number = number
        self.borders: dict[tuple[int, int], str] = {(-1, 0): self.image_grid[0],  # up
                                                    # right
                                                    (0, 1): str([row[-1] for row in self.image_grid]),
                                                    # down
                                                    (1, 0): self.image_grid[-1],
                                                    # left
                                                    (0, -1): str([row[0] for row in self.image_grid])
                                                    }
        self.position: tuple[int, int] = (0, 0)
        self.neighbors: dict[tuple[int, int], Optional[int]] = {(-1, 0): None,
                                                                (0, 1): None,
                                                                (1, 0): None,
                                                                (0, -1): None
                                                                }

    def identity(self) -> Tile:
        return Tile(self.image_grid,
                    self.number)

    def rotate_90(self) -> Tile:
        return Tile(self.image_grid.rotate_90(),
                    self.number)

    def flip_horizontally(self) -> Tile:
        return Tile(self.image_grid.flip_horizontally(),
                    self.number)

    def flip_vertically(self) -> Tile:
        return Tile(self.image_grid.flip_vertically(),
                    self.number)


def data_input(filename: str) -> list[Tile]:
    with open(filename) as file:
        return [data_transformation(tile_string) for tile_string in file.read().split("\n\n")]


def data_transformation(tile_string: str) -> Tile:
    tile_string_split = tile_string.splitlines()
    return Tile(image_grid=Grid(tile_string_split[1:]),
                number=int(tile_string_split[0].split(" ")[1][:-1]))


def check_for_neighborhood(tile_1: Tile, tile_2: Tile) -> bool:
    for second_border_direction, second_border in tile_2.borders.items():
        if tile_1.neighbors[tuple_negative(second_border_direction)] is None and second_border == tile_1.borders[tuple_negative(second_border_direction)]:
            tile_2.position = tuple_add(
                tile_1.position, tuple_negative(second_border_direction))
            tile_1.neighbors[tuple_negative(
                second_border_direction)] = tile_2.number
            tile_2.neighbors[second_border_direction] = tile_1.number
            return True
    return False


def position_tiles(tiles: list[Tile]) -> dict[tuple[int, int], Tile]:
    flips: list[Callable[[Tile], Tile]] = [Tile.identity,
                                           Tile.flip_horizontally,
                                           Tile.flip_vertically]
    rotations: list[Callable[[Tile], Tile]] = [
        repeated(Tile.rotate_90, n) for n in range(4)]

    grid_tiles: dict[tuple[int, int], Tile] = {(0, 0): tiles[0]}
    free_tiles = tiles[1:]
    while new_free_tiles := free_tiles:
        for tile in new_free_tiles:
            for positioned_tile, flip, rotation in itertools.product(grid_tiles.values(), flips, rotations):
                new_tile = flip(rotation(tile))
                if check_for_neighborhood(positioned_tile, new_tile):
                    grid_tiles[new_tile.position] = new_tile
                    free_tiles.remove(tile)
                    break
    return grid_tiles


def grid_tiles_size(grid_positions: Iterable[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    min_up_down = min(coordinates[0] for coordinates in grid_positions)
    max_up_down = max(coordinates[0] for coordinates in grid_positions)
    min_left_right = min(coordinates[1] for coordinates in grid_positions)
    max_left_right = max(coordinates[1] for coordinates in grid_positions)
    return (min_up_down, max_up_down), (min_left_right, max_left_right)


def part_1(tiles: list[Tile]) -> int:
    grid_positions_tiles = position_tiles(tiles)
    mins_maxs = grid_tiles_size(grid_positions_tiles.keys())
    return prod(grid_positions_tiles[(
        ele1, ele2)].number for ele1, ele2 in itertools.product(*mins_maxs))


def create_image(grid_dict: dict[tuple[int, int], Grid]) -> Grid:
    mins_maxs = grid_tiles_size(grid_dict.keys())
    new_grid = Grid([])
    for up_down_index in range(mins_maxs[0][0], mins_maxs[0][1]+1):
        new_line_grid = grid_dict[(up_down_index, mins_maxs[1][0])]
        for left_right_index in range(mins_maxs[1][0]+1, mins_maxs[1][1]+1):
            new_line_grid = new_line_grid.add_horizontally(
                grid_dict[(up_down_index, left_right_index)])
        new_grid = new_grid.add_vertically(new_line_grid)
    return new_grid


def pattern_positon_list(pattern: Grid) -> list[tuple[int, int]]:
    return [(index_up_down, index_left_right) for index_up_down, row in enumerate(pattern) for index_left_right, character in enumerate(row) if character == "#"]


def overlap(grid_list: list[tuple[int, int]], pattern_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    for position in pattern_list:
        if position not in grid_list:
            return grid_list

    for position in pattern_list:
        grid_list.remove(position)

    return grid_list


def part_2(tiles: list[Tile]) -> int:
    grid_positions_tiles = position_tiles(tiles)
    image = create_image({position:
                          tile.image_grid.eliminate_borders() for position, tile in grid_positions_tiles.items()})
    grid_list = pattern_positon_list(image)

    sea_monser_pattern = Grid("""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines())
    sea_monster_pattern_lst = pattern_positon_list(sea_monser_pattern)

    flips = [Grid.identity, Grid.flip_horizontally, Grid.flip_vertically]
    rotations = [repeated(Grid.rotate_90, n) for n in range(4)]

    for flip, rotation in itertools.product(flips, rotations):
        new_sea_monster_pattern = flip(rotation(sea_monser_pattern))
        sea_monster_height = len(new_sea_monster_pattern)
        sea_monster_length = len(new_sea_monster_pattern[0])
        sea_monster_pattern_lst = pattern_positon_list(new_sea_monster_pattern)

        for row_index, column_index in itertools.product(range(0, len(image) - sea_monster_height), range(0, len(image[0]) - sea_monster_length)):
            pattern_list = [(position[0]+row_index, position[1]+column_index)
                            for position in sea_monster_pattern_lst]
            grid_list = overlap(grid_list, pattern_list)

    return len(grid_list)


def main() -> None:
    tiles = data_input("data")
    p1 = part_1(tiles)
    print(f"Part 1: {p1} is {p1 == 18482479935793}")

    tiles = data_input("data")
    p2 = part_2(tiles)
    print(f"Part 2: {p2} is {p2 == 2118}")


if __name__ == "__main__":
    main()

    # import timeit
    # TILES = data_input("data")
    # print(timeit.timeit("part_1(TILES)", globals=globals(), number=1))
    # TILES = data_input("data")
    # print(timeit.timeit("part_2(TILES)", globals=globals(), number=1))
