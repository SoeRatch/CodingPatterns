# Leetcode link- https://leetcode.com/problems/backspace-string-compare/

# Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".




# class Solution:
#     def getValidStr(self,s):
#         stack=[]
#         for i in range(len(s)):
#             if s[i]=='#' and stack:
#                 stack.pop()
#             elif s[i]!='#':
#                 stack.append(s[i])
#         return ''.join(stack)
    
#     def backspaceCompare(self, s: str, t: str) -> bool: 
#         sv=self.getValidStr(s)
#         st=self.getValidStr(t)

#         return sv==st
    

class Solution:
    def get_next_valid_index(self,st,index):
        backspace_count = 0
        
        while index >= 0:
            if st[index] == '#':            # found a backspace character
                backspace_count += 1
            elif backspace_count > 0:       # a non backspace character
                backspace_count -= 1
            else:
                break
            index -= 1
            
        return index
    
    
    def backspaceCompare(self, s: str, t: str) -> bool: 
        s1 = len(s)-1
        t1 = len(t)-1

        while s1>=0 or t1>=0:
            s1 = self.get_next_valid_index(s,s1)
            t1 = self.get_next_valid_index(t,t1)

            if s1 <0 and t1 <0:
                return True
            elif s1 <0 or t1 <0:
                return False
            elif s[s1] != t[t1]:
                return False
                
            s1 -=1
            t1 -=1

        return True
            
            
