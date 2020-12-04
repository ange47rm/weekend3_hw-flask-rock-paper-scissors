import random

if __name__ == "__main__":
    from player import Player

else:
    from app.models.player import Player


choices = ['rock', 'paper', 'scissors']

class Game ():
    def __init__ (self):
        self.name = "Rock Paper Scissors"
        self.winner = ''

    def play (self, player_1):

        player_2 = Player('Computer', random.choice(choices))

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

        else:
            self.winner = player_2.name
            return self.winner

#  TESTS SETUP (tests passed)

player_1 = Player ('Angelo', "Rock")
new_game = Game ()
new_game.play (player_1)
print (new_game.winner)
