import unittest

from Python.Problems.lc633_sum_of_sq_numbers import *
from Python.Problems.lc680_valid_palindrome_II import *

# 633
def test_lc633():
    assert judge(5) == True

# 680
def test_valid_palindrome():
    assert valid_palindrome("abca") == True
