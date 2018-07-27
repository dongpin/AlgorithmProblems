# 11. Container with most water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

# Approach 1: brute-force
def maxArea1(height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        for i in range(len(height)):
            for j in range(i +1 , len(height)):
                d = j - i
                h = min(height[i], height[j])
                maxWater = max(maxWater, d*h)
        return maxWater

# Approach 2: 
def maxArea2(height):
    l, r, maxWater = 0, len(height) - 1, 0
    while (l < r):
        maxWater = max(maxWater, min(height[l], height[r]) * (r - l))
        if (height[l] < height[r]):
            l += 1
        else:
            r -= 1
    return maxWater                  

def main():
    print(maxArea1([1,8,6,2,5,4,8,3,7]))
    print(maxArea2([1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    main()