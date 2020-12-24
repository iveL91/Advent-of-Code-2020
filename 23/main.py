"""
    aoc_23
    https://adventofcode.com/2020/day/23
    Time: ca. (48 + )min
"""

def get_key_from_value(dct, wanted_value):
    return dct.keys()[dct.values().index(wanted_value)]

class NewCupGame:
    def __init__(self, cups, length) -> None:
        self.cups = {i: i for i in range(length)}
        self.cups |= {i: number for i, number in enumerate(cups)}
        self.position = 0


    def move(self) -> None:
        current_cup = self.cups[self.position]
        picked_up_cups = set(self.cups[self.position+1], self.cups[self.position+2], self.cups[self.position+3])
        destination_cup = current_cup - 1
        while destination_cup in picked_up_cups:
            destination_cup -= 1
            if destination_cup < 0:
                destination_cup = len(self.cups)

        destination_cup_index = get_key_from_value(self.cups, destination_cup)


        

class CupGame:
    def __init__(self, cups: list[int]) -> None:
        one_index = cups.index(1)
        self.cups = cups[one_index:] + cups[:one_index]
        # print(self.cups)
        # self.cups = cups
        self.position: int = self.cups.index(cups[0])
        # print(self.position)


    def move(self) -> None:
        cups = self.cups[self.position:] + self.cups[:self.position]
        current_cup = cups[0]
        picked_up_cups: list[int] = cups[1:4]
        # print()
        # print(f"{current_cup=}")
        # print(f"{picked_up_cups=}")
        available_cups = set(cups).difference([current_cup])
        available_cups = available_cups.difference(picked_up_cups)
        # print(f"{available_cups=}")
        destination_cup = current_cup - 1
        while destination_cup not in available_cups:
            destination_cup -= 1
            if destination_cup < 0:
                destination_cup = len(cups)
        # print(f"{destination_cup=}")
        new_cups = cups[4:] + [cups[0]]
        # print(f"{new_cups=}")
        destination_cup_index: int = new_cups.index(destination_cup)
        self.cups = new_cups[:destination_cup_index+1] + \
            picked_up_cups + new_cups[destination_cup_index+1:]
        # if not self.cups.index(1):
        #     print()
        one_index = self.cups.index(1)
        # print(f"{one_index=}")
        self.cups = self.cups[one_index:] + self.cups[:one_index]
        # print(re_arranged, self.cups[0])
        # print(re_arranged[:5], re_arranged[-3:], self.cups[0])
        # print(f"{self.cups=}")

        # self.position = (-one_index) % len(self.cups)
        self.position = len(self.cups) - one_index
        # print(self.position)
        # self.position %= len(self.cups)
        # print(f"{self.cups[self.position]=}")

    def run(self, moves: int) -> None:
        configurations = set()
        counter = 0
        for _ in range(moves):
            self.move()
            counter += 1
            # if not counter % 1_000_00:
            print(f"{counter=}")
            if tuple(self.cups + [self.position]) in configurations:
                print("HERE")  # , self.cups, counter)
                break
            configurations.add(tuple(self.cups + [self.position]))
        print(f"{counter=}")
        # print(tuple(self.cups[one_index:] + self.cups[:one_index] + [self.position]))
        counter_2 = 0
        for _ in range((moves-counter) % (counter-1)):
            # print("bla")
            counter_2 += 1
            self.move()
        print(f"{counter_2=}")

    def order(self) -> int:
        # return int("".join([str(element) for element in self.cups[1:]]))
        cup_1_index = self.cups.index(1)
        print(f"{cup_1_index=}")
        extended_cups = self.cups * 2
        order_list = extended_cups[cup_1_index+1:cup_1_index+9]
        return int("".join([str(element) for element in order_list]))


def data_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(number) for number in file.read()]


def part_1(cups, runs: int = 100) -> int:
    cup_game = CupGame(cups)
    runs = 100
    cup_game.run(runs)
    return cup_game.order()


# def part_1(cups, runs: int = 100) -> int:
#     cup_game = NewCupGame(cups, 10)
#     print(cup_game.cups)
#     print(cup_game.position)
#     # runs = 100
#     # cup_game.run(runs)
#     # return cup_game.order()


def part_2(cups):
    # length = 1_000_000
    # runs = 10_000_000
    length = 1_000_000
    runs = 10_00
    cup_game = CupGame(cups+list(range(10, length+1)))
    # print(len(cup_game.cups))
    # print(cup_game.cups)
    cup_game.run(runs)
    # print(cup_game.cups)
    print(cup_game.cups[1], cup_game.cups[2])
    return cup_game.cups[1] * cup_game.cups[2]


def main() -> None:
    cups = data_input("test_data")
    # cups = data_input("data")

    p1 = part_1(cups)
    print(f"Part 1: {p1} is {p1 == 97632548}")

    p2 = part_2(cups)
    print(f"Part 2: {p2} is {p2 == 0}")


if __name__ == "__main__":
    main()
