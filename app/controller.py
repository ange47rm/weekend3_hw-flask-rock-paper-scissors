from flask import render_template, request
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route ('/')
def landing():
    return "Test"

@app.route ('/welcome')
def welcome():
    return render_template ('welcome.html')

@app.route ('/game')
def game():
    return render_template ('index.html')

@app.route ('/game/play', methods=['POST'])
def play():
    player_name = request.form['name']
    player_choice = request.form['choice']
    player = Player (player_name, player_choice)
    new_game = Game ()
    new_game.play (player)
    print (request.form)
    if player.choice == new_game.player_2.choice:
        return f"Both {player.name} and Computer have chosen {player.choice.upper()} so it's a draw! Try again!"  
    else:
        return f"Player {player.name} has chosen {player.choice.upper()}, and Computer has chosen {new_game.player_2.choice.upper()} and the winner is {new_game.winner}!"



# print ("Player", player_1.name, "has chosen", player_1.choice, "and computer has picked", new_game.player_2.choice, "and the winner is", new_game.winner)