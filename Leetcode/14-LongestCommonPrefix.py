# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.

def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) < 1:
            return ""
        
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                return strs[0][:i]
    return strs[0]

if __name__ == '__main__':
    print(longest_common_prefix(["flower","flow","flight"]))
    print(longest_common_prefix(["flo","flow","floor"]))
    print(longest_common_prefix(["flo","fl","f"]))