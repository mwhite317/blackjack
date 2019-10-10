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
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in [
                'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'
            ]:
                self.deck.append(Card(s, v))

    def add_deck_to_deck(self, new_deck):
        self.deck += new_deck.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.popleft()

    # self.discard_pile = []
    # def discard_card_in_pile(self):
    #     self.discard_card = self.discard_pile.append(self.draw_card)
    #     return self.discard_card


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
        return "Count: {}\n".format(" or ".join(map(str, self.values)))

    def add_card(self, card):
        self.cards.append(card)
        if len(self.values) == 0:
            self.values = card.values()
            return

        for i, hand_value in enumerate(self.values[:]):
            if len(card.values()) == 2:
                self.values += [hand_value + card.values()[1]]
            self.values[i] += card.values()[0]

    def can_hit(self):
        return min(self.values) < 21

    def can_stand(self):
        return min(self.values) < 21

    def can_double(self):
        return len(self.cards) == 2

    def can_split(self):
        if len(self.cards) != 2:
            return False
        if self.cards[0].value == self.cards[1].value:
            return True
        if self.values == [20]:
            return True

    def can_fold(self):
        return True

    def get_options(self):
        return [option for option in [
            "Hit" if self.can_hit() else "",
            "Stand" if self.can_stand() else "",
            "Double" if self.can_double() else "",
            "Split" if self.can_split() else "",
            "Fold" if self.can_fold() else ""
        ] if option != ""]


class DealerHand(Hand):
    def __str__(self):
        return "cards: {} + ?\n".format(self.cards[0])


if __name__ == '__main__':
    # Card Class Test
    k_h = Card("Hearts", "King")
    a_c = Card("Clubs", "Ace")
    _6_c = Card("Spades", "6")
    _6_d = Card("Diamonds", "6")
    print("Cards print correctly: {}, {}, {}, {}".format(
        k_h, a_c, _6_c, _6_d))
    print(k_h.values())
    print(a_c.values())
    print(_6_c.values())
    print(_6_d.values())

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

    # Hand Class Test
    print("-" * 20)
    hand = Hand()
    fail_hand = Hand()
    hand.add_card(_6_c)
    hand.add_card(_6_d)
    fail_hand.add_card(k_h)
    fail_hand.add_card(a_c)
    fail_hand.add_card(k_h)
    print(hand.values)
    print(fail_hand.values)

    print("Hand hits:", hand.can_hit())
    print("Fail hits:", fail_hand.can_hit())

    print("Hand stand:", hand.can_stand())
    print("Fail stands:", fail_hand.can_stand())

    print("Hand double:", hand.can_double())
    print("Fail double:", fail_hand.can_double())

    print(hand.can_split())

    dealer = DealerHand()

    dealer.add_card(a_c)
    dealer.add_card(k_h)
    print(dealer)
