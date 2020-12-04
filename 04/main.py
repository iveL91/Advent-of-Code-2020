"""
    aoc_04
    https://adventofcode.com/2020/day/4
    Time: ca. (26 + 58)min
"""


def data_input(filename: str = "data") -> list[dict[str, str]]:
    with open(filename) as file:
        return [string_to_passport(password_string) for password_string in file.read().split("\n\n")]


def string_to_passport(string: str) -> dict[str, str]:
    passport_list = [property.split(":") for property in string.split()]
    return {property[0]: property[1] for property in passport_list}


def valid_range(number: int, lower_bound: int, upper_bound: int) -> bool:
    return lower_bound <= number <= upper_bound


def valid_byr(byr: str) -> bool:
    return (len(byr) == 4) and valid_range(int(byr), 1920, 2002)


def valid_iyr(iyr: str) -> bool:
    return (len(iyr) == 4) and valid_range(int(iyr), 2010, 2020)


def valid_eyr(eyr: str) -> bool:
    return (len(eyr) == 4) and valid_range(int(eyr), 2020, 2030)


def valid_hgt(hgt: str) -> bool:
    if hgt[-2:] == "cm":
        return valid_range(int(hgt[:-2]), 150, 193)
    if hgt[-2:] == "in":
        return valid_range(int(hgt[:-2]), 59, 76)
    return False


def valid_hcl(hcl: str) -> bool:
    if hcl[0] != "#":
        return False
    if len(hcl) != 7:
        return False
    valid_characters = list(str(1234567890)) + list("abcdefgh")
    return all(character in valid_characters for character in hcl[1:])


def valid_ecl(ecl: str) -> bool:
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(pid: str) -> bool:
    numbers = list(str(1234567890))
    if len(pid) != 9:
        return False
    return all(character in numbers for character in pid)


def valid_cid(cid: str) -> bool:
    return True


def valid_passport(passport) -> bool:
    if len(passport) < 7:
        return False
    if len(passport) == 8:
        return True
    for key in passport:
        if key == "cid":
            return False
    return True


def part_1(passports):
    return sum(valid_passport(passport) for passport in passports)


def valid_new_passport(passport) -> bool:
    validation_dict = {"byr": valid_byr,
                       "iyr": valid_iyr,
                       "eyr": valid_eyr,
                       "hgt": valid_hgt,
                       "hcl": valid_hcl,
                       "ecl": valid_ecl,
                       "pid": valid_pid,
                       "cid": valid_cid}
    if not valid_range(len(passport), 7, 8):
        return False
    for key, value in passport.items():
        if not validation_dict[key](value):
            return False
        if len(passport) == 7 and key == "cid":
            return False
    return True


def part_2(passports):
    return sum(valid_new_passport(passport) for passport in passports)


def main() -> None:
    passports = data_input("data")

    p1 = part_1(passports)
    print(f"Part 1: {p1} is {p1 == 228}")

    p2 = part_2(passports)
    print(f"Part 2: {p2} is {p2 == 175}")


if __name__ == "__main__":
    main()

    import timeit
    passports = data_input("data")
    print(timeit.timeit("part_1(passports)", globals=globals(), number=10_000))
    print(timeit.timeit("part_2(passports)", globals=globals(), number=10_000))