from random import randint
import sys

from deck import (Hand, DealerHand)


class Chips:
    def __init__(self, total=500):
        self.total = total

    def __str__(self):
        return "Current amount: {} chips".format(self.total)


class Player:
    def __init__(
            self,
            first_name,
            last_name,
            gender,
            chips=Chips()):
        self.chips = chips
        self.gender = gender
        self.last_name = last_name
        self.first_name = first_name
        self.hand = Hand()
        self.bets = 0

    def show_hand(self):
        for j in self.hand:
            j.show()

    def take_card(self, card):
        self.hand.add_card(card)

    def num_of_chips(self):
        return self.chips.total

    def add_chips(self, chips_to_add):
        self.chips.total += chips_to_add

    def bet_chips(self, chips_to_bet):
        self.chips.total -= chips_to_bet
        self.bets += chips_to_bet

    def is_human(self):
        return False

    def hand_string(self):
        return "Your {}\nYour {}".format(self.hand, self.hand.value_string())


class Human(Player):
    def is_human(self):
        return True


class Dealer(Player):
    def __init__(
            self,
            first_name,
            last_name,
            gender,
            chips=Chips()):
        self.chips = chips
        self.gender = gender
        self.last_name = last_name
        self.first_name = first_name
        self.hand = DealerHand()
        self.bets = 0

    def num_of_chips(self):
        return sys.maxsize

    def add_chips(self, chips_to_add):
        pass

    def bet_chips(self, chips_to_bet):
        self.bets += chips_to_bet

    def hand_string(self):
        return "Dealer {}".format(self.hand)

    def choose_option(self, options):
        if min(self.hand.values) in range(16, 22):
            return "Stand"
        return "Hit"


# I know what my hand is
# I store the logic for an AI agent
class RandomPlayer(Player):
    def choose_move(self):
        # TODO
        if 21 in self.hand.values():
            return "BLACKJACK"  # signify winning
        if min(self.hand.values()) > 21:
            return "FOLD"
        choice = randint(2)
        return ["BET", "HOLD", "FOLD"][choice]


# makes random moves

class EasyPlayer(Player):
    # TODO rules for players
    # easy player always stands on 14 or more
    pass


class TerminalPlayer(Player):
    # TODO might not be needed anymore
    pass


class HardPlayer(Player):
    # TODO stands on 17
    # TODO knows card before so makes informed choice
    pass


# counts cards


class ImpossiblePlayer(Player):
    pass


# has perfect knowledge of deck

if __name__ == '__main__':
    player = Player("Mark", "White", "M")

    random_player = RandomPlayer("Jack", "Smith", "M")
