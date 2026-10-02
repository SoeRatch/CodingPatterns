# Leetcode Link: https://leetcode.com/problems/merge-intervals/

# Leetcode 56: Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Python

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        result = []

        # 1 Sort intervals by start value
        intervals.sort(key = lambda item:item[0])

        group_start, group_end = intervals[0][0], intervals[0][1]

        # 2 Scan the intervals and merge
        for i in range(1,n):
            start, end = intervals[i]

            # Check if there is an overlap 
            if start <= group_end:
                # Merge
                group_end = end if end > group_end else group_end
            else:
                # If no overlap then update
                result.append([group_start,group_end])
                group_start, group_end = start, end

        result.append([group_start,group_end])

        return result
