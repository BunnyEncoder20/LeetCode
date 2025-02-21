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
        len1, len2 = self.getLength(l1), self.getLength(l2)
        if len1 < len2:
            l1 = self.addPadding(l1, len2-len1)
        elif len1 > len2:
            l2 = self.addPadding(l2, len1-len2)
        
        carry, result = self.addLists(l1,l2)
        if carry:
            new = ListNode(carry)
            new.next = result
            result = new
        
        return result
    
    def getLength(self, temp):
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def addPadding(self, head, padding):
        for _ in range(padding):
            new = ListNode(0)
            new.next = head
            head = new
        return head
        
    def addLists(self, l1, l2):
        if not l1 and not l2:
            return (0, None)

        carry, nextNode = self.addLists(l1.next, l2.next)
        
        total = l1.val + l2.val + carry
        carry,total = divmod(total, 10)
        newNode = ListNode(total)
        newNode.next = nextNode
        return (carry, newNode)
            
             
        
            
        
        
# @lc code=end

