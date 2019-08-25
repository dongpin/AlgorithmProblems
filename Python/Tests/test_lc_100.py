import unittest

from Python.BasicAlgorithm.Tree import *
from Python.Problems.lc173_bst_iterator import *
from Python.Problems.lc167_two_sum_II import *

def test_lc167_two_sum_II():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

# Test Helpers
def create_sample_tree():
    tree = BinaryTree()
    root = TreeNode(5)
    tree.root = root
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.left.left.right = TreeNode(2)
    return tree

# 167
def test_two_sum_II():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

# 173
def test_bst_iterator():
    tree = create_sample_tree()
    iterator = BstIterator(tree.root)
    res = []
    while iterator.hasNext():
        res.append(iterator.next().data)
    assert res == [1, 2, 3, 4, 5, 6]
