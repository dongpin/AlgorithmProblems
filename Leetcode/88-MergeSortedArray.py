# 88. Merge Sorted Array
#

def merge_sorted_array(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
        
    i, j, t = m - 1, n - 1, m + n -1
    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            nums1[t] = nums2[j]
            j -= 1
        else:
            nums1[t] = nums1[i]
            i -= 1    
        t -= 1
        
    while i >= 0:
        nums1[t] = nums1[i]
        i -= 1
        t -= 1
        
    while j >= 0:
        nums1[t] = nums2[j]
        j -= 1
        t -= 1

def main():
    nums1 = [1,3,5,10,0,0,0,0]
    merge_sorted_array(nums1, 4, [2,3,6,8], 4)
    print(nums1)

if __name__ == '__main__':
    main()