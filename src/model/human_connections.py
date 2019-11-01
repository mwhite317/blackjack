import pickle

from src.model.blackjack_players import Human


class InitialisePlayer:
    def __init__(self):
        self.first_name = input("Please enter your first name: ").lower().capitalize().strip()
        self.last_name = input("Please enter your last name: ").lower().capitalize().strip()
        self.gender_input = self.get_gender_input()

    def initialise(self):
        """
        Creates the player (first name, last name, and gender).

        :return: new created player
        """
        return Human(self.first_name, self.last_name, self.gender_input)

    def get_gender_input(self):
        """
        Input Validation for gender input.

        :return: correct gender input
        """
        gender_input = input("Please enter your gender (type 'M', 'F' or 'X'): ").upper().strip()

        while True:
            if gender_input not in "MFX":
                gender_input = input("Not a valid answer...\nPlease enter your gender (type 'M', 'F' or 'X'): ")
            break
        return gender_input


class SavePlayer:
    def __init__(self):
        self.players = {}
        self.load()

    def save(self, player):
        """
        Allows player to be saved and reused at next login of the game.

        :param player: first name, last name and gender of logged in player
        :return: none
        """
        key = player.first_name + player.last_name + player.gender
        if key in self.players:
            self.players[key] = player
        else:
            self.players.update({key: player})
        with open("players.pickle", "wb") as file_handle:
            pickle.dump(self.players, file_handle)

    def load(self):
        """
        Reads the saved players file to check if current logged in player is a previous player.

        :return: none
        """
        try:
            with open("players.pickle", "rb") as file_handle:
                self.players = pickle.load(file_handle)
        except FileNotFoundError:
            self.players = {}
