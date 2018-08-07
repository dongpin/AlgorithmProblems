# Test if a binary tree satisfies the BST property
#

from TreeNode import TreeNode

def is_BST(node):
    return is_BST_util(node, float('-inf'), float('inf'))

def is_BST_util(node, min_data, max_data):
    if node is None:
        return True
    
    if node.data < min_data or node.data > max_data:
        return False
    
    return is_BST_util(node.left, min_data, node.data) and is_BST_util(node.right, node.data, max_data)

def main():
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)

    print(is_BST(root))

if __name__ == '__main__':
    main()
