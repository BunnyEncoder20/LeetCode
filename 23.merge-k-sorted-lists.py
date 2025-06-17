#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyhead = ListNode(-1)
        temp = dummyhead
        pq = []

        if list is None: return None

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        
        while pq:
            val, i, node = heapq.heappop(pq)

            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
        
        return dummyhead.next
            
        
# @lc code=end

