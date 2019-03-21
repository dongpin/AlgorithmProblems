import unittest

from Python.BasicAlgorithm.Tree import *
from Python.Problems.BST_Iterator_173 import *

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

# Test Cases
def test_height():
    tree = create_sample_tree()
    iterator = BstIterator(tree.root)
    res = []
    while iterator.hasNext():
        res.append(iterator.next().data)
    assert res == [1, 2, 3, 4, 5, 6]
