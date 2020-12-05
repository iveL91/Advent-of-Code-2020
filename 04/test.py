"""test_aoc_04"""

import unittest
from main import data_input, string_to_passport, Passport, BirthYear, Height, HairColor, EyeColor, PassportID, part_1


class TestAoC04(unittest.TestCase):
    """()"""

    def test_part_1(self):
        """()"""
        passports = data_input("test_data")
        result = part_1(passports)
        self.assertEqual(result, 2)

    def test_valid_byr_valid(self):
        self.assertTrue(BirthYear("2002"))

    def test_valid_byr_invalid(self):
        self.assertFalse(BirthYear("2003"))

    def test_valid_hgt_valid_in(self):
        self.assertTrue(Height("60in"))

    def test_valid_hgt_valid_cm(self):
        self.assertTrue(Height("190cm"))

    def test_valid_hgt_invalid_in(self):
        self.assertFalse(Height("190in"))

    def test_valid_hgt_invalid(self):
        self.assertFalse(Height("190"))

    def test_valid_hcl_valid(self):
        self.assertTrue(HairColor("#123abc"))

    def test_valid_hcl_invalid(self):
        self.assertFalse(HairColor("#123abz"))

    def test_valid_hcl_invalid_no_hashtag(self):
        self.assertFalse(HairColor("123abz"))

    def test_valid_ecl_valid(self):
        self.assertTrue(EyeColor("brn"))

    def test_valid_ecl_invalid(self):
        self.assertFalse(EyeColor("war"))

    def test_valid_pid_valid(self):
        self.assertTrue(PassportID("000000001"))

    def test_valid_pid_invalid(self):
        self.assertFalse(PassportID("0123456789"))

    def test_valid_new_passport_invalid_1(self):
        passport = string_to_passport(
            "eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
        print(passport)
        self.assertFalse(passport)

    def test_valid_new_passport_invalid_2(self):
        passport = string_to_passport("""iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946""")
        self.assertFalse(passport)

    def test_valid_new_passport_invalid_3(self):
        passport = string_to_passport("""hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
""")
        self.assertFalse(passport)

    def test_valid_new_passport_invalid_4(self):
        passport = string_to_passport("""hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""")
        self.assertFalse(passport)

    def test_valid_new_passport_valid_1(self):
        passport = string_to_passport("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f""")
        self.assertTrue(passport)

    def test_valid_new_passport_valid_2(self):
        passport = string_to_passport("""eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm""")
        self.assertTrue(passport)

    def test_valid_new_passport_valid_3(self):
        passport = string_to_passport("""hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022""")
        self.assertTrue(passport)

    def test_valid_new_passport_valid_4(self):
        passport = string_to_passport(
            """iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""")
        self.assertTrue(passport)


if __name__ == "__main__":
    unittest.main()
