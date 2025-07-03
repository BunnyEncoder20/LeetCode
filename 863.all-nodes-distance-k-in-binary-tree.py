#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # trivial case 
        if not root: return []

        # hashmap for storing parents of each node
        parent = {}

        # store the parents of each node
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        
        # now, we do bfs from target node
        q = deque([target])
        visited = set([target])
        ans = []
        distance = 0

        # BFS till K distance
        while q:
            # When distance == k, 
            # current queue holds all nodes at that distance
            if distance == k:
                ans.extend([node.val for node in q])
                return ans
            
            # append all nodes at current level
            # (distance) into q
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                # left child
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                
                # right child
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                
                # parent
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
                    visited.add(parent[node])
            
            # after level, increase distance
            distance += 1
        
        # incase there are not nodes at distance k
        return ans
        
# @lc code=end

