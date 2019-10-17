from game import Game
from human_connections import InitialisePlayer, SavePlayer
from main import welcoming, blackjack_welcome, blackjack_rule_display


# @click.group()
def blackjack():
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


if __name__ == '__main__':
    blackjack()
