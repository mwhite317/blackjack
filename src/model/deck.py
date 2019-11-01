import collections
import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def values(self):
        """
        Defines special card values (Jack, Queen, King, Ace).

        :return: card values with updated values to high cards
        """
        card_values = {
            "Ace": [1, 11],
            "King": [10],
            "Queen": [10],
            "Jack": [10],
        }
        return [
            int(self.value)
        ] if self.value not in card_values else card_values.get(self.value)


class Deck:
    def __init__(self):
        self.deck = collections.deque([])
        self.create_deck()

    def __eq__(self, other):
        for c1, c2 in zip(self.deck, other.deck):
            if c1 != c2:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        cards_string = ""

        for card in self.deck:
            cards_string += card.__str__() + "\n"

        return cards_string

    def create_deck(self):
        """
        Creates a deck by assigning card values to each suits.

        :return: none
        """
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in [
                'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'
            ]:
                self.deck.append(Card(s, v))

    def add_deck_to_deck(self, new_deck):
        """
        Adds a new deck to the original deck.

        :param new_deck: another deck
        :return: none
        """
        self.deck += new_deck.deck

    def shuffle_deck(self):
        """
        Uses random to shuffle dictionary of deck.

        :return: none
        """
        random.shuffle(self.deck)

    def draw_card(self):
        """
        Takes card out of deck when drawn.

        :return: pops first card in dictionary
        """
        return self.deck.popleft()


class Hand:
    def __init__(self):
        self.cards = []
        self.values = []

    def __str__(self):
        card_output = ""
        for card in self.cards:
            card_output += card.__str__() + ", "
        return "cards: {}".format(card_output[:-2])

    def value_string(self):
        """
        Formats a the value.
        Prints a string instead of a list.

        :return: Total value formatted
        """
        return "Count: {}\n".format(" or ".join(map(str, self.values)))

    def add_card(self, card):
        """
        Takes a card from deck and adds to player's hand

        :param card: single card including value and suit
        :return: none
        """
        self.cards.append(card)
        if len(self.values) == 0:
            self.values = card.values()
            return

        for i, hand_value in enumerate(self.values[:]):
            if len(card.values()) == 2:
                self.values += [hand_value + card.values()[1]]
            self.values[i] += card.values()[0]

    def can_hit(self):
        """
        Can hit if player's card value is under 21

        :return: True or False
        """
        return min(self.values) < 21

    def can_stand(self):
        """
        Can stand if player's card value is under 21

        :return: True or False
        """
        return min(self.values) < 22

    def can_double(self):
        """
        Can  double is under 2 cards

        :return: True or False
        """
        return len(self.cards) == 2

    def can_split(self):
        """
        Can split if any pair, or pair of 10pt value cards

        :return: True or False
        """
        if len(self.cards) != 2:
            return False
        if self.cards[0].value == self.cards[1].value:
            return True
        if self.values == [20]:
            return True

    def can_fold(self):
        """
        Always possible, there for always True

        :return: True
        """
        return True

    def get_options(self):
        """
       Runs through hit, stand, double, split, and fold.
       Determine which are True.

        :return: possible options based on player's hand
        """
        return [option for option in [
            "Hit" if self.can_hit() else "",
            "Stand" if self.can_stand() else "",
            "Double" if self.can_double() else "",
            "Split" if self.can_split() else "",
            "Fold" if self.can_fold() else ""
        ] if option != ""]


class DealerHand(Hand):
    def __str__(self):
        return "cards: {} + ?".format(self.cards[0])

    def value_string(self):
        """
        Formats the dealer hand value.
        Prints a string instead of a list.

        :return: Total value formatted
        """
        return "Count: {}\n".format(" or ".join(map(str, self.cards[0].values())))


if __name__ == '__main__':
    # Deck Class Test
    deck = Deck()

    print("-" * 20)
    deck_shuffled = Deck()
    deck_shuffled.shuffle_deck()
    deck.add_deck_to_deck(Deck())
    print(deck)
    print("Deck is formatted correctly: {}".format(deck != deck_shuffled))

    print("-" * 20)
    print(deck.draw_card())

