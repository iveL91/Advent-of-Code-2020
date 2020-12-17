"""
    aoc_17
    https://adventofcode.com/2020/day/17
    Time: ca. (56 + 9)min
"""

import itertools

Point = tuple[int, ...]


def tuple_add(tuple_1: Point, tuple_2: Point) -> Point:
    return tuple(ele1 + ele2 for ele1, ele2 in zip(tuple_1, tuple_2))


def data_input(filename: str, dimensions: int) -> dict[Point, bool]:
    with open(filename) as file:
        return data_transformation(file.read(), dimensions)


def data_transformation(string: str, dimensions: int) -> dict[Point, bool]:
    lines = string.splitlines()

    result = {}
    for line_index, line in enumerate(lines):
        for column_index, char in enumerate(line):
            point = tuple([column_index, line_index] + [0] * (dimensions - 2))
            result[point] = char == "#"

    return result


def determine_neighbors(point: Point) -> list[Point]:
    dimensions = len(point)
    result: list[Point] = [tuple_add(point, delta) for delta in itertools.product(
        range(-1, 2), repeat=dimensions)]
    result.remove(point)
    return result


def activate(point: Point, grid: dict[Point, bool]) -> bool:
    neighbors = determine_neighbors(point)
    active_points: int = sum(
        grid[neighbor] for neighbor in neighbors if neighbor in grid)

    if grid[point]:
        return active_points in (2, 3)
    return active_points == 3


def cycle(grid: dict[Point, bool]) -> dict[Point, bool]:
    return {point: activate(point, grid) for point in grid}


def active_cubes(grid: dict[Point, bool]) -> int:
    return sum(state for state in grid.values())


def extend_grid(grid: dict[Point, bool]) -> dict[Point, bool]:
    dimensions: int = 0
    for point in grid:
        dimensions = len(point)
        break

    mins_maxs = []
    for i in range(dimensions):
        values = [point[i] for point in grid]
        mins_maxs.append(range(min(values)-1, max(values)+2))

    extended_grid_empty: dict[Point, bool] = {
        tup: False for tup in itertools.product(*mins_maxs)}
    return extended_grid_empty | grid


def constructor(grid: dict[Point, bool], cycles: int = 6) -> int:
    for _ in range(cycles):
        grid = extend_grid(grid)
        grid = cycle(grid)
    return active_cubes(grid)


def part_1(grid: dict[Point, bool]) -> int:
    return constructor(grid)


def part_2(grid: dict[Point, bool]) -> int:
    return constructor(grid)


def main() -> None:
    grid = data_input("data", 3)
    p1 = part_1(grid)
    print(f"Part 1: {p1} is {p1 == 391}")

    grid = data_input("data", 4)
    p2 = part_2(grid)
    print(f"Part 2: {p2} is {p2 == 2264}")


if __name__ == "__main__":
    main()

    import timeit
    grid = data_input("data", 3)
    print(timeit.timeit("part_1(grid)", globals=globals(), number=100))
    grid = data_input("data", 4)
    print(timeit.timeit("part_2(grid)", globals=globals(), number=1))
