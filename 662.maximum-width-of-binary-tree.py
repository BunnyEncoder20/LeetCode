#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        maxWidth = -math.inf
        q = deque([(root, 0)])
        while q:
            n = len(q)
            levelMin = q[0][1]
            first,last = 0,0
            for i in range(n):
                node, idx = q.popleft()
                idx -= levelMin
                if i == 0:
                    first = idx
                if i == n-1:
                    last = idx
                    
                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
            #end 
            maxWidth = max(maxWidth, last-first+1)
        # end
        return maxWidth
# @lc code=end

