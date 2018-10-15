# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:43:28 2018

@author: Stephanie
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
print("Au tour du joueur")

while (userScore<winScore and computerScore<winScore):    
    turn=True
    turnScore = 0      
     
    while turn == True:#on commence un tour
        dice=random.randint(1,6)#on lance le dé.
        print("Tirage de dé: {}".format(dice))
        if dice != 1:
            turnScore = turnScore + dice
            if player == 1:#si c'est le tour du user   
                answer = yes_no('Voulez-vous continuer? ({})'.format(turnScore))
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
    print('Points de ordinateur : {}'.format(computerScore))
    print('Points du joueur : {}'.format(userScore))    
    
    if player == 2: 
        player = 1
        print("Au tour du Joueur")
    else:
        player = 2
        print("Au tour de l'Ordinateur")
               
if userScore>computerScore:
    result = "Le joueur a gagné : {} points à {} points pour l'ordinateur".format(userScore,computerScore)
else:
    result = "L'ordinateur a gagné : {} points à {} points pour le joueur".format(computerScore,userScore)
print(result)





