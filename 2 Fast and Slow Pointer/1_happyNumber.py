# Leetcode Link- https://leetcode.com/problems/happy-number/

# Happy Number

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# Output: false

# Constraints:
# 1 <= n <= 231 - 1

class Solution:

    def findSquare(self,num):
        sum1=0
        num_str=str(num)
        for digit in num_str:
            sum1+=int(digit)**2
        return sum1

    def isHappy(self, n: int) -> bool:
        # 1 Fast and slow pointer approach
        # sp,fp=n,n

        # while fp!=1 or sp!=1:
        #     sp=self.findSquare(sp)
        #     fp=self.findSquare(self.findSquare(fp))

        #     if sp==1 or fp==1:
        #         return True
        #     elif sp==fp:
        #         return False
        
        # return True

        # 2 Set based approach
        seen_set=set()

        while n!=1 and n not in seen_set:
            seen_set.add(n)
            n=self.findSquare(n)
        
        return n==1

        
        