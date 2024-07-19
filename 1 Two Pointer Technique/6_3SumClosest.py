# Leetcode link- https://leetcode.com/problems/3sum-closest/

# 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
 

import math

class Solution: 

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        closest_sum=math.inf

        nums.sort()

        for i in range(n-2):
            low,high=i+1,n-1
            while low<high:
                curr_sum=nums[i]+nums[low]+nums[high]

                if abs(target-curr_sum)<abs(target-closest_sum):
                    closest_sum=curr_sum

                if curr_sum==target:
                    return closest_sum
                elif curr_sum<target:
                    low+=1
                else:
                    high-=1
                    
        return closest_sum
