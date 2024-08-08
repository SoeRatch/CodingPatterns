# Leetcode Link- https://leetcode.com/problems/palindrome-linked-list/

# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseLinkedList(self,head:Optional[ListNode]) -> bool:
        curr = head
        prev = None
        
        while curr.next:
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp

        curr.next=prev

        return curr
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return True
        
        fp=head
        sp=head
        while fp and fp.next:
            fp=fp.next.next
            sp=sp.next
        
        p2=self.reverseLinkedList(sp)
        p1 = head
        
        while p2:
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
            
        return True