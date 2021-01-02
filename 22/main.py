"""
    aoc_22
    https://adventofcode.com/2020/day/22
    Time: ca. (22 + 58)min
"""


from itertools import zip_longest


Deck = list[int]


class Combat:
    def __init__(self, deck_1: Deck, deck_2: Deck) -> None:
        self.decks = {"1": deck_1, "2": deck_2}

    def __call__(self) -> str:
        while self.decks["1"] and self.decks["2"]:
            cards_drawed = self.decks["1"][0], self.decks["2"][0]
            winners_id = str(cards_drawed.index(max(cards_drawed)) + 1)
            losers_id = "2" if winners_id == "1" else "1"

            self.decks[winners_id] = self.decks[winners_id][1:] + \
                [self.decks[winners_id][0]] + [self.decks[losers_id][0]]
            self.decks[losers_id] = self.decks[losers_id][1:]
        return "1" if self.decks["1"] else "2"


class RecursiveCombat:
    def __init__(self, deck_1: Deck, deck_2: Deck) -> None:
        self.decks = {"1": deck_1, "2": deck_2}
        self.configuration: list[list[tuple[int, int]]] = [
            list(zip_longest(self.decks["1"], self.decks["2"]))]

    def __call__(self) -> str:
        counter = 1
        while self.decks["1"] and self.decks["2"]:
            if self.configuration[-1] in self.configuration[:-1]:
                return "1"

            cards_drawed = self.decks["1"][0], self.decks["2"][0]

            if len(self.decks["1"][1:]) >= cards_drawed[0] and len(self.decks["2"][1:]) >= cards_drawed[1]:
                new_game = RecursiveCombat(
                    self.decks["1"][1:cards_drawed[0]+1].copy(), self.decks["2"][1:cards_drawed[1]+1].copy())
                winners_id = new_game()
            else:
                winners_id = str(cards_drawed.index(max(cards_drawed)) + 1)
            losers_id = "2" if winners_id == "1" else "1"

            self.decks[winners_id] = self.decks[winners_id][1:] + \
                [self.decks[winners_id][0]] + [self.decks[losers_id][0]]
            self.decks[losers_id] = self.decks[losers_id][1:]

            self.configuration.append(
                list(zip_longest(self.decks["1"], self.decks["2"])))
            counter += 1
        return "1" if self.decks["1"] else "2"


def data_input(filename: str) -> tuple[Deck, Deck]:
    with open(filename) as file:
        return data_transformation(file.read())


def data_transformation(string: str) -> tuple[Deck, Deck]:
    players_raw = string.split("\n\n")
    player_1_deck = [int(number) for number in players_raw[0].split("\n")[1:]]
    player_2_deck = [int(number) for number in players_raw[1].split("\n")[1:]]
    return player_1_deck, player_2_deck


def deck_score(deck: Deck) -> int:
    return sum(deck_number * value for deck_number,
               value in zip(reversed(deck), range(1, len(deck)+1)))


def part_1(decks: tuple[Deck, Deck]) -> int:
    game = Combat(*decks)
    winners_id = game()
    return deck_score(game.decks[winners_id])


def part_2(decks: tuple[Deck, Deck]) -> int:
    game = RecursiveCombat(*decks)
    winners_id = game()
    return deck_score(game.decks[winners_id])


def main() -> None:
    decks = data_input("data")

    p1 = part_1(decks)
    print(f"Part 1: {p1} is {p1 == 32162}")

    p2 = part_2(decks)
    print(f"Part 2: {p2} is {p2 == 32534}")


if __name__ == "__main__":
    main()

    # import timeit
    # DECKS = data_input("data")
    # print(timeit.timeit("part_1(DECKS)", globals=globals(), number=10_000))
    # print(timeit.timeit("part_2(DECKS)", globals=globals(), number=1))
