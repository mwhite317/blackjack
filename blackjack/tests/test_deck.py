import unittest

from deck import Hand, Card, DealerHand


class TestCard(unittest.TestCase):
    def setUp(self):
        self.k_h = Card("Hearts", "King")
        self.a_c = Card("Clubs", "Ace")
        self._6_s = Card("Spades", "6")
        self._6_d = Card("Diamonds", "6")
        self._9_ = Card("Diamond", "9")
        self._3_ = Card("Diamond", "3")


class TestInitCard(TestCard):
    def test_suit(self):
        self.assertEqual(self._6_d.suit, "Diamonds")
        self.assertEqual(self._6_s.suit, "Spades")
        self.assertEqual(self.k_h.suit, "Hearts")
        self.assertEqual(self.a_c.suit, "Clubs")
        self.assertEqual(self._9_.suit, "Diamond")
        self.assertEqual(self._3_.suit, "Diamond")

    def test_val(self):
        self.assertEqual(self._6_d.value, "6")
        self.assertEqual(self._6_s.value, "6")
        self.assertEqual(self.k_h.value, "King")
        self.assertEqual(self.a_c.value, "Ace")
        self.assertEqual(self._9_.value, "9")
        self.assertEqual(self._3_.value, "3")

    def test_special_value(self):
        self.assertEqual(self.k_h.values(), [10])
        self.assertEqual(self.a_c.values(), [1, 11])


class TestHand(TestCard):
    hand12 = Hand()
    hand21 = Hand()
    hand30 = Hand()

    def test_add_card(self):
        self.assertEqual(self.hand30.add_card(self.k_h), None)
        self.assertEqual(self.hand30.add_card(self.k_h), None)
        self.assertEqual(self.hand30.add_card(self.k_h), None)

        self.assertEqual(self.hand21.add_card(self._9_), None)
        self.assertEqual(self.hand21.add_card(self._9_), None)
        self.assertEqual(self.hand21.add_card(self._3_), None)

        self.assertEqual(self.hand12.add_card(self._6_s), None)
        self.assertEqual(self.hand12.add_card(self._6_d), None)

    def test_value_string(self):
        self.assertEqual(self.hand12.value_string(), "Count: 12\n")
        self.assertEqual(self.hand21.value_string(), "Count: 21\n")
        self.assertEqual(self.hand30.value_string(), "Count: 30\n")

    def test_can_hit(self):
        self.assertEqual(self.hand12.can_hit(), True)
        self.assertEqual(self.hand21.can_hit(), False)
        self.assertEqual(self.hand30.can_hit(), False)

    def test_can_stand(self):
        self.assertEqual(self.hand12.can_stand(), True)
        self.assertEqual(self.hand21.can_stand(), True)
        self.assertEqual(self.hand30.can_stand(), False)

    def test_can_double(self):
        self.assertEqual(self.hand12.can_double(), True)
        self.assertEqual(self.hand21.can_double(), False)
        self.assertEqual(self.hand30.can_double(), False)

    def test_can_split(self):
        self.assertEqual(self.hand12.can_split(), True)
        self.assertEqual(self.hand21.can_split(), False)
        self.assertEqual(self.hand30.can_split(), False)

    def test_can_split(self):
        self.assertEqual(self.hand12.can_stand(), True)
        self.assertEqual(self.hand21.can_stand(), True)
        self.assertEqual(self.hand30.can_stand(), False)

    def test_can_split(self):
        self.assertEqual(self.hand12.can_fold(), True)
        self.assertEqual(self.hand21.can_fold(), True)
        self.assertEqual(self.hand30.can_fold(), True)


class DealerHand(TestCard):
    dealer = DealerHand()

    def test_add_card(self):
        self.assertEqual(self.dealer.add_card(self.k_h), None)
        self.assertEqual(self.dealer.add_card(self.a_c), None)

    def test_value_string(self):
        self.assertEqual(self.dealer.value_string(), "Count: 10\n")


if __name__ == '__main__':
    unittest.main()
