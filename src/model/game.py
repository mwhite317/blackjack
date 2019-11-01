import sys

from src.model.blackjack_players import *
from src.model.deck import *
from src.model.human_connections import SavePlayer


class Game:
    def __init__(self, human_player):
        self.human_player = human_player
        self.deck = Deck()
        self.players = [self.human_player]
        self.num_decks = 1
        for i in range(self.num_decks - 1):
            self.deck.add_deck_to_deck(Deck())

    def start(self):
        """
        Adds chips to human player if they start game with 0. Calls round class to begin round.

        :return: none
        """
        pronouns = {"M": "Mr.", "F": "Ms.", "X": "Mx."}
        if self.human_player.num_of_chips() == 0:
            print(
                "{} {}, It seems you don't have any chips with you. Don't worry we will buy you in..."
                "\ntransferring chips ...\n"
                    .format(pronouns.get(self.human_player.gender, "X"), self.human_player.last_name))
            self.human_player.add_chips(500)
            print(self.human_player.chip_string())
            self.shall_we_play()

        else:
            print("Welcome back {} {}, good to see you again."
                  .format(pronouns.get(self.human_player.gender, "X"), self.human_player.last_name))
            print(self.human_player.chip_string())
            self.shall_we_play()

        while self.human_player_left():
            rund = Round(self.deck, self.players)
            rund.start_round()
            self.cash_out()

    def human_player_left(self):
        """
        Checks if any human players are left in the round.

        :return: number  of human player left
        """
        return self.human_player.num_of_chips() > 0

    def shall_we_play(self):
        """
        Confirms if player wants to play. Provides an exit if the player wants to leave the game.

        :return: none
        """
        play_input = input("\nShall we play?\n" "1. yes\n" "2. no\n" ": ")

        while play_input not in "12":

            play_input = input("\nShall we play?\n" "1. yes\n" "2. no\n" ": ")
        if play_input == "1":
            pass

        elif play_input == "2":
            print("\nSaving...")
            print("Please remember to type in same first name, last name, and gender from the beginning of the "
                  "Gamgame to "
                  "access your account.")
            save = SavePlayer()
            save.save(self.human_player)
            pronouns = {"M": "Mr.", "F": "Ms.", "X": "Mx."}
            print("Goodbye {} {}, hope to see you soon."
                  .format(pronouns.get(self.human_player.gender, "X"), self.human_player.last_name))
            sys.exit()



    def cash_out(self):
        """
         Buys human players back in the game.

        :return: none
        """
        if self.human_player.num_of_chips() < 6:
            self.human_player.add_chips(250)
            print("It seems you do not have enough chips. Here is an additional 250 chips to keep you going.")
            print(self.human_player.chip_string())


