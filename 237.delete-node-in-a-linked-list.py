#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # edge case: node is tail node
        if not node or not node.next:
            return

        node.val = node.next.val
        node.next = node.next.next
        return 
        
        
        
        
        
                
        
# @lc code=end

