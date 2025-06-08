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
        len1, len2 = self.getlen(l1), self.getlen(l2)

        # pad if the lengths are unequal
        if len1 > len2: l2 = self.getpad(l2, len1-len2)
        elif len2 > len1: l1 = self.getpad(l1, len2-len1)
        
        # recursively add from lsb
        result = ListNode(-1)
        carry, result = self.getSum(l1, l2)
        if carry:
            newhead = ListNode(carry, result)
            result = newhead
        return result
    
    def getlen(self, temp):
        length = 0
        if not temp: return length
        
        while temp:
            length += 1
            temp = temp.next
        
        return length
             
    def getpad(self, ll, n):
        for _ in range(n):
            padnode = ListNode(0, ll)
            ll = padnode
        return ll
    
    def getSum(self, l1, l2):
        if not l1 and not l2:
            return (0, None)
        
        carry, prevhead = self.getSum(l1.next, l2.next)
        
        total = l1.val + l2.val + carry
        carry, total = divmod(total, 10)
        newhead = ListNode(total, prevhead)
        
        return (carry, newhead)
        
# @lc code=end

