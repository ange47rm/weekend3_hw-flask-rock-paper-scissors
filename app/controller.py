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
    return f"The winner is {new_game.winner}!"

