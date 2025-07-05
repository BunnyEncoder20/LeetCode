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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(node, target, path):
            if not node:
                return False
            
            path.append(node)
            if node == target: 
                return True
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
            
            # both lsb and rst return false
            # backtrack
            path.pop()
            return False
        
        path1 = []
        path2 = []
        findPath(root, p, path1)
        findPath(root, q, path2)
        
        lca = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                lca = path1[i]
            else:
                break
        return lca
            
# @lc code=end

