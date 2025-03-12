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
        # morris traversal approach
        temp = root
        while temp:
            if temp.left != None:
                    prev = temp.left
                    while prev.right:
                        prev = prev.right
                    
                    prev.right = temp.right
                    temp.right = temp.left
                    temp.left = None
            
            # update the temp
            temp = temp.right
        
# @lc code=end

