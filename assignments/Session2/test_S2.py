# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:36:02 2018

@author: derobest
"""
import numpy as np
def test_basicTrue():
    """ one of the simplest test that does nothing except saying it works..."""
    assert True


#testing session 1 functions
def load_S1_script():
    """
        utility function that tris to load the script written along the first lesson
        @throws an ImportError exception if the script file does not exist
        @return the script as a loaded module
    """
    S1_script_filename='assignments/Session1/S1_algotools.py'
    import imp
    s1_algotools=imp.load_source('session_1_script', S1_script_filename)
    return  s1_algotools

    
def test_session1script_exists():
    try:
        load_S1_script()
        assert True
    #except  ImportError,e:
    except  ImportError:
        print('Expected script not found, carrefuly check the assignement instructions ')
        assert False

    """
    Test en indiquant le résultat dans le test
     """
def test_average():
    test_tab=[1,2,3,8]
    assert load_S1_script().average_above_zero(test_tab) == 3.5
    
    """
    Tests en utilisant la fonction intégrée mean à numpy.
    """
def check_S1_selective_average(testList):
    ##
    # utility function that asserts if load_S1_script().average_above_zero works fine
    # @param testList a list of values onto average_above_zero is applied
    # @test ensures the function returns the correct average value
    #another way to process the positive elements average to compare with
    positive_elements_float_array=np.array([i for i in testList if i > 0], dtype=float)
    reference_average_value=np.mean(positive_elements_float_array)
    assert load_S1_script().average_above_zero(testList) ==reference_average_value


def test_S1_selective_average_non_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >0
    check_S1_selective_average([1,2,3,4,-7])

def test_S1_selective_average_with_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >=0
    check_S1_selective_average([0,1,2,3,4,-7])

def test_S1_selective_average_with_negative_values():
    ##
    # @test validates average_above_zero works fine with integer values <=0
    #check_S1_selective_average([0,-7])
    check_S1_selective_average([8,7,-7])
    
    
def test_S1_selective_average_with_empty_list():
    ##
    # @test validates average_above_zero works fine with an empty list
    try:
        check_S1_selective_average([])
        assert False
    except ValueError:
        assert True
        

##max_value
    # @test validates max_value works  with input which is not a list
def test_S1_max_value_not_a_list():
    try:
        test_MVList=100
        load_S1_script().max_value(test_MVList)
        assert False
    except ValueError:
        assert True
        
def test_S1_max_value_empty_list():       
    # @test validates max_value works  with input which is an empty list
    try:
        test_MVList=[]
        load_S1_script().max_value(test_MVList)
        assert False
    except ValueError:
        assert True
        
def test_S1_max_value_standard_list():   
    # @test validates max_value works  with input which is an empty list
    test_MVList=[1,2,3,15,9]
    assert load_S1_script().max_value(test_MVList) == (15,3)
    
def test_S1_max_value_negative_value():   
    # @test validates max_value works  with input which is an empty list
    test_MVList=[1,2,-100,15,9]
    assert load_S1_script().max_value(test_MVList) == (15,3)
    
##Reverse_table
def test_S1_revertTable_empty():
    testList=[]
    assert testList==load_S1_script().reverse_table(testList)
    
def test_S1_revertTable_singleElement():
    testList=[1]
    assert testList==load_S1_script().reverse_table(testList)
    
def test_S1_revertTable_evenElement():###################################################
    testList=[1,2]
    #import copy
    #testList_copy=copy.deepcopy(testList)
    #print('reverseTable:{inL}=>{out}'.format(inL=testList_copy,out=load_S1_script().reverse_table(testList))) 
    assert[2,1]==load_S1_script().reverse_table(testList)
    
def test_S1_revertTable_oddElement():
    testList=[1,2,3]  
    assert[3,2,1]==load_S1_script().reverse_table(testList)

def test_S1_revertTable_error_list():
    try:
        testList='a';
        load_S1_script().reverse_table(testList)
        assert False
    except ValueError:
        assert True

##roi_box
def test_S1_roiBBox_regular():
    inputMat=np.zeros((5,6),dtype=np.bool)
    inputMat[2:4,3:5]=np.ones((2,2),dtype=np.bool)
#    assert (load_S1_script().roi_bbox(inputMat)==[[2,3],[2,4],[3,3],[3,4]])
    np.testing.assert_array_equal(load_S1_script().roi_bbox(inputMat), [[2,3],[2,4],[3,3],[3,4]])


##fill_sparse
def test_S1_RandomFillSparse_regular():    
    matrix = np.array([["","","","","",""],["","","","","",""],["","","","","",""]])
    k=4
    randomX=load_S1_script().random_fill_sparse(matrix,k)
    
    cpt=0
    for nlig in range(len(randomX)):
            for ncol in range (len(randomX[0])):
                if randomX[nlig][ncol] == 'X':
                    cpt+= 1
    assert cpt==k


##remove_whiteSpace
def test_S1_RemoveWhiteSpace_regular():    
    word = 'st ri ng'
    assert 'string'==load_S1_script().remove_whitespace(word)


#shuffle
def test_S1_Shuffle():
    list= ["pomme","pêche","poire","abricot"]
    shuffledList = load_S1_script().remove_whitespace(list)
    assert len(list)==len(shuffledList)


def test_S1_SortSelective():
    list=[10,15,7,1,3,3,9]
    expectedSortedList=[1,3,3,7,9,10,15]
    assert expectedSortedList==load_S1_script().sort_selective(list)
    
def test_S1_SortBubble():
    list=[10,15,7,1,3,3,9]
    expectedSortedList=[1,3,3,7,9,10,15]
    assert expectedSortedList==load_S1_script().sort_bubble(list)



        



    


    
    
    



    
    



