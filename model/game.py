from deck import *
from blackjack_players import *


# a list of Player

class Game:
    def __init__(self, players):
        self.human_player = Human("John", "Doe", "M", Chips(500))
        self.deck = Deck()
        self.players = [self.human_player]
        self.num_decks = 1
        for i in range(self.num_decks - 1):
            self.deck.add_deck_to_deck(Deck())

    def start(self):
        if self.human_player.num_of_chips() == 0:
            print(
                "It seems you don't have any chips with you. Don't worry we will buy you in..."
                "\ntransferring chips ...")
            self.human_player.add_chips(500)
            print(self.human_player.num_of_chips())

        while self.human_player_left():
            round = Round(self.deck, self.players)
            round.start_round()

    def human_player_left(self):
        return any(p.is_human() for p in self.players)

    # TODO end method
    # save players to file
    # print end of game messages

    def shall_we_play(self):
        play_input = input("Shall we play?\n" "1. yes\n" "2. no\n" ": ")
        if play_input == "1":
            pass
            # round = Round()
            # start round
        else:
            # quit
            pass


class Round:
    def __init__(self, deck, players):
        self.deck = deck
        self.pot = 0
        self.dealer = Dealer("", "Dealer", "X")
        self.players = players + [self.dealer]

        self.option_functions = {
            "Hit": self.hit,
            "Double": self.double,
            "Split": self.split,
            "Stand": self.stand,
            "Fold": self.fold
        }

    def start_round(self):
        self.shuffle()
        for p in self.players:
            self.buy_in(p)
        self.deal_cards()
        for p in self.players:
            self.betting(p)

    def deal_cards(self):
        for p in self.players:
            p.take_card(self.deck.draw_card())

        for p in self.players:
            p.take_card(self.deck.draw_card())
        print("\nDealing Cards...\n")

    def shuffle(self):
        self.deck.shuffle_deck()
        print("Shuffling cards...\n")

    def options_string(self, options):
        output = "Please choose one...\n"
        i = 1
        for option in options:
            output += "{}. {}\n".format(i, option) if option != "" else ""
            i += 1 if option != "" else 0
        return output

    def betting(self, player):
        if not player.is_human():
            return
        print(player.hand_string())
        print(self.dealer.hand_string())
        options = player.hand.get_options()

        choice_input = input(self.options_string(options) + ": ")
        print("")

        choice = int(choice_input) - 1
        self.option_functions[options[choice]](player)

    def hit(self, player):
        player.take_card(self.deck.draw_card())
        print("Dealing a card...\n")
        print(player.hand_string())

    def double(self, player):
        self.pot += player.bets
        print("Doubling ...\n"
              "Transferring {} chips into the pot...\n".format(player.bets))
        player.bet_chips(player.bets)
        player.take_card(self.deck.draw_card())
        print(player.hand_string())

    def split(self, player):
        # TODO implement split
        pass

    def stand(self, player):
        print("STANDING")
        print(player.hand_string())

    def fold(self, player):
        print("FOLD\n")

    def after_bet(self):
        for player in self.players:
            if player.chips < 10:
                for ai_player in player:
                    if ai_player != human_player:
                        print("{} has cashed out.".format(ai_player))
                        del ai_player
                    print(
                        "It seems you have lost your chips. I will buy you back in!"
                    )
                    chips.total += 250
            print("No one has cashed out yet.")

    def end_of_round(self):
        # give winning player the pot's chips
        # reset hands
        # put hands back in the deck
        pass

    # I know what players there are
    def reset_hands(self):
        for player in self.players:
            player.reset_hand()

    def buy_in(self, player):
        if not player.is_human():
            return
        print("-- Buy in is at least 5 chips --")
        while True:
            try:
                buyin = int(input("Enter your bet: "))
                while buyin < 5 or buyin > player.num_of_chips():
                    if buyin < 5:
                        buyin = int(input("Bet too low! Enter your bet: "))
                    if buyin > player.num_of_chips():
                        buyin = int(input("Not enough funds! Enter your bet: "))
                break
            except:
                pass

        self.pot += buyin
        player.bet_chips(buyin)


# starting a round
# at the start of each round reset their hands to be empty
# at the end of each round, get their cards/return their hands

if __name__ == '__main__':
    print(
        "\n\n\nCONVERT DEALERHAND TO NORMAL HAND AFTER PLAYER FINISHES MOVE. END ROUND. PLAY MULTIPLE ROUNDS. DEAL WITH SPLIT\n\n\n")
    rnd = Round(Deck(), [Human("Mark", "White", "M")])
    rnd.start_round()