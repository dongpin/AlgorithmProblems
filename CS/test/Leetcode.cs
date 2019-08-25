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
    }
}