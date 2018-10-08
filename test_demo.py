""" Basic introduction to unit testing with Python

@brief get started with python testing by looking at https://docs.pytest.org/en/latest/getting-started.html#getstarted. Note that any script to be ran within the python testing framework (pytest) should follow the standard test discovery rules (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
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



#import s1_algotools as algo

#algo.average_above_zeroaverage_above_zero()

#load the scripts to check
def test_session1script_exists():
    try:
        load_S1_script()
        assert True
    except  ImportError,e:
        print('Expected script not found, carrefuly check the assignement instructions ')
        assert False

def check_S1_selective_average(testList):
    ##
    # utility function that asserts if load_S1_script().average_above_zero works fine
    # @param testList a list of values onto average_above_zero is applied
    # @test ensures the function returns the correct average value
    import numpy as np
    #another way to process the positive elements average to compare with
    positive_elements_float_array=np.array([i for i in testList if i >= 0], dtype=float)
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
    check_S1_selective_average([0,-7])

def test_S1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with integer values <=0
    check_S1_selective_average(['ab','c'])

def test_S1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with an empty list
    try:
        check_S1_selective_average([])
        assert False
    except ValueError:
        assert True
