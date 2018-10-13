import unittest

from Python.BasicAlgorithm.Sorting import Sorting

def test_bubble_sort():
    s = Sorting()
    assert s.bubble_sort([]) == []
    assert s.bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert s.bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert s.bubble_sort([6, 2, 11, 4, 5, 99, 22, 1]) == [1, 2, 4, 5, 6, 11, 22, 99]

def test_heap_sort():
    s = Sorting()
    assert s.heap_sort([]) == []
    assert s.heap_sort([1, 2, 3]) == [1, 2, 3]
    assert s.heap_sort([3, 2, 1]) == [1, 2, 3]
    assert s.heap_sort([6, 2, 11, 4, 5, 99, 22, 1]) == [1, 2, 4, 5, 6, 11, 22, 99]