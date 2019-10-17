import os
import sys

myPath = os.path.dirname(os.path.abspath("../model"))
sys.path.insert(0, myPath + '/../')

from model.deck import Hand, Card

# Card Class Test
k_h = Card("Hearts", "King")
a_c = Card("Clubs", "Ace")
_6_c = Card("Spades", "6")
_6_d = Card("Diamonds", "6")
_9_ = Card("Diamond", "9")
_3_ = Card("Diamond", "3")


def test_hand():
    hand12 = Hand()
    hand12.add_card(_6_c)
    hand12.add_card(_6_d)

    assert hand12.can_hit()
