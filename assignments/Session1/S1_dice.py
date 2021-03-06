# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:43:28 2018

@author: Stephanie
"""

"""
    brief : dice game
    The winner is the first obtaining at least 100 points
    If the dice shows 1, the score does not increase
    
    args : 
    question : used in yes_no function : It is the question to be asked to the player
    
    Return :
    Winner and Scores
    
        
    Raises : 
    
    
    """
    
import random


def yes_no(question):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
     
    while True:
        choice = input(question).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
            print("Please respond with 'yes' or 'no'\n")



player=1  # 1=user, 2=computer // je commence par le player 1
userScore = 0
computerScore = 0
winScore=100
result=''
computerLimit=14
print("It is player's turn")

while (userScore<winScore and computerScore<winScore):    
    turn=True
    turnScore = 0      
     
    while turn == True:#on commence un tour
        dice=random.randint(1,6)#on lance le dé.
        print("Roll the dice: {}".format(dice))
        if dice != 1:
            turnScore = turnScore + dice
            if player == 1:#si c'est le tour du user   
                answer = yes_no('Do you want to continue? ({})'.format(turnScore))
                if answer == True:# le joueur a dit qu'il voulait continuer
                    turn=True#le tour continue
                else:
                   userScore = userScore+turnScore
                   turn=False
                   
                 
            else:#si c'est le tour du computer                         
                if turnScore < computerLimit and (winScore-computerScore-turnScore)>0:
                    turn=True
                else:
                    computerScore = computerScore+turnScore
                    turn=False
        else:
            turn = False
    print('Computer Score : {}'.format(computerScore))
    print('Player Score : {}'.format(userScore))    
    
    if player == 2: 
        player = 1
        print("It is player's turn")
    else:
        player = 2
        print("It is computer's turn")
               
if userScore>computerScore:
    result = " Player wins : {} points to {} points for computer".format(userScore,computerScore)
else:
    result = "Computer wins : {} points to {} points for the player".format(computerScore,userScore)
print(result)





