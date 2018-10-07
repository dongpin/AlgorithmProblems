# Node for binary tree
#

from collections import namedtuple

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def height(self):
        def helper(node):
            if not node:
                return 0
            return max(helper(node.left), helper(node.right)) + 1
        return helper(self.root)

    def is_balanced(self):
        BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

        def check_balanced(tree):
            if not tree:
                return BalancedStatusWithHeight(True, -1)
            left_result = check_balanced(tree.left)
            if not left_result.balanced:
                return BalancedStatusWithHeight(False, 0)
            right_result = check_balanced(tree.right)
            if not right_result.balanced:
                return BalancedStatusWithHeight(False, 0)
            
            is_balanced = abs(left_result.height - right_result.height) <= 1
            height = max(left_result.height, right_result.height) + 1
            return BalancedStatusWithHeight(is_balanced, height)
        return check_balanced(self.root).balanced
    
    def is_symmetric(self, tree):
        pass
    
class BinarySearchTree(BinaryTree):
    def __init__(self):
        pass
    