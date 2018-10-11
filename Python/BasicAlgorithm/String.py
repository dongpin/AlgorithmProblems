# Check if sting is palindromic
#

def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

# string sorts
def lsd_sort(s):
    pass

def msd_sort(s):
    pass

def three_way_quicksort(s):
    pass

# substring search
def kmp():
    pass

def boyer_moore():
    pass

def rabin_karp():
    pass

# regular expressions

# data compression

# Longest common subsequence
def longest_common_subsequence(xstr, ystr):
    if not xstr or not ystr:
        return ''
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + longest_common_subsequence(xs, ys)
    else:
        return max(longest_common_subsequence(xstr, ys), longest_common_subsequence(xs, ystr), key=len)

def longest_common_subsequence_iterative(xstr, ystr):
    pass

# Longest increasing subsequence
def longest_increasing_subsequence():
    pass

# Longest palindrome subsequence
def longest_palindrome_subsequence():
    pass

# Longest alternating subsequence
def longest_alternating_subsequence():
    pass

# Longest common substring
def longest_common_substring(xstr, ystr):
    lcs_res = [[0 for _ in range(len(ystr)+1)] for _ in range(len(xstr)+1)]

    result = 0
    for i in range(len(xstr)+1):
        for j in range(len(ystr)+1):
            if i == 0 or j == 0:
                lcs_res[i][j] = 0
            elif xstr[i-1] == ystr[j-1]:
                lcs_res[i][j] = lcs_res[i-1][j-1] + 1
                result = max(result, lcs_res[i][j])
            else:
                lcs_res[i][j] = 0
    return result

# Longest palindrome substring
def longest_palindrome_substring():
    pass

# Longest repeated substring
def longest_repeated_substring():
    pass

    


