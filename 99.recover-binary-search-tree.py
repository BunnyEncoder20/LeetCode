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
    def __init__(self):
        self.first = None
        self.middle = None
        self.last = None
        self.prev = TreeNode(float('-inf'))
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorderTraversal(node):
            if not node: return 
            
            # go to LST
            inorderTraversal(node.left)
            
            # process the current node
            if node.val < self.prev.val:
                # violation
                if not self.first:
                    # first violation
                    self.middle = node
                    self.first = self.prev
                else:
                    self.last = node
            # update the prev node
            self.prev = node
            
            # go to RST
            inorderTraversal(node.right)
        
        # init traversal
        inorderTraversal(root)
        
        # swap the nodes
        if self.first and self.last:
            # if 2 violations (wrong nodes are not adj)
            self.first.val, self.last.val = self.last.val,self.first.val
        elif self.first and self.middle:
            # if 1 voilation (wrong ondes are adj)
            self.first.val,self.middle.val = self.middle.val,self.first.val
        
        return 
            
        
    
        
# @lc code=end

