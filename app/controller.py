from flask import render_template, request
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route ('/welcome')
def welcome():
    return render_template ('welcome.html')

@app.route ('/play', methods=['GET', 'POST'])
def play():
    player_name = request.form['name']
    player_choice = request.form['choice']
    player = Player (player_name, player_choice)
    new_game = Game ()
    new_game.play (player)
    print (request.form)
    return render_template ('index.html')







# @app.route ('/player_1/player_2')
# def play_game():
#     new_game = Game ()
#     new_game.play (player_1, player_2)
#     return f'The winner of the game is {new_game.winner}'