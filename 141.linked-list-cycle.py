#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast  = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # cycle detected
                return True
        
        return False
        
# @lc code=end

