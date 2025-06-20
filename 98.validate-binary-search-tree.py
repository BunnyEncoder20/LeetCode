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
            # base case 
            if node is None:
                # reached end of subtree without violation 
                return True  
            
            if not (mini < node.val < maxi):
                # node val not following BST rule   s
                return False
            
            # validate both left and right sub trees
            leftValid = validate(node.left, mini, node.val)
            rightValid = validate(node.right, node.val, maxi)

            # both should be True for sub tree to be valid itself
            return leftValid and rightValid

        # start recursive validate sub trees
        return validate(root, float('-inf'), float('inf'))
# @lc code=end

