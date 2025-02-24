#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # morris traversal TC:O(n) | SC:O(1) using threaded BT
        inorder = []
        if not root: return inorder
        temp = root
        
        while temp:
            if not temp.left:
                inorder.append(temp.val)
                temp = temp.right
            else:
                # find rightmost node in LST
                rightMostNode = temp.left
                while rightMostNode.right and rightMostNode.right != temp:
                    rightMostNode = rightMostNode.right
                
                if rightMostNode.right == None:
                    rightMostNode.right = temp
                    temp = temp.left
                else:
                    rightMostNode.right = None
                    inorder.append(temp.val)
                    temp = temp.right
        
        return inorder
                        
                
                    
                
                
        
# @lc code=end

