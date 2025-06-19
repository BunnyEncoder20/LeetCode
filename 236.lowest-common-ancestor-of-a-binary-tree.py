#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        """
        Time Complexity: O(N), where N is the number of nodes in the tree
        Space Complexity: O(H), where H is the height of the tree (for the recursion stack and path storage).
        """
        def findPath2Node(node, path, targetNode):
            # base case
            if not node:return

            # add node to path
            path.append(node)

            # if target node found
            if node == targetNode:
                return True
            
            # recursively go and search each ST
            # If target found in any one of them,
            # return True
            if (
                findPath2Node(node.left, path, targetNode) or
                findPath2Node(node.right, path, targetNode)
            ):
                return True
            
            # else target node on this path, remove node 
            # from the path and return false
            path.pop()
            return False


        # Get path to each node 
        p_path, q_path = [], []
        findPath2Node(root, p_path, p)
        findPath2Node(root, q_path, q)


        # Till nodes are equal, keep going
        ans = None
        for pNode, qNode in zip(p_path, q_path):
            if pNode == qNode:
                ans = pNode
            else:
                break
        
        return ans

        
# @lc code=end

