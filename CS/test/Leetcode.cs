using NUnit.Framework;

namespace Tests.LC
{
    using Leetcode;

    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void TwoSum()
        {
            var arr = new int[] { 2, 7, 11, 15 };
            var expected = new int[] { 0, 1 };
            Assert.AreEqual(expected, Algorithm.TwoSum(arr, 9));
        }

        [Test]
        public void LongestSubstrWithoutRepeatingChars()
        {
            Assert.AreEqual(3, Algorithm.FindLongestSubStrWithoutRepeatingChars("abcabcbb"));
        }

        [Test]
        public void LongestPalindromicSubstr()
        {
            Assert.AreEqual("aba", Algorithm.FindLongestPalindromicSubstr("babad"));
            Assert.AreEqual("bb", Algorithm.FindLongestPalindromicSubstr("cbbd"));
        }

        [Test]
        public void NumOfIslands()
        {
            var testGrid1 = new char[][]
            {
                new char[] {'1', '1', '1', '1', '0'},
                new char[] {'1', '1', '0', '1', '0'},
                new char[] {'1', '1', '0', '0', '0'},
                new char[] {'0', '0', '0', '0', '0'}
            };

            Assert.AreEqual(1, Algorithm.CountNumOfIslands(testGrid1));

            var testGrid2 = new char[][]
            {
                new char[] {'1', '1', '0', '0', '0'},
                new char[] {'1', '1', '0', '0', '0'},
                new char[] {'0', '0', '1', '0', '0'},
                new char[] {'0', '0', '0', '1', '1'}
            };

            Assert.AreEqual(3, Algorithm.CountNumOfIslands(testGrid2));

        }

        [Test]
        public void FlattenBinaryTree()
        {
            var root = new TreeNode(1);
            root.Left = new TreeNode(2);
            root.Right = new TreeNode(3);

            Algorithm.FlattenBTtoLL(root);
            Assert.AreEqual(null, root.Left);
            Assert.AreEqual(2, root.Right.Val);
            Assert.AreEqual(null, root.Right.Left);
            Assert.AreEqual(3, root.Right.Right.Val);
            Assert.AreEqual(null, root.Right.Right.Left);
        }
    }
}