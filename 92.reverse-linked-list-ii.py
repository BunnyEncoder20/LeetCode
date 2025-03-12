#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # trivial case
        if not head or left == right:
            return head
        
        # init (dummy cause we might need to reverse from head itself)
        dummy = ListNode(0)
        dummy.next = head
        beforeLeft = dummy
        left,right = left-1,right-1 # zero based indexing
        
        # beforeLeft -> node before left index
        for _ in range(left):
            beforeLeft = beforeLeft.next
        
        # init for reversing the sublist
        temp = beforeLeft.next
        sub_prev = None
        sub_next = None
        
        # reverse sublist till right
        for _ in range(right-left+1):
            sub_next = temp.next
            temp.next = sub_prev
            sub_prev = temp
            temp = sub_next
        
        # reconnect
        beforeLeft.next.next = temp
        beforeLeft.next = sub_prev
        
        return dummy.next
        
        
# @lc code=end

