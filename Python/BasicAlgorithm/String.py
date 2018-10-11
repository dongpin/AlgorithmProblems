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
def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ''
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

def lcs_iterative(xstr, ystr):
    pass


