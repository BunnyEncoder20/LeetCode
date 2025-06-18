#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        if root == None: return ""

        q = deque([root])
        while q:
            node = q.popleft()
            if node != None:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                data.append('#')

        return ",".join(data)

    def deserialize(self, raw_data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not raw_data: return None

        data = deque()
        for val in raw_data.split(","):
            if val == '#':
                data.append(None)
            else:
                data.append(int(val))
        
        root = TreeNode(data.popleft())
        q = deque([root])
        while q:
            node = q.popleft()
            left_val = data.popleft()
            right_val = data.popleft()

            if left_val != None:
                node.left = TreeNode(left_val)
                q.append(node.left)
            if right_val != None:
                node.right = TreeNode(right_val)
                q.append(node.right)
        
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

