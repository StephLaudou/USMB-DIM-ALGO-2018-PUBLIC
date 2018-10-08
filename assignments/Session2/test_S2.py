# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:36:02 2018

@author: derobest
"""

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
    except  ImportError,e:
        print('Expected script not found, carrefuly check the assignement instructions ')
        assert False


#def test_average():
#    test_tab=[1,2,3,-8]
#    assert average_above_zero(test_tab) = 3.5