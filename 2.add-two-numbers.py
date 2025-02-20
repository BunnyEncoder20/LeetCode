#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        dummy = res
        p1 = l1
        p2 = l2
        
        carry,summ = 0,0
        
        while p1 or p2 or carry:
            summ = carry
            
            if p1:
                summ += p1.val
                p1 = p1.next
            if p2:
                summ += p2.val
                p2 = p2.next
            
            carry = summ // 10

            summ = summ % 10
            dummy.next = ListNode(summ)
            dummy = dummy.next
        
        return res.next
            
        
        
# @lc code=end

