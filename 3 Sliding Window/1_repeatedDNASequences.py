# Leetcode Link- https://leetcode.com/problems/repeated-dna-sequences/description/


# Repeated DNA Sequences


# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.

# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)

        seen=set()
        repeated = set()

        
        for left in range(n-9):
            right=left+10
            subs=s[left:right]
            if subs in seen:
                repeated.add(subs)
            seen.add(subs)
        
        return list(repeated)