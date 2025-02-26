#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if node == None or node == p or node == q:
            return node

        lsb = self.lowestCommonAncestor(node.left, p, q)
        rsb = self.lowestCommonAncestor(node.right, p, q)
        
        if lsb == None:
            return rsb
        elif rsb == None:
            return lsb
        elif lsb and rsb:
            return node
        else:
            return None
        
        
# @lc code=end

