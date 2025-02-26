#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        left2right = True
        q = deque([root])
        while q:
            n = len(q)
            lvl = []
            for i in range(n):
                node = q.popleft()
                lvl.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            #end
            ans.append(lvl) if left2right else ans.append(lvl[::-1])
            left2right = not left2right
        #end
        return ans
        
# @lc code=end

