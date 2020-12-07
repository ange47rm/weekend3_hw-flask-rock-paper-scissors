import random

if __name__ == "__main__":
    from player import Player

else:
    from app.models.player import Player


class Game ():
    def __init__ (self):
        self.name = "Rock Paper Scissors"
        self.winner = ''
        choices = ['rock', 'paper', 'scissors']
        self.player_2 = Player('Computer', random.choice(choices))

    def play (self, player_1):

        if player_1.choice == 'rock' and self.player_2.choice == 'scissors':
            self.winner = player_1.name
            return self.winner

        elif player_1.choice == 'scissors' and self.player_2.choice == 'paper':
            self.winner = player_1.name
            return self.winner

        elif player_1.choice == 'paper' and self.player_2.choice == 'rock':
            self.winner = player_1.name
            return self.winner

        elif player_1.choice == self.player_2.choice:
            self.winner = None
            return self.winner

        else:
            self.winner = self.player_2.name
            return self.winner

#  TESTS SETUP (tests passed)

# player_1 = Player ('Angelo', "Rock")
# new_game = Game ()
# new_game.play (player_1)
# print ("Player", player_1.name, "has chosen", player_1.choice.upper(), "and computer has picked", new_game.player_2.choice.upper(), "and the winner is", new_game.winner)