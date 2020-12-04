from flask import render_template, request
from app import app
from app.models.game import Game, choices
from app.models.player import Player

@app.route ('/')
def index():
    return render_template ('index.html')

@app.route ('/rock/scissors')
def play_game():
    game = Game ()
    game.play()
    return f'The'