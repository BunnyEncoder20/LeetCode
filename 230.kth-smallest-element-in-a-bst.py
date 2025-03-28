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
        def inOrder(node):
            nonlocal k, res
            if not node or k == 0: return 
            inOrder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            inOrder(node.right)
        
        res = None
        inOrder(root)
        return res
        
        
# @lc code=end

