#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if root is None or root == p or root == q:
            return root

        LST_search = self.lowestCommonAncestor(root.left, p, q)
        RST_search = self.lowestCommonAncestor(root.right, p, q)

        if LST_search is None:
            return RST_search
        elif RST_search is None:
            return LST_search
        else:
            return root

        
# @lc code=end

