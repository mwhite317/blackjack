import text_rules
from blackjack_players import Player


class InitialisePlayer:
    def welcoming(self):
        """
        Prints welcome message.

        :return: none
        """
        print("Welcome to Blackjack")
        print("Let's set up your user...\n")

    def player_set_up(self):
        """
        Gains player's...
            first name.
            last name.
            gender.


        :return: none
        """
        first_name_input = input("Please enter your first name: ").lower()
        last_name_input = input("Please enter your last name: ").lower()

        gender_input = input("Please enter your gender (type 'M', 'F' or 'X'): ")
        gender_input = gender_input.upper()
        while True:
            if gender_input not in "MFX":
                gender_input = input("Not a valid answer...\nPlease enter your gender (type 'M', 'F' or 'X'): ")
            break

        # TODO
        # human_player = Player(...values...)

        # TODO refactor into function
        def difficulty_input():
            """
            Ask for player's dealer difficulty rating.
            If input is not from menu answer, will ask again

            :return: none,
            """
            user_input = input("Please select the difficulty of dealer:\n"
                               "1. easy\n"
                               "2. medium\n"
                               "3. hard\n"
                               ": ")
            while True:
                if user_input == "1":
                    break
                if user_input == "2":
                    break
                if user_input == "3":
                    break
                else:
                    user_input = input("Not a valid answer...\nPlease select the difficulty of dealer:\n"
                                       "1. easy\n"
                                       "2. medium\n"
                                       "3. hard\n"
                                       ": ")


    # TODO
    # aiPlayerInput = int(aiPlayerInput)
    # for i in range(aiPlayerInput):
    #   players += [EasyPlayer(...values...)]

    print("\nGreat! Lets get started...")

    def blackjack_welcome(self, players):
        """
        Formatted print statement to assign proper pronouns to gender.

        :param players: relies on player's answer to gender question
        :return: none.
        """
        pronouns = {"M": "Mr.", "F": "Ms.", "X": "Mx."}
        for player in players:
            print(
                "\nWelcome {} {} to blackjack. It may have been a while since you played, here are the basic rule:\n"
                    .format(pronouns.get(player.gender, "X"), player.last_name))

    def blackjack_rule_display(self):
        """
        Prints rules of game.

        :return: none
        """
        print(text_rules)

# if __name__ == '__main__':
#     players = player_set_up()
#
#     # players =[ Player("M", "W", "M", 1, 2)]
#     blackjack_welcome(players)
#     rule = blackjack_rule_display()
#
#     game = Game(players)
#     game.start()
