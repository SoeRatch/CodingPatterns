# Leetcode Link- https://leetcode.com/problems/sliding-window-maximum/

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7




from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n= len(nums)
        l,r=0,0
        result=[]
        dq=deque()

        while r<n:
            while dq and nums[r]>=nums[dq[-1]]:
                dq.pop()
            
            dq.append(r)

            if dq[0]<l:
                dq.popleft()
            
            if r+1>=k:
                result.append(nums[dq[0]])
                l+=1
            r+=1

        return result

        
        

        