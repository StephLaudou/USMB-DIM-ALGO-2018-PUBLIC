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
turnScore = 0
dice=0
winScore=7
result=''
answer=True
turn=True
turnScore = 0 
computerLimit=10

while (userScore<winScore and computerScore<winScore):    
    if player == 2 or (userScore==0 and computerScore==0):
        player = 1
    else:
        player = 2
    
    turn=True
    turnScore = 0      
     
    while turn == True:#on commence un tour
        dice=random.randint(1,6)#on lance le dé.
        #print(dice)
        if dice != 1:
            turnScore = turnScore + dice
            if player == 1:#si c'est le tour du user   
                answer = yes_no('Voulez-vous continuer?')
                if answer == True:# le joueur a dit qu'il voulait continuer
                    turn=True#le tour continue
                else:
                   userScore = userScore+turnScore
                   turn=False
                 
            else:#si c'est le tour du computer                         
                if turnScore < computerLimit :
                    turn=True
                else:
                    computerScore = computerScore+turnScore
                    turn=False
        else:
            turn =False
        
        
               
if userScore>computerScore:
    result = 'le joueur a gagné'
else:
    result = 'l ordinateur a gagné'
print(result)
print(userScore)
print(computerScore)



#print('Le joueur a '+str(userScore)+' points')
#print('L ordinateur a '+str(computerScore)+' points')         
#print('Points du joueur'.format(v=moy))            



