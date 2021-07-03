# line 2 = From the app package import the object named app
from app import app 
# line 5 = The flask framework is being asked to import the Flask python class datatype
# line 5 continued = The Flask function render_template is being called directly by the flask package
from flask import Flask, render_template, request, redirect
# line 7 = The Game class is being imported from the game.py file inside the directory named models
from models.game import *
#  line 9 = The Player class is being imported from the player.py file inside the directory named models
from models.player import *

@app.route("/")
def index():
    return render_template("index.html")

# 

@app.route("/<player_1_choice>")
def first_choice():
    # player_1 = Player("Player 1", player_1_choice)
    # return render_template("base.html", player_1=player_1)
    return render_template("base.html")

@app.route("/<player_1_choice>/<player_2_choice>")
def result(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    
    result = decision(player_1, player_2)


    return render_template("scissors.html", result=result)
    

