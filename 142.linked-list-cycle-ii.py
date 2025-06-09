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

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # possible cycle
            if slow == fast:
                break
        
        # Runs only when we encounter break (while-else), 
        # basically no cycle
        else: return None

        # find node from where loop starts
        slow = head
        
        # when they collide again, it'll be at node
        # where the loop starts
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
# @lc code=end

