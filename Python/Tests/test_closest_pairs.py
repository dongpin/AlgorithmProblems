import unittest

from Python.BasicAlgorithm.DC_ClosestPairs import *

def test_closest_pair_1D():
    data = [100*random.random() for i in range(10)]
    assert closest_pair_brute_force(data) == closest_pair_divide_and_conquer(data) 
    
'''
def test_closest_pair_2d():
    data_2d = [(100*random.random(), 100*random.random()) for i in range(10)]
    assert closest_pair_2d_brute_force(data_2d) == closest_pair_2d_divide_and_conquer(data_2d)
'''