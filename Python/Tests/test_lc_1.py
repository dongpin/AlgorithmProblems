import unittest

from Python.Problems.lc32_longest_valid_parentheses import *
from Python.Problems.lc56_merge_intervals import *

# 32
def test_longest_parentheses():
    assert find_longest_valid_parenthese(")()())") == 4

# 56
def test_merge_intervals():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]