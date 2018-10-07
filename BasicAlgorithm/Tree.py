# Node for binary tree
#

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
        pass
    
    def is_symmetric(self, tree):
        pass
    
class BinarySearchTree(BinaryTree):
    def __init__(self):
        pass
    