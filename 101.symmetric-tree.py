#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(leftNode, rightNode):
            # both ended 
            if not leftNode and not rightNode:
                return True
            
            # missing one node
            if (
                not leftNode or 
                not rightNode
            ): return False

            # Both nodes, but data not same
            if leftNode.val != rightNode.val:
                return False
            
            # Move to next nodes in mirrored fashion
            # either both outward or both inward
            return (
                isMirror(leftNode.left, rightNode.right) and 
                isMirror(leftNode.right, rightNode.left)
            )

        # start travesal
        return isMirror(root.left, root.right)
        
# @lc code=end