class Round:
    def __init__(self, deck, players):
        self.deck = deck
        self.pot = 0
        self.dealer = Dealer("", "Dealer", "X")
        self.players = players + [self.dealer]
        self.human_player = players[0]
        self.human_bust = False
        self.player_continues = True
        self.dealer_continues = True
        self.option_functions = {
            "Hit": self.hit,
            "Double": self.double,
            "Split": self.split,
            "Stand": self.stand,
            "Fold": self.fold
        }

    def start_round(self):
        """
        Calls shuffle function. For each player, asks for buy in using calls buy_in function,
         then asks for bet using betting function.

        :return: none
        """
        self.shuffle()
        for p in self.players:
            self.buy_in(p)
        self.deal_cards()
        while self.player_continues:
            for p in self.players:
                self.betting(p)
        self.end_of_round()

    def deal_cards(self):
        """
        Deals two card to each player in the round.
        Note that each player receives one card before dealer gives a second.

        :return:  none
        """
        for p in self.players:
            p.take_card(self.deck.draw_card())

        for p in self.players:
            p.take_card(self.deck.draw_card())
        print("\nDealing Cards...\n")

    def shuffle(self):
        """
        Shuffles deck by calling Deck class in Deck file.

        :return: none
        """
        self.deck.shuffle_deck()
        print("Shuffling cards...\n")

    def options_string(self, options):
        """
        Formats the option menu. Adjust numbers depending on available options.

        :param options: refers to the options set in Hand class from Deck file.
        :return: the organised menu for player
        """
        output = "Please choose one...\n"
        i = 1
        for option in options:
            output += "{}. {}\n".format(i, option) if option != "" else ""
            i += 1 if option != "" else 0
        return output

    def betting(self, player):
        """
        Checks if player is human. Prints player's cards and dealer's first card for human player to see.
        Prints menu for player. Takes menu input from player.

        :param player:  player who is playing the round
        :return: none
        """
        if not player.is_human():
            return
        print(player.hand_string())
        print(self.dealer.hand_string())
        options = player.hand.get_options()

        if min(self.human_player.hand.values) < 22:
            while True:
                try:
                    choice_input = input(self.options_string(options) + ": ")
                    print("")

                    while int(choice_input) not in range(1, len(options) + 1):
                        choice_input = int(input("Error! " + self.options_string(options) + ": "))
                        print("")
                    break
                except:
                    pass

            choice = int(choice_input) - 1
            self.option_functions[options[choice]](player)
            return

        self.bust()

    def hit(self, player):
        """
        Player is given another card.

        :param player: player who is betting
        :return: the updated player's cards
        """
        player.take_card(self.deck.draw_card())
        print("Dealing a card...\n")
        self.player_continues = True

    def double(self, player):
        """
        Player pays the additional same amount paid in buy_in function. Player is given another card and is prevented
        to bet afterwards.

        :param player: player who is betting
        :return: none
        """
        self.pot += player.bets
        self.player_continues = False
        print("Doubling ...\n"
              "Transferring {} chips into the pot...\n".format(player.bets))
        player.bet_chips(player.bets)
        player.take_card(self.deck.draw_card())

    def split(self, player):
        # TODO implement split
        pass

    def stand(self, player):
        """
        Prevents player to continue betting.

        :param player: player who is betting
        :return: none
        """
        self.player_continues = False
        print("You stand.")

    def fold(self, player):
        """
        Prevents the player to continue betting.

        :param player: player who is betting
        :return: none
        """
        self.player_continues = False
        self.human_bust = True
        print("FOLD\n")

    def bust(self):
        """
         Prevents the player and dealer to continue betting. Player loses automatically.

        :return: print statement
        """

        self.player_continues = False
        self.human_bust = True
        self.dealer_continues = False
        print("BUST!\n")

    def end_of_round(self):
        """
        Determines winner if player did not bust or fold. Adds pot amount to winning player and resets values.

        :return: none
        """
        if self.human_bust:
            print("Dealer wins.\n")
            self.dealer.add_chips(self.pot)
            print("Current amount: {}".format(self.human_player.num_of_chips()))

            self.reset()
            return

        self.dealer_turn()

        print("Results:")
        print(self.human_player.hand_string())
        print(self.dealer.hand_string())

        # determine winner
        self.dealer.hand.values = [value for value in self.dealer.hand.values if value <= 21] + [0]
        self.human_player.hand.values = [value for value in self.human_player.hand.values if value <= 21] + [0]
        if max(self.dealer.hand.values) < max(self.human_player.hand.values):
            print("You win!\n")
            self.human_player.add_chips(self.pot)
            print("{} chips awarded to you!".format(self.pot))
            print("Current amount: {}".format(self.human_player.num_of_chips()))

        elif max(self.dealer.hand.values) > max(self.human_player.hand.values):
            print("Dealer wins.\n")
            self.dealer.add_chips(self.pot)
            print("Current amount: {}".format(self.human_player.num_of_chips()))

        else:
            print("It's a tie.\n")
            self.pot = self.pot / 2
            self.human_player.add_chips(self.pot)
            print("{} chips awarded to you!".format(self.pot))
            self.dealer.add_chips(self.pot)
            print("Current amount: {}".format(self.human_player.num_of_chips()))

        self.reset()

    def dealer_turn(self):
        """
        Allows the dealer to hit, stand or fold
        :return:
        """
        self.dealer.bet_chips(self.pot)
        self.pot += self.pot
        print(self.human_player.hand_string())
        self.dealer.hand.__class__ = Hand
        print(self.dealer.hand_string())
        while self.dealer_continues:
            option = self.dealer.choose_option()
            if option == "Hit":
                self.dealer.take_card(self.deck.draw_card())
                print("Dealer hits...")
                print(self.dealer.hand_string())
            if option == "Bust":
                self.dealer_continues = False
                print("Dealer Busts.")
                print(self.dealer.hand_string())
            if option == "Stand":
                self.dealer_continues = False
                print("Dealer stands...")
                print(self.dealer.hand_string())

    def reset(self):
        """
        Resets hands, decks, and reshuffles deck.

        :return:
        """
        self.pot = 0
        self.reset_hands()
        self.deck = Deck()

    def reset_hands(self):
        """
        Resets each players hand.

        :return: none
        """
        for player in self.players:
            player.reset_hand()

    def buy_in(self, player):
        """
        Player buys in.
        Restrictions: must be more than 5 and within the account balance.
        Buy amount is then deducted from player account balance and added to pot.

        :param player: player who is betting
        :return: buy in amount
        """
        if not player.is_human():
            return
        print("-- Buy in is at least 5 chips --")
        while True:
            try:
                buyin = input("Enter your bet (or q to quit): ")
                if buyin in "qQ":
                    self.saving_game()
                    sys.exit()
                buyin = int(buyin)
                while buyin < 5 or buyin > player.num_of_chips():
                    if buyin < 5:
                        buyin = int(input("Bet too low! Enter your bet: "))
                    if buyin > player.num_of_chips():
                        buyin = int(input("Not enough funds! Enter your bet: "))
                break
            except ValueError:
                pass

        self.pot += buyin
        player.bet_chips(buyin)

    def saving_game(self):
        """
        Allows player to continue from where the ended.

        :return: none
        """
        pronouns = {"M": "Mr.", "F": "Ms.", "X": "Mx."}

        print("Saving...")
        print("Please remember to type in same first name, last name, and gender from the beginning of the game to "
              "access your account.")
        save = SavePlayer()
        save.save(self.human_player)
        print("Goodbye {} {}, hope to see you soon."
              .format(pronouns.get(self.human_player.gender, "X"), self.human_player.last_name))


if __name__ == '__main__':
    game = Game(Human("Mark", "White", "M", Chips(10)))
    game.start()
