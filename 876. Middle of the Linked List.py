# Easy — Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next
        
# O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        return s
