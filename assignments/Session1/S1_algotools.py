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
    if not (isinstance(tab, list)):#on verifie si c'est bien une liste (eliminer les cas d'erreur)
        raise ValueError('Expected a list as Input')
    average = -99 
    
    valSum =0.0 #on le met en float
    nPositiveValues=0
    
   
    for val in tab:
        if not (val.dtype == np.float):
            raise ValueError('Expected a float type value')
        if val>0:
           valSum=valSum+float(val)
           nPositiveValues=nPositiveValues+1
 
    if nPositiveValues<= 0:
         raise ValueError('No positive values found')
    
    average= valSum/nPositiveValues
    return average


#Test fonction average    
#test_tab=[1,2,3,8] #¯ decl liste
#test_tab=[0,0]
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
#test_tab=[1,2,3,15,9] #¯ decl liste
#resultMaxValue,resultIndex=max_value(test_tab)
#print(resultMaxValue)
#print(resultIndex)
#print(str(resultMaxValue)+ " " +str(resultIndex))
#print(max_value(test_tab))
    

#Reverse a table
#-----------------VERSION CORRIGEE--------------------------------
def reverse_table(inputList):
    """
    basic function able to revert a list
    args:
        inputlist : the input list to be reverses
    return: the reversed list
    
    """
    #basic input data type check
    if not (isinstance(inputList, list)):#on vérifie si c'est bien une liste (éliminer les cas d'erreur)
        raise ValueError('Expected a list as Input')
    
    
    #revert a list
    listLen=len(inputList)
    loopMaxID=int(np.floor(listLen/2))
    listLen-=1 # si on envoie une liste vide on ne rentre jamais dans la boucle
    #loop over the half of the list
    
    #pb ici = range alloue la memoire pour toute la liste => pb si longue liste
    # => utiliser xrange si python2
    for idx in range(loopMaxID): #on utilise fonction floor de numpy pour avoir val entière
        element=inputList[listLen-idx]
        inputList[listLen-idx]=inputList[idx];
        inputList[idx]=element
    return inputList


#testList=[1,2]
#retour = reverse_table(testList)
#print(retour)
    
#TEST LISTE VIDE
#TEST LISTE 1 ELET
#TEST LISTE PAIRE et IMPAIRE
#Tests fonction maximum value    
#testList=[1,2,3,4] #¯ decl liste
#print('reverseTable: {inL}=>{out}'.format(inL=testList,out=reverse_table(testList)))
# pb de ce print il inverse la liste vant l'affichage (mm buffer ????)
# donc on fait

#import copy 
#testList_copy=copy.deepcopy(testList)
#print('reverseTable:{inL}=>{out}'.format(inL=testList_copy,out=reverse_table(testList)))
#print(reverse_table(testList))
#
###TEST
#def test_revertTable_empty():
#    testList=[]
#        assert testList==reverse_table(testList)
#    
#def test_revertTable_singleElement():
#    testList=[1]
#        assert testList==reverse_table(testList)
#    
#def test_revertTable_evenElement():
#    testList=[1,2]
#    import copy
#    testList_copy=copy.deepcopy(testList)
#    print('reverseTable:{inL}=>{out}'.format(inL=testList_copy,out=reverse_table(testList))) 
#    assert[2,1]==reverse_table(testList)
#    
#def test_revertTable_oddElement():
#    testList=[1,2,3]  
#    assert[3,2,1]==reverse_table(testList)


#----------------MA VERSION----------------------------------------
#def reverse_table(tab):
#    """
#    Brief : reverse a list in place
#    
#    Args : 
#    tab : a list of numeric value
#    
#    Return :
#        the list reversed
#    Raises : 
#    Value error if input tab is ot a list
#    
#    """
#    if not (isinstance(tab, list)):#on vérifie si c'est bien une liste (éliminer les cas d'erreur)
#        raise ValueError('Expected a list as Input')
#    maxIndex = len(tab)-1
#    for i in range(len(tab)//2):
#        valeurOrig = tab[i]     
#        tab[i] = tab[maxIndex-i] #-1 car l indice commence à 0
#        tab[maxIndex-i] = valeurOrig
#    return tab
#

#Tests fonction maximum value    
#test_tab=[1,2,15,9] #¯ decl liste
#test_tab=[] #¯ decl liste
#print(reverse_table(test_tab))
    

#Bounding Box
#-----------------VERSION CORRIGEE--------------------------------
def roi_bbox(inputMat):
    roi=None
    
    
    
    #basic input data type check
    if not (isinstance(inputMat, np.ndarray)):
        raise ValueError('Expected an array as Input')
    if not (inputMat.dtype == np.bool):
        raise ValueError('Expected input of type numpy.bool')
        
    lmin=inputMat.shape[0]
    lmax=0
    cmin=inputMat.shape[1]
    cmax=0
        
    for l in range(inputMat.shape[0]):# .shape donne le tuple
        for c in range(inputMat.shape[1]):
            if inputMat[l,c]:
                if l<lmin:
                    lmin=l
                if l>lmax:
                    lmax=l
                if c<cmin:
                    cmin=c
                if c>cmax:
                    cmax=c
    roi=[[lmin,cmin],
         [lmin,cmax],
         [lmax,cmin],
         [lmax,cmax]]
    return np.array(roi)



