# Leetcode Link- https://leetcode.com/problems/minimum-window-substring/

# Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        min_len = n+1
        min_l = 0

        pattern_freq = defaultdict(int)
        for ch in t:
            pattern_freq[ch]+=1
        
        l,r = 0,0
        required = len(pattern_freq)
        matched = 0

        for r in range(n):
            # 1.  Update frequency
            pattern_freq[s[r]] -=1
            

            # 2. If frequency matches , update match
            if pattern_freq[s[r]] == 0:
                matched+=1
            
            # 3. When a valid window is found ,
            # shrink the window to find a smaller window
            while matched == required:
                # a) update min substring
                if (r-l+1)<min_len:
                    min_len=r-l+1
                    min_l = l
            
                # b) update freq and match
                if pattern_freq[s[l]]==0:
                    matched-=1
                pattern_freq[s[l]]+=1

                # c) shrink the window till the string is valid
                l+=1

        if min_len != n+1:
            return s[min_l:min_l+min_len]
        return ""
        