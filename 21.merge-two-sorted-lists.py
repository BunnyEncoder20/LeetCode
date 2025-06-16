#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        p1, p2, temp = list1, list2, dummyHead
        
        while p1 and p2:
            if p1.val <= p2.val:
                temp.next = p1
                p1 = p1.next
                temp = temp.next
            else:
                temp.next = p2
                p2 = p2.next
                temp = temp.next
        
        while p1:
            temp.next = p1
            p1 = p1.next
            temp = temp.next

        while p2:
            temp.next = p2
            p2 = p2.next
            temp = temp.next

        return dummyHead.next

                
# @lc code=end

