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

def test_is_balanced():
    tree = BinaryTree()
    assert tree.is_balanced() == True
    root = TreeNode(1)
    tree.root = root
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    assert tree.is_balanced() == True
    root.left.left.left = TreeNode(5)
    root.right.left = TreeNode(6)
    assert tree.is_balanced() == False