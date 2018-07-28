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

def main():
    print(binary_search([1,2,4,6,7,8], 6))
    print(binary_search([1,2,4,6,7,8,11,23,45,67,89,102,345], 89))
    print(binary_search([1,2,4,6,7,8], 9))

if __name__ == '__main__':
    main()
