import unittest

from Python.BasicAlgorithm.Tree import *

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

def test_segment_tree():
    tree = SegmentTree([0, 2, 3, 4, 5])
    assert tree.query(1, 3) == 9
    tree.update(1, 2)
    assert tree.query(1, 3) == 11
    assert tree.query(0, 0) == 0
    assert tree.query(-1, -1) == 0
