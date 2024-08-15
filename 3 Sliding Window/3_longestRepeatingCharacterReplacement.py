# Leetcode Link- # https://leetcode.com/problems/longest-repeating-character-replacement/

# Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.



from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        longest_subs = 0
        max_char = 0

        freq = defaultdict(int)
        start = 0

        for end in range(n):
            # Update Frequency
            freq[s[end]]+=1

            # Count Maximum character of the sliding window 
            max_char=max(max_char,freq[s[end]])

            # Check if replacement needed .
            if (end-start+1)-max_char > k:
                # If yes , then shrink the window .
                freq[s[start]]-=1
                start+=1

            longest_subs = max(longest_subs,end-start+1) 
        
        return longest_subs
            
            
        