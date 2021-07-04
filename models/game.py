# Below I have created a Game class along with an if elif statement which determines the game's outcome
# depending on the player's choice.

class Game:
   def __init__(self,):
      pass
# line 8 = Import player class file into this game file from the directory named models
from models.player import *

def decision(player_1, player_2):
   if player_1.choice == player_2.choice:
    return None
    
   elif player_1.choice == "rock" and player_2.choice == "paper":
    return player_2
   elif player_1.choice == "rock" and player_2.choice == "scissors":
    return player_1
   elif player_1.choice == "paper" and player_2.choice == "scissors":
    return player_2
   elif player_1.choice == "paper" and player_2.choice == "rock":
    return player_1
   elif player_1.choice == "scissors" and player_2.choice == "rock":
    return player_2
   elif player_1.choice == "scissors" and player_2.choice == "paper":
    return player_1
    


  

        
    
        

    
