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
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, mini, maxi):
            # base case 
            if node is None:
                return True
            if not (mini<node.val<maxi):
                return False
            
            isLeftValid = validate(node.left, mini, node.val)
            isRightValid = validate(node.right, ndoe.val, maxi)

            return isLeftValid and isRightValid
        
        return validate(root, flaot('-inf'), float('inf'))
# @lc code=end

