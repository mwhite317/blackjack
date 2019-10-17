import texts
from game import Game
from human_connections import (InitialisePlayer, SavePlayer)


def welcoming():
    """
    Prints welcome message.

    :return: none
    """
    print(texts.title)
    print("Welcome to Blackjack")
    print("Let's set up your user...\n")


def blackjack_welcome(player):
    """
    Formatted print statement to assign proper pronouns to gender.

    :param player: relies on player's answer to gender question
    :return: none.
    """
    print("\nGreat! Lets get started...")
    pronouns = {"M": "Mr.", "F": "Ms.", "X": "Mx."}

    print(
        "\nWelcome {} {} to blackjack. It may have been a while since you played, here are the basic rule...".format(
            pronouns.get(player.gender, "X"), player.last_name))


def blackjack_rule_display():
    """
    Prints rules of game.

    :return: none
    """
    print(texts.rules)


if __name__ == '__main__':
    welcoming()
    player_initialiser = InitialisePlayer()
    human_player = player_initialiser.initialise()

    saved_players = SavePlayer()
    key = human_player.first_name + human_player.last_name + human_player.gender
    if key in saved_players.players:
        human_player = saved_players.players[key]

    blackjack_welcome(human_player)
    blackjack_rule_display()

    game = Game(human_player)
    game.start()
