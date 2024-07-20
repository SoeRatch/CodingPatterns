# Leetcode link- https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# Shortest Unsorted Continuous Subarray

# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

# Example 1:
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:
# Input: nums = [1]
# Output: 0



class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        low,high=0,n-1

        while low<n-1 and nums[low]<=nums[low+1]:
            low+=1

        if low==n-1:
            return 0
        
        while high>0 and nums[high]>=nums[high-1]:
            high-=1
        

        subarray_min=nums[low]
        subarray_max=nums[low]

        for i in range(low,high+1):
            subarray_min=min(nums[i],subarray_min)
            subarray_max=max(nums[i],subarray_max)

        while low>0 and nums[low-1]>subarray_min:
            low-=1
        
        while high<n-1 and nums[high+1]<subarray_max:
            high+=1
        
        return high-low+1
        