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
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedHead = ListNode(-1)
        minheap = []
        temp = mergedHead
        
        for head in lists:
            if head:
                heapq.heappush(minheap, (head.val, id(head), head))
        
        while minheap:
            val,_,node = heapq.heappop(minheap)
            if node.next:
                heapq.heappush(minheap, (node.next.val, id(node.next), node.next))
            temp.next = node
            temp = temp.next
        
        return mergedHead.next
            
        
# @lc code=end

