# Leetcode Link- https://leetcode.com/problems/circular-array-loop/

# Circular Array Loop

# You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:
# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

# A cycle in the array consists of a sequence of indices seq of length k where:

# Following the movement rules above results in the repeating index sequence 
# seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.

# Example 1:
# Input: nums = [2,-1,1,2,2]
# Output: true
# Explanation:
# There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
# The cycle's length is 3.

# Example 2:
# Input: nums = [-1,2]
# Output: false
# Explanation:
# The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1.
# By definition the sequence's length must be strictly greater than 1 to be a cycle.


# Constraints:
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
# nums[i] != 0

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        visited_index=set()



        def getNextIndex(index,curr_dir):

            next_index = (index+nums[index])%n

            next_dir = 1 if nums[next_index]>0 else -1

            if curr_dir!=next_dir or index==next_index:
                return -1 

            return next_index




        for i in range(n):
            if i in visited_index:
                continue
                
            sp,fp=i,i
            curr_dir = 1 if nums[i]>0 else -1

            while True:
                visited_index.add(sp)
                visited_index.add(fp)

                sp=getNextIndex(sp,curr_dir)
                fp=getNextIndex(fp,curr_dir)

                if sp == -1 or fp== -1:
                    break
                
                fp=getNextIndex(fp,curr_dir)

                if fp == -1:
                    break
                
                if sp==fp:
                    return True

        return False
        