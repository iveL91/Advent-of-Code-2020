"""
    aoc_04
    https://adventofcode.com/2020/day/4
    Time: ca. (26 + 58)min
"""

from abc import ABC, abstractmethod
from typing import Optional


def in_range(number: int, lower_bound: int, upper_bound: int) -> bool:
    return number in range(lower_bound, upper_bound+1)


class PassportInformation(ABC):
    def __init__(self, value: Optional[str]) -> None:
        self.prop = value

    def exists(self) -> bool:
        return bool(self.prop)

    @abstractmethod
    def __bool__(self, *args, **kwargs) -> bool:
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.prop})"


class Year(PassportInformation):
    def __bool__(self, lower_bound: int, upper_bound: int) -> bool:
        if self.prop is None:
            return False
        return (len(self.prop) == 4) and in_range(int(self.prop), lower_bound, upper_bound)


class BirthYear(Year):
    def __bool__(self) -> bool:
        return super().__bool__(1920, 2002)


class IssueYear(Year):
    def __bool__(self) -> bool:
        return super().__bool__(2010, 2020)


class ExpirationYear(Year):
    def __bool__(self) -> bool:
        return super().__bool__(2020, 2030)


class Height(PassportInformation):
    units: list[str] = ["cm", "in"]
    ranges: dict[str, tuple[int, int]] = {
        unit: bounds for unit, bounds in zip(units, [(150, 193), (59, 76)])}

    def __bool__(self) -> bool:
        if self.prop is None:
            return False
        if (unit := self.prop[-2:]) in self.units:
            return in_range(int(self.prop[:-2]), *self.ranges[unit])
        return False


class HairColor(PassportInformation):
    def __bool__(self) -> bool:
        if self.prop is None or self.prop[0] != "#" or len(self.prop) != 7:
            return False
        valid_characters = list(str(1234567890)) + list("abcdefgh")
        return all(character in valid_characters for character in self.prop[1:])


class EyeColor(PassportInformation):
    def __bool__(self) -> bool:
        if self.prop is None:
            return False
        return self.prop in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


class PassportID(PassportInformation):
    def __bool__(self) -> bool:
        if self.prop is None or len(self.prop) != 9:
            return False
        numbers = list(str(1234567890))
        return all(character in numbers for character in self.prop)


class CountryID(PassportInformation):
    def __bool__(self) -> bool:
        return True

    def exists(self) -> bool:
        return True


class Passport:
    def __init__(self, dct: dict[str, str]) -> None:
        self.byr = BirthYear(dct.get("byr", None))
        self.iyr = IssueYear(dct.get("iyr", None))
        self.eyr = ExpirationYear(dct.get("eyr", None))
        self.hgt = Height(dct.get("hgt", None))
        self.hcl = HairColor(dct.get("hcl", None))
        self.ecl = EyeColor(dct.get("ecl", None))
        self.pid = PassportID(dct.get("pid", None))
        self.cid = CountryID(dct.get("cid", None))

    def exists(self) -> bool:
        return all(var.exists() for var in vars(self).values())

    def __bool__(self) -> bool:
        return all(var for var in vars(self).values())


def data_input(filename: str = "data") -> list[dict[str, str]]:
    with open(filename) as file:
        return [string_to_passport(password_string) for password_string in file.read().split("\n\n")]


def string_to_passport(string: str) -> Passport:
    passport_list = [property.split(":") for property in string.split()]
    return Passport({property[0]: property[1] for property in passport_list})


def part_1(passports) -> int:
    return sum(passport.exists() for passport in passports)


def part_2(passports) -> int:
    return sum(bool(passport) for passport in passports)


def main() -> None:
    passports = data_input("data")

    p1 = part_1(passports)
    print(f"Part 1: {p1} is {p1 == 228}")

    p2 = part_2(passports)
    print(f"Part 2: {p2} is {p2 == 175}")


if __name__ == "__main__":
    main()

    # import timeit
    # passports = data_input("data")
    # print(timeit.timeit("part_1(passports)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(passports)", globals=globals(), number=10_000))
