"""
    aoc_17
    https://adventofcode.com/2020/day/17
    Time: ca. (56 + 9)min
"""

import itertools

Point = tuple[int, ...]


class PocketDimension:
    def __init__(self, grid_dict: dict[Point, bool]):
        self.grid = grid_dict

    @property
    def active_cubes(self) -> int:
        return sum(state for state in self.grid.values())

    def extend(self) -> None:
        dimensions: int = 0
        for point in self.grid:
            dimensions = len(point)
            break

        mins_maxs = []
        for i in range(dimensions):
            values = [point[i] for point in self.grid]
            mins_maxs.append(range(min(values)-1, max(values)+2))

        self.grid = {tup: (self.grid[tup] if tup in self.grid else False)
                     for tup in itertools.product(*mins_maxs)}

    @staticmethod
    def determine_neighbors(point: Point) -> list[Point]:
        dimensions = len(point)
        result: list[Point] = [tuple_add(point, delta) for delta in itertools.product(
            range(-1, 2), repeat=dimensions)]
        result.remove(point)
        return result

    def activate(self, point: Point) -> bool:
        neighbors = self.determine_neighbors(point)
        active_points: int = sum(
            self.grid[neighbor] for neighbor in neighbors if neighbor in self.grid)

        if self.grid[point]:
            return active_points in (2, 3)
        return active_points == 3

    def __call__(self) -> None:
        self.grid = {point: self.activate(point) for point in self.grid}


def tuple_add(tuple_1: Point, tuple_2: Point) -> Point:
    return tuple(ele1 + ele2 for ele1, ele2 in zip(tuple_1, tuple_2))


def data_input(filename: str, dimensions: int) -> PocketDimension:
    with open(filename) as file:
        return data_transformation(file.read(), dimensions)


def data_transformation(string: str, dimensions: int) -> PocketDimension:
    lines = string.splitlines()

    grid_dict = {}
    for line_index, line in enumerate(lines):
        for column_index, char in enumerate(line):
            point = tuple([column_index, line_index] + [0] * (dimensions - 2))
            grid_dict[point] = char == "#"

    return PocketDimension(grid_dict)


def constructor(pocket_dimension: PocketDimension, cycles: int = 6) -> int:
    for _ in range(cycles):
        pocket_dimension.extend()
        pocket_dimension()
    return pocket_dimension.active_cubes


def part_1(grid: PocketDimension) -> int:
    return constructor(grid)


def part_2(grid: PocketDimension) -> int:
    return constructor(grid)


def main() -> None:
    pocket_dimension = data_input("data", 3)
    p1 = part_1(pocket_dimension)
    print(f"Part 1: {p1} is {p1 == 391}")

    pocket_dimension = data_input("data", 4)
    p2 = part_2(pocket_dimension)
    print(f"Part 2: {p2} is {p2 == 2264}")


if __name__ == "__main__":
    main()

    # import timeit
    # pocket_dimension = data_input("data", 3)
    # print(timeit.timeit("part_1(pocket_dimension)", globals=globals(), number=100))
    # pocket_dimension = data_input("data", 4)
    # print(timeit.timeit("part_2(pocket_dimension)", globals=globals(), number=1))
