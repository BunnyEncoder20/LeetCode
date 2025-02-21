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
        mergeHead = ListNode(-1)
        l1,l2,temp = list1,list2,mergeHead
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next    
            else:
                temp.next = l2
                l2 = l2.next 
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
            
        return mergeHead.next
# @lc code=end

