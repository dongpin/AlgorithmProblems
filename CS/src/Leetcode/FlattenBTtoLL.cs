// 114. Flatten Binary Tree to Linked List

namespace Leetcode
{
    public partial class Algorithm
    {
        public static void FlattenBTtoLL(TreeNode root)
        {
            FlattenBTtoLLHelper(root);
        }

        private static TreeNode FlattenBTtoLLHelper(TreeNode root)
        {
            if (root == null)
                return null;
            if (root.Left == null && root.Right == null)
                return root;
            var leftTail = FlattenBTtoLLHelper(root.Left);
            var rightTail = FlattenBTtoLLHelper(root.Right);

            if (leftTail != null)
            {
                leftTail.Right = root.Right;
                root.Right = root.Left;
                root.Left = null;
            }

            return rightTail != null ? rightTail : leftTail;
        }
    }
}