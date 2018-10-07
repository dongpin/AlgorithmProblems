import unittest

from BasicAlgorithm.Tree import TreeNode
from BasicAlgorithm.Tree import BinaryTree

def test_height():
    tree = BinaryTree()
    tree.root = None
    root = TreeNode(1)
    tree.root = root
    assert tree.height() == 1
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert tree.height() == 2
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    assert tree.height() == 4
    root.right.left = TreeNode(6)
    assert tree.height() == 4