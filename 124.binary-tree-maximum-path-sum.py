#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxisum = float('-inf')

        def dfs(node):
            nonlocal maxisum
            if not node:
                return 0
            
            # find sum of subtrees, ignore negatives
            lst_sum = max(0, dfs(node.left))
            rst_sum = max(0, dfs(node.right))

            # update maximum path sum
            maxisum = max(maxisum, node.val + lst_sum + rst_sum)

            # return max path sum including current node and one subtree
            return node.val + max(lst_sum, rst_sum)
        
        dfs(root)
        return maxisum
        
# @lc code=end
