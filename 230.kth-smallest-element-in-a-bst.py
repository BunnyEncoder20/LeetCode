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
        class Results:
            def __init__(self):
                self.count = 0
                self.result = None
                
        def inOrder(node):
            if not node or res.result != None: 
                return 

            inOrder(node.left)
            res.count+=1
            if res.count == k:
                res.result = node.val
                return
            inOrder(node.right)
        
        res = Results()
        inOrder(root)
        return res.result
        
        
# @lc code=end

