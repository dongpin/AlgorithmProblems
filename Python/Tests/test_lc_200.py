import unittest

from Python.Problems.lc215_kth_largest_element_in_array import *

# 215
def test_find_kth_largest():
    assert find_kth_largest([3,2,1,5,6,4], 3) == 4