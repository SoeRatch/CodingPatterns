# Leetcode link- https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev=None
        low = head
        high = head

        while n>0:
            high=high.next
            n-=1
        
        while high is not None:
            prev=low
            low=low.next
            high=high.next

        if prev is None:
            return head.next 
        
        prev.next=low.next

        return head
        