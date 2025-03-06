#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def initTraversal(node):
            '''initial traversal to get all node values'''
            if not node: return 
            initTraversal(node.left)
            inorder.append(node.val)
            initTraversal(node.right)
        
        # construct the inorder arr
        inorder = []
        initTraversal(root)
        inorder.sort()      # correct inorder

        def inOrderTraversal(node):
            '''cross check the inorder with correct inorder'''
            nonlocal i      # so that i is upadted across all recursive calls
            if not node: return 
            inOrderTraversal(node.left)
            if node.val != inorder[i]:
                node.val = inorder[i]
            i += 1
            inOrderTraversal(node.right)

        i = 0
        inOrderTraversal(root)
        
# @lc code=end

