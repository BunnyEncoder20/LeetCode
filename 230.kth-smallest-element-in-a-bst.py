#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def performInorder(node):
            nonlocal count, result
            if not node: return 
            performInorder(node.left)
            count+=1
            if count == k:
                result = node.val
                return
            performInorder(node.right)
        
        count,result = 0,None
        performInorder(root)
        return result
        
        
# @lc code=end

