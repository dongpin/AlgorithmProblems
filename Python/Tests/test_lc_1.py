import unittest

from Python.Problems.lc32_longest_valid_parentheses import *
from Python.Problems.lc56_merge_intervals import *
from Python.Problems.lc44_wildcard_matching import *

# 32
def test_longest_parentheses():
    assert find_longest_valid_parenthese(")()())") == 4

# 44
def test_wildcard_matching():
    assert is_wildcard_match("aa", "*") == True
    assert is_wildcard_match("cb", "?a") == False
    assert is_wildcard_match("adceb", "*a*b") == True
    assert is_wildcard_match("acdcb", "a*c?b") == False

# 56
def test_merge_intervals():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]