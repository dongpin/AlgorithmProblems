import unittest

from Python.Problems.lc524_longest_word_in_dict_thru_deleting import *

# 524
def test_find_longest_word():
    assert find_longest_word("abpcplea", ["ale","apple","monkey","plea"]) == "apple"