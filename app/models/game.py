
from player import Player

choices = ['rock', 'paper', 'scissors']

class Game ():
    def __init__ (self):
        self.name = "Rock Paper Scissors"
        self.winner = ''

    def play (self, player_1, player_2):

        if player_1.choice == 'rock' and player_2.choice == 'scissors':
            self.winner = player_1.name
            return self.winner

        elif player_1.choice == 'scissors' and player_2.choice == 'paper':
            self.winner = player_1.name
            return self.winner

        elif player_1.choice == 'paper' and player_2.choice == 'rock':
            self.winner = player_1.name
            return self.winner

        elif player_1.choice == player_2.choice:
            self.winner = None
            return self.winner

        elif player_1.choice or player_2.choice not in choices:
            self.winner = None
            print (f"One or both player's choices not valid. Choose between 'rock', 'paper' or 'scissors'.")

        else:
            self.winner = player_2.name
            return self.winner

player_1 = Player ('Angelo', "Rock")
player_2 = Player ('Richard', "Papser")
new_game = Game ()
new_game.play (player_1, player_2)
print (new_game.winner)
