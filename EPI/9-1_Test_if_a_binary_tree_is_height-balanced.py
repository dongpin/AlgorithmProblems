# 9.1 Test if a binary tree is height balanced
#

import collections
from TreeNode import TreeNode
    
def height(root):
    if root is None:
        return 0
    return max(height(root.left), root.right) + 1
    
def is_balanced(root):
    if root is None:
        return True

    l_height = height(root.left)
    r_height = height(root.right)

    if abs(l_height  - r_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False

# code on EPI book
def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        
        left = check_balanced(tree.left)
        if not left.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        right = check_balanced(tree.right)
        if not right.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        is_balanced = abs(left.height - right.height) <= 1
        height = max(left.height, right.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    
    return check_balanced(tree).balanced

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    print(height(root))
    print(is_balanced(root))

    print(is_balanced_binary_tree(root))

if __name__ == '__main__':
    main()
