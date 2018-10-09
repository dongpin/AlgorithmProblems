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
    
    def preorder(self):
        res = []
        def preorder_helper(node):
            if node:
                res.append(node.data)
                preorder_helper(node.left)
                preorder_helper(node.right)
        preorder_helper(self.root)
        return res
    
    def inorder(self):
        res = []
        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                res.append(node.data)
                inorder_helper(node.right)
        inorder_helper(self.root)
        return res
    
    def postorder(self):
        res = []
        def postorder_helper(node):
            if node:
                postorder_helper(node.left)
                postorder_helper(node.right)
                res.append(node.data)
        postorder_helper(self.root)
        return res
    
    def bfs(self):
        pass
    
    def dfs_iterative(self):
        pass
    
    def morris(self):
        pass
    
    def level_order_traverse(self):
        pass
    
    def serialize(self):
        pass
    
    def deserialize(self):
        pass

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

    def is_bst(self):
        pass
    
class BinarySearchTree(BinaryTree):
    def __init__(self):
        pass
    
    def delete(self, data):
        pass
    
    def insert(self, data):
        pass

# class BalancedSearchTree: # 2-3 search trees, red-black BSTs
