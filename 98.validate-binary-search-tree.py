#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, mini, maxi):
            if not node:
                return True
            if not (mini < node.val < maxi):
                return False
            leftValid = validate(node.left, mini, node.val)
            rightValid = validate(node.right, node.val, maxi)
            
            return leftValid and rightValid
        
        return validate(root, float('-inf'), float('inf'))
        
# @lc code=end

