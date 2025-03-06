#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.front = []
        self.back = []
        
        # input nodes into the front stack
        temp = root
        while temp:
            self.front.append(temp)
            temp = temp.left
        
        # input nodes into the back stack
        temp = root
        while temp:
            self.back.append(temp)
            temp = temp.right
    
    def next(self):
        node = self.front.pop()
        temp = node.right
        while temp:
            self.front.append(temp)
            temp = temp.left
        return node.val
                
    def before(self):
        node = self.back.pop()
        temp = node.left
        while temp:
            self.back.append(temp)
            temp = temp.right
        return node.val

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        it = BSTIterator(root)
        
        i,j = it.next(), it.before()
        while i < j:
            add = i+j
            if add == k:
                return True
            elif add < k:
                i = it.next()
            else:
                j = it.before()
        return False
            

        
# @lc code=end

