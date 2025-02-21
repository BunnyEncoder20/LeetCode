#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total, carry = 0, 0
        result = None 
        
        # make stacks
        p1,p2 = l1,l2
        stk1, stk2 = [],[]
        while p1:
            stk1.append(p1)
            p1 = p1.next
        while p2:
            stk2.append(p2)
            p2 = p2.next
        
        while stk1 or stk2 or carry:
            total = carry
            if stk1:
                total += stk1.pop().val
            if stk2:
                total += stk2.pop().val
            
            carry, total = divmod(total, 10)
            
            new = ListNode(total)
            new.next = result
            result = new
            
        return result
             
        
            
        
        
# @lc code=end

