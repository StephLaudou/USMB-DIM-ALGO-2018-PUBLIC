# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Bounding Box
import numpy as np


#Average
def average_above_zero(tab):
    """
    brief : computs the average
    
    args : 
    tab : a list of numeric value
    
    Return :
        the computed average
    Raises : 
    Value error if no positive value  
    Value error if input tab is ot a list  
    
    """
    if not (isinstance(tab, list)):#on verifie si c'st bien une liste (eliminer les cas d'erreur)
        raise ValueError('Expected a list as Input')

    average = -99 
    
    valSum =0.0 #on le met en float
    nPositiveValues=0
    
   
    for val in tab:
        if val>0:
           valSum=valSum+float(val)
           nPositiveValues=nPositiveValues+1
 
    if nPositiveValues<= 0:
         raise ValueError('No positive values found')
    
    average= valSum/nPositiveValues
    return average


#Test fonction average    
#test_tab=[1,2,3,-8] #¯ decl liste
#moy=average_above_zero(test_tab)
#print('Positive valus average =')
#print(moy)# print reçoit un bloc quidoit être d etype homogène
#print('Positive valus average ='+str(moy)) # methode moche
#print('Positive valus average ={v}'.format(v=moy)) # v = mot clé


#Maximum value
def max_value(tab):
    """
    Brief : computes the maximum value
    
    Args : 
    tab : a list of numeric value
    
    Return :
        the maximum value of a table
    Raises : 
    Value error if input tab is ot a list
    Value error if input list is empty
    
    """
    if not (isinstance(tab, list)):#on vérifie si c'est bien une liste (éliminer les cas d'erreur)
        raise ValueError('Expected a list as Input')

    if len(tab)==0:
        raise ValueError('Expected not empty list as Input')
        
    maxValueIndex=0
    maxValue=tab[0]
    
    for index,val in enumerate(tab):
        if val>=maxValue:#sup ou egal pour avoir la dernière max value
            maxValue=val
            maxValueIndex=index
     
   
    return (maxValue,maxValueIndex)


#Tests fonction maximum value    
##test_tab=[1,2,3,15,9] #¯ decl liste
#resultMaxValue,resultIndex=max_value(test_tab)
#print(resultMaxValue)
#print(resultIndex)
#print(str(resultMaxValue)+ " " +str(resultIndex))
    

#Reverse a table
def reverse_table(tab):
    """
    Brief : reverse a list in place
    
    Args : 
    tab : a list of numeric value
    
    Return :
        the list reversed
    Raises : 
    Value error if input tab is ot a list
    
    """
    if not (isinstance(tab, list)):#on vérifie si c'est bien une liste (éliminer les cas d'erreur)
        raise ValueError('Expected a list as Input')
    maxIndex = len(tab)-1
    for i in range(len(tab)//2):
        valeurOrig = tab[i]     
        tab[i] = tab[maxIndex-i] #-1 car l indice commence à 0
        tab[maxIndex-i] = valeurOrig
    return tab


#Tests fonction maximum value    
#test_tab=[1,2,15,9] #¯ decl liste
#test_tab=[] #¯ decl liste
#print(reverse_table(test_tab))
    

#Bounding Box
def roi_bbox(image):
    """
    Brief : return an array which contains the coordinates of the bounding box of an image    
    
    Args : image : numpy array, 2D Matrix with binary values
    
    Return : numpy array which contains following coordinates  : top left, top right, bottom left, bottom right
        
    Raises : 
    
    
    """
    #coordonnées des points angle de la matrice / Initialisation avec la taille de l'image
    #valeur des points transposée pour que la boucle marche
    #Point en haut à gauche 
    xHG=len(image[0])-1#nb de colonnes à la première ligne POURQUOI -1 FIXME
    yHG=len(image)-1#nb de ligne de l'image
    #Point en bas à droite
    xBD=0#colonne
    yBD=0#ligne
    
    #je parcours les cases du tableau et analyse celles = 1 (si 1, elle appartient à l'image)
    for nlig in range(len(image)):
        for ncol in range (len(image[0])):
            if image[nlig][ncol] == 1:
                if nlig<yHG:
                    yHG=nlig
                if nlig>yBD:
                    yBD=nlig
                if ncol<xHG:
                    xHG=ncol
                if ncol>xBD:
                    xBD=ncol
    
    arrayCoordinates=np.array([[xHG,yHG],[xBD,yHG],[xHG,yBD],[xBD,yBD]])

    return arrayCoordinates

#Tests bounding box
#image = np.array([[0,0,0,0,0,0],[0,0,1,1,1,0],[0,0,1,1,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0]]) #¯ decl liste
#print(image)
#print(image[1][3])#valeur de la case du tableau à la 2eme ligne (1ere ligne =0) et 3eme colonne
#print(len(image[0]))# nb de colonnes de la ligne 1
#print(len(image))# nb de lignes de l'image
#print(roi_bbox(image))