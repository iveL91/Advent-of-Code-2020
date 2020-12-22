"""
    aoc_21
    https://adventofcode.com/2020/day/21
    Time: ca. (930 (-350?) + 16)min
"""

import itertools


def data_input(filename: str) -> list[tuple[list[str], list[str]]]:
    with open(filename) as file:
        return [data_transformation(line) for line in file.read().splitlines()]


def data_transformation(line: str) -> tuple[list[str], list[str]]:
    line_split = line.split(" (contains ")
    ingredients = line_split[0].split(" ")
    allergens = line_split[1].strip(")").split(", ")
    return ingredients, allergens


def determine_none_allergens(foods: list[tuple[list[str], list[str]]], all_ingredients: set[str], all_allergens: set[str]) -> set[str]:
    none_allergens: set[str] = set()
    for ingredient in all_ingredients:
        for allergen in all_allergens:
            for food in foods:
                if allergen in food[1] and ingredient not in food[0]:
                    break
            else:
                break
        else:
            none_allergens.add(ingredient)
    return none_allergens


def constructor(foods: list[tuple[list[str], list[str]]]) -> tuple[set[str], set[str], set[str]]:
    all_ingredients = set()
    for food in foods:
        all_ingredients.update(set(food[0]))

    all_allergens = set()
    for food in foods:
        all_allergens.update(set(food[1]))

    return all_ingredients, all_allergens, determine_none_allergens(foods, all_ingredients, all_allergens)


def part_1(foods: list[tuple[list[str], list[str]]]) -> int:
    _, _, none_allergens = constructor(foods)
    return sum([sum(ingredient in none_allergens for ingredient in food[0]) for food in foods])


def check_food(food: tuple[list[str], list[str]], ingredients_allergens_pairs: dict[str, str]) -> bool:
    for allergen in food[1]:
        if ingredients_allergens_pairs[allergen] not in food[0]:
            return False
    return True


def determine_allergens(foods: list[tuple[list[str], list[str]]], all_ingredients: set[str], all_allergens: set[str]) -> dict[str, str]:
    for ingredients_permutation in itertools.permutations(all_ingredients, len(all_allergens)):
        ingredients_allergens_pairs = {allergen: ingredient for allergen, ingredient in zip(
            all_allergens, ingredients_permutation)}
        for food in foods:
            if not check_food(food, ingredients_allergens_pairs):
                break
        else:
            return ingredients_allergens_pairs


def part_2(foods: list[tuple[list[str], list[str]]]) -> str:
    all_ingredients, all_allergens, none_allergens = constructor(foods)
    dangerous_ingredients_set = all_ingredients.difference(none_allergens)
    dangerous_ingredients_dict = determine_allergens(
        foods, dangerous_ingredients_set, all_allergens)
    dangerous_ingredients = dict(sorted(dangerous_ingredients_dict.items()))
    return ",".join([ingredient for ingredient in dangerous_ingredients.values()])


def main() -> None:
    foods = data_input("data")

    p1 = part_1(foods)
    print(f"Part 1: {p1} is {p1 == 1930}")

    p2 = part_2(foods)
    print(
        f"Part 2: {p2} is {p2 == 'spcqmzfg,rpf,dzqlq,pflk,bltrbvz,xbdh,spql,bltzkxx'}")


if __name__ == "__main__":
    main()

    import timeit
    FOODS = data_input("data")
    print(timeit.timeit("part_1(FOODS)", globals=globals(), number=1_000))
    
    print(timeit.timeit("part_2(FOODS)", globals=globals(), number=100))
