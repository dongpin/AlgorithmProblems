import unittest

from Python.Problems.lc205_isomorphic_str import *
from Python.Problems.lc215_kth_largest_element_in_array import *
from Python.Problems.lc289_game_of_life import *

# 205


def test_is_isomorphic():
    assert is_isomorphic("egg", "add") == True
    assert is_isomorphic("foo", "bar") == False
    assert is_isomorphic("paper", "title") == True

# 215


def test_find_kth_largest():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 3) == 4


# 289
def test_game_of_life():
    matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    game_of_life(matrix)
    assert matrix == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
