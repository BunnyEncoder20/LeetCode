#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recursiveRight(node,level):
            if node:
                if level == len(res):
                    res.append(node.val)
                recursiveRight(node.right,level+1)
                recursiveRight(node.left, level+1)
        res = []
        recursiveRight(root, 0)
        return res
        
# @lc code=end

