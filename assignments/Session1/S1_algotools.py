# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


import numpy as np

import random

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
#test_tab=[1,2,3,8] #¯ decl liste
#moy=average_above_zero(test_tab)
#print('Positive valus average =')
#print(moy)# print reçoit un bloc quidoit être d etype homogène
#print('Positive valus average ='+str(moy)) # methode moche
#print('Positive valus average ={v}'.format(v=moy)) # v = mot clé

      
#def average_above_zero_numpy(tab):     
#    tab_np=np.array(tab)# conversion d el aliste en array numpy
#    positive_values=tab_np[np.where(tab_np>0)]
#    positive_values_mean=np.mean(positive_values)
#    print(positive_values_mean)
         
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


def random_fill_sparse(table,K):
    """
    brief : fills in a matrix randomly
    
    args : 
        matrix : empty matrix
        K : number of cells to be filled in
    
    Return :
        the matrix (numpy array) filled in with "X" values (char)
    
    Raises : 
        K must be smaller than the table size
        The table must contain Char type values 
    """

    i=0
    y=0#matrix lines
    x=0#matrix column
    
    if K>table.size:
         raise ValueError('K is out of bounds')
         
    if table.dtype != "<U1":
         raise ValueError('The array type must be Char')
      
    
    while i < K:
        y=random.randrange(0,len(table)-1)
        x=random.randrange(0,len(table[0])-1)
        if table[y][x] != "X":
            table[y][x] = "X"
            i=i+1
    return table
        
        
      
    
#Tests nandom filling
#matrix = np.array([["","","","","",""],["","","","","",""],["","","","","",""]])
#matrix = np.array([[0,0,0,0,0,0],[0,0,1,1,1,0],[0,0,1,1,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0]])
#testLen = len(matrix)
#print(testLen)
#testCount = matrix.size
#print(testCount)
#randomX=random_fill_sparse(matrix,4)
#print(matrix.astype(str))
#print(matrix.dtype)
#print(matrix)
#randomX=random_fill_sparse(matrix,20)
#print(randomX)

def remove_whitespace(table):
    """
    brief : remove whitespace characters in a string
    
    args : 
        table: string
        
        Return : string without whitespace
        
    
    Raises : 
        
        
    """
    i = 0
    while i < len(table):
        if table[i] == " ":
            if i+1 < len(table):
                table = table[:i] + table[i+1:]
            else:
                table = table[:i]
        else:
            i += 1
    
    
    return table

#str = 'st ri ng'
#for i in range(0, len(str)):
#    if str[i] == " ":
#        print("toto")
    
#str = '    s t r i n g     '
#str = 'string '
#print('*'+remove_whitespace(str)+'*')