import unittest

from Python.BasicAlgorithm.Tree import TreeNode
from Python.BasicAlgorithm.Tree import BinaryTree

# Test Helpers
def create_sample_tree():
    tree = BinaryTree()
    root = TreeNode(1)
    tree.root = root
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
    return tree

# Test Cases
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

def test_preorder_traverse():
    tree = create_sample_tree()
    assert tree.preorder() == [1, 2, 4, 6, 3, 5]
    tree = BinaryTree()
    assert tree.preorder() == []

def test_inorder_traverse():
    tree = create_sample_tree()
    assert tree.inorder() == [6, 4, 2, 1, 5, 3]

def test_postorder_traverse():
    tree = create_sample_tree()
    assert tree.postorder() == [6, 4, 2, 5, 3, 1]