#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        
        def flatten(node):
            nonlocal prev
            if not node:
                return 
            flatten(node.right)
            flatten(node.left)
            node.right = prev
            node.left = None
            prev = node
        
        flatten(root)
        return root
        
# @lc code=end

