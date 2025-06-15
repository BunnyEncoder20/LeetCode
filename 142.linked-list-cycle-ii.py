#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        slow, fast  = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # cycle detected
                break

        if slow != fast: return None

        slow = head
        if slow == fast: return head

        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        
        
        
        
# @lc code=end

