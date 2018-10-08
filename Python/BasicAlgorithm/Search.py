# Binary Search
#

def binary_search(L, key):
    l, r = 0, len(L) - 1

    while l <= r:
        median = l + (r - l) // 2
        if L[median] < key:
            l = median + 1
        elif L[median] == key:
            return median
        else:
            r = median - 1
    return -1

