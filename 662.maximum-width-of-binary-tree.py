#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            if not node:
                return 0
            lsth = getHeight(node.left)
            rsth = getHeight(node.right)
            maxWidth[0] = max(maxWidth[0], 1 + lsth + rsth)
            return 1 + max(lsth, rsth)
        maxWidth = [0]
        getHeight(root)
        return maxWidth[0]-1
        
# @lc code=end

