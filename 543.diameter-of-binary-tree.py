#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDiameter = -math.inf
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeights(node):
            if not node:
                return 0
            
            lh = getHeights(node.left)
            rh = getHeights(node.right)
            
            # calc the diameter from this node
            self.maxDiameter = max(self.maxDiameter, lh+rh)
            
            return 1 + max(lh, rh)
        
        getHeights(root)
        return self.maxDiameter

        
# @lc code=end

