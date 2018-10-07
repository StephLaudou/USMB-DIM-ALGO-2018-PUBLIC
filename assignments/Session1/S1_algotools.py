# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

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
test_tab=[1,2,3,-8] #¯ decl liste
moy=average_above_zero(test_tab)
print('Positive valus average =')
print(moy)# print reçoit un bloc quidoit être d etype homogène
print('Positive valus average ='+str(moy)) # methode moche
print('Positive valus average ={v}'.format(v=moy)) # v = mot clé


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