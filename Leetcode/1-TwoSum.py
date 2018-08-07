# 1. Two Sum
# 
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def two_sum(arr, sum):
    s = {}
    
    for i in range(len(arr)):
        remainder = sum - arr[i]
        if (remainder in s):
            return [s[remainder], i]
        else:
            s[arr[i]] = i

def main():
    print(two_sum([1, 2, 3, 4, 5], 3))
    print(two_sum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    main()