#inputMat=np.ones((5.6),dtype=np.bool) #permet de créer une matrice de binaire, 5 li 6 col ones = True
inputMat=np.zeros((5,6),dtype=np.bool) #permet de créer une matrice de binaire, 5 li 6 col zero= False
#fill some points within it
#inputMat[2.3]=True
#inputMat[2.4]=True
#OU
inputMat[2:4,3:5]=np.ones((2,2),dtype=np.bool) #on remplit avec des true en créant une nouvelle petite matrice
##print(inputMat.shape[0])#nb de ligne
##print(inputMat.shape[1])#nb de colonne
print('inputMat='+str(inputMat))
roi=roi_bbox(inputMat)
print('roi='+str(roi))


#Autre solution 
#linelist,collist = numpy.nonzero(inputMAt)#Autre solution possible en python => 1 seule boucle et on parcourt moins de ligne
#
#for nonnullitem on range(len(lienlist))::
#    c,l=(linelist[id],collist[id])
#    if c<cmin.....:
#Autre solution  
#4 boucles qu'on peut paralleliser    




#----------------MA VERSION----------------------------------------
#def roi_bbox(image):
#    """
#    Brief : return an array which contains the coordinates of the bounding box of an image    
#    
#    Args : image : numpy array, 2D Matrix with binary values
#    
#    Return : numpy array which contains following coordinates  : top left, top right, bottom left, bottom right
#        
#    Raises : 
#    
#    
#    """
#    #coordonnées des points angle de la matrice / Initialisation avec la taille de l'image
#    #valeur des points transposée pour que la boucle marche
#    #Point en haut à gauche 
#    xHG=len(image[0])-1#nb de colonnes à la première ligne POURQUOI -1 FIXME
#    yHG=len(image)-1#nb de ligne de l'image
#    #Point en bas à droite
#    xBD=0#colonne
#    yBD=0#ligne
#    
#    #je parcours les cases du tableau et analyse celles = 1 (si 1, elle appartient à l'image)
#    for nlig in range(len(image)):
#        for ncol in range (len(image[0])):
#            if image[nlig][ncol] == 1:
#                if nlig<yHG:
#                    yHG=nlig
#                if nlig>yBD:
#                    yBD=nlig
#                if ncol<xHG:
#                    xHG=ncol
#                if ncol>xBD:
#                    xBD=ncol
#    
#    arrayCoordinates=np.array([[xHG,yHG],[xBD,yHG],[xHG,yBD],[xBD,yBD]])
#
#    return arrayCoordinates

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
    

def shuffle(list_in):
    """
    brief : select once and only once items of a list
    
    args : 
        list
    
    Return : a new list with shuffled items
        
    
    Raises : 
        
        
    """
    
    list_out=[]
    i=0 #index list for random function
    
    while len(list) > 0:
        i=random.randint(0,len(list)-1)
        list_out.append(list[i])
        del list[i]
    
    return list_out

#list= ["pomme","pêche","poire","abricot"]
#print(shuffle(list))


def sort_selective(list):
    """
    brief : Sort a list with the selective strategy
    
    args : 
    list : a list of numeric value
    
    Return :
        Sorted list in ascending order
    Raises : 
 
    
    """
    iLastCompare = len(list)-1 #last position to be compared
    
    for iNotSorted in range(0,iLastCompare):# on ne traite pas le dernier indice
        iSmallest = iNotSorted
        
        for iSearch in range(iSmallest,len(list)):
            if list[iSmallest] > list[iSearch]:
                iSmallest = iSearch
    
        backUpValue = list[iNotSorted]
        list[iNotSorted] = list[iSmallest]
        list[iSmallest] = backUpValue

    return list

#list=[3,1]        
#list=[10,-15,7,1,3,3,9,12,4]
#list=[10,15,7,1,3,3,9,12,4]
#list=[]
#list=[9,12,4]
#print(sort_selective(list))
    

def sort_bubble(list):
    """
    brief : Sort a list with the bubble strategy
    
    args : 
    list : a list of numeric value
    
    Return :
        Sorted list in ascending order
    Raises : 
    
    """
               
    for iSortedRight in range(len(list),0,-1):
        for j in range(0,iSortedRight-1):
            if list[j]>list[j+1]:
                backUpValue = list[j]
                list[j] = list[j+1]
                list[j+1] = backUpValue
  
                
    return list

#list=[3,1]
#list=[1,2,3]
#list=[10,15,7,1,3,3,9,12]
#list=[10,15,7,1,3,3,9,12,4]
#list=[9,12,4]
#list=[1,0,-15,7,1,3,3,9,12,4]


#print(sort_bubble(list))









        