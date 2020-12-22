"""
    aoc_21
    https://adventofcode.com/2020/day/21
    Time: ca. (930? + 16)min
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

def part_1(foods: list[tuple[list[str], list[str]]]) -> int:
    foods = sorted(foods, key=lambda x: len(x[1]))
    foods = foods[::-1]
    all_ingredients = set()
    for food in foods:
        all_ingredients.update(set(food[0]))
    print(all_ingredients)

    all_allergens = set()
    for food in foods:
        all_allergens.update(set(food[1]))
    print(all_allergens)

    # foods = sorted(foods, key=lambda x: len(x[1]))
    # print(foods)
    none_allergens = func(foods, all_ingredients, all_allergens)
    print(none_allergens)
    print("PART1", sum([sum(ingredient in none_allergens for ingredient in food[0]) for food in foods]))
    print(len(none_allergens))
    rest_set = all_ingredients.difference(none_allergens)
    dct = func2(foods, rest_set, all_allergens)
    print(dct)
    new_dct = dict(sorted(dct.items() ,  key=lambda x: x[0]))
    print(dict(sorted(dct.items() ,  key=lambda x: x[0])))
    lst = [ingredient for ingredient in new_dct.values()]
    print(lst)
    canonical_list = ",".join(lst)
    print("CAN", canonical_list)
    # print(func2(foods, rest_set, all_allergens))


    # sm = 0
    # for food in foods:
    #     for ingredient in food[0]:
    #         if ingredient 

    return sum([sum(ingredient in none_allergens for ingredient in food[0]) for food in foods])
    # NICHT 67, 192, 
    # RICHTIG 1930

def func(foods, all_ingredients, all_allergens):
    none_allergens = set()
    for ingredient in all_ingredients:
        for allergen in all_allergens:
            # print(ingredient, allergen)
            for food in foods:
                if allergen in food[1] and ingredient not in food[0]:
                    # print(ingredient, allergen, food)
                    break
            else:
                break
        else:
            # print("here")
            none_allergens.add(ingredient)
    return none_allergens

def func2(foods, all_ingredients, all_allergens):
    counter = 0
    for ingredients_permutation in itertools.permutations(all_ingredients, len(all_allergens)):
        counter += 1
        if not counter % 1_000_000:
            print(f"{counter=}")
        # print()
        # print("in perm", ingredients_permutation)
        ingredients_allergens_pairs = {allergen: ingredient for allergen, ingredient in zip(all_allergens, ingredients_permutation)}
        for food in foods:
            # print()
            # print(food)
            # print(ingredients_allergens_pairs)
            if not check_food(food, ingredients_allergens_pairs):
                # print()
                # print(food)
                # print(ingredients_allergens_pairs)
                break
        else:
            return ingredients_allergens_pairs

def check_food(food, ingredients_allergens_pairs):
    for allergen in food[1]:
        if ingredients_allergens_pairs[allergen] not in food[0]:
            return False
    return True

foods = data_input("data")
print(part_1(foods))