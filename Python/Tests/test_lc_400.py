import unittest

from Python.Problems.lc498_diagonal_traverse import *

# 498
def test_diagonal_traverse():
    assert diagonal_traverse([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
    assert diagonal_traverse_less_space([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
