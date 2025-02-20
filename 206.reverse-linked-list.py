#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # trivial case 
        if not head: return head
        
        p = None
        t = head
        n = head.next
        
        while t:
            n = t.next
            t.next = p
            p = t
            t = n
        
        return p
            
        
        
# @lc code=end

