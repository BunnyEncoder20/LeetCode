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

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        bunny = head
        tortoise = head
        
        while bunny and bunny.next:
            tortoise = tortoise.next
            bunny = bunny.next.next
            
            if tortoise == bunny:
                return True
        
        return False
        
# @lc code=end

