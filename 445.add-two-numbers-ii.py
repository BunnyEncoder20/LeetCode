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
        result = ListNode(-1)
        
        l1, l2, l3 = self.reverseLL(l1), self.reverseLL(l2), result

        while l1 or l2 or carry:
            total = carry
            
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total // 10
            total %= 10
            l3.next = ListNode(total)
            l3 = l3.next
        
        return self.reverseLL(result.next)
    
    def reverseLL(self, temp):
        back = None
        while temp:
            front = temp.next
            temp.next = back
            back = temp
            temp = front
        return back
            
        
        
# @lc code=end

