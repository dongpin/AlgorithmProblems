import unittest

from BasicAlgorithm.Search import binary_search

def test_binary_search():
    assert binary_search([1,2,4,6,7,8], 6) == 3
    assert binary_search([1], 1) == 0
    assert binary_search([1,2,4], 6) == -1
    assert binary_search([], 6) == -1