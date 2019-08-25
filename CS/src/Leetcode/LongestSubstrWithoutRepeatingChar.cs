// 3. Longest Substring without Repeating Characters

using System;
using System.Collections.Generic;

namespace Leetcode
{
    public partial class Algorithm
    {
        public static int FindLongestSubStrWithoutRepeatingChars(string s)
        {
            var result = 0;
            var chars = new HashSet<char>();
            var i = 0;
            var j = 0;
            while (i < s.Length && j < s.Length)
            {
                if (chars.Contains(s[j]))
                {
                    chars.Remove(s[i]);
                    i += 1;
                }
                else
                {
                    chars.Add(s[j]);
                    j += 1;
                    result = Math.Max(result, j - i);
                }
            }

            return result;
        }
    }
}