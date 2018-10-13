# Linear Search
#

def linear_search(arr, key):
    for i, v in enumerate(arr):
        if v == key:
            return i
    return -1

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

# Ternary Search
#

def _ternary(arr, key, l, r):
    if (l <= r):
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            return _ternary(arr, key, l, mid1-1)
        elif key > arr[mid2]:
            return _ternary(arr, key, mid2+1, r)
        else:
            return _ternary(arr, key, mid1+1, mid2-1)
    return -1

def ternary_search(arr, key):
    return _ternary(arr, key, 0, len(arr)-1)
