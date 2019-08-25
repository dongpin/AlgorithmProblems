// 5. Longest Palindromic Substring

namespace Leetcode
{
    public partial class Algorithm
    {
        public static string FindLongestPalindromicSubstr(string s)
        {
            var result = string.Empty;
            var dp = new int[s.Length, s.Length];
            for (int i = s.Length - 1; i >= 0; i--)
            {
                for (int j = i; j < s.Length; j++)
                {
                    if (i == j)
                    {
                        dp[i, j] = 1;
                        result = result.Length == 0 ? s[i].ToString() : result;
                    }
                    else if (i + 1 == j && s[i] == s[j])
                    {
                        dp[i, j] = 2;
                        result = j - i + 1 > result.Length ? s.Substring(i, j - i + 1) : result;
                    }
                    else if (s[i] == s[j] && dp[i + 1, j - 1] > 0)
                    {
                        dp[i, j] = dp[i + 1, j - 1] + 2;
                        result = j - i + 1 > result.Length ? s.Substring(i, j - i + 1) : result;
                    }
                }

            }

            return result;
        }
    }
}