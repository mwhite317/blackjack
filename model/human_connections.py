from blackjack_players import Human
import pickle


class InitialisePlayer:
    def __init__(self):
        self.first_name = input("Please enter your first name: ").lower().capitalize()
        self.last_name = input("Please enter your last name: ").lower().capitalize()
        self.gender_input = self.get_gender_input()

    def initialise(self):
        return Human(self.first_name, self.last_name, self.gender_input)

    def get_gender_input(self):
        gender_input = input("Please enter your gender (type 'M', 'F' or 'X'): ").upper()

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
        key = player.first_name + player.last_name + player.gender
        if key in self.players:
            print("Updating know player")
            self.players[key] = player
        else:
            print("Saving new player")
            self.players.update({key: player})
        with open("players.pickle", "wb") as file_handle:
            pickle.dump(self.players, file_handle)

    def load(self):
        try:
            with open("players.pickle", "rb") as file_handle:
                self.players = pickle.load(file_handle)
        except FileNotFoundError:
            self.players = {}
