import sys

from deck import (Hand, DealerHand)


class Chips:
    def __init__(self, total=0):
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
        """
        Show player's hand

        :return: none
        """
        for j in self.hand:
            j.show()

    def take_card(self, card):
        """
        Player is given a card from deck.

        :param card: one card from deck
        :return: none
        """
        self.hand.add_card(card)

    def num_of_chips(self):
        """
        Shows player's total chips.

        :return: total chips
        """
        return self.chips.total

    def chip_string(self):
        return "Current amount: {}".format(self.num_of_chips())

    def add_chips(self, chips_to_add):
        """
        Adds desired amount of chips to chip total.

        :param chips_to_add: the number of chips to add
        :return: none
        """
        self.chips.total += chips_to_add

    def bet_chips(self, chips_to_bet):
        """
        Subtracts the buy in cost from chip total

        :param chips_to_bet: the buy cost
        :return: none
        """
        self.chips.total -= chips_to_bet
        self.bets += chips_to_bet

    def is_human(self):
        """
        Checks if player is human.
        Always set to False.

        :return: False
        """
        return False

    def hand_string(self):
        """
        Formats string of players cards and their count.

        :return: formatted string
        """
        return "Your {}\nYour {}".format(self.hand, self.hand.value_string())

    def reset_hand(self):
        self.hand = Hand()


class Human(Player):
    def is_human(self):
        """
        Always True

        :return: True
        """
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
        """
        Dealer has unlimited funds.

        :return: the maxsize of int
        """
        return sys.maxsize

    def add_chips(self, chips_to_add):
        """
        Passes to avoid complication with Dealers amount. Dealer has infinite amount of chips, therefore, there is no
        need to add chips to dealer.

        :param chips_to_add: chips that dealer wins.
        :return: none/pass
        """
        pass

    def bet_chips(self, chips_to_bet):
        """
        Adds chips to bet into bets

        :param chips_to_bet: buy in cost
        :return: none
        """
        self.bets += chips_to_bet

    def hand_string(self):
        """
        Formats string to print Dealer's hand

        :return: formatted string
        """
        return "Dealer {}\nDealer {}".format(self.hand, self.hand.value_string())

    def choose_option(self):
        """
        Dealer hits or stands.
        If card value under 16, then hits.
        Otherwise, stands.

        :return: Hit or Stand
        """
        if len(self.hand.values) == 2:
            if max(self.hand.values) in range(16, 22) or min(self.hand.values) in range(16, 22):
                return "Stand"
        if min(self.hand.values) in range(16, 22):
            return "Stand"
        if min(self.hand.values) > 22:
            return "Bust"
        return "Hit"

    def reset_hand(self):
        """
        Resets Dealer hand for next round.

        :return: none
        """
        self.hand = DealerHand()
