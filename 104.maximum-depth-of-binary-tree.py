#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            if not node:
                return 0
            lh = getHeight(node.left)
            rh = getHeight(node.right)
            return 1 + max(lh, rh)
        
        return getHeight(root)
        
# @lc code=end

