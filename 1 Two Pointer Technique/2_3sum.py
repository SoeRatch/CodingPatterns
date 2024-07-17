# Leetcode link- https://leetcode.com/problems/3sum/

# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []


class Solution:

    def twoSum(self,nums,target,low,high):
        triplets=[]
        while low<high:
            if nums[low]+nums[high]==target:
                triplets.append([0-target,nums[low],nums[high]])
                low+=1
                high-=1
                while low<high and nums[low]==nums[low-1] :
                    low+=1
                while low<high and nums[high]==nums[high+1]:
                    high-=1
            elif nums[low]+nums[high]<target:
                low+=1
            else:
                high-=1
            
        return triplets


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        result=[]
        for i in range(n-2):
            if i==0 or nums[i]!=nums[i-1]:
                target = 0-nums[i]
                triplets=self.twoSum(nums,target,i+1,n-1)
                if len(triplets)>0:
                    result=result+triplets
            
        return result 
                
            
        
        