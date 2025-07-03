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

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # trivial case
        if not node: return 
        
        # helper func
        def clone_dfs(node):
            '''
            returns the copy node of the node sent.
            '''

            # if node visited
            if node in mpp:
                return mpp[node]

            # make a copy of curr node
            copyNode = Node(node.val)
            mpp[node] = copyNode

            # dfs for neighbouring nodes
            # and append the copy of neighbours 
            # into the copy node's neighbours
            for nn in node.neighbors:
                copyNode.neighbors.append(clone_dfs(nn))
            
            return copyNode
            
            
        # hashmap to map old nodes to new nodes
        mpp = {}
        return clone_dfs(node)
        
# @lc code=end

