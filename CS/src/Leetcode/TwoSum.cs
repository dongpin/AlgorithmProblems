// 1. Two Sum

using System;
using System.Collections;
using System.Collections.Generic;

namespace Leetcode
{
    public partial class Algorithm
    {
        public static int[] TwoSum(int[] nums, int target)
        {
            Dictionary<int, int> numsDict = new Dictionary<int, int>();
            for (var i = 0; i < nums.Length; i++)
            {
                if (numsDict.ContainsKey(target - nums[i]))
                {
                    return new int[] { numsDict[target - nums[i]], i };
                }
                else
                {
                    if (!numsDict.ContainsKey(nums[i]))
                    {
                        numsDict.Add(nums[i], i);
                    }
                }
            }

            return null;
        }
    }
}