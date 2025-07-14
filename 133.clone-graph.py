#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def cloneNode(node):
            # base case
            if node in mpp:
                return mpp[node]

            # copy the node into hashmap
            copyNode = Node(node.val)
            mpp[node] = copyNode

            for nn in node.neighbors:
                copyNode.neighbors.append(cloneNode(nn))

            return copyNode

        mpp = {}
        return cloneNode(node)


# @lc code=end
